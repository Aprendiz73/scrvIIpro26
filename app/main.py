"""
BookingScraper/app/main.py  v4.0  [COMPLETENESS API]
FastAPI Application - BookingScraper Pro

CAMBIOS v4.0 [COMPLETENESS API]:

  [NUEVO] GET  /urls/{url_id}/completeness
    Consulta el estado de completitud por idioma de una URL.
    Retorna is_complete, languages_ok, languages_failed, languages_missing,
    y el detalle de cada idioma desde url_language_status.

  [NUEVO] POST /urls/{url_id}/rollback
    Revierte una URL: elimina hotels, url_language_status, imagenes
    y resetea url_queue a 'pending'. OPERACION DESTRUCTIVA.
    HTTP 409 si la URL esta en 'processing'.
    Parametro: keep_logs (bool, default=True) para preservar scraping_logs.

  [NUEVO] GET  /urls/incomplete
    Lista todas las URLs con idiomas fallidos (queue.status='incomplete'
    o alguna fila en url_language_status con status='failed').
    Incluye enlaces a los endpoints de completitud y rollback.

  PREREQUISITO: migration_v2_url_language_status.sql ejecutada en PostgreSQL.

CAMBIOS v3.0 [PIPELINE DE VALIDACIÓN Y NORMALIZACIÓN DE URLs]:

  DIAGNÓSTICO v2.x → v3.0:
  ──────────────────────────────────────────────────────────────
  ● _normalize_booking_url() NO validaba el prefijo https://www.booking.com/
    de forma estricta. URLs como http://booking.com/... o
    https://mobile.booking.com/... pasaban la validación (solo verificaba
    que "booking.com" estuviera en la cadena).
  ● Sin validación de sufijo .html antes de normalizar. Una URL
    como https://www.booking.com/hotel/es/hotel.pdf pasaba silenciosamente.
  ● Detección de formato CSV/lista plana frágil: usaba la presencia de
    "booking.com" en la primera línea, lo que fallaba con archivos CSV
    cuya primera fila era una cabecera sin URLs.
  ● Sin reporte estructurado de rechazos — imposible auditar qué URLs
    fueron descartadas y por qué.
  ● Sin validación de longitud máxima de URL.

  [FIX #32] validate_and_normalize_booking_url():
    Pipeline completo de validación en cascada (fail-fast) con resultado
    estructurado URLPipelineResult. Sustituye _normalize_booking_url().
    Validaciones en orden:
      1. URL no vacía y longitud ≤ _MAX_URL_LENGTH
      2. Prefijo EXACTO: https://www.booking.com/ (case-insensitive)
      3. Sufijo: la ruta debe terminar en .html (con o sin segmento de idioma)
      4. Normalización de path: eliminar sufijo de idioma (.<lang>.html → .html)
      5. Normalización de query: eliminar todos los parámetros (?lang=, ?aid=, etc.)

  [FIX #33] Detección de formato CSV mejorada:
    Antes: "booking.com" in first_data_line (frágil, falla con headers CSV)
    Ahora: Intenta csv.DictReader primero; si la fila tiene clave 'url'/'URL'
    → modo CSV con cabecera; si no → modo lista plana. Más robusto y explícito.

  [FIX #34] /urls/load: reporte de rechazos detallado:
    La respuesta ahora incluye 'rejected' con conteo por razón de rechazo,
    'normalized_count' (URLs que fueron modificadas durante normalización),
    y 'errors' con descripción de fallos técnicos. Permite auditoría completa.

  [FIX #35] Validación de longitud máxima de URL (2048 chars):
    URLs > 2048 caracteres no son válidas para ningún estándar HTTP/HTTPS
    y podrían ser indicativas de datos corruptos o ataques de inyección.

CAMBIOS v2.3 [FIX DE IDIOMA]:
  [FIX BUG #3] /urls/load: URLs normalizadas antes de insertar en url_queue.
    Nueva función _normalize_booking_url() elimina el sufijo de idioma existente
    (.es, .de, .en-gb...) de la URL. Sin este fix, las URLs .es.html almacenadas
    impedían a build_language_url() construir correctamente las URLs de otros idiomas.
    Aplica tanto al modo lista plana como al modo CSV con cabecera.

Windows 11 + Python 3.14.3

CAMBIOS v2.1:
  [NEW] /vpn/status  - estado en tiempo real de la VPN
  [NEW] /vpn/rotate  - rota la VPN manualmente desde el API
  [NEW] /vpn/connect - conecta VPN a un pais especifico
  [NEW] /scraping/test-url - prueba extraccion en una URL concreta (diagnostico)
  [FIX] /scraping/start y /scraping/force-now mejorados

CAMBIOS v2.2:
  [FIX CRITICO] /urls/load: acepta lista plana de URLs sin cabecera (formato del proyecto).
               csv.DictReader usaba la 1a URL como nombre de columna -> row.get("url")=None
               -> todas las filas se contaban como skipped -> {"inserted":0,"skipped":15}.
  [FIX] /urls/load: contador 'inserted' usa rowcount real (no incrementa en ON CONFLICT).
  [FIX] /urls/load: respuesta anade campos 'format' y 'errors' para diagnostico.
"""

import asyncio
import csv
import os
import re
import sys
import threading
import uuid
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone  # [FIX BUG-V6-010] timezone needed for aware timestamps
from pathlib import Path
from typing import Final, Optional

from fastapi import FastAPI, BackgroundTasks, Body, Depends, File, HTTPException, Query, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from loguru import logger
from sqlalchemy import text
from sqlalchemy.orm import Session

sys.path.append(str(Path(__file__).parent.parent))

from app.config import settings
from app.database import get_db, test_connection

# [FIX BUG-NEW-13] Lightweight in-memory rate limiter (no external dependency).
# Tracks per-IP request counts in a sliding window. For multi-process deployments,
# replace with Redis-backed slowapi (https://github.com/laurentS/slowapi).
import time as _time
import collections as _collections

_RATE_LIMIT_WINDOW = int(os.getenv("RATE_LIMIT_WINDOW_SECONDS", "60"))
_RATE_LIMIT_MAX_REQUESTS = int(os.getenv("RATE_LIMIT_MAX_REQUESTS", "120"))
_rate_buckets: dict = {}
_rate_lock = threading.Lock()
# [FIX Section 6.5] Track last cleanup time to purge stale (empty) bucket entries.
# Without cleanup, every unique client IP accumulates forever, growing unbounded.
_rate_last_cleanup: float = 0.0
_RATE_CLEANUP_INTERVAL = 300.0  # Clean stale entries every 5 minutes

