-- =============================================================================
-- BookingScraper Pro v6.0  —  Complete Database Schema
-- PostgreSQL 15+  |  Idempotent (safe to run multiple times)
-- Generated: 2026-03-03
--
-- SECTIONS:
--   1. Database & Role Provisioning
--   2. Extensions
--   3. Tables (CREATE TABLE IF NOT EXISTS)
--   4. Indexes
--   5. CHECK Constraints (idempotent DO $$ blocks)
--   6. Triggers  (auto-update updated_at)
--   7. Views
--   8. Maintenance helpers
-- =============================================================================


-- =============================================================================
-- SECTION 1 — DATABASE & ROLE PROVISIONING
-- Run as superuser (postgres) once.
-- Subsequent runs are harmless (IF NOT EXISTS guards everywhere).
-- =============================================================================

-- Create the application database (comment out if already exists)
-- CREATE DATABASE booking_scraper
--     ENCODING    = 'UTF8'
--     LC_COLLATE  = 'en_US.UTF-8'
--     LC_CTYPE    = 'en_US.UTF-8'
--     TEMPLATE    = template0;

-- Application role — least-privilege
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'scraper_app') THEN
        CREATE ROLE scraper_app LOGIN PASSWORD 'CHANGE_IN_PRODUCTION';
    END IF;
END $$;

-- Read-only role for reporting / monitoring
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'scraper_readonly') THEN
        CREATE ROLE scraper_readonly LOGIN PASSWORD 'CHANGE_IN_PRODUCTION';
    END IF;
END $$;


-- =============================================================================
-- SECTION 2 — EXTENSIONS
-- =============================================================================

CREATE EXTENSION IF NOT EXISTS pg_stat_statements;  -- slow-query monitoring
CREATE EXTENSION IF NOT EXISTS btree_gin;            -- GIN on standard types
CREATE EXTENSION IF NOT EXISTS pg_trgm;              -- fuzzy text search on hotel names


-- =============================================================================
-- SECTION 3 — TABLES
-- =============================================================================

-- ---------------------------------------------------------------------------
-- 3.1  url_queue
--      Master queue of URLs to scrape. One row per unique URL.
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS url_queue (
    id          SERIAL          PRIMARY KEY,
    url         VARCHAR(512)    NOT NULL,

    -- workflow state: pending | processing | completed | failed
    status      VARCHAR(50)     NOT NULL DEFAULT 'pending',
    priority    INTEGER         NOT NULL DEFAULT 0,

    -- language tag associated with the seed URL (informational)
    language    VARCHAR(10)     NOT NULL DEFAULT 'en',

    -- retry bookkeeping
    retry_count INTEGER         NOT NULL DEFAULT 0,
    max_retries INTEGER         NOT NULL DEFAULT 3,
    last_error  TEXT,
    scraped_at  TIMESTAMPTZ,

    -- audit timestamps (server-side)
    created_at  TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ     NOT NULL DEFAULT NOW(),

    CONSTRAINT uq_url_queue_url UNIQUE (url)
);

COMMENT ON TABLE  url_queue IS 'Master scraping queue — one row per unique hotel URL.';
COMMENT ON COLUMN url_queue.status      IS 'pending | processing | completed | failed';
COMMENT ON COLUMN url_queue.priority    IS 'Higher value = processed first.';
COMMENT ON COLUMN url_queue.retry_count IS 'Number of failed attempts so far.';


-- ---------------------------------------------------------------------------
-- 3.2  hotels
--      Scraped hotel data. One row per (url_id, language) pair.
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hotels (
    id          SERIAL          PRIMARY KEY,

    -- FK to url_queue — nullable to allow standalone inserts during testing
    url_id      INTEGER         REFERENCES url_queue(id) ON DELETE SET NULL,

    -- denormalised URL column avoids JOIN on simple selects
    url         VARCHAR(512),
    language    VARCHAR(10)     NOT NULL DEFAULT 'en',

    -- core hotel data
    name                VARCHAR(255),
    address             TEXT,
    description         TEXT,

    -- ratings
    rating              NUMERIC(4,2),          -- e.g. 8.75
    total_reviews       INTEGER,
    rating_category     VARCHAR(100),
    review_scores       JSONB,                 -- {"cleanliness": 9.5, "location": 9.1, ...}

    -- amenities
    services            JSONB,                 -- ["WiFi", "Pool", ...]
    facilities          JSONB,                 -- {"Category": ["item1", ...]}

    -- policies
    house_rules         TEXT,
    important_info      TEXT,

    -- room inventory
    rooms_info          JSONB,                 -- [{"name": ..., "description": ...}]

    -- images
    images_urls         JSONB,                 -- ["https://...", ...]
    images_local        JSONB,                 -- local file paths after download
    images_count        INTEGER     NOT NULL DEFAULT 0,

    -- audit timestamps
    scraped_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT uq_hotels_url_language UNIQUE (url_id, language)
);

