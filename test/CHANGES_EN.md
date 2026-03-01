# BookingScraper Pro — Bug Fix Report

**Project:** BookingScraper Pro  
**Codebase version reviewed:** v6.0 (scraper_service)  
**Review date:** February 2026  
**Bugs fixed:** 11 of 11  
**Files modified:** 7  

---

## Summary Table

| ID | Severity | File | Title | Status |
|----|----------|------|-------|--------|
| BUG-01 | HIGH | `main.py` | Invalid CORS: wildcard + credentials | ✅ Fixed |
| BUG-02 | HIGH | `database.py` + `models.py` | Dual ORM Base — tables not created | ✅ Fixed |
| BUG-03 | MEDIUM | `scraper_service.py` + `image_downloader.py` | `images_local` never updated after download | ✅ Fixed |
| BUG-04 | MEDIUM | `main.py` | Startup reset causes infinite retry loop | ✅ Fixed |
| BUG-05 | MEDIUM | `main.py` | Wrong version in root endpoint | ✅ Fixed |
| BUG-06 | MEDIUM | `config.py` + `main.py` | `create_directories()` at module import time | ✅ Fixed |
| BUG-07 | LOW | `models.py` | `datetime.utcnow()` deprecated in Python 3.12+ | ✅ Fixed |
| BUG-08 | LOW | `vpn_manager.py` | `IndexError` in `rotate()` on empty country list | ✅ Fixed |
| BUG-09 | LOW | `scraper_service.py` | No `SELECT FOR UPDATE SKIP LOCKED` — race condition | ✅ Fixed |
| BUG-10 | LOW | `main.py` | Deprecated `_normalize_booking_url()` silently returns invalid URLs | ✅ Fixed |
| BUG-11 | LOW | `config.py` + `main.py` | Dual dispatcher (asyncio + Celery beat) without coordination | ✅ Fixed |

---

## Detailed Changes

---

### BUG-01 — CORS: Invalid wildcard origin + credentials

**Severity:** HIGH  
**File:** `main.py`  
**Location:** `CORSMiddleware` configuration

**Problem:**  
`CORSMiddleware` was configured with `allow_origins=['*']` and `allow_credentials=True` simultaneously. The W3C CORS specification explicitly prohibits this combination. Browsers (Chrome, Firefox, Edge) reject all credentialed responses with a wildcard origin. The server returned HTTP 200 but the browser silently blocked the response.

**Fix applied:**
```python
# BEFORE — invalid per spec
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, ...)

# AFTER — explicit origin list from environment variable
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:8080").split(","),
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "X-Requested-With"],
)
```

**Impact of fix:** Frontend requests with credentials (cookies, Authorization headers) now work correctly. Set `CORS_ORIGINS` in `.env` for production.

---

### BUG-02 — Dual ORM Base: tables silently not created

**Severity:** HIGH  
**Files:** `database.py`, `models.py`  
**Location:** `declarative_base()` — both files

**Problem:**  
Both `database.py` and `models.py` declared their own `Base = declarative_base()`. These were two separate, incompatible SQLAlchemy `MetaData` instances. Calling `Base.metadata.create_all(engine)` from `database.py` did not create any table defined in `models.py`. The failure was completely silent — no exception, just missing tables at runtime.

**Fix applied:**
```python
# BEFORE — database.py had its own empty Base
from sqlalchemy.orm import declarative_base
Base = declarative_base()   # ← incompatible with models.py

# AFTER — import the single authoritative Base from models.py
from app.models import Base  # noqa: F401 — re-exported for compatibility
# declarative_base() call removed from database.py entirely
```

**Impact of fix:** `Base.metadata.create_all(engine)` now creates all tables defined in `models.py`. Eliminates silent migration failures on new deployments.

---

### BUG-03 — `images_local` never updated after download

**Severity:** MEDIUM  
**Files:** `scraper_service.py`, `image_downloader.py`  
**Location:** image download block in `scrape_one()` + `ImageDownloader`

**Problem:**  
The `hotels` INSERT set `images_count=0` explicitly. After `_download_images()` ran, `images_count` was updated but `images_local` (the list of local file paths) was never written to the database. It remained `NULL` permanently, making it impossible to know which files were saved on disk.

