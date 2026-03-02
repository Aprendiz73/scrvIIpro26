"""
BookingScraper/app/database.py
Conexión PostgreSQL con SQLAlchemy 2.0
Windows 11 nativo - psycopg3

CORRECCIONES v1.1:
  [FIX] DATABASE_URL: postgresql+psycopg:// (psycopg3)
  [FIX] Todos los raw SQL envueltos en text() → SQLAlchemy 2.0
  [FIX] Pool: QueuePool con pre_ping para reconexión automática
  [FIX] connect_args sin opciones inválidas para psycopg3
"""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import os
from dotenv import load_dotenv
from loguru import logger

# Cargar variables de entorno
load_dotenv()

# ── URL DE CONEXIÓN ────────────────────────────────────────────────────────────
# ✅ FIX: postgresql+psycopg:// para psycopg3 (el prefijo postgresql:// es psycopg2)
_DB_USER     = os.getenv("DB_USER",     "postgres")
# [NEW-01] Default de contraseña eliminado — definir DB_PASSWORD en .env
# El centinela "change_me_in_dotenv" falla visiblemente al conectar.
_DB_PASSWORD = os.getenv("DB_PASSWORD", "change_me_in_dotenv")
_DB_HOST     = os.getenv("DB_HOST",     "localhost")
_DB_PORT     = os.getenv("DB_PORT",     "5432")
_DB_NAME     = os.getenv("DB_NAME",     "booking_scraper")

DATABASE_URL = (
    f"postgresql+psycopg://{_DB_USER}:{_DB_PASSWORD}"
    f"@{_DB_HOST}:{_DB_PORT}/{_DB_NAME}"
)

# ── MOTOR ──────────────────────────────────────────────────────────────────────
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,          # ✅ Reconecta automáticamente si la conexión se cayó
    pool_recycle=3600,           # Recicla conexiones cada 1 hora
    # [FIX BUG-V5-004] Timeouts para evitar bloqueo indefinido bajo carga.
    # pool_timeout: tiempo máximo esperando una conexión libre del pool (30 s).
    # connect_args: timeout TCP a nivel de driver psycopg3 (10 s).
    # pool_reset_on_return: ROLLBACK al devolver la conexión → estado limpio garantizado.
    pool_timeout=30,             # Máximo 30 s esperando conexión del pool
    pool_reset_on_return="rollback",  # Limpia transacciones pendientes al devolver
    connect_args={
        "connect_timeout": 10,       # TCP timeout psycopg3 (segundos)
        "options": "-c statement_timeout=60000",  # 60 s máx por query individual
    },
    echo=os.getenv("DEBUG", "false").lower() == "true",
)

# [FIX BUG-V5-020] Slow Query Logging — registra queries que superen el umbral.
# Umbral configurable vía env var SLOW_QUERY_THRESHOLD_MS (default: 2000 ms).
import time as _time
from sqlalchemy import event as _sa_event

_SLOW_QUERY_MS = float(os.getenv("SLOW_QUERY_THRESHOLD_MS", "2000"))

@_sa_event.listens_for(engine, "before_cursor_execute")
def _before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    conn.info.setdefault("query_start_time", []).append(_time.monotonic())

@_sa_event.listens_for(engine, "after_cursor_execute")
def _after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    start_times = conn.info.get("query_start_time", [])
    if start_times:
        elapsed_ms = (_time.monotonic() - start_times.pop()) * 1000
        if elapsed_ms > _SLOW_QUERY_MS:
            import logging as _logging
            _logging.getLogger("bookingscraper.slowquery").warning(
                f"[SLOW QUERY] {elapsed_ms:.0f}ms | {statement[:200].replace(chr(10), ' ')}"
            )

# ── SESIÓN ─────────────────────────────────────────────────────────────────────
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# ── BASE ORM ───────────────────────────────────────────────────────────────────
# [REGRESS-05/BUG-02] Base importado desde models.py — fuente única de verdad.
# Base = declarative_base() eliminado: causaba que tablas de models.py no se
# crearan con Base.metadata.create_all() — fallo silencioso de migración.
from app.models import Base  # noqa: F401 — re-exported for callers using create_all()



# ── MONITORIZACIÓN DEL POOL ────────────────────────────────────────────────────

