-- ============================================================================
-- install_clean_v49.sql — BookingScraper Pro v6.0
-- Esquema completo para instalación en DB NUEVA (clean install only).
-- Plataforma: PostgreSQL 15+ en Windows 11
--
-- USO:
--   psql -U postgres -d bookingscraper -f install_clean_v49.sql
--
--   El script completo es idempotente (IF NOT EXISTS).
--
-- CHANGELOG v49 (clean install):
--   BUG-STARRATING-002  hotels.star_rating CHECK 0-5 → 0-10
--   BUG-VARCHAR-003     hotels.city / country VARCHAR → TEXT
--   NEW-COLS-001        9 columnas JSON-LD en hotels
--   BUG-IMG-SCHEMA      2 columnas nuevas en image_downloads (id_photo, category)
--   NEW-TABLE-001       Nueva tabla image_data
--   BUG-003/BUG-103     scraping_logs FK via trigger
--   BUG-016             url_language_status incluye status 'incomplete'
--   BUG-019             system_metrics índices temporales
-- ============================================================================

\set ON_ERROR_STOP on

BEGIN;

-- ============================================================================
-- 1. EXTENSIONS
-- ============================================================================
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";
DO $$
BEGIN
    CREATE EXTENSION IF NOT EXISTS "btree_gin";
EXCEPTION WHEN OTHERS THEN
    RAISE NOTICE 'btree_gin no disponible (opcional) — continuando sin ella.';
END;
$$;

-- ============================================================================
-- 2. ROLES
-- ============================================================================
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'app_read') THEN
        CREATE ROLE app_read NOLOGIN;
    END IF;
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'app_write') THEN
        CREATE ROLE app_write NOLOGIN;
    END IF;
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'app_scraper') THEN
        CREATE ROLE app_scraper NOLOGIN;
    END IF;
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'bookingscraper_user') THEN
        CREATE ROLE bookingscraper_user LOGIN PASSWORD 'CHANGE_THIS_PASSWORD_IN_PRODUCTION';
        GRANT app_read    TO bookingscraper_user;
        GRANT app_write   TO bookingscraper_user;
        GRANT app_scraper TO bookingscraper_user;
    END IF;
END
$$;

-- ============================================================================
-- 3. TABLAS
-- ============================================================================

-- url_queue ------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS url_queue (
    id               UUID          NOT NULL DEFAULT uuid_generate_v4(),
    url              VARCHAR(2048) NOT NULL,
    base_url         VARCHAR(2048) NOT NULL,
    external_ref     VARCHAR(64)   NULL,
    hotel_id_booking VARCHAR(64)   NULL,
    status           VARCHAR(32)   NOT NULL DEFAULT 'pending',
    priority         SMALLINT      NOT NULL DEFAULT 5,
    retry_count      SMALLINT      NOT NULL DEFAULT 0,
    max_retries      SMALLINT      NOT NULL DEFAULT 3,
    last_error       VARCHAR(2000) NULL,
    created_at       TIMESTAMPTZ   NOT NULL DEFAULT NOW(),
    updated_at       TIMESTAMPTZ   NOT NULL DEFAULT NOW(),
    scraped_at       TIMESTAMPTZ   NULL,
    version_id       INTEGER       NOT NULL DEFAULT 1,
    CONSTRAINT pk_url_queue           PRIMARY KEY (id),
    CONSTRAINT uq_url_queue_url       UNIQUE (url),
    CONSTRAINT chk_url_queue_status   CHECK (status IN ('pending','processing','done','error','skipped')),
    CONSTRAINT chk_url_queue_priority CHECK (priority BETWEEN 1 AND 10)
);

CREATE INDEX IF NOT EXISTS ix_url_queue_external_ref ON url_queue (external_ref) WHERE external_ref IS NOT NULL;
CREATE INDEX IF NOT EXISTS ix_url_queue_status_priority ON url_queue (status, priority DESC);
CREATE INDEX IF NOT EXISTS ix_url_queue_created_at      ON url_queue (created_at DESC);
CREATE INDEX IF NOT EXISTS ix_url_queue_hotel_id        ON url_queue (hotel_id_booking);

