"""
BookingScraper/app/tasks.py  v4.0  [COMPLETENESS TRACKING + LANGUAGE SNAPSHOT]
Tareas Celery para scraping asincrono - BookingScraper Pro
Windows 11 + Python 3.14.3

CAMBIOS v4.0 [COMPLETENESS TRACKING + LANGUAGE SNAPSHOT]:

  [NUEVO] scrape_hotel_task(): Lee idiomas desde snapshot en url_language_status
    (_get_languages_for_url) en lugar de settings.ENABLED_LANGUAGES directamente.
    GARANTIA: Si LANGUAGES_ENABLED cambia, las tareas ya encoladas procesan sus
    idiomas originales (del snapshot registrado en initialize_url_processing).

  [NUEVO] Integra completeness_service:
    - initialize_url_processing() al inicio de scrape_hotel_task().
    - record_language_success/skipped/failure() en el loop de idiomas.
    - finalize_url() reemplaza el UPDATE directo de url_queue.status.

  [NUEVO] process_pending_urls(): batch_size limitado a MAX_BATCH_SIZE=10.

  [NUEVO] rollback_url_task(): Celery task para revertir una URL (BD + filesystem).
    max_retries=0: accion deliberada del operador, no se reintenta automaticamente.

  [NUEVO] get_url_completeness_task(): Consulta el estado de completitud de una URL.

  [NUEVO] check_incomplete_urls_task(): Lista URLs con idiomas fallidos para
    dashboard del operador. Configurable en beat_schedule cada 6 horas.

CAMBIOS v3.0 [FIX NO-OVERWRITE]:
  [FIX #38] Hotel INSERT: ON CONFLICT DO NOTHING (preserva datos existentes).
  [FIX #39] images_count gestionado en UPDATE posterior, no en INSERT.

CAMBIOS v2.2:
  [FIX] images_count calculado con len(images_urls).
  [FIX] Descarga de imagenes: eliminado limite artificial [:30].

CAMBIOS v1.1:
  [FIX] url_id en INSERT hotels, scraped_at, review_scores/services/facilities JSON real.
  [NEW] save_system_metrics(), cleanup_old_logs().
"""

import json
import time
import psutil
from datetime import datetime, timedelta

from sqlalchemy import text
from loguru import logger

from app.celery_app import celery_app
from app.database import SessionLocal
from app.config import settings
from app.completeness_service import completeness_service, MAX_LANG_RETRIES
from app.scraper_service import _get_languages_for_url, MAX_BATCH_SIZE


# =============================================================================
# TAREA PRINCIPAL: SCRAPING DE UN HOTEL
# =============================================================================