COMMENT ON TABLE  hotels IS 'Scraped hotel records — one row per (url_id, language).';
COMMENT ON COLUMN hotels.review_scores IS 'JSON object with per-category scores, e.g. {"cleanliness":9.5}.';
COMMENT ON COLUMN hotels.images_local  IS 'JSON array of local filesystem paths for downloaded images.';


-- ---------------------------------------------------------------------------
-- 3.3  url_language_status
--      Per-(url, language) processing state.
--      Drives completeness tracking and retry logic in completeness_service.py.
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS url_language_status (
    id          SERIAL          PRIMARY KEY,

    url_id      INTEGER         NOT NULL
                                REFERENCES url_queue(id) ON DELETE CASCADE,
    language    VARCHAR(10)     NOT NULL,

    -- workflow state: pending | processing | completed | failed
    status      VARCHAR(50)     NOT NULL DEFAULT 'pending',

    -- retry bookkeeping
    retry_count INTEGER         NOT NULL DEFAULT 0,
    max_retries INTEGER         NOT NULL DEFAULT 3,
    last_error  TEXT,
    scraped_at  TIMESTAMPTZ,

    -- audit timestamps
    created_at  TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ     NOT NULL DEFAULT NOW(),

    CONSTRAINT uq_uls_url_language UNIQUE (url_id, language)
);

COMMENT ON TABLE url_language_status IS
    'Per (url_id, language) processing state. One row per combination.';