-- hotels ---------------------------------------------------------------------
-- NEW-COLS-001: 9 columnas JSON-LD añadidas en v49
CREATE TABLE IF NOT EXISTS hotels (
    id                   UUID          NOT NULL DEFAULT uuid_generate_v4(),
    url_id               UUID          NOT NULL,
    url                  VARCHAR(2048) NOT NULL,
    language             VARCHAR(10)   NOT NULL,
    hotel_name           VARCHAR(512)  NULL,
    hotel_id_booking     VARCHAR(64)   NULL,
    city                 TEXT          NULL,
    country              TEXT          NULL,
    address              VARCHAR(512)  NULL,
    latitude             FLOAT         NULL,
    longitude            FLOAT         NULL,
    star_rating          FLOAT         NULL,
    review_score         FLOAT         NULL,
    review_count         INTEGER       NULL,
    description          TEXT          NULL,
    amenities            JSONB         NULL DEFAULT '[]'::jsonb,
    room_types           JSONB         NULL DEFAULT '[]'::jsonb,
    policies             JSONB         NULL DEFAULT '{}'::jsonb,
    photos               JSONB         NULL DEFAULT '[]'::jsonb,
    raw_data             JSONB         NULL DEFAULT '{}'::jsonb,
    -- NEW-COLS-001 schema.org / JSON-LD
    main_image_url       VARCHAR(2048) NULL,
    short_description    TEXT          NULL,
    rating_value         FLOAT         NULL,
    best_rating          FLOAT         NULL,
    review_count_schema  INTEGER       NULL,
    street_address       VARCHAR(512)  NULL,
    address_locality     VARCHAR(256)  NULL,
    address_country      VARCHAR(128)  NULL,
    postal_code          VARCHAR(20)   NULL,
    -- metadatos scraping
    scrape_duration_s    FLOAT         NULL,
    scrape_engine        VARCHAR(32)   NULL,
    created_at           TIMESTAMPTZ   NOT NULL DEFAULT NOW(),
    updated_at           TIMESTAMPTZ   NOT NULL DEFAULT NOW(),
    version_id           INTEGER       NOT NULL DEFAULT 1,
    CONSTRAINT pk_hotels                PRIMARY KEY (id),
    CONSTRAINT fk_hotels_url_id         FOREIGN KEY (url_id)
                                            REFERENCES url_queue(id) ON DELETE CASCADE,
    CONSTRAINT uq_hotels_url_lang       UNIQUE (url_id, language),
    CONSTRAINT chk_hotels_star_rating   CHECK (star_rating IS NULL
                                            OR (star_rating >= 0 AND star_rating <= 10)),
    CONSTRAINT chk_hotels_review_score  CHECK (review_score IS NULL
                                            OR (review_score >= 0 AND review_score <= 10)),
    CONSTRAINT chk_hotels_review_count  CHECK (review_count IS NULL OR review_count >= 0),
    CONSTRAINT chk_hotels_rating_value  CHECK (rating_value IS NULL
                                            OR (rating_value >= 0 AND rating_value <= 10)),
    CONSTRAINT chk_hotels_best_rating   CHECK (best_rating IS NULL
                                            OR (best_rating >= 0 AND best_rating <= 10)),
    CONSTRAINT chk_hotels_rv_schema     CHECK (review_count_schema IS NULL
                                            OR review_count_schema >= 0)
);

CREATE UNIQUE INDEX IF NOT EXISTS ix_hotels_url_lang_null
    ON hotels (url_id, language)
    WHERE hotel_name IS NOT NULL;

