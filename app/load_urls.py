"""
BookingScraper/scripts/load_urls.py
Script para carga masiva de URLs a la base de datos
Soporta CSV con/sin encabezado y archivos TXT
Compatible con PostgreSQL 15 y 18
Windows 11 - Python 3.14.3

CORRECCIONES v2.0:
  [FIX BUG-A-12] Migrado de psycopg2 a SQLAlchemy + psycopg3.
    El proyecto usa postgresql+psycopg:// (psycopg3) en toda la capa de BD.
    Usar psycopg2 directamente era inconsistente y requería una dependencia
    extra no necesaria. Ahora usa SQLAlchemy text() con parámetros nombrados,
    coherente con el resto del proyecto.

  [FIX BUG-A-13] Conteo de insertadas/duplicadas ahora es preciso.
    execute_batch() de psycopg2 llama executemany internamente; cursor.rowcount
    con ON CONFLICT DO NOTHING devuelve el rowcount del ÚLTIMO statement del
    batch, no el total. El nuevo approach usa RETURNING id para contar
    exactamente las filas insertadas vs descartadas por conflicto.

  [FIX BUG-A-14] Reemplazados todos los bare except: por except específicos.
    Los 3 bare except: (líneas 29, 154, 290) silenciaban errores críticos.
    Ahora cada bloque captura la excepción específica esperada.
"""

import argparse
import csv
import sys
import os
import re
from pathlib import Path
from typing import List, Tuple

# [FIX BUG-A-12] SQLAlchemy + psycopg3 en lugar de psycopg2 directo
try:
    from sqlalchemy import create_engine, text
    from sqlalchemy.exc import SQLAlchemyError
except ImportError:
    print("ERROR: sqlalchemy no instalado")
    print("Instalar con: pip install sqlalchemy psycopg")
    sys.exit(1)

# [FIX BUG-A-14] Bare except → except ImportError específico
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv es opcional; sin él se usan las vars de entorno del sistema

# =============================================================================
# CONFIGURACIÓN
# =============================================================================

_DB_HOST     = os.getenv("DB_HOST",     "localhost")
_DB_PORT     = os.getenv("DB_PORT",     "5432")
_DB_NAME     = os.getenv("DB_NAME",     "booking_scraper")
_DB_USER     = os.getenv("DB_USER",     "postgres")
_DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# Usados como defaults para argparse
DB_CONFIG = {
    "host":     _DB_HOST,
    "port":     int(_DB_PORT),
    "database": _DB_NAME,
    "user":     _DB_USER,
    "password": _DB_PASSWORD,
}


# =============================================================================
# FUNCIONES DE VALIDACIÓN
# =============================================================================

def is_valid_booking_url(url: str) -> bool:
    """
    Valida que sea una URL válida de Booking.com.

    Args:
        url: URL a validar.

    Returns:
        True si cumple el patrón de URL de hotel en Booking.com.
    """
    if not url or not isinstance(url, str):
        return False
    url = url.strip()
    pattern = r"^https?://(?:www\.)?booking\.com/hotel/.+\.html?$"
    return bool(re.match(pattern, url, re.IGNORECASE))


# =============================================================================
# CLASE PRINCIPAL
# =============================================================================