-- ---------------------------------------------------------------------------
-- 3.4  scraping_logs
--      Detailed audit log for every scraping operation.
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS scraping_logs (
    id                  SERIAL          PRIMARY KEY,

    -- nullable FK — log survives URL deletion for audit purposes
    url_id              INTEGER         REFERENCES url_queue(id) ON DELETE SET NULL,

    -- operation outcome
    status              VARCHAR(50)     NOT NULL,   -- completed | error | retry
    language            VARCHAR(10),
    duration_seconds    NUMERIC(10,3),
    items_extracted     INTEGER         NOT NULL DEFAULT 0,
    error_message       TEXT,

    -- request context
    http_status_code    SMALLINT,
    user_agent          TEXT,
    vpn_ip              VARCHAR(45),               -- IPv4 or IPv6
    task_id             VARCHAR(100),

    -- audit timestamp
    timestamp           TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE  scraping_logs IS 'Immutable audit log — one row per scraping attempt.';
COMMENT ON COLUMN scraping_logs.vpn_ip IS 'VPN exit IP at time of request (IPv4/IPv6).';


-- ---------------------------------------------------------------------------
-- 3.5  vpn_rotations
--      Records every VPN IP rotation event.
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS vpn_rotations (
    id               SERIAL          PRIMARY KEY,
    old_ip           VARCHAR(45),
    new_ip           VARCHAR(45),
    country          VARCHAR(100),
    rotation_reason  VARCHAR(100),
    requests_count   INTEGER         NOT NULL DEFAULT 0,
    success          BOOLEAN         NOT NULL DEFAULT TRUE,
    error_message    TEXT,
    rotated_at       TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE vpn_rotations IS 'Audit log of VPN rotation events.';


-- ---------------------------------------------------------------------------
-- 3.6  system_metrics
--      Periodic system-level snapshots (queue state, performance, resources).
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS system_metrics (
    id                   SERIAL          PRIMARY KEY,

    -- queue counters (snapshot)
    urls_pending         INTEGER         NOT NULL DEFAULT 0,
    urls_processing      INTEGER         NOT NULL DEFAULT 0,
    urls_completed       INTEGER         NOT NULL DEFAULT 0,
    urls_failed          INTEGER         NOT NULL DEFAULT 0,

    -- production counters (cumulative since last reset)
    hotels_scraped       INTEGER         NOT NULL DEFAULT 0,
    images_downloaded    INTEGER         NOT NULL DEFAULT 0,

    -- worker state
    active_workers       SMALLINT        NOT NULL DEFAULT 0,

    -- timing
    avg_scraping_time    NUMERIC(10,3),          -- seconds
    total_scraping_time  NUMERIC(12,3)   NOT NULL DEFAULT 0,

    -- host resources (percentages 0-100)
    cpu_usage            NUMERIC(5,2),
    memory_usage         NUMERIC(5,2),
    disk_usage           NUMERIC(5,2),

    recorded_at          TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE  system_metrics IS 'Periodic system health snapshots — never updated, only inserted.';
COMMENT ON COLUMN system_metrics.avg_scraping_time IS 'Rolling average scraping duration in seconds.';


-- =============================================================================
-- SECTION 4 — INDEXES
-- =============================================================================

-- ── url_queue ────────────────────────────────────────────────────────────────

-- Dispatch query: WHERE status='pending' AND retry_count < max_retries
--                 ORDER BY priority DESC, created_at ASC
CREATE INDEX IF NOT EXISTS ix_urlqueue_dispatch
    ON url_queue (status, priority DESC, created_at ASC)
    WHERE status = 'pending';

-- General status lookups
CREATE INDEX IF NOT EXISTS ix_urlqueue_status
    ON url_queue (status);

-- Priority-based ordering
CREATE INDEX IF NOT EXISTS ix_urlqueue_priority
    ON url_queue (priority DESC);

-- URL lookup (unique constraint creates its own index, this is for partial scans)
CREATE INDEX IF NOT EXISTS ix_urlqueue_url
    ON url_queue (url);


-- ── hotels ───────────────────────────────────────────────────────────────────

-- [FIX BUG-V7-003] Explicit single-column index on language for language-only queries.
-- The composite ix_hotels_url_language (url_id, language) cannot satisfy
-- WHERE language='en' efficiently when language is the non-leading column.
CREATE INDEX IF NOT EXISTS ix_hotels_language
    ON hotels (language);

-- Fast lookup by url_id (FK queries)
CREATE INDEX IF NOT EXISTS ix_hotels_url_id
    ON hotels (url_id);

-- Time-range queries on scraped_at
CREATE INDEX IF NOT EXISTS ix_hotels_scraped_at
    ON hotels (scraped_at DESC);

-- Hotel name search (trigram — requires pg_trgm extension)
CREATE INDEX IF NOT EXISTS ix_hotels_name_trgm
    ON hotels USING GIN (name gin_trgm_ops);

-- review_scores JSONB queries (GIN for @>, ?, ?& operators)
CREATE INDEX IF NOT EXISTS ix_hotels_review_scores_gin
    ON hotels USING GIN (review_scores);

-- services JSONB queries
CREATE INDEX IF NOT EXISTS ix_hotels_services_gin
    ON hotels USING GIN (services);


-- ── url_language_status ───────────────────────────────────────────────────────

-- Composite lookup by (url_id, status) — retry dispatcher
CREATE INDEX IF NOT EXISTS ix_uls_url_status
    ON url_language_status (url_id, status);

-- Status-only queries (all pending across all urls)
CREATE INDEX IF NOT EXISTS ix_uls_status
    ON url_language_status (status);


-- ── scraping_logs ─────────────────────────────────────────────────────────────

-- [FIX BUG-V6-013] Without this, ON DELETE CASCADE from url_queue requires
-- a full sequential scan of scraping_logs for every url_queue delete.
-- At high insert volume this causes severe lock contention.
CREATE INDEX IF NOT EXISTS ix_scraping_logs_url_id
    ON scraping_logs (url_id);

-- Time-range queries (most common access pattern for logs)
CREATE INDEX IF NOT EXISTS ix_scraping_logs_timestamp
    ON scraping_logs (timestamp DESC);

-- Status filter (error dashboards)
CREATE INDEX IF NOT EXISTS ix_scraping_logs_status
    ON scraping_logs (status);

-- task_id lookup (Celery task tracing)
CREATE INDEX IF NOT EXISTS ix_scraping_logs_task_id
    ON scraping_logs (task_id)
    WHERE task_id IS NOT NULL;


-- ── system_metrics ────────────────────────────────────────────────────────────

CREATE INDEX IF NOT EXISTS ix_system_metrics_recorded_at
    ON system_metrics (recorded_at DESC);


-- ── vpn_rotations ─────────────────────────────────────────────────────────────

CREATE INDEX IF NOT EXISTS ix_vpn_rotations_rotated_at
    ON vpn_rotations (rotated_at DESC);


-- =============================================================================
-- SECTION 5 — CHECK CONSTRAINTS  (idempotent DO $$ blocks)
-- =============================================================================

DO $$
BEGIN

    -- ── url_queue ──────────────────────────────────────────────────────────

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_urlqueue_retry_count_nonneg'
          AND conrelid = 'url_queue'::regclass
    ) THEN
        ALTER TABLE url_queue
            ADD CONSTRAINT chk_urlqueue_retry_count_nonneg
            CHECK (retry_count >= 0);
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_urlqueue_max_retries_nonneg'
          AND conrelid = 'url_queue'::regclass
    ) THEN
        ALTER TABLE url_queue
            ADD CONSTRAINT chk_urlqueue_max_retries_nonneg
            CHECK (max_retries >= 0);
    END IF;

    -- [FIX BUG-V6-014] retry_count must not exceed max_retries
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_urlqueue_retry_lte_max'
          AND conrelid = 'url_queue'::regclass
    ) THEN
        ALTER TABLE url_queue
            ADD CONSTRAINT chk_urlqueue_retry_lte_max
            CHECK (retry_count <= max_retries);
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_urlqueue_status_valid'
          AND conrelid = 'url_queue'::regclass
    ) THEN
        ALTER TABLE url_queue
            ADD CONSTRAINT chk_urlqueue_status_valid
            CHECK (status IN ('pending', 'processing', 'completed', 'failed'));
    END IF;

    -- ── url_language_status ────────────────────────────────────────────────

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_uls_retry_count_nonneg'
          AND conrelid = 'url_language_status'::regclass
    ) THEN
        ALTER TABLE url_language_status
            ADD CONSTRAINT chk_uls_retry_count_nonneg
            CHECK (retry_count >= 0);
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_uls_max_retries_nonneg'
          AND conrelid = 'url_language_status'::regclass
    ) THEN
        ALTER TABLE url_language_status
            ADD CONSTRAINT chk_uls_max_retries_nonneg
            CHECK (max_retries >= 0);
    END IF;

    -- [FIX BUG-V6-014]
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_uls_retry_lte_max'
          AND conrelid = 'url_language_status'::regclass
    ) THEN
        ALTER TABLE url_language_status
            ADD CONSTRAINT chk_uls_retry_lte_max
            CHECK (retry_count <= max_retries);
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_uls_status_valid'
          AND conrelid = 'url_language_status'::regclass
    ) THEN
        ALTER TABLE url_language_status
            ADD CONSTRAINT chk_uls_status_valid
            CHECK (status IN ('pending', 'processing', 'completed', 'failed'));
    END IF;

    -- ── hotels ─────────────────────────────────────────────────────────────

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_hotels_images_count_nonneg'
          AND conrelid = 'hotels'::regclass
    ) THEN
        ALTER TABLE hotels
            ADD CONSTRAINT chk_hotels_images_count_nonneg
            CHECK (images_count >= 0);
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_hotels_rating_range'
          AND conrelid = 'hotels'::regclass
    ) THEN
        ALTER TABLE hotels
            ADD CONSTRAINT chk_hotels_rating_range
            CHECK (rating IS NULL OR (rating >= 0 AND rating <= 10));
    END IF;

    -- ── system_metrics ─────────────────────────────────────────────────────

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_metrics_cpu_range'
          AND conrelid = 'system_metrics'::regclass
    ) THEN
        ALTER TABLE system_metrics
            ADD CONSTRAINT chk_metrics_cpu_range
            CHECK (cpu_usage IS NULL OR (cpu_usage >= 0 AND cpu_usage <= 100));
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_metrics_memory_range'
          AND conrelid = 'system_metrics'::regclass
    ) THEN
        ALTER TABLE system_metrics
            ADD CONSTRAINT chk_metrics_memory_range
            CHECK (memory_usage IS NULL OR (memory_usage >= 0 AND memory_usage <= 100));
    END IF;