CREATE INDEX IF NOT EXISTS ix_hotels_city_country  ON hotels (city, country);
CREATE INDEX IF NOT EXISTS ix_hotels_hotel_id      ON hotels (hotel_id_booking);
CREATE INDEX IF NOT EXISTS ix_hotels_created_at    ON hotels (created_at DESC);
CREATE INDEX IF NOT EXISTS ix_hotels_amenities_gin ON hotels USING GIN (amenities);
CREATE INDEX IF NOT EXISTS ix_hotels_name_trgm     ON hotels USING GIN (hotel_name gin_trgm_ops);
CREATE INDEX IF NOT EXISTS ix_hotels_lat_lon       ON hotels (latitude, longitude)
    WHERE latitude IS NOT NULL AND longitude IS NOT NULL;

-- url_language_status --------------------------------------------------------
-- BUG-016: status incluye 'incomplete'
CREATE TABLE IF NOT EXISTS url_language_status (
    id         UUID          NOT NULL DEFAULT uuid_generate_v4(),
    url_id     UUID          NOT NULL,
    language   VARCHAR(10)   NOT NULL,
    status     VARCHAR(32)   NOT NULL DEFAULT 'pending',
    attempts   SMALLINT      NOT NULL DEFAULT 0,
    last_error VARCHAR(2000) NULL,
    created_at TIMESTAMPTZ   NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ   NOT NULL DEFAULT NOW(),
    CONSTRAINT pk_uls          PRIMARY KEY (id),
    CONSTRAINT fk_uls_url_id   FOREIGN KEY (url_id)
                                   REFERENCES url_queue(id) ON DELETE CASCADE,
    CONSTRAINT uq_uls_url_lang UNIQUE (url_id, language),
    CONSTRAINT chk_uls_status  CHECK (status IN
        ('pending','processing','done','error','skipped','incomplete'))
);

CREATE INDEX IF NOT EXISTS ix_uls_url_id ON url_language_status (url_id);
CREATE INDEX IF NOT EXISTS ix_uls_status ON url_language_status (status);

-- image_downloads ------------------------------------------------------------
-- BUG-IMG-SCHEMA (v49): columnas id_photo + category
CREATE TABLE IF NOT EXISTS image_downloads (
    id              UUID          NOT NULL DEFAULT uuid_generate_v4(),
    hotel_id        UUID          NOT NULL,
    url             VARCHAR(2048) NOT NULL,
    local_path      VARCHAR(1024) NULL,
    file_size_bytes INTEGER       NULL,
    content_type    VARCHAR(64)   NULL,
    status          VARCHAR(32)   NOT NULL DEFAULT 'pending',
    error_message   VARCHAR(2000) NULL,
    created_at      TIMESTAMPTZ   NOT NULL DEFAULT NOW(),
    downloaded_at   TIMESTAMPTZ   NULL,
    id_photo        VARCHAR(32)   NULL,
    category        VARCHAR(16)   NULL,
    CONSTRAINT pk_imgdl           PRIMARY KEY (id),
    CONSTRAINT fk_imgdl_hotel_id  FOREIGN KEY (hotel_id)
                                      REFERENCES hotels(id) ON DELETE CASCADE,
    CONSTRAINT uq_imgdl_hotel_url UNIQUE (hotel_id, url),
    CONSTRAINT chk_imgdl_status   CHECK (status IN
        ('pending','downloading','done','error','skipped')),
    CONSTRAINT chk_imgdl_category CHECK (category IS NULL OR category IN
        ('thumb_url','large_url','highres_url'))
);

CREATE INDEX IF NOT EXISTS ix_imgdl_hotel_id ON image_downloads (hotel_id);
CREATE INDEX IF NOT EXISTS ix_imgdl_status   ON image_downloads (status);
CREATE INDEX IF NOT EXISTS ix_imgdl_id_photo ON image_downloads (id_photo)
    WHERE id_photo IS NOT NULL;

