"""
BookingScraper/scripts/verify_system.py
Script de verificación completa del sistema
Booking Scraper Pro
Windows 11 - Python 3.14.3

CORRECCIONES v2.0:
  [FIX BUG-A-07] Rutas de import corregidas:
    ANTES: app.core.database, app.core.config, app.tasks.celery_app
    AHORA: app.database,      app.config,      app.celery_app
  [FIX BUG-A-08] Rutas hardcodeadas C:/BookingScraper eliminadas.
    Raíz del proyecto calculada dinámicamente.
  [FIX BUG-A-09] Estructura de directorios actualizada al layout real.
    ANTES: app/core, app/scraper, app/tasks (layout legacy inexistente)
    AHORA: app/, scripts/, data/ (layout real plano actual)
  [FIX BUG-A-10] check_imports verifica 'psycopg' (psycopg3), no 'psycopg2'.
"""

import sys
import os
from pathlib import Path
import importlib

# [FIX BUG-A-08] Raíz del proyecto — dinámica desde ubicación del script
_PROJECT_ROOT = Path(__file__).parent.parent.resolve()

if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))


def check_python_version():
    """Verificar versión de Python"""
    print("[1] Verificando Python...")
    version = sys.version_info
    print(f"    Python {version.major}.{version.minor}.{version.micro}")
    if version.major != 3 or version.minor < 11:
        print("    ✗ Se requiere Python 3.11 o superior")
        return False
    print("    ✓ Versión compatible")
    return True


def check_imports():
    """Verificar imports críticos"""
    print("\n[2] Verificando imports críticos...")

    modules = {
        'fastapi':      'FastAPI',
        'uvicorn':      'Uvicorn',
        'celery':       'Celery',
        'redis':        'Redis',
        'selenium':     'Selenium',
        'bs4':          'BeautifulSoup',
        'sqlalchemy':   'SQLAlchemy',
        # [FIX BUG-A-10] 'psycopg2' -> 'psycopg': proyecto usa psycopg3
        'psycopg':      'PostgreSQL driver (psycopg3)',
        'PIL':          'Pillow',
        'pandas':       'Pandas',
        'loguru':       'Loguru',
        'dotenv':       'python-dotenv',
        'cloudscraper': 'CloudScraper',
        'psutil':       'psutil',
    }

    errors = []
    for module, name in modules.items():
        try:
            importlib.import_module(module)
            print(f"    ✓ {name}")
        except ImportError as e:
            print(f"    ✗ {name} — {e}")
            errors.append(module)

    if errors:
        print(f"\n    Faltan {len(errors)} módulos: {', '.join(errors)}")
        return False
    return True


def check_project_structure():
    """Verificar estructura real del proyecto"""
    print("\n[3] Verificando estructura del proyecto...")
    print(f"    Raíz: {_PROJECT_ROOT}")

    # [FIX BUG-A-08] Base dinámica
    # [FIX BUG-A-09] Layout real: módulos planos en app/, no subdirectorios legacy
    required_dirs = [
        "app",
        "scripts",
        "data",
        "data/images",
        "data/exports",
        "data/logs",
    ]

    missing = []
    for directory in required_dirs:
        dir_path = _PROJECT_ROOT / directory
        if dir_path.exists():
            print(f"    ✓ {directory}")
        else:
            print(f"    ✗ {directory} (no existe)")
            missing.append(directory)

    if missing:
        print(f"\n    Faltan {len(missing)} directorios requeridos")
        return False
    return True


def check_config_files():
    """Verificar archivos de configuración"""
    print("\n[4] Verificando archivos de configuración...")

    # [FIX BUG-A-08] Rutas calculadas dinámicamente
    required = {
        "env.example": "Plantilla de configuración",
        "alembic.ini": "Configuración Alembic",
    }
    optional = {
        ".env":                     "Configuración local",
        "requirements.txt":         "Dependencias Python",
        "requirements_windows.txt": "Dependencias Windows",
    }

    missing = []
    for filename, desc in required.items():
        fp = _PROJECT_ROOT / filename
        if fp.exists():
            print(f"    ✓ {filename} — {desc}")
        else:
            print(f"    ✗ {filename} — {desc} (no existe)")
            missing.append(filename)

    for filename, desc in optional.items():
        fp = _PROJECT_ROOT / filename
        mark = "✓" if fp.exists() else "—"
        print(f"    {mark} {filename} (opcional) — {desc}")

    if missing:
        print(f"\n    Faltan {len(missing)} archivos requeridos")
        return False
    return True


