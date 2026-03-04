-- [FIX BUG-NEW-02] Migration v2: Create url_language_status table
-- Fixes: completeness_service.py references this table but it was never created.
-- Run ONCE against the booking_scraper database before starting the service.

BEGIN;

CREATE TABLE IF NOT EXISTS url_language_status (
    id          SERIAL PRIMARY KEY,
    url_id      INTEGER NOT NULL
                    REFERENCES url_queue(id) ON DELETE CASCADE,
    language    VARCHAR(10) NOT NULL,
    status      VARCHAR(50) NOT NULL DEFAULT 'pending',
    -- [FIX BUG-NEW-10] CHECK constraints prevent negative retry counters
    retry_count INTEGER NOT NULL DEFAULT 0 CHECK (retry_count >= 0),
    max_retries INTEGER NOT NULL DEFAULT 3 CHECK (max_retries >= 0),
    last_error  TEXT,
    scraped_at  TIMESTAMPTZ,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Unique constraint: one row per (url_id, language)
CREATE UNIQUE INDEX IF NOT EXISTS uls_url_lang_unique
    ON url_language_status (url_id, language);

-- [FIX BUG-NEW-04 / BUG-NEW-05] Composite index for retry/status queries
CREATE INDEX IF NOT EXISTS ix_uls_url_status
    ON url_language_status (url_id, status);

-- [FIX BUG-NEW-04] Composite index for primary dispatch query:
--   WHERE status = 'pending' AND retry_count < max_retries
--   ORDER BY priority DESC, created_at ASC
CREATE INDEX IF NOT EXISTS ix_urlqueue_dispatch
    ON url_queue (status, priority DESC, created_at ASC)
    WHERE status = 'pending';

-- [FIX BUG-NEW-10] CHECK constraints prevent negative retry counters
DO $$
BEGIN
    -- retry_count >= 0
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_urlqueue_retry_count_nonneg'
          AND conrelid = 'url_queue'::regclass
    ) THEN
        ALTER TABLE url_queue
            ADD CONSTRAINT chk_urlqueue_retry_count_nonneg
            CHECK (retry_count >= 0);
    END IF;

    -- max_retries >= 0
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
END $$;

COMMIT;

-- [FIX BUG-V6-013] Index on scraping_logs.url_id for fast FK cascade operations
CREATE INDEX IF NOT EXISTS ix_scraping_logs_url_id
    ON scraping_logs (url_id);

-- [FIX BUG-V6-014] retry_count <= max_retries constraint for url_language_status
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_uls_retry_lte_max'
          AND conrelid = 'url_language_status'::regclass
    ) THEN
        ALTER TABLE url_language_status
            ADD CONSTRAINT chk_uls_retry_lte_max
            CHECK (retry_count <= max_retries);
    END IF;

    -- [FIX BUG-AUD-001] Add status CHECK constraint to url_language_status.
    -- Required by completeness_service.py which writes 'skipped_existing'.
    -- DROP+ADD pattern: safe to re-run if constraint already exists.
    IF EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_uls_status_valid'
          AND conrelid = 'url_language_status'::regclass
    ) THEN
        ALTER TABLE url_language_status DROP CONSTRAINT chk_uls_status_valid;
    END IF;
    ALTER TABLE url_language_status
        ADD CONSTRAINT chk_uls_status_valid
        CHECK (status IN ('pending', 'processing', 'completed', 'failed', 'skipped_existing'));

    -- [FIX BUG-AUD-001] Also ensure url_queue has its status CHECK constraint.
    -- scraper_service.py writes 'incomplete' — must be permitted.
    IF EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'chk_urlqueue_status_valid'
          AND conrelid = 'url_queue'::regclass
    ) THEN
        ALTER TABLE url_queue DROP CONSTRAINT chk_urlqueue_status_valid;
    END IF;
    ALTER TABLE url_queue
        ADD CONSTRAINT chk_urlqueue_status_valid
        CHECK (status IN ('pending', 'processing', 'completed', 'failed', 'incomplete'));
END $$;

-- [FIX BUG-V7-003] Explicit single-column index on hotels.language for language-only queries.
-- The composite ix_hotels_url_language (url_id, language) cannot efficiently satisfy
-- WHERE language='en' because 'language' is the non-leading column in the composite index.
-- SQLAlchemy's index=True on the Column creates an implicit index, but an explicit named
-- index ensures the query planner always has a dedicated path for language-only filters.
CREATE INDEX IF NOT EXISTS ix_hotels_language ON hotels (language);
