-- =============================================================================
-- MIGRACIÓN v2: url_language_status + vw_url_completeness
-- BookingScraper Pro - Control de Completitud por Idioma
-- =============================================================================
--
-- PROPÓSITO:
--   Añade tracking granular de estado por idioma para cada URL en procesamiento.
--   Esto permite control de reintentos independiente por idioma y verificación
--   de completitud respecto a LANGUAGES_ENABLED.
--
-- IMPACTO EN ESCALABILIDAD:
--   Cardinalidad: N_urls × N_idiomas.
--   Con LANGUAGES_ENABLED=5 y 100K URLs → 500K filas.
--   Los índices están diseñados para los patrones de acceso más frecuentes:
--     - JOIN con url_queue por url_id (más frecuente)
--     - Filtrado por status (para dashboards y monitoreo)
--     - Búsqueda de filas 'failed' (para alertas)
--
-- SEGURIDAD:
--   FK con ON DELETE CASCADE: si se elimina una URL de url_queue, sus
--   registros de language_status se eliminan automáticamente.
--   DEFERRABLE INITIALLY DEFERRED: permite DELETE + INSERT en la misma
--   transacción sin violar la FK momentáneamente (útil en rollbacks).
--
-- IDEMPOTENCIA:
--   Todos los CREATE usan IF NOT EXISTS / OR REPLACE → seguro re-ejecutar.
--
-- AUTOR: Arquitecto de Software Empresarial
-- FECHA: 2026-02-28
-- VERSION: 2.0.0
-- =============================================================================

BEGIN;

-- ─────────────────────────────────────────────────────────────────────────────
-- 1. TABLA: url_language_status
-- ─────────────────────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS url_language_status (
    -- Clave primaria: serial autoincremental
    id              SERIAL          PRIMARY KEY,

    -- Referencia a la URL en procesamiento
    -- ON DELETE CASCADE: eliminar URL → eliminar todos sus language_status
    -- DEFERRABLE: permite operaciones transaccionales complejas sin violar FK
    url_id          INTEGER         NOT NULL
                    REFERENCES url_queue(id)
                    ON DELETE CASCADE
                    DEFERRABLE INITIALLY DEFERRED,

    -- Código de idioma (e.g., 'en', 'es', 'de', 'fr', 'it')
    -- VARCHAR(10) cubre locales completos como 'en-gb', 'zh-tw'
    language        VARCHAR(10)     NOT NULL,

    -- Estado del procesamiento del idioma
    -- Dominio cerrado: cualquier valor fuera del CHECK es rechazado por PostgreSQL
    status          VARCHAR(30)     NOT NULL    DEFAULT 'pending',

    -- Control de reintentos por idioma
    -- retry_count: cuántas veces ha fallado este idioma
    -- max_retries: límite configurado (por requerimiento = 1: "máximo una vez más")
    retry_count     INTEGER         NOT NULL    DEFAULT 0,
    max_retries     INTEGER         NOT NULL    DEFAULT 1,

    -- Último error registrado (truncado a 500 chars en aplicación)
    last_error      TEXT,

    -- Timestamp de cuando el idioma fue scrapeado exitosamente
    scraped_at      TIMESTAMPTZ,

    -- Timestamps de auditoría
    created_at      TIMESTAMPTZ     NOT NULL    DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL    DEFAULT NOW(),

    -- ─── CONSTRAINTS ──────────────────────────────────────────────────────

    -- Unicidad: un solo registro por (url_id, language)
    -- Garantiza que ON CONFLICT DO NOTHING / DO UPDATE funcionen correctamente
    CONSTRAINT uq_url_language_status
        UNIQUE (url_id, language),

    -- Dominio de status: cualquier otro valor es rechazado a nivel de BD
    -- (no depende de validación a nivel aplicación)
    CONSTRAINT chk_url_lang_status_domain
        CHECK (status IN (
            'pending',          -- no procesado aún
            'scraping',         -- en proceso actualmente
            'completed',        -- scrapeado y guardado exitosamente
            'failed',           -- falló tras agotar max_retries
            'skipped_existing'  -- dato ya existía en BD (ON CONFLICT DO NOTHING)
        )),

    -- Integridad: retry_count y max_retries deben ser no negativos
    CONSTRAINT chk_retry_count_non_negative
        CHECK (retry_count >= 0),

    CONSTRAINT chk_max_retries_non_negative
        CHECK (max_retries >= 0)
);