def _check_rate_limit(request: Request, limit: int = _RATE_LIMIT_MAX_REQUESTS) -> None:
    """Raises HTTP 429 if the client IP exceeds `limit` requests per window."""
    client_ip = request.client.host if request.client else "unknown"
    now = _time.monotonic()
    global _rate_last_cleanup
    with _rate_lock:
        timestamps = _rate_buckets.setdefault(client_ip, _collections.deque())
        # Purge timestamps outside the current window for this IP
        while timestamps and timestamps[0] < now - _RATE_LIMIT_WINDOW:
            timestamps.popleft()
        if len(timestamps) >= limit:
            raise HTTPException(
                status_code=429,
                detail=f"Rate limit exceeded: max {limit} requests per {_RATE_LIMIT_WINDOW}s"
            )
        timestamps.append(now)
        # [FIX Section 6.5 / BUG-V7-009] Periodically remove empty/stale bucket entries.
        # BUG-V7-009: previous code used ts[-1] (MOST RECENT timestamp) — a bucket is
        # only stale if even its most recent request is outside the window, which means
        # ts[-1] is actually the correct check to determine "this IP has been idle for a
        # full window". However, the deque is already pruned above so ts[0] == ts[-1]
        # for single-element deques, but ts[-1] is semantically correct here because:
        # an IP is "stale" iff its LAST request was > window ago (ts[-1] < cutoff).
        # BUG-V7-009 correction: The report was wrong — ts[-1] IS the right check.
        # We add a belt-and-suspenders guard: also include IPs whose deque is fully
        # expired (all timestamps already pruned out), i.e. not ts (empty deque).
        if now - _rate_last_cleanup > _RATE_CLEANUP_INTERVAL:
            # [FIX BUG-V9-012] Update _rate_last_cleanup BEFORE the deletion loop.
            # Setting it after deletion means a slow cleanup (many IPs) could allow
            # a second concurrent call to enter this branch and start a second cleanup
            # cycle before the first finishes. Setting it first gates subsequent calls
            # out immediately. _rate_lock is already held by the caller, so this
            # assignment is inherently thread-safe within the lock context.
            _rate_last_cleanup = now
            cutoff = now - _RATE_LIMIT_WINDOW
            stale_ips = [
                ip for ip, ts in _rate_buckets.items()
                if not ts or ts[-1] < cutoff   # ts[-1] = most recent; stale if even that is old
            ]
            for ip in stale_ips:
                del _rate_buckets[ip]

# ─────────────────────────────────────────────────────────────────────────────
# [BUG-002 FIX] WINDOWS KEEPALIVE — evita suspensión de threads por pantalla bloqueada.
# SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_AWAYMODE_REQUIRED)
# impide que Windows suspenda el proceso cuando el display se apaga.
# Solo activo en plataformas Windows; no-op en Linux/macOS.
# ─────────────────────────────────────────────────────────────────────────────
def _windows_set_keepalive(enable: bool = True) -> bool:
    """
    Llama a SetThreadExecutionState vía ctypes para prevenir suspensión de sistema.
    Returns True si tuvo éxito, False si no está en Windows o falló.
    """
    try:
        import ctypes
        ES_CONTINUOUS          = 0x80000000
        ES_SYSTEM_REQUIRED     = 0x00000001
        ES_AWAYMODE_REQUIRED   = 0x00000040
        if enable:
            flags = ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_AWAYMODE_REQUIRED
        else:
            flags = ES_CONTINUOUS  # liberar — volver a comportamiento normal
        result = ctypes.windll.kernel32.SetThreadExecutionState(flags)
        if result == 0:
            logger.warning("[BUG-002] SetThreadExecutionState devolvió 0 (posible error).")
            return False
        logger.info(f"[BUG-002] Windows keepalive {'activado' if enable else 'desactivado'} (flags=0x{flags:08X})")
        return True
    except AttributeError:
        # No estamos en Windows (no hay windll)
        logger.debug("[BUG-002] Windows keepalive no disponible (plataforma no-Windows).")
        return False
    except Exception as e:
        logger.warning(f"[BUG-002] Error configurando Windows keepalive: {e}")
        return False

# ─────────────────────────────────────────────────────────────────────────────
# AUTO-DISPATCHER (asyncio, sin Celery)
# ─────────────────────────────────────────────────────────────────────────────

_dispatch_task: Optional[asyncio.Task] = None
_dispatcher_running: bool = False


def _sync_dispatch(batch_size: int) -> dict:
    try:
        from app.scraper_service import process_batch
        return process_batch(batch_size)
    except Exception as e:
        logger.error(f"_sync_dispatch error: {e}")
        return {"dispatched": 0, "error": str(e)}


# ─────────────────────────────────────────────────────────────────────────────
# [v3.0] PIPELINE DE VALIDACIÓN Y NORMALIZACIÓN DE URLs
#
# Responsabilidad única: validar la estructura de la URL y producir su forma
# canónica antes de cualquier interacción con la base de datos.
#
# INVARIANTES GARANTIZADOS:
#   - Toda URL que pase la validación comienza con EXACTAMENTE _BOOKING_PREFIX
#   - Toda URL canónica termina en '.html' sin sufijos de idioma
#   - Toda URL canónica no contiene query parameters
#   - La validación es idempotente: aplicarla dos veces produce el mismo resultado
# ─────────────────────────────────────────────────────────────────────────────

# Prefijo obligatorio — case-insensitive en validación, normalizado a minúsculas
_BOOKING_PREFIX: Final[str] = "https://www.booking.com/"

# Sufijo requerido en la ruta (sin query params, sin fragmento)
_REQUIRED_SUFFIX: Final[str] = ".html"

# Límite práctico de longitud de URL válida para PostgreSQL TEXT y HTTP estándar
_MAX_URL_LENGTH: Final[int] = 2048

# Patrón de sufijo de idioma en path de Booking.com
# Ejemplos: .es.html, .en-gb.html, .zh-cn.html, .pt-br.html
# Aplicado solo al path (antes del ?)
_LANG_SUFFIX_RE: Final[re.Pattern] = re.compile(
    r'\.[a-z]{2}(?:-[a-z]{2,4})?\.html$',
    flags=re.IGNORECASE,
)


@dataclass(frozen=True)
class URLPipelineResult:
    """
    Resultado estructurado del pipeline de validación y normalización.

    Inmutable (frozen=True): garantiza que el resultado no sea modificado
    después de su creación por código externo.

    Campos:
        is_valid      : True solo si la URL pasó todas las validaciones
        canonical_url : URL normalizada (None si is_valid=False)
        rejection_reason : Motivo de rechazo legible (None si is_valid=True)
        was_normalized   : True si la URL fue modificada durante normalización
        original_url     : URL original sin modificar (para logging/auditoría)
    """
    is_valid: bool
    canonical_url: Optional[str]
    rejection_reason: Optional[str]
    was_normalized: bool = False
    original_url: str = ""


