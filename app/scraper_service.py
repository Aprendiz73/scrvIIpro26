"""
BookingScraper/app/scraper_service.py  v6.0  [COMPLETENESS TRACKING + LANGUAGE SNAPSHOT]
Servicio de scraping directo - BookingScraper Pro

CAMBIOS v6.0 [COMPLETENESS TRACKING + LANGUAGE SNAPSHOT]:

  PROBLEMA RESUELTO:
  - El sistema marcaba una URL como 'completed' si scraped_count > 0.
    1/5 idiomas era indistinguible de 5/5 idiomas.
  - Si LANGUAGES_ENABLED cambiaba con el scraper activo, las URLs ya
    inicializadas podian recibir idiomas nuevos (violacion de regla de negocio).

  [NUEVO] completeness_service: tracking por idioma en url_language_status.
  [NUEVO] _get_languages_for_url(): Lee idiomas desde SNAPSHOT en url_language_status,
    NO desde settings.ENABLED_LANGUAGES. Si LANGUAGES_ENABLED cambia mientras el
    scraper corre, las URLs ya inicializadas procesan sus idiomas originales.
  [NUEVO] Retry por idioma: hasta MAX_LANG_RETRIES intentos antes de 'failed'.
  [NUEVO] url_queue.status 'incomplete': URLs con algun idioma fallido tras reintentos.
  [NUEVO] process_batch() limita a MAX_BATCH_SIZE=10 URLs por ciclo.

CAMBIOS v5.1 [FIX NO-OVERWRITE + images_count]:
  [FIX #36] _save_hotel(): ON CONFLICT DO NOTHING
  [FIX #37] _save_hotel(): images_count=0 explicito en INSERT.

CAMBIOS v5.0: VPN UK-first para en-gb.
CAMBIOS v4.0: Bloquear guardado en idioma incorrecto.
CAMBIOS v3.1: imagenes del primer idioma exitoso.
CAMBIOS v2.x: mejoras incrementales.
"""

import json
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional, Set
from loguru import logger

from sqlalchemy import text

from app.database import SessionLocal
from app.config import settings
from app.completeness_service import completeness_service, MAX_LANG_RETRIES


# Pool de threads
_executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="scraper")
_lock = threading.Lock()
_active_ids: Set[int] = set()
_stats = {
    "total_dispatched": 0,
    "total_completed": 0,
    "total_failed": 0,
    "currently_processing": 0,
    "consecutive_failures": 0,
    "hotels_since_vpn_rotate": 0,
    "lang_mismatch_count": 0,
    "lang_mismatch_blocked": 0,
}
_MAX_LANG_RETRY = 2
_stats_lock = threading.Lock()

# [v6.0] Limite maximo de URLs por batch (regla de negocio)
MAX_BATCH_SIZE: int = 10

_vpn_manager = None
_vpn_lock = threading.Lock()


def _get_vpn_manager():
    """Devuelve el VPN manager singleton (thread-safe)."""
    global _vpn_manager
    if not settings.VPN_ENABLED:
        return None
    with _vpn_lock:
        if _vpn_manager is None:
            try:
                from app.vpn_manager import vpn_manager_factory
                _vpn_manager = vpn_manager_factory(interactive=False)
                logger.info("VPN Manager iniciado (singleton)")
            except Exception as e:
                logger.error(f"Error iniciando VPN Manager: {e}")
                _vpn_manager = None
    return _vpn_manager


def rotate_vpn_now() -> Dict:
    """Rota la VPN inmediatamente. Llamado desde /vpn/rotate."""
    vpn = _get_vpn_manager()
    if not vpn:
        return {"success": False, "reason": "VPN_ENABLED=False o VPN no disponible"}
    with _vpn_lock:
        try:
            logger.info("Rotacion VPN manual solicitada...")
            success = vpn.rotate()
            with _stats_lock:
                _stats["consecutive_failures"] = 0
                _stats["hotels_since_vpn_rotate"] = 0
            return {"success": success, "new_ip": vpn.current_ip, "server": vpn.current_server}
        except Exception as e:
            logger.error(f"Error rotando VPN: {e}")
            return {"success": False, "error": str(e)}


