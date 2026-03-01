-- =============================================================================
-- BookingScraper Pro — init_db.sql  v2.0
-- Schema PostgreSQL alineado con SQLAlchemy models.py
--
-- [FIX NEW-04] Script corregido para eliminar divergencias con models.py:
--   - Columna: hotels.url_id (FK a url_queue)       → AÑADIDA
--   - Columna: hotels.images_local JSONB             → AÑADIDA
--   - Columna: hotels.url VARCHAR(512)               → AÑADIDA
--   - Columna: url_queue.last_error TEXT             → RENOMBRADA (era error_message)
--   - Columna: url_queue.scraped_at TIMESTAMPTZ      → AÑADIDA (era last_attempt)
--   - Columna: url_queue.language VARCHAR(10)        → AÑADIDA
--   - Tabla:   url_language_status                   → AÑADIDA (antes ausente)
--   - UNIQUE constraint hotels: (url_id, language)  → CORREGIDO (antes booking_url)
--   - Índices: alineados con ix_urlqueue_status_priority, ix_hotels_url_language
--
-- NOTAS:
--   Este script crea el schema desde cero. Para bases existentes, usar
--   migration_v2_url_language_status.sql (gestión de cambios incrementales).
--   Las columnas usan TIMESTAMPTZ (timezone-aware) consistente con func.now().
-- =============================================================================

-- Extensiones requeridas
CREATE EXTENSION IF NOT EXISTS "pg_trgm";    -- búsqueda de texto eficiente
CREATE EXTENSION IF NOT EXISTS "btree_gin";  -- soporte GIN para tipos básicos

-- =============================================================================
-- TABLA: url_queue
-- Cola principal de URLs a procesar. Una fila por URL.
-- =============================================================================

CREATE TABLE IF NOT EXISTS url_queue (
    id          SERIAL PRIMARY KEY,
    url         VARCHAR(512)    NOT NULL,
    status      VARCHAR(50)     NOT NULL DEFAULT 'pending',
    priority    INTEGER         NOT NULL DEFAULT 0,
    language    VARCHAR(10)              DEFAULT 'en',
    retry_count INTEGER         NOT NULL DEFAULT 0,
    max_retries INTEGER         NOT NULL DEFAULT 3,
    last_error  TEXT,
    scraped_at  TIMESTAMPTZ,
    created_at  TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ     NOT NULL DEFAULT NOW(),

    CONSTRAINT url_queue_url_unique UNIQUE (url),
    CONSTRAINT url_queue_status_check CHECK (
        status IN ('pending','processing','completed','failed','incomplete')
    )
);

-- Índices para url_queue
CREATE UNIQUE INDEX IF NOT EXISTS url_queue_url_key
    ON url_queue (url);

CREATE INDEX IF NOT EXISTS ix_urlqueue_status_priority
    ON url_queue (status, priority DESC);

CREATE INDEX IF NOT EXISTS idx_url_status
    ON url_queue (status);

CREATE INDEX IF NOT EXISTS idx_url_priority
    ON url_queue (priority DESC);

CREATE INDEX IF NOT EXISTS idx_url_retry
    ON url_queue (retry_count, max_retries)
    WHERE status = 'failed';

-- =============================================================================
-- TABLA: hotels
-- Datos extraídos de hoteles. Una fila por (url_id, language).
-- =============================================================================

