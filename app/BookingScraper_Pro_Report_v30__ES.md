# BookingScraper Pro — Reporte del Sistema
**Versión:** 6.0.0 (Auditoría v31) | **Fecha:** 2026-03-05 | **Plataforma:** Windows 11 (local)

---

## 1. Objetivo de la Aplicación

**BookingScraper Pro** es un sistema de extracción automática de datos de calidad productiva, orientado a [Booking.com](https://www.booking.com). Su propósito es recolectar datos estructurados de hoteles—nombres, direcciones, puntuaciones, descripciones, servicios, habitaciones y galerías de imágenes—en **múltiples idiomas simultáneamente**, almacenando todo en una base de datos PostgreSQL local para exportación y análisis.

### Metas Principales

| Meta | Implementación |
|---|---|
| Extracción multi-idioma | 5 idiomas por defecto: `en`, `es`, `de`, `fr`, `it` |
| Resistencia anti-detección | Rotación NordVPN + CloudScraper + delays aleatorios |
| Integridad de datos | Constraints PostgreSQL, upserts idempotentes, locking optimista |
| Captura completa de imágenes | Interacción con modal de galería vía Selenium + descarga paralela |
| Confiabilidad productiva | Circuit breakers, watchdog, shutdown limpio, logging de auditoría |

---

## 2. Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────────────────┐
│                      Windows 11 — Local                             │
│                                                                      │
│  ┌──────────────┐  REST API     ┌─────────────────────────────────┐ │
│  │  Cliente /   │◄──────────────►│      FastAPI (main.py)          │ │
│  │  Navegador   │               │ /health /metrics /stats          │ │
│  └──────────────┘               │ /scraping/upload /vpn/status     │ │
│                                 └──────────────┬────────────────── ┘ │
│                                                │                     │
│                          ┌─────────────────────▼────────────────┐   │
│                          │       scraper_service.py              │   │
│                          │  - Despacho de URLs (CTE atómica)    │   │
│                          │  - ThreadPoolExecutor                 │   │
│                          │  - Circuit breaker VPN               │   │
│                          │  - Circuit breaker Redis (HIGH-002)   │   │
│                          └──────┬────────────────┬──────────────┘   │
│                                 │                │                   │
│              ┌──────────────────▼──┐    ┌────────▼──────────────┐   │
│              │    scraper.py       │    │ vpn_manager_windows   │   │
│              │  BookingScraper     │    │ Wrapper NordVPN CLI   │   │
│              │  CloudScraper/Brave │    │ Rotación de IP + caché│   │
│              │  Inyección de idioma│    └───────────────────────┘   │
│              └──────────┬──────── ┘                                 │
│                         │                                           │
│         ┌───────────────▼──────────────────────────────────────┐   │
│         │                  extractor.py                         │   │
│         │  BeautifulSoup + XPath — extracción de datos hotel    │   │
│         │  Diccionarios de categoría de rating en 8 idiomas     │   │
│         └──────────────────────────┬───────────────────────────┘   │
│                                    │                                │
│  ┌─────────────────┐   ┌───────────▼──────────────┐  ┌──────────┐ │
│  │image_downloader │   │      PostgreSQL           │  │  Redis/  │ │
│  │ Pillow resize   │   │  6 tablas + 20+ índices   │  │ Memurai  │ │
│  │ integrity check │   │  JSONB, GIN, partial idx  │  │ (broker) │ │
│  └─────────────────┘   └──────────────────────────┘  └──────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

### Stack Tecnológico

| Componente | Tecnología | Versión |
|---|---|---|
| Framework API | FastAPI + Uvicorn | 0.115.x / 0.32.x |
| ORM | SQLAlchemy | 2.0.x |
| Base de datos | PostgreSQL | 15+ |
| Driver BD | psycopg3 (psycopg[binary]) | 3.2.x |
| Cola de tareas | Celery (solo pool) | 5.4.x |
| Broker de mensajes | Redis / Memurai | 5.2.x |
| Automatización de navegador | Selenium + Brave | 4.27.x |
| Scraping HTTP | CloudScraper | 1.2.x |
| Procesamiento de imágenes | Pillow | 11.0.x |
| Configuración | Pydantic Settings v2 | 2.10.x |
| Logging | Loguru | 0.7.x |
| VPN | NordVPN CLI (Windows) | — |
| Runtime | Python | 3.14.x |
| SO | Windows 11 | local |

---

## 3. Workflow del Sistema

### 3.1 Ingesta de URLs

```
Archivo CSV (urls_ejemplo.csv)
         │
         ▼
   load_urls.py
         │
   INSERT INTO url_queue
   (url, status='pending', priority=0)
   ON CONFLICT DO NOTHING
```

Cada línea del CSV contiene una URL de hotel de Booking.com. El loader deduplica en el INSERT.

### 3.2 Ciclo de Despacho

El sistema soporta dos modos de despacho (configurado via `USE_CELERY_DISPATCHER`):

**Modo A — Bucle asyncio (por defecto, recomendado para Windows 11):**
```
main.py lifespan startup
    │
    └── _auto_dispatch_loop() [Tarea asyncio]
              │
              cada 30 segundos:
              │
              ▼
        scraper_service.process_batch(batch_size)
              │
              ▼
        CTE atómica: SELECT filas pending + UPDATE a 'processing'
        (FOR UPDATE SKIP LOCKED — cero condiciones de carrera)
              │
              ▼
        ThreadPoolExecutor.submit(scrape_one, url_id)
```

**Modo B — Celery Beat (opcional):**
```
celery beat → tarea process_pending_urls → process_batch()
```

### 3.3 Pipeline de Scraping (por URL)

```
scrape_one(url_id)
    │
    ├── 1. Verificación VPN / reconexión si es necesario
    │
    ├── 2. completeness_service.initialize_url_processing()
    │       └── INSERT filas url_language_status (idempotente)
    │
    ├── 3. Por cada idioma (ordenados alfabéticamente — prevención de deadlock):
    │       │
    │       ├── build_language_url() → construye URL localizada
    │       │   Ej.: hotel.en-gb.html?lang=en-gb
    │       │
    │       ├── CloudScraper o Brave browser → GET página
    │       │
    │       ├── extractor.py → parsear HTML:
    │       │   • nombre del hotel (limpiado: sin prefijos de estrellas)
    │       │   • dirección, descripción
    │       │   • rating + rating_category (diccionario 8 idiomas)
    │       │   • subscores de reviews (JSONB)
    │       │   • instalaciones, servicios (JSONB)
    │       │   • house_rules, important_info
    │       │   • images_urls (interacción con modal de galería via Selenium)
    │       │
    │       ├── Verificación de idioma → rotar VPN + reintentar si idioma incorrecto
    │       │
    │       ├── _save_hotel() → INSERT INTO hotels ON CONFLICT DO NOTHING
    │       │
    │       └── record_language_success/failure()
    │
    ├── 4. Descarga de imágenes (solo language=DEFAULT):
    │       └── image_downloader.ImageDownloader.download_images()
    │           • ThreadPoolExecutor (MAX_IMAGE_WORKERS en paralelo)
    │           • Verificación de integridad Pillow.verify()
    │           • Redimensionar a máximo 1920×1080 JPEG
    │           • Idempotente: omite archivos existentes
    │
    ├── 5. completeness_service.finalize_url()
    │       └── UPDATE url_queue SET status='completed'/'incomplete'
    │
    └── 6. _maybe_rotate_vpn() → rotar después de cada N hoteles
```

### 3.4 Estrategia de Rotación VPN

```
Disparadores para rotación VPN:
  • Cada VPN_ROTATE_EVERY_N=10 hoteles (programado)
  • Tras 3+ fallos consecutivos (detección de anomalía)
  • Tras 3+ mismatches de idioma (bloqueo geo-IP detectado)
  • Explícito: POST /vpn/rotate

Circuit Breaker (VPN):
  CERRADO → normal → ABIERTO (tras 5 fallos) → cooldown 300s → SEMI-ABIERTO → prueba
```

### 3.5 Almacenamiento de Datos

```
url_queue           → una fila por URL única de hotel
hotels              → una fila por (url × idioma)
url_language_status → tracker de progreso por idioma
scraping_logs       → rastro de auditoría completo
vpn_rotations       → log de eventos VPN
system_metrics      → snapshots periódicos de recursos
```

### 3.6 Exportación

```
export_data.py
    │
    ├── CSV   → pandas DataFrame → hotels.csv
    ├── JSON  → hotels.json
    └── Excel → hotels.xlsx (via openpyxl)
```

---

## 4. Esquema de Base de Datos

### Tablas y Constraints Clave

| Tabla | PK | Índices Clave | Constraints Notables |
|---|---|---|---|
| `url_queue` | `id` | Índice parcial `status='pending'`, `url` UNIQUE | CHECK status en enum |
| `hotels` | `id` | UNIQUE `(url_id, lang)`, GIN en todas las cols JSONB, B-Tree en `url` | CHECK rating 0–10, guardas de tipo JSONB |
| `url_language_status` | `id` | UNIQUE `(url_id, language)` | CASCADE delete desde url_queue |
| `scraping_logs` | `id` | `url_id`, `timestamp DESC` | — |
| `vpn_rotations` | `id` | `rotated_at DESC` | — |
| `system_metrics` | `id` | `recorded_at DESC` | — |

### Seguridad de Concurrencia

- **CTE atómica de despacho**: round-trip SQL único elimina la ventana de carrera SELECT+UPDATE
- **FOR UPDATE SKIP LOCKED**: cero bloqueo entre workers concurrentes
- **Locking optimista**: columna `version_id` en `url_queue` y `url_language_status`
- **Orden alfabético de idiomas**: prevención de deadlock por adquisición consistente de locks
- **Aislamiento serializable** disponible via `get_serializable_db()` para rutas críticas

---

## 5. Modelo de Seguridad

| Capa | Implementación |
|---|---|
| Autenticación API | Verificación de header `API_KEY` (configurable, vacío = modo dev) |
| SQL Injection | 100% consultas parametrizadas (SQLAlchemy text() con params bound) |
| Gestión de credenciales | Todos los secretos via `.env` (nunca hardcodeados) |
| Exposición de errores | HTTP 500 genérico con correlation ID — sin stack traces al cliente |
| Rate limiting | Ventana deslizante en memoria por IP de cliente, limpieza de buckets obsoletos |
| Path traversal | Guardia `is_relative_to()` en image_downloader |
| Truncado de errores | `MAX_ERROR_LEN=2000` previene desbordamiento de columna DB |
| Sanitización de logs | Credenciales de URL eliminadas antes de logging |

---

## 6. Correcciones Enterprise — Auditoría v31

### Corregidos en esta versión

| ID | Severidad | Descripción | Archivo(s) |
|---|---|---|---|
| HIGH-002 | ALTA | Circuit breaker Redis — previene latencia bloqueante tras fallo de Redis | `scraper_service.py` |
| HIGH-004 | ALTA | Signal handlers Windows (SIGINT, SIGBREAK) para shutdown limpio | `main.py` |
| HIGH-005 | MEDIA | Constante `MAX_ERROR_LEN` centralizada — elimina duplicados hardcodeados | `config.py`, `scraper_service.py`, `completeness_service.py` |
| HIGH-013 | MEDIA | Límites de tiempo Celery ajustados (600s→180s) — previene agotamiento de workers | `tasks.py` |
| MED-022 | MEDIA | Endpoint `/metrics` — contadores JSON de rendimiento para monitoreo | `main.py` |
| NUEVO | BAJA | Import `os` faltante en `tasks.py` | `tasks.py` |
| NUEVO | BAJA | Nuevas variables `.env.example` documentadas (Redis CB, MAX_ERROR_LEN, límites Celery) | `.env.example` |
| NUEVO | SQL | Script de instalación limpia `install_clean_v31.sql` con todas las tablas + índices | `install_clean_v31.sql` |

### Resueltos previamente (v30 y anteriores)

| ID | Descripción |
|---|---|
| CRIT-001 | `vpn_manager.py` faltante |
| CRIT-002 | Función `build_language_url()` faltante |
| CRIT-003 | Condición de carrera en despacho de URLs — reemplazado con CTE atómica |
| CRIT-004 | Agotamiento del pool — caps de tamaño de pool con límite máximo |
| CRIT-007 | Acumulación de archivos HTML debug — purga por edad/tamaño |
| HIGH-001 | Truncado silencioso de batch_size — reemplazado con `ValueError` explícito |
| HIGH-003 | Índice B-Tree faltante en `hotels.url` |
| HIGH-006 | `/health` retornando HTTP 200 en estado degradado (ahora 503) |
| HIGH-007 | TTL de caché IP VPN demasiado largo (30s→5s) + invalidación explícita |
| HIGH-008 | Verificación de integridad de imágenes vía `Pillow.Image.verify()` |
| HIGH-009 | Limpieza de sesión `scrape_one()` en bloque `finally` |
| HIGH-010 | Índice GIN faltante en `hotels.images_urls` |
| MED-011 | Reintento con backoff exponencial para conexión a BD |
| LOW-006 | Llamadas `print()` reemplazadas con `logger.info()` |

---

## 7. Referencia de Configuración

Todos los ajustes se gestionan via `app/.env.example` → copiar a `app/.env` y completar valores.

### Configuración crítica

```env
# Base de datos (requerido)
DB_PASSWORD=<tu_password_postgres>

# Scraping
LANGUAGES_ENABLED=en,es,de,fr,it
USE_SELENIUM=True          # True=navegador Brave, False=CloudScraper
DOWNLOAD_IMAGES=True

# VPN (opcional)
VPN_ENABLED=False          # True solo con NordVPN instalado
SCRAPER_MAX_WORKERS=1      # debe ser 1 cuando VPN_ENABLED=True

# Límites de tareas Celery (v31)
CELERY_TASK_SOFT_TIME_LIMIT=150
CELERY_TASK_TIME_LIMIT=180

# Circuit breaker Redis (v31)
REDIS_FAILURE_THRESHOLD=5
REDIS_COOLDOWN_SECONDS=60

# Almacenamiento de errores
MAX_ERROR_LEN=2000
```

---

## 8. Instalación — Windows 11

```batch
:: 1. Clonar repositorio
git clone https://github.com/Aprendiz73/scrvIIpro26.git C:\BookingScraper
cd C:\BookingScraper

:: 2. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate

:: 3. Instalar dependencias
pip install -r app\requirements.txt

:: 4. Configurar entorno
copy app\.env.example app\.env
:: Editar app\.env con tu DB_PASSWORD y configuración

:: 5. Crear base de datos (psql como superusuario postgres)
psql -U postgres -c "CREATE DATABASE booking_scraper ENCODING='UTF8' TEMPLATE=template0;"
psql -U postgres -d booking_scraper -f app\install_clean_v31.sql

:: 6. Iniciar servicios (Memurai/Redis debe estar corriendo)
start_services.bat

:: 7. Cargar URLs
python -m app.load_urls app\urls_ejemplo.csv

:: 8. Acceder a la API
:: http://localhost:8000/docs
```

---

## 9. Endpoints de la API

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/health` | Salud del sistema (200 OK / 503 degradado) |
| GET | `/metrics` | Contadores de rendimiento (v31 NUEVO) |
| GET | `/stats` | Estadísticas de scraping |
| GET | `/vpn/status` | Estado VPN + circuit breaker |
| POST | `/vpn/rotate` | Forzar rotación de VPN |
| POST | `/scraping/upload-csv` | Subir archivo CSV de URLs |
| POST | `/scraping/force-now` | Forzar despacho inmediato |
| GET | `/docs` | Swagger UI |

---

## 10. Issues Abiertos Pendientes

| ID | Prioridad | Descripción |
|---|---|---|
| MED-012 | MEDIA | Migraciones Alembic no automatizadas (scripts SQL manuales) |
| MED-015 | MEDIA | Sin particionamiento en `scraping_logs` (necesario >10M filas) |
| MED-018 | MEDIA | Sin OpenTelemetry / trazabilidad distribuida |
| HIGH-011 | MEDIA | Rate limiter solo en memoria (no distribuido entre workers) |
| HIGH-012 | BAJA | FK nullable `hotels.url_id` — registros huérfanos posibles |
| HIGH-014 | BAJA | `LANGUAGES_ENABLED` validado al inicio pero no en recarga en runtime |

---

*Reporte generado: 2026-03-05 | Ciclo de auditoría: v31 Enterprise*