def get_vpn_status() -> Dict:
    """Estado de la VPN. Llamado desde /vpn/status."""
    vpn = _get_vpn_manager()
    if not vpn:
        return {"enabled": False, "reason": "VPN_ENABLED=False en .env"}
    try:
        return {
            "enabled": True,
            **vpn.get_status(),
            "hotels_since_rotate": _stats.get("hotels_since_vpn_rotate", 0),
            "consecutive_failures": _stats.get("consecutive_failures", 0),
        }
    except Exception as e:
        return {"enabled": True, "error": str(e)}


def _maybe_rotate_vpn(force: bool = False):
    """Rota la VPN si se supero el limite o hay demasiados fallos."""
    vpn = _get_vpn_manager()
    if not vpn:
        return
    with _stats_lock:
        consec = _stats["consecutive_failures"]
        since_rotate = _stats["hotels_since_vpn_rotate"]
    rotate_every = getattr(settings, "VPN_ROTATE_EVERY_N", 10)
    too_many_failures = consec >= 3
    if not (force or since_rotate >= rotate_every or too_many_failures):
        return
    reason = "manual" if force else ("bloqueo_ip" if too_many_failures else "periodica")
    logger.info(f"Rotando VPN (motivo={reason}, fallos={consec}, hoteles={since_rotate})...")
    with _vpn_lock:
        try:
            success = vpn.rotate()
            if success:
                with _stats_lock:
                    _stats["consecutive_failures"] = 0
                    _stats["hotels_since_vpn_rotate"] = 0
                logger.success(f"VPN rotada -> IP: {vpn.current_ip}")
            else:
                logger.warning("Rotacion VPN fallo - continuando con IP actual")
        except Exception as e:
            logger.error(f"Error en rotacion VPN: {e}")


# =============================================================================
# [v6.0] HELPER: LEER IDIOMAS DESDE SNAPSHOT EN url_language_status
# =============================================================================

def _get_languages_for_url(db, url_id: int) -> List[str]:
    """
    Lee los idiomas a procesar para una URL desde url_language_status.

    FUENTE DE VERDAD: El snapshot registrado por initialize_url_processing()
    al momento de la carga. Garantiza que si LANGUAGES_ENABLED cambia
    mientras el scraper corre, las URLs ya inicializadas no se ven afectadas.

    ORDENAMIENTO: DEFAULT ('en') siempre primero, resto alfabetico.

    FALLBACK: Si no hay snapshot (URL pre-migracion), usa settings.ENABLED_LANGUAGES.
    """
    DEFAULT = settings.DEFAULT_LANGUAGE  # "en"
    try:
        rows = db.execute(
            text("""
                SELECT language
                FROM   url_language_status
                WHERE  url_id = :url_id
                ORDER BY
                    CASE WHEN language = :default_lang THEN 0 ELSE 1 END,
                    language
            """),
            {"url_id": url_id, "default_lang": DEFAULT}
        ).fetchall()

        if rows:
            languages = [r[0] for r in rows]
            logger.debug(f"  [{url_id}] Idiomas desde snapshot: {languages}")
            return languages

        # Fallback: URL sin snapshot (pre-migracion)
        logger.warning(
            f"  [{url_id}] Sin snapshot en url_language_status. "
            f"Usando settings.ENABLED_LANGUAGES como fallback."
        )
        fallback = list(settings.ENABLED_LANGUAGES)
        if DEFAULT in fallback:
            return [DEFAULT] + [l for l in fallback if l != DEFAULT]
        return [DEFAULT] + fallback

    except Exception as e:
        logger.error(f"  [{url_id}] Error leyendo idiomas desde snapshot: {e}. Fallback.")
        fallback = list(settings.ENABLED_LANGUAGES)
        if DEFAULT in fallback:
            return [DEFAULT] + [l for l in fallback if l != DEFAULT]
        return [DEFAULT] + fallback


# =============================================================================
# PUNTO DE ENTRADA: PROCESAR BATCH
# =============================================================================