@celery_app.task(bind=True, max_retries=3, name="app.tasks.scrape_hotel_task")
def scrape_hotel_task(self, url_id: int):
    """
    Scrapea un hotel completo en todos los idiomas del snapshot.

    [v4.0] CAMBIOS CRITICOS:
    - Lee idiomas desde url_language_status (snapshot), no desde settings.
    - Integra completeness_service para tracking granular por idioma.
    - finalize_url() reemplaza UPDATE directo de url_queue.status.
    - url_queue puede quedar 'completed' (todos OK) o 'incomplete' (algun fallo).

    NOTA ARQUITECTONICA:
      La solucion ideal es delegar completamente a scraper_service::scrape_one():
        from app.scraper_service import scrape_one
        return scrape_one(url_id)
      Mantenido como tarea independiente por compatibilidad con beats existentes.
    """
    db = SessionLocal()
    start_time = time.time()
    DEFAULT = settings.DEFAULT_LANGUAGE  # "en"

    try:
        # 1. Obtener URL de la BD
        row = db.execute(
            text("SELECT url, language FROM url_queue WHERE id = :id"),
            {"id": url_id}
        ).fetchone()

        if not row:
            logger.error(f"URL ID {url_id} no encontrada en url_queue")
            return {"error": "URL no encontrada"}

        base_url   = row[0]
        queue_lang = row[1] or "en"
        logger.info(f"[Celery] Procesando URL ID {url_id}: {base_url} (queue_lang={queue_lang})")

        # 2. Marcar como 'processing'
        db.execute(
            text("UPDATE url_queue SET status = 'processing', updated_at = NOW() WHERE id = :id"),
            {"id": url_id}
        )
        db.commit()

        # 3. Importar utilidades de scraping
        from app.scraper import BookingScraper, build_language_url, _detect_page_language
        from app.image_downloader import ImageDownloader

        # [v4.0] Snapshot de idiomas (idempotente)
        completeness_service.initialize_url_processing(url_id, db)
        db.commit()

        # [v4.0] Leer idiomas desde snapshot -- NO desde settings.ENABLED_LANGUAGES
        languages = _get_languages_for_url(db, url_id)

        scraped_count     = 0
        first_hotel_name  = None
        images_downloaded = False

        for lang in languages:
            lang_url = build_language_url(base_url, lang)
            logger.info(f"  -> [{url_id}] Idioma [{lang}]: {lang_url}")

            lang_succeeded = False

            # [v4.0] Retry loop por idioma
            for attempt in range(1, MAX_LANG_RETRIES + 2):
                try:
                    with BookingScraper() as scraper:
                        data = scraper.scrape_hotel(lang_url, language=lang)

                    if not data or not data.get("name"):
                        logger.warning(f"  [{url_id}][{lang}] Sin datos (attempt={attempt})")
                        _log_scraping(db, url_id, lang, "no_data",
                                      time.time() - start_time, 0, "No se extrajeron datos")
                        has_retry = completeness_service.record_language_failure(
                            url_id, lang, "Sin datos extraidos", db
                        )
                        db.commit()
                        if has_retry and attempt <= MAX_LANG_RETRIES:
                            continue
                        else:
                            break

                    if first_hotel_name is None:
                        first_hotel_name = data.get("name")

                    # Verificacion de idioma
                    detected = data.get("detected_lang")
                    if detected and detected != lang:
                        logger.error(
                            f"  [{url_id}][{lang}] IDIOMA INCORRECTO - NO SE GUARDA: "
                            f"solicitado='{lang}', pagina en '{detected}'"
                        )
                        _log_scraping(db, url_id, lang, "lang_mismatch",
                                      time.time() - start_time, 0,
                                      f"Pagina en '{detected}', solicitado '{lang}'. NO guardado.")
                        has_retry = completeness_service.record_language_failure(
                            url_id, lang,
                            f"lang_mismatch: solicitado={lang} detectado={detected}", db
                        )
                        db.commit()
                        if has_retry and attempt <= MAX_LANG_RETRIES:
                            continue
                        else:
                            break

                    # Guardar hotel en BD (ON CONFLICT DO NOTHING)
                    insert_result = db.execute(
                        text("""
                            INSERT INTO hotels (
                                url_id, url, language,
                                name, address, description,
                                rating, total_reviews, rating_category,
                                review_scores, services, facilities,
                                house_rules, important_info, rooms_info,
                                images_urls, images_count, scraped_at, updated_at
                            ) VALUES (
                                :url_id, :url, :language,
                                :name, :address, :description,
                                :rating, :total_reviews, :rating_category,
                                :review_scores::jsonb, :services::jsonb, :facilities::jsonb,
                                :house_rules, :important_info, :rooms_info::jsonb,
                                :images_urls::jsonb, 0, NOW(), NOW()
                            )
                            ON CONFLICT (url_id, language) DO NOTHING
                        """),
                        {
                            "url_id":           url_id,
                            "url":              lang_url,
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

                    if insert_result.rowcount == 0:
                        logger.debug(
                            f"  [{url_id}][{lang}] Registro ya existe - "
                            f"preservando (ON CONFLICT DO NOTHING)"
                        )
                        completeness_service.record_language_skipped(url_id, lang, db)
                    else:
                        completeness_service.record_language_success(url_id, lang, db)
                    db.commit()

                    scraped_count += 1
                    duration = time.time() - start_time
                    _log_scraping(db, url_id, lang, "completed", duration,
                                  len(data.get("images_urls") or []))

                    logger.success(
                        f"  [{url_id}][{lang}] '{first_hotel_name}' "
                        f"| rating={data.get('rating')} "
                        f"| imgs={len(data.get('images_urls') or [])}"
                    )

                    # Descarga de imagenes: solo lang=DEFAULT confirmado
                    if lang == DEFAULT and not images_downloaded and settings.DOWNLOAD_IMAGES:
                        img_urls = data.get("images_urls") or []
                        if img_urls:
                            try:
                                downloader = ImageDownloader()
                                results = downloader.download_images(url_id, img_urls, language=DEFAULT)
                                n_ok = len(results)
                                if n_ok > 0:
                                    db.execute(
                                        text("""
                                            UPDATE hotels
                                            SET images_count = :count, updated_at = NOW()
                                            WHERE url_id = :uid AND language = :lang
                                        """),
                                        {"count": n_ok, "uid": url_id, "lang": DEFAULT}
                                    )
                                    db.commit()
                                logger.info(f"  [{url_id}] {n_ok}/{len(img_urls)} imagenes descargadas (en/)")
                            except Exception as img_err:
                                logger.warning(f"  [{url_id}] Error imagenes: {img_err}")
                        images_downloaded = True

                    lang_succeeded = True
                    break  # exito -> salir del retry loop

                except Exception as lang_err:
                    logger.error(f"  [{url_id}][{lang}] attempt={attempt}: {lang_err}")
                    _log_scraping(db, url_id, lang, "error",
                                  time.time() - start_time, 0, str(lang_err)[:500])
                    has_retry = completeness_service.record_language_failure(
                        url_id, lang, str(lang_err), db
                    )
                    try:
                        db.rollback()
                        db.commit()
                    except Exception:
                        pass
                    if has_retry and attempt <= MAX_LANG_RETRIES:
                        logger.info(f"  [{url_id}][{lang}] Reintentando (attempt {attempt+1})...")
                        continue
                    else:
                        break

            if not lang_succeeded:
                logger.warning(f"  [{url_id}][{lang}] Idioma fallido definitivamente.")

        # [v4.0] Finalizacion via completeness_service
        try:
            report       = completeness_service.finalize_url(url_id, db)
            new_status   = "completed" if report.is_complete else "incomplete"
        except Exception as finalize_err:
            logger.error(f"[Celery] Error en finalize_url URL {url_id}: {finalize_err}")
            new_status = "completed" if scraped_count > 0 else "failed"
            db.execute(
                text("""
                    UPDATE url_queue
                    SET status = :status, scraped_at = NOW(), updated_at = NOW()
                    WHERE id = :id
                """),
                {"status": new_status, "id": url_id}
            )
            db.commit()

        total_duration = time.time() - start_time
        logger.success(
            f"[Celery] {url_id} -> {new_status} | {scraped_count}/{len(languages)} idiomas "
            f"| {total_duration:.1f}s | {first_hotel_name}"
        )

        return {
            "success":    scraped_count > 0,
            "hotel_name": first_hotel_name,
            "languages":  scraped_count,
            "duration":   round(total_duration, 2),
            "status":     new_status,
        }

    except Exception as e:
        logger.error(f"Error fatal en task URL {url_id}: {e}")
        db.rollback()
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

        if self.request.retries < self.max_retries:
            logger.info(f"Reintentando URL {url_id} (intento {self.request.retries + 1})")
            raise self.retry(exc=e, countdown=settings.RETRY_DELAY)

        return {"error": str(e)}

    finally:
        db.close()


# =============================================================================
# TAREA DE DESPACHO: BATCH DE URLs PENDIENTES
# =============================================================================

@celery_app.task(name="app.tasks.process_pending_urls")
def process_pending_urls(batch_size: int = 5):
    """
    Despacha un lote de URLs pendientes al worker.
    Ejecutada periodicamente por Celery Beat (cada 30s).

    [v4.0] batch_size limitado a MAX_BATCH_SIZE (10 URLs).
    """
    # [v4.0] Cap de batch size
    if batch_size > MAX_BATCH_SIZE:
        logger.warning(
            f"batch_size={batch_size} supera MAX_BATCH_SIZE={MAX_BATCH_SIZE}. Reduciendo."
        )
        batch_size = MAX_BATCH_SIZE

    db = SessionLocal()
    try:
        rows = db.execute(
            text("""
                SELECT id FROM url_queue
                WHERE status = 'pending'
                  AND retry_count < max_retries
                ORDER BY priority DESC, created_at ASC
                LIMIT :limit
            """),
            {"limit": batch_size}
        ).fetchall()

        url_ids = [r[0] for r in rows]

        if not url_ids:
            logger.debug("No hay URLs pendientes")
            return {"dispatched": 0}

        for uid in url_ids:
            scrape_hotel_task.delay(uid)

        logger.info(f"Despachadas {len(url_ids)} tareas de scraping")
        return {"dispatched": len(url_ids), "url_ids": url_ids}

    finally:
        db.close()


# =============================================================================
# [v4.0] NUEVA TAREA: ROLLBACK DE URL
# =============================================================================

@celery_app.task(
    bind=True,
    name="app.tasks.rollback_url_task",
    max_retries=0,    # Accion deliberada del operador -- no reintentar
    time_limit=120,   # 2 minutos maximo (BD + filesystem)
)
def rollback_url_task(self, url_id: int, keep_logs: bool = True):
    """
    Revierte completamente una URL: elimina hotels, url_language_status,
    imagenes del filesystem y resetea url_queue a 'pending'.

    max_retries=0: El rollback es una accion deliberada del operador.
    Si falla, el operador debe investigar manualmente -- no reintentar.

    Args:
        url_id:    ID de la URL a revertir
        keep_logs: Si True, preserva scraping_logs (auditoria)
    """
    logger.info(f"[Celery] Iniciando rollback URL {url_id} (keep_logs={keep_logs})")
    result = completeness_service.rollback_url(url_id, keep_logs)

    if result["success"]:
        logger.success(f"[Celery] Rollback URL {url_id} completado: {result}")
    else:
        logger.error(f"[Celery] Rollback URL {url_id} fallido: {result['error']}")

    return result


# =============================================================================
# [v4.0] NUEVA TAREA: CONSULTAR COMPLETITUD DE URL
# =============================================================================

@celery_app.task(name="app.tasks.get_url_completeness_task")
def get_url_completeness_task(url_id: int):
    """
    Consulta el estado de completitud de una URL sin modificar nada.
    Util para dashboard del operador y monitoreo.
    """
    try:
        report = completeness_service.check_completeness(url_id)
        return {
            "url_id":            report.url_id,
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
    except Exception as e:
        logger.error(f"Error en get_url_completeness_task URL {url_id}: {e}")
        return {"error": str(e)}


# =============================================================================
# [v4.0] NUEVA TAREA: LISTAR URLs INCOMPLETAS
# =============================================================================

@celery_app.task(name="app.tasks.check_incomplete_urls_task")
def check_incomplete_urls_task():
    """
    Lista URLs con idiomas fallidos para dashboard del operador.
    Configurable en beat_schedule: crontab(hour='*/6') cada 6 horas.

    Detecta:
    - url_queue.status = 'incomplete' (finalize_url() las marco asi)
    - URLs con url_language_status.status = 'failed' aunque queue sea 'completed'
      (inconsistencia que puede ocurrir si el sistema fue actualizado a v6.0 con
      URLs ya procesadas)
    """
    db = SessionLocal()
    try:
        rows = db.execute(
            text("""
                SELECT
                    q.id,
                    q.url,
                    q.status,
                    COUNT(uls.language) FILTER (WHERE uls.status = 'failed') AS failed_langs,
                    ARRAY_AGG(uls.language ORDER BY uls.language)
                        FILTER (WHERE uls.status = 'failed') AS failed_languages
                FROM url_queue q
                JOIN url_language_status uls ON uls.url_id = q.id
                WHERE q.status IN ('incomplete', 'completed')
                GROUP BY q.id, q.url, q.status
                HAVING COUNT(uls.language) FILTER (WHERE uls.status = 'failed') > 0
                ORDER BY q.id
            """)
        ).fetchall()

        result = [
            {
                "url_id":           r[0],
                "url":              r[1],
                "queue_status":     r[2],
                "failed_languages": r[4] or [],
            }
            for r in rows
        ]

        if result:
            logger.warning(
                f"[check_incomplete] {len(result)} URLs con idiomas fallidos: "
                f"{[r['url_id'] for r in result]}"
            )
        else:
            logger.info("[check_incomplete] No hay URLs con idiomas fallidos.")

        return {"total_incomplete": len(result), "urls": result}

    except Exception as e:
        logger.error(f"Error en check_incomplete_urls_task: {e}")
        return {"error": str(e)}
    finally:
        db.close()


# =============================================================================
# TAREA PERIODICA: METRICAS DEL SISTEMA
# =============================================================================

@celery_app.task(name="app.tasks.save_system_metrics")
def save_system_metrics():
    """Captura y guarda metricas del sistema cada 5 minutos."""
    db = SessionLocal()
    try:
        stats = db.execute(text("""
            SELECT
                COUNT(*) FILTER (WHERE status = 'pending')    AS pending,
                COUNT(*) FILTER (WHERE status = 'processing') AS processing,
                COUNT(*) FILTER (WHERE status = 'completed')  AS completed,
                COUNT(*) FILTER (WHERE status = 'failed')     AS failed,
                COUNT(*) FILTER (WHERE status = 'incomplete') AS incomplete
            FROM url_queue
        """)).fetchone()

        hotels_total = db.execute(text("SELECT COUNT(*) FROM hotels")).scalar() or 0
        images_total = db.execute(text("SELECT COALESCE(SUM(images_count), 0) FROM hotels")).scalar() or 0

        cpu    = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk   = psutil.disk_usage("C:\\").percent if psutil.disk_usage.__doc__ else 0.0

        db.execute(
            text("""
                INSERT INTO system_metrics (
                    urls_pending, urls_processing, urls_completed, urls_failed,
                    hotels_scraped, images_downloaded,
                    cpu_usage, memory_usage, disk_usage,
                    recorded_at
                ) VALUES (
                    :pending, :processing, :completed, :failed,
                    :hotels, :images,
                    :cpu, :memory, :disk,
                    NOW()
                )
            """),
            {
                "pending":    stats[0] or 0,
                "processing": stats[1] or 0,
                "completed":  stats[2] or 0,
                "failed":     stats[3] or 0,
                "hotels":     hotels_total,
                "images":     images_total,
                "cpu":        cpu,
                "memory":     memory,
                "disk":       disk,
            }
        )
        db.commit()
        logger.debug(
            f"Metricas guardadas | CPU:{cpu}% MEM:{memory}% "
            f"pending:{stats[0]} completed:{stats[2]} incomplete:{stats[4]}"
        )
        return {"recorded": True}

    except Exception as e:
        logger.error(f"Error guardando metricas: {e}")
        return {"error": str(e)}
    finally:
        db.close()


# =============================================================================
# TAREA PERIODICA: LIMPIEZA DE LOGS
# =============================================================================

@celery_app.task(name="app.tasks.cleanup_old_logs")
def cleanup_old_logs(days: int = 30):
    """Elimina logs de scraping con mas de `days` dias de antiguedad."""
    db = SessionLocal()
    try:
        result = db.execute(
            text("""
                DELETE FROM scraping_logs
                WHERE timestamp < NOW() - (INTERVAL '1 day' * :days)
            """),
            {"days": days}
        )
        db.commit()
        deleted = result.rowcount
        logger.info(f"Logs limpiados: {deleted} registros eliminados (>{days} dias)")
        return {"deleted": deleted}
    except Exception as e:
        logger.error(f"Error limpiando logs: {e}")
        return {"error": str(e)}
    finally:
        db.close()


# =============================================================================
# UTILIDAD INTERNA
# =============================================================================

def _log_scraping(
    db, url_id: int, language: str,
    status: str, duration: float,
    items: int, error: str = None
):
    """Inserta una linea en scraping_logs."""
    try:
        db.execute(
            text("""
                INSERT INTO scraping_logs
                    (url_id, language, status, duration_seconds, items_extracted, error_message, timestamp)
                VALUES
                    (:url_id, :lang, :status, :dur, :items, :error, NOW())
            """),
            {
                "url_id": url_id,
                "lang":   language,
                "status": status,
                "dur":    round(duration, 2),
                "items":  items,
                "error":  error,
            }
        )
        db.commit()
    except Exception as e:
        logger.debug(f"No se pudo registrar log: {e}")