**Fix applied in `image_downloader.py`:**
```python
@staticmethod
def get_local_paths(hotel_id: int, lang: str = "en") -> List[str]:
    """Returns list of local image file paths for a given hotel."""
    base = Path(settings.IMAGES_PATH) / f"hotel_{hotel_id}" / lang
    if not base.exists():
        return []
    extensions = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tiff"}
    return [str(f) for f in sorted(base.rglob("*")) if f.is_file() and f.suffix.lower() in extensions]
```

**Fix applied in `scraper_service.py`:**
```python
# BEFORE — only images_count updated
db.execute(text("UPDATE hotels SET images_count = :count, updated_at = NOW() WHERE ..."), ...)

# AFTER — both images_count AND images_local updated
local_paths = ImageDownloader.get_local_paths(url_id, lang=DEFAULT)
db.execute(text("""
    UPDATE hotels
    SET images_count = :count,
        images_local = CAST(:local_paths AS jsonb),
        updated_at   = NOW()
    WHERE url_id = :url_id AND language = :lang
"""), {"count": n_downloaded, "local_paths": json.dumps(local_paths), ...})
```

**Impact of fix:** `images_local` is now correctly populated with local file paths after every successful image download batch.

---

### BUG-04 — Startup reset causes infinite retry loop on permanent failures

**Severity:** MEDIUM  
**File:** `main.py`  
**Location:** `lifespan()` — startup reset block

**Problem:**  
On startup, the lifespan reset **all** `status='failed'` URLs back to `pending` with `retry_count=0`. This included permanently failed URLs (hotel removed from Booking.com, invalid content, unreachable domain). On every restart, the system re-enqueued and re-processed URLs that would always fail, wasting resources indefinitely.

**Fix applied:**
```python
# BEFORE — resets ALL failed URLs unconditionally
UPDATE url_queue SET status='pending', retry_count=0, last_error=NULL
WHERE status='failed'

# AFTER — only resets transient failures (retries still available)
UPDATE url_queue SET status='pending', updated_at=NOW()
WHERE status='failed' AND retry_count < max_retries
```

**Impact of fix:** URLs that have exhausted their retry budget remain in permanent `failed` state across restarts. Only truly transient failures are re-queued.

---

### BUG-05 — Wrong version returned by root endpoint

**Severity:** MEDIUM  
**File:** `main.py`  
**Location:** `GET /` — `root()` function

**Problem:**  
The root endpoint returned `"version": "3.0.0"` hardcoded. The application is v4.0.0 (confirmed by the FastAPI constructor, module docstring, and new v4.0 endpoints). The value also differed from `APP_VERSION` in `settings`.

**Fix applied:**
```python
# BEFORE
return {"app": "BookingScraper Pro", "version": "3.0.0", ...}

# AFTER — single source of truth
return {"app": settings.APP_NAME, "version": settings.APP_VERSION, ...}
```

**Impact of fix:** Version consistency across the API, configuration, and monitoring systems.

---

### BUG-06 — `create_directories()` runs at module import time

**Severity:** MEDIUM  
**Files:** `config.py`, `main.py`  
**Location:** Module-level call at end of `config.py`

**Problem:**  
`create_directories()` was called automatically every time `config.py` was imported. If the process lacked write permission on `C:\BookingScraper\` (CI environment, container, restricted user), `os.makedirs` raised `PermissionError` and the entire import failed — preventing the server from starting at all.

**Fix applied in `config.py`:**
```python
# BEFORE — automatic execution at import
create_directories()   # ← runs on every import

# AFTER — call removed from module level entirely
# [FIX BUG-06] create_directories() is now called from main.py lifespan only.
```

**Fix applied in `main.py` lifespan:**
```python
try:
    from app.config import create_directories
    create_directories()
    logger.info("✓ Data directories verified/created")
except PermissionError as _dir_err:
    logger.warning(f"⚠️ Could not create data directories: {_dir_err}. "
                   "Image downloads will fail if path doesn't exist.")