def process_batch(batch_size: int = 5) -> Dict:
    """
    Obtiene URLs pendientes de la BD y las envia al thread pool.
    Thread-safe. Puede llamarse desde asyncio (via run_in_executor).

    [v6.0] Hard cap: batch_size no puede superar MAX_BATCH_SIZE (10).
    """
    # [v6.0] Cap de batch size
    if batch_size > MAX_BATCH_SIZE:
        logger.warning(
            f"batch_size={batch_size} supera MAX_BATCH_SIZE={MAX_BATCH_SIZE}. Reduciendo."
        )
        batch_size = MAX_BATCH_SIZE

    # [FIX v5.0] VPN al iniciar: preferir UK para en-gb
    vpn = _get_vpn_manager()
    if vpn and settings.VPN_ENABLED:
        try:
            if not vpn.verify_vpn_active():
                logger.warning("VPN inactiva al procesar batch - conectando a UK...")
                success = vpn.connect("UK")
                if not success:
                    logger.warning("Conexion a UK fallo - intentando cualquier pais...")
                    vpn.connect()
        except Exception as e:
            logger.warning(f"Error verificando VPN: {e}")

    db = SessionLocal()
    try:
        # [FIX BUG-09] SELECT ... FOR UPDATE SKIP LOCKED garantiza exclusión
        # mutua a nivel de base de datos para múltiples procesos concurrentes
        # (asyncio dispatcher + Celery beat simultáneos).
        # ANTES: SELECT sin bloqueo → race condition entre procesos distintos
        # → misma URL procesada dos veces con doble petición HTTP al mismo hotel.
        # AHORA: PostgreSQL bloquea las filas seleccionadas; otros procesos las
        # saltan (SKIP LOCKED) y toman otras URLs del pool.
        rows = db.execute(
            text("""
                SELECT id FROM url_queue
                WHERE  status = 'pending'
                  AND  retry_count < max_retries
                ORDER BY priority DESC, created_at ASC
                LIMIT  :limit
                FOR UPDATE SKIP LOCKED
            """),
            {"limit": batch_size}
        ).fetchall()

        url_ids = [r[0] for r in rows]

        if not url_ids:
            logger.debug("No hay URLs pendientes para despachar")
            return {"dispatched": 0, "message": "No hay URLs pendientes"}

        with _lock:
            new_ids = [uid for uid in url_ids if uid not in _active_ids]
            _active_ids.update(new_ids)

        if not new_ids:
            return {"dispatched": 0, "message": "Todas las URLs ya estan en proceso"}

        for uid in new_ids:
            db.execute(
                text("UPDATE url_queue SET status = 'processing', updated_at = NOW() WHERE id = :id"),
                {"id": uid}
            )
        db.commit()

        for uid in new_ids:
            _executor.submit(_run_safe, uid)

        with _stats_lock:
            _stats["total_dispatched"] += len(new_ids)
            _stats["currently_processing"] += len(new_ids)

        logger.info(f"Despachadas {len(new_ids)} URLs al thread pool")
        return {"dispatched": len(new_ids), "url_ids": new_ids}

    except Exception as e:
        logger.error(f"Error en process_batch: {e}")
        return {"dispatched": 0, "error": str(e)}
    finally:
        db.close()


# =============================================================================
# SCRAPING DE UN HOTEL INDIVIDUAL
# =============================================================================

def _run_safe(url_id: int):
    """Wrapper que libera el ID del set _active_ids al terminar."""
    try:
        scrape_one(url_id)
    except Exception as e:
        logger.error(f"Error inesperado en _run_safe({url_id}): {e}")
    finally:
        with _lock:
            _active_ids.discard(url_id)
        with _stats_lock:
            _stats["currently_processing"] = max(0, _stats["currently_processing"] - 1)


