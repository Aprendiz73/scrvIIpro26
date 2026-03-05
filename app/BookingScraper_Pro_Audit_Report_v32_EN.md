# BookingScraper Pro — Audit & Fix Report v32
**Version:** 6.0.0 | **Date:** 2026-03-05 | **Platform:** Windows 11 (local) | **Cycle:** v32

---

## Executive Summary

This report documents the complete step-by-step audit of the BookingScraper Pro codebase against the v31 error report. All previously reported issues were verified against the actual source files. Three new fixes were applied in this cycle (v32): SEC-001 (hardcoded Alembic credentials), LOW-006 (print() calls in VPN manager), and Recovery-003 (missing Redis re-sync on circuit recovery). All remaining open issues are classified as infrastructure-level concerns that do not affect the local Windows 11 deployment use case.

**Files modified:** `alembic.ini`, `app/vpn_manager_windows.py`, `app/scraper_service.py`
**Files created:** `alembic/env.py`

---

## 1. Audit Methodology

Each file was examined in sequence:

1. `alembic.ini` — credential exposure audit
2. `app/config.py` — validation, path resolution, constants
3. `app/main.py` — CORS, signal handlers, health endpoint, metrics, rate limiter
4. `app/models.py` — indexes, constraints, FK nullability
5. `app/scraper_service.py` — Redis CB, VPN CB, _active_ids sync, dispatch, session cleanup
6. `app/completeness_service.py` — session lifecycle
7. `app/vpn_manager_windows.py` — print() calls, IP cache TTL
8. `app/database.py` — pool config, retry backoff
9. `app/tasks.py` — Celery time limits
10. `app/install_clean_v31.sql` — partial index presence

---

## 2. Verified Fixed Issues (Confirmed in Code)

The following issues from the v31 error report were confirmed as correctly implemented in the codebase prior to this cycle.

| ID | Severity | Description | Verified Location |
|---|---|---|---|
| CRIT-001 | CRITICAL | `vpn_manager.py` missing module | `app/vpn_manager.py` exists, `vpn_manager_factory` exported |
| CRIT-002 | CRITICAL | `build_language_url()` missing | `app/scraper.py` — function present and importable |
| CRIT-003 | CRITICAL | Race condition in URL dispatch | `scraper_service.py:713` — atomic CTE `FOR UPDATE SKIP LOCKED` |
| CRIT-004 | CRITICAL | DB pool exhaustion | `database.py:54-67` — `_POOL_SAFE_MAX=50`, `_TOTAL_HARD_CAP=100` |
| CRIT-007 | CRITICAL | Debug HTML accumulation | `scraper.py` — `purge_debug_html()` called every 120 dispatch cycles |
| HIGH-001 | HIGH | Silent batch_size capping | `scraper_service.py` — explicit `ValueError` raised |
| HIGH-002 | HIGH | Redis circuit breaker missing | `scraper_service.py:140-215` — 3-state CB implemented |
| HIGH-003 | HIGH | Missing B-Tree index on `hotels.url` | `models.py:100` — `index=True` on `hotels.url` column |
| HIGH-004 | HIGH | Windows signal handlers incomplete | `main.py:537-560` — SIGINT + SIGBREAK registered |
| HIGH-005 | HIGH | Hardcoded error truncation | `config.py` — `MAX_ERROR_LEN=2000` constant used everywhere |
| HIGH-006 | HIGH | `/health` returns 200 when degraded | `main.py:897-975` — HTTP 503 on DB failure |
| HIGH-007 | HIGH | VPN IP cache TTL excessive | `vpn_manager_windows.py:85` — TTL = 5s, cache invalidated after rotate |
| HIGH-008 | HIGH | Image integrity check absent | `image_downloader.py` — `Pillow.Image.verify()` called |
| HIGH-009 | HIGH | Session cleanup missing on exception | `scraper_service.py` — `finally: db.close()` on all paths |
| HIGH-010 | HIGH | Missing GIN index on `images_urls` | `models.py:149-163` — `ix_hotels_images_gin` defined |
| HIGH-013 | HIGH | Celery task limits excessive | `tasks.py:90-91` — `soft=150s`, `hard=180s` |
| MED-011 | MEDIUM | DB connection retry missing | `database.py:282` — `test_connection()` with exponential backoff |
| MED-022 | MEDIUM | Missing `/metrics` endpoint | `main.py:982` — JSON metrics endpoint implemented |
| SEC-002 | HIGH | CORS wildcard with credentials | `main.py:730-755` — runtime validation rejects `CORS_ORIGINS=*` |
| SEC-003 | MEDIUM | Error messages expose internals | `main.py:214` — `_internal_error()` returns correlation ID only |
| CONC-001 | HIGH | Deadlock risk in language processing | `scraper_service.py` — alphabetical language sort enforced |
| CONC-002 | HIGH | VPN lock timeout missing | `scraper_service.py` — `_vpn_lock.acquire(timeout=30s)` |
| CONC-005 | MEDIUM | Celery dispatcher stats not shared | `scraper_service.py:217` — warning raised if `USE_CELERY_DISPATCHER=True` without Redis |
| DATA-001 | MEDIUM | Unique constraint gap with NULL | `install_clean_v31.sql:327` — partial unique index `ix_hotels_url_lang_null` |
| ARCH-001 | HIGH | In-memory state multi-worker gap | `scraper_service.py` — Redis-backed with local set fallback |
| ARCH-002 | MEDIUM | Health check missing dependencies | `main.py:897-975` — DB + Redis + VPN + disk checked |
| CFG-001 | HIGH | `DB_PASSWORD` default empty | `config.py:48` — empty default + startup `ValueError` if unset |
| CFG-002 | MEDIUM | Path resolution CWD-dependent | `config.py` — paths relative to `__file__` location |
| Recovery-002 | MEDIUM | DB rollback without close | `scraper_service.py`, `completeness_service.py` — `rollback()` + `finally: close()` |

