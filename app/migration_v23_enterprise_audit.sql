-- =============================================================================
-- BookingScraper Pro — Migration v23 Enterprise Audit
-- Generated: 2026-03-04
-- Purpose: Fixes from ERROR_REPORT_v23 that require direct SQL (cannot be
--          created by SQLAlchemy's create_all() due to PostgreSQL-specific syntax).
-- =============================================================================
-- Run order: AFTER bookingscraper_schema_v6.sql and migration_v21_enterprise_audit.sql
-- All index operations use CONCURRENTLY — no table locks, safe for running
-- against a live database.
-- =============================================================================

BEGIN;

-- ── [ERR-DB-002] Partial index for dispatch query ─────────────────────────────
-- The dispatch query: WHERE status='pending' AND retry_count < max_retries
-- A FULL index on (status, priority, created_at) indexes ALL rows including
-- completed, failed, processing — ~85-90% waste on a mature queue.
-- A PARTIAL index only indexes rows WHERE status='pending', which is the
-- only condition that matters for dispatch performance.
--
-- SQLAlchemy's Index() does not support postgresql_where with create_all().
-- Must be created here as raw SQL with CONCURRENTLY.
--
-- REPLACES: ix_urlqueue_dispatch (full index — keep it if you cannot run
-- CONCURRENTLY, it still provides a functional index)
-- =============================================================================

COMMIT;

-- CONCURRENTLY must run outside a transaction block
-- (Cannot be inside BEGIN/COMMIT)

-- Drop the full index replaced by the partial one (optional — the partial
-- index is ~85% smaller and faster for the dispatch query):
-- DROP INDEX CONCURRENTLY IF EXISTS ix_urlqueue_dispatch;

CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_urlqueue_pending_dispatch
    ON url_queue (priority DESC, created_at ASC)
    WHERE status = 'pending'
      AND retry_count < max_retries;

COMMENT ON INDEX ix_urlqueue_pending_dispatch IS
    '[ERR-DB-002] Partial index for dispatch query: '
    'WHERE status=''pending'' AND retry_count < max_retries. '
    '~85-90% smaller than full index. Created 2026-03-04.';


-- ── [ERR-DB-004] Partial unique index for null url_id ─────────────────────────
-- The unique constraint (url_id, language) cannot enforce uniqueness when
-- url_id IS NULL (SQL NULL != NULL). A partial unique index covers this case.
-- Only indexes rows where url_id IS NULL — prevents duplicate (url, language)
-- pairs for URLs not yet linked to url_queue.

CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS ix_hotels_url_lang_null
    ON hotels (url, language)
    WHERE url_id IS NULL;

COMMENT ON INDEX ix_hotels_url_lang_null IS
    '[ERR-DB-004] Partial unique index for (url, language) when url_id IS NULL. '
    'Prevents duplicates that the main unique constraint cannot catch. '
    'Created 2026-03-04.';


-- ── [ERR-DB-007] Autovacuum tuning for high-churn tables ─────────────────────
-- url_queue and url_language_status are high-UPDATE tables (status transitions
-- on every hotel processed). Default autovacuum settings are tuned for tables
-- that change 20% of rows; these tables can change 100% of rows per run.
-- FILLFACTOR=70 leaves 30% freespace per page for HOT updates.

ALTER TABLE url_queue SET (
    autovacuum_vacuum_scale_factor  = 0.05,   -- vacuum after 5% row changes (default 20%)
    autovacuum_analyze_scale_factor = 0.02,   -- analyze after 2% row changes
    autovacuum_vacuum_cost_delay    = 2,       -- ms between vacuum pages (default 20)
    fillfactor                      = 70       -- 30% freespace for HOT updates
);

ALTER TABLE url_language_status SET (
    autovacuum_vacuum_scale_factor  = 0.05,
    autovacuum_analyze_scale_factor = 0.02,
    autovacuum_vacuum_cost_delay    = 2,
    fillfactor                      = 70
);

COMMENT ON TABLE url_queue IS
    '[ERR-DB-007] autovacuum tuned: scale_factor=0.05, fillfactor=70 for HOT updates.';
COMMENT ON TABLE url_language_status IS
    '[ERR-DB-007] autovacuum tuned: scale_factor=0.05, fillfactor=70 for HOT updates.';


-- ── Verify migrations applied ──────────────────────────────────────────────────
DO $$
DECLARE
    v_partial_idx  BOOLEAN;
    v_null_idx     BOOLEAN;
BEGIN
    SELECT EXISTS (
        SELECT 1 FROM pg_indexes
        WHERE tablename = 'url_queue'
          AND indexname  = 'ix_urlqueue_pending_dispatch'
    ) INTO v_partial_idx;

    SELECT EXISTS (
        SELECT 1 FROM pg_indexes
        WHERE tablename = 'hotels'
          AND indexname  = 'ix_hotels_url_lang_null'
    ) INTO v_null_idx;

    RAISE NOTICE '[v23 migration] ix_urlqueue_pending_dispatch: %', v_partial_idx;
    RAISE NOTICE '[v23 migration] ix_hotels_url_lang_null: %', v_null_idx;

    IF NOT v_partial_idx THEN
        RAISE WARNING '[v23 migration] ix_urlqueue_pending_dispatch NOT FOUND — run CONCURRENTLY outside transaction';
    END IF;
    IF NOT v_null_idx THEN
        RAISE WARNING '[v23 migration] ix_hotels_url_lang_null NOT FOUND — run CONCURRENTLY outside transaction';
    END IF;
END;
$$;