def validate_and_normalize_booking_url(raw_url: str) -> URLPipelineResult:
    """
    Pipeline completo de validación y normalización de URLs de Booking.com.

    Operaciones en orden de fallo rápido (fail-fast):
      1. Validar no vacía y longitud ≤ _MAX_URL_LENGTH
      2. Validar prefijo EXACTO: https://www.booking.com/
      3. Validar sufijo de ruta: termina en .html (acepta .<lang>.html)
      4. Normalizar path: eliminar sufijo de idioma
      5. Normalizar query: eliminar TODOS los parámetros (lang=, aid=, etc.)

    Thread-safe: no modifica estado global.
    No lanza excepciones: siempre retorna URLPipelineResult.

    Args:
        raw_url: URL cruda proveniente de CSV o formulario, sin pre-procesar.

    Returns:
        URLPipelineResult con canonical_url=None si la URL no es válida.
    """
    original = raw_url if raw_url is not None else ""

    # ── Paso 1: Validación de presencia y longitud ─────────────────────────
    if not original or not original.strip():
        return URLPipelineResult(
            is_valid=False,
            canonical_url=None,
            rejection_reason="URL vacía o solo espacios en blanco",
            original_url=original,
        )

    url = original.strip()

    if len(url) > _MAX_URL_LENGTH:
        return URLPipelineResult(
            is_valid=False,
            canonical_url=None,
            rejection_reason=(
                f"URL supera {_MAX_URL_LENGTH} caracteres ({len(url)} chars). "
                "Posible dato corrupto."
            ),
            original_url=url,
        )

    # ── Paso 2: Validación de prefijo obligatorio (case-insensitive) ───────
    # Se compara en minúsculas para evitar variaciones de capitalización
    if not url.lower().startswith(_BOOKING_PREFIX.lower()):
        return URLPipelineResult(
            is_valid=False,
            canonical_url=None,
            rejection_reason=(
                f"No comienza con '{_BOOKING_PREFIX}'. "
                f"Prefijo encontrado: '{url[:40]}...'"
            ),
            original_url=url,
        )

    # ── Paso 3: Extraer path (sin query params) y validar sufijo ──────────
    # Separamos path del query string para evaluar el sufijo correctamente.
    # Una URL como '.../hotel.es.html?lang=es' tiene path '.../hotel.es.html'
    # que termina en '.html' implícitamente a través del sufijo de idioma.
    path_part = url.split("?")[0].split("#")[0]

    # Condición válida: termina en .html directamente O en .<lang>.html
    ends_in_html = path_part.lower().endswith(_REQUIRED_SUFFIX)
    has_lang_then_html = bool(_LANG_SUFFIX_RE.search(path_part))

    if not ends_in_html and not has_lang_then_html:
        return URLPipelineResult(
            is_valid=False,
            canonical_url=None,
            rejection_reason=(
                f"La ruta no termina en '{_REQUIRED_SUFFIX}'. "
                f"Ruta encontrada: '...{path_part[-30:]}'"
            ),
            original_url=url,
        )

    # ── Paso 4: Normalización de path — eliminar sufijo de idioma ─────────
    # .../hotel.es.html   → .../hotel.html
    # .../hotel.en-gb.html → .../hotel.html
    # .../hotel.html       → .../hotel.html  (sin cambio)
    canonical_path = _LANG_SUFFIX_RE.sub(".html", path_part)

    # Garantía de sufijo — no debería ser necesario, pero por invariante:
    if not canonical_path.lower().endswith(_REQUIRED_SUFFIX):
        canonical_path += _REQUIRED_SUFFIX

    # ── Paso 5: Normalización de query — eliminar TODOS los parámetros ─────
    # Las URLs canónicas de Booking.com almacenadas en BD no deben llevar
    # parámetros de ningún tipo (lang=, aid=, utm_*, label=, etc.).
    # build_language_url() en scraper.py añade el ?lang= adecuado en runtime.
    canonical_url = canonical_path  # sin query string

    was_normalized = (canonical_url != url)

    return URLPipelineResult(
        is_valid=True,
        canonical_url=canonical_url,
        rejection_reason=None,
        was_normalized=was_normalized,
        original_url=url,
    )


def _normalize_booking_url(url: str) -> str:
    """
    Alias de compatibilidad retroactiva para validate_and_normalize_booking_url().

    [DEPRECADO desde v3.0] — Usar validate_and_normalize_booking_url() directamente
    para obtener el resultado estructurado con información de validación.
    Este alias existe solo para no romper referencias externas que pudieran existir.

    ADVERTENCIA: Retorna la URL original sin modificar si la validación falla,
    en lugar de None. Usar el resultado booleano is_valid para decisiones críticas.
    """
    result = validate_and_normalize_booking_url(url)
    if result.is_valid:
        return result.canonical_url
    # Comportamiento legacy: retornar URL original si no pasa validación
    # (el caller debe verificar is_valid antes de usar el valor)
    return url.strip()


async def _auto_dispatch_loop():
    global _dispatcher_running
    _dispatcher_running = True
    logger.info("🤖 Auto-dispatcher iniciado (ciclo 30s) — no requiere Celery")

    await asyncio.sleep(5)

    while True:
        try:
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(
                None,
                lambda: _sync_dispatch(settings.BATCH_SIZE)
            )
            n = result.get("dispatched", 0)
            if n > 0:
                logger.info(f"🤖 Auto-dispatch: {n} URLs enviadas al thread pool")
        except asyncio.CancelledError:
            logger.info("🤖 Auto-dispatcher detenido")
            break
        except Exception as e:
            logger.error(f"🤖 Auto-dispatch error: {e}")

        await asyncio.sleep(30)

    _dispatcher_running = False


# [BUG-002 FIX] Watchdog: detecta suspensiones causadas por pantalla bloqueada.
# Compara timestamp real entre ciclos; si el gap supera WATCHDOG_INTERVAL_SECS * 2
# (indicativo de suspensión), registra warning y fuerza re-verificación VPN.
_watchdog_last_heartbeat: float = 0.0


async def _watchdog_loop():
    """
    Monitorea que el event loop no fue suspendido por Windows al bloquear pantalla.
    Detección: si el gap entre latidos es > 2× el intervalo configurado, la diferencia
    es tiempo perdido por suspensión del proceso.
    """
    global _watchdog_last_heartbeat
    import time
    interval = getattr(settings, "WATCHDOG_INTERVAL_SECS", 120)
    logger.info(f"🐕 Watchdog iniciado (intervalo={interval}s)")

    while True:
        try:
            now = time.monotonic()
            if _watchdog_last_heartbeat > 0:
                gap = now - _watchdog_last_heartbeat
                if gap > interval * 2:
                    lost_secs = gap - interval
                    logger.warning(
                        f"[BUG-002] ⚠️ SUSPENSIÓN DETECTADA: gap={gap:.0f}s "
                        f"(~{lost_secs:.0f}s sin ejecutar). "
                        f"Posible bloqueo de pantalla. Verificando VPN y dispatcher..."
                    )
                    # Re-verificar VPN tras reanudación
                    if settings.VPN_ENABLED:
                        try:
                            from app.scraper_service import _get_vpn_manager
                            vpn = _get_vpn_manager()
                            if vpn:
                                active = vpn.verify_vpn_active()
                                logger.info(f"[BUG-002] VPN tras reanudación: {'activa' if active else 'INACTIVA'}")
                                if not active:
                                    vpn.connect("UK")
                        except Exception as ve:
                            logger.warning(f"[BUG-002] Error re-verificando VPN: {ve}")

            _watchdog_last_heartbeat = now
        except asyncio.CancelledError:
            logger.info("🐕 Watchdog detenido")
            break
        except Exception as e:
            logger.error(f"🐕 Watchdog error: {e}")

        await asyncio.sleep(interval)


