# BookingScraper Pro — Reporte de Instalación y Modificaciones v33

**Versión:** 6.0.0  
**Fecha:** 2026-03-05  
**Plataforma:** Windows 11 (despliegue local, proceso único)  
**Ciclo:** v33 — Instalación Limpia  
**Repositorio:** https://github.com/Aprendiz73/scrvIIpro26.git

---

## Tabla de Contenidos

1. [Requisitos del Sistema](#1-requisitos-del-sistema)
2. [Estructura de Archivos del Proyecto](#2-estructura-de-archivos-del-proyecto)
3. [Instalación Limpia — Paso a Paso](#3-instalación-limpia--paso-a-paso)
4. [Referencia de Configuración (.env)](#4-referencia-de-configuración-env)
5. [Configuración de la Base de Datos](#5-configuración-de-la-base-de-datos)
6. [Iniciar y Detener la Aplicación](#6-iniciar-y-detener-la-aplicación)
7. [Referencia de Endpoints API](#7-referencia-de-endpoints-api)
8. [Modificaciones Realizadas (v30 → v33)](#8-modificaciones-realizadas-v30--v33)
9. [Visión General de la Arquitectura](#9-visión-general-de-la-arquitectura)
10. [Resolución de Problemas](#10-resolución-de-problemas)

---

## 1. Requisitos del Sistema

### Software Obligatorio

| Componente | Versión | Notas |
|---|---|---|
| Windows 11 | 21H2 o posterior | 64-bit requerido |
| Python | 3.14.x | Build estándar con GIL desde python.org |
| PostgreSQL | 14 o posterior | Instalación local |
| Git | Cualquier reciente | Para clonar el repositorio |

### Software Opcional

| Componente | Propósito | Requerido Cuando |
|---|---|---|
| Memurai / Redis para Windows | Cola de tareas + estado compartido | `USE_CELERY_DISPATCHER=True` |
| NordVPN (cliente Windows + CLI) | Rotación de IP durante el scraping | `VPN_ENABLED=True` |
| Brave Browser | Automatización con Selenium | `USE_SELENIUM=True` |

### Hardware Mínimo

| Recurso | Mínimo | Recomendado |
|---|---|---|
| RAM | 4 GB | 8 GB |
| Disco | 10 GB libre | 20 GB libre |
| CPU | 2 núcleos | 4 núcleos |
| Red | Banda ancha cualquiera | Conexión estable |

---

## 2. Estructura de Archivos del Proyecto

```
C:\BookingScraper\                          ← Raíz del proyecto
│
├── .env                                    ← Tu configuración (copia de .env.example)
├── .env.example                            ← Plantilla con TODOS los ajustes documentados
├── .gitignore                              ← Excluye .env, venv, __pycache__, data/
│
├── alembic.ini                             ← Config Alembic (credenciales vía env.py, NO en texto plano)
│
├── alembic/
│   └── env.py                             ← Runtime Alembic: lee DB_PASSWORD desde .env
│
├── app/                                    ← Paquete principal de la aplicación
│   │
│   ├── main.py              (2.075 líneas) ← App FastAPI, lifespan, rutas, rate limiter
│   ├── config.py            (407 líneas)  ← Settings Pydantic, variables de entorno, rutas
│   ├── models.py            (339 líneas)  ← Modelos ORM SQLAlchemy + índices
│   ├── database.py          (350 líneas)  ← Pool de conexiones, sesiones, health check
│   │
│   ├── scraper_service.py   (1.494 líneas)← Orquestación: despacho, rotación VPN, CB Redis
│   ├── scraper.py           (1.369 líneas)← Fetch de página con Selenium/CloudScraper + parse
│   ├── extractor.py         (485 líneas)  ← Extracción de datos del HTML parseado
│   ├── completeness_service.py (631 líneas)← Seguimiento de completitud por idioma
│   ├── image_downloader.py  (324 líneas)  ← Descarga de imágenes, redimensión, verificación Pillow
│   │
│   ├── tasks.py             (231 líneas)  ← Tareas Celery (modo opcional)
│   ├── celery_app.py        (103 líneas)  ← Configuración Celery (solo pool, Windows)
│   │
│   ├── vpn_manager.py       (78 líneas)   ← Factory VPN (enrutador por plataforma)
│   ├── vpn_manager_windows.py (762 líneas)← Implementación NordVPN para Windows
│   │
│   ├── install_clean_v31.sql (648 líneas) ← ⚠️ SOLO INSTALACIÓN LIMPIA — elimina y recrea todas las tablas
│   │
│   ├── export_data.py                     ← Exportación de datos CSV/JSON/Excel
│   ├── load_urls.py                       ← Importación masiva de URLs desde CSV
│   ├── create_tables.py                   ← Creación programática de tablas (alternativa al SQL)
│   ├── verify_system.py                   ← Script de verificación del sistema en startup
│   │
│   ├── requirements.txt                   ← Dependencias Python (compatibles con Python 3.14)
│   └── urls_ejemplo.csv                  ← Formato de ejemplo del archivo de entrada de URLs
│
├── scripts/                               ← Scripts utilitarios (duplicados de app/)
│   ├── __init__.py
│   ├── create_project_structure.py
│   ├── create_tables.py
│   ├── export_data.py
│   ├── load_urls.py
│   └── verify_system.py
│
├── data/                                  ← Creado automáticamente al primer arranque
│   ├── images/                            ← Imágenes de hoteles descargadas
│   ├── exports/                           ← Exportaciones CSV/JSON/Excel
│   ├── logs/                              ← Archivos de log rotativos (api.log, máx 10 × 50 MB)
│   └── debug_html/                        ← HTML de depuración temporal (purgado cada 24h)
│
├── inicio_rapido.bat                      ← Inicio rápido: solo FastAPI (recomendado)
├── start_services.bat                     ← Inicio completo: FastAPI + Worker Celery + Beat
├── stop_services.bat / detener_todo.bat   ← Detener todos los procesos
├── backup_db.bat                          ← Backup de PostgreSQL con pg_dump
├── limpiar_cache.bat                      ← Limpiar __pycache__ de Python
└── instalar_edge_driver.bat               ← Instalar Edge WebDriver (si se usa Edge)
```

> **Nota sobre `alembic_env.py`:** El archivo descargado como `alembic_env.py` debe colocarse en `C:\BookingScraper\alembic\env.py`. Solo se utiliza al ejecutar comandos de migración Alembic (`alembic upgrade head`). Si usas `install_clean_v31.sql` para una instalación limpia, este archivo no es necesario para la operación normal.

---

## 3. Instalación Limpia — Paso a Paso

> ⚠️ **Esta es una guía de INSTALACIÓN LIMPIA.** Asume una base de datos vacía. No ejecutes `install_clean_v31.sql` en una base de datos que ya tenga datos — eliminará y recreará todas las tablas.

### Paso 1 — Clonar el Repositorio

```bat
cd C:\
git clone https://github.com/Aprendiz73/scrvIIpro26.git BookingScraper
cd C:\BookingScraper
```

### Paso 2 — Crear el Entorno Virtual Python

```bat
cd C:\BookingScraper
python -m venv venv
```

Verificar la versión de Python:
```bat
venv\Scripts\python.exe --version
```
Salida esperada: `Python 3.14.x`

### Paso 3 — Instalar Dependencias Python

```bat
venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\python.exe -m pip install -r app\requirements.txt
```

> **Importante para Python 3.14:** Todos los paquetes en `requirements.txt` tienen ruedas (wheels) `cp314-win_amd64` o `abi3` verificadas. No degradar las versiones — las versiones fijadas son específicas para compatibilidad con Python 3.14.

Tiempo de instalación estimado: 3–8 minutos según velocidad de red.

### Paso 4 — Configurar el Entorno

```bat
copy .env.example .env
notepad .env
```

**Ajustes mínimos requeridos a cambiar:**

```ini
DB_PASSWORD=tu_contraseña_real_de_postgres
API_KEY=cualquier-cadena-aleatoria-fuerte-que-elijas
```

Todos los demás ajustes tienen valores predeterminados seguros para despliegue local en Windows 11.

### Paso 5 — Crear la Base de Datos PostgreSQL

Abre **pgAdmin** o **psql** y ejecuta:

```sql
-- En psql o en la herramienta de consulta de pgAdmin:
CREATE DATABASE booking_scraper;
```

Luego en una ventana de comandos:

```bat
cd C:\BookingScraper
venv\Scripts\python.exe -c "from app.config import settings; print(settings.DATABASE_URL)"
```

Esto confirma que tu `.env` se está leyendo correctamente.

### Paso 6 — Instalar el Esquema de Base de Datos (Limpio)

**Opción A — Usando la línea de comandos psql:**
```bat
psql -U postgres -d booking_scraper -f app\install_clean_v31.sql
```

**Opción B — Usando pgAdmin:**
1. Abrir pgAdmin → conectar a la base de datos `booking_scraper`
2. Herramientas → Herramienta de Consulta
3. Abrir `app\install_clean_v31.sql`
4. Ejecutar (F5)

Salida esperada: serie de instrucciones `CREATE TABLE`, `CREATE INDEX`, `CREATE FUNCTION`, `SELECT` sin errores.

**Qué crea `install_clean_v31.sql`:**

| Objeto | Tipo | Notas |
|---|---|---|
| `url_queue` | Tabla | Cola de entrada de URLs con prioridad y lógica de reintentos |
| `hotels` | Tabla | Datos de hoteles extraídos (multi-idioma) |
| `url_language_status` | Tabla | Seguimiento de progreso de scraping por idioma |
| `scraping_logs` | Tabla Particionada | Particiones mensuales por rango (FIX-025) |
| `vpn_rotations` | Tabla | Log de auditoría de rotaciones VPN |
| `system_metrics` | Tabla | Instantáneas de CPU/memoria/disco |
| `create_scraping_logs_partition()` | Función | Gestión de particiones en PL/pgSQL |
| 25+ índices | Índices | B-Tree, GIN, índices parciales |

### Paso 7 — Verificar la Instalación

```bat
cd C:\BookingScraper
venv\Scripts\python.exe app\verify_system.py
```

Salida esperada:
```
✓ Python 3.14.x
✓ Todas las importaciones OK
✓ Conexión a base de datos OK
✓ Tablas verificadas
✓ Sistema listo
```

### Paso 8 — Cargar URLs

Preparar un archivo CSV (una URL por línea, sin cabecera):

```
https://www.booking.com/hotel/es/hotel-name.en-gb.html
https://www.booking.com/hotel/fr/paris-hotel.en-gb.html
```

Cargar en la base de datos:
```bat
venv\Scripts\python.exe app\load_urls.py --file urls_ejemplo.csv
```

### Paso 9 — Iniciar la Aplicación

**Modo recomendado (asyncio, sin Celery requerido):**
```bat
inicio_rapido.bat
```
o manualmente:
```bat
cd C:\BookingScraper
venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

La aplicación iniciará y comenzará el scraping automáticamente tras un retardo de inicialización de 5 segundos.

Abrir el navegador: **http://localhost:8000/docs**

---

## 4. Referencia de Configuración (.env)

### Ajustes Críticos

| Variable | Valor por Defecto | Requerido | Descripción |
|---|---|---|---|
| `DB_PASSWORD` | *(vacío)* | **SÍ** | Contraseña PostgreSQL — la app no inicia si está vacío |
| `API_KEY` | *(vacío)* | Recomendado | Protege `/scraping/force-now` y otros endpoints de escritura |

### Base de Datos

| Variable | Por Defecto | Descripción |
|---|---|---|
| `DB_HOST` | `localhost` | Host PostgreSQL |
| `DB_PORT` | `5432` | Puerto PostgreSQL |
| `DB_USER` | `postgres` | Usuario PostgreSQL |
| `DB_NAME` | `booking_scraper` | Nombre de la base de datos |
| `DB_POOL_SIZE` | `5` | Conexiones por proceso |
| `DB_MAX_OVERFLOW` | `5` | Conexiones extra durante picos |
| `DB_TOTAL_HARD_CAP` | `50` | Máximo entre todos los procesos |

### Comportamiento del Scraping

| Variable | Por Defecto | Descripción |
|---|---|---|
| `USE_SELENIUM` | `False` | `True` = Brave/Chromium; `False` = CloudScraper |
| `SCRAPER_MAX_WORKERS` | `1` | **Debe ser 1 cuando VPN_ENABLED=True** |
| `LANGUAGES_ENABLED` | `en,es,de,fr,it` | Códigos ISO 639-1 separados por coma |
| `DEFAULT_LANGUAGE` | `en` | Se raspa primero en cada hotel |
| `BATCH_SIZE` | `5` | URLs despachadas por ciclo de 30 segundos |
| `MAX_RETRIES` | `3` | Máximo de intentos por URL |
| `MIN_REQUEST_DELAY` | `2.0` | Segundos mínimos entre peticiones |
| `MAX_REQUEST_DELAY` | `5.0` | Segundos máximos entre peticiones |

### VPN (Opcional)

| Variable | Por Defecto | Descripción |
|---|---|---|
| `VPN_ENABLED` | `False` | Activar rotación de NordVPN |
| `VPN_COUNTRIES` | `UK,US,CA,DE,FR,NL,IT,ES` | Pool de países para rotación |
| `VPN_ROTATE_EVERY_N` | `10` | Hoteles entre rotaciones |
| `VPN_FAILOVER_TIMEOUT_SECS` | `90` | Segundos antes de modo degradado |

### Nuevos en v33

| Variable | Por Defecto | Descripción |
|---|---|---|
| `EXECUTOR_SHUTDOWN_TIMEOUT_SECS` | `30` | Segundos de espera para tareas en vuelo durante apagado graceful (FIX-019) |

---

## 5. Configuración de la Base de Datos

### Visión General del Esquema

```
url_queue (entrada)
    │
    ├──→ hotels (salida: datos de hotel por idioma)
    ├──→ url_language_status (progreso por idioma)
    └──→ scraping_logs (auditoría — particionado mensualmente)
             scraping_logs_2026_03   ← partición: marzo 2026
             scraping_logs_2026_04   ← partición: abril 2026
             scraping_logs_2026_05   ← partición: mayo 2026
             ...

vpn_rotations   (log de auditoría VPN)
system_metrics  (monitoreo de recursos)
```

### Gestión de Particiones Mensuales

La tabla `scraping_logs` usa particionamiento mensual por rango (nuevo en v33). Se crean tres particiones en el momento de la instalación (mes actual + 2 adelante). Para crear particiones futuras:

```sql
-- Ejecutar al inicio de cada nuevo mes
SELECT create_scraping_logs_partition(2026, 6);   -- Junio 2026
SELECT create_scraping_logs_partition(2026, 7);   -- Julio 2026
```

> **Consejo:** Añade esta llamada a la tarea Celery `cleanup_old_logs` existente para que la creación de particiones ocurra automáticamente cada mes.

### Configuración Recomendada de PostgreSQL

Para despliegue local en Windows 11, añadir a `postgresql.conf`:

```ini
max_connections = 50          # Suficiente para FastAPI + pgAdmin
shared_buffers = 256MB        # 25% de la RAM disponible (para sistema de 4 GB)
work_mem = 16MB               # Memoria de ordenación/hash por consulta
maintenance_work_mem = 128MB  # VACUUM, CREATE INDEX
log_min_duration_statement = 1000  # Registrar consultas más lentas que 1s
```

---

## 6. Iniciar y Detener la Aplicación

### Modo A — Solo FastAPI (Recomendado para Windows 11)

El despachador asyncio integrado corre dentro del proceso FastAPI. **No se requiere Celery.**

```bat
:: Iniciar
inicio_rapido.bat

:: O manualmente:
cd C:\BookingScraper
venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000

:: Detener: Ctrl+C en la ventana de consola
```

### Modo B — Stack Completo (FastAPI + Celery + Beat)

Solo necesario cuando `USE_CELERY_DISPATCHER=True` y Memurai/Redis está en ejecución.

```bat
:: Iniciar todos los servicios (abre 3 ventanas de consola)
start_services.bat

:: Detener todos los servicios
stop_services.bat
```

### Verificar el Estado de la Aplicación

```
http://localhost:8000/health           ← Estado de BD + Redis + VPN + disco
http://localhost:8000/scraping/status  ← Trabajos activos, conteos de cola
http://localhost:8000/metrics          ← CPU, memoria, estadísticas de pool
http://localhost:8000/docs             ← Documentación interactiva de la API
```

---

## 7. Referencia de Endpoints API

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/health` | Estado del sistema (BD, Redis, VPN, disco) |
| `GET` | `/scraping/status` | Trabajos activos, conteos de cola, estado VPN |
| `GET` | `/metrics` | CPU, memoria, pool BD, estadísticas de logs |
| `GET` | `/hotels` | Listar hoteles extraídos (paginado) |
| `GET` | `/hotels/{id}` | Detalle de un hotel |
| `POST` | `/urls` | Añadir URLs a la cola de scraping |
| `POST` | `/scraping/force-now` | Despacho inmediato (requiere API_KEY) |
| `GET` | `/vpn/status` | Estado de la conexión VPN |
| `POST` | `/vpn/rotate` | Rotación manual VPN (requiere API_KEY) |
| `GET` | `/export` | Exportar datos (CSV/JSON/Excel) |

---

## 8. Modificaciones Realizadas (v30 → v33)

Esta sección documenta cada corrección aplicada en todos los ciclos de auditoría.

### v33 — Este Ciclo (8 correcciones)

#### FIX-018 — Backoff Exponencial en Reintentos de Celery
**Archivo:** `app/tasks.py`  
**Problema:** `self.retry(exc=exc)` usaba un retardo constante de 60 segundos. Después de un reinicio de base de datos, todas las tareas en espera de reintento disparaban simultáneamente (thundering herd), potencialmente abrumando el servicio recién recuperado.  
**Corrección:** Fórmula de backoff exponencial `min(base × 2ⁿ, 3600)` donde `n = self.request.retries`. La base es 60s para `process_pending_urls` y 300s para `cleanup_old_logs`.

```python
# Antes
raise self.retry(exc=exc)

# Después
_backoff = min(60 * (2 ** self.request.retries), 3600)
raise self.retry(exc=exc, countdown=_backoff)
```

---

#### FIX-019 — Apagado Graceful del ThreadPoolExecutor
**Archivo:** `app/main.py`  
**Problema:** `_executor.shutdown(wait=False, cancel_futures=True)` en el cierre del lifespan cancelaba abruptamente los threads de scraping en vuelo. Los threads con transacciones DB abiertas dejaban `url_queue.status='processing'` bloqueado hasta el próximo reinicio.  
**Corrección:** Apagado en dos fases: (1) intento de finalización graceful con timeout de 30 segundos (`EXECUTOR_SHUTDOWN_TIMEOUT_SECS`), (2) cancelación forzada solo si expira el timeout, con advertencia explicativa en el log.

---

#### FIX-020 — Carrera TOCTOU en verify_vpn_active()
**Archivo:** `app/vpn_manager_windows.py`  
**Problema:** `self.original_ip` se leía sin mantener `_ip_cache_lock`. Una llamada concurrente a `_detect_original_ip()` durante la rotación podía sobreescribirla entre el check de nulo y la comparación, produciendo un falso positivo "VPN activa".  
**Corrección:** `original_ip` se captura ahora en una variable local bajo `_ip_cache_lock` al inicio de `verify_vpn_active()`. Todas las comparaciones posteriores usan la copia local.

---

#### FIX-021 — Techo de Retención de Archivos de Log
**Archivo:** `app/main.py`  
**Problema:** `retention="7 days"` con `rotation="50 MB"` podía acumular 168+ archivos de rotación (8,4 GB) durante scraping de alto volumen.  
**Corrección:** Cambiado a `retention=10` (conservar últimos 10 archivos rotados). Con `compression="gz"`, el uso máximo de disco para logs es ≤500 MB raw, ~50 MB comprimido.

---

#### FIX-022 — Ventanas de Consola Parpadeando en Llamadas CLI VPN
**Archivo:** `app/vpn_manager_windows.py`  
**Problema:** Cada llamada `subprocess.run()` al CLI de NordVPN creaba una ventana de consola visible en Windows, causando parpadeos disruptivos durante el scraping en background.  
**Corrección:** Añadido `_CREATE_NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)` y aplicado `creationflags=_CREATE_NO_WINDOW` a las 5 llamadas subprocess. En plataformas no-Windows, el flag evalúa a 0 (no-op).

---

#### FIX-023 — Advertencia de Modo Degradado Redis en Startup
**Archivo:** `app/scraper_service.py`  
**Problema:** Cuando Redis era inalcanzable, el sistema caía silenciosamente en fallback local de `_active_ids` sin indicación visible de que funcionaba en modo degradado.  
**Corrección:** Añadido `logger.warning()` explícito en el startup del módulo cuando `_redis_client is None`, explicando el impacto operacional y proporcionando pasos de remediación.

---

#### FIX-024 — Clasificación de Errores: Transitorios vs Fatales
**Archivo:** `app/scraper_service.py`  
**Problema:** Todas las excepciones de scraping se registraban al mismo nivel de severidad y se trataban con la misma lógica de reintento. Los errores de red transitorios aparecían como `ERROR` (fatiga de alertas), y los errores de programación fatales (ValueError) se reintentaban inútilmente.  
**Corrección:** Añadidos los helpers `_is_transient_error(exc)` y `_log_scrape_error()`. Los errores transitorios (ConnectionError, TimeoutError, palabras clave de red) se registran como `WARNING`. Los errores fatales (ValueError, TypeError, AttributeError) se registran como `ERROR` con traceback completo.

---

#### FIX-025 — Particionamiento Mensual de scraping_logs
**Archivo:** `app/install_clean_v31.sql`  
**Problema:** `scraping_logs` era una tabla sin particiones. Al volumen esperado (50K filas/día), alcanza 18M filas en un año. Las consultas filtradas por timestamp requerían escaneo completo de la tabla O(18M).  
**Corrección:** Convertida a `PARTITION BY RANGE (timestamp)` con granularidad mensual. El partition pruning de PostgreSQL reduce el escaneo a ≤2 particiones por consulta. `SERIAL PRIMARY KEY` reemplazado por `BIGSERIAL` + `PRIMARY KEY (id, timestamp)` compuesta (requerido por las reglas de particionamiento). Función PL/pgSQL `create_scraping_logs_partition(year, month)` gestiona la creación de particiones. Tres particiones pre-creadas en el momento de la instalación.

---

### v32 (3 correcciones)

| Corrección | Descripción |
|---|---|
| FIX-015 | Eliminadas las credenciales hardcodeadas de `alembic.ini` — reemplazadas por override en tiempo de ejecución vía `alembic/env.py` leyendo desde `.env` |
| FIX-016 | Reemplazadas 34 llamadas `print()` en `vpn_manager_windows.py` por `logger.info/warning/error()` — enruta toda la salida a través del pipeline de rotación de Loguru |
| FIX-017 | Re-sincronización de `_active_ids` desde Redis cuando el circuit breaker se recupera de OPEN → CLOSED — previene riesgo de doble reclamación tras corte de Redis |

---

### v31 (16 correcciones)

| Corrección | Descripción |
|---|---|
| BUG-001 | Añadido `vpn_manager.py` faltante (módulo factory) — causaba `ImportError` en startup |
| BUG-002 | Keepalive de Windows con `SetThreadExecutionState` + corutina watchdog — previene suspensión por pantalla bloqueada |
| BUG-003 | Añadida `build_language_url()` a `scraper.py` — causaba `NameError` que crasheaba todo el scraping |
| BUG-004 | Despacho atómico CTE con `FOR UPDATE SKIP LOCKED` — elimina carrera TOCTOU en selección de URLs |
| BUG-005 | Límite máximo del pool de conexiones: `_POOL_SAFE_MAX=50`, `_TOTAL_HARD_CAP=100` |
| BUG-006 | `SCRAPER_MAX_WORKERS` desde `.env` (configurable) |
| BUG-007 | Manejadores de señales Windows: SIGINT + SIGBREAK registrados con guarda de plataforma |
| BUG-008 | Circuit breaker de Redis (3 estados: CLOSED/OPEN/HALF-OPEN) con cooldown de 60s |
| BUG-009 | Índice GIN `ix_hotels_images_gin` en columna JSONB `images_urls` |
| BUG-010 | Los reintentos por idioma incorrecto ahora activan la rotación VPN |
| BUG-011 | Timeout de failover VPN con fallback de modo degradado |
| BUG-012 | Estadísticas de rotación VPN expuestas en la API `/scraping/status` |
| BUG-013 | Validación de `DB_PASSWORD` en startup — rechaza inicio si está vacío |
| BUG-014 | Rutas resueltas relativas a la ubicación de `config.py`, no al CWD |
| BUG-015 | Purga automática de HTML de depuración cada 120 ciclos de despacho |
| BUG-016 | Límites de tiempo Celery: `soft=150s`, `hard=180s` (reducido desde 600s) |

---

### v30 (ciclos previos)

| Corrección | Descripción |
|---|---|
| DATA-001 | Índice único parcial para `(url, language)` cuando `url_id IS NULL` |
| HIGH-003 | Índice B-Tree en `hotels.url` |
| HIGH-006 | `/health` devuelve HTTP 503 ante fallo de BD (antes siempre 200) |
| HIGH-007 | TTL de caché IP VPN = 5 segundos (era 300s — causaba comparaciones con IP obsoleta) |
| HIGH-008 | Verificación de integridad de imágenes con `Pillow.Image.verify()` |
| HIGH-010 | `MAX_URL_LENGTH=512` alineado con columna BD `VARCHAR(512)` |
| SEC-002 | CORS wildcard rechazado en startup cuando `allow_credentials=True` |
| SEC-003 | Las respuestas de error devuelven solo ID de correlación, nunca stack traces |
| CONC-001 | Idiomas ordenados alfabéticamente para prevenir deadlock |
| CONC-002 | `_vpn_lock.acquire(timeout=30)` — previene bloqueo indefinido |
| MED-011 | Reintento de conexión BD con backoff exponencial |
| MED-022 | Endpoint JSON `/metrics` (CPU, memoria, pool, disco) |
| Recovery-002 | `rollback()` + `finally: db.close()` en todos los caminos de error de BD |
| ARCH-001 | `_active_ids` respaldado por Redis con fallback a set local |
| ARCH-002 | Health check valida BD + Redis + VPN + disco |
| CFG-001 | `DB_PASSWORD` cadena vacía rechazada en startup |

---

## 9. Visión General de la Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                   Proceso Windows 11                     │
│                                                         │
│  ┌──────────────┐    ┌───────────────────────────────┐  │
│  │   FastAPI    │    │   Despachador asyncio auto    │  │
│  │  (uvicorn)   │    │   (cada 30 segundos)          │  │
│  │              │    │   process_batch(batch_size=5) │  │
│  │  API REST    │    └───────────────┬───────────────┘  │
│  │  /health     │                   │                   │
│  │  /hotels     │    ┌──────────────▼──────────────┐   │
│  │  /urls       │    │     scraper_service.py       │   │
│  │  /metrics    │    │  ┌─────────────────────────┐ │   │
│  └──────────────┘    │  │  ThreadPoolExecutor     │ │   │
│                       │  │  max_workers=1          │ │   │
│                       │  │  (Windows: secuencial)  │ │   │
│                       │  └──────────┬──────────────┘ │   │
│                       │             │                 │   │
│                       │  ┌──────────▼──────────────┐ │   │
│                       │  │     BookingScraper       │ │   │
│                       │  │  (Selenium O             │ │   │
│                       │  │   CloudScraper)          │ │   │
│                       │  └─────────────────────────┘ │   │
│                       └──────────────────────────────┘   │
│                                                         │
│  ┌───────────────┐    ┌───────────────┐                  │
│  │  PostgreSQL   │    │  Redis/       │                  │
│  │  (local)      │    │  Memurai      │                  │
│  │               │    │  (opcional)   │                  │
│  │  url_queue    │    │  _active_ids  │                  │
│  │  hotels       │    │  rate limits  │                  │
│  │  scraping_logs│    └───────────────┘                  │
│  └───────────────┘                                       │
└─────────────────────────────────────────────────────────┘
```

**Decisiones de Diseño Clave para Windows 11:**

- `SCRAPER_MAX_WORKERS=1`: La cuenta de NordVPN permite una sola conexión activa; el scraping serializado evita condiciones de carrera en la VPN
- `Celery solo pool`: `multiprocessing` de Python en Windows requiere modo `spawn` (sin `fork`); el solo pool evita todos los problemas relacionados
- `Despachador asyncio`: Integrado en el proceso FastAPI — no se necesita un worker Celery separado para operación estándar
- `Redis opcional`: El sistema funciona completamente sin Redis; Redis añade seguimiento distribuido de reclamaciones y rate limiting para posibles configuraciones multi-proceso futuras

---

## 10. Resolución de Problemas

### La aplicación no inicia

**Síntoma:** `ValueError: DB_PASSWORD is required`  
**Solución:** Establecer `DB_PASSWORD=tu_contraseña` en `.env`

**Síntoma:** `ImportError: No module named 'app.vpn_manager'`  
**Solución:** Verificar que `app/vpn_manager.py` existe en el repositorio. Ejecutar `git pull` para sincronizar el último código.

**Síntoma:** `ModuleNotFoundError` para cualquier paquete  
**Solución:** Activar venv y reinstalar: `venv\Scripts\python.exe -m pip install -r app\requirements.txt`

---

### Errores de base de datos

**Síntoma:** `connection pool exhausted`  
**Solución:** Reducir `DB_POOL_SIZE` y `DB_MAX_OVERFLOW` en `.env`, o incrementar `max_connections` en PostgreSQL

**Síntoma:** `relation "scraping_logs" does not exist`  
**Solución:** Ejecutar `install_clean_v31.sql` en la base de datos

**Síntoma:** `no partition of relation "scraping_logs" found for row`  
**Solución:** Crear la partición faltante: `SELECT create_scraping_logs_partition(AÑO, MES);`

---

### Problemas de scraping

**Síntoma:** Todas las URLs atascadas en estado `processing`  
**Solución 1:** Reiniciar la aplicación (el reset de startup mueve `processing` → `pending` incrementando el contador de reintentos)  
**Solución 2:** Reset manual: `UPDATE url_queue SET status='pending', retry_count=0 WHERE status='processing';`

**Síntoma:** URLs llegando a estado `failed` inmediatamente  
**Solución:** Revisar la columna `last_error`: `SELECT url, last_error FROM url_queue WHERE status='failed' LIMIT 10;`

**Síntoma:** El navegador Selenium no abre  
**Solución:** Establecer `BROWSER_BRAVE_PATH=C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe` en `.env`

---

### Problemas de VPN

**Síntoma:** Ventanas de consola parpadeando durante operaciones VPN  
**Estado:** Corregido en v33 (FIX-022) — flag `CREATE_NO_WINDOW` aplicado a todas las llamadas subprocess

**Síntoma:** La rotación VPN no parece cambiar la IP  
**Solución 1:** Verificar que la lista `VPN_COUNTRIES` tiene al menos 2 países  
**Solución 2:** Consultar caché de IP VPN: `GET /vpn/status`  
**Solución 3:** Rotación manual: `POST /vpn/rotate` (requiere cabecera API_KEY)

---

### Gestión de logs

**Síntoma:** `data/logs/` consumiendo demasiado espacio en disco  
**Estado:** Corregido en v33 (FIX-021) — `retention=10` limita los archivos de log a 10 × 50 MB = 500 MB máximo  
**Limpieza manual:** Eliminar archivos en `data/logs/` más antiguos del periodo de retención deseado

---

*Reporte generado: 2026-03-05 | Ciclo: v33 | Plataforma: Windows 11 (local) | Instalación limpia*