def get_pool_status() -> dict:
    """
    [NEW-07] Métricas de utilización del pool en tiempo real.
    Expuesto en GET /health bajo la clave "db_pool".
    Permite detectar saturación antes de que se produzcan timeouts.
    """
    pool = engine.pool
    try:
        checked_out = pool.checkedout()
        capacity    = pool.size() + pool.overflow()
        return {
            "pool_size":       pool.size(),
            "checked_out":     checked_out,
            "overflow":        pool.overflow(),
            "checked_in":      pool.checkedin(),
            "utilization_pct": round(100.0 * checked_out / max(capacity, 1), 1),
        }
    except Exception as _pe:
        return {"error": str(_pe)}


def log_pool_status(threshold_pct: float = 80.0) -> None:
    """
    [NEW-07] Registra estado del pool. Emite WARNING si utilización >= threshold_pct%.
    """
    status = get_pool_status()
    pct    = status.get("utilization_pct", 0)
    if pct >= threshold_pct:
        logger.warning(
            f"⚠️ DB Pool alta utilización {pct}% | "
            f"size={status.get('pool_size')} checked_out={status.get('checked_out')} "
            f"overflow={status.get('overflow')}"
        )
    else:
        logger.debug(
            f"DB Pool OK {pct}% | "
            f"size={status.get('pool_size')} checked_out={status.get('checked_out')}"
        )


# ── DEPENDENCIA FASTAPI ────────────────────────────────────────────────────────
def get_db():
    """
    Generador de sesión para FastAPI (Depends).
    Uso: db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ── UTILIDADES ─────────────────────────────────────────────────────────────────
def test_connection() -> bool:
    """
    Prueba la conexión a PostgreSQL.
    ✅ FIX: Usa text() para SQLAlchemy 2.0
    """
    try:
        with SessionLocal() as db:
            # ✅ FIX: text() obligatorio en SQLAlchemy 2.0
            db.execute(text("SELECT 1"))
        logger.success("✓ Conexión a PostgreSQL exitosa")
        return True
    except Exception as e:
        logger.error(f"✗ Error de conexión a PostgreSQL: {e}")
        return False


def get_db_version() -> str:
    """
    Devuelve la versión de PostgreSQL.
    ✅ FIX: Usa text() para SQLAlchemy 2.0
    """
    try:
        with SessionLocal() as db:
            result = db.execute(text("SELECT version()")).fetchone()  # ✅ text()
        return result[0] if result else "Unknown"
    except Exception as e:
        return f"Error: {e}"


def execute_sql_file(filepath: str) -> bool:
    """
    Ejecuta un archivo SQL completo.
    ✅ FIX: Usa text() para SQLAlchemy 2.0
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            sql_content = f.read()

        # Separar por ; para ejecutar statement a statement
        statements = [s.strip() for s in sql_content.split(";") if s.strip()]

        with SessionLocal() as db:
            for stmt in statements:
                db.execute(text(stmt))   # ✅ text()
            db.commit()

        logger.success(f"✓ Archivo SQL ejecutado: {filepath}")
        return True
    except Exception as e:
        logger.error(f"✗ Error ejecutando SQL '{filepath}': {e}")
        return False


def get_url_queue_stats() -> dict:
    """
    Devuelve estadísticas de la cola de URLs.
    ✅ FIX: Usa text() para SQLAlchemy 2.0
    """
    try:
        with SessionLocal() as db:
            result = db.execute(text("""
                SELECT
                    COUNT(*) FILTER (WHERE status = 'pending')    AS pending,
                    COUNT(*) FILTER (WHERE status = 'processing') AS processing,
                    COUNT(*) FILTER (WHERE status = 'completed')  AS completed,
                    COUNT(*) FILTER (WHERE status = 'failed')     AS failed,
                    COUNT(*)                                       AS total
                FROM url_queue
            """)).fetchone()   # ✅ text()

        return {
            "pending":    result[0] or 0,
            "processing": result[1] or 0,
            "completed":  result[2] or 0,
            "failed":     result[3] or 0,
            "total":      result[4] or 0,
        }
    except Exception as e:
        logger.error(f"Error obteniendo stats: {e}")
        return {"pending": 0, "processing": 0, "completed": 0, "failed": 0, "total": 0}


# ── TEST STANDALONE ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("  Test de Conexión a PostgreSQL")
    print("=" * 60)

    if test_connection():
        print(f"\nVersión: {get_db_version()}")
        print(f"\nEstadísticas de URL Queue:")
        stats = get_url_queue_stats()
        for k, v in stats.items():
            print(f"  {k:12s}: {v}")
    else:
        print("\n✗ No se pudo conectar. Verificar PostgreSQL y .env")

    print("=" * 60)
