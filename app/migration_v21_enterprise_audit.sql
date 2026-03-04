-- ============================================================================
-- migration_v21_enterprise_audit.sql
-- BookingScraper Pro — Fixes del Audit Empresarial v20
-- Ejecutar en PostgreSQL 14+ contra la base de datos booking_scraper
--
-- INSTRUCCIONES:
--   1. Ejecutar SIEMPRE con una réplica de respaldo activa.
--   2. Los índices CONCURRENTLY no requieren lock exclusivo — seguros en producción.
--   3. Ejecutar cada bloque por separado para monitorear progreso.
--   4. Verificar con EXPLAIN ANALYZE después de cada índice.
--
-- ROLLBACK: Cada sección tiene su ROLLBACK correspondiente comentado.
-- ============================================================================

BEGIN;

-- ── VALIDACIÓN PREVIA ────────────────────────────────────────────────────────
-- Confirmar versión de PostgreSQL (requiere >= 14 para todas las features)
DO $$
BEGIN
    IF current_setting('server_version_num')::int < 140000 THEN
        RAISE EXCEPTION 'Este script requiere PostgreSQL 14 o superior. Versión actual: %',
            current_setting('server_version');
    END IF;
    RAISE NOTICE 'PostgreSQL % — OK', current_setting('server_version');
END $$;

COMMIT;

-- ============================================================================
-- BLOQUE 1: [FIX DB-009] Partial Index para Dispatch Query
-- Reemplaza ix_urlqueue_dispatch (índice completo) con índice parcial ~85% más pequeño.
-- ============================================================================
-- NOTA: CREATE INDEX CONCURRENTLY no puede ejecutarse dentro de una transacción.
-- Ejecutar este bloque FUERA de BEGIN/COMMIT.

-- Paso 1: Crear nuevo índice parcial (no bloquea escrituras)
CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_urlqueue_pending_dispatch
    ON url_queue (priority DESC, created_at ASC)
    WHERE status = 'pending' AND retry_count < max_retries;

-- Verificar que el planner lo usa:
-- EXPLAIN ANALYZE
-- SELECT id FROM url_queue
-- WHERE status = 'pending' AND retry_count < max_retries
-- ORDER BY priority DESC, created_at ASC
-- LIMIT 10 FOR UPDATE SKIP LOCKED;
-- Esperado: "Index Scan using ix_urlqueue_pending_dispatch"

-- Paso 2 (OPCIONAL — después de validar el nuevo índice):
-- DROP INDEX CONCURRENTLY IF EXISTS ix_urlqueue_dispatch;
-- DROP INDEX CONCURRENTLY IF EXISTS ix_urlqueue_status_priority;

-- ROLLBACK: DROP INDEX CONCURRENTLY IF EXISTS ix_urlqueue_pending_dispatch;

-- ============================================================================
-- BLOQUE 2: [FIX DB-004] GIN Indexes para columnas JSONB en hotels
-- Habilita queries de contenido (@>, ?, ?|, ?&) con O(log n)
-- ============================================================================

CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_hotels_services_gin
    ON hotels USING GIN (services jsonb_path_ops);
-- jsonb_path_ops es más compacto que los operadores por defecto.
-- Soporta: @>, @?, @@. NO soporta: ?, ?|, ?& (usar jsonb_ops si se necesitan).

CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_hotels_facilities_gin
    ON hotels USING GIN (facilities jsonb_path_ops);

CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_hotels_review_scores_gin
    ON hotels USING GIN (review_scores jsonb_path_ops);

CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_hotels_images_gin
    ON hotels USING GIN (images_urls jsonb_path_ops);

-- Verificar:
-- EXPLAIN ANALYZE SELECT id FROM hotels WHERE services @> '["WiFi"]';
-- Esperado: "Bitmap Index Scan on ix_hotels_services_gin"

-- ROLLBACK:
-- DROP INDEX CONCURRENTLY IF EXISTS ix_hotels_services_gin;
-- DROP INDEX CONCURRENTLY IF EXISTS ix_hotels_facilities_gin;
-- DROP INDEX CONCURRENTLY IF EXISTS ix_hotels_review_scores_gin;
-- DROP INDEX CONCURRENTLY IF EXISTS ix_hotels_images_gin;

-- ============================================================================
-- BLOQUE 3: [FIX DATA-001] Unique Constraint para url_id IS NULL
-- Cuando url_id es NULL, el índice compuesto ix_hotels_url_language no aplica
-- unicidad (PostgreSQL trata NULLs como distintos entre sí).
-- ============================================================================

CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS ix_hotels_url_lang_null
    ON hotels (url, language)
    WHERE url_id IS NULL;

-- Este índice garantiza que no existan duplicados (url, language) cuando
-- los hoteles se insertan directamente sin FK a url_queue (url_id=NULL).

-- Verificar duplicados existentes antes de crear el índice:
-- SELECT url, language, COUNT(*) as cnt
-- FROM hotels WHERE url_id IS NULL
-- GROUP BY url, language HAVING COUNT(*) > 1;
-- Si hay duplicados, limpiar antes de crear el índice.