END $$;


-- =============================================================================
-- SECTION 6 — TRIGGERS  (auto-update updated_at)
-- =============================================================================

-- Generic trigger function (shared by all tables that have updated_at)
CREATE OR REPLACE FUNCTION fn_set_updated_at()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;

-- Attach to url_queue
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
        WHERE tgname = 'trg_url_queue_updated_at'
    ) THEN
        CREATE TRIGGER trg_url_queue_updated_at
            BEFORE UPDATE ON url_queue
            FOR EACH ROW EXECUTE FUNCTION fn_set_updated_at();
    END IF;
END $$;

-- Attach to hotels
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
        WHERE tgname = 'trg_hotels_updated_at'
    ) THEN
        CREATE TRIGGER trg_hotels_updated_at
            BEFORE UPDATE ON hotels
            FOR EACH ROW EXECUTE FUNCTION fn_set_updated_at();
    END IF;
END $$;

-- Attach to url_language_status
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_trigger
        WHERE tgname = 'trg_uls_updated_at'
    ) THEN
        CREATE TRIGGER trg_uls_updated_at
            BEFORE UPDATE ON url_language_status
            FOR EACH ROW EXECUTE FUNCTION fn_set_updated_at();
    END IF;
END $$;


-- =============================================================================
-- SECTION 7 — VIEWS
-- =============================================================================