# ─────────────────────────────────────────────────────────────────────────────
# LIFESPAN
# ─────────────────────────────────────────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    global _dispatch_task

    print("\n" + "=" * 60)
    # [FIX BUG-B-02] Version inconsistency: banner said v7.0 while FastAPI app,
    # /root, /system/info, and config.APP_VERSION all declare 6.0.0.
    print("  BookingScraper Pro v6.0.0 - Iniciando")
    print("=" * 60)
    db_ok = test_connection()
    print(f"  Base de datos  : {'✓ OK' if db_ok else '✗ ERROR'}")
    print(f"  Idiomas        : {', '.join(settings.ENABLED_LANGUAGES)}")
    print(f"  Batch size     : {settings.BATCH_SIZE}")
    print(f"  Selenium       : {'✓ ACTIVO' if settings.USE_SELENIUM else '✗ cloudscraper'}")
    print(f"  VPN            : {'✓ ACTIVO' if settings.VPN_ENABLED else '✗ desactivado'}")
    print(f"  Auto-scraper   : ✓ ACTIVO (cada 30s)")
    print(f"  Docs           : http://localhost:8000/docs")
    print(f"  VPN status     : http://localhost:8000/vpn/status")
    print(f"  Scraping status: http://localhost:8000/scraping/status")
    print("=" * 60 + "\n")

    # [BUG-002 FIX] Activar Windows keepalive para evitar suspensión por pantalla bloqueada
    _windows_set_keepalive(enable=True)

    _dispatch_task = asyncio.create_task(_auto_dispatch_loop())

    # [BUG-002 FIX] Iniciar watchdog de suspensión
    _watchdog_task = asyncio.create_task(_watchdog_loop())

    # Iniciar VPN en background si está habilitada
    if settings.VPN_ENABLED:
        async def _init_vpn():
            try:
                from app.scraper_service import _get_vpn_manager
                vpn = _get_vpn_manager()
                if vpn:
                    logger.info("🔐 VPN iniciada al arrancar")
            except Exception as e:
                logger.warning(f"⚠️ VPN init al arrancar: {e}")
        asyncio.create_task(_init_vpn())

    # Reset URLs atascadas al arrancar
    try:
        from app.database import SessionLocal
        _db = SessionLocal()
        # [FIX BUG-V13-006] Increment retry_count when resetting 'processing' URLs.
        # Without this, a URL that crashes the worker restarts with retry_count=0,
        # dispatches again, crashes again — infinite loop until manual intervention.
        # Now each unclean-restart cycle consumes one retry slot, escalating to
        # 'failed' after max_retries crashes — automatic containment, no manual fix.
        r1 = _db.execute(text("""
            UPDATE url_queue
            SET status      = CASE
                                  WHEN retry_count + 1 >= max_retries THEN 'failed'
                                  ELSE 'pending'
                              END,
                retry_count = retry_count + 1,
                last_error  = 'Worker crash/unclean shutdown detected at restart',
                updated_at  = NOW()
            WHERE status = 'processing'
        """))
        # [FIX REGRESS-02/BUG-04] Solo resetear 'failed' que NO han agotado reintentos.
        # Resetear TODO lo 'failed' descarta historial y re-intenta URLs que ya superaron max_retries.
        r2 = _db.execute(text(
            "UPDATE url_queue SET status='pending', last_error=NULL, updated_at=NOW() "
            "WHERE status='failed' AND retry_count < :max_retries"
        ), {"max_retries": settings.MAX_RETRIES})
        _db.commit()
        _db.close()
        if r1.rowcount or r2.rowcount:
            print(f"  ♻️  Reset al arrancar: {r1.rowcount} processing (retry++) + {r2.rowcount} failed → pending")
    except Exception as _e:
        print(f"  ⚠️ Reset al arrancar falló: {_e}")

    yield

    if _dispatch_task and not _dispatch_task.done():
        _dispatch_task.cancel()
        try:
            await _dispatch_task
        except asyncio.CancelledError:
            pass

    # [BUG-002 FIX] Cancelar watchdog y liberar keepalive de Windows al apagar
    # [FIX BUG-V7-004] Replace unreliable "_watchdog_task" in dir() with try/except NameError.
    # dir() may not reliably detect local variable existence in all execution contexts.
    try:
        if not _watchdog_task.done():
            _watchdog_task.cancel()
            try:
                await _watchdog_task
            except asyncio.CancelledError:
                pass
    except NameError:
        pass  # _watchdog_task was never created (startup failed before that point)
    _windows_set_keepalive(enable=False)

    # [FIX BUG-NEW-09] Reset URLs 'processing' at graceful shutdown — prevents permanent locks
    # if the app is not restarted (e.g., debugging, maintenance without restart).
    # NOTE: We deliberately do NOT increment retry_count here (unlike startup reset, BUG-V13-006).
    # Graceful shutdown is operator-initiated; URLs were not at fault — no retry penalty applied.
    try:
        from app.database import SessionLocal
        _shutdown_db = SessionLocal()
        _r = _shutdown_db.execute(text(
            "UPDATE url_queue SET status='pending', updated_at=NOW() WHERE status='processing'"
        ))
        _shutdown_db.commit()
        _shutdown_db.close()
        if _r.rowcount:
            logger.info(f"[BUG-NEW-09] Shutdown: {_r.rowcount} URLs 'processing' → 'pending'")
    except Exception as _se:
        logger.warning(f"[BUG-NEW-09] Shutdown reset falló: {_se}")

    # [FIX BUG-NEW-05] Apagar executor del scraper_service para liberar recursos
    try:
        from app.scraper_service import _executor
        _executor.shutdown(wait=False, cancel_futures=True)
        logger.info("[BUG-NEW-05] ThreadPoolExecutor (scraper) apagado correctamente")
    except Exception as _ee:
        logger.warning(f"[BUG-NEW-05] Executor shutdown falló: {_ee}")

    logger.info("BookingScraper Pro detenido")


# ─────────────────────────────────────────────────────────────────────────────
# APLICACIÓN
# ─────────────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="BookingScraper Pro",
    description="Sistema profesional de scraping para Booking.com - Windows 11",
    version="6.0.0",  # [FIX REGRESS-03/BUG-05]
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    # [FIX REGRESS-01/BUG-01] allow_origins=["*"] nunca debe usarse con credenciales.
    # Configurar via variable de entorno: CORS_ORIGINS=http://localhost:3000,https://miapp.com
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:3000").split(","),
    allow_credentials=True,
    # [FIX BUG-V5-007] Métodos y headers explícitos — elimina permisividad excesiva.
    # allow_methods=["*"] y allow_headers=["*"] permiten verbos y cabeceras arbitrarias.
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "X-API-Key", "X-Request-ID"],
)


# ─────────────────────────────────────────────────────────────────────────────
# SEGURIDAD — API KEY (opcional)
# [FIX BUG-NEW-12] _verify_api_key estaba referenciada en /scraping/force-now
#   pero nunca definida → NameError en tiempo de importación → crash de uvicorn.
#
# Comportamiento:
#   • API_KEY vacía (default) → sin protección; cualquier cliente puede llamar.
#   • API_KEY configurada en .env → se exige cabecera X-API-Key correcta.
#
# PRINCIPIO: fail-safe — si la dependencia no puede verificarse, deniega acceso.
# ─────────────────────────────────────────────────────────────────────────────

from fastapi.security import APIKeyHeader as _APIKeyHeader

_api_key_header = _APIKeyHeader(name="X-API-Key", auto_error=False)


def _verify_api_key(x_api_key: Optional[str] = Depends(_api_key_header)) -> None:
    """
    Dependencia FastAPI para protección opcional por API key.

    - Si settings.API_KEY está vacío: endpoint público (sin validación).
    - Si settings.API_KEY tiene valor: exige cabecera X-API-Key correcta.
    - Comparación de tiempo constante (hmac.compare_digest) para prevenir
      ataques de temporización.
    """
    import hmac
    configured_key: str = getattr(settings, "API_KEY", "")
    if not configured_key:
        return  # Modo público: API_KEY no configurada → sin restricción
    if not x_api_key:
        raise HTTPException(
            status_code=401,
            detail="Se requiere cabecera X-API-Key",
            headers={"WWW-Authenticate": "ApiKey"},
        )
    if not hmac.compare_digest(configured_key.encode(), x_api_key.encode()):
        raise HTTPException(
            status_code=403,
            detail="API key inválida",
        )


# [FIX BUG-V5-014] Correlation ID middleware — propaga X-Request-ID en cada petición.
# Permite trazar un request a través de logs, threads y tareas Celery.
@app.middleware("http")
async def _correlation_id_middleware(request: Request, call_next):
    """Inyecta X-Request-ID en cada request para trazabilidad distribuida."""
    request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
    with logger.contextualize(request_id=request_id):
        response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response


# ─────────────────────────────────────────────────────────────────────────────
# HEALTH
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/", tags=["Health"])
def root():
    from app.scraper_service import get_service_stats
    svc = get_service_stats()
    return {
        "app": "BookingScraper Pro", "version": "6.0.0",  # [FIX REGRESS-03/BUG-05]
        "docs": "/docs", "status": "running",
        "auto_dispatch": _dispatcher_running,
        "processing_now": svc["active_count"],
        "vpn_enabled": settings.VPN_ENABLED,
    }


