# BookingScraper Pro — Installation & Modification Report v33

**Version:** 6.0.0  
**Date:** 2026-03-05  
**Platform:** Windows 11 (local deployment, single-process)  
**Cycle:** v33 — Clean Install  
**Repository:** https://github.com/Aprendiz73/scrvIIpro26.git

---

## Table of Contents

1. [System Requirements](#1-system-requirements)
2. [Project File Structure](#2-project-file-structure)
3. [Clean Installation — Step by Step](#3-clean-installation--step-by-step)
4. [Configuration Reference (.env)](#4-configuration-reference-env)
5. [Database Setup](#5-database-setup)
6. [Starting and Stopping the Application](#6-starting-and-stopping-the-application)
7. [API Endpoints Reference](#7-api-endpoints-reference)
8. [Modifications Made (v30 → v33)](#8-modifications-made-v30--v33)
9. [Architecture Overview](#9-architecture-overview)
10. [Troubleshooting](#10-troubleshooting)

---

## 1. System Requirements

### Mandatory Software

| Component | Version | Notes |
|---|---|---|
| Windows 11 | 21H2 or later | 64-bit required |
| Python | 3.14.x | Standard GIL build from python.org |
| PostgreSQL | 14 or later | Local installation |
| Git | Any recent | For cloning repository |

### Optional Software

| Component | Purpose | Required When |
|---|---|---|
| Memurai / Redis for Windows | Task queue + state sharing | `USE_CELERY_DISPATCHER=True` or Redis-backed rate limiting |
| NordVPN (Windows client + CLI) | IP rotation during scraping | `VPN_ENABLED=True` |
| Brave Browser | Selenium automation | `USE_SELENIUM=True` |

### Minimum Hardware

| Resource | Minimum | Recommended |
|---|---|---|
| RAM | 4 GB | 8 GB |
| Disk | 10 GB free | 20 GB free |
| CPU | 2 cores | 4 cores |
| Network | Any broadband | Stable connection |

---

## 2. Project File Structure

```
C:\BookingScraper\                          ← Project root
│
├── .env                                    ← Your configuration (copy from .env.example)
├── .env.example                            ← Configuration template — ALL settings documented
├── .gitignore                              ← Excludes .env, venv, __pycache__, data/
│
├── alembic.ini                             ← Alembic config (credentials via env.py, NOT hardcoded)
│
├── alembic/
│   └── env.py                             ← Alembic runtime: reads DB_PASSWORD from .env
│
├── app/                                    ← Main application package
│   │
│   ├── main.py              (2,075 lines)  ← FastAPI app, lifespan, routes, rate limiter
│   ├── config.py            (407 lines)   ← Pydantic settings, all env vars, path resolution
│   ├── models.py            (339 lines)   ← SQLAlchemy ORM models + indexes
│   ├── database.py          (350 lines)   ← Connection pool, sessions, health check
│   │
│   ├── scraper_service.py   (1,494 lines) ← Orchestration: dispatch, VPN rotation, Redis CB
│   ├── scraper.py           (1,369 lines) ← Selenium/CloudScraper page fetch + parse
│   ├── extractor.py         (485 lines)   ← Data extraction from parsed HTML
│   ├── completeness_service.py (631 lines)← Language completeness tracking
│   ├── image_downloader.py  (324 lines)   ← Image download, resize, Pillow verify
│   │
│   ├── tasks.py             (231 lines)   ← Celery tasks (optional mode)
│   ├── celery_app.py        (103 lines)   ← Celery configuration (solo pool, Windows)
│   │
│   ├── vpn_manager.py       (78 lines)    ← VPN factory (platform router)
│   ├── vpn_manager_windows.py (762 lines) ← NordVPN Windows implementation
│   │
│   ├── install_clean_v31.sql (648 lines)  ← ⚠️ CLEAN INSTALL ONLY — drops and recreates all tables
│   │
│   ├── export_data.py                     ← CSV/JSON/Excel data export
│   ├── load_urls.py                       ← Bulk URL import from CSV
│   ├── create_tables.py                   ← Programmatic table creation (alternative to SQL)
│   ├── verify_system.py                   ← Startup system verification script
│   │
│   ├── requirements.txt                   ← Python dependencies (Python 3.14 compatible)
│   └── urls_ejemplo.csv                  ← Sample URL input file format
│
├── scripts/                               ← Utility scripts (duplicates of app/ scripts)
│   ├── __init__.py
│   ├── create_project_structure.py
│   ├── create_tables.py
│   ├── export_data.py
│   ├── load_urls.py
│   └── verify_system.py
│
├── data/                                  ← Created automatically at first run
│   ├── images/                            ← Downloaded hotel images
│   ├── exports/                           ← CSV/JSON/Excel exports
│   ├── logs/                              ← Rotating log files (api.log, max 10 × 50 MB)
│   └── debug_html/                        ← Temporary debug HTML (auto-purged after 24h)
│
├── inicio_rapido.bat                      ← Quick start: FastAPI only (recommended)
├── start_services.bat                     ← Full start: FastAPI + Celery worker + Beat
├── stop_services.bat / detener_todo.bat   ← Stop all processes
├── backup_db.bat                          ← PostgreSQL backup via pg_dump
├── limpiar_cache.bat                      ← Clear Python __pycache__
└── instalar_edge_driver.bat               ← Install Edge WebDriver (if using Edge)
```

> **Note on `alembic_env.py`:** The file downloaded as `alembic_env.py` must be placed at `C:\BookingScraper\alembic\env.py`. It is only used when running Alembic migration commands (`alembic upgrade head`). If you use `install_clean_v31.sql` for a fresh install, this file is not needed for normal operation.

---

## 3. Clean Installation — Step by Step

> ⚠️ **This is a CLEAN INSTALL guide.** It assumes an empty database. Do not run `install_clean_v31.sql` on a database that already has data — it will drop and recreate all tables.

### Step 1 — Clone the Repository

```bat
cd C:\
git clone https://github.com/Aprendiz73/scrvIIpro26.git BookingScraper
cd C:\BookingScraper
```

### Step 2 — Create Python Virtual Environment

```bat
cd C:\BookingScraper
python -m venv venv
```

Verify the Python version:
```bat
venv\Scripts\python.exe --version
```
Expected output: `Python 3.14.x`

### Step 3 — Install Python Dependencies

```bat
venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\python.exe -m pip install -r app\requirements.txt
```

> **Important for Python 3.14:** All packages in `requirements.txt` have been verified to have `cp314-win_amd64` or `abi3` wheels available. Do not downgrade versions — the pins are specific to Python 3.14 compatibility.

Expected install time: 3–8 minutes depending on network speed.

### Step 4 — Configure Environment

```bat
copy .env.example .env
notepad .env
```

**Minimum required settings to change:**

```ini
DB_PASSWORD=your_actual_postgres_password
API_KEY=any-strong-random-string-you-choose
```

All other settings have safe defaults for Windows 11 local deployment.

### Step 5 — Create PostgreSQL Database

Open **pgAdmin** or **psql** and run:

```sql
-- In psql or pgAdmin Query Tool:
CREATE DATABASE booking_scraper;
```

Then in a command prompt:

```bat
cd C:\BookingScraper
venv\Scripts\python.exe -c "from app.config import settings; print(settings.DATABASE_URL)"
```

This confirms your `.env` is being read correctly.

### Step 6 — Install Database Schema (Clean)

**Option A — Using psql command line:**
```bat
psql -U postgres -d booking_scraper -f app\install_clean_v31.sql
```

**Option B — Using pgAdmin:**
1. Open pgAdmin → connect to `booking_scraper` database
2. Tools → Query Tool
3. Open `app\install_clean_v31.sql`
4. Execute (F5)

Expected output: series of `CREATE TABLE`, `CREATE INDEX`, `CREATE FUNCTION`, `SELECT` statements without errors.

**What `install_clean_v31.sql` creates:**

| Object | Type | Notes |
|---|---|---|
| `url_queue` | Table | URL input queue with priority, retry logic |
| `hotels` | Table | Extracted hotel data (multi-language) |
| `url_language_status` | Table | Per-language scraping progress tracker |
| `scraping_logs` | Partitioned Table | Monthly range partitions (FIX-025) |
| `vpn_rotations` | Table | VPN rotation audit log |
| `system_metrics` | Table | CPU/memory/disk snapshots |
| `create_scraping_logs_partition()` | Function | PL/pgSQL partition management |
| 25+ indexes | Indexes | B-Tree, GIN, partial indexes |

### Step 7 — Verify Installation

```bat
cd C:\BookingScraper
venv\Scripts\python.exe app\verify_system.py
```

Expected output:
```
✓ Python 3.14.x
✓ All imports OK
✓ Database connection OK
✓ Tables verified
✓ System ready
```

### Step 8 — Load URLs

Prepare a CSV file (one URL per line, no header):

```
https://www.booking.com/hotel/es/hotel-name.en-gb.html
https://www.booking.com/hotel/fr/paris-hotel.en-gb.html
```

Load into the database:
```bat
venv\Scripts\python.exe app\load_urls.py --file urls_ejemplo.csv
```

### Step 9 — Start the Application

**Recommended mode (asyncio, no Celery required):**
```bat
inicio_rapido.bat
```
or manually:
```bat
cd C:\BookingScraper
venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The application will start and automatically begin scraping after a 5-second initialization delay.

Open your browser: **http://localhost:8000/docs**

---

## 4. Configuration Reference (.env)

### Critical Settings

| Variable | Default | Required | Description |
|---|---|---|---|
| `DB_PASSWORD` | *(empty)* | **YES** | PostgreSQL password — app refuses to start if empty |
| `API_KEY` | *(empty)* | Recommended | Protects `/scraping/force-now` and other write endpoints |

### Database

| Variable | Default | Description |
|---|---|---|
| `DB_HOST` | `localhost` | PostgreSQL host |
| `DB_PORT` | `5432` | PostgreSQL port |
| `DB_USER` | `postgres` | PostgreSQL user |
| `DB_NAME` | `booking_scraper` | Database name |
| `DB_POOL_SIZE` | `5` | Connections per process |
| `DB_MAX_OVERFLOW` | `5` | Extra connections during peak |
| `DB_TOTAL_HARD_CAP` | `50` | Max across all processes |

### Scraping Behaviour

| Variable | Default | Description |
|---|---|---|
| `USE_SELENIUM` | `False` | `True` = Brave/Chromium; `False` = CloudScraper |
| `SCRAPER_MAX_WORKERS` | `1` | **Must be 1 when VPN_ENABLED=True** |
| `LANGUAGES_ENABLED` | `en,es,de,fr,it` | Comma-separated ISO 639-1 codes |
| `DEFAULT_LANGUAGE` | `en` | Scraped first on each hotel |
| `BATCH_SIZE` | `5` | URLs dispatched per 30-second cycle |
| `MAX_RETRIES` | `3` | Max retry attempts per URL |
| `MIN_REQUEST_DELAY` | `2.0` | Minimum seconds between requests |
| `MAX_REQUEST_DELAY` | `5.0` | Maximum seconds between requests |

### VPN (Optional)

| Variable | Default | Description |
|---|---|---|
| `VPN_ENABLED` | `False` | Enable NordVPN rotation |
| `VPN_COUNTRIES` | `UK,US,CA,DE,FR,NL,IT,ES` | Rotation pool |
| `VPN_ROTATE_EVERY_N` | `10` | Hotels between rotations |
| `VPN_FAILOVER_TIMEOUT_SECS` | `90` | Seconds before degraded mode |

### New in v33

| Variable | Default | Description |
|---|---|---|
| `EXECUTOR_SHUTDOWN_TIMEOUT_SECS` | `30` | Seconds to wait for in-flight tasks during graceful shutdown (FIX-019) |

---

## 5. Database Setup

### Schema Overview

```
url_queue (input)
    │
    ├──→ hotels (output: hotel data per language)
    ├──→ url_language_status (progress per language)
    └──→ scraping_logs (audit — monthly partitioned)
             scraping_logs_2026_03   ← partition: March 2026
             scraping_logs_2026_04   ← partition: April 2026
             scraping_logs_2026_05   ← partition: May 2026
             ...

vpn_rotations   (VPN audit log)
system_metrics  (resource monitoring)
```

### Monthly Partition Management

The `scraping_logs` table uses monthly range partitioning (new in v33). Three partitions are created at install time (current month + 2 ahead). To create future partitions:

```sql
-- Run at the start of each new month
SELECT create_scraping_logs_partition(2026, 6);   -- June 2026
SELECT create_scraping_logs_partition(2026, 7);   -- July 2026
```

> **Tip:** Add this call to the existing `cleanup_old_logs` Celery task so partition creation happens automatically each month.

### PostgreSQL Recommended Settings

For local Windows 11 deployment, add to `postgresql.conf`:

```ini
max_connections = 50          # Enough for FastAPI + pgAdmin
shared_buffers = 256MB        # 25% of available RAM (for 4 GB system)
work_mem = 16MB               # Per-query sort/hash memory
maintenance_work_mem = 128MB  # VACUUM, CREATE INDEX
log_min_duration_statement = 1000  # Log queries slower than 1s
```

---

## 6. Starting and Stopping the Application

### Mode A — FastAPI Only (Recommended for Windows 11)

The built-in asyncio dispatcher runs inside the FastAPI process. **No Celery required.**

```bat
:: Start
inicio_rapido.bat

:: Or manually:
cd C:\BookingScraper
venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000

:: Stop: Ctrl+C in the console window
```

### Mode B — Full Stack (FastAPI + Celery + Beat)

Only needed when `USE_CELERY_DISPATCHER=True` and Memurai/Redis is running.

```bat
:: Start all services (opens 3 console windows)
start_services.bat

:: Stop all services
stop_services.bat
```

### Checking Application Health

```
http://localhost:8000/health        ← DB + Redis + VPN + disk status
http://localhost:8000/scraping/status  ← Active jobs, queue counts
http://localhost:8000/metrics       ← CPU, memory, pool stats
http://localhost:8000/docs          ← Interactive API documentation
```

---

## 7. API Endpoints Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | System health (DB, Redis, VPN, disk) |
| `GET` | `/scraping/status` | Active jobs, queue counts, VPN status |
| `GET` | `/metrics` | CPU, memory, DB pool, log stats |
| `GET` | `/hotels` | List scraped hotels (paginated) |
| `GET` | `/hotels/{id}` | Single hotel detail |
| `POST` | `/urls` | Add URLs to scraping queue |
| `POST` | `/scraping/force-now` | Trigger immediate dispatch (requires API_KEY) |
| `GET` | `/vpn/status` | VPN connection status |
| `POST` | `/vpn/rotate` | Manual VPN rotation (requires API_KEY) |
| `GET` | `/export` | Export data (CSV/JSON/Excel) |

---

## 8. Modifications Made (v30 → v33)

This section documents every fix applied across all audit cycles.

### v33 — This Cycle (8 fixes)

#### FIX-018 — Celery Retry Exponential Backoff
**File:** `app/tasks.py`  
**Problem:** `self.retry(exc=exc)` used a constant 60-second delay. After a database restart, all retrying tasks fired simultaneously (thundering herd), potentially overwhelming the just-recovered service.  
**Fix:** Exponential backoff formula `min(base × 2ⁿ, 3600)` where `n = self.request.retries`. Base is 60s for `process_pending_urls` and 300s for `cleanup_old_logs`.

```python
# Before
raise self.retry(exc=exc)

# After
_backoff = min(60 * (2 ** self.request.retries), 3600)
raise self.retry(exc=exc, countdown=_backoff)
```

---

#### FIX-019 — Graceful ThreadPoolExecutor Shutdown
**File:** `app/main.py`  
**Problem:** `_executor.shutdown(wait=False, cancel_futures=True)` in the lifespan shutdown abruptly cancelled in-flight scraping threads. Threads with open database transactions left `url_queue.status='processing'` locked until the next restart.  
**Fix:** Two-phase shutdown: (1) attempt graceful completion with 30-second timeout (`EXECUTOR_SHUTDOWN_TIMEOUT_SECS`), (2) force-cancel only if timeout expires, with an explanatory warning logged.

---

#### FIX-020 — VPN verify_vpn_active() TOCTOU Race
**File:** `app/vpn_manager_windows.py`  
**Problem:** `self.original_ip` was read without holding `_ip_cache_lock`. A concurrent `_detect_original_ip()` call during rotation could overwrite it between the null-check and the comparison, producing a false "VPN active" result.  
**Fix:** `original_ip` is now captured into a local variable under `_ip_cache_lock` at the top of `verify_vpn_active()`. All subsequent comparisons use the local copy.

---

#### FIX-021 — Log File Retention Ceiling
**File:** `app/main.py`  
**Problem:** `retention="7 days"` with `rotation="50 MB"` could accumulate 168+ rotation files (8.4 GB) during high-volume scraping.  
**Fix:** Changed to `retention=10` (keep last 10 rotated files). With `compression="gz"`, maximum disk usage for logs is ≤500 MB raw, ~50 MB compressed.

---

#### FIX-022 — Console Window Flash on VPN CLI Calls
**File:** `app/vpn_manager_windows.py`  
**Problem:** Every NordVPN CLI call (`subprocess.run()`) created a visible console window on Windows, causing disruptive flashes during background scraping.  
**Fix:** Added `_CREATE_NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)` and applied `creationflags=_CREATE_NO_WINDOW` to all 5 subprocess calls. On non-Windows platforms, the flag evaluates to 0 (no-op).

---

#### FIX-023 — Redis Degraded Mode Warning at Startup
**File:** `app/scraper_service.py`  
**Problem:** When Redis was unreachable, the system silently fell back to local in-memory `_active_ids` with no visible indication that it was running in degraded mode.  
**Fix:** Added an explicit `logger.warning()` at module startup when `_redis_client is None`, explaining the operational impact and providing remediation steps.

---

#### FIX-024 — Error Classification: Transient vs Fatal
**File:** `app/scraper_service.py`  
**Problem:** All scraping exceptions were logged at the same severity level and treated with identical retry logic. Transient network errors appeared as `ERROR` (alert fatigue), and fatal programming errors (ValueError) were retried uselessly.  
**Fix:** Added `_is_transient_error(exc)` and `_log_scrape_error()` helpers. Transient errors (ConnectionError, TimeoutError, network keywords) log as `WARNING`. Fatal errors (ValueError, TypeError, AttributeError) log as `ERROR` with full traceback.

---

#### FIX-025 — scraping_logs Monthly Range Partitioning
**File:** `app/install_clean_v31.sql`  
**Problem:** `scraping_logs` was a plain table. At expected volume (50K rows/day), it reaches 18M rows in one year. Timestamp-filtered queries required full table scan O(18M).  
**Fix:** Converted to `PARTITION BY RANGE (timestamp)` with monthly granularity. PostgreSQL partition pruning reduces scan to ≤2 partitions per query. `SERIAL PRIMARY KEY` replaced with `BIGSERIAL` + composite `PRIMARY KEY (id, timestamp)` (required by PostgreSQL partitioning rules). PL/pgSQL function `create_scraping_logs_partition(year, month)` manages partition creation. Three partitions pre-created at install time.

---

### v32 (3 fixes)

| Fix | Description |
|---|---|
| FIX-015 | Removed hardcoded credentials from `alembic.ini` — replaced with runtime override via `alembic/env.py` reading from `.env` |
| FIX-016 | Replaced 34 `print()` calls in `vpn_manager_windows.py` with `logger.info/warning/error()` — routes all output through Loguru's rotation pipeline |
| FIX-017 | Added `_active_ids` re-sync from Redis when circuit breaker recovers from OPEN → CLOSED — prevents double-claim risk after Redis outage |

---

### v31 (16 fixes)

| Fix | Description |
|---|---|
| BUG-001 | Added missing `vpn_manager.py` (factory module) — was causing `ImportError` at startup |
| BUG-002 | Windows keepalive via `SetThreadExecutionState` + watchdog coroutine — prevents screen-lock suspension |
| BUG-003 | Added `build_language_url()` to `scraper.py` — was causing `NameError` crashing all scraping |
| BUG-004 | Atomic CTE dispatch with `FOR UPDATE SKIP LOCKED` — eliminates TOCTOU race in URL selection |
| BUG-005 | Connection pool hard cap: `_POOL_SAFE_MAX=50`, `_TOTAL_HARD_CAP=100` |
| BUG-006 | `SCRAPER_MAX_WORKERS` from `.env` (configurable) |
| BUG-007 | Windows signal handlers: SIGINT + SIGBREAK registered with platform guard |
| BUG-008 | Redis circuit breaker (3-state: CLOSED/OPEN/HALF-OPEN) with 60s cooldown |
| BUG-009 | GIN index `ix_hotels_images_gin` on `images_urls` JSONB column |
| BUG-010 | Language mismatch retries now trigger VPN rotation |
| BUG-011 | VPN failover timeout with degraded-mode fallback |
| BUG-012 | VPN rotation stats exposed in `/scraping/status` API |
| BUG-013 | `DB_PASSWORD` validation at startup — refuses to start if empty |
| BUG-014 | Paths resolved relative to `config.py` location, not CWD |
| BUG-015 | Debug HTML auto-purge every 120 dispatch cycles |
| BUG-016 | Celery time limits: `soft=150s`, `hard=180s` (down from 600s) |

---

### v30 (previous cycles)

| Fix | Description |
|---|---|
| DATA-001 | Partial unique index for `(url, language)` when `url_id IS NULL` |
| HIGH-003 | B-Tree index on `hotels.url` |
| HIGH-006 | `/health` returns HTTP 503 on DB failure (was always 200) |
| HIGH-007 | VPN IP cache TTL = 5 seconds (was 300s — caused stale IP comparisons) |
| HIGH-008 | Image integrity check via `Pillow.Image.verify()` |
| HIGH-010 | `MAX_URL_LENGTH=512` aligned to `VARCHAR(512)` DB column |
| SEC-002 | CORS wildcard rejected at startup when `allow_credentials=True` |
| SEC-003 | Error responses return correlation ID only, never stack traces |
| CONC-001 | Languages sorted alphabetically to prevent deadlock |
| CONC-002 | `_vpn_lock.acquire(timeout=30)` — prevents indefinite blocking |
| MED-011 | DB connection retry with exponential backoff |
| MED-022 | `/metrics` JSON endpoint (CPU, memory, pool, disk) |
| Recovery-002 | `rollback()` + `finally: db.close()` on all DB error paths |
| ARCH-001 | `_active_ids` backed by Redis with local set fallback |
| ARCH-002 | Health check validates DB + Redis + VPN + disk |
| CFG-001 | `DB_PASSWORD` empty string rejected at startup |

---

## 9. Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    Windows 11 Process                    │
│                                                         │
│  ┌──────────────┐    ┌───────────────────────────────┐  │
│  │   FastAPI    │    │     asyncio auto-dispatcher   │  │
│  │  (uvicorn)   │    │   (every 30 seconds)          │  │
│  │              │    │   process_batch(batch_size=5) │  │
│  │  REST API    │    └───────────────┬───────────────┘  │
│  │  /health     │                   │                   │
│  │  /hotels     │    ┌──────────────▼──────────────┐   │
│  │  /urls       │    │     scraper_service.py       │   │
│  │  /metrics    │    │  ┌─────────────────────────┐ │   │
│  └──────────────┘    │  │  ThreadPoolExecutor     │ │   │
│                       │  │  max_workers=1          │ │   │
│                       │  │  (Windows: sequential)  │ │   │
│                       │  └──────────┬──────────────┘ │   │
│                       │             │                 │   │
│                       │  ┌──────────▼──────────────┐ │   │
│                       │  │     BookingScraper       │ │   │
│                       │  │  (Selenium OR            │ │   │
│                       │  │   CloudScraper)          │ │   │
│                       │  └─────────────────────────┘ │   │
│                       └──────────────────────────────┘   │
│                                                         │
│  ┌───────────────┐    ┌───────────────┐                  │
│  │  PostgreSQL   │    │  Redis/       │                  │
│  │  (local)      │    │  Memurai      │                  │
│  │               │    │  (optional)   │                  │
│  │  url_queue    │    │  _active_ids  │                  │
│  │  hotels       │    │  rate limits  │                  │
│  │  scraping_logs│    └───────────────┘                  │
│  └───────────────┘                                       │
└─────────────────────────────────────────────────────────┘
```

**Key Design Decisions for Windows 11:**

- `SCRAPER_MAX_WORKERS=1`: NordVPN account allows one active connection; serialized scraping avoids VPN race conditions
- `Celery solo pool`: Python's `multiprocessing` on Windows requires `spawn` mode (no `fork`); solo pool avoids all related issues
- `asyncio dispatcher`: Built into the FastAPI process — no separate Celery worker needed for standard operation
- `Redis optional`: The system runs fully without Redis; Redis adds distributed claim tracking and rate limiting for potential future multi-process setups

---

## 10. Troubleshooting

### Application won't start

**Symptom:** `ValueError: DB_PASSWORD is required`  
**Fix:** Set `DB_PASSWORD=your_password` in `.env`

**Symptom:** `ImportError: No module named 'app.vpn_manager'`  
**Fix:** Verify `app/vpn_manager.py` exists in the repository. Run `git pull` to sync latest code.

**Symptom:** `ModuleNotFoundError` for any package  
**Fix:** Activate venv and reinstall: `venv\Scripts\python.exe -m pip install -r app\requirements.txt`

---

### Database errors

**Symptom:** `connection pool exhausted`  
**Fix:** Reduce `DB_POOL_SIZE` and `DB_MAX_OVERFLOW` in `.env`, or increase PostgreSQL `max_connections`

**Symptom:** `relation "scraping_logs" does not exist`  
**Fix:** Run `install_clean_v31.sql` on the database

**Symptom:** `no partition of relation "scraping_logs" found for row`  
**Fix:** Create the missing partition: `SELECT create_scraping_logs_partition(YEAR, MONTH);`

---

### Scraping issues

**Symptom:** All URLs stuck in `processing` state  
**Fix 1:** Restart the application (startup reset moves `processing` → `pending` with retry count increment)  
**Fix 2:** Manual reset: `UPDATE url_queue SET status='pending', retry_count=0 WHERE status='processing';`

**Symptom:** URLs reaching `failed` status immediately  
**Fix:** Check `last_error` column: `SELECT url, last_error FROM url_queue WHERE status='failed' LIMIT 10;`

**Symptom:** Selenium browser not opening  
**Fix:** Set `BROWSER_BRAVE_PATH=C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe` in `.env`

---

### VPN issues

**Symptom:** Console windows flashing during VPN operations  
**Status:** Fixed in v33 (FIX-022) — `CREATE_NO_WINDOW` flag applied to all subprocess calls

**Symptom:** VPN rotation appears to not change IP  
**Fix 1:** Check `VPN_COUNTRIES` list has at least 2 countries  
**Fix 2:** Check VPN IP cache: `GET /vpn/status`  
**Fix 3:** Manual rotation: `POST /vpn/rotate` (requires API_KEY header)

---

### Log management

**Symptom:** `data/logs/` consuming too much disk space  
**Status:** Fixed in v33 (FIX-021) — `retention=10` caps log files at 10 × 50 MB = 500 MB max  
**Manual cleanup:** Delete files in `data/logs/` older than desired retention period

---

*Report generated: 2026-03-05 | Cycle: v33 | Platform: Windows 11 (local) | Fresh install*