class URLLoader:
    """Cargador de URLs a la base de datos PostgreSQL (usa SQLAlchemy/psycopg3)."""

    def __init__(self, db_config: dict):
        self.db_config = db_config
        self._engine = None

    # ── CONEXIÓN ─────────────────────────────────────────────────────────────

    def connect(self) -> bool:
        """Construye el engine SQLAlchemy y verifica la conexión."""
        cfg = self.db_config
        # [FIX BUG-A-12] postgresql+psycopg:// usa psycopg3 — coherente con app/database.py
        url = (
            f"postgresql+psycopg://{cfg['user']}:{cfg['password']}"
            f"@{cfg['host']}:{cfg['port']}/{cfg['database']}"
        )
        try:
            self._engine = create_engine(url, pool_pre_ping=True)
            with self._engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("✓ Conectado a PostgreSQL")
            print(f"  Base de datos: {cfg['database']}")
            print(f"  Usuario:       {cfg['user']}")
            return True
        except SQLAlchemyError as e:
            print(f"✗ Error conectando a PostgreSQL: {e}")
            print("\nVerificar:")
            print(f"  - PostgreSQL está corriendo en {cfg['host']}:{cfg['port']}")
            print(f"  - Base de datos '{cfg['database']}' existe")
            print(f"  - Usuario '{cfg['user']}' tiene permisos")
            print(f"  - DB_PASSWORD es correcto")
            return False

    def disconnect(self) -> None:
        """Cierra el engine SQLAlchemy."""
        if self._engine:
            self._engine.dispose()
        print("✓ Desconectado de PostgreSQL")

    # ── CARGA DESDE CSV ───────────────────────────────────────────────────────

    def load_urls_from_csv(self, filepath: str) -> Tuple[int, int, List[str]]:
        """
        Carga URLs desde archivo CSV.

        Formatos aceptados:
          - Solo URLs (una por línea, sin encabezado)
          - url,priority  (con o sin encabezado)
          - URL en primera columna

        Returns:
            (urls_insertadas, urls_duplicadas, lista_de_errores)
        """
        urls_to_insert: List[Tuple[str, int]] = []
        errors: List[str] = []

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                first_line = f.readline().strip()
                f.seek(0)

                has_header = (
                    first_line.lower().startswith("url")
                    or ("," in first_line and not first_line.startswith("http"))
                )

                reader = csv.reader(f)
                if has_header:
                    next(reader)

                for i, row in enumerate(reader, start=1):
                    if not row or not row[0].strip():
                        continue

                    url = row[0].strip()
                    priority = 0
                    if len(row) > 1:
                        # [FIX BUG-A-14] except ValueError específico (no bare except:)
                        try:
                            priority = int(row[1])
                        except ValueError:
                            priority = 0

                    if not is_valid_booking_url(url):
                        errors.append(f"Línea {i}: URL inválida — {url}")
                        continue

                    urls_to_insert.append((url, priority))

        except FileNotFoundError:
            print(f"✗ Archivo no encontrado: {filepath}")
            return 0, 0, [f"Archivo no encontrado: {filepath}"]
        except (OSError, csv.Error) as e:
            print(f"✗ Error leyendo archivo: {e}")
            return 0, 0, [f"Error leyendo archivo: {e}"]

        if not urls_to_insert:
            print("✗ No se encontraron URLs válidas en el archivo")
            return 0, 0, errors

        return self._insert_urls(urls_to_insert, errors)

    # ── CARGA DESDE TXT ───────────────────────────────────────────────────────

    def load_urls_from_txt(self, filepath: str) -> Tuple[int, int, List[str]]:
        """
        Carga URLs desde archivo TXT (una URL por línea).
        Líneas que comienzan con # son ignoradas.
        """
        urls_to_insert: List[Tuple[str, int]] = []
        errors: List[str] = []

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, start=1):
                    url = line.strip()
                    if not url or url.startswith("#"):
                        continue
                    if not is_valid_booking_url(url):
                        errors.append(f"Línea {i}: URL inválida — {url}")
                        continue
                    urls_to_insert.append((url, 0))

        except FileNotFoundError:
            print(f"✗ Archivo no encontrado: {filepath}")
            return 0, 0, [f"Archivo no encontrado: {filepath}"]
        except OSError as e:
            print(f"✗ Error leyendo archivo: {e}")
            return 0, 0, [f"Error leyendo archivo: {e}"]

        if not urls_to_insert:
            print("✗ No se encontraron URLs válidas en el archivo")
            return 0, 0, errors

        return self._insert_urls(urls_to_insert, errors)

    # ── INSERCIÓN ────────────────────────────────────────────────────────────

    def _insert_urls(
        self,
        urls: List[Tuple[str, int]],
        errors: List[str],
    ) -> Tuple[int, int, List[str]]:
        """
        Inserta URLs en la base de datos en lotes de 100.

        [FIX BUG-A-13] Conteo preciso mediante RETURNING id.
        execute_batch() de psycopg2 usaba cursor.rowcount que con ON CONFLICT
        DO NOTHING devuelve solo el rowcount del ÚLTIMO statement del batch,
        produciendo conteos incorrectos. Con SQLAlchemy + RETURNING, contamos
        exactamente las filas insertadas y deducimos las duplicadas.

        Returns:
            (insertadas, duplicadas, errores)
        """
        insertadas = 0
        duplicadas = 0
        batch_size = 100
        total = len(urls)

        print(f"\nInsertando {total} URLs en la base de datos...")

        try:
            with self._engine.begin() as conn:
                for i in range(0, total, batch_size):
                    batch = urls[i : i + batch_size]
                    batch_inserted = 0

                    # [FIX BUG-A-13] INSERT individual con RETURNING para conteo exacto.
                    # Un único executemany con RETURNING no está bien soportado en todos
                    # los drivers para ON CONFLICT DO NOTHING — iteramos el batch de 100.
                    for url, priority in batch:
                        result = conn.execute(
                            text(
                                "INSERT INTO url_queue (url, priority, status) "
                                "VALUES (:url, :priority, 'pending') "
                                "ON CONFLICT (url) DO NOTHING "
                                "RETURNING id"
                            ),
                            {"url": url, "priority": priority},
                        )
                        rows = result.fetchall()
                        batch_inserted += len(rows)  # 1 si insertada, 0 si duplicada

                    insertadas += batch_inserted
                    duplicadas += len(batch) - batch_inserted

                    progress = min(i + batch_size, total)
                    print(f"  Procesadas: {progress}/{total} URLs", end="\r")

            print()  # Nueva línea tras progress

        except SQLAlchemyError as e:
            errors.append(f"Error insertando URLs: {e}")
            print(f"\n✗ Error en inserción: {e}")

        return insertadas, duplicadas, errors

    # ── ESTADÍSTICAS ─────────────────────────────────────────────────────────

    def get_statistics(self) -> dict:
        """Obtiene estadísticas de la cola de URLs por estado."""
        try:
            with self._engine.connect() as conn:
                result = conn.execute(
                    text(
                        "SELECT status, COUNT(*) AS cnt "
                        "FROM url_queue GROUP BY status ORDER BY status"
                    )
                )
                return {row[0]: row[1] for row in result.fetchall()}
        except SQLAlchemyError as e:
            print(f"⚠ No se pudieron obtener estadísticas: {e}")
            return {}


# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(
        description="Carga masiva de URLs de Booking.com a PostgreSQL",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  Cargar CSV con URLs solamente:
    python load_urls.py --file urls.csv

  Cargar CSV con URLs y prioridades:
    python load_urls.py --file urls_con_prioridad.csv

  Cargar archivo TXT:
    python load_urls.py --file urls.txt

Formatos de archivo CSV aceptados:
  1. Solo URLs (una por línea, sin encabezado)
  2. Con encabezado: url,priority
  3. URL en primera columna (ignora resto)

Formato de archivo TXT:
  - Una URL por línea
  - Líneas que empiecen con # son ignoradas
        """,
    )

    parser.add_argument("--file",        type=str, required=True,
                        help="Ruta al archivo CSV o TXT con las URLs")
    parser.add_argument("--db-host",     type=str,  default=DB_CONFIG["host"],
                        help=f"Host PostgreSQL (default: {DB_CONFIG['host']})")
    parser.add_argument("--db-port",     type=int,  default=DB_CONFIG["port"],
                        help=f"Puerto PostgreSQL (default: {DB_CONFIG['port']})")
    parser.add_argument("--db-name",     type=str,  default=DB_CONFIG["database"],
                        help=f"Base de datos (default: {DB_CONFIG['database']})")
    parser.add_argument("--db-user",     type=str,  default=DB_CONFIG["user"],
                        help=f"Usuario (default: {DB_CONFIG['user']})")
    parser.add_argument("--db-password", type=str,  default=DB_CONFIG["password"],
                        help="Password (default: desde .env)")

    args = parser.parse_args()

    print("=" * 70)
    print("  CARGADOR DE URLs - Booking Scraper Pro")
    print("=" * 70)
    print()

    db_config = {
        "host":     args.db_host,
        "port":     args.db_port,
        "database": args.db_name,
        "user":     args.db_user,
        "password": args.db_password,
    }

    filepath = Path(args.file)
    if not filepath.exists():
        print(f"✗ ERROR: Archivo no encontrado: {filepath}")
        sys.exit(1)

    extension = filepath.suffix.lower()
    if extension not in (".csv", ".txt"):
        print(f"✗ ERROR: Formato no soportado: {extension}")
        print("  Formatos aceptados: .csv, .txt")
        sys.exit(1)

    print(f"Archivo: {filepath}")
    print(f"Tipo:    {extension}")
    print()

    loader = URLLoader(db_config)
    if not loader.connect():
        sys.exit(1)

    try:
        if extension == ".csv":
            added, duplicates, errors = loader.load_urls_from_csv(str(filepath))
        else:
            added, duplicates, errors = loader.load_urls_from_txt(str(filepath))

        print()
        print("=" * 70)
        print("  RESULTADOS")
        print("=" * 70)
        print(f"  URLs añadidas:    {added}")
        print(f"  URLs duplicadas:  {duplicates}")
        print(f"  Errores:          {len(errors)}")
        print()

        if errors:
            print("Errores encontrados:")
            for error in errors[:10]:
                print(f"  - {error}")
            if len(errors) > 10:
                print(f"  ... y {len(errors) - 10} errores más")
            print()

        stats = loader.get_statistics()
        if stats:
            print("Estadísticas de la cola:")
            for status, count in stats.items():
                print(f"  {status:12}: {count}")

        print("=" * 70)

        if added > 0:
            print("\n✓ URLs cargadas exitosamente")
            sys.exit(0)
        else:
            print("\n⚠ No se añadieron URLs nuevas")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\n✗ Operación cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        loader.disconnect()


if __name__ == "__main__":
    main()
