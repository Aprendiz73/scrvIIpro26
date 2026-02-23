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
[32mINFO[0m:     Started reloader process [[36m[1m15072[0m] using [36m[1mWatchFiles[0m
INFO:     Started server process [23236]
INFO:     Waiting for application startup.

============================================================
  BookingScraper Pro v2.1 - Iniciando
============================================================
2026-02-23 01:25:36.994 | SUCCESS  | app.database:test_connection:81 - ✓ Conexión a PostgreSQL exitosa
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

2026-02-23 01:25:37.000 | INFO     | app.main:_auto_dispatch_loop:61 - 🤖 Auto-dispatcher iniciado (ciclo 30s) — no requiere Celery

Current NordVPN version: 7.57.4.0

2026-02-23 01:25:38.160 | INFO     | app.vpn_manager_windows:_detect_method:111 - ✓ NordVPN CLI detectado
2026-02-23 01:25:38.531 | INFO     | app.vpn_manager_windows:_detect_original_ip:148 - IP original: 91.242.248.149
2026-02-23 01:25:38.532 | INFO     | app.vpn_manager_windows:__init__:91 - VPN Manager Windows inicializado | método=cli | interactive=False | sistema=10.0.26200
2026-02-23 01:25:38.532 | INFO     | app.scraper_service:_get_vpn_manager:84 - ✓ VPN Manager iniciado (singleton)
2026-02-23 01:25:38.532 | INFO     | app.main:_init_vpn:118 - 🔐 VPN iniciada al arrancar
INFO:     Application startup complete.
2026-02-23 01:25:42.015 | WARNING  | app.vpn_manager_windows:verify_vpn_active:456 - ⚠️ VPN inactiva | IP=91.242.248.149 == original=91.242.248.149
2026-02-23 01:25:42.015 | WARNING  | app.scraper_service:process_batch:189 - ⚠️ VPN inactiva al procesar batch — intentando conectar...
2026-02-23 01:25:42.016 | INFO     | app.vpn_manager_windows:connect:169 - Conectando a Germany (DE)...
2026-02-23 01:25:45.873 | INFO     | app.vpn_manager_windows:_connect_via_cli:202 - Conectando CLI a Germany...
2026-02-23 01:25:57.788 | ERROR    | app.vpn_manager_windows:_connect_via_cli:229 - ✗ VPN CLI conectó pero IP no cambió
2026-02-23 01:25:57.791 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
INFO:     127.0.0.1:60499 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:60499 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:60499 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:60499 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:56825 - "POST /urls/load HTTP/1.1" 200 OK
2026-02-23 01:26:28.215 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:26:28.234 | INFO     | app.scraper_service:process_batch:241 - 🚀 Despachadas 10 URLs al thread pool
2026-02-23 01:26:28.235 | INFO     | app.main:_auto_dispatch_loop:74 - 🤖 Auto-dispatch: 10 URLs enviadas al thread pool
2026-02-23 01:26:28.235 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 01:26:28.236 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=193 | https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.html
2026-02-23 01:26:28.236 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 01:26:28.236 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:26:28.247 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 01:26:33.323 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 01:26:33.324 | INFO     | app.scraper_service:scrape_one:325 -   → [193] Idioma [en]: https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.html
2026-02-23 01:26:33.325 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.html (intento 1)
2026-02-23 01:26:59.600 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:26:59.691 | INFO     | app.scraper_service:process_batch:241 - 🚀 Despachadas 6 URLs al thread pool
2026-02-23 01:26:59.692 | INFO     | app.main:_auto_dispatch_loop:74 - 🤖 Auto-dispatch: 6 URLs enviadas al thread pool
2026-02-23 01:27:17.251 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:27:30.041 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:27:30.043 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:28:00.395 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:28:00.397 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:28:10.932 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Gardens Hill Resort & Spa, Beau Vallon (precios actualizados 2026)' | 1,779,927 bytes
2026-02-23 01:28:11.642 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:28:11.840 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 01:28:11.841 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-23 01:28:11.843 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 01:28:11.843 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | 1,779,927b
2026-02-23 01:28:11.868 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [193][en] 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | imgs=8
2026-02-23 01:28:12.092 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [193] 12 cookies extraídas del browser
2026-02-23 01:28:12.093 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 01:28:12.095 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=193 lang=en
2026-02-23 01:28:13.113 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_106b1d98e88c.jpg (118,426 bytes, 1280×855)
2026-02-23 01:28:13.120 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_3b5e6cb74323.jpg (152,428 bytes, 1280×842)
2026-02-23 01:28:13.120 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_4384e2acb219.jpg (220,396 bytes, 1280×855)
2026-02-23 01:28:13.123 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_ef344d260f9f.jpg (175,879 bytes, 1280×855)
2026-02-23 01:28:13.129 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_4063ccc3381e.jpg (239,518 bytes, 1201×900)
2026-02-23 01:28:13.409 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_a90a53522b61.jpg (154,110 bytes, 1280×855)
2026-02-23 01:28:13.556 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_bebd502e1a3c.jpg (143,413 bytes, 1280×855)
2026-02-23 01:28:13.561 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_9764a811e6c3.jpg (153,382 bytes, 1280×833)
2026-02-23 01:28:13.563 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 01:28:13.564 | INFO     | app.scraper_service:_download_images:608 -   📷 [193] 8/8 imágenes descargadas
2026-02-23 01:28:13.565 | INFO     | app.scraper_service:scrape_one:325 -   → [193] Idioma [es]: https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.es.html
2026-02-23 01:28:13.565 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.es.html (intento 1)
2026-02-23 01:28:30.745 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:28:30.747 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:28:53.404 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:29:01.114 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:29:01.116 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:29:31.482 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:29:31.484 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:29:46.938 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Gardens Hill Resort & Spa, Beau Vallon (precios actualizados 2026)' | 1,778,357 bytes
2026-02-23 01:29:47.104 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:29:47.333 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 01:29:47.333 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-23 01:29:47.335 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 01:29:47.335 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | 1,778,357b
2026-02-23 01:29:47.367 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [193][es] 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | imgs=8
2026-02-23 01:29:47.367 | INFO     | app.scraper_service:scrape_one:325 -   → [193] Idioma [de]: https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.de.html
2026-02-23 01:29:47.368 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.de.html (intento 1)
2026-02-23 01:30:01.833 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:30:01.835 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:30:25.184 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:30:32.187 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:30:32.190 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:31:02.534 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:31:02.536 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:31:18.785 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Gardens Hill Resort & Spa, Beau Vallon (precios actualizados 2026)' | 1,700,707 bytes
2026-02-23 01:31:18.947 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:31:19.134 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 01:31:19.134 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-23 01:31:19.136 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 01:31:19.136 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | 1,700,707b
2026-02-23 01:31:19.169 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [193][de] 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | imgs=8
2026-02-23 01:31:19.169 | INFO     | app.scraper_service:scrape_one:325 -   → [193] Idioma [fr]: https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.fr.html
2026-02-23 01:31:19.170 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.fr.html (intento 1)
2026-02-23 01:31:32.969 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:31:32.971 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:31:58.610 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:32:03.417 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:32:03.419 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:32:33.771 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:32:33.773 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:32:52.153 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Gardens Hill Resort & Spa, Beau Vallon (precios actualizados 2026)' | 1,785,470 bytes
2026-02-23 01:32:52.354 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:32:52.647 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 01:32:52.648 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-23 01:32:52.650 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 01:32:52.650 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | 1,785,470b
2026-02-23 01:32:52.677 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [193][fr] 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | imgs=8
2026-02-23 01:32:52.678 | INFO     | app.scraper_service:scrape_one:325 -   → [193] Idioma [it]: https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.it.html
2026-02-23 01:32:52.680 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/garden-hill-resort-amp-spa.it.html (intento 1)
2026-02-23 01:33:04.114 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:33:04.116 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:33:32.751 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:33:34.574 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:33:34.576 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:34:05.644 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:34:05.646 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:34:26.388 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Gardens Hill Resort & Spa, Beau Vallon (precios actualizados 2026)' | 1,783,282 bytes
2026-02-23 01:34:26.550 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:34:26.778 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 01:34:26.778 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-23 01:34:26.789 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 01:34:26.790 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | 1,783,282b
2026-02-23 01:34:26.810 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [193][it] 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | rating=8.7 | imgs=8
2026-02-23 01:34:29.302 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 193
2026-02-23 01:34:29.316 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [193] COMPLETADO | 'Gardens Hill Resort & Spa, Beau Vallon, Seychelles' | 5/5 idiomas | 481.1s
2026-02-23 01:34:29.317 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 01:34:29.325 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=194 | https://www.booking.com/hotel/sc/cb-seychelles.html
2026-02-23 01:34:29.326 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 01:34:29.326 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:34:29.326 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 01:34:30.776 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 01:34:30.776 | INFO     | app.scraper_service:scrape_one:325 -   → [194] Idioma [en]: https://www.booking.com/hotel/sc/cb-seychelles.html
2026-02-23 01:34:30.778 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/cb-seychelles.html (intento 1)
2026-02-23 01:34:36.215 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:34:36.217 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:35:06.572 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:35:06.575 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:35:09.511 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:35:36.924 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:35:36.926 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:36:03.113 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cheval Blanc Seychelles, Mahé (precios actualizados 2026)' | 1,824,038 bytes
2026-02-23 01:36:03.236 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:36:03.433 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 01:36:03.434 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-23 01:36:03.461 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 01:36:03.480 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★★ Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | 1,824,038b
2026-02-23 01:36:03.519 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [194][en] '★★★★★ Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | imgs=8
2026-02-23 01:36:03.531 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [194] 12 cookies extraídas del browser
2026-02-23 01:36:03.532 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 01:36:03.533 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=194 lang=en
2026-02-23 01:36:04.070 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_c3efbc9c5587.jpg (121,576 bytes, 1280×719)
2026-02-23 01:36:04.135 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_6fc33e853a69.jpg (133,966 bytes, 1280×852)
2026-02-23 01:36:04.154 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_ef75b341d853.jpg (89,252 bytes, 1280×853)
2026-02-23 01:36:04.162 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_ba387a1a0b85.jpg (212,676 bytes, 1280×853)
2026-02-23 01:36:04.244 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_d6e4c11bef3a.jpg (170,252 bytes, 1280×853)
2026-02-23 01:36:04.437 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_a1636e9be478.jpg (317,873 bytes, 1200×900)
2026-02-23 01:36:04.441 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_ae740d8fd385.jpg (201,790 bytes, 1280×853)
2026-02-23 01:36:04.542 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_cb580cedf981.jpg (302,261 bytes, 1280×853)
2026-02-23 01:36:04.544 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 01:36:04.544 | INFO     | app.scraper_service:_download_images:608 -   📷 [194] 8/8 imágenes descargadas
2026-02-23 01:36:04.545 | INFO     | app.scraper_service:scrape_one:325 -   → [194] Idioma [es]: https://www.booking.com/hotel/sc/cb-seychelles.es.html
2026-02-23 01:36:04.545 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/cb-seychelles.es.html (intento 1)
2026-02-23 01:36:07.271 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:36:07.273 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:36:37.715 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:36:37.720 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:36:45.268 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:37:08.143 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:37:08.146 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:37:38.494 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:37:38.496 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:37:38.951 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cheval Blanc Seychelles, Mahé (precios actualizados 2026)' | 1,930,779 bytes
2026-02-23 01:37:39.116 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:37:39.335 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 01:37:39.335 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['rating_category', 'rooms']
2026-02-23 01:37:39.336 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 01:37:39.337 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★★ Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | 1,930,779b
2026-02-23 01:37:39.360 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [194][es] '★★★★★ Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | imgs=8
2026-02-23 01:37:39.361 | INFO     | app.scraper_service:scrape_one:325 -   → [194] Idioma [de]: https://www.booking.com/hotel/sc/cb-seychelles.de.html
2026-02-23 01:37:39.361 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/cb-seychelles.de.html (intento 1)
2026-02-23 01:38:08.850 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:38:08.852 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:38:19.826 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:38:39.195 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:38:39.197 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:39:09.548 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:39:09.550 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:39:13.459 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cheval Blanc Seychelles, Mahé (precios actualizados 2026)' | 1,937,535 bytes
2026-02-23 01:39:13.600 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:39:13.822 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 01:39:13.822 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-23 01:39:13.834 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 01:39:13.836 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★★ Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | 1,937,535b
2026-02-23 01:39:13.869 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [194][de] '★★★★★ Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | imgs=8
2026-02-23 01:39:13.870 | INFO     | app.scraper_service:scrape_one:325 -   → [194] Idioma [fr]: https://www.booking.com/hotel/sc/cb-seychelles.fr.html
2026-02-23 01:39:13.871 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/cb-seychelles.fr.html (intento 1)
2026-02-23 01:39:39.903 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:39:39.905 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:39:53.519 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:40:10.256 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:40:10.259 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:40:40.601 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:40:40.603 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:40:47.133 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cheval Blanc Seychelles, Mahé (precios actualizados 2026)' | 1,939,870 bytes
2026-02-23 01:40:47.313 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:40:47.659 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 01:40:47.659 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-23 01:40:47.660 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 01:40:47.660 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★★ Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | 1,939,870b
2026-02-23 01:40:47.680 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [194][fr] '★★★★★ Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | imgs=8
2026-02-23 01:40:47.681 | INFO     | app.scraper_service:scrape_one:325 -   → [194] Idioma [it]: https://www.booking.com/hotel/sc/cb-seychelles.it.html
2026-02-23 01:40:47.681 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/cb-seychelles.it.html (intento 1)
2026-02-23 01:41:10.953 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:41:10.955 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:41:27.860 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:41:41.407 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:41:41.409 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:42:11.844 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:42:11.846 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:42:21.504 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cheval Blanc Seychelles, Mahé (precios actualizados 2026)' | 1,939,934 bytes
2026-02-23 01:42:21.655 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:42:21.882 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 01:42:21.883 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-23 01:42:21.884 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 01:42:21.884 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★★ Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | 1,939,934b
2026-02-23 01:42:21.904 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [194][it] '★★★★★ Cheval Blanc Seychelles, Mahé, Seychelles' | rating=9.4 | imgs=8
2026-02-23 01:42:24.368 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 194
2026-02-23 01:42:24.383 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [194] COMPLETADO | '★★★★★ Cheval Blanc Seychelles, Mahé, Seychelles' | 5/5 idiomas | 475.1s
2026-02-23 01:42:24.384 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 01:42:24.387 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=195 | https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.html
2026-02-23 01:42:24.387 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 01:42:24.387 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:42:24.387 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 01:42:25.952 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 01:42:25.953 | INFO     | app.scraper_service:scrape_one:325 -   → [195] Idioma [en]: https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.html
2026-02-23 01:42:25.954 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.html (intento 1)
2026-02-23 01:42:42.226 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:42:42.230 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:43:02.277 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:43:12.584 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:43:12.586 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:43:42.934 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:43:42.936 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:43:46.642 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Avani+ Barbarons Seychelles, Grand'Anse (precios actualizados 2026)' | 1,880,149 bytes
2026-02-23 01:43:46.824 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:43:47.028 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 01:43:47.028 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-23 01:43:47.030 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 01:43:47.030 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | 1,880,149b
2026-02-23 01:43:47.051 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [195][en] '★★★★ Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | imgs=8
2026-02-23 01:43:47.063 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [195] 14 cookies extraídas del browser
2026-02-23 01:43:47.064 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 01:43:47.065 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=195 lang=en
2026-02-23 01:43:47.583 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_71259672c207.jpg (90,596 bytes, 1280×691)
2026-02-23 01:43:47.605 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_d41aa39ab96e.jpg (93,372 bytes, 1280×691)
2026-02-23 01:43:47.689 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_5de2ff92435b.jpg (142,746 bytes, 1280×691)
2026-02-23 01:43:47.699 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_fdd7b521fe15.jpg (186,574 bytes, 1280×691)
2026-02-23 01:43:47.720 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_803bfa7c4f5f.jpg (212,121 bytes, 1280×691)
2026-02-23 01:43:47.771 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_6fa6c43c50c4.jpg (103,020 bytes, 1280×691)
2026-02-23 01:43:47.854 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_85e4c2c3a976.jpg (109,283 bytes, 1280×691)
2026-02-23 01:43:47.858 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_b8e4876cc695.jpg (163,424 bytes, 1280×691)
2026-02-23 01:43:47.860 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 01:43:47.860 | INFO     | app.scraper_service:_download_images:608 -   📷 [195] 8/8 imágenes descargadas
2026-02-23 01:43:47.861 | INFO     | app.scraper_service:scrape_one:325 -   → [195] Idioma [es]: https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.es.html
2026-02-23 01:43:47.862 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.es.html (intento 1)
2026-02-23 01:44:13.282 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:44:13.284 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:44:27.778 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:44:43.619 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:44:43.621 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:45:13.978 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:45:13.980 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:45:21.519 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Avani+ Barbarons Seychelles, Grand'Anse (precios actualizados 2026)' | 1,955,447 bytes
2026-02-23 01:45:21.773 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:45:22.284 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 01:45:22.285 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['rating_category', 'rooms']
2026-02-23 01:45:22.288 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 01:45:22.288 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | 1,955,447b
2026-02-23 01:45:22.313 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [195][es] '★★★★ Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | imgs=8
2026-02-23 01:45:22.313 | INFO     | app.scraper_service:scrape_one:325 -   → [195] Idioma [de]: https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.de.html
2026-02-23 01:45:22.314 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.de.html (intento 1)
2026-02-23 01:45:44.357 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:45:44.359 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:46:00.631 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:46:14.712 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:46:14.714 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:46:45.144 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:46:45.146 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:46:54.259 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Avani+ Barbarons Seychelles, Grand'Anse (precios actualizados 2026)' | 1,962,296 bytes
2026-02-23 01:46:54.475 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:46:54.739 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 01:46:54.740 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-23 01:46:54.742 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 01:46:54.743 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | 1,962,296b
2026-02-23 01:46:54.767 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [195][de] '★★★★ Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | imgs=8
2026-02-23 01:46:54.768 | INFO     | app.scraper_service:scrape_one:325 -   → [195] Idioma [fr]: https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.fr.html
2026-02-23 01:46:54.768 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.fr.html (intento 1)
2026-02-23 01:47:15.908 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:47:15.909 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:47:32.757 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:47:46.282 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:47:46.283 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:48:16.647 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:48:16.649 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:48:26.266 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Avani+ Barbarons Seychelles, Grand'Anse (precios actualizados 2026)' | 1,968,976 bytes
2026-02-23 01:48:26.434 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:48:26.712 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 01:48:26.713 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-23 01:48:26.714 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 01:48:26.714 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | 1,968,976b
2026-02-23 01:48:26.735 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [195][fr] '★★★★ Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | imgs=8
2026-02-23 01:48:26.735 | INFO     | app.scraper_service:scrape_one:325 -   → [195] Idioma [it]: https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.it.html
2026-02-23 01:48:26.735 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/sc/avani-seychelles-barbarons-resort-amp-spa.it.html (intento 1)
2026-02-23 01:48:47.290 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:48:47.292 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:49:04.967 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:49:18.306 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:49:18.308 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:49:48.646 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:49:48.648 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:49:58.593 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Avani+ Barbarons Seychelles, Grand'Anse (precios actualizados 2026)' | 1,855,621 bytes
2026-02-23 01:49:58.764 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:49:59.018 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 01:49:59.019 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-23 01:49:59.021 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 01:49:59.021 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | 1,855,621b
2026-02-23 01:49:59.040 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [195][it] '★★★★ Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | rating=9.1 | imgs=8
2026-02-23 01:50:01.504 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 195
2026-02-23 01:50:01.518 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [195] COMPLETADO | '★★★★ Avani+ Barbarons Seychelles, Grand'Anse, Seychelles' | 5/5 idiomas | 457.1s
2026-02-23 01:50:01.519 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 01:50:01.519 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=196 | https://www.booking.com/hotel/bb/leroy.html
2026-02-23 01:50:01.519 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 01:50:01.522 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:50:01.522 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 01:50:03.266 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 01:50:03.266 | INFO     | app.scraper_service:scrape_one:325 -   → [196] Idioma [en]: https://www.booking.com/hotel/bb/leroy.html
2026-02-23 01:50:03.268 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/bb/leroy.html (intento 1)
2026-02-23 01:50:19.013 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:50:19.015 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:50:41.621 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:50:49.362 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:50:49.364 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:51:19.717 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:51:19.723 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:51:35.296 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Hôtel Le Roy, Christ Church (precios actualizados en 2026)' | 1,981,602 bytes
2026-02-23 01:51:35.459 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:51:35.647 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 01:51:35.648 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-23 01:51:35.659 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 01:51:35.659 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | 1,981,602b
2026-02-23 01:51:35.680 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [196][en] 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | imgs=8
2026-02-23 01:51:35.691 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [196] 12 cookies extraídas del browser
2026-02-23 01:51:35.693 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 01:51:35.694 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=196 lang=en
2026-02-23 01:51:36.064 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_100661c31d5e.jpg (24,693 bytes, 360×480)
2026-02-23 01:51:36.251 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_7aa7698e850b.jpg (125,679 bytes, 1280×853)
2026-02-23 01:51:36.334 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_3f640e2e2f4a.jpg (63,586 bytes, 675×900)
2026-02-23 01:51:36.353 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_294355900c02.jpg (167,745 bytes, 1200×900)
2026-02-23 01:51:36.361 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_250c87976845.jpg (208,234 bytes, 1200×900)
2026-02-23 01:51:36.368 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_61b67ea50277.jpg (76,364 bytes, 675×900)
2026-02-23 01:51:36.479 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_b71ac3954766.jpg (64,818 bytes, 600×800)
2026-02-23 01:51:36.493 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_8e87f8e913a8.jpg (176,490 bytes, 675×900)
2026-02-23 01:51:36.495 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 01:51:36.495 | INFO     | app.scraper_service:_download_images:608 -   📷 [196] 8/8 imágenes descargadas
2026-02-23 01:51:36.497 | INFO     | app.scraper_service:scrape_one:325 -   → [196] Idioma [es]: https://www.booking.com/hotel/bb/leroy.es.html
2026-02-23 01:51:36.497 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/bb/leroy.es.html (intento 1)
2026-02-23 01:51:50.146 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:51:50.147 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:52:14.247 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:52:20.563 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:52:20.565 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:52:50.905 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:52:50.907 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:53:07.851 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Hôtel Le Roy, Christ Church (precios actualizados en 2026)' | 1,979,250 bytes
2026-02-23 01:53:08.022 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:53:08.200 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 01:53:08.201 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-23 01:53:08.202 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 01:53:08.202 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | 1,979,250b
2026-02-23 01:53:08.228 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [196][es] 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | imgs=8
2026-02-23 01:53:08.228 | INFO     | app.scraper_service:scrape_one:325 -   → [196] Idioma [de]: https://www.booking.com/hotel/bb/leroy.de.html
2026-02-23 01:53:08.228 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/bb/leroy.de.html (intento 1)
2026-02-23 01:53:21.257 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:53:21.259 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:53:47.359 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:53:51.597 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:53:51.599 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:54:21.938 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:54:21.940 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:54:40.914 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Hôtel Le Roy, Christ Church (precios actualizados en 2026)' | 1,985,454 bytes
2026-02-23 01:54:41.073 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:54:41.261 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 01:54:41.261 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-23 01:54:41.263 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 01:54:41.263 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | 1,985,454b
2026-02-23 01:54:41.283 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [196][de] 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | imgs=8
2026-02-23 01:54:41.283 | INFO     | app.scraper_service:scrape_one:325 -   → [196] Idioma [fr]: https://www.booking.com/hotel/bb/leroy.fr.html
2026-02-23 01:54:41.283 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/bb/leroy.fr.html (intento 1)
2026-02-23 01:54:52.297 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:54:52.300 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:55:20.216 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:55:22.694 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:55:22.696 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:55:53.060 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:55:53.061 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:56:13.857 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Hôtel Le Roy, Christ Church (precios actualizados en 2026)' | 1,927,357 bytes
2026-02-23 01:56:14.028 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:56:14.190 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 01:56:14.190 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-23 01:56:14.192 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 01:56:14.192 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | 1,927,357b
2026-02-23 01:56:14.215 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [196][fr] 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | imgs=8
2026-02-23 01:56:14.215 | INFO     | app.scraper_service:scrape_one:325 -   → [196] Idioma [it]: https://www.booking.com/hotel/bb/leroy.it.html
2026-02-23 01:56:14.216 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/bb/leroy.it.html (intento 1)
2026-02-23 01:56:23.500 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:56:23.501 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:56:53.451 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:56:54.818 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:56:54.820 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:57:25.257 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:57:25.259 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:57:47.025 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Hôtel Le Roy, Christ Church (precios actualizados en 2026)' | 1,985,585 bytes
2026-02-23 01:57:47.185 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:57:47.486 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 01:57:47.486 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-23 01:57:47.488 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 01:57:47.488 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | 1,985,585b
2026-02-23 01:57:47.509 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [196][it] 'Hôtel Le Roy, Christ Church, Barbados' | rating=8.6 | imgs=8
2026-02-23 01:57:50.213 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 196
2026-02-23 01:57:50.226 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [196] COMPLETADO | 'Hôtel Le Roy, Christ Church, Barbados' | 5/5 idiomas | 468.7s
2026-02-23 01:57:50.227 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 01:57:50.227 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=197 | https://www.booking.com/hotel/bs/the-island-garden.html
2026-02-23 01:57:50.228 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 01:57:50.228 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:57:50.231 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 01:57:51.770 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 01:57:51.771 | INFO     | app.scraper_service:scrape_one:325 -   → [197] Idioma [en]: https://www.booking.com/hotel/bs/the-island-garden.html
2026-02-23 01:57:51.773 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/bs/the-island-garden.html (intento 1)
2026-02-23 01:57:55.684 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:57:55.686 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:58:26.037 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:58:26.038 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:58:28.945 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:58:56.374 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:58:56.376 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:59:13.045 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'The Island Garden Hotel, Nassau (precios actualizados en 2026)' | 1,369,436 bytes
2026-02-23 01:59:13.145 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 01:59:13.265 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 01:59:13.266 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-23 01:59:13.267 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 01:59:13.267 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | 1,369,436b
2026-02-23 01:59:13.284 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [197][en] 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | imgs=8
2026-02-23 01:59:13.316 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [197] 14 cookies extraídas del browser
2026-02-23 01:59:13.316 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 01:59:13.318 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=197 lang=en
2026-02-23 01:59:13.896 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_7d51a57a9fb6.jpg (160,171 bytes, 1200×900)
2026-02-23 01:59:13.970 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_7b0e28712af2.jpg (92,359 bytes, 900×900)
2026-02-23 01:59:14.013 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_04d08f5cb0f4.jpg (75,413 bytes, 1280×853)
2026-02-23 01:59:14.030 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_3bd1886b2b12.jpg (67,684 bytes, 900×900)
2026-02-23 01:59:14.123 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_2b44a7a04eef.jpg (29,666 bytes, 506×900)
2026-02-23 01:59:14.133 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_6d8ae04dc4a3.jpg (193,611 bytes, 1200×900)
2026-02-23 01:59:14.297 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_23347fdc4a1d.jpg (45,237 bytes, 900×900)
2026-02-23 01:59:14.319 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_f9981f676c90.jpg (49,348 bytes, 675×900)
2026-02-23 01:59:14.320 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 01:59:14.320 | INFO     | app.scraper_service:_download_images:608 -   📷 [197] 8/8 imágenes descargadas
2026-02-23 01:59:14.321 | INFO     | app.scraper_service:scrape_one:325 -   → [197] Idioma [es]: https://www.booking.com/hotel/bs/the-island-garden.es.html
2026-02-23 01:59:14.321 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/bs/the-island-garden.es.html (intento 1)
2026-02-23 01:59:27.093 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:59:27.095 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 01:59:52.643 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 01:59:57.447 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 01:59:57.450 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:00:27.815 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:00:27.817 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:00:46.255 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'The Island Garden Hotel, Nassau (precios actualizados en 2026)' | 1,338,970 bytes
2026-02-23 02:00:46.353 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:00:46.463 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 02:00:46.463 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-23 02:00:46.465 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 02:00:46.465 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | 1,338,970b
2026-02-23 02:00:46.482 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [197][es] 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | imgs=8
2026-02-23 02:00:46.482 | INFO     | app.scraper_service:scrape_one:325 -   → [197] Idioma [de]: https://www.booking.com/hotel/bs/the-island-garden.de.html
2026-02-23 02:00:46.482 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/bs/the-island-garden.de.html (intento 1)
2026-02-23 02:00:58.162 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:00:58.164 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:01:23.065 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:01:28.527 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:01:28.529 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:01:58.978 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:01:58.981 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:02:16.632 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'The Island Garden Hotel, Nassau (precios actualizados en 2026)' | 1,342,610 bytes
2026-02-23 02:02:16.732 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:02:16.857 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 02:02:16.858 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-23 02:02:16.859 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 02:02:16.859 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | 1,342,610b
2026-02-23 02:02:16.868 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [197][de] 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | imgs=8
2026-02-23 02:02:16.868 | INFO     | app.scraper_service:scrape_one:325 -   → [197] Idioma [fr]: https://www.booking.com/hotel/bs/the-island-garden.fr.html
2026-02-23 02:02:16.868 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/bs/the-island-garden.fr.html (intento 1)
2026-02-23 02:02:29.409 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:02:29.411 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:02:54.569 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:02:59.776 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:02:59.778 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:03:30.129 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:03:30.131 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:03:48.162 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'The Island Garden Hotel, Nassau (precios actualizados en 2026)' | 1,344,970 bytes
2026-02-23 02:03:48.260 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:03:48.405 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 02:03:48.405 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-23 02:03:48.407 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 02:03:48.407 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | 1,344,970b
2026-02-23 02:03:48.425 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [197][fr] 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | imgs=8
2026-02-23 02:03:48.426 | INFO     | app.scraper_service:scrape_one:325 -   → [197] Idioma [it]: https://www.booking.com/hotel/bs/the-island-garden.it.html
2026-02-23 02:03:48.426 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/bs/the-island-garden.it.html (intento 1)
2026-02-23 02:04:00.799 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:04:00.803 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:04:25.773 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:04:31.155 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:04:31.158 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:05:01.511 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:05:01.513 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:05:19.403 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'The Island Garden Hotel, Nassau (precios actualizados en 2026)' | 1,344,955 bytes
2026-02-23 02:05:19.501 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:05:19.616 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 02:05:19.616 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-23 02:05:19.618 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 02:05:19.618 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | 1,344,955b
2026-02-23 02:05:19.636 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [197][it] 'The Island Garden Hotel, Nassau, Bahamas' | rating=6.6 | imgs=8
2026-02-23 02:05:22.059 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 197
2026-02-23 02:05:22.073 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [197] COMPLETADO | 'The Island Garden Hotel, Nassau, Bahamas' | 5/5 idiomas | 451.8s
2026-02-23 02:05:22.075 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 02:05:22.077 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=198 | https://www.booking.com/hotel/tc/grace-bay-club.html
2026-02-23 02:05:22.077 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 02:05:22.077 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:05:22.078 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 02:05:23.783 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 02:05:23.784 | INFO     | app.scraper_service:scrape_one:325 -   → [198] Idioma [en]: https://www.booking.com/hotel/tc/grace-bay-club.html
2026-02-23 02:05:23.786 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/tc/grace-bay-club.html (intento 1)
2026-02-23 02:05:31.881 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:05:31.883 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:06:02.227 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:06:02.229 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:06:02.387 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:06:32.577 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:06:32.579 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:06:56.065 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Grace Bay Club, Grace Bay (precios actualizados en 2026)' | 2,576,983 bytes
2026-02-23 02:06:56.239 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:06:56.498 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 02:06:56.498 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:06:56.500 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 02:06:56.500 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | 2,576,983b
2026-02-23 02:06:56.520 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [198][en] 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | imgs=8
2026-02-23 02:06:56.531 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [198] 12 cookies extraídas del browser
2026-02-23 02:06:56.531 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 02:06:56.532 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=198 lang=en
2026-02-23 02:06:57.219 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_7f928c3061d7.jpg (193,123 bytes, 1280×854)
2026-02-23 02:06:57.295 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_764d8ab9a2e3.jpg (110,466 bytes, 1280×614)
2026-02-23 02:06:57.380 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_af0bf2c87017.jpg (175,683 bytes, 1280×852)
2026-02-23 02:06:57.441 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_6ad01b5b8bd5.jpg (208,280 bytes, 1240×900)
2026-02-23 02:06:57.449 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_fb703e094336.jpg (141,438 bytes, 1280×853)
2026-02-23 02:06:57.660 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_f2909cddf03b.jpg (172,682 bytes, 1280×853)
2026-02-23 02:06:57.695 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_1ef3c13f45a2.jpg (56,706 bytes, 709×900)
2026-02-23 02:06:57.814 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_e0515a7586b3.jpg (219,420 bytes, 1280×853)
2026-02-23 02:06:57.816 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 02:06:57.817 | INFO     | app.scraper_service:_download_images:608 -   📷 [198] 8/8 imágenes descargadas
2026-02-23 02:06:57.818 | INFO     | app.scraper_service:scrape_one:325 -   → [198] Idioma [es]: https://www.booking.com/hotel/tc/grace-bay-club.es.html
2026-02-23 02:06:57.818 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/tc/grace-bay-club.es.html (intento 1)
2026-02-23 02:07:03.010 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:07:03.012 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:07:33.431 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:07:33.433 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:07:39.283 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:08:03.776 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:08:03.778 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:08:32.949 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Grace Bay Club, Grace Bay (precios actualizados en 2026)' | 2,569,006 bytes
2026-02-23 02:08:33.164 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:08:33.484 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 02:08:33.485 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:08:33.486 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 02:08:33.486 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | 2,569,006b
2026-02-23 02:08:33.506 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [198][es] 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | imgs=8
2026-02-23 02:08:33.507 | INFO     | app.scraper_service:scrape_one:325 -   → [198] Idioma [de]: https://www.booking.com/hotel/tc/grace-bay-club.de.html
2026-02-23 02:08:33.507 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/tc/grace-bay-club.de.html (intento 1)
2026-02-23 02:08:34.117 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:08:34.119 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:09:04.461 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:09:04.463 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:09:14.184 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:09:34.806 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:09:34.808 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:10:05.151 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:10:05.153 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:10:07.738 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Grace Bay Club, Grace Bay (precios actualizados en 2026)' | 2,574,965 bytes
2026-02-23 02:10:07.914 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:10:08.195 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 02:10:08.195 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:10:08.197 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 02:10:08.197 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | 2,574,965b
2026-02-23 02:10:08.215 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [198][de] 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | imgs=8
2026-02-23 02:10:08.215 | INFO     | app.scraper_service:scrape_one:325 -   → [198] Idioma [fr]: https://www.booking.com/hotel/tc/grace-bay-club.fr.html
2026-02-23 02:10:08.218 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/tc/grace-bay-club.fr.html (intento 1)
2026-02-23 02:10:35.512 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:10:35.514 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:10:48.042 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:11:05.856 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:11:05.858 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:11:36.197 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:11:36.199 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:11:41.563 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Grace Bay Club, Grace Bay (precios actualizados en 2026)' | 2,574,945 bytes
2026-02-23 02:11:41.738 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:11:42.002 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 02:11:42.002 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:11:42.004 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 02:11:42.004 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | 2,574,945b
2026-02-23 02:11:42.025 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [198][fr] 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | imgs=8
2026-02-23 02:11:42.025 | INFO     | app.scraper_service:scrape_one:325 -   → [198] Idioma [it]: https://www.booking.com/hotel/tc/grace-bay-club.it.html
2026-02-23 02:11:42.028 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/tc/grace-bay-club.it.html (intento 1)
2026-02-23 02:12:06.814 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:12:06.816 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:12:21.909 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:12:37.238 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:12:37.241 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:13:07.585 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:13:07.586 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:13:15.474 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Grace Bay Club, Grace Bay (precios actualizados en 2026)' | 2,575,206 bytes
2026-02-23 02:13:15.655 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:13:15.919 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 02:13:15.920 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:13:15.921 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 02:13:15.921 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | 2,575,206b
2026-02-23 02:13:15.930 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [198][it] 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | rating=9.0 | imgs=8
2026-02-23 02:13:18.345 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 198
2026-02-23 02:13:18.359 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [198] COMPLETADO | 'Grace Bay Club, Grace Bay, Islas Turks y Caicos' | 5/5 idiomas | 476.3s
2026-02-23 02:13:18.360 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 02:13:18.363 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=199 | https://www.booking.com/hotel/tc/south-bank.html
2026-02-23 02:13:18.364 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 02:13:18.364 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:13:18.364 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 02:13:19.914 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 02:13:19.915 | INFO     | app.scraper_service:scrape_one:325 -   → [199] Idioma [en]: https://www.booking.com/hotel/tc/south-bank.html
2026-02-23 02:13:19.916 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/tc/south-bank.html (intento 1)
2026-02-23 02:13:37.936 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:13:37.938 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:13:58.431 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:14:08.286 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:14:08.288 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:14:38.679 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:14:38.681 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:14:52.026 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'South Bank, Long Bay Hills (precios actualizados 2026)' | 2,576,662 bytes
2026-02-23 02:14:52.211 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:14:52.487 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 02:14:52.487 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:14:52.489 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 02:14:52.490 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★★ South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | 2,576,662b
2026-02-23 02:14:52.512 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [199][en] '★★★★★ South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | imgs=8
2026-02-23 02:14:52.525 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [199] 12 cookies extraídas del browser
2026-02-23 02:14:52.526 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 02:14:52.527 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=199 lang=en
2026-02-23 02:14:53.237 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_dc1cdc54f407.jpg (223,612 bytes, 1200×900)
2026-02-23 02:14:53.259 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_9422fb3c823e.jpg (101,340 bytes, 1280×853)
2026-02-23 02:14:53.341 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_a58a3ebfc877.jpg (112,209 bytes, 1280×853)
2026-02-23 02:14:53.444 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_d5720df4d59e.jpg (168,622 bytes, 1280×853)
2026-02-23 02:14:53.485 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_0719ca1a0547.jpg (268,793 bytes, 1280×842)
2026-02-23 02:14:53.627 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_2ee520051eb6.jpg (143,000 bytes, 1280×853)
2026-02-23 02:14:53.676 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_525e2949ce6d.jpg (181,707 bytes, 1280×853)
2026-02-23 02:14:53.981 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_15e6c051541c.jpg (112,383 bytes, 1280×853)
2026-02-23 02:14:53.983 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 02:14:53.983 | INFO     | app.scraper_service:_download_images:608 -   📷 [199] 8/8 imágenes descargadas
2026-02-23 02:14:53.984 | INFO     | app.scraper_service:scrape_one:325 -   → [199] Idioma [es]: https://www.booking.com/hotel/tc/south-bank.es.html
2026-02-23 02:14:53.985 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/tc/south-bank.es.html (intento 1)
2026-02-23 02:15:09.023 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:15:09.025 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:15:33.536 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:15:39.374 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:15:39.376 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:16:09.734 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:16:09.736 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:16:27.184 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'South Bank, Long Bay Hills (precios actualizados 2026)' | 2,568,832 bytes
2026-02-23 02:16:27.384 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:16:27.644 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 02:16:27.644 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['facilities', 'rooms']
2026-02-23 02:16:27.646 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 02:16:27.646 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★★ South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | 2,568,832b
2026-02-23 02:16:27.667 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [199][es] '★★★★★ South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | imgs=8
2026-02-23 02:16:27.978 | INFO     | app.scraper_service:scrape_one:325 -   → [199] Idioma [de]: https://www.booking.com/hotel/tc/south-bank.de.html
2026-02-23 02:16:27.978 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/tc/south-bank.de.html (intento 1)
2026-02-23 02:16:40.074 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:16:40.078 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:17:07.398 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:17:10.508 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:17:10.510 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:17:40.929 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:17:40.931 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:18:00.933 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'South Bank, Long Bay Hills (precios actualizados 2026)' | 2,574,784 bytes
2026-02-23 02:18:01.088 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:18:01.295 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 02:18:01.295 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:18:01.297 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 02:18:01.297 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★★ South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | 2,574,784b
2026-02-23 02:18:01.316 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [199][de] '★★★★★ South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | imgs=8
2026-02-23 02:18:01.316 | INFO     | app.scraper_service:scrape_one:325 -   → [199] Idioma [fr]: https://www.booking.com/hotel/tc/south-bank.fr.html
2026-02-23 02:18:01.316 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/tc/south-bank.fr.html (intento 1)
2026-02-23 02:18:11.278 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:18:11.280 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:18:41.039 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:18:41.648 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:18:41.650 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:19:12.012 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:19:12.014 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:19:34.649 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'South Bank, Long Bay Hills (precios actualizados 2026)' | 2,574,733 bytes
2026-02-23 02:19:34.821 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:19:35.016 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 02:19:35.016 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:19:35.017 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 02:19:35.017 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★★ South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | 2,574,733b
2026-02-23 02:19:35.038 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [199][fr] '★★★★★ South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | imgs=8
2026-02-23 02:19:35.038 | INFO     | app.scraper_service:scrape_one:325 -   → [199] Idioma [it]: https://www.booking.com/hotel/tc/south-bank.it.html
2026-02-23 02:19:35.038 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/tc/south-bank.it.html (intento 1)
2026-02-23 02:19:42.358 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:19:42.360 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:20:12.716 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:20:12.718 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:20:14.405 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:20:43.066 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:20:43.067 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:21:08.019 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'South Bank, Long Bay Hills (precios actualizados 2026)' | 2,574,699 bytes
2026-02-23 02:21:08.190 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:21:08.397 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 02:21:08.397 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:21:08.399 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 02:21:08.399 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★★ South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | 2,574,699b
2026-02-23 02:21:08.418 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [199][it] '★★★★★ South Bank, Long Bay Hills, Islas Turks y Caicos' | rating=9.6 | imgs=8
2026-02-23 02:21:10.827 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 199
2026-02-23 02:21:10.840 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [199] COMPLETADO | '★★★★★ South Bank, Long Bay Hills, Islas Turks y Caicos' | 5/5 idiomas | 472.5s
2026-02-23 02:21:10.842 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 02:21:10.842 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=200 | https://www.booking.com/hotel/vc/the-pink-sands-club.html
2026-02-23 02:21:10.845 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 02:21:10.845 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:21:10.845 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 02:21:12.513 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 02:21:12.513 | INFO     | app.scraper_service:scrape_one:325 -   → [200] Idioma [en]: https://www.booking.com/hotel/vc/the-pink-sands-club.html
2026-02-23 02:21:12.516 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/vc/the-pink-sands-club.html (intento 1)
2026-02-23 02:21:13.413 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:21:13.415 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:21:43.798 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:21:43.800 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:21:50.857 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:22:14.217 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:22:14.219 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:22:44.418 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Mandarin Oriental, Canouan, Canouan (precios actualizados en 2026)' | 1,759,843 bytes
2026-02-23 02:22:44.552 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:22:44.744 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 02:22:44.744 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-23 02:22:44.744 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:22:44.746 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 02:22:44.746 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | 1,759,843b
2026-02-23 02:22:44.752 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:22:44.767 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [200][en] 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | imgs=8
2026-02-23 02:22:44.776 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [200] 12 cookies extraídas del browser
2026-02-23 02:22:44.777 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 02:22:44.778 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=200 lang=en
2026-02-23 02:22:45.395 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_2d2ff4f4723c.jpg (60,890 bytes, 600×900)
2026-02-23 02:22:45.510 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_15dc437fc51d.jpg (141,179 bytes, 1280×853)
2026-02-23 02:22:45.531 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_e980facea79e.jpg (133,223 bytes, 1280×853)
2026-02-23 02:22:45.563 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_78795924e441.jpg (177,600 bytes, 1201×900)
2026-02-23 02:22:45.573 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_810b7cccde88.jpg (145,297 bytes, 1280×853)
2026-02-23 02:22:45.897 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_c4f3de71ac58.jpg (140,782 bytes, 1272×900)
2026-02-23 02:22:45.912 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_6870ac56647a.jpg (118,515 bytes, 1280×853)
2026-02-23 02:22:46.004 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_9f3e0a88b1df.jpg (236,659 bytes, 1280×853)
2026-02-23 02:22:46.006 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 02:22:46.006 | INFO     | app.scraper_service:_download_images:608 -   📷 [200] 8/8 imágenes descargadas
2026-02-23 02:22:46.008 | INFO     | app.scraper_service:scrape_one:325 -   → [200] Idioma [es]: https://www.booking.com/hotel/vc/the-pink-sands-club.es.html
2026-02-23 02:22:46.008 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/vc/the-pink-sands-club.es.html (intento 1)
2026-02-23 02:23:15.100 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:23:15.102 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:23:26.035 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:23:45.440 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:23:45.443 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:24:15.786 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:24:15.788 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:24:19.524 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Mandarin Oriental, Canouan, Canouan (precios actualizados en 2026)' | 1,756,142 bytes
2026-02-23 02:24:19.665 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:24:19.842 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 02:24:19.842 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-23 02:24:19.844 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 02:24:19.844 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | 1,756,142b
2026-02-23 02:24:19.864 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [200][es] 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | imgs=8
2026-02-23 02:24:19.864 | INFO     | app.scraper_service:scrape_one:325 -   → [200] Idioma [de]: https://www.booking.com/hotel/vc/the-pink-sands-club.de.html
2026-02-23 02:24:19.864 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/vc/the-pink-sands-club.de.html (intento 1)
2026-02-23 02:24:46.141 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:24:46.143 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:24:57.350 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:25:16.501 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:25:16.503 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:25:46.855 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:25:46.928 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:25:50.903 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Mandarin Oriental, Canouan, Canouan (precios actualizados en 2026)' | 1,762,267 bytes
2026-02-23 02:25:51.060 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:25:51.280 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 02:25:51.281 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-23 02:25:51.283 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 02:25:51.283 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | 1,762,267b
2026-02-23 02:25:51.305 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [200][de] 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | imgs=8
2026-02-23 02:25:51.306 | INFO     | app.scraper_service:scrape_one:325 -   → [200] Idioma [fr]: https://www.booking.com/hotel/vc/the-pink-sands-club.fr.html
2026-02-23 02:25:51.306 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/vc/the-pink-sands-club.fr.html (intento 1)
2026-02-23 02:26:17.279 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:26:17.280 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:26:29.917 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:26:47.638 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:26:47.640 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:27:18.102 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:27:18.174 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:27:23.487 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Mandarin Oriental, Canouan, Canouan (precios actualizados en 2026)' | 1,762,221 bytes
2026-02-23 02:27:23.614 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:27:23.800 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 02:27:23.800 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rooms']
2026-02-23 02:27:23.801 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 02:27:23.801 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | 1,762,221b
2026-02-23 02:27:23.845 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [200][fr] 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | imgs=8
2026-02-23 02:27:23.845 | INFO     | app.scraper_service:scrape_one:325 -   → [200] Idioma [it]: https://www.booking.com/hotel/vc/the-pink-sands-club.it.html
2026-02-23 02:27:23.847 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/vc/the-pink-sands-club.it.html (intento 1)
2026-02-23 02:27:48.766 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:27:48.767 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:28:01.918 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:28:19.107 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:28:19.108 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:28:49.456 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:28:49.457 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:28:55.489 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Mandarin Oriental, Canouan, Canouan (precios actualizados en 2026)' | 1,762,264 bytes
2026-02-23 02:28:55.647 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:28:55.906 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 02:28:55.907 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-23 02:28:55.908 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 02:28:55.908 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | 1,762,264b
2026-02-23 02:28:55.920 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [200][it] 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | rating=7.1 | imgs=8
2026-02-23 02:28:58.346 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 200
2026-02-23 02:28:58.360 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [200] COMPLETADO | 'Mandarin Oriental, Canouan, Canouan, San Vicente y las Granadinas' | 5/5 idiomas | 467.5s
2026-02-23 02:28:58.361 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 02:28:58.365 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=201 | https://www.booking.com/hotel/mv/niyama-private-islands-maldives.html
2026-02-23 02:28:58.365 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 02:28:58.365 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:28:58.366 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 02:29:05.359 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 02:29:05.360 | INFO     | app.scraper_service:scrape_one:325 -   → [201] Idioma [en]: https://www.booking.com/hotel/mv/niyama-private-islands-maldives.html
2026-02-23 02:29:05.362 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/niyama-private-islands-maldives.html (intento 1)
2026-02-23 02:29:19.861 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:29:19.863 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:29:43.208 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:29:50.205 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:29:50.207 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:30:20.694 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:30:20.695 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:30:37.119 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Niyama Private Islands Maldives, Dhaalu Atoll (precios actualizados en 2026)' | 2,249,394 bytes
2026-02-23 02:30:37.458 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:30:37.921 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 02:30:37.922 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-23 02:30:37.923 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 02:30:37.924 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | 2,249,394b
2026-02-23 02:30:37.943 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [201][en] 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | imgs=8
2026-02-23 02:30:37.951 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [201] 12 cookies extraídas del browser
2026-02-23 02:30:37.952 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 02:30:37.953 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=201 lang=en
2026-02-23 02:30:38.477 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_c16a1c886e4b.jpg (95,865 bytes, 720×900)
2026-02-23 02:30:38.508 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_c069ba21948a.jpg (117,214 bytes, 1280×852)
2026-02-23 02:30:38.542 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_b1a4ac28381d.jpg (140,993 bytes, 1280×900)
2026-02-23 02:30:38.555 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_6a6aea4bc539.jpg (149,403 bytes, 1119×900)
2026-02-23 02:30:38.619 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_56eff861f222.jpg (218,942 bytes, 1201×900)
2026-02-23 02:30:38.759 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_9876171d2a55.jpg (155,879 bytes, 1280×900)
2026-02-23 02:30:38.922 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_5dd09569ff52.jpg (355,195 bytes, 1202×900)
2026-02-23 02:30:38.940 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_0f3a25dc7c7b.jpg (365,047 bytes, 1280×900)
2026-02-23 02:30:38.942 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 02:30:38.942 | INFO     | app.scraper_service:_download_images:608 -   📷 [201] 8/8 imágenes descargadas
2026-02-23 02:30:38.945 | INFO     | app.scraper_service:scrape_one:325 -   → [201] Idioma [es]: https://www.booking.com/hotel/mv/niyama-private-islands-maldives.es.html
2026-02-23 02:30:38.945 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/niyama-private-islands-maldives.es.html (intento 1)
2026-02-23 02:30:51.046 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:30:51.048 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:31:17.621 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:31:21.399 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:31:21.401 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:31:51.747 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:31:51.749 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:32:11.376 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Niyama Private Islands Maldives, Dhaalu Atoll (precios actualizados en 2026)' | 2,240,961 bytes
2026-02-23 02:32:11.572 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:32:11.828 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 02:32:11.829 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-23 02:32:11.830 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 02:32:11.830 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | 2,240,961b
2026-02-23 02:32:11.853 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [201][es] 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | imgs=8
2026-02-23 02:32:11.854 | INFO     | app.scraper_service:scrape_one:325 -   → [201] Idioma [de]: https://www.booking.com/hotel/mv/niyama-private-islands-maldives.de.html
2026-02-23 02:32:11.855 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/niyama-private-islands-maldives.de.html (intento 1)
2026-02-23 02:32:22.175 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:32:22.177 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:32:49.331 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:32:52.604 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:32:52.606 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:33:23.003 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:33:23.005 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:33:43.043 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Niyama Private Islands Maldives, Dhaalu Atoll (precios actualizados en 2026)' | 2,244,969 bytes
2026-02-23 02:33:43.265 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:33:43.544 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 02:33:43.544 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-23 02:33:43.545 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 02:33:43.546 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | 2,244,969b
2026-02-23 02:33:43.555 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [201][de] 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | imgs=8
2026-02-23 02:33:43.555 | INFO     | app.scraper_service:scrape_one:325 -   → [201] Idioma [fr]: https://www.booking.com/hotel/mv/niyama-private-islands-maldives.fr.html
2026-02-23 02:33:43.557 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/niyama-private-islands-maldives.fr.html (intento 1)
2026-02-23 02:33:53.374 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:33:53.376 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:34:21.801 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:34:23.733 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:34:23.735 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:34:54.106 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:34:54.108 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:35:15.482 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Niyama Private Islands Maldives, Dhaalu Atoll (precios actualizados en 2026)' | 2,247,438 bytes
2026-02-23 02:35:15.691 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:35:15.988 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 02:35:15.988 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-23 02:35:15.989 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 02:35:15.990 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | 2,247,438b
2026-02-23 02:35:16.009 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [201][fr] 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | imgs=8
2026-02-23 02:35:16.010 | INFO     | app.scraper_service:scrape_one:325 -   → [201] Idioma [it]: https://www.booking.com/hotel/mv/niyama-private-islands-maldives.it.html
2026-02-23 02:35:16.010 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/niyama-private-islands-maldives.it.html (intento 1)
2026-02-23 02:35:24.467 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:35:24.469 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:35:54.480 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:35:54.829 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:35:54.831 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:36:25.194 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:36:25.196 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:36:48.219 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Niyama Private Islands Maldives, Dhaalu Atoll (precios actualizados en 2026)' | 2,247,414 bytes
2026-02-23 02:36:48.431 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:36:48.719 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 02:36:48.720 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-23 02:36:48.722 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 02:36:48.722 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | 2,247,414b
2026-02-23 02:36:48.741 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [201][it] 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | rating=9.5 | imgs=8
2026-02-23 02:36:51.168 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 201
2026-02-23 02:36:51.183 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [201] COMPLETADO | 'Niyama Private Islands Maldives, Dhaalu Atoll, Maldivas' | 5/5 idiomas | 472.8s
2026-02-23 02:36:51.185 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 02:36:51.188 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=202 | https://www.booking.com/hotel/mv/ananea-madivaru-maldives.html
2026-02-23 02:36:51.188 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 02:36:51.188 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:36:51.188 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 02:36:52.764 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 02:36:52.764 | INFO     | app.scraper_service:scrape_one:325 -   → [202] Idioma [en]: https://www.booking.com/hotel/mv/ananea-madivaru-maldives.html
2026-02-23 02:36:52.767 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/ananea-madivaru-maldives.html (intento 1)
2026-02-23 02:36:55.800 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:36:55.803 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:37:26.232 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:37:26.234 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:37:31.639 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:37:56.673 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:37:56.675 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:38:25.229 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Ananea Madivaru Maldives, Toroka (precios actualizados 2026)' | 1,786,141 bytes
2026-02-23 02:38:25.387 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:38:25.581 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 02:38:25.581 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'rooms']
2026-02-23 02:38:25.583 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 02:38:25.583 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.8 | 1,786,141b
2026-02-23 02:38:25.603 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [202][en] 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.8 | imgs=8
2026-02-23 02:38:25.613 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [202] 12 cookies extraídas del browser
2026-02-23 02:38:25.613 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 02:38:25.615 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=202 lang=en
2026-02-23 02:38:26.168 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_7f7f5649a82b.jpg (102,424 bytes, 1280×720)
2026-02-23 02:38:26.172 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_f2f0c5cb9826.jpg (127,536 bytes, 1280×853)
2026-02-23 02:38:26.196 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_f7ad212d3fc5.jpg (119,502 bytes, 1280×853)
2026-02-23 02:38:26.205 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_0860c860648f.jpg (136,086 bytes, 1280×853)
2026-02-23 02:38:26.372 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_bde2e0cff14b.jpg (115,098 bytes, 1280×853)
2026-02-23 02:38:26.490 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_ea15bbacb1e8.jpg (220,036 bytes, 1280×853)
2026-02-23 02:38:26.535 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_d2100e5fc277.jpg (209,022 bytes, 1280×853)
2026-02-23 02:38:26.543 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_11e5ede835b0.jpg (135,276 bytes, 1280×853)
2026-02-23 02:38:26.545 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 02:38:26.545 | INFO     | app.scraper_service:_download_images:608 -   📷 [202] 8/8 imágenes descargadas
2026-02-23 02:38:26.546 | INFO     | app.scraper_service:scrape_one:325 -   → [202] Idioma [es]: https://www.booking.com/hotel/mv/ananea-madivaru-maldives.es.html
2026-02-23 02:38:26.546 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/ananea-madivaru-maldives.es.html (intento 1)
2026-02-23 02:38:27.028 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:38:27.030 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:38:57.390 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:38:57.392 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:39:04.762 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:39:27.837 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:39:27.839 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:39:58.186 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:39:58.188 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:39:58.421 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Ananea Madivaru Maldives, Toroka (precios actualizados 2026)' | 1,784,248 bytes
2026-02-23 02:39:58.557 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:39:58.755 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 02:39:58.756 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['rooms']
2026-02-23 02:39:58.757 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 02:39:58.757 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.8 | 1,784,248b
2026-02-23 02:39:58.776 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [202][es] 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.8 | imgs=8
2026-02-23 02:39:58.776 | INFO     | app.scraper_service:scrape_one:325 -   → [202] Idioma [de]: https://www.booking.com/hotel/mv/ananea-madivaru-maldives.de.html
2026-02-23 02:39:58.776 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/ananea-madivaru-maldives.de.html (intento 1)
2026-02-23 02:40:28.553 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:40:28.555 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:40:36.419 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:40:58.894 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:40:58.895 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:41:29.258 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:41:29.260 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:41:29.988 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Ananea Madivaru Maldives, Toroka (precios actualizados 2026)' | 1,789,117 bytes
2026-02-23 02:41:30.120 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:41:30.360 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 02:41:30.361 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-23 02:41:30.362 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 02:41:30.363 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.8 | 1,789,117b
2026-02-23 02:41:30.382 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [202][de] 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.8 | imgs=8
2026-02-23 02:41:30.382 | INFO     | app.scraper_service:scrape_one:325 -   → [202] Idioma [fr]: https://www.booking.com/hotel/mv/ananea-madivaru-maldives.fr.html
2026-02-23 02:41:30.382 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/ananea-madivaru-maldives.fr.html (intento 1)
2026-02-23 02:41:59.612 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:41:59.614 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:42:09.613 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:42:30.036 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:42:30.038 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:43:00.465 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:43:00.467 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:43:03.151 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Ananea Madivaru Maldives, Toroka (precios actualizados 2026)' | 1,791,439 bytes
2026-02-23 02:43:03.296 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:43:03.494 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 02:43:03.494 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-23 02:43:03.496 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 02:43:03.496 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.8 | 1,791,439b
2026-02-23 02:43:03.516 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [202][fr] 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.8 | imgs=8
2026-02-23 02:43:03.516 | INFO     | app.scraper_service:scrape_one:325 -   → [202] Idioma [it]: https://www.booking.com/hotel/mv/ananea-madivaru-maldives.it.html
2026-02-23 02:43:03.517 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/ananea-madivaru-maldives.it.html (intento 1)
2026-02-23 02:43:30.813 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:43:30.815 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:43:42.788 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:44:01.167 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:44:01.168 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:44:31.518 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:44:31.520 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:44:36.263 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Ananea Madivaru Maldives, Toroka (precios actualizados 2026)' | 1,789,052 bytes
2026-02-23 02:44:36.470 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:44:36.835 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 02:44:36.835 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'rooms']
2026-02-23 02:44:36.837 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 02:44:36.837 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.8 | 1,789,052b
2026-02-23 02:44:36.858 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [202][it] 'Ananea Madivaru Maldives, Toroka, Maldivas' | rating=8.8 | imgs=8
2026-02-23 02:44:39.474 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 202
2026-02-23 02:44:39.488 | INFO     | app.scraper_service:_maybe_rotate_vpn:159 - 🔄 Rotando VPN (motivo=periodica, fallos_consec=0, hoteles=10)...
2026-02-23 02:44:39.489 | INFO     | app.vpn_manager_windows:rotate:353 - 🔄 Rotando VPN...
2026-02-23 02:44:40.388 | INFO     | app.vpn_manager_windows:disconnect:328 - ✓ VPN desconectada (CLI)
2026-02-23 02:44:45.389 | INFO     | app.vpn_manager_windows:connect:169 - Conectando a Canada (CA)...
2026-02-23 02:44:49.245 | INFO     | app.vpn_manager_windows:_connect_via_cli:202 - Conectando CLI a Canada...
2026-02-23 02:45:01.159 | SUCCESS  | app.vpn_manager_windows:_connect_via_cli:226 - ✓ Conectado a Canada — IP: 217.216.97.27
2026-02-23 02:45:01.160 | SUCCESS  | app.vpn_manager_windows:rotate:373 - ✓ Rotación exitosa → Canada
2026-02-23 02:45:01.161 | SUCCESS  | app.scraper_service:_maybe_rotate_vpn:168 - ✓ VPN rotada → IP: 217.216.97.27
2026-02-23 02:45:01.161 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [202] COMPLETADO | 'Ananea Madivaru Maldives, Toroka, Maldivas' | 5/5 idiomas | 468.3s
2026-02-23 02:45:01.163 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 02:45:01.164 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=203 | https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.html
2026-02-23 02:45:01.164 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 02:45:01.164 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.97.27
2026-02-23 02:45:01.164 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 02:45:02.172 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:45:02.204 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:45:02.583 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 02:45:02.584 | INFO     | app.scraper_service:scrape_one:325 -   → [203] Idioma [en]: https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.html
2026-02-23 02:45:02.587 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.html (intento 1)
2026-02-23 02:45:32.755 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:45:32.758 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:45:44.557 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:46:03.270 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:46:03.273 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:46:33.815 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:46:33.817 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:46:38.211 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cocomo Maldives, Himmafushi (precios actualizados 2026)' | 1,644,592 bytes
2026-02-23 02:46:38.466 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:46:38.639 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 02:46:38.640 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:46:38.641 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 02:46:38.641 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.3 | 1,644,592b
2026-02-23 02:46:38.661 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [203][en] '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.3 | imgs=8
2026-02-23 02:46:38.669 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [203] 12 cookies extraídas del browser
2026-02-23 02:46:38.670 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 02:46:38.671 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=203 lang=en
2026-02-23 02:46:39.960 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_fb52ba10b612.jpg (47,922 bytes, 675×900)
2026-02-23 02:46:39.998 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_6720b23bba07.jpg (87,754 bytes, 1280×587)
2026-02-23 02:46:40.222 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_9f9751a498fb.jpg (208,689 bytes, 1280×853)
2026-02-23 02:46:40.236 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_b042e84a2533.jpg (157,926 bytes, 1280×853)
2026-02-23 02:46:40.253 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_88b26b6b1318.jpg (143,390 bytes, 1280×853)
2026-02-23 02:46:40.783 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_f8fbae44681e.jpg (61,345 bytes, 1280×463)
2026-02-23 02:46:41.067 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_3944c703f4d4.jpg (162,470 bytes, 1280×853)
2026-02-23 02:46:41.111 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_e803df097bfc.jpg (107,333 bytes, 1280×853)
2026-02-23 02:46:41.113 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 02:46:41.114 | INFO     | app.scraper_service:_download_images:608 -   📷 [203] 8/8 imágenes descargadas
2026-02-23 02:46:41.116 | INFO     | app.scraper_service:scrape_one:325 -   → [203] Idioma [es]: https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.es.html
2026-02-23 02:46:41.116 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.es.html (intento 1)
2026-02-23 02:47:04.480 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:47:04.482 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:47:22.278 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:47:35.174 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:47:35.176 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:48:05.732 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:48:05.734 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:48:15.877 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cocomo Maldives, Himmafushi (precios actualizados 2026)' | 1,636,869 bytes
2026-02-23 02:48:16.013 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:48:16.212 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 02:48:16.213 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:48:16.215 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 02:48:16.215 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.3 | 1,636,869b
2026-02-23 02:48:16.235 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [203][es] '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.3 | imgs=8
2026-02-23 02:48:16.235 | INFO     | app.scraper_service:scrape_one:325 -   → [203] Idioma [de]: https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.de.html
2026-02-23 02:48:16.236 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.de.html (intento 1)
2026-02-23 02:48:36.290 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:48:36.292 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:48:55.400 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:49:06.792 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:49:06.794 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:49:37.305 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:49:37.308 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:49:48.987 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cocomo Maldives, Himmafushi (precios actualizados 2026)' | 1,642,498 bytes
2026-02-23 02:49:49.155 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:49:49.318 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 02:49:49.318 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:49:49.320 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 02:49:49.320 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.3 | 1,642,498b
2026-02-23 02:49:49.345 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [203][de] '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.3 | imgs=8
2026-02-23 02:49:49.346 | INFO     | app.scraper_service:scrape_one:325 -   → [203] Idioma [fr]: https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.fr.html
2026-02-23 02:49:49.346 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.fr.html (intento 1)
2026-02-23 02:50:07.849 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:50:07.851 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:50:28.793 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:50:38.358 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:50:38.360 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:51:08.902 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:51:08.904 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:51:22.470 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cocomo Maldives, Himmafushi (precios actualizados 2026)' | 1,643,988 bytes
2026-02-23 02:51:22.737 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:51:22.901 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 02:51:22.901 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:51:22.903 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 02:51:22.903 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.3 | 1,643,988b
2026-02-23 02:51:22.912 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [203][fr] '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.3 | imgs=8
2026-02-23 02:51:22.912 | INFO     | app.scraper_service:scrape_one:325 -   → [203] Idioma [it]: https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.it.html
2026-02-23 02:51:22.912 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cocomo-maldives-k-himmafushi.it.html (intento 1)
2026-02-23 02:51:39.419 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:51:39.421 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:52:01.221 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:52:10.127 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:52:10.129 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:52:40.793 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:52:40.795 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:52:54.807 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cocomo Maldives, Himmafushi (precios actualizados 2026)' | 1,645,560 bytes
2026-02-23 02:52:54.957 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:52:55.209 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 02:52:55.209 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:52:55.211 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 02:52:55.211 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.3 | 1,645,560b
2026-02-23 02:52:55.228 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [203][it] '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | rating=9.3 | imgs=8
2026-02-23 02:52:57.661 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 203
2026-02-23 02:52:57.676 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [203] COMPLETADO | '★★★★ Cocomo Maldives, Himmafushi, Maldivas' | 5/5 idiomas | 476.5s
2026-02-23 02:52:57.678 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 02:52:57.682 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=204 | https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.html
2026-02-23 02:52:57.682 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 02:52:57.682 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:52:57.682 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 02:52:59.077 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 02:52:59.077 | INFO     | app.scraper_service:scrape_one:325 -   → [204] Idioma [en]: https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.html
2026-02-23 02:52:59.079 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.html (intento 1)
2026-02-23 02:53:11.347 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:53:11.351 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:53:41.899 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:53:41.901 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:53:42.045 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:54:12.488 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:54:12.490 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:54:35.656 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cheval Blanc Randheli, Maldives, Randheli (precios actualizados 2026)' | 1,684,610 bytes
2026-02-23 02:54:35.803 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:54:35.995 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 02:54:35.997 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:54:35.998 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 02:54:35.998 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | 1,684,610b
2026-02-23 02:54:36.019 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [204][en] 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | imgs=8
2026-02-23 02:54:36.073 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [204] 12 cookies extraídas del browser
2026-02-23 02:54:36.074 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 02:54:36.081 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=204 lang=en
2026-02-23 02:54:37.206 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_1161f041afee.jpg (214,274 bytes, 1200×900)
2026-02-23 02:54:37.609 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_dbfe223f3b49.jpg (115,426 bytes, 1280×853)
2026-02-23 02:54:37.635 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_42a1161c074f.jpg (130,203 bytes, 1200×900)
2026-02-23 02:54:37.656 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_e4c3374ed58e.jpg (168,169 bytes, 1200×900)
2026-02-23 02:54:37.673 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_bd14890af3b8.jpg (149,690 bytes, 1280×862)
2026-02-23 02:54:38.173 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_28b20c546b71.jpg (163,992 bytes, 1280×854)
2026-02-23 02:54:38.585 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_c72d0f079b7c.jpg (168,977 bytes, 1280×853)
2026-02-23 02:54:38.594 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_15a467481acd.jpg (156,576 bytes, 1280×853)
2026-02-23 02:54:38.595 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 02:54:38.596 | INFO     | app.scraper_service:_download_images:608 -   📷 [204] 8/8 imágenes descargadas
2026-02-23 02:54:38.596 | INFO     | app.scraper_service:scrape_one:325 -   → [204] Idioma [es]: https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.es.html
2026-02-23 02:54:38.597 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.es.html (intento 1)
2026-02-23 02:54:43.037 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:54:43.039 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:55:13.595 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:55:13.597 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:55:18.917 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:55:44.097 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:55:44.099 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:56:12.472 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cheval Blanc Randheli, Maldives, Randheli (precios actualizados 2026)' | 1,675,849 bytes
2026-02-23 02:56:12.637 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:56:12.836 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 02:56:12.837 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['facilities', 'rooms']
2026-02-23 02:56:12.838 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 02:56:12.838 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | 1,675,849b
2026-02-23 02:56:12.868 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [204][es] 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | imgs=8
2026-02-23 02:56:12.868 | INFO     | app.scraper_service:scrape_one:325 -   → [204] Idioma [de]: https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.de.html
2026-02-23 02:56:12.870 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.de.html (intento 1)
2026-02-23 02:56:14.639 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:56:14.641 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:56:45.588 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:56:45.589 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:56:52.181 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:57:16.278 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:57:16.280 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:57:46.419 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cheval Blanc Randheli, Maldives, Randheli (precios actualizados 2026)' | 1,699,255 bytes
2026-02-23 02:57:46.543 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:57:46.712 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 02:57:46.712 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'rooms']
2026-02-23 02:57:46.714 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 02:57:46.714 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | 1,699,255b
2026-02-23 02:57:46.732 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [204][de] 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | imgs=8
2026-02-23 02:57:46.732 | INFO     | app.scraper_service:scrape_one:325 -   → [204] Idioma [fr]: https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.fr.html
2026-02-23 02:57:46.733 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.fr.html (intento 1)
2026-02-23 02:57:47.028 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:57:47.030 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:58:17.575 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:58:17.577 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:58:25.055 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 02:58:48.128 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:58:48.129 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:59:18.606 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cheval Blanc Randheli, Maldives, Randheli (precios actualizados 2026)' | 1,682,304 bytes
2026-02-23 02:59:18.647 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:59:18.650 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:59:18.800 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 02:59:18.967 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 02:59:18.967 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'facilities', 'rooms']
2026-02-23 02:59:18.969 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 02:59:18.969 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | 1,682,304b
2026-02-23 02:59:18.986 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [204][fr] 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | imgs=8
2026-02-23 02:59:18.986 | INFO     | app.scraper_service:scrape_one:325 -   → [204] Idioma [it]: https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.it.html
2026-02-23 02:59:18.986 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/cheval-blanc-randheli-noonu-atoll.it.html (intento 1)
2026-02-23 02:59:49.200 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 02:59:49.202 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 02:59:56.492 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:00:19.747 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:00:19.749 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:00:50.112 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Cheval Blanc Randheli, Maldives, Randheli (precios actualizados 2026)' | 1,681,251 bytes
2026-02-23 03:00:50.218 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:00:50.328 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:00:50.397 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 03:00:50.398 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:00:50.399 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 03:00:50.399 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | 1,681,251b
2026-02-23 03:00:50.399 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:00:50.417 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [204][it] 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | rating=10.0 | imgs=8
2026-02-23 03:00:53.045 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 204
2026-02-23 03:00:53.059 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [204] COMPLETADO | 'Cheval Blanc Randheli, Maldives, Randheli, Maldivas' | 5/5 idiomas | 475.4s
2026-02-23 03:00:53.061 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 03:00:53.063 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=205 | https://www.booking.com/hotel/mv/icom-blue-seaview.html
2026-02-23 03:00:53.063 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 03:00:53.063 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:00:53.064 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 03:00:54.575 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 03:00:54.575 | INFO     | app.scraper_service:scrape_one:325 -   → [205] Idioma [en]: https://www.booking.com/hotel/mv/icom-blue-seaview.html
2026-02-23 03:00:54.577 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/icom-blue-seaview.html (intento 1)
2026-02-23 03:01:21.108 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:01:21.111 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:01:35.785 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:01:51.657 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:01:51.659 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:02:22.359 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:02:22.362 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:02:29.346 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'iCom Blue Seaview, Maafushi (precios actualizados en 2026)' | 1,836,048 bytes
2026-02-23 03:02:29.540 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:02:29.734 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 03:02:29.734 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:02:29.735 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 03:02:29.735 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | 1,836,048b
2026-02-23 03:02:29.756 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [205][en] 'iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | imgs=8
2026-02-23 03:02:30.346 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [205] 12 cookies extraídas del browser
2026-02-23 03:02:30.347 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 03:02:30.350 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=205 lang=en
2026-02-23 03:02:31.699 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_7ed313d40b2a.jpg (101,756 bytes, 1280×853)
2026-02-23 03:02:31.801 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_1b6b1641933a.jpg (122,378 bytes, 1200×900)
2026-02-23 03:02:31.891 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_aca18abe7430.jpg (195,868 bytes, 1280×720)
2026-02-23 03:02:32.121 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_e643ae694c2a.jpg (53,288 bytes, 675×900)
2026-02-23 03:02:32.429 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_9cb4697517f0.jpg (200,361 bytes, 1280×720)
2026-02-23 03:02:32.656 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_2a26dfce25d0.jpg (125,904 bytes, 1200×900)
2026-02-23 03:02:32.663 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_4e8501fddbae.jpg (102,723 bytes, 1280×854)
2026-02-23 03:02:32.857 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_9eac350b3a8a.jpg (120,656 bytes, 1280×854)
2026-02-23 03:02:32.915 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 03:02:32.916 | INFO     | app.scraper_service:_download_images:608 -   📷 [205] 8/8 imágenes descargadas
2026-02-23 03:02:32.917 | INFO     | app.scraper_service:scrape_one:325 -   → [205] Idioma [es]: https://www.booking.com/hotel/mv/icom-blue-seaview.es.html
2026-02-23 03:02:32.917 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/icom-blue-seaview.es.html (intento 1)
2026-02-23 03:02:53.016 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:02:53.019 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:03:14.531 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:03:23.557 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:03:23.559 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:03:54.069 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:03:54.070 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:04:08.068 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'iCom Blue Seaview, Maafushi (precios actualizados en 2026)' | 1,826,928 bytes
2026-02-23 03:04:08.233 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:04:08.502 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 03:04:08.502 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['facilities', 'rooms']
2026-02-23 03:04:08.503 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 03:04:08.504 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | 1,826,928b
2026-02-23 03:04:08.522 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [205][es] 'iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | imgs=8
2026-02-23 03:04:08.522 | INFO     | app.scraper_service:scrape_one:325 -   → [205] Idioma [de]: https://www.booking.com/hotel/mv/icom-blue-seaview.de.html
2026-02-23 03:04:08.522 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/icom-blue-seaview.de.html (intento 1)
2026-02-23 03:04:24.594 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:04:24.597 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:04:48.106 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:04:55.097 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:04:55.099 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:05:25.635 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:05:25.636 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:05:41.667 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'iCom Blue Seaview, Maafushi (precios actualizados en 2026)' | 1,833,837 bytes
2026-02-23 03:05:41.821 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:05:41.997 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 03:05:41.998 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:05:41.999 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 03:05:41.999 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | 1,833,837b
2026-02-23 03:05:42.017 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [205][de] 'iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | imgs=8
2026-02-23 03:05:42.017 | INFO     | app.scraper_service:scrape_one:325 -   → [205] Idioma [fr]: https://www.booking.com/hotel/mv/icom-blue-seaview.fr.html
2026-02-23 03:05:42.017 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/icom-blue-seaview.fr.html (intento 1)
2026-02-23 03:05:56.176 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:05:56.179 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:06:21.441 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:06:26.684 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:06:26.686 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:06:57.199 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:06:57.201 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:07:14.985 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'iCom Blue Seaview, Maafushi (precios actualizados en 2026)' | 1,833,587 bytes
2026-02-23 03:07:15.140 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:07:15.317 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 03:07:15.318 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:07:15.324 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 03:07:15.326 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | 1,833,587b
2026-02-23 03:07:15.345 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [205][fr] 'iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | imgs=8
2026-02-23 03:07:15.345 | INFO     | app.scraper_service:scrape_one:325 -   → [205] Idioma [it]: https://www.booking.com/hotel/mv/icom-blue-seaview.it.html
2026-02-23 03:07:15.345 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/icom-blue-seaview.it.html (intento 1)
2026-02-23 03:07:27.891 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:07:27.893 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:07:53.280 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:07:58.554 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:07:58.557 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:08:29.062 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:08:29.064 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:08:46.856 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'iCom Blue Seaview, Maafushi (precios actualizados en 2026)' | 1,833,326 bytes
2026-02-23 03:08:47.032 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:08:47.215 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 03:08:47.215 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:08:47.217 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 03:08:47.217 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | 1,833,326b
2026-02-23 03:08:47.236 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [205][it] 'iCom Blue Seaview, Maafushi, Maldivas' | rating=8.7 | imgs=8
2026-02-23 03:08:49.774 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 205
2026-02-23 03:08:49.789 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [205] COMPLETADO | 'iCom Blue Seaview, Maafushi, Maldivas' | 5/5 idiomas | 476.7s
2026-02-23 03:08:49.792 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 03:08:49.793 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=206 | https://www.booking.com/hotel/mv/eri-maldives.html
2026-02-23 03:08:49.793 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 03:08:49.793 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:08:49.794 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 03:08:51.500 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 03:08:51.501 | INFO     | app.scraper_service:scrape_one:325 -   → [206] Idioma [en]: https://www.booking.com/hotel/mv/eri-maldives.html
2026-02-23 03:08:51.503 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/eri-maldives.html (intento 1)
2026-02-23 03:08:59.912 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:08:59.914 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:09:30.436 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:09:30.438 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:09:35.975 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:10:00.941 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:10:00.943 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:10:29.534 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Eri Maldives, Atolón de Malé Norte (precios actualizados 2026)' | 1,565,641 bytes
2026-02-23 03:10:29.656 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:10:29.862 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 03:10:29.862 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:10:29.864 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 03:10:29.865 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | 1,565,641b
2026-02-23 03:10:29.882 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [206][en] '★★★★ Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | imgs=8
2026-02-23 03:10:29.890 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [206] 12 cookies extraídas del browser
2026-02-23 03:10:29.890 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 03:10:29.891 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=206 lang=en
2026-02-23 03:10:30.988 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_561a168f5a57.jpg (241,885 bytes, 1200×900)
2026-02-23 03:10:31.070 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_b04d8bee7ffd.jpg (95,537 bytes, 1280×818)
2026-02-23 03:10:31.389 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_2f5f08096fae.jpg (117,747 bytes, 1201×900)
2026-02-23 03:10:31.464 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_76f597b75325.jpg (130,703 bytes, 1280×853)
2026-02-23 03:10:31.476 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:10:31.477 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:10:31.485 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_83926d7eb940.jpg (175,897 bytes, 1200×900)
2026-02-23 03:10:31.913 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_ca1e4ea9c62c.jpg (111,399 bytes, 1125×900)
2026-02-23 03:10:31.974 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_985550f1c961.jpg (98,578 bytes, 675×900)
2026-02-23 03:10:32.382 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_bb8f9018ed16.jpg (131,286 bytes, 1197×900)
2026-02-23 03:10:32.384 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 03:10:32.385 | INFO     | app.scraper_service:_download_images:608 -   📷 [206] 8/8 imágenes descargadas
2026-02-23 03:10:32.386 | INFO     | app.scraper_service:scrape_one:325 -   → [206] Idioma [es]: https://www.booking.com/hotel/mv/eri-maldives.es.html
2026-02-23 03:10:32.386 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/eri-maldives.es.html (intento 1)
2026-02-23 03:11:01.980 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:11:01.981 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:11:12.412 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:11:32.486 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:11:32.488 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:12:03.033 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:12:03.035 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:12:06.029 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Eri Maldives, Atolón de Malé Norte (precios actualizados 2026)' | 1,556,515 bytes
2026-02-23 03:12:06.188 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:12:06.377 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 03:12:06.377 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:12:06.379 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 03:12:06.379 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | 1,556,515b
2026-02-23 03:12:06.399 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [206][es] '★★★★ Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | imgs=8
2026-02-23 03:12:06.399 | INFO     | app.scraper_service:scrape_one:325 -   → [206] Idioma [de]: https://www.booking.com/hotel/mv/eri-maldives.de.html
2026-02-23 03:12:06.399 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/eri-maldives.de.html (intento 1)
2026-02-23 03:12:33.732 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:12:33.734 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:12:44.125 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:13:04.423 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:13:04.425 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:13:34.940 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:13:34.942 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:13:37.737 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Eri Maldives, Atolón de Malé Norte (precios actualizados 2026)' | 1,563,104 bytes
2026-02-23 03:13:37.887 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:13:38.055 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 03:13:38.055 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:13:38.062 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 03:13:38.063 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | 1,563,104b
2026-02-23 03:13:38.089 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [206][de] '★★★★ Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | imgs=8
2026-02-23 03:13:38.090 | INFO     | app.scraper_service:scrape_one:325 -   → [206] Idioma [fr]: https://www.booking.com/hotel/mv/eri-maldives.fr.html
2026-02-23 03:13:38.090 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/eri-maldives.fr.html (intento 1)
2026-02-23 03:14:05.487 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:14:05.489 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:14:17.311 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:14:36.030 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:14:36.032 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:15:06.535 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:15:06.537 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:15:10.885 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Eri Maldives, Atolón de Malé Norte (precios actualizados 2026)' | 1,562,441 bytes
2026-02-23 03:15:11.098 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:15:11.255 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 03:15:11.255 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:15:11.257 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 03:15:11.257 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | 1,562,441b
2026-02-23 03:15:11.275 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [206][fr] '★★★★ Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | imgs=8
2026-02-23 03:15:11.276 | INFO     | app.scraper_service:scrape_one:325 -   → [206] Idioma [it]: https://www.booking.com/hotel/mv/eri-maldives.it.html
2026-02-23 03:15:11.276 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/eri-maldives.it.html (intento 1)
2026-02-23 03:15:37.029 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:15:37.031 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:15:55.418 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:16:07.579 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:16:07.581 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:16:38.116 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:16:38.118 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:16:48.917 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Eri Maldives, Atolón de Malé Norte (precios actualizados 2026)' | 1,563,390 bytes
2026-02-23 03:16:49.040 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:16:49.279 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 03:16:49.279 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:16:49.281 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 03:16:49.282 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ '★★★★ Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | 1,563,390b
2026-02-23 03:16:49.301 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [206][it] '★★★★ Eri Maldives, Atolón de Malé Norte, Maldivas' | rating=9.2 | imgs=8
2026-02-23 03:16:51.739 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 206
2026-02-23 03:16:51.753 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [206] COMPLETADO | '★★★★ Eri Maldives, Atolón de Malé Norte, Maldivas' | 5/5 idiomas | 482.0s
2026-02-23 03:16:51.755 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 03:16:51.757 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=207 | https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.html
2026-02-23 03:16:51.758 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 03:16:51.758 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:16:51.758 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 03:16:53.256 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 03:16:53.256 | INFO     | app.scraper_service:scrape_one:325 -   → [207] Idioma [en]: https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.html
2026-02-23 03:16:53.257 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.html (intento 1)
2026-02-23 03:17:08.653 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:17:08.655 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:17:33.808 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:17:39.343 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:17:39.345 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:18:10.016 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:18:10.018 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:18:27.375 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male (precios actualizados en 2026)' | 1,753,109 bytes
2026-02-23 03:18:27.623 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:18:27.882 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 03:18:27.882 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:18:27.883 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 03:18:27.884 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.5 | 1,753,109b
2026-02-23 03:18:27.891 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [207][en] 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.5 | imgs=8
2026-02-23 03:18:27.901 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [207] 13 cookies extraídas del browser
2026-02-23 03:18:27.901 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 03:18:27.905 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=207 lang=en
2026-02-23 03:18:28.894 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_5868cee62598.jpg (165,778 bytes, 1280×828)
2026-02-23 03:18:28.985 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_38c55cadaa1e.jpg (207,909 bytes, 1183×900)
2026-02-23 03:18:29.007 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_50786e7231bb.jpg (224,576 bytes, 900×900)
2026-02-23 03:18:29.253 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_9c4b8d4c92ab.jpg (179,599 bytes, 1280×873)
2026-02-23 03:18:29.362 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_80ac6704dfd9.jpg (124,555 bytes, 1280×817)
2026-02-23 03:18:29.453 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_903adf6a201c.jpg (138,437 bytes, 1280×853)
2026-02-23 03:18:29.650 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_b7094196037c.jpg (115,139 bytes, 1280×853)
2026-02-23 03:18:29.825 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_3a329ced569b.jpg (153,042 bytes, 1280×869)
2026-02-23 03:18:29.827 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 03:18:29.828 | INFO     | app.scraper_service:_download_images:608 -   📷 [207] 8/8 imágenes descargadas
2026-02-23 03:18:29.829 | INFO     | app.scraper_service:scrape_one:325 -   → [207] Idioma [es]: https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.es.html
2026-02-23 03:18:29.829 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.es.html (intento 1)
2026-02-23 03:18:40.563 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:18:40.565 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:19:11.101 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:19:11.103 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:19:11.960 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:19:41.598 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:19:41.600 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:20:05.537 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male (precios actualizados en 2026)' | 1,743,174 bytes
2026-02-23 03:20:05.724 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:20:05.906 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 03:20:05.906 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['facilities', 'rooms']
2026-02-23 03:20:05.908 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 03:20:05.908 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.5 | 1,743,174b
2026-02-23 03:20:05.926 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [207][es] 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.5 | imgs=8
2026-02-23 03:20:05.927 | INFO     | app.scraper_service:scrape_one:325 -   → [207] Idioma [de]: https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.de.html
2026-02-23 03:20:05.927 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.de.html (intento 1)
2026-02-23 03:20:12.146 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:20:12.149 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:20:42.687 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:20:42.689 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:20:45.837 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:21:13.237 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:21:13.239 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:21:39.688 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male (precios actualizados en 2026)' | 1,748,631 bytes
2026-02-23 03:21:39.851 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:21:40.091 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 03:21:40.091 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:21:40.093 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 03:21:40.093 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.5 | 1,748,631b
2026-02-23 03:21:40.112 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [207][de] 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.5 | imgs=8
2026-02-23 03:21:40.112 | INFO     | app.scraper_service:scrape_one:325 -   → [207] Idioma [fr]: https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.fr.html
2026-02-23 03:21:40.112 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.fr.html (intento 1)
2026-02-23 03:21:43.776 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:21:43.778 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:22:14.273 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:22:14.275 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:22:19.123 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:22:44.967 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:22:44.969 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:23:12.707 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male (precios actualizados en 2026)' | 1,750,967 bytes
2026-02-23 03:23:12.891 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:23:13.103 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 03:23:13.103 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:23:13.105 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 03:23:13.105 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.5 | 1,750,967b
2026-02-23 03:23:13.124 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [207][fr] 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.5 | imgs=8
2026-02-23 03:23:13.124 | INFO     | app.scraper_service:scrape_one:325 -   → [207] Idioma [it]: https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.it.html
2026-02-23 03:23:13.124 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/dusitd2-feydhoo-maldives-all-inclusive-resort.it.html (intento 1)
2026-02-23 03:23:15.654 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:23:15.656 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:23:46.155 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:23:46.157 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:23:52.641 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:24:16.703 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:24:16.705 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:24:46.220 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male (precios actualizados en 2026)' | 1,750,893 bytes
2026-02-23 03:24:46.366 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:24:46.603 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 03:24:46.604 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:24:46.605 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 03:24:46.605 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.5 | 1,750,893b
2026-02-23 03:24:46.626 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [207][it] 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | rating=9.5 | imgs=8
2026-02-23 03:24:47.242 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:24:47.244 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:24:48.998 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 207
2026-02-23 03:24:49.011 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [207] COMPLETADO | 'dusitD2 Feydhoo Maldives - All Inclusive Resort - with Free Transfers, Male, Maldivas' | 5/5 idiomas | 477.3s
2026-02-23 03:24:49.012 | INFO     | app.scraper_service:scrape_one:291 -
────────────────────────────────────────────────────────────
2026-02-23 03:24:49.013 | INFO     | app.scraper_service:scrape_one:292 - 🏨 Iniciando scraping | ID=208 | https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.html
2026-02-23 03:24:49.013 | INFO     | app.scraper_service:scrape_one:293 - ────────────────────────────────────────────────────────────
2026-02-23 03:24:49.015 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:24:49.016 | INFO     | app.scraper:__new__:675 - Scraper: Selenium (USE_SELENIUM=True)
2026-02-23 03:24:50.619 | SUCCESS  | app.scraper:_try_brave:412 - ✓ Brave iniciado
2026-02-23 03:24:50.619 | INFO     | app.scraper_service:scrape_one:325 -   → [208] Idioma [en]: https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.html
2026-02-23 03:24:50.620 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.html (intento 1)
2026-02-23 03:25:17.743 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:25:17.745 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:25:33.094 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:25:48.299 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:25:48.375 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:26:18.899 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:26:18.901 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:26:27.225 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri (precios actualizados en 2026)' | 1,907,956 bytes
2026-02-23 03:26:27.478 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:26:27.750 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [en]
2026-02-23 03:26:27.751 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [en]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:26:27.753 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [en]
2026-02-23 03:26:27.753 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | 1,907,956b
2026-02-23 03:26:27.775 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [208][en] 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | imgs=8
2026-02-23 03:26:27.786 | DEBUG    | app.scraper_service:_download_images:601 -   📷 [208] 12 cookies extraídas del browser
2026-02-23 03:26:27.786 | INFO     | app.image_downloader:__init__:63 - ImageDownloader iniciado | ruta: C:\BookingScraper\data\images
2026-02-23 03:26:27.787 | INFO     | app.image_downloader:download_images:107 - 📷 Descargando 8 imágenes | hotel=208 lang=en
2026-02-23 03:26:29.193 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0001_53c185ab71e5.jpg (116,339 bytes, 1280×853)
2026-02-23 03:26:29.289 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0002_e45aac14347c.jpg (115,902 bytes, 1280×853)
2026-02-23 03:26:29.313 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0003_ce0d6df9cfbb.jpg (134,401 bytes, 1280×853)
2026-02-23 03:26:29.347 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0004_7a17d0234815.jpg (158,115 bytes, 1280×853)
2026-02-23 03:26:29.390 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0000_739017938e45.jpg (164,594 bytes, 1200×900)
2026-02-23 03:26:30.172 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0005_2582f0a76ac3.jpg (131,881 bytes, 1280×853)
2026-02-23 03:26:30.269 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0007_af47a57ee849.jpg (157,653 bytes, 1280×853)
2026-02-23 03:26:30.276 | DEBUG    | app.image_downloader:_download_single:209 - ✓ img_0006_132c94ad9349.jpg (163,159 bytes, 1280×853)
2026-02-23 03:26:30.278 | SUCCESS  | app.image_downloader:download_images:129 - ✓ Descarga completa | 8/8 OK | 0 fallidas | 0 saltadas
2026-02-23 03:26:30.279 | INFO     | app.scraper_service:_download_images:608 -   📷 [208] 8/8 imágenes descargadas
2026-02-23 03:26:30.280 | INFO     | app.scraper_service:scrape_one:325 -   → [208] Idioma [es]: https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.es.html
2026-02-23 03:26:30.280 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.es.html (intento 1)
2026-02-23 03:26:49.447 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:26:49.449 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:27:10.411 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:27:19.939 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:27:19.941 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:27:50.604 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:27:50.679 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:28:04.023 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri (precios actualizados en 2026)' | 1,898,448 bytes
2026-02-23 03:28:04.177 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:28:04.356 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [es]
2026-02-23 03:28:04.356 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [es]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:28:04.358 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [es]
2026-02-23 03:28:04.358 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | 1,898,448b
2026-02-23 03:28:04.409 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [208][es] 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | imgs=8
2026-02-23 03:28:04.410 | INFO     | app.scraper_service:scrape_one:325 -   → [208] Idioma [de]: https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.de.html
2026-02-23 03:28:04.412 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.de.html (intento 1)
2026-02-23 03:28:21.371 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:28:21.373 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:28:44.054 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:28:51.879 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:28:51.881 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:29:22.428 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:29:22.430 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:29:38.388 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri (precios actualizados en 2026)' | 1,906,376 bytes
2026-02-23 03:29:38.529 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:29:38.723 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [de]
2026-02-23 03:29:38.724 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [de]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:29:38.725 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [de]
2026-02-23 03:29:38.725 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | 1,906,376b
2026-02-23 03:29:38.746 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [208][de] 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | imgs=8
2026-02-23 03:29:38.746 | INFO     | app.scraper_service:scrape_one:325 -   → [208] Idioma [fr]: https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.fr.html
2026-02-23 03:29:38.747 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.fr.html (intento 1)
2026-02-23 03:29:52.952 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:29:52.954 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:30:19.773 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:30:23.501 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:30:23.503 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:30:54.015 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:30:54.017 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:31:14.150 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri (precios actualizados en 2026)' | 1,908,388 bytes
2026-02-23 03:31:14.348 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:31:14.517 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [fr]
2026-02-23 03:31:14.519 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [fr]: ['rating_category', 'rooms']
2026-02-23 03:31:14.521 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [fr]
2026-02-23 03:31:14.522 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | 1,908,388b
2026-02-23 03:31:14.547 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [208][fr] 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | imgs=8
2026-02-23 03:31:14.547 | INFO     | app.scraper_service:scrape_one:325 -   → [208] Idioma [it]: https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.it.html
2026-02-23 03:31:14.547 | INFO     | app.scraper:scrape_hotel:450 - 🔍 [Selenium] https://www.booking.com/hotel/mv/centara-grand-lagoon-maldives.it.html (intento 1)
2026-02-23 03:31:24.559 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:31:24.561 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:31:53.719 | DEBUG    | app.scraper:_wait_for_hotel_content:587 -   ✓ Hotel detectado via: [data-testid='property-description']
2026-02-23 03:31:55.061 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:31:55.062 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:32:25.611 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:32:25.613 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:32:47.333 | DEBUG    | app.scraper:scrape_hotel:481 -   📄 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri (precios actualizados en 2026)' | 1,905,467 bytes
2026-02-23 03:32:47.559 | DEBUG    | app.extractor:extract_name:228 -   Nombre extraído vía: og:title
2026-02-23 03:32:47.780 | DEBUG    | app.extractor:extract_images:866 -   [extractor] 8 fotos de hotel extraidas [it]
2026-02-23 03:32:47.780 | DEBUG    | app.extractor:extract_all:207 -   [extractor] Campos vacios [it]: ['rating_category', 'facilities', 'rooms']
2026-02-23 03:32:47.781 | DEBUG    | app.extractor:extract_all:210 -   [extractor] 8 imagenes extraidas [it]
2026-02-23 03:32:47.782 | SUCCESS  | app.scraper:scrape_hotel:499 -   ✓ 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | 1,905,467b
2026-02-23 03:32:47.801 | SUCCESS  | app.scraper_service:scrape_one:356 -   ✓ [208][it] 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | rating=9.4 | imgs=8
2026-02-23 03:32:50.234 | DEBUG    | app.scraper_service:scrape_one:424 -   ✓ Driver Selenium cerrado para hotel 208
2026-02-23 03:32:50.249 | SUCCESS  | app.scraper_service:scrape_one:451 - ✅ [208] COMPLETADO | 'Centara Grand Lagoon Maldives - Free Round Trip Speedboat when stay 4 nights or more between 17 April - 15 October 2026, Nakatukufuri, Maldivas' | 5/5 idiomas | 481.2s
2026-02-23 03:32:56.268 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:32:56.270 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:33:26.940 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:33:26.942 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:33:57.498 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:33:57.501 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:34:28.043 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:34:28.045 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:34:58.558 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:34:58.560 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:35:29.057 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:35:29.059 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:35:59.565 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:35:59.568 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:36:30.076 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:36:30.078 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:37:00.623 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:37:00.625 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:37:31.137 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:37:31.138 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:38:01.798 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:38:01.800 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:38:32.461 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:38:32.463 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:39:02.966 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:39:02.968 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:39:33.522 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:39:33.524 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:40:04.055 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:40:04.057 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:40:34.592 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:40:34.593 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:41:05.099 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:41:05.101 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:41:35.617 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:41:35.618 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:42:06.162 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:42:06.163 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:42:36.701 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:42:36.704 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:43:07.381 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:43:07.383 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:43:38.035 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:43:38.037 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:44:08.550 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:44:08.552 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:44:39.093 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:44:39.095 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:45:09.637 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:45:09.639 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:45:40.155 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:45:40.157 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:46:10.668 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:46:10.670 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:46:41.226 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:46:41.228 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:47:11.735 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:47:11.736 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:47:42.241 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:47:42.243 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:48:12.927 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:48:12.929 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:48:43.558 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:48:43.560 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:49:14.041 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:49:14.043 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:49:44.535 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:49:44.537 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:50:15.029 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:50:15.031 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:50:45.505 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:50:45.506 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:51:16.006 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:51:16.007 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:51:46.511 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:51:46.513 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:52:16.994 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:52:16.996 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:52:47.474 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:52:47.476 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:53:18.106 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:53:18.108 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:53:48.771 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:53:48.773 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:54:19.260 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:54:19.262 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:54:49.776 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:54:49.778 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:55:20.271 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:55:20.273 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:55:50.775 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:55:50.777 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:56:21.282 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:56:21.284 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:56:51.778 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:56:51.781 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:57:22.285 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:57:22.287 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:57:52.792 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:57:52.794 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:58:23.452 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:58:23.454 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:58:54.087 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:58:54.089 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:59:24.572 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:59:24.574 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 03:59:55.057 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 03:59:55.059 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:00:25.551 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:00:25.552 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:00:56.035 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:00:56.037 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:01:26.531 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:01:26.533 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:01:57.036 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:01:57.037 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:02:27.554 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:02:27.556 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:02:58.094 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:02:58.095 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:03:28.767 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:03:28.769 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:03:59.466 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:03:59.468 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:04:29.975 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:04:29.977 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:05:00.510 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:05:00.512 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:05:31.013 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:05:31.016 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:06:01.519 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:06:01.521 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:06:32.025 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:06:32.027 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:07:02.536 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:07:02.538 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:07:33.087 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:07:33.089 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:08:03.625 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:08:03.627 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:08:34.280 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:08:34.282 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:09:04.952 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:09:04.954 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:09:35.494 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:09:35.496 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:10:06.033 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:10:06.035 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:10:36.533 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:10:36.535 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:11:07.050 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:11:07.052 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:11:37.603 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:11:37.605 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:12:08.111 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:12:08.112 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:12:38.624 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:12:38.626 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:13:09.159 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:13:09.161 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:13:39.822 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:13:39.823 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:14:10.513 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:14:10.515 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:14:41.066 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:14:41.067 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:15:11.582 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:15:11.584 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:15:42.062 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:15:42.064 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:16:12.557 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:16:12.559 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:16:43.414 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:16:43.416 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:17:13.908 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:17:13.909 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:17:44.389 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:17:44.391 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:18:14.879 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:18:14.881 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:18:45.511 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:18:45.512 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:19:16.138 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:19:16.140 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:19:46.632 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:19:46.634 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:20:17.118 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:20:17.120 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:20:47.624 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:20:47.626 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:21:18.127 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:21:18.128 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:21:48.639 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:21:48.640 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:22:19.134 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:22:19.136 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:22:49.641 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:22:49.643 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:23:20.139 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:23:20.141 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:23:50.766 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:23:50.768 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:24:21.402 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:24:21.404 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:24:51.893 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:24:51.895 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:25:22.386 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:25:22.388 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:25:52.884 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:25:52.960 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:26:23.456 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:26:23.458 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:26:53.932 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:26:53.934 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:27:24.416 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:27:24.417 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:27:54.893 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:27:54.895 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:28:25.398 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:28:25.463 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:28:56.085 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:28:56.087 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:29:26.751 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:29:26.753 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:29:57.244 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:29:57.246 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:30:27.737 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:30:27.739 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:30:58.228 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:30:58.230 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:31:28.707 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:31:28.709 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:31:59.207 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:31:59.209 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:32:29.687 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:32:29.689 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:33:00.203 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:33:00.205 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:33:30.686 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:33:30.688 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:34:01.324 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:34:01.326 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:34:31.980 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:34:31.982 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:35:02.537 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:35:02.538 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:35:33.086 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:35:33.088 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:36:03.645 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:36:03.647 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:36:34.166 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:36:34.168 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:37:04.680 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:37:04.682 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:37:35.188 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:37:35.190 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:38:05.692 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:38:05.694 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:38:36.206 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:38:36.207 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:39:06.860 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:39:06.862 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:39:37.510 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:39:37.512 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:40:07.989 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:40:07.991 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:40:38.489 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:40:38.491 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:41:08.976 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:41:08.978 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:41:39.464 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:41:39.466 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:42:09.960 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:42:09.962 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:42:40.460 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:42:40.462 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:43:10.935 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:43:10.937 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:43:41.444 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:43:41.446 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:44:12.080 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:44:12.082 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:44:42.729 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:44:42.731 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:45:13.214 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:45:13.215 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:45:43.696 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:45:43.698 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:46:14.194 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:46:14.196 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:46:44.674 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:46:44.675 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:47:15.183 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:47:15.185 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:47:45.671 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:47:45.673 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:48:16.149 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:48:16.151 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:48:46.659 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:48:46.661 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:49:17.290 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:49:17.292 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:49:47.917 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:49:47.919 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:50:18.411 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:50:18.413 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:50:48.890 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:50:48.892 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:51:19.386 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:51:19.387 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:51:49.871 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:51:49.872 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:52:20.351 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:52:20.353 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:52:50.829 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:52:50.831 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:53:21.410 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:53:21.411 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:53:51.897 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:53:51.899 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:54:22.551 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:54:22.553 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:54:53.193 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:54:53.195 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:55:23.700 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:55:23.703 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:55:54.204 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:55:54.205 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:56:24.694 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:56:24.696 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:56:55.587 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:56:55.589 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:57:26.062 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:57:26.064 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:57:56.559 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:57:56.560 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:58:27.046 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:58:27.048 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:58:57.556 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:58:57.558 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:59:28.209 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:59:28.211 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 04:59:58.872 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 04:59:58.874 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:00:29.357 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:00:29.359 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:00:59.837 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:00:59.839 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:01:30.344 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:01:30.346 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:02:00.842 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:02:00.843 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:02:31.346 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:02:31.347 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:03:01.864 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:03:01.866 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:03:32.368 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:03:32.371 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:04:02.862 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:04:02.863 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:04:33.493 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:04:33.495 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:05:04.155 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:05:04.157 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:05:34.656 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:05:34.658 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:06:05.140 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:06:05.142 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:06:35.628 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:06:35.630 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:07:06.125 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:07:06.127 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:07:36.627 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:07:36.629 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:08:07.113 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:08:07.115 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:08:37.613 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:08:37.615 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:09:08.088 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:09:08.090 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:09:38.738 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:09:38.742 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:10:09.374 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:10:09.376 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:10:39.859 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:10:39.861 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:11:10.350 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:11:10.352 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:11:40.835 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:11:40.837 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:12:11.340 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:12:11.342 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:12:42.073 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:12:42.075 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:13:12.575 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:13:12.578 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:13:43.067 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:13:43.069 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:14:13.569 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:14:13.571 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:14:44.207 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:14:44.208 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:15:15.154 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:15:15.156 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:15:45.651 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:15:45.653 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:16:16.134 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:16:16.136 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:16:46.625 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:16:46.627 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:17:17.111 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:17:17.113 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:17:47.603 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:17:47.605 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:18:18.094 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:18:18.097 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:18:48.593 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:18:48.595 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:19:19.121 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:19:19.122 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:19:49.770 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:19:49.772 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:20:20.416 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:20:20.418 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:20:50.928 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:20:50.929 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:21:21.429 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:21:21.431 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:21:51.921 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:21:51.923 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:22:22.406 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:22:22.408 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:22:52.890 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:22:52.892 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:23:23.376 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:23:23.378 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:23:53.849 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:23:53.851 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:24:24.354 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:24:24.355 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:24:54.986 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:24:54.988 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:25:25.621 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:25:25.623 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:25:56.104 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:25:56.168 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:26:26.696 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:26:26.698 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:26:57.213 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:26:57.215 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:27:27.691 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:27:27.693 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:27:58.167 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:27:58.169 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:28:28.663 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:28:28.749 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:28:59.223 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:28:59.226 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:29:29.741 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:29:29.743 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:30:00.386 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:30:00.388 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:30:31.012 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:30:31.014 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:31:01.497 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:31:01.499 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:31:31.996 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:31:31.998 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:32:02.505 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:32:02.507 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:32:33.004 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:32:33.006 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:33:03.487 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:33:03.489 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:33:33.993 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:33:33.995 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:34:04.468 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:34:04.470 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:34:34.964 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:34:34.966 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:35:05.587 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:35:05.588 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:35:36.230 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:35:36.232 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:36:06.724 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:36:06.726 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:36:37.200 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:36:37.203 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:37:07.683 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:37:07.685 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:37:38.162 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:37:38.164 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:38:08.649 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:38:08.651 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:38:39.130 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:38:39.132 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:39:09.615 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:39:09.617 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:39:40.125 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:39:40.127 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:40:10.754 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:40:10.755 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:40:41.384 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:40:41.386 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:41:11.877 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:41:11.879 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:41:42.368 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:41:42.371 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:42:12.872 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:42:12.874 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:42:43.367 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:42:43.369 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:43:13.839 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:43:13.841 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:43:44.323 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:43:44.325 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:44:15.612 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:44:15.613 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:44:46.092 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:44:46.094 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:45:16.720 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:45:16.722 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:45:47.354 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:45:47.357 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:46:17.830 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:46:17.832 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:46:48.314 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:46:48.316 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:47:18.803 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:47:18.805 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:47:49.281 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:47:49.283 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:48:19.770 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:48:19.772 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:48:50.249 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:48:50.250 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:49:20.729 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:49:20.731 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:49:51.242 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:49:51.243 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:50:21.862 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:50:21.863 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:50:52.498 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:50:52.500 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:51:22.985 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:51:22.986 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:51:53.476 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:51:53.478 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:52:23.966 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:52:23.968 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:52:54.460 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:52:54.462 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:53:24.943 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:53:24.945 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:53:55.430 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:53:55.432 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:54:25.919 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:54:25.921 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:54:56.398 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:54:56.400 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:55:27.050 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:55:27.052 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:55:57.705 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:55:57.708 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:56:28.189 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:56:28.191 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:56:58.688 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:56:58.690 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:57:29.197 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:57:29.199 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:57:59.682 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:57:59.684 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:58:30.158 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:58:30.160 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:59:00.635 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:59:00.637 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 05:59:31.124 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 05:59:31.126 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:00:01.623 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:00:01.625 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:00:32.256 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:00:32.259 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:01:02.884 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:01:02.885 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:01:33.357 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:01:33.359 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:02:03.853 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:02:03.855 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:02:34.347 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:02:34.349 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:03:04.831 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:03:04.832 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:03:35.319 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:03:35.321 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:04:05.810 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:04:05.811 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:04:36.305 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:04:36.308 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:05:06.798 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:05:06.800 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:05:37.449 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:05:37.451 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:06:08.079 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:06:08.081 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:06:38.576 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:06:38.578 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:07:09.073 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:07:09.075 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:07:39.567 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:07:39.568 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:08:10.047 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:08:10.049 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:08:40.551 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:08:40.553 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:09:11.031 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:09:11.033 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:09:41.528 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:09:41.530 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:10:12.028 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:10:12.030 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:10:42.678 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:10:42.680 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:11:13.319 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:11:13.321 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:11:43.801 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:11:43.803 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:12:14.303 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:12:14.304 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:12:44.793 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:12:44.794 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:13:15.281 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:13:15.283 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:13:45.781 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:13:45.783 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:14:16.265 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:14:16.266 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:14:46.751 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:14:46.753 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:15:17.246 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:15:17.248 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:15:47.897 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:15:47.899 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:16:18.527 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:16:18.529 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:16:49.015 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:16:49.017 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:17:19.507 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:17:19.509 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:17:50.019 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:17:50.021 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:18:20.510 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:18:20.511 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:18:50.997 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:18:50.999 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:19:21.486 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:19:21.488 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:19:52.002 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:19:52.003 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:20:22.491 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:20:22.494 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:20:53.123 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:20:53.125 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:21:23.757 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:21:23.759 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:21:54.234 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:21:54.236 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:22:24.715 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:22:24.717 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:22:55.213 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:22:55.214 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:23:25.700 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:23:25.702 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:23:56.171 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:23:56.172 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:24:26.663 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:24:26.665 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:24:57.144 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:24:57.146 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:25:27.630 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:25:27.632 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:25:58.275 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:25:58.336 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:26:28.958 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:26:28.960 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:26:59.448 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:26:59.449 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:27:29.935 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:27:29.937 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:28:00.422 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:28:00.424 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:28:30.903 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:28:30.969 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:29:01.467 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:29:01.469 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:29:31.956 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:29:31.958 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:30:02.438 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:30:02.441 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:30:32.934 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:30:32.936 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:31:03.583 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:31:03.585 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:31:34.212 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:31:34.214 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:32:04.718 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:32:04.720 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:32:35.221 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:32:35.223 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:33:05.702 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:33:05.704 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:33:36.197 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:33:36.199 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:34:06.690 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:34:06.691 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:34:37.184 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:34:37.186 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:35:07.689 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:35:07.691 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:35:38.169 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:35:38.171 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:36:08.808 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:36:08.810 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:36:39.460 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:36:39.462 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:37:09.932 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:37:09.934 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:37:40.413 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:37:40.415 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:38:10.898 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:38:10.900 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:38:41.386 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:38:41.388 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:39:11.882 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:39:11.884 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:39:42.372 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:39:42.374 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:40:12.864 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:40:12.866 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:40:44.586 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:40:44.588 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:41:15.208 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:41:15.210 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:41:45.837 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:41:45.839 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:42:16.342 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:42:16.344 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:42:46.838 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:42:46.840 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:43:17.338 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:43:17.340 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:43:47.822 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:43:47.824 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:44:18.310 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:44:18.312 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:44:48.783 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:44:48.785 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:45:19.258 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:45:19.260 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:45:49.752 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:45:49.754 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:46:20.390 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:46:20.393 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:46:51.027 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:46:51.029 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:47:21.505 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:47:21.506 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:47:52.018 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:47:52.020 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:48:22.506 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:48:22.509 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
2026-02-23 06:48:52.979 | INFO     | app.vpn_manager_windows:verify_vpn_active:453 - ✓ VPN activa — IP: 217.216.107.96
2026-02-23 06:48:52.982 | DEBUG    | app.scraper_service:process_batch:210 - ℹ️ No hay URLs pendientes para despachar