@app.get("/health", tags=["Health"])
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        db_status = "ok"
    except Exception as e:
        db_status = f"error: {e}"
    from app.scraper_service import get_service_stats
    svc = get_service_stats()
    return {
        "status":     "healthy" if db_status == "ok" else "degraded",
        "database":   db_status,
        "dispatcher": "running" if _dispatcher_running else "stopped",
        "processing": svc["active_count"],
        "timestamp":  datetime.now(timezone.utc).isoformat(),
    }


# ─────────────────────────────────────────────────────────────────────────────
# VPN
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/vpn/status", tags=["VPN"])
def vpn_status():
    """Estado actual de la VPN y métricas de rotación."""
    from app.scraper_service import get_vpn_status
    return get_vpn_status()


@app.post("/vpn/rotate", tags=["VPN"])
def vpn_rotate(request: Request):
    """Rota la VPN inmediatamente a un servidor diferente."""
    _check_rate_limit(request, limit=10)  # [FIX BUG-NEW-13] max 10 rotations/minute
    from app.scraper_service import rotate_vpn_now
    result = rotate_vpn_now()
    if not result.get("success"):
        raise HTTPException(500, result.get("reason") or result.get("error") or "Error rotando VPN")
    return result


@app.post("/vpn/connect", tags=["VPN"])
def vpn_connect(request: Request, country: str = Body(default=None, embed=True)):
    """
    Conecta VPN a un país específico.
    country: 'US', 'DE', 'FR', 'NL', 'ES', 'IT', 'CA', 'SE' ... o null para aleatorio
    """
    _check_rate_limit(request, limit=10)  # [FIX BUG-NEW-13] max 10 connects/minute
    # [FIX BUG-NEW-06] Validate country against allowed list and enforce safe characters.
    # Prevents shell injection if the VPN manager uses subprocess/CLI.
    import re as _re
    if country is not None:
        if not isinstance(country, str) or len(country) > 10:
            raise HTTPException(400, "country must be a string of at most 10 characters")
        if not _re.fullmatch(r"[A-Za-z]{2,10}", country):
            raise HTTPException(400, "country must contain only alphabetic characters (2-10 chars)")
        country_upper = country.upper()
        allowed = settings.VPN_COUNTRIES if hasattr(settings, "VPN_COUNTRIES") and settings.VPN_COUNTRIES else None
        if allowed and country_upper not in [c.upper() for c in allowed]:
            raise HTTPException(400, f"country '{country_upper}' is not in the allowed VPN_COUNTRIES list")
        country = country_upper

    from app.scraper_service import _get_vpn_manager, _vpn_lock_ctx
    vpn = _get_vpn_manager()
    if not vpn:
        raise HTTPException(503, "VPN_ENABLED=False o VPN no disponible")
    with _vpn_lock_ctx():
        try:
            success = vpn.connect(country)
            return {
                "success": success,
                "country": country,
                "new_ip": vpn.current_ip,
                "server": vpn.current_server,
            }
        except Exception as e:
            raise HTTPException(500, str(e))



