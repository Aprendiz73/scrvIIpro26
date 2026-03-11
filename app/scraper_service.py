"""
scraper_service.py — BookingScraper Pro v49
Fixes applied:
  BUG-104 / SCRAP-CON-003: Redis uses a shared connection pool, not per-call new conn.
  SCRAP-BUG-016          : max_workers validated at runtime, not just at config load.
  SCRAP-BUG-017          : Timeout configurable via settings, not hardcoded.
  SCRAP-COMP-003         : High-complexity methods decomposed into helpers.
  VPN-FIX-001            : VPN wired into ScraperService — connect() before batch,
                           rotate() on scrape failure via should_rotate().
  VPN-FIX-002            : Startup diagnostic log shows VPN/Headless config clearly.

New in v49:
  BUG-DESC-001/002       : Thread-safe CloudScraperEngine + SeleniumEngine (scraper.py).
  BUG-IMG-401            : Image URLs preserve ?k= auth token (scraper.py).
  NEW-PHOTOS-001         : _scrape_language() uses download_photo_batch() when rich
                           hotelPhotos JS metadata is available; falls back to
                           download_batch() for URL-only list.

Platform: Windows 11 / ThreadPoolExecutor (not ProcessPoolExecutor).
"""

from __future__ import annotations

import logging
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError as FuturesTimeout
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

import redis as redis_lib

from app.config import get_settings
from app.database import get_db
from app.extractor import HotelExtractor, detect_language
from app.models import Hotel, ScrapingLog, URLLanguageStatus, URLQueue
from app.scraper import CloudScraperEngine, SeleniumEngine, build_language_url
from app.vpn_manager_windows import get_vpn_manager

# BUG-IMG-001 FIX: ImageDownloader was never imported — _ImageDownloader was always
# undefined, making the `if _ImageDownloader is not None` guard permanently False.
# No images were ever downloaded and no image_downloads rows were ever written.
try:
    from app.image_downloader import ImageDownloader as _ImageDownloader
except ImportError:
    _ImageDownloader = None  # type: ignore[assignment,misc]

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Module-level VPN manager (singleton — initialised once per worker process)
# ---------------------------------------------------------------------------
_vpn_manager = None
_vpn_manager_lock = threading.Lock()


def _get_vpn():
    """Return (or create) the module-level VPN manager."""
    global _vpn_manager
    if _vpn_manager is None:
        with _vpn_manager_lock:
            if _vpn_manager is None:
                _vpn_manager = get_vpn_manager()
    return _vpn_manager


# ---------------------------------------------------------------------------
# Shared Redis connection pool — BUG-104 fix
# ---------------------------------------------------------------------------
_redis_pool: Optional[redis_lib.ConnectionPool] = None
_redis_pool_lock = threading.Lock()


def _get_redis_pool() -> Optional[redis_lib.ConnectionPool]:
    """Return (or create) the shared Redis connection pool."""
    global _redis_pool
    if _redis_pool is None:
        with _redis_pool_lock:
            if _redis_pool is None:  # double-checked locking
                try:
                    cfg = get_settings()
                    _redis_pool = redis_lib.ConnectionPool.from_url(
                        cfg.REDIS_URL,
                        max_connections=cfg.REDIS_MAX_CONNECTIONS,
                        decode_responses=True,
                        socket_connect_timeout=3,
                        socket_timeout=3,
                    )
                    logger.info("Redis connection pool created: max_connections=%d", cfg.REDIS_MAX_CONNECTIONS)
                except Exception as exc:
                    logger.warning("Could not create Redis pool: %s", exc)
    return _redis_pool


def _get_redis_client() -> Optional[redis_lib.Redis]:
    """Return a Redis client backed by the shared pool."""
    pool = _get_redis_pool()
    if pool:
        return redis_lib.Redis(connection_pool=pool)
    return None


# ---------------------------------------------------------------------------
# Distributed URL lock via Redis SET NX
# ---------------------------------------------------------------------------