CREATE TABLE IF NOT EXISTS hotels (
    id              SERIAL PRIMARY KEY,
    url_id          INTEGER         REFERENCES url_queue(id) ON DELETE SET NULL,
    url             VARCHAR(512),
    language        VARCHAR(10)     NOT NULL DEFAULT 'en',

    -- Información básica
    name            VARCHAR(255),
    address         TEXT,
    description     TEXT,

    -- Puntuaciones
    rating          FLOAT,
    total_reviews   INTEGER,
    rating_category VARCHAR(100),
    review_scores   JSONB,

    -- Servicios e instalaciones
    services        JSONB,
    facilities      JSONB,

    -- Políticas
    house_rules     TEXT,
    important_info  TEXT,

    -- Habitaciones
    rooms_info      JSONB,

    -- Imágenes
    images_urls     JSONB,
    images_local    JSONB,
    images_count    INTEGER         NOT NULL DEFAULT 0,

    -- Metadatos
    scraped_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

-- Índice único por url_id + language (una fila por hotel + idioma)
CREATE UNIQUE INDEX IF NOT EXISTS ix_hotels_url_language
    ON hotels (url_id, language);

CREATE INDEX IF NOT EXISTS idx_hotels_name
    ON hotels (name);

CREATE INDEX IF NOT EXISTS idx_hotels_language
    ON hotels (language);

CREATE INDEX IF NOT EXISTS idx_hotels_rating
    ON hotels (rating DESC NULLS LAST);

CREATE INDEX IF NOT EXISTS idx_hotels_scraped_at
    ON hotels (scraped_at DESC);

-- Índices GIN para búsquedas en JSONB (NEW-05 recommendation)
CREATE INDEX IF NOT EXISTS idx_hotels_services_gin
    ON hotels USING GIN (services);

CREATE INDEX IF NOT EXISTS idx_hotels_facilities_gin
    ON hotels USING GIN (facilities);

-- =============================================================================
-- TABLA: url_language_status
-- Tracking de completitud por URL + idioma. Una fila por (url_id, language).
-- Requerida por completeness_service.py (v6.0).
-- =============================================================================

CREATE TABLE IF NOT EXISTS url_language_status (
    id              SERIAL PRIMARY KEY,
    url_id          INTEGER         NOT NULL REFERENCES url_queue(id) ON DELETE CASCADE,
    language        VARCHAR(10)     NOT NULL,
    status          VARCHAR(50)     NOT NULL DEFAULT 'pending',
    retry_count     INTEGER         NOT NULL DEFAULT 0,
    max_retries     INTEGER         NOT NULL DEFAULT 3,
    last_error      TEXT,
    scraped_at      TIMESTAMPTZ,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),

    CONSTRAINT uls_url_lang_unique UNIQUE (url_id, language),
    CONSTRAINT uls_status_check CHECK (
        status IN ('pending','processing','completed','failed','skipped')
    )
);

-- Índices para url_language_status
-- [NEW-05] Índice compuesto para consultas por url_id + status (retry eligibility)
CREATE INDEX IF NOT EXISTS ix_uls_url_status
    ON url_language_status (url_id, status);

-- Índices parciales eficientes (ya presentes en producción, documentados aquí)
CREATE INDEX IF NOT EXISTS ix_uls_failed_updated
    ON url_language_status (updated_at DESC)
    WHERE status = 'failed';

CREATE INDEX IF NOT EXISTS ix_uls_pending_retry
    ON url_language_status (url_id)
    WHERE status IN ('pending', 'failed') AND retry_count < max_retries;

-- =============================================================================
-- TABLA: scraping_logs
-- Log detallado de cada operación de scraping.
-- =============================================================================