```

**Impact of fix:** Server starts successfully even without write access to data paths. A warning is logged but startup is not blocked.

---

### BUG-07 — `datetime.utcnow()` deprecated in Python 3.12+

**Severity:** LOW  
**File:** `models.py`  
**Location:** `Column` defaults in `URLQueue`, `Hotel`, `ScrapingLog`, `VPNRotation`, `SystemMetrics`

**Problem:**  
All timestamp columns used `default=datetime.utcnow`. `datetime.utcnow()` was deprecated in Python 3.12 (PEP 615) and generates `DeprecationWarning`. The project uses Python 3.14.3 where the warning is active. The function will be removed in a future Python version.

**Fix applied:**
```python
# BEFORE — deprecated in Python 3.12+
from datetime import datetime
created_at = Column(DateTime, default=datetime.utcnow)
updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# AFTER — SQLAlchemy 2.0 + Python 3.12+ correct approach
from sqlalchemy import func
created_at = Column(DateTime(timezone=True), server_default=func.now())
updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
```

**Impact of fix:** Eliminates deprecation warnings on every application startup. Timestamps are now timezone-aware and generated by PostgreSQL server clock (more accurate in distributed scenarios).

---

### BUG-08 — `IndexError` in `vpn_manager.rotate()` on empty country list

**Severity:** LOW  
**File:** `vpn_manager.py`  
**Location:** `NordVPNManager.rotate()` — `random.choice()` call

**Problem:**  
If `self.countries` was empty (misconfiguration in `VPN_COUNTRIES`) and `rotate()` was called, `random.choice([])` raised an uncaught `IndexError` that propagated through the scraping thread, potentially interrupting active scraping.

**Fix applied:**
```python
# BEFORE — potential IndexError if countries list is empty
available = [c for c in self.countries if c != self.current_server]
new_country = random.choice(available) if available else random.choice(self.countries)

# AFTER — explicit guards with clear error message
available = [c for c in self.countries if c != self.current_server]
if not available:
    available = list(self.countries)   # fallback: retry any country
if not available:
    logger.error("✗ VPN_COUNTRIES is empty — cannot rotate. Check .env configuration.")
    return False
new_country = random.choice(available)
```

**Impact of fix:** Graceful failure with a clear error message instead of an uncaught `IndexError`. VPN rotation failure is logged and the scraping thread continues.

---

### BUG-09 — Race condition in dispatch: missing `SELECT FOR UPDATE SKIP LOCKED`

**Severity:** LOW  
**File:** `scraper_service.py`  
**Location:** `process_batch()` — SELECT query

**Problem:**  
URL dispatch used two separate database operations: `SELECT id ... WHERE status='pending'` followed by `UPDATE status='processing'`. Between these two operations, another process (Celery beat or a second worker) could select the same URLs. The in-memory `_active_ids` set only prevented duplicates within the same process, not across separate processes.

**Fix applied:**
```python
# BEFORE — two non-atomic operations, race condition possible
SELECT id FROM url_queue WHERE status = 'pending' ... LIMIT :limit

# AFTER — atomic, safe for multi-process environments
SELECT id FROM url_queue
WHERE status = 'pending' AND retry_count < max_retries
ORDER BY priority DESC, created_at ASC
LIMIT :limit
FOR UPDATE SKIP LOCKED   -- PostgreSQL-level mutual exclusion
```

**Impact of fix:** PostgreSQL guarantees that each row is selected by exactly one process. Other processes skip locked rows (`SKIP LOCKED`) and take different URLs from the pool, eliminating double-processing.

---

### BUG-10 — Deprecated `_normalize_booking_url()` silently returns invalid URLs

**Severity:** LOW  
**File:** `main.py`  
**Location:** `_normalize_booking_url()` function

**Problem:**  
The deprecated function returned `url.strip()` (the original unmodified URL) when validation failed, without any indication of failure. Any caller using this function instead of `validate_and_normalize_booking_url()` could silently insert invalid URLs into the database.

**Fix applied:**
```python
# BEFORE — silent invalid URL return
def _normalize_booking_url(url: str) -> str:
    result = validate_and_normalize_booking_url(url)
    if result.is_valid:
        return result.canonical_url
    return url.strip()   # ← silently returns invalid URL

# AFTER — DeprecationWarning + ValueError on invalid URL
def _normalize_booking_url(url: str) -> str:
    warnings.warn(
        "_normalize_booking_url() is deprecated since v3.0. "
        "Use validate_and_normalize_booking_url() instead.",
        DeprecationWarning, stacklevel=2,
    )
    result = validate_and_normalize_booking_url(url)
    if not result.is_valid:
        raise ValueError(f"Invalid URL: {result.rejection_reason}")
    return result.canonical_url