-- ---------------------------------------------------------------------------
-- 7.1  v_queue_summary
--      Operational dashboard — queue state at a glance.
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_queue_summary AS
SELECT
    status,
    COUNT(*)                                AS total,
    MIN(created_at)                         AS oldest_entry,
    MAX(updated_at)                         AS latest_update,
    AVG(retry_count)::NUMERIC(5,2)          AS avg_retries,
    SUM(CASE WHEN retry_count >= max_retries THEN 1 ELSE 0 END) AS exhausted
FROM url_queue
GROUP BY status;

COMMENT ON VIEW v_queue_summary IS
    'Aggregated URL queue state by status — used by /api/stats endpoints.';


-- ---------------------------------------------------------------------------
-- 7.2  v_scraping_progress
--      Per-URL completeness across all languages.
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_scraping_progress AS
SELECT
    uq.id                                           AS url_id,
    uq.url,
    uq.status                                       AS queue_status,
    COUNT(uls.id)                                   AS languages_total,
    SUM(CASE WHEN uls.status = 'completed' THEN 1 ELSE 0 END) AS languages_done,
    SUM(CASE WHEN uls.status = 'failed'    THEN 1 ELSE 0 END) AS languages_failed,
    SUM(CASE WHEN uls.status = 'pending'   THEN 1 ELSE 0 END) AS languages_pending,
    ROUND(
        100.0 * SUM(CASE WHEN uls.status = 'completed' THEN 1 ELSE 0 END)
              / NULLIF(COUNT(uls.id), 0),
        1
    )                                               AS completion_pct,
    MAX(uls.scraped_at)                             AS last_scraped_at
FROM url_queue uq
LEFT JOIN url_language_status uls ON uls.url_id = uq.id
GROUP BY uq.id, uq.url, uq.status;

COMMENT ON VIEW v_scraping_progress IS
    'Per-URL language completion percentages — drives the progress dashboard.';