-- ─────────────────────────────────────────────────────────────────────────────
-- 2. ÍNDICES ESTRATÉGICOS
-- ─────────────────────────────────────────────────────────────────────────────

-- Índice principal: búsquedas por url_id (JOIN más frecuente con url_queue)
-- Tipo: B-Tree (óptimo para equality y range queries en columna entera)
-- Selectividad: alta si pocos idiomas por URL (típicamente 5)
CREATE INDEX IF NOT EXISTS ix_uls_url_id
    ON url_language_status (url_id);

-- Índice compuesto para verificación de completitud:
-- SELECT language, status FROM url_language_status WHERE url_id = :id
-- Plan esperado: Index Scan on ix_uls_url_id_status (covering index → no heap fetch)
CREATE INDEX IF NOT EXISTS ix_uls_url_id_status
    ON url_language_status (url_id, status);

-- Índice parcial para alertas y monitoreo de fallos:
-- SELECT * FROM url_language_status WHERE status = 'failed' ORDER BY updated_at DESC
-- Parcial: solo indexa las filas 'failed' → tamaño mínimo, selectividad máxima
CREATE INDEX IF NOT EXISTS ix_uls_failed_updated
    ON url_language_status (updated_at DESC)
    WHERE status = 'failed';

-- Índice para encontrar idiomas pendientes de reintento:
-- SELECT url_id, language FROM url_language_status
-- WHERE status = 'pending' AND retry_count > 0
CREATE INDEX IF NOT EXISTS ix_uls_pending_retry
    ON url_language_status (url_id, language)
    WHERE status = 'pending' AND retry_count > 0;

-- ─────────────────────────────────────────────────────────────────────────────
-- 3. TRIGGER: updated_at automático
-- ─────────────────────────────────────────────────────────────────────────────
-- Garantiza que updated_at siempre refleja la última modificación,
-- independientemente de si la aplicación lo actualiza explícitamente.

CREATE OR REPLACE FUNCTION fn_update_timestamp()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;

-- Trigger solo si no existe ya (idempotente)
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
        WHERE tgname = 'trg_uls_updated_at'
          AND tgrelid = 'url_language_status'::regclass
    ) THEN
        CREATE TRIGGER trg_uls_updated_at
            BEFORE UPDATE ON url_language_status
            FOR EACH ROW
            EXECUTE FUNCTION fn_update_timestamp();
    END IF;
END;
$$;

-- ─────────────────────────────────────────────────────────────────────────────
-- 4. VISTA: vw_url_completeness
-- ─────────────────────────────────────────────────────────────────────────────
-- Vista materializable para monitoreo rápido de completitud.
-- Evita JOINs manuales desde la aplicación y el dashboard.
--
-- Plan de ejecución esperado:
--   HashAggregate on url_language_status + Index Scan on url_queue
--   No riesgo de seq scan si se filtra por url_queue.id o uls.url_id

CREATE OR REPLACE VIEW vw_url_completeness AS
SELECT
    q.id                                                                AS url_id,
    q.url,
    q.status                                                            AS queue_status,
    q.priority,
    COUNT(uls.language)                                                 AS langs_tracked,
    COUNT(uls.language) FILTER (
        WHERE uls.status IN ('completed', 'skipped_existing')
    )                                                                   AS langs_ok,
    COUNT(uls.language) FILTER (WHERE uls.status = 'failed')           AS langs_failed,
    COUNT(uls.language) FILTER (WHERE uls.status = 'pending')          AS langs_pending,
    ARRAY_AGG(uls.language ORDER BY uls.language) FILTER (
        WHERE uls.status = 'failed'
    )                                                                   AS failed_languages,
    ARRAY_AGG(uls.language ORDER BY uls.language) FILTER (
        WHERE uls.status IN ('completed', 'skipped_existing')
    )                                                                   AS ok_languages,
    q.created_at,
    q.scraped_at,
    -- Bandera de completitud: True si todos los idiomas rastreados están OK
    -- y no hay ninguno fallido ni pendiente
    CASE
        WHEN COUNT(uls.language) > 0
         AND COUNT(uls.language) FILTER (WHERE uls.status = 'failed')  = 0
         AND COUNT(uls.language) FILTER (WHERE uls.status = 'pending') = 0
         AND COUNT(uls.language) FILTER (
                WHERE uls.status IN ('completed', 'skipped_existing')
             ) = COUNT(uls.language)
        THEN TRUE
        ELSE FALSE
    END                                                                 AS is_complete
