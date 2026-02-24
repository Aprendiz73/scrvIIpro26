C:\BookingScraper>inicio_rapido.bat

============================================================
  BookingScraper Pro v2.0 - Inicio Rapido
  MODO SIMPLIFICADO: Solo uvicorn (sin Celery necesario)
  El scraping corre automaticamente dentro de FastAPI
============================================================

[1/3] Limpiando cache Python...
  OK - cache limpia

[2/3] Verificando entorno virtual...
  OK

[3/3] Arrancando FastAPI + Auto-Scraper integrado...

============================================================
  NO necesitas Celery ni ningun otro proceso.

  API:     http://localhost:8000
  Docs:    http://localhost:8000/docs
  Status:  http://localhost:8000/scraping/status
  Salud:   http://localhost:8000/health

  El scraping inicia automaticamente 5s despues de arrancar.
  Ver progreso en esta consola.

  Para parar: Ctrl+C
============================================================

[32mINFO[0m:     Will watch for changes in these directories: ['C:\\BookingScraper']
[32mINFO[0m:     Uvicorn running on [1mhttp://0.0.0.0:8000[0m (Press CTRL+C to quit)
[32mINFO[0m:     Started reloader process [[36m[1m18332[0m] using [36m[1mWatchFiles[0m
INFO:     Started server process [26564]
INFO:     Waiting for application startup.

============================================================
  BookingScraper Pro v2.1 - Iniciando
============================================================
2026-02-24 00:55:27.957 | SUCCESS  | app.database:test_connection:81 - ✓ Conexión a PostgreSQL exitosa
  Base de datos  : ✓ OK
  Idiomas        : en, es, de, fr, it
  Batch size     : 10
  Selenium       : ✓ ACTIVO
  VPN            : ✓ ACTIVO
  Auto-scraper   : ✓ ACTIVO (cada 30s)
  Docs           : http://localhost:8000/docs
  VPN status     : http://localhost:8000/vpn/status
  Scraping status: http://localhost:8000/scraping/status
============================================================

2026-02-24 00:55:27.964 | INFO     | app.main:_auto_dispatch_loop:61 - 🤖 Auto-dispatcher iniciado (ciclo 30s) — no requiere Celery
2026-02-24 00:55:29.354 | INFO     | app.vpn_manager_windows:_detect_method:113 - ✓ NordVPN CLI detectado
2026-02-24 00:55:29.871 | INFO     | app.vpn_manager_windows:_detect_original_ip:150 - IP original: 185.195.59.185
2026-02-24 00:55:29.871 | INFO     | app.vpn_manager_windows:__init__:91 - VPN Manager Windows inicializado | método=cli | interactive=False | sistema=10.0.26200
2026-02-24 00:55:29.872 | INFO     | app.scraper_service:_get_vpn_manager:107 - ✓ VPN Manager iniciado (singleton)
2026-02-24 00:55:29.873 | INFO     | app.main:_init_vpn:118 - 🔐 VPN iniciada al arrancar
INFO:     Application startup complete.
2026-02-24 00:55:32.977 | WARNING  | app.vpn_manager_windows:verify_vpn_active:462 - ⚠️ VPN inactiva | IP=185.195.59.185 == original=185.195.59.185
2026-02-24 00:55:32.978 | WARNING  | app.scraper_service:process_batch:212 - ⚠️ VPN inactiva al procesar batch — intentando conectar...
2026-02-24 00:55:32.979 | INFO     | app.vpn_manager_windows:connect:171 - Conectando a Netherlands (NL)...
2026-02-24 00:55:37.029 | INFO     | app.vpn_manager_windows:_connect_via_cli:207 - Conectando CLI a Netherlands...
INFO:     127.0.0.1:57114 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:57114 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:57114 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:57114 - "GET /openapi.json HTTP/1.1" 200 OK
2026-02-24 00:55:48.911 | ERROR    | app.vpn_manager_windows:_connect_via_cli:234 - ✗ VPN CLI conectó pero IP no cambió
2026-02-24 00:55:48.914 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
INFO:     127.0.0.1:59136 - "POST /urls/load HTTP/1.1" 200 OK
2026-02-24 00:56:19.316 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 00:56:19.335 | INFO     | app.scraper_service:process_batch:264 - 🚀 Despachadas 10 URLs al thread pool
2026-02-24 00:56:19.336 | INFO     | app.main:_auto_dispatch_loop:74 - 🤖 Auto-dispatch: 10 URLs enviadas al thread pool
2026-02-24 00:56:19.336 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 00:56:19.336 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=225 | https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.html
2026-02-24 00:56:19.337 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 00:56:19.337 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 00:56:19.349 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 00:56:21.526 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 00:56:21.528 | INFO     | app.scraper_service:scrape_one:367 -   → [225] Idioma [en]: https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.html
2026-02-24 00:56:21.529 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.html (intento 1)
2026-02-24 00:56:49.723 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 00:56:49.805 | INFO     | app.scraper_service:process_batch:264 - 🚀 Despachadas 6 URLs al thread pool
2026-02-24 00:56:49.806 | INFO     | app.main:_auto_dispatch_loop:74 - 🤖 Auto-dispatch: 6 URLs enviadas al thread pool
2026-02-24 00:56:58.422 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 00:57:20.130 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 00:57:20.132 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 00:57:50.450 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 00:57:50.452 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 00:57:52.043 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Gardens Hill Resort & Spa, Beau Vallon (precios actualizados en 2026)' | 1,796,024 bytes
2026-02-24 00:57:52.414 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 00:57:52.600 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 00:57:52.600 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 00:57:52.601 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 00:57:52.601 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | 1,796,024b
2026-02-24 00:57:52.625 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [225][en] 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | imgs=8
2026-02-24 00:57:52.713 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [225] 12 cookies extraídas del browser
2026-02-24 00:57:52.714 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 00:57:52.715 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=225 lang=en
2026-02-24 00:57:53.396 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_106b1d98e88c.jpg (118,426 bytes, 1280×855)
2026-02-24 00:57:53.408 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_4384e2acb219.jpg (220,396 bytes, 1280×855)
2026-02-24 00:57:53.422 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_3b5e6cb74323.jpg (152,428 bytes, 1280×842)
2026-02-24 00:57:53.496 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_ef344d260f9f.jpg (175,879 bytes, 1280×855)
2026-02-24 00:57:53.519 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_4063ccc3381e.jpg (239,518 bytes, 1201×900)
2026-02-24 00:57:53.732 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_ecc467d87209.jpg (188,501 bytes, 1280×853)
2026-02-24 00:57:53.738 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_bebd502e1a3c.jpg (143,413 bytes, 1280×855)
2026-02-24 00:57:53.813 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_a90a53522b61.jpg (154,110 bytes, 1280×855)
2026-02-24 00:57:53.815 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 00:57:53.815 | INFO     | app.scraper_service:_download_images:671 -   📷 [225] 8/8 imágenes descargadas
2026-02-24 00:57:53.816 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [225] Imagenes marcadas como descargadas
2026-02-24 00:57:53.816 | INFO     | app.scraper_service:scrape_one:367 -   → [225] Idioma [es]: https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.es.html
2026-02-24 00:57:53.816 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.es.html (intento 1)
2026-02-24 00:58:20.774 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 00:58:20.776 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 00:58:32.437 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 00:58:51.109 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 00:58:51.111 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 00:59:21.457 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 00:59:21.459 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 00:59:26.026 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Gardens Hill Resort & Spa, Beau Vallon (precios actualizados en 2026)' | 1,786,848 bytes
2026-02-24 00:59:26.176 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 00:59:26.351 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 00:59:26.351 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-24 00:59:26.352 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 00:59:26.352 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | 1,786,848b
2026-02-24 00:59:26.376 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [225][es] 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | imgs=8
2026-02-24 00:59:26.376 | INFO     | app.scraper_service:scrape_one:367 -   → [225] Idioma [de]: https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.de.html
2026-02-24 00:59:26.376 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.de.html (intento 1)
2026-02-24 00:59:51.782 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 00:59:51.784 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:00:03.332 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:00:22.102 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:00:22.105 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:00:52.416 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:00:52.418 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:00:56.975 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Gardens Hill Resort & Spa, Beau Vallon (precios actualizados en 2026)' | 1,794,005 bytes
2026-02-24 01:00:57.117 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:00:57.311 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 01:00:57.311 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 01:00:57.313 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 01:00:57.313 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | 1,794,005b
2026-02-24 01:00:57.348 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [225][de] 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | imgs=8
2026-02-24 01:00:57.348 | INFO     | app.scraper_service:scrape_one:367 -   → [225] Idioma [fr]: https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.fr.html
2026-02-24 01:00:57.349 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.fr.html (intento 1)
2026-02-24 01:01:22.807 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:01:22.809 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:01:36.587 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:01:53.200 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:01:53.202 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:02:23.525 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:02:23.527 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:02:30.191 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Gardens Hill Resort & Spa, Beau Vallon (precios actualizados en 2026)' | 1,793,918 bytes
2026-02-24 01:02:30.352 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:02:30.542 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 01:02:30.542 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 01:02:30.544 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 01:02:30.544 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | 1,793,918b
2026-02-24 01:02:30.565 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [225][fr] 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | imgs=8
2026-02-24 01:02:30.565 | INFO     | app.scraper_service:scrape_one:367 -   → [225] Idioma [it]: https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.it.html
2026-02-24 01:02:30.565 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.it.html (intento 1)
2026-02-24 01:02:53.849 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:02:53.851 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:03:07.028 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:03:24.171 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:03:24.173 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:03:54.495 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:03:54.497 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:04:00.648 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Gardens Hill Resort & Spa, Beau Vallon (precios actualizados en 2026)' | 1,793,992 bytes
2026-02-24 01:04:00.793 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:04:00.993 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 01:04:00.994 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 01:04:00.995 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 01:04:00.995 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | 1,793,992b
2026-02-24 01:04:01.016 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [225][it] 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | imgs=8
2026-02-24 01:04:03.398 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 225
2026-02-24 01:04:03.412 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [225] COMPLETADO | 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | 5/5 idiomas | 464.1s
2026-02-24 01:04:03.414 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 01:04:03.419 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=226 | https://www.booking.com/hotel/sc/cb-seychelles.html
2026-02-24 01:04:03.419 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 01:04:03.419 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:04:03.420 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 01:04:05.190 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 01:04:05.191 | INFO     | app.scraper_service:scrape_one:367 -   → [226] Idioma [en]: https://www.booking.com/hotel/sc/cb-seychelles.html
2026-02-24 01:04:05.192 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/cb-seychelles.html (intento 1)
2026-02-24 01:04:24.834 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:04:24.836 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:04:42.113 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:04:55.157 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:04:55.158 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:05:25.644 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:05:25.646 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:05:35.628 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cheval Blanc Seychelles, Mahé (precios actualizados en 2026)' | 1,933,970 bytes
2026-02-24 01:05:35.768 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:05:35.976 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 01:05:35.976 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 01:05:35.978 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 01:05:35.978 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | 1,933,970b
2026-02-24 01:05:36.009 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [226][en] 'Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | imgs=8
2026-02-24 01:05:36.020 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [226] 12 cookies extraídas del browser
2026-02-24 01:05:36.022 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 01:05:36.023 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=226 lang=en
2026-02-24 01:05:36.650 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_ef75b341d853.jpg (89,252 bytes, 1280×853)
2026-02-24 01:05:36.653 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_6fc33e853a69.jpg (133,966 bytes, 1280×852)
2026-02-24 01:05:36.674 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_c3efbc9c5587.jpg (121,576 bytes, 1280×719)
2026-02-24 01:05:36.678 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_d6e4c11bef3a.jpg (170,252 bytes, 1280×853)
2026-02-24 01:05:36.712 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_ba387a1a0b85.jpg (212,676 bytes, 1280×853)
2026-02-24 01:05:37.072 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_cb580cedf981.jpg (302,261 bytes, 1280×853)
2026-02-24 01:05:37.112 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_ae740d8fd385.jpg (201,790 bytes, 1280×853)
2026-02-24 01:05:37.128 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_a1636e9be478.jpg (317,873 bytes, 1200×900)
2026-02-24 01:05:37.130 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 01:05:37.137 | INFO     | app.scraper_service:_download_images:671 -   📷 [226] 8/8 imágenes descargadas
2026-02-24 01:05:37.138 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [226] Imagenes marcadas como descargadas
2026-02-24 01:05:37.139 | INFO     | app.scraper_service:scrape_one:367 -   → [226] Idioma [es]: https://www.booking.com/hotel/sc/cb-seychelles.es.html
2026-02-24 01:05:37.139 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/cb-seychelles.es.html (intento 1)
2026-02-24 01:05:55.974 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:05:55.976 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:06:16.621 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:06:26.356 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:06:26.358 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:06:56.740 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:06:56.743 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:07:10.151 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cheval Blanc Seychelles, Mahé (precios actualizados en 2026)' | 1,938,795 bytes
2026-02-24 01:07:10.298 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:07:10.488 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 01:07:10.489 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rating_category', 'rooms']
2026-02-24 01:07:10.490 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 01:07:10.491 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | 1,938,795b
2026-02-24 01:07:10.511 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [226][es] 'Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | imgs=8
2026-02-24 01:07:10.511 | INFO     | app.scraper_service:scrape_one:367 -   → [226] Idioma [de]: https://www.booking.com/hotel/sc/cb-seychelles.de.html
2026-02-24 01:07:10.512 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/cb-seychelles.de.html (intento 1)
2026-02-24 01:07:27.081 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:07:27.082 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:07:49.814 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:07:57.403 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:07:57.405 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:08:27.721 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:08:27.723 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:08:43.421 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cheval Blanc Seychelles, Mahé (precios actualizados en 2026)' | 1,938,808 bytes
2026-02-24 01:08:43.594 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:08:43.803 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 01:08:43.804 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 01:08:43.805 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 01:08:43.805 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | 1,938,808b
2026-02-24 01:08:43.825 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [226][de] 'Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | imgs=8
2026-02-24 01:08:43.826 | INFO     | app.scraper_service:scrape_one:367 -   → [226] Idioma [fr]: https://www.booking.com/hotel/sc/cb-seychelles.fr.html
2026-02-24 01:08:43.826 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/cb-seychelles.fr.html (intento 1)
2026-02-24 01:08:58.043 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:08:58.045 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:09:22.308 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:09:28.372 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:09:28.375 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:09:58.703 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:09:58.705 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:10:15.839 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cheval Blanc Seychelles, Mahé (precios actualizados en 2026)' | 1,938,806 bytes
2026-02-24 01:10:15.974 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:10:16.171 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 01:10:16.172 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 01:10:16.173 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 01:10:16.174 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | 1,938,806b
2026-02-24 01:10:16.196 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [226][fr] 'Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | imgs=8
2026-02-24 01:10:16.196 | INFO     | app.scraper_service:scrape_one:367 -   → [226] Idioma [it]: https://www.booking.com/hotel/sc/cb-seychelles.it.html
2026-02-24 01:10:16.197 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/cb-seychelles.it.html (intento 1)
2026-02-24 01:10:29.022 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:10:29.024 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:10:55.493 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:10:59.342 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:10:59.344 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:11:29.762 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:11:29.764 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:11:49.045 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cheval Blanc Seychelles, Mahé (precios actualizados en 2026)' | 1,937,786 bytes
2026-02-24 01:11:49.174 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:11:49.374 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 01:11:49.374 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 01:11:49.375 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 01:11:49.376 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | 1,937,786b
2026-02-24 01:11:49.395 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [226][it] 'Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | imgs=8
2026-02-24 01:11:51.770 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 226
2026-02-24 01:11:51.784 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [226] COMPLETADO | 'Cheval Blanc Seychelles, Mahé, Seychelles' | 5/5 idiomas | 468.4s
2026-02-24 01:11:51.786 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 01:11:51.788 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=227 | https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.html
2026-02-24 01:11:51.788 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 01:11:51.788 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:11:51.788 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 01:11:53.490 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 01:11:53.490 | INFO     | app.scraper_service:scrape_one:367 -   → [227] Idioma [en]: https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.html
2026-02-24 01:11:53.492 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.html (intento 1)
2026-02-24 01:12:00.149 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:12:00.151 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:12:30.501 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:12:30.503 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:12:31.298 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:13:00.825 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:13:00.827 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:13:24.844 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Avani+ Barbarons Seychelles, Grand'Anse (precios actualizados en 2026)' | 1,972,465 bytes
2026-02-24 01:13:25.029 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:13:25.271 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 01:13:25.271 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 01:13:25.272 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 01:13:25.272 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | 1,972,465b
2026-02-24 01:13:25.292 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [227][en] 'Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | imgs=8
2026-02-24 01:13:25.301 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [227] 12 cookies extraídas del browser
2026-02-24 01:13:25.302 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 01:13:25.303 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=227 lang=en
2026-02-24 01:13:25.856 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_71259672c207.jpg (90,596 bytes, 1280×691)
2026-02-24 01:13:25.912 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_d41aa39ab96e.jpg (93,372 bytes, 1280×691)
2026-02-24 01:13:25.929 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_5de2ff92435b.jpg (142,746 bytes, 1280×691)
2026-02-24 01:13:25.959 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_803bfa7c4f5f.jpg (212,121 bytes, 1280×691)
2026-02-24 01:13:25.967 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_fdd7b521fe15.jpg (186,574 bytes, 1280×691)
2026-02-24 01:13:26.153 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_6fa6c43c50c4.jpg (103,020 bytes, 1280×691)
2026-02-24 01:13:26.208 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_85e4c2c3a976.jpg (109,283 bytes, 1280×691)
2026-02-24 01:13:26.258 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_b8e4876cc695.jpg (163,424 bytes, 1280×691)
2026-02-24 01:13:26.354 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 01:13:26.354 | INFO     | app.scraper_service:_download_images:671 -   📷 [227] 8/8 imágenes descargadas
2026-02-24 01:13:26.355 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [227] Imagenes marcadas como descargadas
2026-02-24 01:13:26.355 | INFO     | app.scraper_service:scrape_one:367 -   → [227] Idioma [es]: https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.es.html
2026-02-24 01:13:26.355 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.es.html (intento 1)
2026-02-24 01:13:31.148 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:13:31.150 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:14:01.459 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:14:01.461 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:14:04.458 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:14:31.789 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:14:31.791 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:14:58.031 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Avani+ Barbarons Seychelles, Grand'Anse (precios actualizados en 2026)' | 1,963,696 bytes
2026-02-24 01:14:58.256 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:14:58.630 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 01:14:58.631 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rating_category', 'rooms']
2026-02-24 01:14:58.632 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 01:14:58.633 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | 1,963,696b
2026-02-24 01:14:58.654 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [227][es] 'Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | imgs=8
2026-02-24 01:14:58.654 | INFO     | app.scraper_service:scrape_one:367 -   → [227] Idioma [de]: https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.de.html
2026-02-24 01:14:58.654 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.de.html (intento 1)
2026-02-24 01:15:02.108 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:15:02.111 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:15:32.431 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:15:32.433 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:15:37.314 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:16:02.758 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:16:02.759 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:16:30.859 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Avani+ Barbarons Seychelles, Grand'Anse (precios actualizados en 2026)' | 1,968,025 bytes
2026-02-24 01:16:31.026 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:16:31.263 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 01:16:31.263 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 01:16:31.264 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 01:16:31.265 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | 1,968,025b
2026-02-24 01:16:31.287 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [227][de] 'Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | imgs=8
2026-02-24 01:16:31.287 | INFO     | app.scraper_service:scrape_one:367 -   → [227] Idioma [fr]: https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.fr.html
2026-02-24 01:16:31.288 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.fr.html (intento 1)
2026-02-24 01:16:33.150 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:16:33.152 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:17:04.552 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:17:04.554 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:17:11.244 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:17:34.871 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:17:34.873 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:18:04.847 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Avani+ Barbarons Seychelles, Grand'Anse (precios actualizados en 2026)' | 1,970,375 bytes
2026-02-24 01:18:05.008 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:18:05.298 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 01:18:05.299 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 01:18:05.298 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:18:05.300 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 01:18:05.301 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | 1,970,375b
2026-02-24 01:18:05.305 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:18:05.320 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [227][fr] 'Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | imgs=8
2026-02-24 01:18:05.320 | INFO     | app.scraper_service:scrape_one:367 -   → [227] Idioma [it]: https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.it.html
2026-02-24 01:18:05.320 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.it.html (intento 1)
2026-02-24 01:18:36.045 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:18:36.047 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:18:43.556 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:19:06.440 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:19:06.442 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:19:36.775 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:19:36.777 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:19:37.105 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Avani+ Barbarons Seychelles, Grand'Anse (precios actualizados en 2026)' | 1,970,442 bytes
2026-02-24 01:19:37.281 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:19:37.513 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 01:19:37.513 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 01:19:37.515 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 01:19:37.515 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | 1,970,442b
2026-02-24 01:19:37.537 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [227][it] 'Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | imgs=8
2026-02-24 01:19:40.246 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 227
2026-02-24 01:19:40.259 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [227] COMPLETADO | 'Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | 5/5 idiomas | 468.5s
2026-02-24 01:19:40.261 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 01:19:40.261 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=228 | https://www.booking.com/hotel/bb/leroy.html
2026-02-24 01:19:40.261 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 01:19:40.261 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:19:40.264 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 01:19:41.752 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 01:19:41.752 | INFO     | app.scraper_service:scrape_one:367 -   → [228] Idioma [en]: https://www.booking.com/hotel/bb/leroy.html
2026-02-24 01:19:41.754 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/bb/leroy.html (intento 1)
2026-02-24 01:20:07.089 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:20:07.091 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:20:18.520 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:20:37.559 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:20:37.562 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:21:08.037 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:21:08.040 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:21:12.062 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Hôtel Le Roy, Christ Church (precios actualizados en 2026)' | 1,987,380 bytes
2026-02-24 01:21:12.208 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:21:12.397 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 01:21:12.398 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 01:21:12.399 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 01:21:12.399 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | 1,987,380b
2026-02-24 01:21:12.418 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [228][en] 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | imgs=8
2026-02-24 01:21:12.427 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [228] 12 cookies extraídas del browser
2026-02-24 01:21:12.428 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 01:21:12.429 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=228 lang=en
2026-02-24 01:21:12.761 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_100661c31d5e.jpg (24,693 bytes, 360×480)
2026-02-24 01:21:12.951 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_61b67ea50277.jpg (76,364 bytes, 675×900)
2026-02-24 01:21:13.040 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_7aa7698e850b.jpg (125,679 bytes, 1280×853)
2026-02-24 01:21:13.042 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_3f640e2e2f4a.jpg (63,586 bytes, 675×900)
2026-02-24 01:21:13.130 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_250c87976845.jpg (208,234 bytes, 1200×900)
2026-02-24 01:21:13.150 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_294355900c02.jpg (167,745 bytes, 1200×900)
2026-02-24 01:21:13.230 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_b71ac3954766.jpg (64,818 bytes, 600×800)
2026-02-24 01:21:13.332 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_8e87f8e913a8.jpg (176,490 bytes, 675×900)
2026-02-24 01:21:13.334 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 01:21:13.335 | INFO     | app.scraper_service:_download_images:671 -   📷 [228] 8/8 imágenes descargadas
2026-02-24 01:21:13.336 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [228] Imagenes marcadas como descargadas
2026-02-24 01:21:13.336 | INFO     | app.scraper_service:scrape_one:367 -   → [228] Idioma [es]: https://www.booking.com/hotel/bb/leroy.es.html
2026-02-24 01:21:13.336 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/bb/leroy.es.html (intento 1)
2026-02-24 01:21:38.427 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:21:38.429 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:21:50.950 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:22:08.838 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:22:08.840 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:22:39.313 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:22:39.315 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:22:44.493 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Hôtel Le Roy, Christ Church (precios actualizados en 2026)' | 1,979,224 bytes
2026-02-24 01:22:44.653 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:22:44.814 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 01:22:44.815 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-24 01:22:44.816 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 01:22:44.817 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | 1,979,224b
2026-02-24 01:22:44.836 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [228][es] 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | imgs=8
2026-02-24 01:22:44.836 | INFO     | app.scraper_service:scrape_one:367 -   → [228] Idioma [de]: https://www.booking.com/hotel/bb/leroy.de.html
2026-02-24 01:22:44.836 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/bb/leroy.de.html (intento 1)
2026-02-24 01:23:09.660 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:23:09.662 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:23:23.954 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:23:39.986 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:23:39.988 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:24:10.325 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:24:10.327 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:24:17.596 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Hôtel Le Roy, Christ Church (precios actualizados en 2026)' | 1,985,853 bytes
2026-02-24 01:24:17.735 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:24:17.919 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 01:24:17.920 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 01:24:17.922 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 01:24:17.922 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | 1,985,853b
2026-02-24 01:24:17.940 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [228][de] 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | imgs=8
2026-02-24 01:24:17.941 | INFO     | app.scraper_service:scrape_one:367 -   → [228] Idioma [fr]: https://www.booking.com/hotel/bb/leroy.fr.html
2026-02-24 01:24:17.941 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/bb/leroy.fr.html (intento 1)
2026-02-24 01:24:41.492 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:24:41.494 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:24:57.815 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:25:11.856 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:25:11.858 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:25:42.235 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:25:42.236 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:25:51.393 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Hôtel Le Roy, Christ Church (precios actualizados en 2026)' | 1,985,905 bytes
2026-02-24 01:25:51.538 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:25:51.718 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 01:25:51.718 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 01:25:51.719 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 01:25:51.720 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | 1,985,905b
2026-02-24 01:25:51.741 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [228][fr] 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | imgs=8
2026-02-24 01:25:51.741 | INFO     | app.scraper_service:scrape_one:367 -   → [228] Idioma [it]: https://www.booking.com/hotel/bb/leroy.it.html
2026-02-24 01:25:51.741 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/bb/leroy.it.html (intento 1)
2026-02-24 01:26:12.559 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:26:12.561 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:26:31.556 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:26:42.976 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:26:42.978 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:27:13.373 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:27:13.375 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:27:25.171 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Hôtel Le Roy, Christ Church (precios actualizados en 2026)' | 1,985,778 bytes
2026-02-24 01:27:25.306 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:27:25.478 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 01:27:25.478 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 01:27:25.480 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 01:27:25.480 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | 1,985,778b
2026-02-24 01:27:25.498 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [228][it] 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | imgs=8
2026-02-24 01:27:27.867 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 228
2026-02-24 01:27:27.881 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [228] COMPLETADO | 'Hôtel Le Roy, Christ Church, Barbados' | 5/5 idiomas | 467.6s
2026-02-24 01:27:27.883 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 01:27:27.884 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=229 | https://www.booking.com/hotel/bs/the-island-garden.html
2026-02-24 01:27:27.884 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 01:27:27.885 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:27:27.885 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 01:27:29.186 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 01:27:29.186 | INFO     | app.scraper_service:scrape_one:367 -   → [229] Idioma [en]: https://www.booking.com/hotel/bs/the-island-garden.html
2026-02-24 01:27:29.194 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/bs/the-island-garden.html (intento 1)
2026-02-24 01:27:43.684 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:27:43.686 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:28:08.046 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:28:13.995 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:28:13.997 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:28:44.311 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:28:44.313 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:29:01.552 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'The Island Garden Hotel, Nassau (precios actualizados en 2026)' | 1,360,449 bytes
2026-02-24 01:29:01.646 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:29:01.766 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 01:29:01.766 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 01:29:01.768 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 01:29:01.768 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | 1,360,449b
2026-02-24 01:29:01.786 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [229][en] 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | imgs=8
2026-02-24 01:29:01.797 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [229] 12 cookies extraídas del browser
2026-02-24 01:29:01.798 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 01:29:01.799 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=229 lang=en
2026-02-24 01:29:02.451 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_3bd1886b2b12.jpg (67,684 bytes, 900×900)
2026-02-24 01:29:02.471 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_04d08f5cb0f4.jpg (75,413 bytes, 1280×853)
2026-02-24 01:29:02.516 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_7b0e28712af2.jpg (92,359 bytes, 900×900)
2026-02-24 01:29:02.579 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_7d51a57a9fb6.jpg (160,171 bytes, 1200×900)
2026-02-24 01:29:02.611 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_6d8ae04dc4a3.jpg (193,611 bytes, 1200×900)
2026-02-24 01:29:02.662 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_2b44a7a04eef.jpg (29,666 bytes, 506×900)
2026-02-24 01:29:02.720 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_23347fdc4a1d.jpg (45,237 bytes, 900×900)
2026-02-24 01:29:02.733 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_f9981f676c90.jpg (49,348 bytes, 675×900)
2026-02-24 01:29:02.734 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 01:29:02.734 | INFO     | app.scraper_service:_download_images:671 -   📷 [229] 8/8 imágenes descargadas
2026-02-24 01:29:02.736 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [229] Imagenes marcadas como descargadas
2026-02-24 01:29:02.736 | INFO     | app.scraper_service:scrape_one:367 -   → [229] Idioma [es]: https://www.booking.com/hotel/bs/the-island-garden.es.html
2026-02-24 01:29:02.736 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/bs/the-island-garden.es.html (intento 1)
2026-02-24 01:29:14.638 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:29:14.640 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:29:41.497 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:29:44.950 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:29:44.952 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:30:15.272 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:30:15.274 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:30:35.068 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'The Island Garden Hotel, Nassau (precios actualizados en 2026)' | 1,352,319 bytes
2026-02-24 01:30:35.155 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:30:35.262 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 01:30:35.262 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-24 01:30:35.264 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 01:30:35.264 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | 1,352,319b
2026-02-24 01:30:35.282 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [229][es] 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | imgs=8
2026-02-24 01:30:35.282 | INFO     | app.scraper_service:scrape_one:367 -   → [229] Idioma [de]: https://www.booking.com/hotel/bs/the-island-garden.de.html
2026-02-24 01:30:35.282 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/bs/the-island-garden.de.html (intento 1)
2026-02-24 01:30:45.580 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:30:45.582 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:31:11.851 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:31:15.919 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:31:15.920 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:31:46.320 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:31:46.323 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:32:05.382 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'The Island Garden Hotel, Nassau (precios actualizados en 2026)' | 1,358,397 bytes
2026-02-24 01:32:05.469 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:32:05.585 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 01:32:05.585 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 01:32:05.587 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 01:32:05.587 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | 1,358,397b
2026-02-24 01:32:05.595 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [229][de] 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | imgs=8
2026-02-24 01:32:05.595 | INFO     | app.scraper_service:scrape_one:367 -   → [229] Idioma [fr]: https://www.booking.com/hotel/bs/the-island-garden.fr.html
2026-02-24 01:32:05.595 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/bs/the-island-garden.fr.html (intento 1)
2026-02-24 01:32:16.708 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:32:16.710 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:32:43.773 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:32:47.034 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:32:47.036 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:33:17.345 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:33:17.346 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:33:37.334 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'The Island Garden Hotel, Nassau (precios actualizados en 2026)' | 1,358,437 bytes
2026-02-24 01:33:37.455 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:33:37.571 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 01:33:37.572 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 01:33:37.573 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 01:33:37.573 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | 1,358,437b
2026-02-24 01:33:37.591 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [229][fr] 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | imgs=8
2026-02-24 01:33:37.591 | INFO     | app.scraper_service:scrape_one:367 -   → [229] Idioma [it]: https://www.booking.com/hotel/bs/the-island-garden.it.html
2026-02-24 01:33:37.591 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/bs/the-island-garden.it.html (intento 1)
2026-02-24 01:33:47.662 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:33:47.664 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:34:16.477 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:34:18.118 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:34:18.120 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:34:48.451 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:34:48.453 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:35:09.976 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'The Island Garden Hotel, Nassau (precios actualizados en 2026)' | 1,358,514 bytes
2026-02-24 01:35:10.063 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:35:10.173 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 01:35:10.174 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 01:35:10.175 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 01:35:10.175 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | 1,358,514b
2026-02-24 01:35:10.192 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [229][it] 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | imgs=8
2026-02-24 01:35:12.539 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 229
2026-02-24 01:35:12.553 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [229] COMPLETADO | 'The Island Garden Hotel, Nassau, Bahamas' | 5/5 idiomas | 464.7s
2026-02-24 01:35:12.554 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 01:35:12.554 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=230 | https://www.booking.com/hotel/tc/grace-bay-club.html
2026-02-24 01:35:12.554 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 01:35:12.554 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:35:12.560 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 01:35:14.218 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 01:35:14.218 | INFO     | app.scraper_service:scrape_one:367 -   → [230] Idioma [en]: https://www.booking.com/hotel/tc/grace-bay-club.html
2026-02-24 01:35:14.219 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/tc/grace-bay-club.html (intento 1)
2026-02-24 01:35:19.971 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:35:19.973 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:35:50.296 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:35:50.298 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:35:52.316 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:36:20.615 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:36:20.617 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:36:45.962 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Grace Bay Club, Grace Bay (precios actualizados en 2026)' | 2,576,158 bytes
2026-02-24 01:36:46.125 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:36:46.380 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 01:36:46.380 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'facilities', 'rooms']
2026-02-24 01:36:46.381 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 01:36:46.381 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | 2,576,158b
2026-02-24 01:36:46.393 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [230][en] 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | imgs=8
2026-02-24 01:36:46.402 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [230] 12 cookies extraídas del browser
2026-02-24 01:36:46.403 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 01:36:46.404 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=230 lang=en
2026-02-24 01:36:46.984 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_764d8ab9a2e3.jpg (110,466 bytes, 1280×614)
2026-02-24 01:36:47.154 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_6ad01b5b8bd5.jpg (208,280 bytes, 1240×900)
2026-02-24 01:36:47.164 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_af0bf2c87017.jpg (175,683 bytes, 1280×852)
2026-02-24 01:36:47.282 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_f2909cddf03b.jpg (172,682 bytes, 1280×853)
2026-02-24 01:36:47.295 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_fb703e094336.jpg (141,438 bytes, 1280×853)
2026-02-24 01:36:47.319 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_1ef3c13f45a2.jpg (56,706 bytes, 709×900)
2026-02-24 01:36:47.427 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_7f928c3061d7.jpg (193,123 bytes, 1280×854)
2026-02-24 01:36:47.435 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_e0515a7586b3.jpg (219,420 bytes, 1280×853)
2026-02-24 01:36:47.436 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 01:36:47.436 | INFO     | app.scraper_service:_download_images:671 -   📷 [230] 8/8 imágenes descargadas
2026-02-24 01:36:47.438 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [230] Imagenes marcadas como descargadas
2026-02-24 01:36:47.438 | INFO     | app.scraper_service:scrape_one:367 -   → [230] Idioma [es]: https://www.booking.com/hotel/tc/grace-bay-club.es.html
2026-02-24 01:36:47.438 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/tc/grace-bay-club.es.html (intento 1)
2026-02-24 01:36:51.018 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:36:51.020 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:37:21.401 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:37:21.403 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:37:27.124 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:37:51.720 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:37:51.722 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:38:20.738 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Grace Bay Club, Grace Bay (precios actualizados en 2026)' | 2,569,496 bytes
2026-02-24 01:38:20.907 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:38:21.151 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 01:38:21.151 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rating_category', 'facilities', 'rooms']
2026-02-24 01:38:21.153 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 01:38:21.153 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | 2,569,496b
2026-02-24 01:38:21.171 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [230][es] 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | imgs=8
2026-02-24 01:38:21.171 | INFO     | app.scraper_service:scrape_one:367 -   → [230] Idioma [de]: https://www.booking.com/hotel/tc/grace-bay-club.de.html
2026-02-24 01:38:21.171 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/tc/grace-bay-club.de.html (intento 1)
2026-02-24 01:38:22.045 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:38:22.047 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:38:52.358 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:38:52.360 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:39:01.968 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:39:22.671 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:39:22.673 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:39:52.986 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:39:52.988 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:39:55.571 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Grace Bay Club, Grace Bay (precios actualizados en 2026)' | 2,575,381 bytes
2026-02-24 01:39:55.736 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:39:55.995 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 01:39:55.996 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'facilities', 'rooms']
2026-02-24 01:39:55.997 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 01:39:55.997 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | 2,575,381b
2026-02-24 01:39:56.016 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [230][de] 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | imgs=8
2026-02-24 01:39:56.016 | INFO     | app.scraper_service:scrape_one:367 -   → [230] Idioma [fr]: https://www.booking.com/hotel/tc/grace-bay-club.fr.html
2026-02-24 01:39:56.016 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/tc/grace-bay-club.fr.html (intento 1)
2026-02-24 01:40:23.299 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:40:23.301 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:40:34.495 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:40:53.630 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:40:53.632 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:41:23.941 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:41:23.943 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:41:28.076 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Grace Bay Club, Grace Bay (precios actualizados en 2026)' | 2,575,455 bytes
2026-02-24 01:41:28.314 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:41:28.666 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 01:41:28.666 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'facilities', 'rooms']
2026-02-24 01:41:28.668 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 01:41:28.668 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | 2,575,455b
2026-02-24 01:41:28.687 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [230][fr] 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | imgs=8
2026-02-24 01:41:28.687 | INFO     | app.scraper_service:scrape_one:367 -   → [230] Idioma [it]: https://www.booking.com/hotel/tc/grace-bay-club.it.html
2026-02-24 01:41:28.687 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/tc/grace-bay-club.it.html (intento 1)
2026-02-24 01:41:54.322 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:41:54.324 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:42:07.538 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:42:24.703 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:42:24.705 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:42:55.021 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:42:55.024 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:43:01.110 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Grace Bay Club, Grace Bay (precios actualizados en 2026)' | 2,575,675 bytes
2026-02-24 01:43:01.272 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:43:01.541 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 01:43:01.541 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'facilities', 'rooms']
2026-02-24 01:43:01.543 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 01:43:01.543 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | 2,575,675b
2026-02-24 01:43:01.562 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [230][it] 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | imgs=8
2026-02-24 01:43:03.929 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 230
2026-02-24 01:43:03.944 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [230] COMPLETADO | 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | 5/5 idiomas | 471.4s
2026-02-24 01:43:03.945 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 01:43:03.947 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=231 | https://www.booking.com/hotel/tc/south-bank.html
2026-02-24 01:43:03.948 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 01:43:03.948 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:43:03.948 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 01:43:05.602 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 01:43:05.602 | INFO     | app.scraper_service:scrape_one:367 -   → [231] Idioma [en]: https://www.booking.com/hotel/tc/south-bank.html
2026-02-24 01:43:05.604 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/tc/south-bank.html (intento 1)
2026-02-24 01:43:25.334 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:43:25.336 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:43:43.380 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:43:55.646 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:43:55.649 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:44:25.961 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:44:25.963 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:44:36.980 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'South Bank, Long Bay Hills (precios actualizados en 2026)' | 2,585,825 bytes
2026-02-24 01:44:37.127 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:44:37.316 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 01:44:37.316 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'facilities', 'rooms']
2026-02-24 01:44:37.318 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 01:44:37.318 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | 2,585,825b
2026-02-24 01:44:37.336 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [231][en] 'South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | imgs=8
2026-02-24 01:44:37.344 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [231] 12 cookies extraídas del browser
2026-02-24 01:44:37.345 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 01:44:37.346 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=231 lang=en
2026-02-24 01:44:37.937 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_9422fb3c823e.jpg (101,340 bytes, 1280×853)
2026-02-24 01:44:37.986 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_a58a3ebfc877.jpg (112,209 bytes, 1280×853)
2026-02-24 01:44:38.011 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_d5720df4d59e.jpg (168,622 bytes, 1280×853)
2026-02-24 01:44:38.029 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_dc1cdc54f407.jpg (223,612 bytes, 1200×900)
2026-02-24 01:44:38.097 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_0719ca1a0547.jpg (268,793 bytes, 1280×842)
2026-02-24 01:44:38.198 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_15e6c051541c.jpg (112,383 bytes, 1280×853)
2026-02-24 01:44:38.206 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_2ee520051eb6.jpg (143,000 bytes, 1280×853)
2026-02-24 01:44:38.291 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_525e2949ce6d.jpg (181,707 bytes, 1280×853)
2026-02-24 01:44:38.293 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 01:44:38.294 | INFO     | app.scraper_service:_download_images:671 -   📷 [231] 8/8 imágenes descargadas
2026-02-24 01:44:38.295 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [231] Imagenes marcadas como descargadas
2026-02-24 01:44:38.296 | INFO     | app.scraper_service:scrape_one:367 -   → [231] Idioma [es]: https://www.booking.com/hotel/tc/south-bank.es.html
2026-02-24 01:44:38.296 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/tc/south-bank.es.html (intento 1)
2026-02-24 01:44:56.291 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:44:56.293 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:45:17.221 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:45:26.606 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:45:26.608 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:45:56.925 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:45:56.927 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:46:10.860 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'South Bank, Long Bay Hills (precios actualizados en 2026)' | 2,577,928 bytes
2026-02-24 01:46:11.022 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:46:11.192 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 01:46:11.193 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['facilities', 'rooms']
2026-02-24 01:46:11.194 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 01:46:11.194 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | 2,577,928b
2026-02-24 01:46:11.215 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [231][es] 'South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | imgs=8
2026-02-24 01:46:11.215 | INFO     | app.scraper_service:scrape_one:367 -   → [231] Idioma [de]: https://www.booking.com/hotel/tc/south-bank.de.html
2026-02-24 01:46:11.215 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/tc/south-bank.de.html (intento 1)
2026-02-24 01:46:27.241 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:46:27.243 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:46:48.585 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:46:57.627 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:46:57.629 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:47:28.007 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:47:28.009 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:47:42.193 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'South Bank, Long Bay Hills (precios actualizados en 2026)' | 2,583,911 bytes
2026-02-24 01:47:42.325 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:47:42.512 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 01:47:42.512 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'facilities', 'rooms']
2026-02-24 01:47:42.514 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 01:47:42.514 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | 2,583,911b
2026-02-24 01:47:42.532 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [231][de] 'South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | imgs=8
2026-02-24 01:47:42.532 | INFO     | app.scraper_service:scrape_one:367 -   → [231] Idioma [fr]: https://www.booking.com/hotel/tc/south-bank.fr.html
2026-02-24 01:47:42.532 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/tc/south-bank.fr.html (intento 1)
2026-02-24 01:47:58.329 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:47:58.330 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:48:20.593 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:48:28.659 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:48:28.661 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:48:58.984 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:48:58.986 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:49:14.252 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'South Bank, Long Bay Hills (precios actualizados en 2026)' | 2,583,939 bytes
2026-02-24 01:49:14.387 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:49:14.564 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 01:49:14.565 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'facilities', 'rooms']
2026-02-24 01:49:14.566 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 01:49:14.566 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | 2,583,939b
2026-02-24 01:49:14.583 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [231][fr] 'South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | imgs=8
2026-02-24 01:49:14.583 | INFO     | app.scraper_service:scrape_one:367 -   → [231] Idioma [it]: https://www.booking.com/hotel/tc/south-bank.it.html
2026-02-24 01:49:14.584 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/tc/south-bank.it.html (intento 1)
2026-02-24 01:49:29.307 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:49:29.309 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:49:52.321 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:49:59.634 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:49:59.636 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:50:29.958 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:50:29.960 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:50:45.900 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'South Bank, Long Bay Hills (precios actualizados en 2026)' | 2,583,844 bytes
2026-02-24 01:50:46.031 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:50:46.209 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 01:50:46.209 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'facilities', 'rooms']
2026-02-24 01:50:46.211 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 01:50:46.211 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | 2,583,844b
2026-02-24 01:50:46.230 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [231][it] 'South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | imgs=8
2026-02-24 01:50:48.593 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 231
2026-02-24 01:50:48.607 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [231] COMPLETADO | 'South Bank, Long Bay Hills, Islas Turks y Caicos' | 5/5 idiomas | 464.7s
2026-02-24 01:50:48.608 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 01:50:48.611 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=232 | https://www.booking.com/hotel/vc/the-pink-sands-club.html
2026-02-24 01:50:48.611 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 01:50:48.612 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:50:48.612 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 01:50:49.979 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 01:50:49.979 | INFO     | app.scraper_service:scrape_one:367 -   → [232] Idioma [en]: https://www.booking.com/hotel/vc/the-pink-sands-club.html
2026-02-24 01:50:49.981 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/vc/the-pink-sands-club.html (intento 1)
2026-02-24 01:51:00.281 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:51:00.283 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:51:27.425 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:51:30.642 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:51:30.644 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:52:01.199 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:52:01.201 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:52:20.979 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Mandarin Oriental, Canouan, Canouan (precios actualizados 2026)' | 1,764,611 bytes
2026-02-24 01:52:21.101 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:52:21.292 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 01:52:21.293 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 01:52:21.294 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 01:52:21.294 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | 1,764,611b
2026-02-24 01:52:21.313 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [232][en] 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | imgs=8
2026-02-24 01:52:21.326 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [232] 12 cookies extraídas del browser
2026-02-24 01:52:21.326 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 01:52:21.327 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=232 lang=en
2026-02-24 01:52:22.102 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_2d2ff4f4723c.jpg (60,890 bytes, 600×900)
2026-02-24 01:52:22.191 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_15dc437fc51d.jpg (141,179 bytes, 1280×853)
2026-02-24 01:52:22.277 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_e980facea79e.jpg (133,223 bytes, 1280×853)
2026-02-24 01:52:22.286 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_810b7cccde88.jpg (145,297 bytes, 1280×853)
2026-02-24 01:52:22.302 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_78795924e441.jpg (177,600 bytes, 1201×900)
2026-02-24 01:52:22.710 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_6870ac56647a.jpg (118,515 bytes, 1280×853)
2026-02-24 01:52:22.726 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_c4f3de71ac58.jpg (140,782 bytes, 1272×900)
2026-02-24 01:52:22.835 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_9f3e0a88b1df.jpg (236,659 bytes, 1280×853)
2026-02-24 01:52:22.837 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 01:52:22.838 | INFO     | app.scraper_service:_download_images:671 -   📷 [232] 8/8 imágenes descargadas
2026-02-24 01:52:22.839 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [232] Imagenes marcadas como descargadas
2026-02-24 01:52:22.839 | INFO     | app.scraper_service:scrape_one:367 -   → [232] Idioma [es]: https://www.booking.com/hotel/vc/the-pink-sands-club.es.html
2026-02-24 01:52:22.840 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/vc/the-pink-sands-club.es.html (intento 1)
2026-02-24 01:52:31.579 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:52:31.581 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:53:01.899 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:53:01.901 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:53:02.615 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:53:32.237 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:53:32.239 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:53:56.202 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Mandarin Oriental, Canouan, Canouan (precios actualizados 2026)' | 1,755,845 bytes
2026-02-24 01:53:56.322 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:53:56.484 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 01:53:56.485 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-24 01:53:56.486 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 01:53:56.486 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | 1,755,845b
2026-02-24 01:53:56.504 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [232][es] 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | imgs=8
2026-02-24 01:53:56.504 | INFO     | app.scraper_service:scrape_one:367 -   → [232] Idioma [de]: https://www.booking.com/hotel/vc/the-pink-sands-club.de.html
2026-02-24 01:53:56.504 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/vc/the-pink-sands-club.de.html (intento 1)
2026-02-24 01:54:02.567 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:54:02.569 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:54:32.881 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:54:32.883 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:54:34.901 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:55:03.193 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:55:03.195 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:55:28.471 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Mandarin Oriental, Canouan, Canouan (precios actualizados 2026)' | 1,761,800 bytes
2026-02-24 01:55:28.641 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:55:28.817 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 01:55:28.817 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 01:55:28.819 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 01:55:28.819 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | 1,761,800b
2026-02-24 01:55:28.945 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [232][de] 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | imgs=8
2026-02-24 01:55:28.946 | INFO     | app.scraper_service:scrape_one:367 -   → [232] Idioma [fr]: https://www.booking.com/hotel/vc/the-pink-sands-club.fr.html
2026-02-24 01:55:28.947 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/vc/the-pink-sands-club.fr.html (intento 1)
2026-02-24 01:55:33.512 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:55:33.514 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:56:03.834 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:56:03.836 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:56:06.051 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:56:34.151 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:56:34.153 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:56:59.535 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Mandarin Oriental, Canouan, Canouan (precios actualizados 2026)' | 1,673,675 bytes
2026-02-24 01:56:59.697 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:56:59.828 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 01:56:59.828 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rooms']
2026-02-24 01:56:59.829 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 01:56:59.830 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | 1,673,675b
2026-02-24 01:56:59.937 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [232][fr] 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | imgs=8
2026-02-24 01:56:59.937 | INFO     | app.scraper_service:scrape_one:367 -   → [232] Idioma [it]: https://www.booking.com/hotel/vc/the-pink-sands-club.it.html
2026-02-24 01:56:59.939 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/vc/the-pink-sands-club.it.html (intento 1)
2026-02-24 01:57:04.679 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:57:04.681 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:57:35.109 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:57:35.111 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:57:38.171 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:58:05.422 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:58:05.424 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:58:31.811 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Mandarin Oriental, Canouan, Canouan (precios actualizados 2026)' | 1,767,037 bytes
2026-02-24 01:58:31.938 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 01:58:32.124 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 01:58:32.124 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 01:58:32.126 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 01:58:32.126 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | 1,767,037b
2026-02-24 01:58:32.147 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [232][it] 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | imgs=8
2026-02-24 01:58:34.503 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 232
2026-02-24 01:58:34.516 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [232] COMPLETADO | 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | 5/5 idiomas | 465.9s
2026-02-24 01:58:34.517 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 01:58:34.518 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=233 | https://www.booking.com/hotel/mv/niyama-private-islands-maldives.html
2026-02-24 01:58:34.518 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 01:58:34.518 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:58:34.520 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 01:58:36.114 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:58:36.116 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:58:37.778 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 01:58:37.779 | INFO     | app.scraper_service:scrape_one:367 -   → [233] Idioma [en]: https://www.booking.com/hotel/mv/niyama-private-islands-maldives.html
2026-02-24 01:58:37.780 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/niyama-private-islands-maldives.html (intento 1)
2026-02-24 01:59:06.429 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:59:06.431 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 01:59:15.403 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 01:59:36.744 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 01:59:36.746 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:00:07.062 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:00:07.064 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:00:09.075 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Niyama Private Islands Maldives, Dhaalu Atoll (precios actualizados en 2026)' | 2,101,194 bytes
2026-02-24 02:00:09.243 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:00:09.433 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 02:00:09.434 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 02:00:09.435 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 02:00:09.435 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | 2,101,194b
2026-02-24 02:00:09.454 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [233][en] 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | imgs=8
2026-02-24 02:00:09.469 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [233] 12 cookies extraídas del browser
2026-02-24 02:00:09.470 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 02:00:09.471 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=233 lang=en
2026-02-24 02:00:09.967 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_c16a1c886e4b.jpg (95,865 bytes, 720×900)
2026-02-24 02:00:10.000 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_b1a4ac28381d.jpg (140,993 bytes, 1280×900)
2026-02-24 02:00:10.013 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_6a6aea4bc539.jpg (149,403 bytes, 1119×900)
2026-02-24 02:00:10.033 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_56eff861f222.jpg (218,942 bytes, 1201×900)
2026-02-24 02:00:10.234 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_c069ba21948a.jpg (117,214 bytes, 1280×852)
2026-02-24 02:00:10.277 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_0f3a25dc7c7b.jpg (365,047 bytes, 1280×900)
2026-02-24 02:00:10.483 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_9876171d2a55.jpg (155,879 bytes, 1280×900)
2026-02-24 02:00:10.581 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_5dd09569ff52.jpg (355,195 bytes, 1202×900)
2026-02-24 02:00:10.583 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 02:00:10.584 | INFO     | app.scraper_service:_download_images:671 -   📷 [233] 8/8 imágenes descargadas
2026-02-24 02:00:10.585 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [233] Imagenes marcadas como descargadas
2026-02-24 02:00:10.585 | INFO     | app.scraper_service:scrape_one:367 -   → [233] Idioma [es]: https://www.booking.com/hotel/mv/niyama-private-islands-maldives.es.html
2026-02-24 02:00:10.585 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/niyama-private-islands-maldives.es.html (intento 1)
2026-02-24 02:00:37.383 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:00:37.385 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:00:50.395 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:01:07.703 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:01:07.705 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:01:38.028 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:01:38.031 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:01:43.956 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Niyama Private Islands Maldives, Dhaalu Atoll (precios actualizados en 2026)' | 2,092,707 bytes
2026-02-24 02:01:44.126 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:01:44.370 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 02:01:44.372 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-24 02:01:44.373 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 02:01:44.375 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | 2,092,707b
2026-02-24 02:01:44.396 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [233][es] 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | imgs=8
2026-02-24 02:01:44.396 | INFO     | app.scraper_service:scrape_one:367 -   → [233] Idioma [de]: https://www.booking.com/hotel/mv/niyama-private-islands-maldives.de.html
2026-02-24 02:01:44.397 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/niyama-private-islands-maldives.de.html (intento 1)
2026-02-24 02:02:08.408 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:02:08.410 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:02:23.028 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:02:38.789 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:02:38.791 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:03:09.119 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:03:09.121 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:03:16.616 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Niyama Private Islands Maldives, Dhaalu Atoll (precios actualizados en 2026)' | 2,099,116 bytes
2026-02-24 02:03:16.770 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:03:16.935 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 02:03:16.935 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 02:03:16.936 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 02:03:16.937 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | 2,099,116b
2026-02-24 02:03:16.956 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [233][de] 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | imgs=8
2026-02-24 02:03:16.956 | INFO     | app.scraper_service:scrape_one:367 -   → [233] Idioma [fr]: https://www.booking.com/hotel/mv/niyama-private-islands-maldives.fr.html
2026-02-24 02:03:16.956 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/niyama-private-islands-maldives.fr.html (intento 1)
2026-02-24 02:03:39.434 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:03:39.436 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:03:54.039 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:04:09.756 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:04:09.758 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:04:40.065 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:04:40.067 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:04:47.596 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Niyama Private Islands Maldives, Dhaalu Atoll (precios actualizados en 2026)' | 2,099,213 bytes
2026-02-24 02:04:47.750 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:04:47.992 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 02:04:47.993 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 02:04:47.994 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 02:04:47.994 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | 2,099,213b
2026-02-24 02:04:48.013 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [233][fr] 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | imgs=8
2026-02-24 02:04:48.013 | INFO     | app.scraper_service:scrape_one:367 -   → [233] Idioma [it]: https://www.booking.com/hotel/mv/niyama-private-islands-maldives.it.html
2026-02-24 02:04:48.013 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/niyama-private-islands-maldives.it.html (intento 1)
2026-02-24 02:05:10.378 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:05:10.380 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:05:25.574 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:05:40.713 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:05:40.715 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:06:11.044 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:06:11.046 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:06:19.283 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Niyama Private Islands Maldives, Dhaalu Atoll (precios actualizados en 2026)' | 2,099,114 bytes
2026-02-24 02:06:19.438 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:06:19.606 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 02:06:19.606 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 02:06:19.607 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 02:06:19.608 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | 2,099,114b
2026-02-24 02:06:19.627 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [233][it] 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | imgs=8
2026-02-24 02:06:21.990 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 233
2026-02-24 02:06:22.005 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [233] COMPLETADO | 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | 5/5 idiomas | 467.5s
2026-02-24 02:06:22.006 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 02:06:22.008 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=234 | https://www.booking.com/hotel/mv/ananea-madivaru-maldives.html
2026-02-24 02:06:22.009 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 02:06:22.009 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:06:22.009 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 02:06:23.741 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 02:06:23.741 | INFO     | app.scraper_service:scrape_one:367 -   → [234] Idioma [en]: https://www.booking.com/hotel/mv/ananea-madivaru-maldives.html
2026-02-24 02:06:23.743 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/ananea-madivaru-maldives.html (intento 1)
2026-02-24 02:06:41.377 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:06:41.379 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:07:03.382 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:07:11.769 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:07:11.774 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:07:42.164 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:07:42.166 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:07:56.956 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Ananea Madivaru Maldives, Toroka (precios actualizados en 2026)' | 1,685,044 bytes
2026-02-24 02:07:57.084 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:07:57.312 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 02:07:57.313 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 02:07:57.315 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 02:07:57.315 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.7 | 1,685,044b
2026-02-24 02:07:57.329 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [234][en] 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.7 | imgs=8
2026-02-24 02:07:57.342 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [234] 12 cookies extraídas del browser
2026-02-24 02:07:57.343 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 02:07:57.344 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=234 lang=en
2026-02-24 02:07:58.371 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_7f7f5649a82b.jpg (102,424 bytes, 1280×720)
2026-02-24 02:07:58.411 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_f7ad212d3fc5.jpg (119,502 bytes, 1280×853)
2026-02-24 02:07:58.436 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_0860c860648f.jpg (136,086 bytes, 1280×853)
2026-02-24 02:07:58.437 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_f2f0c5cb9826.jpg (127,536 bytes, 1280×853)
2026-02-24 02:07:58.558 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_d2100e5fc277.jpg (209,022 bytes, 1280×853)
2026-02-24 02:07:58.880 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_bde2e0cff14b.jpg (115,098 bytes, 1280×853)
2026-02-24 02:07:58.977 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_11e5ede835b0.jpg (135,276 bytes, 1280×853)
2026-02-24 02:07:59.032 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_ea15bbacb1e8.jpg (220,036 bytes, 1280×853)
2026-02-24 02:07:59.034 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 02:07:59.035 | INFO     | app.scraper_service:_download_images:671 -   📷 [234] 8/8 imágenes descargadas
2026-02-24 02:07:59.035 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [234] Imagenes marcadas como descargadas
2026-02-24 02:07:59.036 | INFO     | app.scraper_service:scrape_one:367 -   → [234] Idioma [es]: https://www.booking.com/hotel/mv/ananea-madivaru-maldives.es.html
2026-02-24 02:07:59.036 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/ananea-madivaru-maldives.es.html (intento 1)
2026-02-24 02:08:12.495 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:08:12.496 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:08:37.297 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:08:42.848 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:08:42.850 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:09:13.167 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:09:13.170 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:09:30.878 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Ananea Madivaru Maldives, Toroka (precios actualizados en 2026)' | 1,675,819 bytes
2026-02-24 02:09:31.009 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:09:31.134 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 02:09:31.134 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-24 02:09:31.136 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 02:09:31.136 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.7 | 1,675,819b
2026-02-24 02:09:31.154 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [234][es] 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.7 | imgs=8
2026-02-24 02:09:31.154 | INFO     | app.scraper_service:scrape_one:367 -   → [234] Idioma [de]: https://www.booking.com/hotel/mv/ananea-madivaru-maldives.de.html
2026-02-24 02:09:31.154 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/ananea-madivaru-maldives.de.html (intento 1)
2026-02-24 02:09:43.496 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:09:43.498 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:10:08.970 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:10:13.827 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:10:13.829 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:10:44.147 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:10:44.149 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:11:02.514 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Ananea Madivaru Maldives, Toroka (precios actualizados en 2026)' | 1,680,591 bytes
2026-02-24 02:11:02.623 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:11:02.791 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 02:11:02.792 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 02:11:02.793 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 02:11:02.794 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.7 | 1,680,591b
2026-02-24 02:11:02.802 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [234][de] 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.7 | imgs=8
2026-02-24 02:11:02.802 | INFO     | app.scraper_service:scrape_one:367 -   → [234] Idioma [fr]: https://www.booking.com/hotel/mv/ananea-madivaru-maldives.fr.html
2026-02-24 02:11:02.802 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/ananea-madivaru-maldives.fr.html (intento 1)
2026-02-24 02:11:14.475 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:11:14.476 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:11:40.127 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:11:44.822 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:11:44.824 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:12:15.221 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:12:15.222 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:12:33.753 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Ananea Madivaru Maldives, Toroka (precios actualizados en 2026)' | 1,750,832 bytes
2026-02-24 02:12:33.871 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:12:34.050 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 02:12:34.050 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 02:12:34.052 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 02:12:34.052 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.7 | 1,750,832b
2026-02-24 02:12:34.073 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [234][fr] 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.7 | imgs=8
2026-02-24 02:12:34.073 | INFO     | app.scraper_service:scrape_one:367 -   → [234] Idioma [it]: https://www.booking.com/hotel/mv/ananea-madivaru-maldives.it.html
2026-02-24 02:12:34.073 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/ananea-madivaru-maldives.it.html (intento 1)
2026-02-24 02:12:45.616 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:12:45.618 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:13:12.021 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:13:15.946 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:13:15.948 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:13:46.262 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 64.238.204.249
2026-02-24 02:13:46.264 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:14:05.619 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Ananea Madivaru Maldives, Toroka (precios actualizados en 2026)' | 1,682,778 bytes
2026-02-24 02:14:05.719 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:14:05.858 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 02:14:05.858 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 02:14:05.859 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 02:14:05.860 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.7 | 1,682,778b
2026-02-24 02:14:05.878 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [234][it] 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.7 | imgs=8
2026-02-24 02:14:08.277 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 234
2026-02-24 02:14:08.293 | INFO     | app.scraper_service:_maybe_rotate_vpn:182 - 🔄 Rotando VPN (motivo=periodica, fallos_consec=0, hoteles=10)...
2026-02-24 02:14:08.294 | INFO     | app.vpn_manager_windows:rotate:359 - 🔄 Rotando VPN...
2026-02-24 02:14:11.110 | INFO     | app.vpn_manager_windows:disconnect:334 - ✓ VPN desconectada (CLI)
2026-02-24 02:14:16.110 | INFO     | app.vpn_manager_windows:connect:171 - Conectando a Italy (IT)...
2026-02-24 02:14:19.867 | INFO     | app.vpn_manager_windows:_connect_via_cli:207 - Conectando CLI a Italy...
2026-02-24 02:14:33.209 | SUCCESS  | app.vpn_manager_windows:_connect_via_cli:231 - ✓ Conectado a Italy — IP: 194.34.233.13
2026-02-24 02:14:33.209 | SUCCESS  | app.vpn_manager_windows:rotate:379 - ✓ Rotación exitosa → Italy
2026-02-24 02:14:33.211 | SUCCESS  | app.scraper_service:_maybe_rotate_vpn:191 - ✓ VPN rotada → IP: 194.34.233.13
2026-02-24 02:14:33.211 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [234] COMPLETADO | 'Ananea Madivaru Maldives, Toroka, Maldivas' | 5/5 idiomas | 466.3s
2026-02-24 02:14:33.211 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:14:33.214 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 02:14:33.215 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=235 | https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.html
2026-02-24 02:14:33.215 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 02:14:33.215 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:14:33.216 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 02:14:33.215 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:14:33.962 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 02:14:33.962 | INFO     | app.scraper_service:scrape_one:367 -   → [235] Idioma [en]: https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.html
2026-02-24 02:14:33.964 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.html (intento 1)
2026-02-24 02:15:03.668 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:15:03.671 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:15:12.754 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:15:34.020 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:15:34.021 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:16:04.456 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:16:04.458 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:16:06.261 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cocomo Maldives, Himmafushi (precios actualizados 2026)' | 1,737,378 bytes
2026-02-24 02:16:06.398 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:16:06.582 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 02:16:06.583 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 02:16:06.584 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 02:16:06.584 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.2 | 1,737,378b
2026-02-24 02:16:06.601 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [235][en] '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.2 | imgs=8
2026-02-24 02:16:06.609 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [235] 12 cookies extraídas del browser
2026-02-24 02:16:06.610 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 02:16:06.611 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=235 lang=en
2026-02-24 02:16:07.038 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_fb52ba10b612.jpg (47,922 bytes, 675×900)
2026-02-24 02:16:07.128 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_6720b23bba07.jpg (87,754 bytes, 1280×587)
2026-02-24 02:16:07.199 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_88b26b6b1318.jpg (143,390 bytes, 1280×853)
2026-02-24 02:16:07.200 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_b042e84a2533.jpg (157,926 bytes, 1280×853)
2026-02-24 02:16:07.228 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_9f9751a498fb.jpg (208,689 bytes, 1280×853)
2026-02-24 02:16:07.241 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_f8fbae44681e.jpg (61,345 bytes, 1280×463)
2026-02-24 02:16:07.376 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_e803df097bfc.jpg (107,333 bytes, 1280×853)
2026-02-24 02:16:07.379 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_3944c703f4d4.jpg (162,470 bytes, 1280×853)
2026-02-24 02:16:07.381 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 02:16:07.381 | INFO     | app.scraper_service:_download_images:671 -   📷 [235] 8/8 imágenes descargadas
2026-02-24 02:16:07.382 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [235] Imagenes marcadas como descargadas
2026-02-24 02:16:07.382 | INFO     | app.scraper_service:scrape_one:367 -   → [235] Idioma [es]: https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.es.html
2026-02-24 02:16:07.382 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.es.html (intento 1)
2026-02-24 02:16:34.837 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:16:34.839 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:16:46.641 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:17:05.182 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:17:05.184 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:17:35.533 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:17:35.535 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:17:40.191 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cocomo Maldives, Himmafushi (precios actualizados 2026)' | 1,727,978 bytes
2026-02-24 02:17:40.323 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:17:40.506 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 02:17:40.506 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rating_category', 'rooms']
2026-02-24 02:17:40.508 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 02:17:40.508 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.2 | 1,727,978b
2026-02-24 02:17:40.536 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [235][es] '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.2 | imgs=8
2026-02-24 02:17:40.536 | INFO     | app.scraper_service:scrape_one:367 -   → [235] Idioma [de]: https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.de.html
2026-02-24 02:17:40.536 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.de.html (intento 1)
2026-02-24 02:18:05.891 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:18:05.893 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:18:19.834 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:18:36.257 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:18:36.258 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:19:06.607 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:19:06.609 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:19:13.374 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cocomo Maldives, Himmafushi (precios actualizados 2026)' | 1,735,210 bytes
2026-02-24 02:19:13.585 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:19:13.782 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 02:19:13.783 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 02:19:13.784 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 02:19:13.784 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.2 | 1,735,210b
2026-02-24 02:19:13.804 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [235][de] '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.2 | imgs=8
2026-02-24 02:19:13.804 | INFO     | app.scraper_service:scrape_one:367 -   → [235] Idioma [fr]: https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.fr.html
2026-02-24 02:19:13.804 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.fr.html (intento 1)
2026-02-24 02:19:37.035 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:19:37.037 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:19:52.930 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:20:07.484 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:20:07.486 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:20:37.835 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:20:37.837 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:20:46.419 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cocomo Maldives, Himmafushi (precios actualizados 2026)' | 1,740,383 bytes
2026-02-24 02:20:46.554 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:20:46.727 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 02:20:46.727 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 02:20:46.729 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 02:20:46.729 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.2 | 1,740,383b
2026-02-24 02:20:46.748 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [235][fr] '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.2 | imgs=8
2026-02-24 02:20:46.748 | INFO     | app.scraper_service:scrape_one:367 -   → [235] Idioma [it]: https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.it.html
2026-02-24 02:20:46.748 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.it.html (intento 1)
2026-02-24 02:21:08.205 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:21:08.207 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:21:24.073 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:21:38.579 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:21:38.581 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:22:08.958 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:22:08.960 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:22:17.687 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cocomo Maldives, Himmafushi (precios actualizados 2026)' | 1,735,160 bytes
2026-02-24 02:22:17.823 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:22:17.999 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 02:22:17.999 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 02:22:18.000 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 02:22:18.000 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.2 | 1,735,160b
2026-02-24 02:22:18.018 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [235][it] '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.2 | imgs=8
2026-02-24 02:22:20.481 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 235
2026-02-24 02:22:20.495 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [235] COMPLETADO | '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | 5/5 idiomas | 467.3s
2026-02-24 02:22:20.496 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 02:22:20.496 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=236 | https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.html
2026-02-24 02:22:20.499 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 02:22:20.499 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:22:20.500 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 02:22:21.924 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 02:22:21.924 | INFO     | app.scraper_service:scrape_one:367 -   → [236] Idioma [en]: https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.html
2026-02-24 02:22:21.926 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.html (intento 1)
2026-02-24 02:22:39.301 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:22:39.305 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:22:57.889 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:23:09.810 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:23:09.812 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:23:40.163 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:23:40.165 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:23:42.252 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cheval Blanc Randheli, Maldives, Randheli (precios actualizados 2026)' | 1,884,773 bytes
2026-02-24 02:23:42.425 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:23:42.678 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 02:23:42.679 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 02:23:42.680 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 02:23:42.680 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | 1,884,773b
2026-02-24 02:23:42.688 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [236][en] 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | imgs=8
2026-02-24 02:23:42.697 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [236] 14 cookies extraídas del browser
2026-02-24 02:23:42.697 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 02:23:42.698 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=236 lang=en
2026-02-24 02:23:43.249 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_dbfe223f3b49.jpg (115,426 bytes, 1280×853)
2026-02-24 02:23:43.265 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_42a1161c074f.jpg (130,203 bytes, 1200×900)
2026-02-24 02:23:43.299 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_bd14890af3b8.jpg (149,690 bytes, 1280×862)
2026-02-24 02:23:43.302 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_e4c3374ed58e.jpg (168,169 bytes, 1200×900)
2026-02-24 02:23:43.350 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_1161f041afee.jpg (214,274 bytes, 1200×900)
2026-02-24 02:23:43.548 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_28b20c546b71.jpg (163,992 bytes, 1280×854)
2026-02-24 02:23:43.551 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_15a467481acd.jpg (156,576 bytes, 1280×853)
2026-02-24 02:23:43.663 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_c72d0f079b7c.jpg (168,977 bytes, 1280×853)
2026-02-24 02:23:43.664 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 02:23:43.665 | INFO     | app.scraper_service:_download_images:671 -   📷 [236] 8/8 imágenes descargadas
2026-02-24 02:23:43.666 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [236] Imagenes marcadas como descargadas
2026-02-24 02:23:43.666 | INFO     | app.scraper_service:scrape_one:367 -   → [236] Idioma [es]: https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.es.html
2026-02-24 02:23:43.666 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.es.html (intento 1)
2026-02-24 02:24:10.519 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:24:10.521 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:24:21.675 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:24:40.942 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:24:40.944 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:25:11.364 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:25:11.366 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:25:15.200 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cheval Blanc Randheli, Maldives, Randheli (precios actualizados 2026)' | 1,861,957 bytes
2026-02-24 02:25:15.340 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:25:15.569 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 02:25:15.570 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-24 02:25:15.571 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 02:25:15.571 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | 1,861,957b
2026-02-24 02:25:15.591 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [236][es] 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | imgs=8
2026-02-24 02:25:15.591 | INFO     | app.scraper_service:scrape_one:367 -   → [236] Idioma [de]: https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.de.html
2026-02-24 02:25:15.591 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.de.html (intento 1)
2026-02-24 02:25:41.713 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:25:41.715 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:25:53.367 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:26:12.078 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:26:12.080 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:26:42.444 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:26:42.446 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:26:46.849 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cheval Blanc Randheli, Maldives, Randheli (precios actualizados 2026)' | 1,857,805 bytes
2026-02-24 02:26:46.990 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:26:47.228 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 02:26:47.228 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 02:26:47.230 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 02:26:47.230 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | 1,857,805b
2026-02-24 02:26:47.249 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [236][de] 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | imgs=8
2026-02-24 02:26:47.249 | INFO     | app.scraper_service:scrape_one:367 -   → [236] Idioma [fr]: https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.fr.html
2026-02-24 02:26:47.249 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.fr.html (intento 1)
2026-02-24 02:27:12.796 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:27:12.798 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:27:25.253 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:27:43.157 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:27:43.159 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:28:13.527 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:28:13.530 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:28:18.861 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cheval Blanc Randheli, Maldives, Randheli (precios actualizados 2026)' | 1,858,966 bytes
2026-02-24 02:28:19.006 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:28:19.251 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 02:28:19.251 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 02:28:19.252 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 02:28:19.253 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | 1,858,966b
2026-02-24 02:28:19.262 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [236][fr] 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | imgs=8
2026-02-24 02:28:19.263 | INFO     | app.scraper_service:scrape_one:367 -   → [236] Idioma [it]: https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.it.html
2026-02-24 02:28:19.263 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.it.html (intento 1)
2026-02-24 02:28:43.901 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:28:43.903 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:28:57.386 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:29:14.263 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:29:14.265 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:29:44.692 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:29:44.694 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:29:50.956 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Cheval Blanc Randheli, Maldives, Randheli (precios actualizados 2026)' | 1,860,217 bytes
2026-02-24 02:29:51.099 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:29:51.333 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 02:29:51.334 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 02:29:51.335 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 02:29:51.336 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | 1,860,217b
2026-02-24 02:29:51.372 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [236][it] 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | imgs=8
2026-02-24 02:29:53.727 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 236
2026-02-24 02:29:53.741 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [236] COMPLETADO | 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | 5/5 idiomas | 453.2s
2026-02-24 02:29:53.742 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 02:29:53.742 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=237 | https://www.booking.com/hotel/mv/icom-blue-seaview.html
2026-02-24 02:29:53.742 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 02:29:53.745 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:29:53.745 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 02:29:55.270 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 02:29:55.270 | INFO     | app.scraper_service:scrape_one:367 -   → [237] Idioma [en]: https://www.booking.com/hotel/mv/icom-blue-seaview.html
2026-02-24 02:29:55.272 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/icom-blue-seaview.html (intento 1)
2026-02-24 02:30:15.127 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:30:15.129 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:30:33.790 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:30:45.490 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:30:45.492 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:31:15.908 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:31:15.910 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:31:27.294 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'iCom Blue Seaview, Maafushi (precios actualizados 2026)' | 1,941,713 bytes
2026-02-24 02:31:27.449 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:31:27.688 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 02:31:27.690 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 02:31:27.691 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 02:31:27.692 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★ iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | 1,941,713b
2026-02-24 02:31:27.710 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [237][en] '★★★★ iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | imgs=8
2026-02-24 02:31:27.721 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [237] 12 cookies extraídas del browser
2026-02-24 02:31:27.723 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 02:31:27.727 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=237 lang=en
2026-02-24 02:31:28.209 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_e643ae694c2a.jpg (53,288 bytes, 675×900)
2026-02-24 02:31:28.307 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_7ed313d40b2a.jpg (101,756 bytes, 1280×853)
2026-02-24 02:31:28.344 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_1b6b1641933a.jpg (122,378 bytes, 1200×900)
2026-02-24 02:31:28.372 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_aca18abe7430.jpg (195,868 bytes, 1280×720)
2026-02-24 02:31:28.398 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_9cb4697517f0.jpg (200,361 bytes, 1280×720)
2026-02-24 02:31:28.519 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_2a26dfce25d0.jpg (125,904 bytes, 1200×900)
2026-02-24 02:31:28.520 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_9eac350b3a8a.jpg (120,656 bytes, 1280×854)
2026-02-24 02:31:28.525 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_4e8501fddbae.jpg (102,723 bytes, 1280×854)
2026-02-24 02:31:28.527 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 02:31:28.527 | INFO     | app.scraper_service:_download_images:671 -   📷 [237] 8/8 imágenes descargadas
2026-02-24 02:31:28.528 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [237] Imagenes marcadas como descargadas
2026-02-24 02:31:28.529 | INFO     | app.scraper_service:scrape_one:367 -   → [237] Idioma [es]: https://www.booking.com/hotel/mv/icom-blue-seaview.es.html
2026-02-24 02:31:28.529 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/icom-blue-seaview.es.html (intento 1)
2026-02-24 02:31:46.284 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:31:46.285 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:32:06.112 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:32:16.623 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:32:16.624 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:32:46.971 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:32:46.972 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:32:59.705 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'iCom Blue Seaview, Maafushi (precios actualizados 2026)' | 1,941,358 bytes
2026-02-24 02:32:59.848 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:33:00.039 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 02:33:00.040 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-24 02:33:00.041 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 02:33:00.042 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★ iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | 1,941,358b
2026-02-24 02:33:00.062 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [237][es] '★★★★ iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | imgs=8
2026-02-24 02:33:00.062 | INFO     | app.scraper_service:scrape_one:367 -   → [237] Idioma [de]: https://www.booking.com/hotel/mv/icom-blue-seaview.de.html
2026-02-24 02:33:00.062 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/icom-blue-seaview.de.html (intento 1)
2026-02-24 02:33:17.332 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:33:17.334 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:33:39.982 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:33:47.679 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:33:47.681 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:34:18.040 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:34:18.042 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:34:33.554 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'iCom Blue Seaview, Maafushi (precios actualizados 2026)' | 1,948,300 bytes
2026-02-24 02:34:33.736 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:34:33.930 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 02:34:33.931 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 02:34:33.932 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 02:34:33.932 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★ iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | 1,948,300b
2026-02-24 02:34:33.950 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [237][de] '★★★★ iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | imgs=8
2026-02-24 02:34:33.952 | INFO     | app.scraper_service:scrape_one:367 -   → [237] Idioma [fr]: https://www.booking.com/hotel/mv/icom-blue-seaview.fr.html
2026-02-24 02:34:33.953 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/icom-blue-seaview.fr.html (intento 1)
2026-02-24 02:34:48.485 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:34:48.487 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:35:12.133 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:35:18.905 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:35:18.907 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:35:49.255 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:35:49.257 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:36:05.699 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'iCom Blue Seaview, Maafushi (precios actualizados 2026)' | 1,948,588 bytes
2026-02-24 02:36:05.835 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:36:06.025 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 02:36:06.025 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 02:36:06.027 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 02:36:06.027 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★ iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | 1,948,588b
2026-02-24 02:36:06.045 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [237][fr] '★★★★ iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | imgs=8
2026-02-24 02:36:06.046 | INFO     | app.scraper_service:scrape_one:367 -   → [237] Idioma [it]: https://www.booking.com/hotel/mv/icom-blue-seaview.it.html
2026-02-24 02:36:06.046 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/icom-blue-seaview.it.html (intento 1)
2026-02-24 02:36:19.632 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:36:19.633 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:36:43.433 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:36:50.002 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:36:50.004 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:37:20.371 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:37:20.373 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:37:36.941 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'iCom Blue Seaview, Maafushi (precios actualizados 2026)' | 1,947,856 bytes
2026-02-24 02:37:37.110 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:37:37.307 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 02:37:37.307 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 02:37:37.309 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 02:37:37.309 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★ iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | 1,947,856b
2026-02-24 02:37:37.330 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [237][it] '★★★★ iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | imgs=8
2026-02-24 02:37:39.717 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 237
2026-02-24 02:37:39.732 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [237] COMPLETADO | '★★★★ iCom Blue Seaview, Maafushi, Maldivas' | 5/5 idiomas | 466.0s
2026-02-24 02:37:39.734 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 02:37:39.734 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=238 | https://www.booking.com/hotel/mv/eri-maldives.html
2026-02-24 02:37:39.734 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 02:37:39.734 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:37:39.735 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 02:37:41.485 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 02:37:41.486 | INFO     | app.scraper_service:scrape_one:367 -   → [238] Idioma [en]: https://www.booking.com/hotel/mv/eri-maldives.html
2026-02-24 02:37:41.487 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/eri-maldives.html (intento 1)
2026-02-24 02:37:50.897 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:37:50.900 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:38:18.463 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:38:21.244 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:38:21.246 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:38:51.715 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:38:51.717 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:39:12.004 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Eri Maldives, Atolón de Malé Norte (precios actualizados en 2026)' | 1,645,795 bytes
2026-02-24 02:39:12.132 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:39:12.305 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 02:39:12.305 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 02:39:12.307 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 02:39:12.307 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | 1,645,795b
2026-02-24 02:39:12.314 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [238][en] 'Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | imgs=8
2026-02-24 02:39:12.325 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [238] 12 cookies extraídas del browser
2026-02-24 02:39:12.325 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 02:39:12.326 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=238 lang=en
2026-02-24 02:39:12.831 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_b04d8bee7ffd.jpg (95,537 bytes, 1280×818)
2026-02-24 02:39:12.844 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_2f5f08096fae.jpg (117,747 bytes, 1201×900)
2026-02-24 02:39:12.886 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_76f597b75325.jpg (130,703 bytes, 1280×853)
2026-02-24 02:39:12.894 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_83926d7eb940.jpg (175,897 bytes, 1200×900)
2026-02-24 02:39:12.905 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_561a168f5a57.jpg (241,885 bytes, 1200×900)
2026-02-24 02:39:13.003 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_ca1e4ea9c62c.jpg (111,399 bytes, 1125×900)
2026-02-24 02:39:13.007 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_985550f1c961.jpg (98,578 bytes, 675×900)
2026-02-24 02:39:13.240 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_bb8f9018ed16.jpg (131,286 bytes, 1197×900)
2026-02-24 02:39:13.242 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 02:39:13.243 | INFO     | app.scraper_service:_download_images:671 -   📷 [238] 8/8 imágenes descargadas
2026-02-24 02:39:13.244 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [238] Imagenes marcadas como descargadas
2026-02-24 02:39:13.244 | INFO     | app.scraper_service:scrape_one:367 -   → [238] Idioma [es]: https://www.booking.com/hotel/mv/eri-maldives.es.html
2026-02-24 02:39:13.244 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/eri-maldives.es.html (intento 1)
2026-02-24 02:39:22.067 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:39:22.069 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:39:51.975 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:39:52.606 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:39:52.608 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:40:23.038 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:40:23.040 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:40:45.620 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Eri Maldives, Atolón de Malé Norte (precios actualizados en 2026)' | 1,641,535 bytes
2026-02-24 02:40:45.755 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:40:45.919 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 02:40:45.919 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rating_category', 'rooms']
2026-02-24 02:40:45.921 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 02:40:45.921 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | 1,641,535b
2026-02-24 02:40:45.928 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [238][es] 'Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | imgs=8
2026-02-24 02:40:45.929 | INFO     | app.scraper_service:scrape_one:367 -   → [238] Idioma [de]: https://www.booking.com/hotel/mv/eri-maldives.de.html
2026-02-24 02:40:45.929 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/eri-maldives.de.html (intento 1)
2026-02-24 02:40:53.397 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:40:53.399 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:41:22.913 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:41:23.756 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:41:23.759 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:41:54.121 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:41:54.123 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:42:16.474 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Eri Maldives, Atolón de Malé Norte (precios actualizados en 2026)' | 1,645,904 bytes
2026-02-24 02:42:16.608 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:42:16.772 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 02:42:16.774 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 02:42:16.775 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 02:42:16.775 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | 1,645,904b
2026-02-24 02:42:16.795 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [238][de] 'Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | imgs=8
2026-02-24 02:42:16.796 | INFO     | app.scraper_service:scrape_one:367 -   → [238] Idioma [fr]: https://www.booking.com/hotel/mv/eri-maldives.fr.html
2026-02-24 02:42:16.796 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/eri-maldives.fr.html (intento 1)
2026-02-24 02:42:24.481 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:42:24.485 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:42:54.836 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:42:54.838 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:42:55.705 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:43:25.195 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:43:25.197 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:43:49.269 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Eri Maldives, Atolón de Malé Norte (precios actualizados en 2026)' | 1,648,249 bytes
2026-02-24 02:43:49.398 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:43:49.561 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 02:43:49.562 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 02:43:49.563 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 02:43:49.563 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | 1,648,249b
2026-02-24 02:43:49.581 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [238][fr] 'Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | imgs=8
2026-02-24 02:43:49.581 | INFO     | app.scraper_service:scrape_one:367 -   → [238] Idioma [it]: https://www.booking.com/hotel/mv/eri-maldives.it.html
2026-02-24 02:43:49.582 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/eri-maldives.it.html (intento 1)
2026-02-24 02:43:55.552 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:43:55.554 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:44:25.904 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:44:25.906 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:44:28.611 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:44:56.329 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:44:56.331 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:45:22.141 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Eri Maldives, Atolón de Malé Norte (precios actualizados en 2026)' | 1,648,163 bytes
2026-02-24 02:45:22.273 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:45:22.437 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 02:45:22.437 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 02:45:22.438 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 02:45:22.439 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ 'Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | 1,648,163b
2026-02-24 02:45:22.456 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [238][it] 'Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | imgs=8
2026-02-24 02:45:24.804 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 238
2026-02-24 02:45:24.818 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [238] COMPLETADO | 'Eri Maldives, Atolón de Malé Norte, Maldivas' | 5/5 idiomas | 465.1s
2026-02-24 02:45:24.819 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 02:45:24.822 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=239 | https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.html
2026-02-24 02:45:24.822 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 02:45:24.822 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:45:24.822 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 02:45:26.392 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 02:45:26.392 | INFO     | app.scraper_service:scrape_one:367 -   → [239] Idioma [en]: https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.html
2026-02-24 02:45:26.393 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.html (intento 1)
2026-02-24 02:45:26.746 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:45:26.748 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:45:57.411 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:45:57.414 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:46:03.834 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:46:27.761 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:46:27.763 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:46:57.367 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male (precios actualizados 2026)' | 1,874,266 bytes
2026-02-24 02:46:57.523 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:46:57.748 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 02:46:57.749 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 02:46:57.750 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 02:46:57.750 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★★ dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.4 | 1,874,266b
2026-02-24 02:46:57.769 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [239][en] '★★★★★ dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.4 | imgs=8
2026-02-24 02:46:57.779 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [239] 12 cookies extraídas del browser
2026-02-24 02:46:57.780 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 02:46:57.781 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=239 lang=en
2026-02-24 02:46:58.126 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:46:58.128 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:46:58.333 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_80ac6704dfd9.jpg (124,555 bytes, 1280×817)
2026-02-24 02:46:58.359 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_5868cee62598.jpg (165,778 bytes, 1280×828)
2026-02-24 02:46:58.415 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_903adf6a201c.jpg (138,437 bytes, 1280×853)
2026-02-24 02:46:58.450 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_50786e7231bb.jpg (224,576 bytes, 900×900)
2026-02-24 02:46:58.453 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_38c55cadaa1e.jpg (207,909 bytes, 1183×900)
2026-02-24 02:46:58.765 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_b7094196037c.jpg (115,139 bytes, 1280×853)
2026-02-24 02:46:58.856 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_3a329ced569b.jpg (153,042 bytes, 1280×869)
2026-02-24 02:46:58.875 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_9c4b8d4c92ab.jpg (179,599 bytes, 1280×873)
2026-02-24 02:46:58.877 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 02:46:58.878 | INFO     | app.scraper_service:_download_images:671 -   📷 [239] 8/8 imágenes descargadas
2026-02-24 02:46:58.879 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [239] Imagenes marcadas como descargadas
2026-02-24 02:46:58.880 | INFO     | app.scraper_service:scrape_one:367 -   → [239] Idioma [es]: https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.es.html
2026-02-24 02:46:58.880 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.es.html (intento 1)
2026-02-24 02:47:28.494 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:47:28.496 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:47:37.901 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:47:58.888 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:47:58.890 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:48:29.241 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:48:29.242 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:48:31.411 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male (precios actualizados 2026)' | 1,868,169 bytes
2026-02-24 02:48:31.569 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:48:31.788 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 02:48:31.788 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rating_category', 'rooms']
2026-02-24 02:48:31.790 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 02:48:31.790 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★★ dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.4 | 1,868,169b
2026-02-24 02:48:31.809 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [239][es] '★★★★★ dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.4 | imgs=8
2026-02-24 02:48:31.810 | INFO     | app.scraper_service:scrape_one:367 -   → [239] Idioma [de]: https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.de.html
2026-02-24 02:48:31.810 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.de.html (intento 1)
2026-02-24 02:48:59.612 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:48:59.614 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:49:09.535 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:49:29.981 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:49:29.983 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:50:00.446 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:50:00.448 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:50:03.068 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male (precios actualizados 2026)' | 1,876,119 bytes
2026-02-24 02:50:03.268 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:50:03.636 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 02:50:03.636 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 02:50:03.638 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 02:50:03.638 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★★ dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.4 | 1,876,119b
2026-02-24 02:50:03.657 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [239][de] '★★★★★ dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.4 | imgs=8
2026-02-24 02:50:03.657 | INFO     | app.scraper_service:scrape_one:367 -   → [239] Idioma [fr]: https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.fr.html
2026-02-24 02:50:03.657 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.fr.html (intento 1)
2026-02-24 02:50:30.881 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:50:30.883 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:50:42.367 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:51:01.266 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:51:01.267 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:51:31.624 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:51:31.626 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:51:35.923 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male (precios actualizados 2026)' | 1,876,781 bytes
2026-02-24 02:51:36.069 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:51:36.284 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 02:51:36.285 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 02:51:36.286 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 02:51:36.286 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★★ dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.4 | 1,876,781b
2026-02-24 02:51:36.305 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [239][fr] '★★★★★ dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.4 | imgs=8
2026-02-24 02:51:36.305 | INFO     | app.scraper_service:scrape_one:367 -   → [239] Idioma [it]: https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.it.html
2026-02-24 02:51:36.306 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.it.html (intento 1)
2026-02-24 02:52:01.984 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:52:01.985 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:52:14.530 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:52:32.339 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:52:32.341 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:53:02.722 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:53:02.725 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:53:08.147 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male (precios actualizados 2026)' | 1,876,819 bytes
2026-02-24 02:53:08.316 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:53:08.565 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 02:53:08.565 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 02:53:08.567 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 02:53:08.567 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★★ dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.4 | 1,876,819b
2026-02-24 02:53:08.585 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [239][it] '★★★★★ dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.4 | imgs=8
2026-02-24 02:53:10.925 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 239
2026-02-24 02:53:10.940 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [239] COMPLETADO | '★★★★★ dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | 5/5 idiomas | 466.1s
2026-02-24 02:53:10.942 | INFO     | app.scraper_service:scrape_one:314 -
────────────────────────────────────────────────────────────
2026-02-24 02:53:10.943 | INFO     | app.scraper_service:scrape_one:315 - 🏨 Iniciando scraping | ID=240 | https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.html
2026-02-24 02:53:10.944 | INFO     | app.scraper_service:scrape_one:316 - ────────────────────────────────────────────────────────────
2026-02-24 02:53:10.944 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:53:10.944 | INFO     | app.scraper:__new__:688 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-24 02:53:12.583 | SUCCESS  | app.scraper:_try_brave:421 - ✓ Brave iniciado
2026-02-24 02:53:12.583 | INFO     | app.scraper_service:scrape_one:367 -   → [240] Idioma [en]: https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.html
2026-02-24 02:53:12.584 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.html (intento 1)
2026-02-24 02:53:33.305 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:53:33.308 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:53:51.311 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:54:03.663 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:54:03.665 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:54:34.015 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:54:34.017 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:54:44.909 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri (precios actualizados 2026)' | 1,949,473 bytes
2026-02-24 02:54:45.037 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:54:45.210 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-24 02:54:45.211 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-24 02:54:45.213 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [en]
2026-02-24 02:54:45.213 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★★ Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | 1,949,473b
2026-02-24 02:54:45.230 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [240][en] '★★★★★ Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | imgs=8
2026-02-24 02:54:45.241 | DEBUG    | app.scraper_service:_download_images:664 -   📷 [240] 12 cookies extraídas del browser
2026-02-24 02:54:45.242 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-24 02:54:45.243 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=240 lang=en
2026-02-24 02:54:45.749 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_e45aac14347c.jpg (115,902 bytes, 1280×853)
2026-02-24 02:54:45.764 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_53c185ab71e5.jpg (116,339 bytes, 1280×853)
2026-02-24 02:54:45.781 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_ce0d6df9cfbb.jpg (134,401 bytes, 1280×853)
2026-02-24 02:54:45.813 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_7a17d0234815.jpg (158,115 bytes, 1280×853)
2026-02-24 02:54:45.926 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_2582f0a76ac3.jpg (131,881 bytes, 1280×853)
2026-02-24 02:54:45.936 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_10ade5ee3218.jpg (152,566 bytes, 1043×900)
2026-02-24 02:54:46.006 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_132c94ad9349.jpg (163,159 bytes, 1280×853)
2026-02-24 02:54:46.442 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_af47a57ee849.jpg (157,653 bytes, 1280×853)
2026-02-24 02:54:46.443 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-24 02:54:46.444 | INFO     | app.scraper_service:_download_images:671 -   📷 [240] 8/8 imágenes descargadas
2026-02-24 02:54:46.445 | DEBUG    | app.scraper_service:scrape_one:419 -   📷 [240] Imagenes marcadas como descargadas
2026-02-24 02:54:46.445 | INFO     | app.scraper_service:scrape_one:367 -   → [240] Idioma [es]: https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.es.html
2026-02-24 02:54:46.446 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.es.html (intento 1)
2026-02-24 02:55:04.440 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:55:04.441 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:55:25.583 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:55:34.869 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:55:34.871 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:56:05.227 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:56:05.290 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:56:19.133 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri (precios actualizados 2026)' | 1,939,994 bytes
2026-02-24 02:56:19.266 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:56:19.420 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-24 02:56:19.420 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [es]: ['rating_category', 'rooms']
2026-02-24 02:56:19.422 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [es]
2026-02-24 02:56:19.422 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★★ Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | 1,939,994b
2026-02-24 02:56:19.441 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [240][es] '★★★★★ Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | imgs=8
2026-02-24 02:56:19.442 | INFO     | app.scraper_service:scrape_one:367 -   → [240] Idioma [de]: https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.de.html
2026-02-24 02:56:19.442 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.de.html (intento 1)
2026-02-24 02:56:35.632 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:56:35.634 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:56:57.394 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:57:06.015 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:57:06.017 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:57:36.347 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:57:36.410 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:57:50.981 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri (precios actualizados 2026)' | 1,947,309 bytes
2026-02-24 02:57:51.141 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:57:51.299 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-24 02:57:51.299 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-24 02:57:51.301 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [de]
2026-02-24 02:57:51.301 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★★ Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | 1,947,309b
2026-02-24 02:57:51.347 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [240][de] '★★★★★ Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | imgs=8
2026-02-24 02:57:51.347 | INFO     | app.scraper_service:scrape_one:367 -   → [240] Idioma [fr]: https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.fr.html
2026-02-24 02:57:51.349 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.fr.html (intento 1)
2026-02-24 02:58:06.735 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:58:06.738 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:58:29.846 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 02:58:37.065 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:58:37.067 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:59:07.392 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:59:07.394 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 02:59:23.462 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri (precios actualizados 2026)' | 1,946,651 bytes
2026-02-24 02:59:23.613 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 02:59:23.774 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-24 02:59:23.775 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-24 02:59:23.776 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [fr]
2026-02-24 02:59:23.776 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★★ Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | 1,946,651b
2026-02-24 02:59:23.796 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [240][fr] '★★★★★ Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | imgs=8
2026-02-24 02:59:23.796 | INFO     | app.scraper_service:scrape_one:367 -   → [240] Idioma [it]: https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.it.html
2026-02-24 02:59:23.797 | INFO     | app.scraper:scrape_hotel:463 - 🔍 [Selenium] https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.it.html (intento 1)
2026-02-24 02:59:37.720 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 02:59:37.721 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:00:00.857 | DEBUG    | app.scraper:_wait_for_hotel_content:600 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-24 03:00:08.145 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:00:08.147 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:00:38.529 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:00:38.530 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:00:54.463 | DEBUG    | app.scraper:scrape_hotel:494 -   📄 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri (precios actualizados 2026)' | 1,947,049 bytes
2026-02-24 03:00:54.584 | DEBUG    | app.extractor:extract_name:232 -   Nombre extraído vía: og:title
2026-02-24 03:00:54.739 | DEBUG    | app.extractor:extract_images:877 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-24 03:00:54.740 | DEBUG    | app.extractor:extract_all:211 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-24 03:00:54.741 | DEBUG    | app.extractor:extract_all:214 -   [extractor] 8 imagenes extraidas [it]
2026-02-24 03:00:54.741 | SUCCESS  | app.scraper:scrape_hotel:512 -   ✓ '★★★★★ Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | 1,947,049b
2026-02-24 03:00:54.760 | SUCCESS  | app.scraper_service:scrape_one:398 -   ✓ [240][it] '★★★★★ Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | imgs=8
2026-02-24 03:00:57.109 | DEBUG    | app.scraper_service:scrape_one:487 -   ✓ Driver Selenium cerrado para hotel 240
2026-02-24 03:00:57.123 | SUCCESS  | app.scraper_service:scrape_one:514 - ✅ [240] COMPLETADO | '★★★★★ Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | 5/5 idiomas | 466.2s
2026-02-24 03:01:08.873 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:01:08.875 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:01:39.220 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:01:39.222 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:02:09.582 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:02:09.584 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:02:39.942 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:02:39.944 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:03:10.294 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:03:10.295 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:03:40.654 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:03:40.656 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:04:10.995 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:04:10.997 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:04:41.322 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:04:41.324 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:05:11.718 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:05:11.720 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:05:42.114 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:05:42.116 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:06:12.469 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:06:12.471 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:06:42.800 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:06:42.801 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:07:13.139 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:07:13.141 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:07:43.471 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:07:43.473 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:08:13.811 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:08:13.813 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:08:44.146 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:08:44.148 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:09:14.502 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:09:14.504 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:09:44.834 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:09:44.835 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:10:15.236 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:10:15.238 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:10:45.662 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:10:45.664 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:11:16.014 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:11:16.016 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:11:46.334 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:11:46.336 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:12:16.681 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:12:16.683 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:12:47.041 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:12:47.043 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:13:17.393 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:13:17.394 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:13:47.773 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:13:47.775 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:14:18.158 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:14:18.160 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:14:48.502 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:14:48.504 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:15:18.929 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:15:18.931 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:15:49.359 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:15:49.361 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:16:19.730 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:16:19.731 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:16:50.091 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:16:50.093 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:17:20.447 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:17:20.449 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:17:50.797 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:17:50.799 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:18:21.154 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:18:21.155 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:18:51.502 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:18:51.504 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:19:21.845 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:19:21.847 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:19:52.207 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:19:52.209 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:20:22.640 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:20:22.642 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:20:53.081 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:20:53.083 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:21:23.431 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:21:23.433 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:21:53.793 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:21:53.795 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:22:24.318 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:22:24.320 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:22:54.689 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:22:54.691 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:23:25.043 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:23:25.045 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:23:55.393 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:23:55.395 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:24:25.753 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:24:25.755 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:24:56.107 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:24:56.109 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:25:26.573 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:25:26.575 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:25:57.004 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:25:57.006 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:26:27.359 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:26:27.360 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:26:57.703 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:26:57.705 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:27:28.050 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:27:28.052 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:27:58.398 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:27:58.400 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:28:28.739 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:28:28.740 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:28:59.102 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:28:59.104 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:29:29.459 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:29:29.461 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:29:59.838 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:29:59.840 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:30:30.264 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:30:30.266 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:31:00.699 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:31:00.701 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:31:31.051 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:31:31.053 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:32:01.407 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:32:01.408 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:32:31.759 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:32:31.761 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:33:02.129 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:33:02.131 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:33:32.484 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:33:32.486 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:34:02.856 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:34:02.857 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:34:33.239 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:34:33.241 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:35:03.600 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:35:03.602 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:35:34.044 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:35:34.046 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:36:04.479 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:36:04.481 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:36:34.836 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:36:34.837 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:37:05.190 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:37:05.192 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:37:35.552 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:37:35.554 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:38:05.915 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:38:05.917 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:38:36.268 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:38:36.270 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:39:06.616 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:39:06.618 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:39:36.957 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:39:36.959 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:40:07.320 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:40:07.322 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:40:37.748 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:40:37.750 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:41:08.170 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:41:08.172 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:41:38.545 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:41:38.547 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:42:08.908 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:42:08.910 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:42:39.254 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:42:39.255 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:43:09.579 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:43:09.581 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:43:39.900 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:43:39.902 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:44:10.248 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:44:10.250 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:44:40.581 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:44:40.582 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:45:10.927 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:45:10.929 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:45:41.338 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:45:41.339 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:46:11.820 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:46:11.822 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:46:42.162 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:46:42.164 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:47:12.510 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:47:12.512 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:47:42.864 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:47:42.866 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:48:13.200 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:48:13.202 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:48:43.550 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:48:43.551 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:49:13.893 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:49:13.894 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:49:44.228 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:49:44.230 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:50:14.571 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:50:14.573 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:50:44.974 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:50:44.976 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:51:15.371 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:51:15.372 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:51:45.698 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:51:45.700 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:52:16.042 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:52:16.044 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:52:46.373 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:52:46.375 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:53:16.696 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:53:16.698 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:53:47.022 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:53:47.023 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:54:17.355 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:54:17.356 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:54:47.677 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:54:47.679 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:55:18.016 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:55:18.018 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:55:48.430 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:55:48.434 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:56:18.859 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:56:18.928 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:56:49.273 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:56:49.275 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:57:19.615 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:57:19.617 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:57:49.950 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:57:50.013 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:58:20.363 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:58:20.365 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:58:50.686 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:58:50.688 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:59:21.034 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:59:21.035 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 03:59:51.377 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 03:59:51.379 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:00:21.714 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:00:21.716 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:00:52.134 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:00:52.135 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:01:22.541 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:01:22.543 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:01:52.860 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:01:52.862 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:02:23.183 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:02:23.185 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:02:53.528 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:02:53.530 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:03:23.915 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:03:23.917 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:03:54.249 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:03:54.250 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:04:24.598 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:04:24.599 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:04:54.954 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:04:54.956 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:05:25.275 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:05:25.277 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:05:55.684 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:05:55.685 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:06:26.080 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:06:26.082 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:06:56.403 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:06:56.405 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:07:26.742 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:07:26.744 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:07:57.073 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:07:57.075 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:08:27.433 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:08:27.434 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:08:57.767 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:08:57.768 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:09:28.088 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:09:28.090 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:09:58.427 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:09:58.430 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:10:28.760 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:10:28.762 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:10:59.162 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:10:59.164 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:11:29.572 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:11:29.574 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:11:59.934 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:11:59.936 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:12:30.273 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:12:30.275 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:13:00.641 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:13:00.643 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:13:30.986 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:13:30.987 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:14:01.332 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:14:01.334 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:14:31.683 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:14:31.685 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:15:02.042 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:15:02.043 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:15:32.366 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:15:32.367 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:16:02.773 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:16:02.775 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:16:33.167 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:16:33.169 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:17:03.521 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:17:03.523 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:17:33.858 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:17:33.860 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:18:04.216 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:18:04.218 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:18:34.567 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:18:34.569 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:19:04.932 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:19:04.934 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:19:35.268 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:19:35.269 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:20:05.606 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:20:05.608 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:20:35.945 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:20:35.947 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:21:06.369 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:21:06.371 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:21:36.768 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:21:36.770 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:22:07.100 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:22:07.102 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:22:37.422 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:22:37.424 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:23:07.747 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:23:07.749 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:23:38.087 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:23:38.089 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:24:08.434 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:24:08.436 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:24:38.769 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:24:38.770 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:25:09.114 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:25:09.116 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:25:39.447 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:25:39.449 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:26:09.841 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:26:09.843 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:26:40.255 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:26:40.256 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:27:10.596 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:27:10.598 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:27:40.918 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:27:40.920 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:28:11.260 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:28:11.262 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:28:41.585 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:28:41.587 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:29:11.921 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:29:11.923 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:29:42.259 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:29:42.261 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:30:12.583 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:30:12.585 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:30:42.929 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:30:42.931 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:31:13.325 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:31:13.327 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:31:43.739 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:31:43.741 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:32:14.097 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:32:14.099 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:32:44.440 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:32:44.441 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:33:14.768 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:33:14.770 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:33:45.099 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:33:45.101 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:34:15.466 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:34:15.468 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:34:45.804 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:34:45.806 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:35:16.130 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:35:16.132 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:35:46.485 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:35:46.487 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:36:16.888 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:36:16.890 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:36:47.295 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:36:47.296 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:37:17.636 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:37:17.638 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:37:47.976 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:37:47.978 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:38:18.312 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:38:18.314 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:38:48.651 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:38:48.653 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:39:19.008 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:39:19.009 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:39:49.352 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:39:49.354 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:40:19.697 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:40:19.698 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:40:50.042 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:40:50.044 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:41:20.448 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:41:20.450 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:41:50.843 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:41:50.845 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:42:21.185 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:42:21.187 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:42:51.532 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:42:51.534 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:43:21.873 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:43:21.875 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:43:52.220 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:43:52.222 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:44:22.549 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:44:22.550 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:44:52.875 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:44:52.877 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:45:23.220 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:45:23.222 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:45:53.550 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:45:53.552 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:46:23.949 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:46:23.950 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:46:54.385 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:46:54.386 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:47:24.722 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:47:24.723 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:47:55.051 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:47:55.053 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:48:25.392 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:48:25.394 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:48:55.730 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:48:55.732 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:49:26.064 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:49:26.065 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:49:56.394 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:49:56.396 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:50:26.735 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:50:26.737 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:50:57.068 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:50:57.070 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:51:27.478 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:51:27.480 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:51:57.891 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:51:57.893 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:52:28.258 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:52:28.260 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:52:58.578 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:52:58.579 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:53:28.912 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:53:28.914 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:53:59.240 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:53:59.242 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:54:29.567 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:54:29.569 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:54:59.894 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:54:59.896 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:55:30.233 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:55:30.235 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:56:00.572 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:56:00.574 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:56:30.964 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:56:30.966 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:57:01.373 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:57:01.449 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:57:31.780 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:57:31.782 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:58:02.106 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:58:02.108 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:58:32.447 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:58:32.508 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:59:02.832 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:59:02.834 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 04:59:33.167 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 04:59:33.169 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:00:03.501 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:00:03.502 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:00:33.828 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:00:33.829 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:01:04.169 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:01:04.171 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:01:34.569 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:01:34.571 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:02:04.995 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:02:04.997 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:02:35.332 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:02:35.333 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:03:05.672 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:03:05.674 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:03:36.004 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:03:36.006 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:04:06.335 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:04:06.337 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:04:36.661 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:04:36.663 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:05:07.000 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:05:07.002 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:05:37.328 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:05:37.330 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:06:07.680 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:06:07.682 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:06:38.069 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:06:38.071 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:07:08.491 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:07:08.493 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:07:38.823 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:07:38.825 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:08:09.161 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:08:09.163 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:08:39.519 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:08:39.521 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:09:09.866 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:09:09.867 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:09:40.202 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:09:40.204 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:10:10.527 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:10:10.529 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:10:40.857 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:10:40.859 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:11:11.192 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:11:11.194 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:11:41.597 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:11:41.599 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:12:11.994 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:12:11.996 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:12:42.321 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:12:42.323 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:13:12.655 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:13:12.657 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:13:43.003 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:13:43.005 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:14:13.347 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:14:13.349 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:14:43.675 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:14:43.677 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:15:14.030 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:15:14.032 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:15:44.369 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:15:44.371 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:16:14.698 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:16:14.700 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:16:45.091 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:16:45.093 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:17:15.482 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:17:15.483 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:17:45.815 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:17:45.816 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:18:16.163 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:18:16.164 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:18:46.504 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:18:46.505 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:19:16.846 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:19:16.848 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:19:47.172 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:19:47.174 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:20:17.511 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:20:17.513 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:20:47.854 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:20:47.856 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:21:18.194 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:21:18.196 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:21:48.604 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:21:48.606 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:22:19.012 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:22:19.014 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:22:49.371 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:22:49.373 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:23:19.711 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:23:19.713 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:23:50.046 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:23:50.048 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:24:20.372 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:24:20.374 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:24:50.704 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:24:50.706 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:25:21.030 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:25:21.032 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:25:51.373 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:25:51.375 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:26:21.703 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:26:21.705 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:26:52.103 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:26:52.105 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:27:22.500 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:27:22.502 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:27:52.829 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:27:52.831 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:28:23.177 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:28:23.179 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:28:53.510 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:28:53.511 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:29:23.836 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:29:23.837 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:29:54.177 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:29:54.179 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:30:24.511 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:30:24.513 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:30:54.844 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:30:54.846 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:31:25.193 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:31:25.194 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:31:55.586 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:31:55.588 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:32:25.984 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:32:25.985 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:32:56.308 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:32:56.310 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:33:26.644 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:33:26.645 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:33:56.998 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:33:56.999 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:34:27.338 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:34:27.340 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:34:57.666 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:34:57.667 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:35:27.995 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:35:27.997 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:35:58.321 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:35:58.323 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:36:28.654 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:36:28.656 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:36:59.040 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:36:59.041 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:37:29.449 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:37:29.451 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:37:59.792 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:37:59.794 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:38:30.124 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:38:30.126 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:39:00.458 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:39:00.460 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:39:30.788 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:39:30.790 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:40:01.107 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:40:01.109 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:40:31.435 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:40:31.437 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:41:01.760 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:41:01.762 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:41:32.090 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:41:32.092 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:42:02.477 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:42:02.479 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:42:32.874 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:42:32.876 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:43:03.205 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:43:03.207 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:43:33.531 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:43:33.533 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:44:03.866 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:44:03.867 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:44:34.221 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:44:34.223 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:45:04.560 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:45:04.562 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:45:34.891 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:45:34.893 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:46:05.241 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:46:05.243 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:46:35.578 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:46:35.579 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:47:05.981 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:47:05.983 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:47:36.385 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:47:36.387 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:48:06.705 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:48:06.707 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:48:37.051 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:48:37.053 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:49:07.396 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:49:07.398 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:49:37.762 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:49:37.764 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:50:08.098 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:50:08.099 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:50:38.426 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:50:38.428 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:51:08.782 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:51:08.783 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:51:39.109 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:51:39.112 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:52:09.541 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:52:09.543 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:52:39.941 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:52:39.942 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:53:10.286 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:53:10.288 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:53:40.658 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:53:40.660 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:54:11.011 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:54:11.013 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:54:41.358 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:54:41.359 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:55:11.699 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:55:11.701 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:55:42.041 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:55:42.043 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:56:12.377 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:56:12.378 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:56:42.714 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:56:42.716 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:57:13.113 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:57:13.115 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:57:43.530 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:57:43.602 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:58:13.935 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:58:13.937 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:58:44.279 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:58:44.281 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:59:14.603 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:59:14.686 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 05:59:45.027 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 05:59:45.030 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:00:15.360 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:00:15.362 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:00:45.694 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:00:45.696 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:01:16.024 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:01:16.026 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:01:46.368 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:01:46.370 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:02:16.759 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:02:16.761 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:02:47.156 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:02:47.158 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:03:17.505 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:03:17.507 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:03:47.830 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:03:47.832 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:04:18.163 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:04:18.165 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:04:48.508 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:04:48.509 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:05:18.864 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:05:18.866 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:05:49.187 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:05:49.189 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:06:19.509 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:06:19.511 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:06:49.851 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:06:49.852 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:07:20.255 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:07:20.258 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:07:50.651 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:07:50.653 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:08:20.991 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:08:20.992 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:08:51.311 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:08:51.313 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:09:21.839 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:09:21.841 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:09:52.174 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:09:52.176 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:10:22.501 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:10:22.503 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:10:52.817 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:10:52.819 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:11:23.153 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:11:23.155 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:11:53.486 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:11:53.488 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:12:23.877 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:12:23.879 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:12:54.297 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:12:54.299 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:13:24.631 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:13:24.633 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:13:54.974 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:13:54.976 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:14:25.302 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:14:25.304 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:14:55.644 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:14:55.646 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:15:25.974 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:15:25.975 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:15:56.311 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:15:56.313 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:16:26.662 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:16:26.664 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:16:56.991 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:16:56.992 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:17:27.396 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:17:27.398 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:17:57.810 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:17:57.812 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:18:28.151 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:18:28.152 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:18:58.479 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:18:58.481 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:19:28.824 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:19:28.826 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:19:59.183 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:19:59.184 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:20:29.513 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:20:29.514 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:20:59.842 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:20:59.844 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:21:30.180 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:21:30.182 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:22:00.529 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:22:00.531 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:22:30.936 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:22:30.938 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:23:01.361 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:23:01.363 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:23:31.690 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:23:31.692 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:24:02.030 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:24:02.032 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:24:32.359 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:24:32.360 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:25:02.685 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:25:02.687 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:25:33.016 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:25:33.018 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:26:03.354 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:26:03.356 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:26:33.689 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:26:33.691 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:27:04.021 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:27:04.022 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
2026-02-24 06:27:34.412 | INFO     | app.vpn_manager_windows:verify_vpn_active:459 - ✓ VPN activa — IP: 194.34.233.13
2026-02-24 06:27:34.414 | DEBUG    | app.scraper_service:process_batch:233 - ℹ️ No hay URLs pendientes para despachar