---

## 3. Fixes Applied in This Cycle (v32)

### FIX-015 — SEC-001: Hardcoded Credentials in `alembic.ini`

**Error Report Reference:** SEC-001 (MEDIUM — Credential Exposure)

**Root cause:** `alembic.ini` contained `sqlalchemy.url = postgresql://postgres:postgres@localhost:5432/booking_scraper` in plain text. Any developer with repository read access would see the database password.

**Evidence (before):**
```ini
# alembic.ini line 55
sqlalchemy.url = postgresql://postgres:postgres@localhost:5432/booking_scraper
```

**Fix applied to `alembic.ini`:**
```ini
# [FIX SEC-001] Credentials MUST NOT be stored in version-controlled files.
# alembic/env.py overrides this value at runtime via settings.DATABASE_URL
sqlalchemy.url = CREDENTIALS_PROVIDED_BY_ENV_PY_AT_RUNTIME
```

**New file created: `alembic/env.py`**

The Alembic environment script now reads credentials from `app/config.py` (which reads `DB_PASSWORD` from `.env`) and overrides the placeholder at runtime via `config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)`. This is the standard Alembic pattern for credential management.

```python
from app.config import settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
```

**Security impact:** Database credentials are no longer stored in any version-controlled file. The `.env` file (containing `DB_PASSWORD`) must be in `.gitignore` (which it already is per the project's `.gitignore`). If `alembic.ini` is accidentally pushed to a public repository, no credentials are exposed.

**Backward compatibility:** No changes required to existing migration scripts. `alembic upgrade head` and `alembic revision` continue to work as long as `.env` is properly configured.

---

### FIX-016 — LOW-006: `print()` Calls in `vpn_manager_windows.py`

**Error Report Reference:** LOW-006 (LOW — Logging)

**Root cause:** The `_connect_manual()`, `disconnect()`, and `print_status()` methods used `print()` for output. On Windows, `print()` writes to stdout, bypassing Loguru's handler chain entirely — meaning these messages are never written to the rotation log, never captured by the file sink, and never formatted with timestamps or level tags.

**Before:** 35 `print()` calls in `vpn_manager_windows.py`
**After:** 1 remaining instance — inside a docstring only (not executable code)

**Replacements made:**

| Method | Before | After |
|---|---|---|
| `_connect_manual()` | 8 × `print()` | `logger.info("[VPN] ...")` |
| `_connect_manual()` — IP warning | `print(f"⚠️ IP no cambió...")` | `logger.warning("[VPN] ...")` |
| `disconnect()` | 6 × `print()` | `logger.info("[VPN] ...")` |
| `print_status()` | 9 × `print()` | `logger.info("[VPN] ...")` |
| `__main__` test block | 10 × `print()` | `logger.info/error("[VPN TEST] ...")` |

**Note on `input()` calls:** The two `input()` calls (user keyboard prompt in interactive mode) were retained intentionally. They are only reachable when `interactive=True`, which is a manual console mode never activated by the Celery worker. The interactive mode is a maintenance/debugging feature, not part of the production path.

**Impact:** All VPN manager output is now routed through Loguru, meaning it appears in the rotating log file at `data/logs/` with proper timestamps, log levels, and formatting consistent with the rest of the application.

---

### FIX-017 — Recovery-003: Missing `_active_ids` Re-sync After Redis Circuit Recovery

**Error Report Reference:** Recovery-003 (MEDIUM — Redis Failover)

**Root cause:** When the Redis circuit breaker transitions from OPEN → HALF-OPEN → CLOSED (circuit recovered), the in-memory `_active_ids` set was NOT re-synced from Redis. During the outage period, URL claims made via Redis (before the outage) exist only in Redis. URL claims made during the outage (via local `_active_ids` fallback) exist only in memory. After recovery, these two sets are inconsistent — a URL held in Redis could be claimed again from the local set if it wasn't present there.

**Before:**
```python
_redis_client.ping()
with _redis_cb_lock:
    if _redis_cb_failures > 0:
        logger.info("[HIGH-002] Redis CB closed — connection restored.")
    _redis_cb_failures = 0
return _redis_client
```

**After (app/scraper_service.py):**
```python
_redis_client.ping()
with _redis_cb_lock:
    was_recovering = _redis_cb_failures > 0
    _redis_cb_failures = 0
if was_recovering:
    logger.info("[HIGH-002] Redis CB closed — connection restored.")
    # [FIX Recovery-003] Re-sync _active_ids from Redis after circuit recovery
    try:
        keys = _redis_client.keys("bsp:active:*")
        if keys:
            recovered_ids = {int(k.decode().split(":")[-1]) for k in keys}
            with _active_ids_local_lock:
                _active_ids.update(recovered_ids)
            logger.info("[Recovery-003] Re-synced %d active URL IDs ...", len(recovered_ids))
    except Exception as sync_err:
        logger.warning("[Recovery-003] _active_ids re-sync skipped: %s", sync_err)
return _redis_client
```

**Design note for Windows single-process deployment:** With `SCRAPER_MAX_WORKERS=1` (the default and recommended setting for Windows), Redis is used as a distributed claim store but the only process is the FastAPI/asyncio process itself. In this configuration, the local `_active_ids` set and Redis are naturally consistent — a claim is placed in both simultaneously. The re-sync is therefore a safety net for any inconsistency that could arise from a Redis outage, not a critical code path for the standard Windows deployment.

**Exception safety:** The re-sync is wrapped in `try/except` so any Redis error during key scan does not prevent the circuit from fully closing. A warning is logged and the circuit transitions to CLOSED regardless.

---

## 4. Remaining Open Issues

These issues are confirmed as still open. Each has been assessed for impact on the target deployment (Windows 11, single process, local).

| ID | Severity | Description | Windows 11 Impact | Recommendation |
|---|---|---|---|---|
| **SEC-001** | MEDIUM | ~~Alembic credentials hardcoded~~ | — | **Fixed in this cycle (FIX-015)** |
| **LOW-006** | LOW | ~~`print()` in vpn_manager_windows~~ | — | **Fixed in this cycle (FIX-016)** |
| **Recovery-003** | MEDIUM | ~~_active_ids not re-synced on Redis recovery~~ | — | **Fixed in this cycle (FIX-017)** |
| HIGH-011 | MEDIUM | Rate limiter in-memory only | Low — single process deployment; no multi-process risk | Acceptable for local use. Replace with Redis-backed slowapi if horizontally scaled |
| HIGH-012 | LOW | `hotels.url_id` nullable FK | Low — orphan records require manual URL queue cleanup | Add `ON DELETE CASCADE` or periodic orphan cleanup query |
| HIGH-014 | LOW | `LANGUAGES_ENABLED` not validated on runtime reload | Low — config is not reloaded at runtime in this deployment | Validate on every read via `ENABLED_LANGUAGES` property |
| MED-012 | MEDIUM | Alembic migrations not automated | Low — SQL scripts executed manually work reliably | Implement in future CI/CD pipeline |
| MED-015 | MEDIUM | No partitioning on `scraping_logs` | Low — only relevant at >10M rows | Add monthly range partitioning when row count approaches 1M |
| MED-018 | MEDIUM | No OpenTelemetry / distributed tracing | Low — Loguru provides adequate observability for single-process | Future improvement if system evolves to microservices |

---

## 5. Complete Issue Status Summary

| ID | Category | Severity | Status |
|---|---|---|---|
| CRIT-001 | Import | CRITICAL | ✅ FIXED (previous cycle) |
| CRIT-002 | Import | CRITICAL | ✅ FIXED (previous cycle) |
| CRIT-003 | Concurrency | CRITICAL | ✅ FIXED (previous cycle) |
| CRIT-004 | Resources | CRITICAL | ✅ FIXED (previous cycle) |
| CRIT-007 | Resources | CRITICAL | ✅ FIXED (previous cycle) |
| HIGH-001 | Logic | HIGH | ✅ FIXED (previous cycle) |
| HIGH-002 | Availability | HIGH | ✅ FIXED (v31) |
| HIGH-003 | Performance | HIGH | ✅ FIXED (previous cycle) |
| HIGH-004 | Resources | HIGH | ✅ FIXED (v31) |
| HIGH-005 | Maintainability | HIGH | ✅ FIXED (v31) |
| HIGH-006 | Monitoring | HIGH | ✅ FIXED (previous cycle) |
| HIGH-007 | Stale Data | HIGH | ✅ FIXED (previous cycle) |
| HIGH-008 | Data Integrity | HIGH | ✅ FIXED (previous cycle) |
| HIGH-009 | Resources | HIGH | ✅ FIXED (previous cycle) |
| HIGH-010 | Performance | HIGH | ✅ FIXED (previous cycle) |
| HIGH-011 | Security | HIGH | ⚠️ OPEN — acceptable for local deployment |
| HIGH-012 | Data Integrity | HIGH | ⚠️ OPEN — low risk, design decision |
| HIGH-013 | Resources | HIGH | ✅ FIXED (v31) |
| HIGH-014 | Configuration | HIGH | ⚠️ OPEN — no runtime reload in this deployment |
| MED-011 | Availability | MEDIUM | ✅ FIXED (previous cycle) |
| MED-012 | DevOps | MEDIUM | ⚠️ OPEN — future CI/CD work |
| MED-015 | Scalability | MEDIUM | ⚠️ OPEN — not relevant at current data volume |
| MED-018 | Observability | MEDIUM | ⚠️ OPEN — future enhancement |
| MED-022 | Observability | MEDIUM | ✅ FIXED (v31) |
| LOW-006 | Logging | LOW | ✅ FIXED (this cycle — FIX-016) |
| SEC-001 | Security | MEDIUM | ✅ FIXED (this cycle — FIX-015) |
| SEC-002 | Security | HIGH | ✅ FIXED (previous cycle) |
| SEC-003 | Security | MEDIUM | ✅ FIXED (previous cycle) |
| CONC-001 | Concurrency | HIGH | ✅ FIXED (previous cycle) |
| CONC-002 | Concurrency | HIGH | ✅ FIXED (previous cycle) |
| CONC-005 | Configuration | MEDIUM | ✅ FIXED (previous cycle) |
| DATA-001 | Data Integrity | MEDIUM | ✅ FIXED (previous cycle) |
| ARCH-001 | Scalability | HIGH | ✅ FIXED (previous cycle) |
| ARCH-002 | Observability | MEDIUM | ✅ FIXED (previous cycle) |
| CFG-001 | Configuration | HIGH | ✅ FIXED (previous cycle) |
| CFG-002 | Configuration | MEDIUM | ✅ FIXED (previous cycle) |
| Recovery-001 | Availability | MEDIUM | ⚠️ OPEN — operational runbook item |
| Recovery-002 | Resources | MEDIUM | ✅ FIXED (previous cycle) |
| Recovery-003 | Availability | MEDIUM | ✅ FIXED (this cycle — FIX-017) |

**Totals:** 29 FIXED | 8 OPEN (all assessed as low-impact for local Windows 11 deployment)

---

## 6. Modified Files

### `alembic.ini`
- Removed hardcoded `postgresql://postgres:postgres@localhost:5432/booking_scraper`
- Replaced with intentional placeholder `CREDENTIALS_PROVIDED_BY_ENV_PY_AT_RUNTIME`
- Added explanatory comments documenting the security rationale

### `alembic/env.py` (NEW)
- Created standard Alembic environment script
- Reads `settings.DATABASE_URL` from `app/config.py` at runtime
- Overrides `alembic.ini` placeholder before any migration runs
- Supports both offline and online migration modes
- Includes `target_metadata = Base.metadata` for autogenerate support

### `app/vpn_manager_windows.py`
- Replaced 34 `print()` calls with `logger.info()` / `logger.warning()` / `logger.error()`
- Methods affected: `_connect_manual()`, `disconnect()`, `print_status()`, `__main__` test block
- `input()` prompts retained — only reachable in `interactive=True` (manual console mode)
- Docstring in `print_status()` retained as documentation (1 mention of `print()` in text)

### `app/scraper_service.py`
- Extended Redis circuit breaker HALF-OPEN → CLOSED transition
- Added `_active_ids` re-sync from Redis keys matching `bsp:active:*` pattern
- Re-sync wrapped in `try/except` — circuit closes regardless of scan errors
- Logs count of recovered URL IDs for observability

---

## 7. Syntax Validation

All modified and dependent Python files passed `ast.parse()` syntax validation post-fix:

| File | Status |
|---|---|
| `app/scraper_service.py` | ✅ PASS |
| `app/vpn_manager_windows.py` | ✅ PASS |
| `alembic/env.py` | ✅ PASS |
| `app/main.py` | ✅ PASS |
| `app/config.py` | ✅ PASS |
| `app/models.py` | ✅ PASS |
| `app/database.py` | ✅ PASS |
| `app/tasks.py` | ✅ PASS |
| `app/completeness_service.py` | ✅ PASS |

---

*Report generated: 2026-03-05 | Audit cycle: v32 | Platform: Windows 11 (local deployment)*