CREATE TABLE IF NOT EXISTS scraping_logs (
    id               SERIAL PRIMARY KEY,
    url_id           INTEGER     REFERENCES url_queue(id) ON DELETE SET NULL,
    status           VARCHAR(50) NOT NULL,
    language         VARCHAR(10),
    duration_seconds FLOAT,
    items_extracted  INTEGER     NOT NULL DEFAULT 0,
    error_message    TEXT,
    http_status_code INTEGER,
    user_agent       TEXT,
    vpn_ip           VARCHAR(50),
    task_id          VARCHAR(100),
    timestamp        TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_logs_timestamp
    ON scraping_logs (timestamp DESC);

CREATE INDEX IF NOT EXISTS idx_logs_url_id
    ON scraping_logs (url_id);

CREATE INDEX IF NOT EXISTS idx_logs_status
    ON scraping_logs (status);

-- =============================================================================
-- TABLA: vpn_rotations
-- Registro de rotaciones de VPN.
-- =============================================================================

CREATE TABLE IF NOT EXISTS vpn_rotations (
    id              SERIAL PRIMARY KEY,
    old_ip          VARCHAR(45),
    new_ip          VARCHAR(45),
    country         VARCHAR(100),
    rotation_reason VARCHAR(100),
    requests_count  INTEGER     NOT NULL DEFAULT 0,
    success         BOOLEAN     NOT NULL DEFAULT TRUE,
    error_message   TEXT,
    rotated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_vpn_rotated_at
    ON vpn_rotations (rotated_at DESC);

-- =============================================================================
-- TABLA: system_metrics
-- Métricas del sistema capturadas periódicamente.
-- =============================================================================

CREATE TABLE IF NOT EXISTS system_metrics (
    id                  SERIAL PRIMARY KEY,
    urls_pending        INTEGER NOT NULL DEFAULT 0,
    urls_processing     INTEGER NOT NULL DEFAULT 0,
    urls_completed      INTEGER NOT NULL DEFAULT 0,
    urls_failed         INTEGER NOT NULL DEFAULT 0,
    hotels_scraped      INTEGER NOT NULL DEFAULT 0,
    images_downloaded   INTEGER NOT NULL DEFAULT 0,
    active_workers      INTEGER NOT NULL DEFAULT 0,
    avg_scraping_time   FLOAT,
    total_scraping_time FLOAT   NOT NULL DEFAULT 0.0,
    cpu_usage           FLOAT,
    memory_usage        FLOAT,
    disk_usage          FLOAT,
    recorded_at         TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_metrics_recorded_at
    ON system_metrics (recorded_at DESC);

-- =============================================================================
-- VISTA: vw_url_completeness
-- Resumen de completitud de scraping por URL.
-- =============================================================================

CREATE OR REPLACE VIEW vw_url_completeness AS
SELECT
    q.id                                            AS url_id,
    q.url,
    q.status                                        AS queue_status,
    COUNT(uls.id)                                   AS total_languages,
    COUNT(uls.id) FILTER (WHERE uls.status = 'completed') AS completed_languages,
    COUNT(uls.id) FILTER (WHERE uls.status = 'failed')    AS failed_languages,
    COUNT(uls.id) FILTER (WHERE uls.status = 'pending')   AS pending_languages,
    ROUND(
        100.0 * COUNT(uls.id) FILTER (WHERE uls.status = 'completed')
        / NULLIF(COUNT(uls.id), 0),
        1
    )                                               AS completion_pct,
    MAX(uls.updated_at)                             AS last_updated
FROM url_queue q
LEFT JOIN url_language_status uls ON uls.url_id = q.id
GROUP BY q.id, q.url, q.status;

-- =============================================================================
-- FUNCIÓN: updated_at trigger
-- Actualiza updated_at automáticamente en INSERT/UPDATE.
-- =============================================================================

CREATE OR REPLACE FUNCTION fn_update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trg_url_queue_updated_at
    BEFORE UPDATE ON url_queue
    FOR EACH ROW EXECUTE FUNCTION fn_update_updated_at();

CREATE OR REPLACE TRIGGER trg_hotels_updated_at
    BEFORE UPDATE ON hotels
    FOR EACH ROW EXECUTE FUNCTION fn_update_updated_at();

CREATE OR REPLACE TRIGGER trg_uls_updated_at
    BEFORE UPDATE ON url_language_status
    FOR EACH ROW EXECUTE FUNCTION fn_update_updated_at();

-- =============================================================================
-- FIN DEL SCRIPT
-- =============================================================================
-- Para verificar la instalación:
--   \dt           -- listar tablas
--   \di           -- listar índices
--   SELECT COUNT(*) FROM url_queue;
-- =============================================================================