def check_database_connection():
    """Verificar conexión a base de datos"""
    print("\n[5] Verificando conexión a PostgreSQL...")
    try:
        # [FIX BUG-A-07] Ruta correcta: app.database (no app.core.database)
        from app.database import engine
        from sqlalchemy import text
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("    ✓ Conexión exitosa")
        return True
    except Exception as e:
        print(f"    ✗ Error: {e}")
        return False


def check_redis_connection():
    """Verificar conexión a Redis/Memurai"""
    print("\n[6] Verificando conexión a Redis/Memurai...")
    try:
        import redis
        # [FIX BUG-A-07] Ruta correcta: app.config (no app.core.config)
        from app.config import settings
        r = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            password=settings.REDIS_PASSWORD or None,
            decode_responses=True,
        )
        r.ping()
        print("    ✓ Conexión exitosa")
        return True
    except Exception as e:
        print(f"    ✗ Error: {e}")
        return False


def check_database_tables():
    """Verificar tablas de la base de datos"""
    print("\n[7] Verificando tablas de la base de datos...")
    try:
        # [FIX BUG-A-07] Ruta correcta: app.database
        from app.database import engine
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()

        required_tables = [
            "url_queue", "hotels", "scraping_logs",
            "vpn_rotations", "system_metrics", "url_language_status",
        ]

        missing = []
        for table in required_tables:
            if table in tables:
                print(f"    ✓ Tabla '{table}'")
            else:
                print(f"    ✗ Tabla '{table}' no existe")
                missing.append(table)

        if missing:
            print(f"\n    Faltan {len(missing)} tablas. Ejecutar create_tables.py")
            return False
        return True

    except Exception as e:
        print(f"    ✗ Error: {e}")
        return False


def check_celery_config():
    """Verificar configuración de Celery"""
    print("\n[8] Verificando configuración de Celery...")
    try:
        # [FIX BUG-A-07] Ruta correcta: app.celery_app (no app.tasks.celery_app)
        from app.celery_app import celery_app
        print(f"    ✓ Celery configurado")
        print(f"    Broker:  {celery_app.conf.broker_url}")
        print(f"    Backend: {celery_app.conf.result_backend}")
        print(f"    Pool:    {celery_app.conf.worker_pool}")
        return True
    except Exception as e:
        print(f"    ✗ Error: {e}")
        return False


def main():
    """Ejecutar todas las verificaciones"""
    print("=" * 70)
    print(" VERIFICACIÓN COMPLETA DEL SISTEMA")
    print(" Booking Scraper Pro - Windows 11")
    print(f" Raíz: {_PROJECT_ROOT}")
    print("=" * 70)
    print()

    checks = [
        ("Versión de Python",         check_python_version),
        ("Imports de módulos",        check_imports),
        ("Estructura del proyecto",   check_project_structure),
        ("Archivos de configuración", check_config_files),
        ("Conexión PostgreSQL",       check_database_connection),
        ("Conexión Redis/Memurai",    check_redis_connection),
        ("Tablas de base de datos",   check_database_tables),
        ("Configuración Celery",      check_celery_config),
    ]

    results = []
    for name, func in checks:
        try:
            result = func()
            results.append((name, result))
        except Exception as e:
            print(f"\n    ✗ Error inesperado en '{name}': {e}")
            results.append((name, False))

    print("\n" + "=" * 70)
    print(" RESUMEN")
    print("=" * 70)
    print()

    passed = sum(1 for _, r in results if r)
    total  = len(results)
    for name, result in results:
        print(f"  {'✓' if result else '✗'} {name}")

    print()
    print(f"Verificaciones: {passed}/{total} exitosas")

    if passed == total:
        print()
        print("=" * 70)
        print(" ✓ SISTEMA COMPLETAMENTE FUNCIONAL")
        print("=" * 70)
        return 0
    else:
        print()
        print("=" * 70)
        print(" ✗ SISTEMA TIENE PROBLEMAS — Revisar los errores anteriores")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    sys.exit(main())