FROM      url_queue              q
LEFT JOIN url_language_status    uls ON uls.url_id = q.id
GROUP BY  q.id, q.url, q.status, q.priority, q.created_at, q.scraped_at;

COMMENT ON VIEW vw_url_completeness IS
    'Vista de completitud de scraping por URL. '
    'Muestra el resumen de estados de idioma por cada URL en la cola. '
    'Consultar con WHERE url_id = :id para una URL específica, '
    'o WHERE langs_failed > 0 para todas las URLs incompletas.';

-- ─────────────────────────────────────────────────────────────────────────────
-- 5. SOPORTE PARA ESTADO 'incomplete' EN url_queue
-- ─────────────────────────────────────────────────────────────────────────────
-- url_queue.status actualmente no tiene CHECK constraint explícito (verificado en
-- models.py → Column(String(50), default="pending")).
-- Añadimos un CHECK si no existe, con dominio extendido que incluye 'incomplete'.
--
-- ANÁLISIS DE RIESGO: Si hay filas con status = 'incomplete' ya (poco probable),
-- este CHECK no las afectará (ALTER TABLE ADD CONSTRAINT valida filas existentes).
-- Si hubiera una constraint previa, la reemplazamos.

DO $$
BEGIN
    -- Verificar si ya existe la constraint
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_url_queue_status'
          AND conrelid = 'url_queue'::regclass
    ) THEN
        ALTER TABLE url_queue
        ADD CONSTRAINT chk_url_queue_status
        CHECK (status IN (
            'pending',      -- esperando ser procesada
            'processing',   -- siendo procesada actualmente
            'completed',    -- todos los idiomas procesados exitosamente
            'failed',       -- falló después de agotar max_retries de la URL
            'incomplete'    -- NUEVO: procesada pero algún idioma falló
        ));
    END IF;
END;
$$;

-- ─────────────────────────────────────────────────────────────────────────────
-- 6. COMENTARIOS DE DOCUMENTACIÓN
-- ─────────────────────────────────────────────────────────────────────────────

COMMENT ON TABLE url_language_status IS
    'Tracking granular de estado por idioma para cada URL en procesamiento. '
    'Permite control de reintentos por idioma independiente del retry de la URL. '
    'Poblada por completeness_service.py durante el scraping. '
    'Limpiada por rollback_url() cuando el usuario ejecuta un rollback.';

COMMENT ON COLUMN url_language_status.status IS
    'pending: no procesado | '
    'scraping: en proceso actualmente | '
    'completed: scrapeado y guardado OK | '
    'failed: falló tras agotar max_retries | '
    'skipped_existing: dato ya existía en BD (preservado por ON CONFLICT DO NOTHING)';

COMMENT ON COLUMN url_language_status.max_retries IS
    'Máx reintentos permitidos por idioma. '
    'Por requerimiento del sistema: 1 (una sola oportunidad de reintento). '
    'Configurable por idioma si se requiere en el futuro.';

COMMENT ON COLUMN url_language_status.retry_count IS
    'Número de intentos fallidos registrados. '
    'Cuando retry_count > max_retries, el idioma es marcado como "failed". '
    'retry_count=0 = ningún fallo aún. '
    'retry_count=1 = falló una vez (dentro del límite si max_retries=1). '
    'retry_count=2 = falló dos veces (supera max_retries=1 → failed).';

COMMIT;

-- =============================================================================
-- VERIFICACIÓN POST-MIGRACIÓN
-- =============================================================================
-- Ejecutar después del COMMIT para confirmar que la migración fue exitosa:
--
-- SELECT
--     table_name,
--     column_name,
--     data_type
-- FROM information_schema.columns
-- WHERE table_name = 'url_language_status'
-- ORDER BY ordinal_position;
--
-- SELECT conname, contype FROM pg_constraint
-- WHERE conrelid = 'url_language_status'::regclass;
--
-- SELECT indexname, indexdef FROM pg_indexes
-- WHERE tablename = 'url_language_status';
--
-- SELECT viewname FROM pg_views WHERE viewname = 'vw_url_completeness';
-- =============================================================================