CREATE UNIQUE INDEX IF NOT EXISTS uq_imgdl_hotel_photo_cat
    ON image_downloads (hotel_id, id_photo, category)
    WHERE id_photo IS NOT NULL AND category IS NOT NULL;

-- image_data -----------------------------------------------------------------
-- NEW-TABLE-001 (v49): metadatos completos por foto única de Booking.com
CREATE TABLE IF NOT EXISTS image_data (
    id               UUID        NOT NULL DEFAULT uuid_generate_v4(),
    id_photo         VARCHAR(32) NOT NULL,
    hotel_id         UUID        NOT NULL,
    orientation      VARCHAR(16) NULL,
    photo_width      INTEGER     NULL,
    photo_height     INTEGER     NULL,
    alt              TEXT        NULL,
    created_at_photo TIMESTAMPTZ NULL,
    created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT pk_image_data           PRIMARY KEY (id),
    CONSTRAINT uq_image_data_id_photo  UNIQUE (id_photo),
    CONSTRAINT fk_image_data_hotel     FOREIGN KEY (hotel_id)
                                           REFERENCES hotels(id) ON DELETE CASCADE,
    CONSTRAINT chk_imgdata_orientation CHECK (orientation IS NULL OR orientation IN
        ('landscape','portrait','square')),
    CONSTRAINT chk_imgdata_width       CHECK (photo_width  IS NULL OR photo_width  > 0),
    CONSTRAINT chk_imgdata_height      CHECK (photo_height IS NULL OR photo_height > 0)
);

CREATE INDEX IF NOT EXISTS ix_imgdata_hotel_id ON image_data (hotel_id);

-- system_metrics -------------------------------------------------------------
-- BUG-019: índices para series temporales
CREATE TABLE IF NOT EXISTS system_metrics (
    id                  BIGSERIAL   PRIMARY KEY,
    recorded_at         TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    cpu_usage           FLOAT       NULL,
    memory_usage        FLOAT       NULL,
    active_workers      SMALLINT    NULL,
    db_pool_checked_out SMALLINT    NULL,
    redis_connected     BOOLEAN     NULL,
    urls_pending        INTEGER     NULL,
    urls_done           INTEGER     NULL,
    extra_data          JSONB       NULL DEFAULT '{}'::jsonb
);

CREATE INDEX IF NOT EXISTS ix_sysmetrics_recorded_cpu ON system_metrics (recorded_at DESC, cpu_usage);
CREATE INDEX IF NOT EXISTS ix_sysmetrics_recorded_mem ON system_metrics (recorded_at DESC, memory_usage);

-- ============================================================================
-- 4. PARTICIONADA: scraping_logs
-- BUG-003/BUG-103: FK enforced via trigger (no FK en tablas particionadas)
-- ============================================================================
CREATE TABLE IF NOT EXISTS scraping_logs (
    id            UUID         NOT NULL DEFAULT uuid_generate_v4(),
    url_id        UUID         NOT NULL,
    hotel_id      UUID         NULL,
    language      VARCHAR(10)  NULL,
    event_type    VARCHAR(64)  NOT NULL,
    status        VARCHAR(32)  NOT NULL,
    error_message TEXT         NULL,
    duration_ms   INTEGER      NULL,
    worker_id     VARCHAR(128) NULL,
    extra_data    JSONB        NULL DEFAULT '{}'::jsonb,
    scraped_at    TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    CONSTRAINT pk_scraping_logs PRIMARY KEY (id, scraped_at)
) PARTITION BY RANGE (scraped_at);

CREATE OR REPLACE FUNCTION trg_fn_scraping_logs_fk_check()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM url_queue WHERE id = NEW.url_id) THEN
        RAISE EXCEPTION 'scraping_logs FK violation: url_id=% not found in url_queue', NEW.url_id
            USING ERRCODE = 'foreign_key_violation';
    END IF;
    IF NEW.hotel_id IS NOT NULL THEN
        IF NOT EXISTS (SELECT 1 FROM hotels WHERE id = NEW.hotel_id) THEN
            RAISE EXCEPTION 'scraping_logs FK violation: hotel_id=% not found in hotels', NEW.hotel_id
                USING ERRCODE = 'foreign_key_violation';
        END IF;
    END IF;
    RETURN NEW;
