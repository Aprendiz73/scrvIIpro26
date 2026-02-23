============================================================
  BookingScraper Pro v2.0 - INSTRUCCIONES DE USO
============================================================

PROBLEMA RESUELTO: El scraping no ejecutaba porque dependía
de Celery worker externo. Ahora corre DENTRO de FastAPI
de forma automática sin necesitar ningún proceso adicional.

============================================================
  PASO 1: MIGRACIÓN DE BASE DE DATOS (OBLIGATORIO)
============================================================

Antes de arrancar la app por primera vez con v2.0,
ejecuta el script SQL de migración en pgAdmin:

  1. Abre pgAdmin 4
  2. Selecciona la base de datos "booking_scraper"
  3. Clic en "Query Tool" (icono de lápiz)
  4. Abre el archivo: migracion_bd_v2.sql
  5. Haz clic en "Execute" (F5)
  6. Verifica que en "Messages" aparezcan líneas con "AÑADIDA" o "ya existe"
     (no debe haber errores rojos)

  IMPORTANTE: Este paso añade columnas faltantes a las tablas
  existentes. Si no lo ejecutas, el scraping fallará.

============================================================
  PASO 2: ARRANCAR LA APLICACIÓN
============================================================

Opción A - Usando el script (RECOMENDADO):
  Doble clic en: inicio_rapido.bat

Opción B - Manual desde consola:
  cd C:\BookingScraper
  venv\Scripts\activate
  python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

  NO necesitas arrancar Celery. El scraping es automático.

============================================================
  PASO 3: VERIFICAR QUE FUNCIONA
============================================================

Cuando arranque, verás en la consola:
  ============================================================
    BookingScraper Pro v2.0 - Iniciando
  ============================================================
    Base de datos  : ✓ OK
    Auto-scraper   : ✓ ACTIVO (cada 30s)
  ============================================================
  🤖 Auto-dispatcher iniciado (ciclo 30s) — no requiere Celery

Abre en el navegador:
  http://localhost:8000/scraping/status
  → Muestra en tiempo real qué URLs se están procesando

  http://localhost:8000/docs
  → Documentación interactiva de todos los endpoints

============================================================
  PASO 4: CÓMO FUNCIONA AHORA
============================================================

1. Cargas URLs con POST /urls/upload  (ya funciona ✓)

2. El auto-dispatcher revisa cada 30 segundos si hay
   URLs con status='pending' y las procesa automáticamente.
   NO tienes que hacer nada más.

3. También puedes forzar el inicio inmediato con:
   POST /scraping/start  (modo directo, sin Celery)
   POST /scraping/force-now  (ejecuta y espera el resultado)

4. Para ver progreso:
   GET /scraping/status  ← NUEVO endpoint, muy útil
   GET /stats
   GET /scraping/logs

5. Cuando termina, los datos están en:
   GET /hotels
   GET /export/csv
   GET /export/json

============================================================
  ENDPOINTS NUEVOS EN v2.0
============================================================

  POST /scraping/force-now    Despacho inmediato y síncrono
  GET  /scraping/status       Estado en tiempo real del scraper
  POST /urls/reset-processing Resetea URLs atascadas en 'processing'

============================================================
  ESTRUCTURA DE ARCHIVOS
============================================================

  C:\BookingScraper\
  ├── app\
  │   ├── main.py              ← Servidor FastAPI + Auto-dispatcher
  │   ├── scraper_service.py   ← NUEVO: servicio de scraping directo
  │   ├── scraper.py           ← Scraper httpx/Selenium
  │   ├── extractor.py         ← Parser HTML Booking.com
  │   ├── models.py            ← Modelos SQLAlchemy
  │   ├── database.py          ← Conexión PostgreSQL
  │   ├── config.py            ← Configuración (.env)
  │   ├── tasks.py             ← Tareas Celery (opcionales)
  │   └── image_downloader.py  ← Descarga de imágenes
  ├── migracion_bd_v2.sql      ← Ejecutar una vez en pgAdmin
  ├── inicio_rapido.bat        ← Script de arranque
  └── limpiar_cache.bat        ← Limpieza de __pycache__

============================================================
  CONFIGURACIÓN (.env)
============================================================

Edita C:\BookingScraper\.env para ajustar:

  DB_HOST=localhost
  DB_PORT=5432
  DB_USER=postgres
  DB_PASSWORD=2221
  DB_NAME=booking_scraper

  LANGUAGES_ENABLED=en,es,de,fr,it
  BATCH_SIZE=5
  MAX_CONCURRENT_TASKS=3
  USE_SELENIUM=False
  VPN_ENABLED=False
  DOWNLOAD_IMAGES=True

============================================================
  SOLUCIÓN DE PROBLEMAS
============================================================

Problema: "scraped_at column does not exist"
Solución: Ejecuta migracion_bd_v2.sql en pgAdmin

Problema: El scraping no avanza después de varios minutos
Solución: GET /scraping/status para ver qué está pasando
          POST /urls/reset-processing para liberar URLs atascadas

Problema: HTTP 403 de Booking.com
Solución: Booking.com detectó el scraping. Espera 10-15 minutos
          y ajusta MIN_REQUEST_DELAY=3.0, MAX_REQUEST_DELAY=7.0 en .env

Problema: Quiero más velocidad
Solución: Aumenta MAX_CONCURRENT_TASKS=5 en .env
          (no subir demasiado o Booking.com bloqueará)

============================================================