def scrape_one(url_id: int) -> Dict:
    """
    Scrapea un hotel completo en todos los idiomas del snapshot.

    [v6.0] CAMBIOS CRITICOS:
    - initialize_url_processing(): registra snapshot de idiomas en url_language_status.
    - _get_languages_for_url(): lee idiomas desde snapshot, no desde settings.
    - Retry loop por idioma: hasta MAX_LANG_RETRIES intentos adicionales.
    - record_language_success/skipped/failure(): tracking granular por idioma.
    - finalize_url(): determina completed (todos OK) o incomplete (algun fallo).

    [v2.1] Con Selenium: crea UN SOLO driver por hotel.
    """
    db = SessionLocal()
    start_time = time.time()
    DEFAULT = settings.DEFAULT_LANGUAGE  # "en"

    try:
        row = db.execute(
            text("SELECT url, language FROM url_queue WHERE id = :id"),
            {"id": url_id}
        ).fetchone()

        if not row:
            logger.error(f"URL ID {url_id} no encontrada en url_queue")
            return {"error": "URL no encontrada"}

        base_url   = row[0]
        queue_lang = row[1] or "en"
        logger.info(f"\n{chr(8212)*60}")
        logger.info(f"Iniciando scraping | ID={url_id} | lang_queue={queue_lang} | {base_url}")
        logger.info(f"{chr(8212)*60}")

        # VPN check
        vpn = _get_vpn_manager()
        if vpn and settings.VPN_ENABLED:
            try:
                with _vpn_lock:
                    vpn.reconnect_if_disconnected()
            except Exception as vpn_err:
                logger.warning(f"VPN check error: {vpn_err}")

        from app.scraper import BookingScraper, build_language_url

        # [v6.0] Snapshot de idiomas en url_language_status (idempotente)
        completeness_service.initialize_url_processing(url_id, db)
        db.commit()

        # [v6.0] Leer idiomas desde snapshot -- NO desde settings.ENABLED_LANGUAGES
        languages = _get_languages_for_url(db, url_id)

        scraped_count     = 0
        hotel_name        = None
        lang_failures     = 0
        images_downloaded = False

        if settings.USE_SELENIUM:
            scraper_instance = BookingScraper()
        else:
            scraper_instance = None

        try:
            for lang in languages:
                lang_url = build_language_url(base_url, lang)
                logger.info(f"  -> [{url_id}] Idioma [{lang}]: {lang_url}")

                lang_succeeded = False

                # [v6.0] Retry loop por idioma
                # range(1, MAX_LANG_RETRIES+2) = [1,2] con MAX_LANG_RETRIES=1
                for attempt in range(1, MAX_LANG_RETRIES + 2):
                    try:
                        if settings.USE_SELENIUM:
                            data = scraper_instance.scrape_hotel(lang_url, language=lang)
                        else:
                            with BookingScraper() as scraper:
                                data = scraper.scrape_hotel(lang_url, language=lang)

                        # Sin datos
                        if not data or not data.get("name"):
                            logger.warning(f"  [{url_id}][{lang}] Sin datos (attempt={attempt})")
                            _log(db, url_id, lang, "no_data",
                                 time.time() - start_time, 0, "Sin datos extraidos")
                            has_retry = completeness_service.record_language_failure(
                                url_id, lang, "Sin datos extraidos", db
                            )
                            db.commit()
                            if has_retry and attempt <= MAX_LANG_RETRIES:
                                logger.info(f"  [{url_id}][{lang}] Reintentando (attempt {attempt+1})...")
                                continue
                            else:
                                lang_failures += 1
                                break

                        if hotel_name is None:
                            hotel_name = data["name"]

                        # Verificacion de idioma detectado
                        detected = data.get("detected_lang")
                        if detected and detected != lang:
                            logger.error(
                                f"  [{url_id}][{lang}] IDIOMA INCORRECTO - NO SE GUARDA: "
                                f"solicitado='{lang}', pagina en '{detected}'"
                            )
                            with _stats_lock:
                                _stats["lang_mismatch_count"] = _stats.get("lang_mismatch_count", 0) + 1
                                _stats["lang_mismatch_blocked"] = _stats.get("lang_mismatch_blocked", 0) + 1

                            _log(db, url_id, lang, "lang_mismatch",
                                 time.time() - start_time, 0,
                                 f"Pagina en '{detected}', solicitado '{lang}'. NO guardado.")

                            has_retry = completeness_service.record_language_failure(
                                url_id, lang,
                                f"lang_mismatch: solicitado={lang} detectado={detected}", db
                            )
                            db.commit()

                            if lang == DEFAULT and _stats.get("lang_mismatch_count", 0) >= 3:
                                logger.warning(f"  [{url_id}] Mismatches acumulados - rotando VPN...")
                                _maybe_rotate_vpn(force=True)
                                with _stats_lock:
                                    _stats["lang_mismatch_count"] = 0

                            if has_retry and attempt <= MAX_LANG_RETRIES:
                                logger.info(
                                    f"  [{url_id}][{lang}] Reintentando por mismatch "
                                    f"(attempt {attempt+1})..."
                                )
                                continue
                            else:
                                lang_failures += 1
                                break
                        else:
                            with _stats_lock:
                                _stats["lang_mismatch_count"] = 0

                        # Guardar en BD
                        saved = _save_hotel(db, url_id, lang_url, lang, data)

                        if saved:
                            scraped_count += 1
                            lang_failures  = 0
                            completeness_service.record_language_success(url_id, lang, db)
                            db.commit()
                        else:
                            logger.debug(
                                f"  [{url_id}][{lang}] Registro ya existe - "
                                f"preservando (ON CONFLICT DO NOTHING)"
                            )
                            scraped_count += 1
                            completeness_service.record_language_skipped(url_id, lang, db)
                            db.commit()

                        duration   = time.time() - start_time
                        imgs_count = len(data.get("images_urls") or [])
                        _log(db, url_id, lang, "completed", duration, 1)

                        logger.success(
                            f"  [{url_id}][{lang}] '{hotel_name}' "
                            f"| rating={data.get('rating')} | imgs={imgs_count}"
                        )

                        # Descarga de imagenes: solo lang=DEFAULT confirmado
                        if lang == DEFAULT and not images_downloaded and settings.DOWNLOAD_IMAGES:
                            imgs = data.get("images_urls") or []
                            if imgs:
                                driver = scraper_instance.driver if settings.USE_SELENIUM else None
                                n_downloaded = _download_images(url_id, imgs, DEFAULT, driver=driver)
                                if n_downloaded and n_downloaded > 0:
                                    try:
                                        # [FIX BUG-03] Actualizar images_count E images_local.
                                        # ANTES: solo se actualizaba images_count; images_local
                                        # quedaba NULL permanentemente aunque hubiera archivos en disco.
                                        # AHORA: también se persisten las rutas locales de las imágenes.
                                        from app.image_downloader import ImageDownloader as _IDL
                                        local_paths = _IDL.get_local_paths(url_id, lang=DEFAULT)
                                        db.execute(
                                            text("""
                                                UPDATE hotels
                                                SET images_count = :count,
                                                    images_local = CAST(:local_paths AS jsonb),
                                                    updated_at   = NOW()
                                                WHERE url_id = :url_id AND language = :lang
                                            """),
                                            {
                                                "count":       n_downloaded,
                                                "local_paths": json.dumps(local_paths),
                                                "url_id":      url_id,
                                                "lang":        DEFAULT,
                                            }
                                        )
                                        db.commit()
                                    except Exception as upd_err:
                                        logger.debug(f"  No se pudo actualizar images_count/local: {upd_err}")
                            images_downloaded = True

                        lang_succeeded = True
                        break  # exito -> salir del retry loop

                    except Exception as lang_err:
                        err_str = str(lang_err)
                        logger.error(f"  [{url_id}][{lang}] attempt={attempt}: {err_str[:200]}")
                        try:
                            db.rollback()
                        except Exception:
                            pass

                        # Brave crasheo -> recrear driver y reintentar
                        if settings.USE_SELENIUM and "invalid session id" in err_str.lower():
                            logger.warning(f"  [{url_id}][{lang}] Brave crasheo - recreando driver...")
                            try:
                                scraper_instance.close()
                            except Exception:
                                pass
                            try:
                                scraper_instance = BookingScraper()
                                data = scraper_instance.scrape_hotel(lang_url, language=lang)
                                if data and data.get("name"):
                                    if hotel_name is None:
                                        hotel_name = data["name"]
                                    saved = _save_hotel(db, url_id, lang_url, lang, data)
                                    scraped_count += 1
                                    lang_failures  = 0
                                    duration = time.time() - start_time
                                    _log(db, url_id, lang, "completed", duration,
                                         len(data.get("images_urls") or []))
                                    if saved:
                                        completeness_service.record_language_success(url_id, lang, db)
                                    else:
                                        completeness_service.record_language_skipped(url_id, lang, db)
                                    db.commit()
                                    logger.success(f"  [{url_id}][{lang}] '{hotel_name}' (recuperado)")
                                    if not images_downloaded and settings.DOWNLOAD_IMAGES:
                                        imgs = data.get("images_urls") or []
                                        if imgs:
                                            drv = scraper_instance.driver if settings.USE_SELENIUM else None
                                            n_dl = _download_images(url_id, imgs, DEFAULT, driver=drv)
                                            if n_dl and n_dl > 0:
                                                try:
                                                    # [FIX BUG-03] También actualizar images_local aquí
                                                    from app.image_downloader import ImageDownloader as _IDL2
                                                    local_paths = _IDL2.get_local_paths(url_id, lang=DEFAULT)
                                                    db.execute(
                                                        text(
                                                            "UPDATE hotels "
                                                            "SET images_count=:c, "
                                                            "    images_local=CAST(:lp AS jsonb), "
                                                            "    updated_at=NOW() "
                                                            "WHERE url_id=:u AND language=:lang"
                                                        ),
                                                        {"c": n_dl, "lp": json.dumps(local_paths),
                                                         "u": url_id, "lang": DEFAULT}
                                                    )
                                                    db.commit()
                                                except Exception:
                                                    pass
                                        images_downloaded = True
                                    lang_succeeded = True
                                    break
                            except Exception as retry_err:
                                logger.error(f"  [{url_id}][{lang}] Reintento tras crash fallido: {retry_err}")
                                try:
                                    db.rollback()
                                except Exception:
                                    pass

                        _log(db, url_id, lang, "error", time.time() - start_time, 0, err_str[:500])
                        has_retry = completeness_service.record_language_failure(
                            url_id, lang, err_str, db
                        )
                        try:
                            db.commit()
                        except Exception:
                            pass

                        if has_retry and attempt <= MAX_LANG_RETRIES:
                            logger.info(
                                f"  [{url_id}][{lang}] Reintentando tras error "
                                f"(attempt {attempt+1})..."
                            )
                            continue
                        else:
                            lang_failures += 1
                            if lang_failures >= 3:
                                logger.warning(f"  [{url_id}] {lang_failures} fallos - posible bloqueo IP")
                                with _stats_lock:
                                    _stats["consecutive_failures"] += 1
                                _maybe_rotate_vpn()
                            break

                if not lang_succeeded:
                    logger.warning(f"  [{url_id}][{lang}] Idioma fallido definitivamente.")

        finally:
            if settings.USE_SELENIUM and scraper_instance is not None:
                try:
                    scraper_instance.close()
                    logger.debug(f"  Driver Selenium cerrado para hotel {url_id}")
                except Exception:
                    pass

        # [v6.0] Finalizacion via completeness_service
        # Evalua completitud -> actualiza url_queue a 'completed' o 'incomplete'
        try:
            report       = completeness_service.finalize_url(url_id, db)
            final_status = "completed" if report.is_complete else "incomplete"
        except Exception as finalize_err:
            logger.error(f"[{url_id}] Error en finalize_url: {finalize_err}")
            final_status = "completed" if scraped_count > 0 else "failed"
            db.execute(
                text("""
                    UPDATE url_queue
                    SET status = :status, scraped_at = NOW(), updated_at = NOW()
                    WHERE id = :id
                """),
                {"status": final_status, "id": url_id}
            )
            db.commit()

        total_dur = time.time() - start_time

        if scraped_count > 0:
            with _stats_lock:
                _stats["total_completed"] += 1
                _stats["consecutive_failures"] = 0
                _stats["hotels_since_vpn_rotate"] += 1
            _maybe_rotate_vpn()
            logger.success(
                f"[{url_id}] {final_status.upper()} | '{hotel_name}' "
                f"| {scraped_count}/{len(languages)} idiomas | {total_dur:.1f}s"
            )
        else:
            with _stats_lock:
                _stats["total_failed"] += 1
                _stats["consecutive_failures"] += 1
            _maybe_rotate_vpn()
            logger.error(f"[{url_id}] FALLIDO | {total_dur:.1f}s")

        return {
            "success":    scraped_count > 0,
            "hotel_name": hotel_name,
            "languages":  scraped_count,
            "duration":   round(total_dur, 2),
            "status":     final_status,
        }

    except Exception as e:
        logger.error(f"Error fatal URL {url_id}: {e}", exc_info=True)
        db.rollback()
        with _stats_lock:
            _stats["total_failed"] += 1
            _stats["consecutive_failures"] += 1
        _maybe_rotate_vpn()
        try:
            db.execute(
                text("""
                    UPDATE url_queue
                    SET status = CASE
                            WHEN retry_count + 1 >= max_retries THEN 'failed'
                            ELSE 'pending'
                        END,
                        retry_count = retry_count + 1,
                        last_error  = :error,
                        updated_at  = NOW()
                    WHERE id = :id
                """),
                {"id": url_id, "error": str(e)[:500]}
            )
            db.commit()
        except Exception:
            pass
        return {"error": str(e)}

    finally:
        db.close()