-- ---------------------------------------------------------------------------
-- 7.3  v_hotel_completeness
--      Data quality snapshot per hotel row.
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_hotel_completeness AS
SELECT
    h.id,
    h.url_id,
    h.language,
    h.name,
    h.rating,
    h.images_count,
    -- completeness score: 1 point per populated field out of 7 key fields
    (
        (CASE WHEN h.name        IS NOT NULL AND h.name <> ''        THEN 1 ELSE 0 END) +
        (CASE WHEN h.address     IS NOT NULL AND h.address <> ''     THEN 1 ELSE 0 END) +
        (CASE WHEN h.description IS NOT NULL AND h.description <> '' THEN 1 ELSE 0 END) +
        (CASE WHEN h.rating      IS NOT NULL                         THEN 1 ELSE 0 END) +
        (CASE WHEN h.review_scores IS NOT NULL                       THEN 1 ELSE 0 END) +
        (CASE WHEN h.services    IS NOT NULL                         THEN 1 ELSE 0 END) +
        (CASE WHEN h.images_count > 0                                THEN 1 ELSE 0 END)
    )                                                       AS fields_populated,
    7                                                       AS fields_total,
    ROUND(
        100.0 * (
            (CASE WHEN h.name        IS NOT NULL AND h.name <> ''        THEN 1 ELSE 0 END) +
            (CASE WHEN h.address     IS NOT NULL AND h.address <> ''     THEN 1 ELSE 0 END) +
            (CASE WHEN h.description IS NOT NULL AND h.description <> '' THEN 1 ELSE 0 END) +
            (CASE WHEN h.rating      IS NOT NULL                         THEN 1 ELSE 0 END) +
            (CASE WHEN h.review_scores IS NOT NULL                       THEN 1 ELSE 0 END) +
            (CASE WHEN h.services    IS NOT NULL                         THEN 1 ELSE 0 END) +
            (CASE WHEN h.images_count > 0                                THEN 1 ELSE 0 END)
        ) / 7.0,
        1
    )                                                       AS completeness_pct,
    h.scraped_at,
    h.updated_at
FROM hotels h;

COMMENT ON VIEW v_hotel_completeness IS
    'Data quality score per hotel row — 7 key fields, 0-100% completeness.';


-- ---------------------------------------------------------------------------
-- 7.4  v_error_summary
--      Rolling 24h error analysis for operational alerting.
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_error_summary AS
SELECT
    DATE_TRUNC('hour', timestamp)           AS hour,
    language,
    COUNT(*)                                AS total_attempts,
    SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS successes,
    SUM(CASE WHEN status = 'error'     THEN 1 ELSE 0 END) AS errors,
    SUM(CASE WHEN status = 'retry'     THEN 1 ELSE 0 END) AS retries,
    ROUND(AVG(duration_seconds)::NUMERIC, 3) AS avg_duration_sec,
    ROUND(
        100.0 * SUM(CASE WHEN status = 'error' THEN 1 ELSE 0 END)
              / NULLIF(COUNT(*), 0),
        2
    )                                       AS error_rate_pct
FROM scraping_logs
WHERE timestamp >= NOW() - INTERVAL '24 hours'
GROUP BY DATE_TRUNC('hour', timestamp), language
ORDER BY hour DESC, language;

COMMENT ON VIEW v_error_summary IS
    'Hourly error rates for the last 24h — feeds monitoring alerts.';


-- ---------------------------------------------------------------------------
-- 7.5  v_vpn_health
--      VPN rotation effectiveness summary.
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_vpn_health AS
SELECT
    DATE_TRUNC('hour', rotated_at)          AS hour,
    COUNT(*)                                AS total_rotations,
    SUM(CASE WHEN success THEN 1 ELSE 0 END) AS successful,
    SUM(CASE WHEN NOT success THEN 1 ELSE 0 END) AS failed,
    ROUND(
        100.0 * SUM(CASE WHEN success THEN 1 ELSE 0 END)
              / NULLIF(COUNT(*), 0),
        1
    )                                       AS success_rate_pct,
    AVG(requests_count)::NUMERIC(8,1)       AS avg_requests_per_rotation
FROM vpn_rotations
WHERE rotated_at >= NOW() - INTERVAL '24 hours'
GROUP BY DATE_TRUNC('hour', rotated_at)
ORDER BY hour DESC;

COMMENT ON VIEW v_vpn_health IS 'Hourly VPN rotation health for the last 24h.';


-- ---------------------------------------------------------------------------
-- 7.6  v_latest_system_metrics
--      Most recent system snapshot (single-row convenience view).
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_latest_system_metrics AS
SELECT *
FROM system_metrics
ORDER BY recorded_at DESC
LIMIT 1;

COMMENT ON VIEW v_latest_system_metrics IS
    'Latest system_metrics snapshot — used by /api/system/status.';


-- =============================================================================
-- SECTION 8 — GRANTS
-- =============================================================================

-- Application user: full DML on all tables, read on all views
GRANT CONNECT ON DATABASE booking_scraper TO scraper_app;
GRANT USAGE   ON SCHEMA public            TO scraper_app;

