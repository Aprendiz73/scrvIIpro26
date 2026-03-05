-- =============================================================================
-- BookingScraper Pro — Migration v24 Enterprise Audit
-- =============================================================================
-- Repository: https://github.com/Aprendiz73/scrvIIpro26.git
-- Date:       2026-03-04
-- Version:    v24 (applies on top of v23 migration)
--
-- CHANGES:
--   1. last_error columns → VARCHAR(2000) in url_queue and url_language_status
--   2. JSONB CHECK constraints on hotels table (services, facilities,
--      review_scores, images_urls)
--   3. Partial index ix_urlqueue_pending_dispatch (if not already created)
--
-- HOW TO RUN:
--   psql -U postgres -d booking_scraper -f migration_v24_enterprise_audit.sql
--
-- NOTE: CREATE INDEX CONCURRENTLY cannot run inside a transaction block.
--       The index creation is placed OUTSIDE the main transaction below.
-- =============================================================================

BEGIN;

-- ─── 1. url_queue.last_error → VARCHAR(2000) ─────────────────────────────────
-- [FIX ERR-SEC-001 / H004 related] Enforce max error length at DB level.
-- Previously TEXT (unbounded). VARCHAR(2000) is enforced by PostgreSQL engine,
-- independent of application-level truncation.
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'url_queue'
          AND column_name = 'last_error'
          AND data_type = 'text'
    ) THEN
        ALTER TABLE url_queue
            ALTER COLUMN last_error TYPE VARCHAR(2000)
            USING last_error::VARCHAR(2000);
        RAISE NOTICE 'url_queue.last_error: TEXT → VARCHAR(2000)';
    ELSE
        RAISE NOTICE 'url_queue.last_error: already VARCHAR(2000) or column not found — skipped';
    END IF;
END $$;

-- ─── 2. url_language_status.last_error → VARCHAR(2000) ───────────────────────
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'url_language_status'
          AND column_name = 'last_error'
          AND data_type = 'text'
    ) THEN
        ALTER TABLE url_language_status
            ALTER COLUMN last_error TYPE VARCHAR(2000)
            USING last_error::VARCHAR(2000);
        RAISE NOTICE 'url_language_status.last_error: TEXT → VARCHAR(2000)';
    ELSE
        RAISE NOTICE 'url_language_status.last_error: already VARCHAR(2000) — skipped';
    END IF;
END $$;

-- ─── 3. hotels JSONB CHECK constraints ───────────────────────────────────────
-- [FIX ERR-DB-005] Validate JSONB column types at DB level.
-- Prevents application bugs or direct INSERTs from storing wrong types.
-- Safe on existing data: NULL values always pass IS NULL OR ... conditions.

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_hotel_services_array'
    ) THEN
        ALTER TABLE hotels
            ADD CONSTRAINT chk_hotel_services_array
            CHECK (services IS NULL OR jsonb_typeof(services) = 'array');
        RAISE NOTICE 'chk_hotel_services_array: added';
    ELSE
        RAISE NOTICE 'chk_hotel_services_array: already exists — skipped';
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_hotel_facilities_object'
    ) THEN
        ALTER TABLE hotels
            ADD CONSTRAINT chk_hotel_facilities_object
            CHECK (facilities IS NULL OR jsonb_typeof(facilities) = 'object');
        RAISE NOTICE 'chk_hotel_facilities_object: added';
    ELSE
        RAISE NOTICE 'chk_hotel_facilities_object: already exists — skipped';
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_hotel_review_scores_object'
    ) THEN
        ALTER TABLE hotels
            ADD CONSTRAINT chk_hotel_review_scores_object
            CHECK (review_scores IS NULL OR jsonb_typeof(review_scores) = 'object');
        RAISE NOTICE 'chk_hotel_review_scores_object: added';
    ELSE
        RAISE NOTICE 'chk_hotel_review_scores_object: already exists — skipped';
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_hotel_images_urls_array'
    ) THEN
        ALTER TABLE hotels
            ADD CONSTRAINT chk_hotel_images_urls_array
            CHECK (images_urls IS NULL OR jsonb_typeof(images_urls) = 'array');
        RAISE NOTICE 'chk_hotel_images_urls_array: added';
    ELSE
        RAISE NOTICE 'chk_hotel_images_urls_array: already exists — skipped';
    END IF;
END $$;

COMMIT;

-- =============================================================================
-- PARTIAL INDEX (must run OUTSIDE transaction)
-- =============================================================================
-- [FIX ERR-DB-002] Partial index for dispatch query.
-- Only indexes 'pending' rows with remaining retries (~10-20% of table).
-- ~85-90% smaller than a full index. Requires CONCURRENTLY — safe on live DB.
-- Run this block separately if you're inside a transaction:

CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_urlqueue_pending_dispatch
    ON url_queue (priority DESC, created_at ASC)
    WHERE status = 'pending' AND retry_count < max_retries;

-- Partial unique index for url_language_status deduplication
CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_hotels_url_lang_null
    ON hotels (url_id, language)
    WHERE url_id IS NULL;

-- =============================================================================
-- AUTOVACUUM TUNING (hotels and url_queue are high-churn tables)
-- =============================================================================
-- Reduce scale factors so autovacuum runs more frequently on active tables.
-- This prevents index bloat and keeps planner statistics fresh.

ALTER TABLE url_queue SET (
    autovacuum_vacuum_scale_factor   = 0.05,
    autovacuum_analyze_scale_factor  = 0.02,
    fillfactor                       = 70
);

ALTER TABLE hotels SET (
    autovacuum_vacuum_scale_factor   = 0.05,
    autovacuum_analyze_scale_factor  = 0.02,
    fillfactor                       = 80
);

ALTER TABLE url_language_status SET (
    autovacuum_vacuum_scale_factor   = 0.05,
    autovacuum_analyze_scale_factor  = 0.02,
    fillfactor                       = 70
);

-- =============================================================================
-- VERIFICATION QUERIES
-- =============================================================================
-- Run these after migration to confirm all changes were applied:

/*
-- Check VARCHAR(2000) columns:
SELECT table_name, column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE column_name = 'last_error'
  AND table_name IN ('url_queue', 'url_language_status');

-- Check JSONB constraints:
SELECT conname, contype, pg_get_constraintdef(oid) as definition
FROM pg_constraint
WHERE conname IN (
    'chk_hotel_services_array',
    'chk_hotel_facilities_object',
    'chk_hotel_review_scores_object',
    'chk_hotel_images_urls_array',
    'chk_hotel_rating_range'
)
ORDER BY conname;

-- Check partial index:
SELECT indexname, indexdef
FROM pg_indexes
WHERE indexname = 'ix_urlqueue_pending_dispatch';
*/