def _try_claim_url(url_id: str) -> bool:
    """Attempt to claim a URL for processing via Redis SET NX."""
    try:
        r = _get_redis_client()
        if r:
            key = f"url_lock:{url_id}"
            cfg = get_settings()
            timeout = cfg.SCRAPER_REQUEST_TIMEOUT * cfg.MAX_RETRIES * 3
            return bool(r.set(key, "1", nx=True, ex=timeout))
    except Exception as exc:
        logger.debug("Redis claim failed for %s: %s — proceeding without distributed lock.", url_id, exc)
    return True  # Fallback: allow processing if Redis unavailable


def _release_url(url_id: str) -> None:
    """Release a URL lock from Redis."""
    try:
        r = _get_redis_client()
        if r:
            r.delete(f"url_lock:{url_id}")
    except Exception as exc:
        logger.debug("Redis release failed for %s: %s", url_id, exc)


# ---------------------------------------------------------------------------
# Stats (protected by lock)
# ---------------------------------------------------------------------------

class _Stats:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self.processed = 0
        self.succeeded = 0
        self.failed = 0
        self.skipped = 0

    def record(self, *, succeeded: bool = False, failed: bool = False, skipped: bool = False) -> None:
        with self._lock:
            self.processed += 1
            if succeeded:
                self.succeeded += 1
            elif failed:
                self.failed += 1
            elif skipped:
                self.skipped += 1

    def to_dict(self) -> Dict[str, int]:
        with self._lock:
            return {
                "processed": self.processed,
                "succeeded": self.succeeded,
                "failed": self.failed,
                "skipped": self.skipped,
            }


# ---------------------------------------------------------------------------
# ScraperService
# ---------------------------------------------------------------------------