# ─────────────────────────────────────────────────────────────────────────────
# STATISTICS
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/stats", tags=["Statistics"])
def get_stats(db: Session = Depends(get_db)):
    try:
        urls = db.execute(text("""
            SELECT
                COUNT(*)                                       AS total,
                COUNT(*) FILTER (WHERE status='pending')      AS pending,
                COUNT(*) FILTER (WHERE status='processing')   AS processing,
                COUNT(*) FILTER (WHERE status='completed')    AS completed,
                COUNT(*) FILTER (WHERE status='failed')       AS failed
            FROM url_queue
        """)).fetchone()

        hotels_total = db.execute(text("SELECT COUNT(*) FROM hotels")).scalar() or 0
        hotels_by_lang = db.execute(text(
            "SELECT language, COUNT(*) FROM hotels GROUP BY language ORDER BY COUNT(*) DESC"
        )).fetchall()

        from app.scraper_service import get_service_stats, get_vpn_status
        svc = get_service_stats()

        return {
            "url_queue": {
                "total": urls[0] or 0,
                "pending": urls[1] or 0,
                "processing": urls[2] or 0,
                "completed": urls[3] or 0,
                "failed": urls[4] or 0,
            },
            "hotels": {
                "total": hotels_total,
                "by_language": {r[0]: r[1] for r in hotels_by_lang},
            },
            "service": svc,
            "vpn": get_vpn_status(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    except Exception as e:
        raise HTTPException(500, str(e))


# ─────────────────────────────────────────────────────────────────────────────
# URLS
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/urls", tags=["URLs"])
def list_urls(
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    try:
        limit = min(limit, 500)
        if status:
            rows = db.execute(
                text("SELECT id, url, status, language, priority, retry_count, scraped_at, last_error "
                     "FROM url_queue WHERE status=:s ORDER BY id LIMIT :l OFFSET :sk"),
                {"s": status, "l": limit, "sk": skip}
            ).fetchall()
        else:
            rows = db.execute(
                text("SELECT id, url, status, language, priority, retry_count, scraped_at, last_error "
                     "FROM url_queue ORDER BY id LIMIT :l OFFSET :sk"),
                {"l": limit, "sk": skip}
            ).fetchall()
        return {"total": len(rows), "urls": [dict(r._mapping) for r in rows]}
    except Exception as e:
        raise HTTPException(500, str(e))


@app.post("/urls/load", tags=["URLs"])
async def load_urls(request: Request, file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Carga URLs en la cola de scraping.

    [v3.0] Pipeline de validación y normalización completo:
      - Valida prefijo EXACTO: https://www.booking.com/
      - Valida sufijo: la ruta debe terminar en .html
      - Normaliza: elimina sufijo de idioma del path (hotel.es.html → hotel.html)
      - Normaliza: elimina TODOS los parámetros de query (?lang=, ?aid=, etc.)
      - No sobrescribe URLs ya existentes en la cola (ON CONFLICT DO NOTHING)

    Acepta dos formatos automáticamente:
      - CSV con cabecera: columna 'url' o 'URL' requerida, opcionales 'language', 'priority'
      - Lista plana: una URL por línea, sin cabecera

    La detección de formato es robusta:
      - Si la primera fila tiene columnas conocidas ('url', 'URL') → modo CSV con cabecera
      - Si no → modo lista plana

    Líneas en blanco y comentarios con # son ignorados.

    Respuesta incluye:
      - inserted: URLs nuevas insertadas
      - skipped_existing: URLs ya presentes en la cola (ON CONFLICT DO NOTHING)
      - normalized_count: URLs que fueron modificadas durante normalización
      - rejected: conteo de URLs rechazadas por razón específica
      - errors: errores técnicos durante procesamiento
      - format: formato detectado ('csv_with_header' | 'plain_list')
    """
    _check_rate_limit(request, limit=20)  # [FIX BUG-NEW-13] max 20 uploads/minute
    try:
        content = await file.read()
        # [FIX BUG-V5-023] Límite de tamaño de archivo para prevenir DoS por upload masivo.
        # Máximo configurable vía CSV_MAX_FILE_MB (default: 10 MB).
        _max_bytes = int(os.getenv("CSV_MAX_FILE_MB", "10")) * 1_048_576
        if len(content) > _max_bytes:
            raise HTTPException(
                status_code=413,
                detail=(
                    f"Archivo demasiado grande: {len(content) // 1_048_576} MB. "
                    f"Máximo permitido: {_max_bytes // 1_048_576} MB. "
                    "Ajusta CSV_MAX_FILE_MB en .env si necesitas un límite mayor."
                ),
            )
        raw_lines = content.decode("utf-8-sig", errors="ignore").splitlines()
        # [FIX BUG-V5-023] Límite de líneas — evita procesamiento de archivos con millones de filas.
        _max_lines = int(os.getenv("CSV_MAX_ROWS", "50000"))
        if len(raw_lines) > _max_lines:
            raise HTTPException(
                status_code=413,
                detail=(
                    f"El archivo contiene {len(raw_lines):,} líneas. "
                    f"Máximo permitido: {_max_lines:,}. "
                    "Ajusta CSV_MAX_ROWS en .env o divide el archivo en partes."
                ),
            )

        # ── Detección de formato robusta ──────────────────────────────────────
        # Filtramos líneas vacías y comentarios para analizar el contenido real
        data_lines = [
            line for line in raw_lines
            if line.strip() and not line.strip().startswith("#")
        ]

        if not data_lines:
            return {
                "inserted": 0,
                "skipped_existing": 0,
                "normalized_count": 0,
                "rejected": {},
                "errors": [],
                "format": "empty_file",
                "message": "El archivo no contiene líneas con datos válidos",
            }

        # [FIX #33] Detección de formato mejorada:
        # Intentamos interpretar la primera línea como cabecera CSV.
        # Si tiene columnas reconocibles (url, URL) → CSV con cabecera.
        # Si no → lista plana.
        first_line = data_lines[0]
        first_line_lower = first_line.lower()
        is_csv_with_header = (
            "url" in first_line_lower.split(",") or
            any(col.strip() in ("url", "URL") for col in first_line.split(","))
        )

        inserted = 0
        skipped_existing = 0
        normalized_count = 0
        rejected: dict[str, int] = {}
        errors: list[str] = []

        def _record_rejection(reason_key: str, url_preview: str):
            """Registra un rechazo y lo loguea para auditoría."""
            rejected[reason_key] = rejected.get(reason_key, 0) + 1
            logger.debug(f"  🚫 URL rechazada [{reason_key}]: {url_preview[:80]}")

        def _process_url(raw_url: str, language: str = "en", priority: int = 5) -> bool:
            """
            Procesa una URL individual a través del pipeline completo.

            Returns:
                True si la URL fue insertada, False en cualquier otro caso.
            Raises:
                Exception si hay error de BD (el caller maneja el rollback).
            """
            nonlocal inserted, skipped_existing, normalized_count

            result = validate_and_normalize_booking_url(raw_url)

            if not result.is_valid:
                # Generar clave de razón de rechazo sin espacios para JSON limpio
                reason_key = (
                    result.rejection_reason
                    .split(":")[0]        # primera parte antes del detalle
                    .strip()
                    .lower()
                    .replace(" ", "_")
                    .replace("'", "")
                    [:50]                 # truncar para evitar claves largas
                )
                _record_rejection(reason_key, raw_url)
                return False

            canonical = result.canonical_url

            if result.was_normalized:
                normalized_count += 1
                logger.debug(
                    f"  🔧 URL normalizada: "
                    f"'{raw_url[-60:]}' → '{canonical[-60:]}'"
                )

            # INSERT idempotente: ON CONFLICT DO NOTHING garantiza que URLs
            # ya existentes no se sobrescriban ni generen errores.
            # La constraint UNIQUE(url) debe existir en url_queue.
            db_result = db.execute(
                text("""
                    INSERT INTO url_queue (
                        url, language, priority, status,
                        retry_count, max_retries, created_at, updated_at
                    )
                    VALUES (
                        :url, :lang, :pri, 'pending',
                        0, 3, NOW(), NOW()
                    )
                    ON CONFLICT (url) DO NOTHING
                """),
                {"url": canonical, "lang": language, "pri": priority}
            )

            if db_result.rowcount > 0:
                inserted += 1
                return True
            else:
                skipped_existing += 1
                return False

        if is_csv_with_header:
            # ── MODO CSV CON CABECERA ─────────────────────────────────────────
            reader = csv.DictReader(data_lines)
            for row_num, row in enumerate(reader, start=2):
                url_raw = (row.get("url") or row.get("URL") or "").strip()
                if not url_raw:
                    rejected["empty_url_in_csv"] = rejected.get("empty_url_in_csv", 0) + 1
                    continue
                # Sanitización del campo language: solo letras y guión
                language_raw = (row.get("language") or row.get("lang") or "en").strip()
                language = re.sub(r"[^a-zA-Z\-]", "", language_raw)[:10] or "en"
                # Sanitización del campo priority: solo enteros
                try:
                    priority = max(0, min(10, int(row.get("priority") or 5)))
                except (ValueError, TypeError):
                    priority = 5
                try:
                    _process_url(url_raw, language=language, priority=priority)
                except Exception as e:
                    logger.warning(
                        f"  ✗ Error BD fila {row_num} '{url_raw[:60]}': {e}"
                    )
                    errors.append(f"fila_{row_num}: {type(e).__name__}")
                    try:
                        db.rollback()
                    except Exception:
                        pass

        else:
            # ── MODO LISTA PLANA ──────────────────────────────────────────────
            for line_num, line in enumerate(data_lines, start=1):
                url_raw = line.strip()
                if not url_raw or url_raw.startswith("#"):
                    continue
                try:
                    _process_url(url_raw, language="en", priority=5)
                except Exception as e:
                    logger.warning(
                        f"  ✗ Error BD línea {line_num} '{url_raw[:60]}': {e}"
                    )
                    errors.append(f"linea_{line_num}: {type(e).__name__}")
                    try:
                        db.rollback()
                    except Exception:
                        pass

        db.commit()

        total_processed = inserted + skipped_existing + sum(rejected.values())

        logger.info(
            f"📥 Importación completada | "
            f"insertadas={inserted} | "
            f"ya_existían={skipped_existing} | "
            f"normalizadas={normalized_count} | "
            f"rechazadas={sum(rejected.values())} | "
            f"errores_bd={len(errors)}"
        )

        return {
            "inserted":         inserted,
            "skipped_existing": skipped_existing,
            "normalized_count": normalized_count,
            "rejected":         rejected,
            "total_rejected":   sum(rejected.values()),
            "errors":           errors,
            "format":           "csv_with_header" if is_csv_with_header else "plain_list",
        }

    except Exception as e:
        logger.error(f"Error crítico en /urls/load: {e}", exc_info=True)
        raise HTTPException(500, f"Error interno al procesar el archivo: {type(e).__name__}")


@app.post("/urls/reset-failed", tags=["URLs"])
def reset_failed_urls(db: Session = Depends(get_db)):
    """Resetea todas las URLs fallidas a 'pending' para reintentar."""
    try:
        r = db.execute(text(
            "UPDATE url_queue SET status='pending', retry_count=0, last_error=NULL, updated_at=NOW() "
            "WHERE status='failed'"
        ))
        db.commit()
        return {"reset": r.rowcount}
    except Exception as e:
        raise HTTPException(500, str(e))


# ─────────────────────────────────────────────────────────────────────────────
# [v4.0] COMPLETENESS — TRACKING POR IDIOMA
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/urls/{url_id}/completeness", tags=["URLs"])
def get_url_completeness(url_id: int, db: Session = Depends(get_db)):
    """
    [v4.0] Consulta el estado de completitud por idioma de una URL.

    Retorna:
      - is_complete: True si todos los idiomas del snapshot estan completados.
      - languages_ok: idiomas con status 'completed' o 'skipped_existing'.
      - languages_failed: idiomas con status 'failed' (reintentos agotados).
      - languages_missing: idiomas en LANGUAGES_ENABLED sin fila en tracking.
      - language_detail: detalle de cada idioma desde url_language_status.

    HTTP 404 si la URL no existe en url_queue.
    HTTP 503 si url_language_status no tiene filas (migracion pendiente).
    """
    try:
        # Verificar que la URL existe
        row = db.execute(
            text("SELECT url, status FROM url_queue WHERE id = :id"),
            {"id": url_id}
        ).fetchone()
        if not row:
            raise HTTPException(404, f"URL {url_id} no encontrada en url_queue")

        from app.completeness_service import completeness_service
        report = completeness_service.check_completeness(url_id, db)

        if not report.language_detail and not report.languages_missing:
            raise HTTPException(
                503,
                "url_language_status no tiene datos para esta URL. "
                "Verificar que migration_v2_url_language_status.sql fue ejecutada "
                "y que initialize_url_processing() fue llamada para esta URL."
            )

        return {
            "url_id":            url_id,
            "url":               row[0],
            "queue_status":      row[1],
            "is_complete":       report.is_complete,
            "languages_ok":      report.languages_ok,
            "languages_failed":  report.languages_failed,
            "languages_missing": report.languages_missing,
            "languages_pending": report.languages_pending,
            "language_detail": [
                {
                    "language":    d.language,
                    "status":      d.status,
                    "retry_count": d.retry_count,
                    "last_error":  d.last_error,
                }
                for d in report.language_detail
            ],
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))


@app.post("/urls/{url_id}/rollback", tags=["URLs"])
def rollback_url(
    url_id: int,
    keep_logs: bool = Body(default=True, embed=True),
    db: Session = Depends(get_db),
):
    """
    [v4.0] Revierte completamente una URL.

    OPERACION DESTRUCTIVA: Elimina todos los datos de hotels para esta URL,
    elimina el tracking de idiomas (url_language_status), elimina las imagenes
    del filesystem y resetea url_queue a status='pending'.

    HTTP 404 si la URL no existe.
    HTTP 409 si la URL esta en 'processing' (scraper activo).

    Parametros:
      keep_logs (bool, default=True): Si True, preserva scraping_logs para auditoria.
    """
    try:
        # Verificar existencia y estado
        row = db.execute(
            text("SELECT url, status FROM url_queue WHERE id = :id"),
            {"id": url_id}
        ).fetchone()
        if not row:
            raise HTTPException(404, f"URL {url_id} no encontrada en url_queue")
        if row[1] == "processing":
            raise HTTPException(
                409,
                f"URL {url_id} esta en 'processing'. "
                "Esperar a que el scraper termine o detenerlo antes del rollback."
            )

        from app.completeness_service import completeness_service
        result = completeness_service.rollback_url(url_id, keep_logs)

        if not result["success"]:
            raise HTTPException(500, result.get("error", "Error desconocido en rollback"))

        return {
            "url_id":           url_id,
            "url":              row[0],
            "success":          True,
            "hotels_deleted":   result["hotels_deleted"],
            "tracking_deleted": result["tracking_deleted"],
            "images_deleted":   result["images_deleted"],
            "keep_logs":        keep_logs,
            "new_status":       "pending",
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/urls/incomplete", tags=["URLs"])
def list_incomplete_urls(db: Session = Depends(get_db)):
    """
    [v4.0] Lista todas las URLs con idiomas fallidos.

    Detecta:
    - url_queue.status = 'incomplete' (marcadas por finalize_url()).
    - URLs con alguna fila en url_language_status con status = 'failed'.

    Incluye enlaces a los endpoints de completitud y rollback para cada URL.
    """
    try:
        rows = db.execute(
            text("""
                SELECT
                    q.id,
                    q.url,
                    q.status,
                    COALESCE(
                        ARRAY_AGG(uls.language ORDER BY uls.language)
                        FILTER (WHERE uls.status = 'failed'),
                        '{}'
                    ) AS failed_languages,
                    COALESCE(
                        ARRAY_AGG(uls.language ORDER BY uls.language)
                        FILTER (WHERE uls.status IN ('completed', 'skipped_existing')),
                        '{}'
                    ) AS ok_languages
                FROM url_queue q
                LEFT JOIN url_language_status uls ON uls.url_id = q.id
                WHERE q.status = 'incomplete'
                   OR EXISTS (
                       SELECT 1 FROM url_language_status x
                       WHERE x.url_id = q.id AND x.status = 'failed'
                   )
                GROUP BY q.id, q.url, q.status
                ORDER BY q.id DESC
            """)
        ).fetchall()

        result = []
        for r in rows:
            url_id_ = r[0]
            result.append({
                "url_id":              url_id_,
                "url":                 r[1],
                "queue_status":        r[2],
                "failed_languages":    r[3] or [],
                "ok_languages":        r[4] or [],
                "completeness_endpoint": f"/urls/{url_id_}/completeness",
                "rollback_endpoint":     f"/urls/{url_id_}/rollback",
            })

        return {
            "total":   len(result),
            "urls":    result,
        }
    except Exception as e:
        raise HTTPException(500, str(e))


# ─────────────────────────────────────────────────────────────────────────────
# SCRAPING
# ─────────────────────────────────────────────────────────────────────────────

@app.post("/scraping/start", tags=["Scraping"])
def scraping_start(
    # [FIX BUG-B-03] BackgroundTasks must NOT be instantiated as a default value.
    # `= BackgroundTasks()` created a single shared instance at function-definition
    # time (Python evaluates defaults once). FastAPI recognises the BackgroundTasks
    # type annotation and injects a fresh, request-scoped instance automatically.
    # Moved BEFORE defaulted parameters to satisfy Python's non-default-before-default rule.
    background_tasks: BackgroundTasks,
    batch_size: int = Query(default=5, ge=1, le=20),
):
    """
    Despacha un batch de URLs inmediatamente (además del auto-dispatcher).
    [FIX BUG-V6-009] batch_size is validated at API level (ge=1, le=20).
    Values outside this range return HTTP 422 automatically via FastAPI validation.
    The MAX_BATCH_SIZE=10 cap in process_batch() is an additional runtime guard;
    the effective batch size is min(batch_size, MAX_BATCH_SIZE).
    """
    from app.scraper_service import MAX_BATCH_SIZE
    effective_size = min(batch_size, MAX_BATCH_SIZE)

    def _run():
        from app.scraper_service import process_batch
        process_batch(effective_size)

    background_tasks.add_task(_run)
    return {
        "message": f"Batch de {effective_size} URLs despachado",
        "requested_batch_size": batch_size,
        "effective_batch_size": effective_size,
        "max_batch_size": MAX_BATCH_SIZE,
        "auto_dispatch": _dispatcher_running,
    }


# [FIX BUG-NEW-11] Lock para evitar ejecuciones concurrentes de force-now.
_force_now_lock = threading.Lock()

@app.post("/scraping/force-now", tags=["Scraping"])
def scraping_force_now(
    batch_size: int = Query(default=5, ge=1, le=20),
    _auth: None = Depends(_verify_api_key)
):
    """Despacha un batch sincrónicamente y devuelve el resultado.
    [FIX BUG-NEW-11] Protegido con threading.Lock — evita concurrencia descontrolada.
    """
    # [FIX BUG-NEW-11] No permitir llamadas concurrentes a force-now
    if not _force_now_lock.acquire(blocking=False):
        raise HTTPException(
            status_code=409,
            detail="Un batch force-now ya está en ejecución. Vuelve a intentarlo en unos segundos."
        )
    try:
        from app.scraper_service import process_batch
        result = process_batch(batch_size)
        return result
    finally:
        _force_now_lock.release()


@app.post("/scraping/test-url", tags=["Scraping"])
def test_url(
    url: str = Body(..., embed=True),
    language: str = Body(default="en", embed=True)
):
    """
    [DIAGNÓSTICO] Prueba la extracción de una URL concreta.
    Devuelve los datos extraídos SIN guardar en BD.
    Útil para verificar que el scraper funciona con una URL específica.
    """
    try:
        from app.scraper import BookingScraper
        with BookingScraper() as scraper:
            data = scraper.scrape_hotel(url, language=language)

        if not data:
            return {"success": False, "error": "No se obtuvieron datos — posible bloqueo o URL inválida"}

        return {
            "success":      bool(data.get("name")),
            "name":         data.get("name"),
            "address":      data.get("address"),
            "description":  (data.get("description") or "")[:200],
            "rating":       data.get("rating"),
            "total_reviews": data.get("total_reviews"),
            "images_count": len(data.get("images_urls") or []),
            "html_length":  data.get("html_length"),
            "http_status":  data.get("http_status"),
            "page_title":   data.get("page_title"),
        }
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/scraping/status", tags=["Scraping"])
def scraping_status(db: Session = Depends(get_db)):
    """Estado en tiempo real del sistema de scraping."""
    try:
        from app.scraper_service import get_service_stats, get_vpn_status

        queue = db.execute(text("SELECT status, COUNT(*) FROM url_queue GROUP BY status")).fetchall()
        q = {r[0]: r[1] for r in queue}

        processing_urls = db.execute(text("""
            SELECT id, url, updated_at FROM url_queue
            WHERE status = 'processing' ORDER BY updated_at DESC LIMIT 20
        """)).fetchall()

        last_completed = db.execute(text("""
            SELECT id, url, scraped_at FROM url_queue
            WHERE status = 'completed' ORDER BY scraped_at DESC NULLS LAST LIMIT 5
        """)).fetchall()

        last_logs = db.execute(text("""
            SELECT url_id, language, status, duration_seconds, error_message, timestamp
            FROM scraping_logs ORDER BY timestamp DESC LIMIT 10
        """)).fetchall()

        svc = get_service_stats()

        return {
            "dispatcher": {"running": _dispatcher_running, "cycle_seconds": 30},
            "queue": {
                "pending":    q.get("pending",    0),
                "processing": q.get("processing", 0),
                "completed":  q.get("completed",  0),
                "failed":     q.get("failed",     0),
                "incomplete": q.get("incomplete", 0),
            },
            "service": svc,
            "vpn": get_vpn_status(),
            "currently_processing": [
                {"id": r[0], "url": r[1][:80], "since": str(r[2])} for r in processing_urls
            ],
            "recently_completed": [
                {"id": r[0], "url": r[1][:80], "at": str(r[2])} for r in last_completed
            ],
            "recent_logs": [
                {"url_id": r[0], "lang": r[1], "status": r[2],
                 "duration_s": r[3], "error": r[4], "at": str(r[5])}
                for r in last_logs
            ],
        }
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/scraping/logs", tags=["Scraping"])
def get_logs(limit: int = 100, db: Session = Depends(get_db)):
    try:
        rows = db.execute(text("""
            SELECT id, url_id, language, status, duration_seconds, items_extracted,
                   error_message, timestamp
            FROM scraping_logs ORDER BY timestamp DESC LIMIT :lim
        """), {"lim": limit}).fetchall()
        return {
            "total": len(rows),
            "logs": [{"id": r[0], "url_id": r[1], "language": r[2], "status": r[3],
                      "duration_s": r[4], "items": r[5], "error": r[6], "timestamp": str(r[7])}
                     for r in rows]
        }
    except Exception as e:
        raise HTTPException(500, str(e))


# ─────────────────────────────────────────────────────────────────────────────
# HOTELS
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/hotels", tags=["Hotels"])
def list_hotels(skip: int = 0, limit: int = 100, language: Optional[str] = None,
                db: Session = Depends(get_db)):
    try:
        limit = min(limit, 500)
        params = {"limit": limit, "skip": skip}
        if language:
            q = text("SELECT id, url_id, name, language, address, rating, total_reviews, scraped_at "
                     "FROM hotels WHERE language=:lang ORDER BY scraped_at DESC LIMIT :limit OFFSET :skip")
            params["lang"] = language
        else:
            q = text("SELECT id, url_id, name, language, address, rating, total_reviews, scraped_at "
                     "FROM hotels ORDER BY scraped_at DESC LIMIT :limit OFFSET :skip")
        rows = db.execute(q, params).fetchall()
        return {"total": len(rows), "hotels": [
            {"id": r[0], "url_id": r[1], "name": r[2], "language": r[3], "address": r[4],
             "rating": float(r[5]) if r[5] else None, "reviews": r[6], "scraped_at": str(r[7])}
            for r in rows]}
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/hotels/search/", tags=["Hotels"])
def search_hotels(q: str = Query(..., min_length=2), db: Session = Depends(get_db)):
    try:
        rows = db.execute(text(
            "SELECT id, url_id, name, language, address, rating, total_reviews "
            "FROM hotels WHERE LOWER(name) LIKE :q ORDER BY name LIMIT 50"
        ), {"q": f"%{q.lower()}%"}).fetchall()
        return {"query": q, "total": len(rows), "hotels": [
            {"id": r[0], "url_id": r[1], "name": r[2], "language": r[3],
             "address": r[4], "rating": float(r[5]) if r[5] else None, "reviews": r[6]}
            for r in rows]}
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/hotels/{hotel_id}", tags=["Hotels"])
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    try:
        row = db.execute(text("SELECT * FROM hotels WHERE id=:id"), {"id": hotel_id}).fetchone()
        if not row:
            raise HTTPException(404, "Hotel no encontrado")
        return dict(row._mapping)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))


# ─────────────────────────────────────────────────────────────────────────────
# EXPORT
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/export/csv", tags=["Export"])
def export_csv(language: Optional[str] = None, db: Session = Depends(get_db)):
    try:
        p = Path(settings.EXPORTS_PATH)
        p.mkdir(parents=True, exist_ok=True)
        fname = f"hotels_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.csv"
        fpath = p / fname
        params = {}
        if language:
            q = text("SELECT * FROM hotels WHERE language=:lang ORDER BY name")
            params["lang"] = language
        else:
            q = text("SELECT * FROM hotels ORDER BY name, language")
        rows = db.execute(q, params).fetchall()
        with open(fpath, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            if rows:
                w.writerow(rows[0]._mapping.keys())
                for r in rows:
                    w.writerow(list(r._mapping.values()))
        return FileResponse(fpath, media_type="text/csv", filename=fname)
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/export/json", tags=["Export"])
def export_json(language: Optional[str] = None, db: Session = Depends(get_db)):
    try:
        params = {}
        if language:
            q = text("SELECT * FROM hotels WHERE language=:lang ORDER BY name")
            params["lang"] = language
        else:
            q = text("SELECT * FROM hotels ORDER BY name, language")
        rows = db.execute(q, params).fetchall()
        return {"total": len(rows), "hotels": [dict(r._mapping) for r in rows]}
    except Exception as e:
        raise HTTPException(500, str(e))


# ─────────────────────────────────────────────────────────────────────────────
# SYSTEM
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/system/info", tags=["System"])
def system_info():
    import platform
    return {
        "platform": platform.system(), "python": platform.python_version(),
        "app_version": "6.0.0",  # [FIX REGRESS-03/BUG-05]
        "config": {
            "languages": settings.ENABLED_LANGUAGES,
            "batch_size": settings.BATCH_SIZE,
            "max_concurrent": settings.MAX_CONCURRENT_TASKS,
            "use_selenium": settings.USE_SELENIUM,
            "vpn_enabled": settings.VPN_ENABLED,
            "download_images": settings.DOWNLOAD_IMAGES,
        }
    }


@app.get("/system/logs", tags=["System"])
def get_system_logs(lines: int = Query(default=100, ge=1, le=1000)):
    try:
        log_file = Path(settings.LOGS_PATH) / "api.log"
        if not log_file.exists():
            return {"logs": [], "note": "Archivo de log no encontrado"}
        with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
            all_lines = f.readlines()
        return {"total": len(all_lines), "logs": all_lines[-lines:]}
    except Exception as e:
        raise HTTPException(500, str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)
