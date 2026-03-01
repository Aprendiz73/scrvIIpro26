"""
BookingScraper/app/completeness_service.py  v1.0
Servicio de completitud de idiomas por URL - BookingScraper Pro

RESPONSABILIDAD:
  Rastrear el estado de scraping de cada idioma de forma independiente para
  cada URL. Permite distinguir entre:
    - URL completamente procesada (todos los idiomas del snapshot OK)
    - URL parcialmente procesada (algunos idiomas fallaron → 'incomplete')

PROBLEMA QUE RESUELVE:
  El sistema anterior marcaba una URL como 'completed' si al menos UN idioma
  era exitoso (scraped_count > 0). 1/5 idiomas era indistinguible de 5/5.

INVARIANTES GARANTIZADAS:
  - initialize_url_processing() es idempotente (ON CONFLICT DO NOTHING)
  - record_language_success() es idempotente (ON CONFLICT DO UPDATE)
  - finalize_url() es segura ante concurrencia (WHERE status NOT IN ('completed'))
  - Todas las operaciones son transaccionales en PostgreSQL

REGLAS DE NEGOCIO (DEFINIDAS POR EL OPERADOR):
  1. URLs ya procesadas con N idiomas quedan OK al cambiar LANGUAGES_ENABLED.
     No se requiere resincronización automática.
  2. URLs nuevas toman el valor actual de LANGUAGES_ENABLED en el momento
     de llamar a initialize_url_processing().
  3. URLs en proceso mantienen su snapshot de idiomas (registrado en
     url_language_status). scrape_one() lee desde url_language_status,
     no desde settings.ENABLED_LANGUAGES.
  4. Los cambios de entorno (.env) solo se realizan con el scraper detenido.

TABLA REQUERIDA:
  url_language_status — ver migration_v2_url_language_status.sql

CORRECCIONES v2.0 [NEW-08, NEW-10]: ver inline [FIX ...] comments.
"""

import os
import threading
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from sqlalchemy import text
from loguru import logger

from app.database import SessionLocal
from app.config import settings


# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTES
# ─────────────────────────────────────────────────────────────────────────────

# Máximo de reintentos por idioma dentro del mismo ciclo de scraping.
# "Máximo una vez más" → 1 reintento → 2 intentos totales.
MAX_LANG_RETRIES: int = 1

_STATUS_FILE_PROCESSING: str = "in_process.txt"
_STATUS_FILE_COMPLETED:  str = "completed.txt"
_STATUS_FILE_INCOMPLETE: str = "incomplete.txt"


# ─────────────────────────────────────────────────────────────────────────────
# TIPOS
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class LanguageStatusDetail:
    language:    str
    status:      str
    retry_count: int
    last_error:  Optional[str]


@dataclass
class CompletenessReport:
    url_id:            int
    is_complete:       bool
    languages_ok:      List[str]
    languages_failed:  List[str]
    languages_missing: List[str]
    languages_pending: List[str]
    language_detail:   List[LanguageStatusDetail] = field(default_factory=list)

    @property
    def summary(self) -> str:
        return (
            f"URL {self.url_id} | "
            f"completo={self.is_complete} | "
            f"ok={self.languages_ok} | "
            f"fallidos={self.languages_failed} | "
            f"faltantes={self.languages_missing}"
        )


# ─────────────────────────────────────────────────────────────────────────────
# SERVICIO
# ─────────────────────────────────────────────────────────────────────────────