class ScraperService:
    """
    Orchestrates URL scraping with worker pool, VPN rotation, and DB persistence.
    Windows 11: uses ThreadPoolExecutor (not multiprocessing) for I/O-bound tasks.
    """

    def __init__(self) -> None:
        self._cfg = get_settings()
        self._cloud_engine = CloudScraperEngine()
        self._selenium_engine = SeleniumEngine()
        self._stats = _Stats()
        # VPN-FIX-001: initialise VPN manager (NullVPNManager when VPN_ENABLED=False)
        self._vpn = _get_vpn()
        # VPN-FIX-002: diagnostic log — always visible in Celery Worker on startup
        logger.info(
            "ScraperService INIT | VPN_ENABLED=%s | HEADLESS_BROWSER=%s | "
            "workers=%d | languages=%s | vpn_interval=%ds | vpn_countries=%s",
            self._cfg.VPN_ENABLED,
            self._cfg.HEADLESS_BROWSER,
            self._cfg.SCRAPER_MAX_WORKERS,
            ",".join(self._cfg.ENABLED_LANGUAGES),
            self._cfg.VPN_ROTATION_INTERVAL,
            ",".join(self._cfg.VPN_COUNTRIES) if self._cfg.VPN_ENABLED else "N/A",
        )

    # ── Public API ────────────────────────────────────────────────────────────

    def dispatch_batch(
        self,
        url_ids: Optional[List[str]] = None,
        max_workers: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Dispatch a batch of scraping jobs.
        SCRAP-BUG-016: max_workers clamped to config maximum at runtime.
        VPN-FIX-001:   connect VPN before batch; rotate on block detection.
        """
        workers = self._resolve_workers(max_workers)
        urls = self._fetch_pending_urls(url_ids)

        if not urls:
            return {"status": "no_work", "queued": 0}

        # ── VPN: connect before batch starts ─────────────────────────────────
        if self._cfg.VPN_ENABLED:
            try:
                connected = self._vpn.connect()
                if connected:
                    logger.info("VPN connected OK before batch start.")
                else:
                    logger.warning("VPN connect returned False — proceeding without VPN.")
            except Exception as vpn_exc:
                logger.warning("VPN connect error: %s — proceeding without VPN.", vpn_exc)

        logger.info("Dispatching batch: urls=%d workers=%d", len(urls), workers)

        try:
            with ThreadPoolExecutor(max_workers=workers) as executor:
                futures = {
                    executor.submit(self._process_url, url_obj): url_obj
                    for url_obj in urls
                }
                for future in as_completed(futures, timeout=None):
                    url_obj = futures[future]
                    try:
                        future.result()
                    except Exception as exc:
                        logger.error("URL %s raised exception: [%s] %s", url_obj.id, type(exc).__name__, exc)
                        self._mark_error(url_obj, str(exc)[:2000])
                        self._stats.record(failed=True)
        finally:
            # BUG-BROWSER-CLOSE FIX: always close Selenium after batch.
            # Without this the browser + chromedriver.exe stay alive indefinitely
            # on Windows 11, consuming ~300 MB RAM and a Desktop Heap slot.
            try:
                self._selenium_engine.close()
                logger.info("Selenium browser closed after batch completion.")
            except Exception as close_exc:
                logger.warning("Selenium close error (non-critical): %s", close_exc)

        result = self._stats.to_dict()
        result["status"] = "complete"
        return result

    # ── Private helpers ───────────────────────────────────────────────────────

    def _resolve_workers(self, requested: Optional[int]) -> int:
        """Clamp max_workers to config limit. SCRAP-BUG-016 fix."""
        max_allowed = self._cfg.SCRAPER_MAX_WORKERS
        if requested is None:
            return max_allowed
        clamped = min(max(1, requested), max_allowed)
        if clamped != requested:
            logger.warning(
                "Requested max_workers=%d exceeds limit=%d. Clamped to %d.",
                requested, max_allowed, clamped,
            )
        return clamped

    def _fetch_pending_urls(self, url_ids: Optional[List[str]]) -> List[URLQueue]:
        """Fetch pending URL records from the database."""
        with get_db() as session:
            q = session.query(URLQueue).filter(URLQueue.status == "pending")
            if url_ids:
                try:
                    uuids = [uuid.UUID(uid) for uid in url_ids]
                    q = q.filter(URLQueue.id.in_(uuids))
                except ValueError as exc:
                    logger.warning("Invalid UUID in url_ids: %s", exc)
            rows = q.order_by(URLQueue.priority.desc(), URLQueue.created_at).limit(200).all()
            session.expunge_all()
            return rows

    def _process_url(self, url_obj: URLQueue) -> None:
        """Process a single URL through all enabled languages."""
        url_id_str = str(url_obj.id)

        if not _try_claim_url(url_id_str):
            logger.debug("URL %s already claimed, skipping.", url_id_str)
            self._stats.record(skipped=True)
            return

        try:
            self._mark_processing(url_obj)
            languages = self._cfg.ENABLED_LANGUAGES

            all_ok = True
            for lang in languages:
                ok = self._scrape_language(url_obj, lang)
                if not ok:
                    all_ok = False

            # Treat partial success as done so URL is not requeued indefinitely
            self._mark_done(url_obj, all_ok=True)
            self._stats.record(succeeded=True)

        except Exception as exc:
            logger.error("_process_url failed for %s: [%s] %s", url_id_str, type(exc).__name__, exc)
            self._mark_error(url_obj, str(exc)[:2000])
            self._stats.record(failed=True)
        finally:
            _release_url(url_id_str)

    def _scrape_language(self, url_obj: URLQueue, lang: str) -> bool:
        """
        Scrape one language variant of a hotel URL. Returns True on success.

        NEW-PHOTOS-001 (v49): Image download strategy:
          1. Preferred: download_photo_batch(hotel_id, photos) — uses rich hotelPhotos
             JS metadata (id_photo, thumb_url, large_url, highres_url with k= tokens).
             Available when SeleniumEngine._last_gallery_photos is populated (en only).
          2. Fallback: download_batch(hotel_id, image_urls) — URL-only list from DOM.
             Used when hotelPhotos JS was not found on page.

        VPN-FIX-001: rotate VPN when all engines fail and should_rotate() is True.
        BUG-IMG-401: gallery_urls now contain full URLs with k= auth params (scraper.py).
        """
        lang_url = build_language_url(url_obj.base_url or url_obj.url, lang)
        start_ts = time.monotonic()

        html = self._cloud_engine.scrape(lang_url, retries=self._cfg.MAX_LANG_RETRIES)

        # Fallback to Selenium if CloudScraper fails
        if html is None:
            logger.info("CloudScraper failed for %s/%s — trying Selenium.", url_obj.id, lang)
            html = self._selenium_engine.scrape(lang_url, lang)

        # ── VPN: rotate on block detection and retry once ─────────────────────
        if html is None and self._cfg.VPN_ENABLED:
            try:
                if self._vpn.should_rotate():
                    logger.info(
                        "VPN rotating (interval=%ds elapsed) after failure %s/%s",
                        self._cfg.VPN_ROTATION_INTERVAL, url_obj.id, lang,
                    )
                    rotated = self._vpn.rotate()
                    if rotated:
                        logger.info("VPN rotated — retrying %s/%s with CloudScraper.", url_obj.id, lang)
                        html = self._cloud_engine.scrape(lang_url, retries=1)
                        if html is None:
                            logger.info("CloudScraper still blocked — retrying Selenium after VPN rotate.")
                            html = self._selenium_engine.scrape(lang_url, lang)
                    else:
                        logger.warning("VPN rotation failed for %s/%s", url_obj.id, lang)
                else:
                    elapsed = int(time.monotonic() - self._vpn._last_rotation) if hasattr(self._vpn, '_last_rotation') else 0
                    logger.debug("VPN rotate skipped — %ds elapsed of %ds interval",
                                 elapsed, self._cfg.VPN_ROTATION_INTERVAL)
            except Exception as vpn_exc:
                logger.warning("VPN rotate error for %s/%s: %s", url_obj.id, lang, vpn_exc)

        duration_ms = int((time.monotonic() - start_ts) * 1000)

        if html is None:
            self._log_scraping_event(url_obj, lang, "scrape_failed", "error", duration_ms)
            self._upsert_lang_status(url_obj, lang, "error", "All scraping engines failed")
            return False

        # Extract hotel data
        extractor = HotelExtractor(html, url=lang_url, language=lang)
        hotel_data = extractor.extract_all()

        # ── Photo data collection (English only) ──────────────────────────────
        # Images are language-independent; collected once per hotel via English.
        # NEW-PHOTOS-001 (v49): prefer rich photo metadata (hotelPhotos JS) over
        # plain URL list, because JS metadata includes id_photo, alt, orientation,
        # dimensions, and all three size variants with full k= auth tokens.
        gallery_photos: List[Dict] = []   # rich metadata (preferred)
        gallery_urls:   List[str]  = []   # URL-only fallback

        if lang == "en":
            # Rich metadata path (NEW-PHOTOS-001)
            if hasattr(self._selenium_engine, "_last_gallery_photos"):
                gallery_photos = self._selenium_engine._last_gallery_photos or []

            # URL fallback path (BUG-IMG-003 / BUG-IMG-401)
            if hasattr(self._selenium_engine, "_last_gallery_urls"):
                gallery_urls = self._selenium_engine._last_gallery_urls or []

            if gallery_photos:
                logger.info(
                    "Photos: %d rich photo records (hotelPhotos JS) for %s",
                    len(gallery_photos), url_obj.id,
                )
            elif gallery_urls:
                logger.info(
                    "Photos: %d URL-only records (DOM fallback) for %s",
                    len(gallery_urls), url_obj.id,
                )
            else:
                logger.debug("Photos: no gallery data collected for %s", url_obj.id)

            # Attach URL list to hotel_data for hotels.photos JSONB column
            if gallery_photos:
                # Extract highres URLs (preferred) for the photos JSONB column
                hotel_data["photos"] = [
                    p.get("highres_url") or p.get("large_url") or p.get("thumb_url", "")
                    for p in gallery_photos
                    if p.get("highres_url") or p.get("large_url") or p.get("thumb_url")
                ]
            elif gallery_urls:
                hotel_data["photos"] = gallery_urls

        # Persist hotel record
        try:
            self._upsert_hotel(url_obj, lang, hotel_data, duration_ms)
            self._log_scraping_event(url_obj, lang, "scrape_success", "done", duration_ms)
            self._upsert_lang_status(url_obj, lang, "done", None)

            # ── Image download (English only, after hotel row is committed) ───
            if lang == "en" and _ImageDownloader is not None:
                has_photos = bool(gallery_photos or gallery_urls)
                if has_photos:
                    self._download_images(url_obj, lang, gallery_photos, gallery_urls)

            return True

        except Exception as exc:
            logger.error("Hotel upsert failed for %s/%s: %s", url_obj.id, lang, exc)
            self._log_scraping_event(url_obj, lang, "upsert_failed", "error", duration_ms, str(exc))
            self._upsert_lang_status(url_obj, lang, "error", str(exc)[:2000])
            return False

    def _download_images(
        self,
        url_obj: URLQueue,
        lang: str,
        gallery_photos: List[Dict],
        gallery_urls: List[str],
    ) -> None:
        """
        Trigger image downloads for a hotel after its row has been persisted.

        NEW-PHOTOS-001 (v49):
          - When gallery_photos is available (hotelPhotos JS metadata), calls
            download_photo_batch(hotel_id, photos). This method persists image_data
            rows (id_photo, dimensions, alt, orientation) and image_downloads rows
            for all three size variants (thumb, large, highres) with correct k= tokens.
          - When only gallery_urls is available, falls back to
            download_batch(hotel_id, image_urls) (URL-only, v48 behaviour).

        BUG-IMG-401: URLs now include the mandatory ?k= auth token (fixed in scraper.py).
        The downloader receives full URLs — no reconstruction needed here.
        """
        try:
            # Resolve hotel UUID from the row that was just upserted
            hotel_uuid: Optional[uuid.UUID] = None
            with get_db() as _sess:
                _hotel_row = (
                    _sess.query(Hotel)
                    .filter_by(url_id=url_obj.id, language=lang)
                    .first()
                )
                if _hotel_row:
                    hotel_uuid = _hotel_row.id

            if hotel_uuid is None:
                logger.warning(
                    "ImageDownloader: could not resolve hotel_id for %s/%s — skipping images",
                    url_obj.id, lang,
                )
                return

            downloader = _ImageDownloader()

            # NEW-PHOTOS-001: preferred path — rich photo metadata
            if gallery_photos:
                if hasattr(downloader, "download_photo_batch"):
                    results = downloader.download_photo_batch(
                        hotel_id=hotel_uuid,
                        photos=gallery_photos,
                    )
                    # download_photo_batch returns {id_photo: bool} or {url: bool}
                    downloaded = sum(1 for ok in results.values() if ok)
                    logger.info(
                        "ImageDownloader (photo_batch): %d/%d photos saved for hotel %s",
                        downloaded, len(gallery_photos), hotel_uuid,
                    )
                else:
                    # download_photo_batch not available — fall back to URL extraction
                    logger.warning(
                        "download_photo_batch not found on ImageDownloader — "
                        "extracting URLs from gallery_photos as fallback"
                    )
                    fallback_urls = [
                        p.get("highres_url") or p.get("large_url") or p.get("thumb_url", "")
                        for p in gallery_photos
                        if p.get("highres_url") or p.get("large_url") or p.get("thumb_url")
                    ]
                    if fallback_urls:
                        results = downloader.download_batch(
                            hotel_id=hotel_uuid,
                            image_urls=fallback_urls,
                        )
                        downloaded = sum(1 for ok in results.values() if ok)
                        logger.info(
                            "ImageDownloader (batch fallback from photos): %d/%d saved for hotel %s",
                            downloaded, len(fallback_urls), hotel_uuid,
                        )

            # URL-only fallback path (BUG-IMG-003 original fix, now with k= tokens)
            elif gallery_urls:
                results = downloader.download_batch(
                    hotel_id=hotel_uuid,
                    image_urls=gallery_urls,
                )
                downloaded = sum(1 for ok in results.values() if ok)
                logger.info(
                    "ImageDownloader (url_batch): %d/%d images saved for hotel %s",
                    downloaded, len(gallery_urls), hotel_uuid,
                )

        except Exception as img_exc:
            logger.warning("ImageDownloader failed for %s: %s", url_obj.id, img_exc)

    def _upsert_hotel(
        self,
        url_obj: URLQueue,
        lang: str,
        data: Dict[str, Any],
        duration_ms: int,
    ) -> None:
        # BUG-HOTEL-UPSERT: avoid TypeError from duplicate keyword arguments.
        # Extractor output may contain keys that are already set as explicit kwargs.
        _EXPLICIT_KEYS = {
            "language", "url_id", "scrape_duration_s", "scrape_engine",
            "version_id", "created_at", "updated_at", "id",
        }
        with get_db() as session:
            existing = (
                session.query(Hotel)
                .filter_by(url_id=url_obj.id, language=lang)
                .first()
            )
            if existing:
                for k, v in data.items():
                    if hasattr(existing, k) and k not in _EXPLICIT_KEYS:
                        setattr(existing, k, v)
                existing.scrape_duration_s = duration_ms / 1000
                existing.version_id += 1
            else:
                hotel = Hotel(
                    url_id=url_obj.id,
                    language=lang,
                    scrape_duration_s=duration_ms / 1000,
                    scrape_engine="cloudscraper",
                    **{k: v for k, v in data.items()
                       if hasattr(Hotel, k) and k not in _EXPLICIT_KEYS},
                )
                session.add(hotel)

    def _upsert_lang_status(
        self,
        url_obj: URLQueue,
        lang: str,
        status: str,
        error: Optional[str],
    ) -> None:
        with get_db() as session:
            row = (
                session.query(URLLanguageStatus)
                .filter_by(url_id=url_obj.id, language=lang)
                .first()
            )
            if row:
                row.status = status
                row.last_error = error
                row.attempts += 1
            else:
                session.add(URLLanguageStatus(
                    url_id=url_obj.id,
                    language=lang,
                    status=status,
                    last_error=error,
                    attempts=1,
                ))

    def _log_scraping_event(
        self,
        url_obj: URLQueue,
        lang: str,
        event_type: str,
        status: str,
        duration_ms: int,
        error_msg: Optional[str] = None,
    ) -> None:
        try:
            with get_db() as session:
                session.add(ScrapingLog(
                    url_id=url_obj.id,
                    language=lang,
                    event_type=event_type,
                    status=status,
                    duration_ms=duration_ms,
                    error_message=(error_msg or "")[:2000] if error_msg else None,
                ))
        except Exception as exc:
            logger.warning("Failed to write ScrapingLog: %s", exc)

    def _mark_processing(self, url_obj: URLQueue) -> None:
        with get_db() as session:
            row = session.get(URLQueue, url_obj.id)
            if row:
                row.status = "processing"

    def _mark_done(self, url_obj: URLQueue, all_ok: bool) -> None:
        with get_db() as session:
            row = session.get(URLQueue, url_obj.id)
            if row:
                row.status = "done" if all_ok else "error"
                row.scraped_at = datetime.now(timezone.utc)

    def _mark_error(self, url_obj: URLQueue, error: str) -> None:
        with get_db() as session:
            row = session.get(URLQueue, url_obj.id)
            if row:
                row.status = "error"
                row.retry_count += 1
                row.last_error = error[:2000]
                if row.retry_count >= row.max_retries:
                    row.status = "error"