# =============================================================================
# HELPERS INTERNOS
# =============================================================================

def _save_hotel(db, url_id: int, url: str, lang: str, data: Dict) -> bool:
    """
    Inserta un hotel. ON CONFLICT DO NOTHING preserva datos existentes.
    Returns True si se inserto nuevo registro, False si ya existia.
    """
    result = db.execute(
        text("""
            INSERT INTO hotels (
                url_id, url, language,
                name, address, description,
                rating, total_reviews, rating_category,
                review_scores, services, facilities,
                house_rules, important_info,
                rooms_info, images_urls, images_count,
                scraped_at, updated_at
            ) VALUES (
                :url_id, :url, :language,
                :name, :address, :description,
                :rating, :total_reviews, :rating_category,
                CAST(:review_scores AS jsonb), CAST(:services AS jsonb), CAST(:facilities AS jsonb),
                :house_rules, :important_info,
                CAST(:rooms_info AS jsonb), CAST(:images_urls AS jsonb), 0,
                NOW(), NOW()
            )
            ON CONFLICT (url_id, language) DO NOTHING
        """),
        {
            "url_id":           url_id,
            "url":              url,
            "language":         lang,
            "name":             data.get("name"),
            "address":          data.get("address"),
            "description":      data.get("description"),
            "rating":           data.get("rating"),
            "total_reviews":    data.get("total_reviews"),
            "rating_category":  data.get("rating_category"),
            "review_scores":    json.dumps(data.get("review_scores") or {}),
            "services":         json.dumps(data.get("services")      or []),
            "facilities":       json.dumps(data.get("facilities")    or {}),
            "house_rules":      data.get("house_rules"),
            "important_info":   data.get("important_info"),
            "rooms_info":       json.dumps(data.get("rooms")         or []),
            "images_urls":      json.dumps(data.get("images_urls")   or []),
        }
    )
    db.commit()
    return result.rowcount > 0


