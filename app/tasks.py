"""
BookingScraper/app/tasks.py  (fix SQL injection v2.1)
Tareas Celery para scraping asíncrono - BookingScraper Pro
Windows 11 + Python 3.14.3

CORRECCIONES v1.1:
  [FIX] Columna url_id en INSERT hotels (era url_queue_id en models anterior)
  [FIX] scraped_at: columna ahora existe en URLQueue (añadida en models.py)
  [FIX] review_scores, services, facilities, rooms_info → JSON real (no str/join)
  [FIX] images_urls → JSON real (no join con coma)
  [FIX] text() en todos los raw SQL (SQLAlchemy 2.0)
  [NEW] save_system_metrics(): tarea periódica de métricas del sistema
  [NEW] cleanup_old_logs(): limpieza de logs antiguos (referenciada en beat)
  [FIX] Imports desde app.celery_app (no redefinir Celery aquí)
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


# ═══════════════════════════════════════════════════════════════════════════════
# TAREA PRINCIPAL: SCRAPING DE UN HOTEL
# ═══════════════════════════════════════════════════════════════════════════════

@celery_app.task(bind=True, max_retries=3, name="app.tasks.scrape_hotel_task")
def scrape_hotel_task(self, url_id: int):
    """
    Scrapea un hotel completo en todos los idiomas habilitados.

    Args:
        url_id: ID de la URL en la tabla url_queue
    """
    db = SessionLocal()
    start_time = time.time()

    try:
        # ── 1. Obtener URL de la BD ────────────────────────────────────────────
        row = db.execute(
            text("SELECT url, language FROM url_queue WHERE id = :id"),
            {"id": url_id}
        ).fetchone()

        if not row:
            logger.error(f"URL ID {url_id} no encontrada en url_queue")
            return {"error": "URL no encontrada"}

        base_url = row[0]
        base_lang = row[1] or "en"

        logger.info(f"🔄 Procesando URL ID {url_id}: {base_url}")

        # ── 2. Marcar como 'processing' ───────────────────────────────────────
        db.execute(
            text("""
                UPDATE url_queue
                SET status = 'processing', updated_at = NOW()
                WHERE id = :id
            """),
            {"id": url_id}
        )
        db.commit()

        # ── 3. Scraping por idioma ─────────────────────────────────────────────
        from app.scraper import BookingScraper
        from app.image_downloader import ImageDownloader

        languages = settings.ENABLED_LANGUAGES  # propiedad que parsea el CSV
        scraped_count = 0
        first_hotel_name = None

        for lang in languages:
            try:
                # Construir URL con extensión de idioma
                ext = settings.LANGUAGE_EXT.get(lang, f".{lang}")
                if ext:
                    # Reemplazar .html por .{lang}.html
                    lang_url = base_url.replace(".html", f"{ext}.html")
                else:
                    lang_url = base_url

                logger.info(f"  → Idioma {lang}: {lang_url}")

                # Crear scraper y extraer
                with BookingScraper() as scraper:
                    data = scraper.scrape_hotel(lang_url, language=lang)

                if not data or not data.get("name"):
                    logger.warning(f"  ⚠️ Sin datos para {lang}")
                    _log_scraping(db, url_id, lang, "no_data",
                                  time.time() - start_time, 0, "No se extrajeron datos")
                    continue

                if first_hotel_name is None:
                    first_hotel_name = data.get("name")

                # ── 4. Guardar hotel en BD ─────────────────────────────────────
                # ✅ FIX: url_id (no url_queue_id); JSON real con json.dumps()
                db.execute(
                    text("""
                        INSERT INTO hotels (
                            url_id, url, language,
                            name, address, description,
                            rating, total_reviews, rating_category,
                            review_scores, services, facilities,
                            house_rules, important_info, rooms_info,
                            images_urls, scraped_at, updated_at
                        ) VALUES (
                            :url_id, :url, :language,
                            :name, :address, :description,
                            :rating, :total_reviews, :rating_category,
                            :review_scores::jsonb, :services::jsonb, :facilities::jsonb,
                            :house_rules, :important_info, :rooms_info::jsonb,
                            :images_urls::jsonb, NOW(), NOW()
                        )
                        ON CONFLICT (url_id, language) DO UPDATE SET
                            name            = EXCLUDED.name,
                            address         = EXCLUDED.address,
                            description     = EXCLUDED.description,
                            rating          = EXCLUDED.rating,
                            total_reviews   = EXCLUDED.total_reviews,
                            rating_category = EXCLUDED.rating_category,
                            review_scores   = EXCLUDED.review_scores,
                            services        = EXCLUDED.services,
                            facilities      = EXCLUDED.facilities,
                            house_rules     = EXCLUDED.house_rules,
                            important_info  = EXCLUDED.important_info,
                            rooms_info      = EXCLUDED.rooms_info,
                            images_urls     = EXCLUDED.images_urls,
                            updated_at      = NOW()
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
                        # ✅ FIX: json.dumps() → JSON real, no str()
                        "review_scores":    json.dumps(data.get("review_scores") or {}),
                        "services":         json.dumps(data.get("services")      or []),
                        "facilities":       json.dumps(data.get("facilities")    or {}),
                        "house_rules":      data.get("house_rules"),
                        "important_info":   data.get("important_info"),
                        "rooms_info":       json.dumps(data.get("rooms")         or []),
                        # ✅ FIX: lista de URLs como JSON array, no join con coma
                        "images_urls":      json.dumps(data.get("images_urls")   or []),
                    }
                )
                db.commit()

                scraped_count += 1
                duration = time.time() - start_time
                _log_scraping(db, url_id, lang, "completed", duration,
                              len(data.get("images_urls") or []))

                # ── 5. Descargar imágenes (solo en idioma base) ────────────────
                if lang == base_lang and settings.DOWNLOAD_IMAGES:
                    img_urls = data.get("images_urls") or []
                    if img_urls:
                        try:
                            downloader = ImageDownloader()
                            downloader.download_images(url_id, img_urls[:30])
                            logger.info(f"  📷 {len(img_urls[:30])} imágenes descargadas")
                        except Exception as img_err:
                            logger.warning(f"  ⚠️ Error imágenes: {img_err}")

            except Exception as lang_err:
                logger.error(f"  ✗ Error en idioma {lang}: {lang_err}")
                _log_scraping(db, url_id, lang, "error",
                              time.time() - start_time, 0, str(lang_err))

        # ── 6. Actualizar URL queue ────────────────────────────────────────────
        new_status = "completed" if scraped_count > 0 else "failed"
        # ✅ FIX: scraped_at ahora existe en URLQueue (añadida en models.py)
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
            f"✅ {url_id} → {new_status} | {scraped_count}/{len(languages)} idiomas "
            f"| {total_duration:.1f}s | {first_hotel_name}"
        )

        return {
            "success":    scraped_count > 0,
            "hotel_name": first_hotel_name,
            "languages":  scraped_count,
            "duration":   round(total_duration, 2),
        }

    except Exception as e:
        logger.error(f"❌ Error fatal en task URL {url_id}: {e}")
        db.rollback()

        # Marcar como fallida y registrar error
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

        # Reintentar si no superó el máximo
        if self.request.retries < self.max_retries:
            logger.info(f"🔄 Reintentando URL {url_id} (intento {self.request.retries + 1})")
            raise self.retry(exc=e, countdown=settings.RETRY_DELAY)

        return {"error": str(e)}

    finally:
        db.close()


