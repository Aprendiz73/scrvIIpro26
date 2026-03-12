"""
load_urls.py — BookingScraper Pro v49
Carga URLs desde CSV sin cabecera:
    id_externo_hotel,url_booking

Formato del CSV (sin cabecera, separador coma, sin espacios):
    1001,https://www.booking.com/hotel/br/manaus-hoteis-millennium.html
    1002,https://www.booking.com/hotel/br/colonna-park.html

Uso:
    python scripts/load_urls.py urls.csv
    python scripts/load_urls.py urls.csv --dry-run

Notas:
    - Soporta saltos de linea Windows (CRLF) y Unix (LF).
    - El id_externo_hotel se guarda en url_queue.external_ref.
    - Si la columna external_ref aun no existe en la tabla, la inserta
      de forma segura sin esa columna (compatibilidad hacia atras).
    - Duplicados (por URL) se omiten via ON CONFLICT DO NOTHING.
    - Usa INSERT directo con SQL parametrizado — no depende del ORM.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, NamedTuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from loguru import logger
from sqlalchemy import inspect, text
from app.config import get_settings
from app.database import get_db

_cfg = get_settings()

# ── Constantes ────────────────────────────────────────────────────────────────
_BOOKING_PREFIX = "https://www.booking.com/hotel/"
_MAX_URL_LEN    = 2048
_MAX_FILE_MB    = getattr(_cfg, "CSV_MAX_FILE_MB", 10)


class _Row(NamedTuple):
    ext_id: str
    url: str


# ── Validación ────────────────────────────────────────────────────────────────

def _is_valid_url(url: str) -> bool:
    return (
        bool(url)
        and url.startswith(_BOOKING_PREFIX)
        and len(url) <= _MAX_URL_LEN
    )


def _is_valid_id(raw: str) -> bool:
    return bool(raw) and raw.isdigit()


# ── Parseo CSV ────────────────────────────────────────────────────────────────

def _parse_csv(filepath: Path) -> List[_Row]:
    """
    Lee CSV sin cabecera con formato: id,url
    Maneja CRLF y LF. Devuelve solo filas validas.
    """
    size_mb = filepath.stat().st_size / (1024 * 1024)
    if size_mb > _MAX_FILE_MB:
        logger.error("Archivo demasiado grande: {:.1f} MB (max {} MB).", size_mb, _MAX_FILE_MB)
        return []

    rows: List[_Row] = []
    total = 0
    invalid = 0

    # universal newlines=True maneja CR, LF, CRLF automaticamente
    with open(filepath, encoding="utf-8", newline="") as f:
        for lineno, raw_line in enumerate(f, start=1):
            # Quitar \r\n, \n, espacios extremos
            line = raw_line.strip()
            if not line:
                continue
            total += 1

            # Separar solo en la PRIMERA coma para tolerar URLs con comas (raro pero posible)
            comma = line.find(",")
            if comma < 1:
                logger.warning("Linea {}: sin coma separadora — omitida: {!r}", lineno, line)
                invalid += 1
                continue

            raw_id  = line[:comma].strip()
            raw_url = line[comma + 1:].strip()

            if not _is_valid_id(raw_id):
                logger.warning("Linea {}: id {!r} no es numerico — omitida.", lineno, raw_id)
                invalid += 1
                continue

            if not _is_valid_url(raw_url):
                logger.warning("Linea {}: URL invalida — omitida: {!r}", lineno, raw_url)
                invalid += 1
                continue

            rows.append(_Row(ext_id=raw_id, url=raw_url))

    logger.info(
        "CSV leido: {} lineas, {} validas, {} invalidas.",
        total, len(rows), invalid,
    )
    return rows


# ── Deteccion de columna external_ref ────────────────────────────────────────

def _has_external_ref_column() -> bool:
    """Verifica si la columna external_ref existe en url_queue."""
    try:
        from app.database import _get_engine
        engine = _get_engine()
        insp = inspect(engine)
        cols = [c["name"] for c in insp.get_columns("url_queue")]
        return "external_ref" in cols
    except Exception as exc:
        logger.warning("No se pudo inspeccionar url_queue: {} — omitiendo external_ref.", exc)
        return False


# ── Carga a DB ────────────────────────────────────────────────────────────────

def load_csv(filepath: Path, dry_run: bool = False) -> int:
    """
    Inserta las URLs en url_queue usando SQL parametrizado.
    Duplicados se omiten via ON CONFLICT DO NOTHING (por url).

    Returns:
        Numero de filas insertadas efectivamente.
    """
    rows = _parse_csv(filepath)
    if not rows:
        logger.warning("Ninguna URL valida en {}.", filepath)
        return 0

    if dry_run:
        logger.info("[DRY-RUN] Se cargarian {} URLs:", len(rows))
        for r in rows:
            logger.info("  id={:>6}  {}", r.ext_id, r.url)
        return 0

    has_ext = _has_external_ref_column()
    if has_ext:
        logger.info("Columna external_ref detectada — se guardara el id externo.")
    else:
        logger.warning(
            "Columna external_ref NO existe en url_queue — "
            "se insertara solo url/base_url. "
            "Aplica install_clean_v49.sql para habilitar esta columna."
        )

    if has_ext:
        sql = text("""
            INSERT INTO url_queue (url, base_url, external_ref)
            VALUES (:url, :url, :ext_id)
            ON CONFLICT (url) DO NOTHING
        """)
    else:
        sql = text("""
            INSERT INTO url_queue (url, base_url)
            VALUES (:url, :url)
            ON CONFLICT (url) DO NOTHING
        """)

    inserted = 0
    errors   = 0

    with get_db() as session:
        for row in rows:
            try:
                params = {"url": row.url}
                if has_ext:
                    params["ext_id"] = row.ext_id

                result = session.execute(sql, params)
                if result.rowcount == 1:
                    inserted += 1
                # rowcount == 0 → duplicado omitido por ON CONFLICT

            except Exception as exc:
                logger.error("Error en id={} url={}: {}", row.ext_id, row.url, exc)
                errors += 1

    skipped = len(rows) - inserted - errors
    logger.info(
        "Carga completada — insertados: {}  duplicados omitidos: {}  errores: {}",
        inserted, skipped, errors,
    )
    return inserted


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Carga URLs de Booking.com desde CSV sin cabecera (id,url)."
    )
    parser.add_argument("csv_file", help="Ruta al archivo CSV")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Solo muestra las URLs que se insertarian sin modificar la DB",
    )
    args = parser.parse_args()

    csv_path = Path(args.csv_file)
    if not csv_path.exists():
        logger.error("Archivo no encontrado: {}", csv_path)
        sys.exit(1)

    count = load_csv(csv_path, dry_run=args.dry_run)
    sys.exit(0)
