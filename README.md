# BookingScraper Pro

Sistema de scraping de hoteles de Booking.com con FastAPI, Celery, PostgreSQL 18 y Memurai.

## Requisitos

- Windows 11
- Python 3.14.3
- PostgreSQL 18
- Memurai (Redis para Windows)
- NordVPN (opcional)

## Instalacion Rapida

1. Ejecutar `instalar_dependencias.bat` para crear el entorno virtual e instalar paquetes
2. Configurar `.env` con las credenciales de la base de datos
3. Ejecutar `inicio_rapido.bat` para iniciar todos los servicios

## Uso

Ejecutar `control_master.bat` para acceder al panel de control con todas las opciones.

### Estructura del Proyecto

```
BookingScraper/
  app/
    api/          - Endpoints REST (URLs, Hotels, Jobs, System)
    core/         - Configuracion, DB, Redis, Logging
    models/       - Modelos SQLAlchemy
    schemas/      - Schemas Pydantic
    services/     - Logica de negocio
    tasks/        - Tareas Celery
    main.py       - Aplicacion FastAPI
  scripts/        - Scripts auxiliares
  alembic/        - Migraciones de DB
  logs/           - Archivos de log
  data/           - Datos exportados
```

### Codificacion UTF-8

Todo el sistema usa codificacion UTF-8. Si el archivo `.env` tiene caracteres especiales
en la contraseña de PostgreSQL, guardar el archivo como UTF-8 (en Notepad: Guardar como > UTF-8).

Ejecutar `python scripts/check_encoding.py` para verificar la codificacion de todos los archivos.

## API

- Documentacion: http://localhost:8000/docs
- Health check: http://localhost:8000/api/health
- Estadisticas: http://localhost:8000/api/stats