# ═══════════════════════════════════════════════════════════════════════════════
# TAREA DE DESPACHO: BATCH DE URLs PENDIENTES
# ═══════════════════════════════════════════════════════════════════════════════

@celery_app.task(name="app.tasks.process_pending_urls")
def process_pending_urls(batch_size: int = 5):
    """
    Despacha un lote de URLs pendientes al worker.
    Ejecutada periódicamente por Celery Beat (cada 30s).

    Args:
        batch_size: Número máximo de URLs a despachar por ciclo
    """
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
            logger.debug("ℹ️ No hay URLs pendientes")
            return {"dispatched": 0}

        for uid in url_ids:
            scrape_hotel_task.delay(uid)

        logger.info(f"🚀 Despachadas {len(url_ids)} tareas de scraping")
        return {"dispatched": len(url_ids), "url_ids": url_ids}

    finally:
        db.close()


# ═══════════════════════════════════════════════════════════════════════════════
# TAREA PERIÓDICA: MÉTRICAS DEL SISTEMA
# ═══════════════════════════════════════════════════════════════════════════════

@celery_app.task(name="app.tasks.save_system_metrics")
def save_system_metrics():
    """
    Captura y guarda métricas del sistema cada 5 minutos.
    Referenciada en beat_schedule de celery_app.py.
    """
    db = SessionLocal()
    try:
        # Stats de URL queue
        stats = db.execute(text("""
            SELECT
                COUNT(*) FILTER (WHERE status = 'pending')    AS pending,
                COUNT(*) FILTER (WHERE status = 'processing') AS processing,
                COUNT(*) FILTER (WHERE status = 'completed')  AS completed,
                COUNT(*) FILTER (WHERE status = 'failed')     AS failed
            FROM url_queue
        """)).fetchone()

        hotels_total = db.execute(
            text("SELECT COUNT(*) FROM hotels")
        ).scalar() or 0

        images_total = db.execute(
            text("SELECT COALESCE(SUM(images_count), 0) FROM hotels")
        ).scalar() or 0

        # Recursos del sistema
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
            f"📊 Métricas guardadas | CPU:{cpu}% MEM:{memory}% "
            f"pending:{stats[0]} completed:{stats[2]}"
        )
        return {"recorded": True}

    except Exception as e:
        logger.error(f"Error guardando métricas: {e}")
        return {"error": str(e)}
    finally:
        db.close()


# ═══════════════════════════════════════════════════════════════════════════════
# TAREA PERIÓDICA: LIMPIEZA DE LOGS
# ═══════════════════════════════════════════════════════════════════════════════

@celery_app.task(name="app.tasks.cleanup_old_logs")
def cleanup_old_logs(days: int = 30):
    """
    Elimina logs de scraping con más de `days` días de antigüedad.
    Referenciada en beat_schedule de celery_app.py.
    """
    db = SessionLocal()
    try:
        # [FIX v2.1] Usar bind parameter para evitar injection de SQL.
        # El pattern .replace() anterior era vulnerable si days llegara
        # de fuente externa. Aqui usamos el multiplicador nativo de INTERVAL.
        result = db.execute(
            text("""
                DELETE FROM scraping_logs
                WHERE timestamp < NOW() - (INTERVAL '1 day' * :days)
            """),
            {"days": days}
        )
        db.commit()
        deleted = result.rowcount
        logger.info(f"🧹 Logs limpiados: {deleted} registros eliminados (>{days} días)")
        return {"deleted": deleted}
    except Exception as e:
        logger.error(f"Error limpiando logs: {e}")
        return {"error": str(e)}
    finally:
        db.close()


# ═══════════════════════════════════════════════════════════════════════════════
# UTILIDAD INTERNA
# ═══════════════════════════════════════════════════════════════════════════════

def _log_scraping(
    db, url_id: int, language: str,
    status: str, duration: float,
    items: int, error: str = None
):
    """Inserta una línea en scraping_logs."""
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