class CompletenessService:
    # [NEW-10] Lock para operaciones de archivo — previene race condition entre threads
    # cuando dos threads procesan el mismo url_id simultáneamente (defensa en profundidad,
    # ya que BUG-09 eliminó el race a nivel de BD, pero el sistema de archivos no tiene MVCC).
    _file_lock = threading.Lock()

    """
    Servicio stateless de tracking de completitud por idioma.
    Thread-safe: sin estado compartido en memoria.
    """

    def initialize_url_processing(self, url_id: int, db=None) -> None:
        """
        Registra en url_language_status una fila por cada idioma en LANGUAGES_ENABLED.
        Idempotente: ON CONFLICT DO NOTHING preserva filas existentes.

        INVARIANTE CRÍTICO: El snapshot registrado aquí es la fuente de verdad
        de los idiomas a procesar para esta URL. Si LANGUAGES_ENABLED cambia
        después, esta URL sigue con su snapshot original.
        """
        enabled_langs = settings.ENABLED_LANGUAGES
        own_session   = db is None
        if own_session:
            db = SessionLocal()

        try:
            for lang in enabled_langs:
                db.execute(
                    text("""
                        INSERT INTO url_language_status
                            (url_id, language, status, retry_count, max_retries,
                             created_at, updated_at)
                        VALUES
                            (:url_id, :lang, 'pending', 0, :max_retries, NOW(), NOW())
                        ON CONFLICT (url_id, language) DO NOTHING
                    """),
                    {"url_id": url_id, "lang": lang, "max_retries": MAX_LANG_RETRIES}
                )
            if own_session:
                db.commit()

            logger.debug(
                f"  [completeness] [{url_id}] Inicializado | idiomas={enabled_langs}"
            )
            self._write_status_file(url_id, _STATUS_FILE_PROCESSING, overwrite=True)

        except Exception as e:
            if own_session:
                db.rollback()
            logger.error(f"  [completeness] [{url_id}] Error en initialize: {e}")
            raise
        finally:
            if own_session:
                db.close()

    def record_language_success(self, url_id: int, language: str, db=None) -> None:
        """Marca un idioma como completado. Idempotente."""
        own_session = db is None
        if own_session:
            db = SessionLocal()
        try:
            db.execute(
                text("""
                    INSERT INTO url_language_status
                        (url_id, language, status, retry_count, max_retries,
                         scraped_at, created_at, updated_at)
                    VALUES
                        (:url_id, :lang, 'completed', 0, :max_retries,
                         NOW(), NOW(), NOW())
                    ON CONFLICT (url_id, language) DO UPDATE
                        SET status     = 'completed',
                            scraped_at = NOW(),
                            updated_at = NOW()
                """),
                {"url_id": url_id, "lang": language, "max_retries": MAX_LANG_RETRIES}
            )
            if own_session:
                db.commit()
            logger.debug(f"  [completeness] [{url_id}][{language}] → completed")
        except Exception as e:
            if own_session:
                db.rollback()
            logger.error(f"  [completeness] [{url_id}][{language}] Error record_success: {e}")
        finally:
            if own_session:
                db.close()

    def record_language_skipped(self, url_id: int, language: str, db=None) -> None:
        """Marca un idioma como skipped_existing (dato ya existía en BD). Cuenta como éxito."""
        own_session = db is None
        if own_session:
            db = SessionLocal()
        try:
            db.execute(
                text("""
                    INSERT INTO url_language_status
                        (url_id, language, status, retry_count, max_retries,
                         scraped_at, created_at, updated_at)
                    VALUES
                        (:url_id, :lang, 'skipped_existing', 0, :max_retries,
                         NOW(), NOW(), NOW())
                    ON CONFLICT (url_id, language) DO UPDATE
                        SET status     = 'skipped_existing',
                            scraped_at = NOW(),
                            updated_at = NOW()
                """),
                {"url_id": url_id, "lang": language, "max_retries": MAX_LANG_RETRIES}
            )
            if own_session:
                db.commit()
            logger.debug(f"  [completeness] [{url_id}][{language}] → skipped_existing")
        except Exception as e:
            if own_session:
                db.rollback()
            logger.error(f"  [completeness] [{url_id}][{language}] Error record_skipped: {e}")
        finally:
            if own_session:
                db.close()

    def record_language_failure(
        self, url_id: int, language: str, error: str, db=None
    ) -> bool:
        """
        Registra un fallo e incrementa retry_count.

        Retorna True si hay reintento disponible (retry_count <= max_retries).
        Retorna False si el idioma queda como 'failed' (reintentos agotados).

        Usa FOR UPDATE para serializar actualizaciones concurrentes en la misma fila.
        """
        own_session = db is None
        if own_session:
            db = SessionLocal()
        try:
            row = db.execute(
                text("""
                    SELECT retry_count, max_retries
                    FROM   url_language_status
                    WHERE  url_id = :url_id AND language = :lang
                    FOR UPDATE
                """),
                {"url_id": url_id, "lang": language}
            ).fetchone()

            if not row:
                db.execute(
                    text("""
                        INSERT INTO url_language_status
                            (url_id, language, status, retry_count, max_retries,
                             last_error, created_at, updated_at)
                        VALUES
                            (:url_id, :lang, 'failed', 1, :max_retries,
                             :error, NOW(), NOW())
                        ON CONFLICT (url_id, language) DO NOTHING
                    """),
                    {"url_id": url_id, "lang": language,
                     "max_retries": MAX_LANG_RETRIES, "error": error[:500]}
                )
                if own_session:
                    db.commit()
                return False

            new_retry  = row[0] + 1
            has_retry  = new_retry <= row[1]
            new_status = "pending" if has_retry else "failed"

            db.execute(
                text("""
                    UPDATE url_language_status
                    SET    retry_count = :rc,
                           status      = :status,
                           last_error  = :error,
                           updated_at  = NOW()
                    WHERE  url_id = :url_id AND language = :lang
                """),
                {"rc": new_retry, "status": new_status, "error": error[:500],
                 "url_id": url_id, "lang": language}
            )
            if own_session:
                db.commit()

            logger.debug(
                f"  [completeness] [{url_id}][{language}] fallo "
                f"retry={new_retry}/{row[1]} → {new_status} | reintento={has_retry}"
            )
            return has_retry

        except Exception as e:
            if own_session:
                db.rollback()
            logger.error(f"  [completeness] [{url_id}][{language}] Error record_failure: {e}")
            return False
        finally:
            if own_session:
                db.close()

    def finalize_url(self, url_id: int, db=None) -> CompletenessReport:
        """
        Evalúa completitud y actualiza url_queue.status a 'completed' o 'incomplete'.
        Protección TOCTOU: WHERE status NOT IN ('completed').
        Escribe el archivo de estado correspondiente.
        """
        own_session = db is None
        if own_session:
            db = SessionLocal()
        try:
            report = self.check_completeness(url_id, db)

            new_status = "completed" if report.is_complete else "incomplete"

            result = db.execute(
                text("""
                    UPDATE url_queue
                    SET    status     = :status,
                           scraped_at = NOW(),
                           updated_at = NOW()
                    WHERE  id     = :id
                      AND  status NOT IN ('completed')
                """),
                {"status": new_status, "id": url_id}
            )
            if own_session:
                db.commit()

            if result.rowcount > 0:
                logger.info(
                    f"  [completeness] [{url_id}] finalizado → {new_status} | "
                    f"{report.summary}"
                )

            self._remove_status_file(url_id, _STATUS_FILE_PROCESSING)
            status_file = (
                _STATUS_FILE_COMPLETED if new_status == "completed"
                else _STATUS_FILE_INCOMPLETE
            )
            self._write_status_file(url_id, status_file, overwrite=True)

            return report

        except Exception as e:
            if own_session:
                db.rollback()
            logger.error(f"  [completeness] [{url_id}] Error en finalize_url: {e}")
            raise
        finally:
            if own_session:
                db.close()

    def check_completeness(self, url_id: int, db=None) -> CompletenessReport:
        """Evalúa la completitud de una URL sin modificar nada."""
        own_session = db is None
        if own_session:
            db = SessionLocal()
        try:
            rows = db.execute(
                text("""
                    SELECT language, status, retry_count, last_error
                    FROM   url_language_status
                    WHERE  url_id = :url_id
                    ORDER BY language
                """),
                {"url_id": url_id}
            ).fetchall()

            ok_statuses = {"completed", "skipped_existing"}
            languages_ok:      List[str] = []
            languages_failed:  List[str] = []
            languages_pending: List[str] = []
            detail:            List[LanguageStatusDetail] = []

            for r in rows:
                lang, status, rc, err = r[0], r[1], r[2], r[3]
                detail.append(LanguageStatusDetail(
                    language=lang, status=status, retry_count=rc, last_error=err
                ))
                if status in ok_statuses:
                    languages_ok.append(lang)
                elif status == "failed":
                    languages_failed.append(lang)
                else:
                    languages_pending.append(lang)

            tracked = {r[0] for r in rows}
            languages_missing = [
                l for l in settings.ENABLED_LANGUAGES if l not in tracked
            ]

            is_complete = (
                len(languages_failed)  == 0 and
                len(languages_pending) == 0 and
                len(languages_missing) == 0 and
                len(languages_ok)       > 0
            )

            return CompletenessReport(
                url_id=url_id,
                is_complete=is_complete,
                languages_ok=languages_ok,
                languages_failed=languages_failed,
                languages_missing=languages_missing,
                languages_pending=languages_pending,
                language_detail=detail,
            )
        except Exception as e:
            logger.error(f"  [completeness] [{url_id}] Error check_completeness: {e}")
            raise
        finally:
            if own_session:
                db.close()

    def rollback_url(self, url_id: int, keep_logs: bool = True) -> Dict:
        """
        Revierte una URL: elimina hotels, url_language_status, imágenes
        y resetea url_queue a 'pending'.

        SECUENCIA: DELETE hotels → DELETE tracking → UPDATE url_queue
                   → COMMIT → rmtree (filesystem post-commit).
        Si el proceso muere entre COMMIT y rmtree, la URL queda en 'pending'
        (correcto) y la carpeta queda huérfana (limpieza manual).
        """
        db = SessionLocal()
        result = {
            "url_id":           url_id,
            "success":          False,
            "hotels_deleted":   0,
            "tracking_deleted": 0,
            "images_deleted":   False,
            "error":            None,
        }
        try:
            status_row = db.execute(
                text("SELECT status FROM url_queue WHERE id = :id"),
                {"id": url_id}
            ).fetchone()

            if not status_row:
                result["error"] = f"URL {url_id} no encontrada en url_queue"
                return result

            if status_row[0] == "processing":
                result["error"] = (
                    f"URL {url_id} está en 'processing'. "
                    "Detener el scraper antes de hacer rollback."
                )
                return result

            r_h = db.execute(
                text("DELETE FROM hotels WHERE url_id = :uid"),
                {"uid": url_id}
            )
            result["hotels_deleted"] = r_h.rowcount

            r_t = db.execute(
                text("DELETE FROM url_language_status WHERE url_id = :uid"),
                {"uid": url_id}
            )
            result["tracking_deleted"] = r_t.rowcount

            db.execute(
                text("""
                    UPDATE url_queue
                    SET    status      = 'pending',
                           retry_count = 0,
                           last_error  = NULL,
                           scraped_at  = NULL,
                           updated_at  = NOW()
                    WHERE  id = :id
                """),
                {"id": url_id}
            )
            db.commit()

            logger.info(
                f"  [completeness] [{url_id}] Rollback BD OK | "
                f"hotels={result['hotels_deleted']} tracking={result['tracking_deleted']}"
            )

        except Exception as e:
            db.rollback()
            result["error"] = str(e)
            logger.error(f"  [completeness] [{url_id}] Error rollback BD: {e}")
            return result
        finally:
            db.close()

        # Filesystem (post-commit, best-effort)
        images_folder = os.path.join(settings.IMAGES_PATH, f"hotel_{url_id}")
        if os.path.isdir(images_folder):
            try:
                import shutil
                shutil.rmtree(images_folder)
                result["images_deleted"] = True
                logger.info(
                    f"  [completeness] [{url_id}] Carpeta eliminada: {images_folder}"
                )
            except Exception as fs_err:
                logger.warning(
                    f"  [completeness] [{url_id}] No se pudo eliminar {images_folder}: "
                    f"{fs_err}. Limpieza manual requerida."
                )

        result["success"] = True
        return result

    # ── Filesystem utilities (best-effort) ───────────────────────────────────

    def _write_status_file(
        self, url_id: int, filename: str, content: str = "", overwrite: bool = False
    ) -> None:
        """
        [NEW-10] Protegido con threading.Lock — previene corrupción de archivos de estado
        cuando múltiples threads procesan la misma URL (defensa en profundidad).
        """
        folder   = os.path.join(settings.IMAGES_PATH, f"hotel_{url_id}")
        filepath = os.path.join(folder, filename)
        with CompletenessService._file_lock:
            try:
                os.makedirs(folder, exist_ok=True)
                mode = "w" if overwrite else "x"
                with open(filepath, mode, encoding="utf-8") as f:
                    f.write(content)
                logger.debug(f"  [completeness] Archivo de estado: {filepath}")
            except FileExistsError:
                pass
            except Exception as e:
                logger.debug(f"  [completeness] No se pudo escribir {filepath}: {e}")

    def _remove_status_file(self, url_id: int, filename: str) -> None:
        filepath = os.path.join(
            settings.IMAGES_PATH, f"hotel_{url_id}", filename
        )
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
        except Exception as _rm_err:
            # [NEW-08] File removal failures logged — not silently swallowed
            logger.debug(f"  [completeness] No se pudo eliminar {filepath}: {_rm_err}")


# Instancia global — stateless, singleton seguro
completeness_service = CompletenessService()