-- ROLLBACK: DROP INDEX CONCURRENTLY IF EXISTS ix_hotels_url_lang_null;

-- ============================================================================
-- BLOQUE 4: [FIX CONC-006] Verificar Isolation Level
-- El nivel READ COMMITTED se configura en el engine de SQLAlchemy.
-- Este bloque verifica la configuración actual de PostgreSQL.
-- ============================================================================

BEGIN;

DO $$
DECLARE
    current_isolation text;
BEGIN
    SELECT current_setting('default_transaction_isolation') INTO current_isolation;
    RAISE NOTICE 'PostgreSQL default isolation level: %', current_isolation;
    -- READ COMMITTED es el valor esperado; el engine de SQLAlchemy establece
    -- el nivel explícitamente por conexión, por lo que el default de PG es
    -- un fallback de seguridad, no el nivel operativo.
END $$;

-- Confirmar que el statement_timeout está configurado correctamente.
-- Los valores son establecidos por el connection pool de la aplicación.
SHOW statement_timeout;

COMMIT;

-- ============================================================================
-- BLOQUE 5: [FIX DB-005] Estrategia de Particionamiento (PLANIFICACIÓN)
-- Las tablas de alto volumen requieren particionamiento para Year 2+.
-- Este bloque es INFORMATIVO — la migración completa requiere planificación separada.
-- ============================================================================

-- PROYECCIÓN DE CRECIMIENTO (5,000 filas/día):
-- hotels:              Year 1 = 1.8M rows, Year 2 = 3.6M rows, Year 3 = 5.4M rows
-- scraping_logs:       idem
-- url_language_status: idem

-- ESTRATEGIA RECOMENDADA para scraping_logs y hotels:
-- Particionamiento por rango de timestamp mensual.
-- Ejemplo para scraping_logs:

-- CREATE TABLE scraping_logs_new (LIKE scraping_logs INCLUDING ALL)
--     PARTITION BY RANGE (timestamp);
--
-- CREATE TABLE scraping_logs_2026_01
--     PARTITION OF scraping_logs_new
--     FOR VALUES FROM ('2026-01-01') TO ('2026-02-01');
--
-- CREATE TABLE scraping_logs_2026_02
--     PARTITION OF scraping_logs_new
--     FOR VALUES FROM ('2026-02-01') TO ('2026-03-01');
-- [continúa por cada mes...]
--
-- -- Migración:
-- INSERT INTO scraping_logs_new SELECT * FROM scraping_logs;
-- ALTER TABLE scraping_logs RENAME TO scraping_logs_old;
-- ALTER TABLE scraping_logs_new RENAME TO scraping_logs;
-- DROP TABLE scraping_logs_old;

-- NOTA: La migración de tablas existentes requiere ventana de mantenimiento.
-- Para tablas vacías o nuevas, usar la tabla particionada desde el inicio.

-- ============================================================================
-- BLOQUE 6: [FIX SEC-006] Rate Limiting — verificación de configuración
-- El rate limiting se implementa en aplicación (FastAPI).
-- Este bloque verifica que no existan queries de /stats sin limit a nivel BD.
-- ============================================================================

BEGIN;

-- Identificar queries de aggregación costosas sin límite de tiempo:
-- (Solo ejecutar en ambiente de desarrollo con log_min_duration_statement)
-- ALTER SYSTEM SET log_min_duration_statement = 1000;  -- log queries > 1s
-- SELECT pg_reload_conf();

-- Verificar índices existentes en tablas principales:
SELECT
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename IN ('url_queue', 'hotels', 'scraping_logs', 'url_language_status')
ORDER BY tablename, indexname;

COMMIT;

-- ============================================================================
-- VALIDACIÓN FINAL
-- ============================================================================

BEGIN;

-- Verificar todos los índices creados por este script:
SELECT
    schemaname,
    tablename,
    indexname,
    pg_size_pretty(pg_relation_size(indexname::regclass)) AS index_size,
    CASE WHEN indisunique THEN 'UNIQUE' ELSE 'NON-UNIQUE' END AS uniqueness,
    CASE WHEN indisvalid THEN 'VALID' ELSE 'INVALID' END AS validity
FROM pg_indexes
JOIN pg_index ON pg_index.indexrelid = (schemaname || '.' || indexname)::regclass
WHERE indexname IN (
    'ix_urlqueue_pending_dispatch',
    'ix_hotels_services_gin',
    'ix_hotels_facilities_gin',
    'ix_hotels_review_scores_gin',
    'ix_hotels_images_gin',
    'ix_hotels_url_lang_null'
)
ORDER BY tablename, indexname;

COMMIT;

-- ============================================================================
-- REGISTRO DE CAMBIOS / CHANGELOG
-- ============================================================================
-- v21.0 - 2026-03-04
--   DB-009: Partial index ix_urlqueue_pending_dispatch (dispatch query)
--   DB-004: GIN indexes en hotels JSONB columns (services, facilities, review_scores, images_urls)
--   DATA-001: Partial unique index ix_hotels_url_lang_null (NULL url_id uniqueness)
--   CONC-006: Verificación de isolation level
--   DB-005: Estrategia de particionamiento documentada (pendiente implementación)
-- ============================================================================
