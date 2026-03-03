
"""
BookingScraper/scripts/create_project_structure.py
Script para crear la estructura completa del proyecto
Booking Scraper Pro
Windows 11 - Python 3.14.3

CORRECCIONES v2.0:
  [FIX BUG-A-15] base_dir hardcodeado a C:/BookingScraper eliminado.
    La raíz del proyecto ahora se calcula desde la ubicación de este script,
    lo que garantiza que funcione en cualquier directorio de instalación.
    Para instalar en C:\\BookingScraper, ejecutar desde ese directorio
    o pasar --base-dir C:\\BookingScraper como argumento.
"""

import os
import argparse
from pathlib import Path

# [FIX BUG-A-15] Raíz dinámica — padre del directorio scripts/
_SCRIPT_DIR   = Path(__file__).parent.resolve()
_DEFAULT_ROOT = _SCRIPT_DIR.parent  # directorio raíz del proyecto

def create_structure(base_dir: Path = None):
    """Crea toda la estructura de directorios del proyecto"""

    # [FIX BUG-A-15] base_dir calculado dinámicamente si no se pasa argumento
    if base_dir is None:
        base_dir = _DEFAULT_ROOT
    
    # Estructura de directorios
    directories = [
        # App principal
        "app",
        "app/core",
        "app/scraper",
        "app/models",
        "app/api",
        "app/api/routes",
        "app/api/dependencies",
        "app/tasks",
        
        # Scripts
        "scripts",
        "scripts/migrations",
        "scripts/backups",
        
        # Data
        "data",
        "data/images",
        "data/images/hotels",
        "data/images/rooms",
        "data/exports",
        "data/exports/csv",
        "data/exports/json",
        "data/exports/xlsx",
        "data/logs",
        "data/temp",
        
        # Logs
        "logs",
        "logs/api",
        "logs/celery",
        "logs/scraper",
        
        # Backups
        "backups",
        "backups/database",
        "backups/configs",
        
        # Documentación
        "docs",
        "docs/guides",
        "docs/api",
        
        # Tests
        "tests",
        "tests/unit",
        "tests/integration",
        
        # Configuración
        "config",
    ]
    
    # Crear directorios
    print("Creando estructura de directorios...")
    for directory in directories:
        dir_path = base_dir / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {directory}")
    
    # Crear archivos __init__.py
    init_dirs = [
        "app",
        "app/core",
        "app/scraper",
        "app/models",
        "app/api",
        "app/api/routes",
        "app/api/dependencies",
        "app/tasks",
        "tests",
        "tests/unit",
        "tests/integration",
    ]
    
    print("\nCreando archivos __init__.py...")
    for directory in init_dirs:
        init_file = base_dir / directory / "__init__.py"
        if not init_file.exists():
            init_file.write_text(f'"""{directory.replace("/", ".")} package"""\n')
            print(f"  ✓ {directory}/__init__.py")
    
    # Crear archivos .gitkeep en directorios vacíos
    gitkeep_dirs = [
        "data/images/hotels",
        "data/images/rooms",
        "data/exports/csv",
        "data/exports/json",
        "data/exports/xlsx",
        "data/temp",
        "logs/api",
        "logs/celery",
        "logs/scraper",
        "backups/database",
        "backups/configs",
    ]
    
    print("\nCreando archivos .gitkeep...")
    for directory in gitkeep_dirs:
        gitkeep_file = base_dir / directory / ".gitkeep"
        gitkeep_file.write_text("")
        print(f"  ✓ {directory}/.gitkeep")
    
    print("\n" + "="*60)
    print("✓ Estructura completa creada en:", base_dir)
    print("="*60)
    print("\nDirectorios creados:", len(directories))
    print("Archivos __init__.py:", len(init_dirs))
    print("Archivos .gitkeep:", len(gitkeep_dirs))


if __name__ == "__main__":
    import argparse as _ap
    _parser = _ap.ArgumentParser(description="Crear estructura de directorios del proyecto")
    _parser.add_argument(
        "--base-dir",
        type=Path,
        default=None,
        help=f"Directorio raíz del proyecto (default: {_DEFAULT_ROOT})",
    )
    _args = _parser.parse_args()
    create_structure(_args.base_dir)