END;
$$;

DO $$
DECLARE
    delta INT; y INT; m INT; pname TEXT; pstart TEXT; pend TEXT; nm INT; ny INT;
BEGIN
    FOR delta IN 0..2 LOOP
        y      := EXTRACT(YEAR  FROM CURRENT_DATE + (delta || ' months')::interval)::int;
        m      := EXTRACT(MONTH FROM CURRENT_DATE + (delta || ' months')::interval)::int;
        pname  := FORMAT('scraping_logs_%s_%s', LPAD(y::text,4,'0'), LPAD(m::text,2,'0'));
        pstart := FORMAT('%s-%s-01', LPAD(y::text,4,'0'), LPAD(m::text,2,'0'));
        IF m = 12 THEN ny := y+1; nm := 1; ELSE ny := y; nm := m+1; END IF;
        pend   := FORMAT('%s-%s-01', LPAD(ny::text,4,'0'), LPAD(nm::text,2,'0'));
        IF NOT EXISTS (SELECT 1 FROM pg_tables WHERE tablename = pname AND schemaname = 'public') THEN
            EXECUTE FORMAT('CREATE TABLE %I PARTITION OF scraping_logs FOR VALUES FROM (%L) TO (%L)',
                pname, pstart::timestamptz, pend::timestamptz);
            EXECUTE FORMAT('CREATE INDEX ON %I (url_id)', pname);
            RAISE NOTICE 'Partición creada: %', pname;
        END IF;
    END LOOP;
END;
$$;

DO $$
DECLARE pname TEXT;
BEGIN
    FOR pname IN
        SELECT tablename FROM pg_tables
        WHERE tablename LIKE 'scraping_logs_%' AND schemaname = 'public'
    LOOP
        EXECUTE FORMAT(
            'DROP TRIGGER IF EXISTS trg_scraping_logs_fk_check ON %I; '
            'CREATE TRIGGER trg_scraping_logs_fk_check '
            'BEFORE INSERT OR UPDATE ON %I '
            'FOR EACH ROW EXECUTE FUNCTION trg_fn_scraping_logs_fk_check()',
            pname, pname);
    END LOOP;
END;
$$;

-- ============================================================================
-- 5. TRIGGER updated_at
-- ============================================================================
CREATE OR REPLACE FUNCTION fn_set_updated_at()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN NEW.updated_at = NOW(); RETURN NEW; END;
$$;

DROP TRIGGER IF EXISTS trg_url_queue_updated_at ON url_queue;
CREATE TRIGGER trg_url_queue_updated_at
    BEFORE UPDATE ON url_queue
    FOR EACH ROW EXECUTE FUNCTION fn_set_updated_at();

DROP TRIGGER IF EXISTS trg_hotels_updated_at ON hotels;
CREATE TRIGGER trg_hotels_updated_at
    BEFORE UPDATE ON hotels
    FOR EACH ROW EXECUTE FUNCTION fn_set_updated_at();

DROP TRIGGER IF EXISTS trg_uls_updated_at ON url_language_status;
CREATE TRIGGER trg_uls_updated_at
    BEFORE UPDATE ON url_language_status
    FOR EACH ROW EXECUTE FUNCTION fn_set_updated_at();

-- ============================================================================
-- 6. GRANTS
-- ============================================================================
GRANT SELECT                         ON ALL TABLES IN SCHEMA public TO app_read;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_write;
GRANT USAGE, SELECT                  ON ALL SEQUENCES IN SCHEMA public TO app_write;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_scraper;
GRANT USAGE, SELECT                  ON ALL SEQUENCES IN SCHEMA public TO app_scraper;

COMMIT;