```

**Impact of fix:** Callers are explicitly warned about the deprecated function and receive a `ValueError` on invalid URLs instead of silently getting corrupted data.

---

### BUG-11 — Dual dispatcher without inter-process coordination

**Severity:** LOW  
**Files:** `config.py`, `main.py`  
**Location:** `beat_schedule` in `celery_app.py` + `_auto_dispatch_loop()` in `main.py`

**Problem:**  
The system had two independent dispatch mechanisms both active simultaneously: (1) the asyncio auto-dispatcher in `main.py` calling `process_batch()` every 30 seconds, and (2) Celery beat executing `process_pending_urls` every 30 seconds. Combined with BUG-09 (no `SELECT FOR UPDATE`), this caused double-processing of URLs and rendered throttling settings ineffective.

**Fix applied in `config.py`:**
```python
# New flag — controls which dispatcher is active
USE_CELERY_DISPATCHER: bool = False
# False = asyncio auto-dispatcher in main.py (default, no Celery needed)
# True  = Celery beat (set when running with Celery infrastructure)
```

**Fix applied in `main.py` lifespan:**
```python
# BEFORE — asyncio dispatcher always started unconditionally
_dispatch_task = asyncio.create_task(_auto_dispatch_loop())

# AFTER — only one dispatcher active at a time
if not settings.USE_CELERY_DISPATCHER:
    _dispatch_task = asyncio.create_task(_auto_dispatch_loop())
    logger.info("Auto-dispatcher asyncio activated")
else:
    logger.info("Dispatch delegated to Celery beat (USE_CELERY_DISPATCHER=True)")
```

**Impact of fix:** Only one dispatch mechanism runs at any time. Set `USE_CELERY_DISPATCHER=True` in `.env` when running Celery beat infrastructure.

---

## Modified Files

| File | Bugs Fixed | Change Type |
|------|-----------|-------------|
| `main.py` | BUG-01, BUG-04, BUG-05, BUG-06, BUG-10, BUG-11 | Multiple fixes |
| `config.py` | BUG-06, BUG-11 | Remove module-level call; add `USE_CELERY_DISPATCHER` |
| `database.py` | BUG-02 | Remove duplicate `Base`; import from `models.py` |
| `models.py` | BUG-07 | Replace `datetime.utcnow` with `server_default=func.now()` |
| `scraper_service.py` | BUG-03, BUG-09 | Update `images_local`; add `FOR UPDATE SKIP LOCKED` |
| `image_downloader.py` | BUG-03 | Add `get_local_paths()` static method |
| `vpn_manager.py` | BUG-08 | Add empty-list guard in `rotate()` |

**Unchanged files:** `scraper.py`, `extractor.py`, `completeness_service.py`, `celery_app.py`, `vpn_manager_windows.py`, `__init__.py`

---

## Environment Variables Added

| Variable | Default | Description |
|----------|---------|-------------|
| `CORS_ORIGINS` | `http://localhost:3000,http://localhost:8080` | Comma-separated list of allowed frontend origins |
| `USE_CELERY_DISPATCHER` | `False` | `True` to use Celery beat; `False` for asyncio dispatcher |

---

## Verification Checklist

- [x] **BUG-01:** `allow_origins` reads from `CORS_ORIGINS` env var; no wildcard with credentials
- [x] **BUG-02:** `database.py` imports `Base` from `models.py`; no duplicate `declarative_base()`
- [x] **BUG-03:** `images_local` updated via `get_local_paths()` in both scraping code paths
- [x] **BUG-04:** Startup reset SQL filtered by `retry_count < max_retries`
- [x] **BUG-05:** Root endpoint returns `settings.APP_VERSION` instead of `"3.0.0"`
- [x] **BUG-06:** `create_directories()` removed from `config.py` module level; called in lifespan with `try/except`
- [x] **BUG-07:** Zero `datetime.utcnow` usages in column definitions; all replaced with `server_default=func.now()`
- [x] **BUG-08:** `rotate()` checks `if not available` before `random.choice()` with clear error message
- [x] **BUG-09:** `process_batch()` SELECT includes `FOR UPDATE SKIP LOCKED`
- [x] **BUG-10:** `_normalize_booking_url()` emits `DeprecationWarning` and raises `ValueError` on invalid URL
- [x] **BUG-11:** `USE_CELERY_DISPATCHER` flag controls which dispatcher is active; asyncio loop only starts when `False`

---

*Report generated: February 2026 | BookingScraper Pro — Static Code Analysis & Bug Fix Audit*