GRANT SELECT, INSERT, UPDATE, DELETE
    ON url_queue, hotels, url_language_status,
       scraping_logs, vpn_rotations, system_metrics
    TO scraper_app;

GRANT SELECT
    ON v_queue_summary, v_scraping_progress, v_hotel_completeness,
       v_error_summary, v_vpn_health, v_latest_system_metrics
    TO scraper_app;

-- Auto-grant on future tables created in this schema
ALTER DEFAULT PRIVILEGES IN SCHEMA public
    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO scraper_app;

-- Read-only user: views + base tables (no write)
GRANT CONNECT ON DATABASE booking_scraper TO scraper_readonly;
GRANT USAGE   ON SCHEMA public            TO scraper_readonly;

GRANT SELECT
    ON url_queue, hotels, url_language_status,
       scraping_logs, vpn_rotations, system_metrics,
       v_queue_summary, v_scraping_progress, v_hotel_completeness,
       v_error_summary, v_vpn_health, v_latest_system_metrics
    TO scraper_readonly;

-- Sequence grants (needed for SERIAL inserts)
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO scraper_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
    GRANT USAGE, SELECT ON SEQUENCES TO scraper_app;


-- =============================================================================
-- SECTION 9 — MAINTENANCE HELPERS
-- =============================================================================

-- ---------------------------------------------------------------------------
-- fn_archive_old_logs()
--   Move scraping_logs older than :days to scraping_logs_archive.
--   Call periodically (e.g. weekly via pg_cron or an external job).
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS scraping_logs_archive
    (LIKE scraping_logs INCLUDING ALL);

COMMENT ON TABLE scraping_logs_archive IS
    'Cold-storage archive for scraping_logs rows older than the retention window.';

CREATE OR REPLACE FUNCTION fn_archive_old_logs(retention_days INTEGER DEFAULT 90)
RETURNS INTEGER
LANGUAGE plpgsql
AS $$
DECLARE
    rows_moved INTEGER;
BEGIN
    WITH moved AS (
        DELETE FROM scraping_logs
        WHERE timestamp < NOW() - (retention_days || ' days')::INTERVAL
        RETURNING *
    )
    INSERT INTO scraping_logs_archive SELECT * FROM moved;

    GET DIAGNOSTICS rows_moved = ROW_COUNT;
    RETURN rows_moved;
END;
$$;

COMMENT ON FUNCTION fn_archive_old_logs IS
    'Archives scraping_logs rows older than retention_days. Returns row count moved.';


-- ---------------------------------------------------------------------------
-- fn_reset_stale_processing()
--   Resets url_queue rows stuck in "processing" state (e.g. after a crash).
--   Safe to call at startup. Returns number of rows reset.
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION fn_reset_stale_processing(stale_minutes INTEGER DEFAULT 60)
RETURNS INTEGER
LANGUAGE plpgsql
AS $$
DECLARE
    rows_reset INTEGER;
BEGIN
    UPDATE url_queue
    SET    status     = 'pending',
           updated_at = NOW()
    WHERE  status     = 'processing'
      AND  updated_at < NOW() - (stale_minutes || ' minutes')::INTERVAL;

    GET DIAGNOSTICS rows_reset = ROW_COUNT;
    RETURN rows_reset;
END;
$$;

COMMENT ON FUNCTION fn_reset_stale_processing IS
    'Resets url_queue rows stuck in processing for longer than stale_minutes.';


-- Same reset for url_language_status
CREATE OR REPLACE FUNCTION fn_reset_stale_uls(stale_minutes INTEGER DEFAULT 60)
RETURNS INTEGER
LANGUAGE plpgsql
AS $$
DECLARE
    rows_reset INTEGER;
BEGIN
    UPDATE url_language_status
    SET    status     = 'pending',
           updated_at = NOW()
    WHERE  status     = 'processing'
      AND  updated_at < NOW() - (stale_minutes || ' minutes')::INTERVAL;

    GET DIAGNOSTICS rows_reset = ROW_COUNT;
    RETURN rows_reset;
END;
$$;

COMMENT ON FUNCTION fn_reset_stale_uls IS
    'Resets url_language_status rows stuck in processing.';


-- =============================================================================
-- END OF SCHEMA — BookingScraper Pro v6.0
-- =============================================================================