def _download_images(url_id: int, img_urls: List[str], lang: str, driver=None) -> int:
    """Descarga imagenes usando cookies del browser Brave."""
    if not img_urls:
        return 0
    try:
        from app.image_downloader import ImageDownloader
        import requests as _req
        session = _req.Session()
        session.headers.update({
            "User-Agent":      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Referer":         "https://www.booking.com/",
            "Accept":          "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9,*;q=0.5",
            "sec-fetch-dest":  "image",
            "sec-fetch-mode":  "no-cors",
            "sec-fetch-site":  "cross-site",
        })
        if driver:
            try:
                browser_cookies = driver.get_cookies()
                for c in browser_cookies:
                    session.cookies.set(c["name"], c["value"], domain=c.get("domain", ".booking.com"))
            except Exception as ce:
                logger.debug(f"  [{url_id}] No se pudieron extraer cookies: {ce}")
        dl = ImageDownloader()
        results = dl.download_images(url_id, img_urls, language=lang, session=session)
        ok = len(results)
        logger.info(f"  [{url_id}] {ok}/{len(img_urls)} imagenes descargadas")
        return ok
    except Exception as e:
        logger.warning(f"  Error descargando imagenes [{url_id}]: {e}")
        return 0


def _log(db, url_id: int, language: str, status: str,
         duration: float, items: int, error: str = None):
    """Inserta una linea en scraping_logs."""
    try:
        db.execute(
            text("""
                INSERT INTO scraping_logs
                    (url_id, language, status, duration_seconds,
                     items_extracted, error_message, timestamp)
                VALUES
                    (:url_id, :lang, :status, :dur, :items, :error, NOW())
            """),
            {"url_id": url_id, "lang": language, "status": status,
             "dur": round(duration, 2), "items": items, "error": error}
        )
        db.commit()
    except Exception as e:
        logger.debug(f"No se pudo insertar log: {e}")


# =============================================================================
# ESTADO DEL SERVICIO
# =============================================================================

def get_service_stats() -> Dict:
    """Devuelve estadisticas en tiempo real del servicio de scraping."""
    with _lock:
        active = list(_active_ids)
    with _stats_lock:
        s = _stats.copy()
    s["active_ids"]   = active
    s["active_count"] = len(active)
    return s
