# BookingScraper Pro — System Report
**Version:** 6.0.0 (Audit v31) | **Date:** 2026-03-05 | **Platform:** Windows 11 (local)

---

## 1. Application Objective

**BookingScraper Pro** is a production-grade automated data extraction system targeting [Booking.com](https://www.booking.com). Its purpose is to collect structured hotel data—names, addresses, ratings, descriptions, facilities, room information, and image galleries—across **multiple languages simultaneously**, storing everything in a local PostgreSQL database for export and analysis.

### Core Goals

| Goal | Implementation |
|---|---|
| Multi-language extraction | 5 languages by default: `en`, `es`, `de`, `fr`, `it` |
| Anti-detection resilience | NordVPN rotation + CloudScraper + randomized delays |
| Data integrity | PostgreSQL constraints, idempotent upserts, optimistic locking |
| Full image capture | Selenium gallery modal interaction + parallel download |
| Production reliability | Circuit breakers, watchdog, graceful shutdown, audit logging |

---

## 2. System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Windows 11 — Local                          │
│                                                                      │
│  ┌──────────────┐   REST API    ┌─────────────────────────────────┐ │
│  │   Client /   │◄─────────────►│       FastAPI (main.py)         │ │
│  │   Browser    │               │  /health  /metrics  /stats      │ │
│  └──────────────┘               │  /scraping/upload  /vpn/status  │ │
│                                 └──────────────┬────────────────── ┘ │
│                                                │                     │
│                          ┌─────────────────────▼────────────────┐   │
│                          │       scraper_service.py              │   │
│                          │  - URL dispatch (atomic CTE)          │   │
│                          │  - ThreadPoolExecutor                 │   │
│                          │  - VPN circuit breaker                │   │
│                          │  - Redis circuit breaker (HIGH-002)   │   │
│                          └──────┬────────────────┬──────────────┘   │
│                                 │                │                   │
│              ┌──────────────────▼──┐    ┌────────▼──────────────┐   │
│              │    scraper.py       │    │  vpn_manager_windows  │   │
│              │  BookingScraper     │    │  NordVPN CLI wrapper  │   │
│              │  CloudScraper/Brave │    │  IP rotation + cache  │   │
│              │  Language injection │    └───────────────────────┘   │
│              └──────────┬──────── ┘                                 │
│                         │                                           │
│         ┌───────────────▼──────────────────────────────────────┐   │
│         │                  extractor.py                         │   │
│         │  BeautifulSoup + XPath hotel data extraction          │   │
│         │  8-language rating category dictionaries              │   │
│         └──────────────────────────┬───────────────────────────┘   │
│                                    │                                │
│  ┌─────────────────┐   ┌───────────▼──────────────┐  ┌──────────┐ │
│  │ image_downloader│   │      PostgreSQL           │  │  Redis/  │ │
│  │ Pillow resize   │   │  6 tables + 20+ indexes   │  │ Memurai  │ │
│  │ integrity check │   │  JSONB, GIN, partial idx  │  │ (broker) │ │
│  └─────────────────┘   └──────────────────────────┘  └──────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

### Technology Stack

| Component | Technology | Version |
|---|---|---|
| API Framework | FastAPI + Uvicorn | 0.115.x / 0.32.x |
| ORM | SQLAlchemy | 2.0.x |
| Database | PostgreSQL | 15+ |
| DB Driver | psycopg3 (psycopg[binary]) | 3.2.x |
| Task Queue | Celery (solo pool) | 5.4.x |
| Message Broker | Redis / Memurai | 5.2.x |
| Browser Automation | Selenium + Brave | 4.27.x |
| HTTP Scraping | CloudScraper | 1.2.x |
| Image Processing | Pillow | 11.0.x |
| Configuration | Pydantic Settings v2 | 2.10.x |
| Logging | Loguru | 0.7.x |
| VPN | NordVPN CLI (Windows) | — |
| Runtime | Python | 3.14.x |
| OS | Windows 11 | local |

---

## 3. System Workflow

### 3.1 URL Ingestion

```
CSV file (urls_ejemplo.csv)
         │
         ▼
   load_urls.py
         │
   INSERT INTO url_queue
   (url, status='pending', priority=0)
   ON CONFLICT DO NOTHING
```

Each line in the CSV contains a single Booking.com hotel URL. The loader deduplicates on insert.

### 3.2 Dispatch Loop

The system supports two dispatch modes (configured via `USE_CELERY_DISPATCHER`):

**Mode A — asyncio loop (default, recommended for Windows 11):**
```
main.py lifespan startup
    │
    └── _auto_dispatch_loop() [asyncio Task]
              │
              every 30 seconds:
              │
              ▼
        scraper_service.process_batch(batch_size)
              │
              ▼
        Atomic CTE: SELECT pending rows + UPDATE to 'processing'
        (FOR UPDATE SKIP LOCKED — zero race conditions)
              │
              ▼
        ThreadPoolExecutor.submit(scrape_one, url_id)
```

**Mode B — Celery Beat (optional):**
```
celery beat → process_pending_urls task → process_batch()
```

### 3.3 Scraping Pipeline (per URL)

```
scrape_one(url_id)
    │
    ├── 1. VPN check / reconnect if needed
    │
    ├── 2. completeness_service.initialize_url_processing()
    │       └── INSERT url_language_status rows (idempotent)
    │
    ├── 3. For each language (sorted alphabetically — deadlock prevention):
    │       │
    │       ├── build_language_url() → constructs localized URL
    │       │   e.g.: hotel.en-gb.html?lang=en-gb
    │       │
    │       ├── CloudScraper or Brave browser → GET page
    │       │
    │       ├── extractor.py → parse HTML:
    │       │   • hotel name (cleaned: no stars prefix, no location suffix)
    │       │   • address, description
    │       │   • rating + rating_category (8-language dict)
    │       │   • review subscores (JSONB)
    │       │   • facilities, services (JSONB)
    │       │   • house_rules, important_info
    │       │   • images_urls (gallery modal interaction via Selenium)
    │       │
    │       ├── Language mismatch check → rotate VPN + retry if wrong language
    │       │
    │       ├── _save_hotel() → INSERT INTO hotels ON CONFLICT DO NOTHING
    │       │
    │       └── record_language_success/failure()
    │
    ├── 4. Image download (language=DEFAULT only):
    │       └── image_downloader.ImageDownloader.download_images()
    │           • ThreadPoolExecutor (MAX_IMAGE_WORKERS parallel)
    │           • Pillow verify() integrity check
    │           • Resize to max 1920×1080 JPEG
    │           • Idempotent: skip existing files
    │
    ├── 5. completeness_service.finalize_url()
    │       └── UPDATE url_queue SET status='completed'/'incomplete'
    │
    └── 6. _maybe_rotate_vpn() → rotate after every N hotels
```

### 3.4 VPN Rotation Strategy

```
Triggers for VPN rotation:
  • Every VPN_ROTATE_EVERY_N=10 hotels (scheduled)
  • After 3+ consecutive failures (anomaly detection)
  • After 3+ language mismatches (geo-IP lock detected)
  • Explicit: POST /vpn/rotate

Circuit Breaker (VPN):
  CLOSED → normal → OPEN (after 5 failures) → cooldown 300s → HALF-OPEN → probe
```

### 3.5 Data Storage

```
url_queue          → one row per unique hotel URL
hotels             → one row per (url × language)
url_language_status → per-language progress tracker
scraping_logs      → full audit trail
vpn_rotations      → VPN event log
system_metrics     → periodic resource snapshots
```

### 3.6 Export

```
export_data.py
    │
    ├── CSV  → pandas DataFrame → hotels.csv
    ├── JSON → hotels.json
    └── Excel → hotels.xlsx (via openpyxl)
```

---

## 4. Database Schema Overview

### Tables & Key Constraints

| Table | PK | Key Indexes | Notable Constraints |
|---|---|---|---|
| `url_queue` | `id` | partial idx `status='pending'`, `url` UNIQUE | CHECK status in enum |
| `hotels` | `id` | UNIQUE `(url_id, lang)`, GIN on all JSONB cols, B-Tree on `url` | CHECK rating 0–10, JSONB type guards |
| `url_language_status` | `id` | UNIQUE `(url_id, language)` | CASCADE delete from url_queue |
| `scraping_logs` | `id` | `url_id`, `timestamp DESC` | — |
| `vpn_rotations` | `id` | `rotated_at DESC` | — |
| `system_metrics` | `id` | `recorded_at DESC` | — |

### Concurrency Safety

- **Atomic CTE dispatch**: single SQL round-trip eliminates the SELECT+UPDATE race window
- **FOR UPDATE SKIP LOCKED**: zero blocking between concurrent workers
- **Optimistic locking**: `version_id` column on `url_queue` and `url_language_status`
- **Alphabetical language ordering**: deadlock prevention via consistent lock acquisition order
- **Serializable isolation** available via `get_serializable_db()` for critical paths

---

## 5. Security Model

| Layer | Implementation |
|---|---|
| API Authentication | `API_KEY` header check (configurable, empty = dev mode) |
| SQL Injection | 100% parameterized queries (SQLAlchemy text() with bound params) |
| Credential management | All secrets via `.env` (never hardcoded) |
| Error exposure | Generic HTTP 500 with correlation ID — no stack traces to client |
| Rate limiting | In-memory sliding window per client IP, stale-bucket cleanup |
| Path traversal | `is_relative_to()` guard in image_downloader |
| Error truncation | `MAX_ERROR_LEN=2000` prevents DB column overflow |
| Log sanitization | URL credentials stripped before logging |

---

## 6. Enterprise Bug Fixes — v31 Audit

### Fixed in this release

| ID | Severity | Description | File(s) |
|---|---|---|---|
| HIGH-002 | HIGH | Redis circuit breaker — prevents blocking latency after Redis failure | `scraper_service.py` |
| HIGH-004 | HIGH | Windows signal handlers (SIGINT, SIGBREAK) for clean shutdown | `main.py` |
| HIGH-005 | MEDIUM | Centralized `MAX_ERROR_LEN` constant — eliminates hardcoded duplicates | `config.py`, `scraper_service.py`, `completeness_service.py` |
| HIGH-013 | MEDIUM | Celery task time limits tightened (600s→180s) — prevents worker exhaustion | `tasks.py` |
| MED-022 | MEDIUM | `/metrics` endpoint — JSON performance counters for monitoring | `main.py` |
| NEW | LOW | `os` import missing from `tasks.py` | `tasks.py` |
| NEW | LOW | New `.env.example` variables documented (REDIS CB, MAX_ERROR_LEN, CELERY limits) | `.env.example` |
| NEW | SQL | Clean install script `install_clean_v31.sql` with all tables + indexes | `install_clean_v31.sql` |

### Previously resolved (v30 and earlier)

| ID | Description |
|---|---|
| CRIT-001 | Missing `vpn_manager.py` |
| CRIT-002 | Missing `build_language_url()` function |
| CRIT-003 | Race condition in URL dispatch — replaced with atomic CTE |
| CRIT-004 | Pool exhaustion — pool size caps with hard limit |
| CRIT-007 | Debug HTML file accumulation — age/size-based purge |
| HIGH-001 | Silent batch_size cap — replaced with explicit `ValueError` |
| HIGH-003 | Missing B-Tree index on `hotels.url` |
| HIGH-006 | `/health` returning HTTP 200 in degraded state (now 503) |
| HIGH-007 | VPN IP cache TTL too long (30s→5s) + explicit cache invalidation |
| HIGH-008 | Image download integrity check via `Pillow.Image.verify()` |
| HIGH-009 | `scrape_one()` session cleanup in `finally` block |
| HIGH-010 | Missing GIN index on `hotels.images_urls` |
| MED-011 | Database connection exponential backoff retry |
| LOW-006 | `print()` calls replaced with `logger.info()` |

---

## 7. Configuration Reference

All settings are managed via `app/.env.example` → copy to `app/.env` and fill in values.

### Critical settings

```env
# Database (required)
DB_PASSWORD=<your_postgres_password>

# Scraping
LANGUAGES_ENABLED=en,es,de,fr,it
USE_SELENIUM=True          # True=Brave browser, False=CloudScraper
DOWNLOAD_IMAGES=True

# VPN (optional)
VPN_ENABLED=False          # set True only with NordVPN installed
SCRAPER_MAX_WORKERS=1      # must be 1 when VPN_ENABLED=True

# Celery task limits (v31)
CELERY_TASK_SOFT_TIME_LIMIT=150
CELERY_TASK_TIME_LIMIT=180

# Redis circuit breaker (v31)
REDIS_FAILURE_THRESHOLD=5
REDIS_COOLDOWN_SECONDS=60

# Error storage
MAX_ERROR_LEN=2000
```

---

## 8. Installation — Windows 11

```batch
:: 1. Clone repository
git clone https://github.com/Aprendiz73/scrvIIpro26.git C:\BookingScraper
cd C:\BookingScraper

:: 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

:: 3. Install dependencies
pip install -r app\requirements.txt

:: 4. Configure environment
copy app\.env.example app\.env
:: Edit app\.env with your DB_PASSWORD and settings

:: 5. Create database (psql as postgres superuser)
psql -U postgres -c "CREATE DATABASE booking_scraper ENCODING='UTF8' TEMPLATE=template0;"
psql -U postgres -d booking_scraper -f app\install_clean_v31.sql

:: 6. Start services (Memurai/Redis must be running)
start_services.bat

:: 7. Load URLs
python -m app.load_urls app\urls_ejemplo.csv

:: 8. Access API
:: http://localhost:8000/docs
```

---

## 9. API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/health` | System health (200 OK / 503 degraded) |
| GET | `/metrics` | Performance counters (v31 NEW) |
| GET | `/stats` | Scraping statistics |
| GET | `/vpn/status` | VPN + circuit breaker state |
| POST | `/vpn/rotate` | Force VPN rotation |
| POST | `/scraping/upload-csv` | Upload URL CSV file |
| POST | `/scraping/force-now` | Force immediate dispatch |
| GET | `/docs` | Swagger UI |

---

## 10. Remaining Open Issues

| ID | Priority | Description |
|---|---|---|
| MED-012 | MEDIUM | Alembic migrations not automated (manual SQL scripts) |
| MED-015 | MEDIUM | No table partitioning on `scraping_logs` (needed >10M rows) |
| MED-018 | MEDIUM | No OpenTelemetry / distributed tracing |
| HIGH-011 | MEDIUM | Rate limiter is in-memory only (not distributed across workers) |
| HIGH-012 | LOW | `hotels.url_id` nullable FK — orphan records possible |
| HIGH-014 | LOW | `LANGUAGES_ENABLED` validated at startup but not at runtime reload |

---

*Report generated: 2026-03-05 | Audit cycle: v31 Enterprise*
