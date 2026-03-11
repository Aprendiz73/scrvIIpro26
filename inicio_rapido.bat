@echo off
REM inicio_rapido.bat -- Arranca BookingScraper Pro v48 completo
REM Activa el entorno virtual y abre 3 terminales independientes:
REM   Terminal 1 — API FastAPI  (http://127.0.0.1:8000)
REM   Terminal 2 — Celery Worker
REM   Terminal 3 — Celery Beat
REM BookingScraper Pro v48 | Windows 11
REM Ejecutar desde C:\BookingScraper (sin .venv activo)
SETLOCAL ENABLEDELAYEDEXPANSION

SET BASE=%~dp0
SET PYTHONPATH=%BASE%
SET PYTHONUNBUFFERED=1

ECHO ============================================================
ECHO  BookingScraper Pro v48 - Inicio Rapido
ECHO ============================================================
ECHO.

REM -- Detectar entorno virtual (.venv o venv) ------------------
SET VENV_ACTIVATE=
IF EXIST "%BASE%.venv\Scripts\activate.bat" (
    SET VENV_ACTIVATE=%BASE%.venv\Scripts\activate.bat
    ECHO [1/4] Entorno virtual detectado: .venv
) ELSE IF EXIST "%BASE%venv\Scripts\activate.bat" (
    SET VENV_ACTIVATE=%BASE%venv\Scripts\activate.bat
    ECHO [1/4] Entorno virtual detectado: venv
) ELSE (
    ECHO [ERROR] No se encontro entorno virtual.
    ECHO         Ejecuta primero: python -m venv .venv
    ECHO         Luego:           .venv\Scripts\activate.bat
    ECHO         Y despues:       pip install -r requirements.txt
    PAUSE & EXIT /B 1
)

REM -- Verificar .env -------------------------------------------
IF NOT EXIST "%BASE%.env" (
    ECHO [ERROR] Archivo .env no encontrado.
    ECHO         Ejecuta: copy .env.example .env
    ECHO         Y configura DB_USER y DB_PASSWORD en .env
    PAUSE & EXIT /B 1
)
ECHO [2/4] .env encontrado OK

REM -- Verificar Redis/Memurai ----------------------------------
ECHO [3/4] Verificando Redis/Memurai...
powershell -Command "try { $t = New-Object System.Net.Sockets.TcpClient('localhost',6379); $t.Close(); Write-Host '  OK - Redis/Memurai activo en puerto 6379' } catch { Write-Host '  AVISO - Redis no responde en puerto 6379. Inicia Memurai o ejecuta start_redis.bat' }" 2>NUL

ECHO.
ECHO [4/4] Abriendo 3 terminales de servicio...
ECHO.

REM -- Terminal 1: API FastAPI ----------------------------------
ECHO   [API]         http://127.0.0.1:8000
ECHO   [Docs]        http://127.0.0.1:8000/docs
start "BSP v48 - API Server" cmd /k "cd /d %BASE% && call %VENV_ACTIVATE% && SET PYTHONPATH=%BASE% && SET PYTHONUNBUFFERED=1 && ECHO. && ECHO ===  BookingScraper API  === && ECHO. && python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --workers 1 --log-level info --access-log"

REM -- Pausa entre arranques para evitar colisiones de import ---
timeout /t 2 /nobreak >NUL

REM -- Terminal 2: Celery Worker --------------------------------
ECHO   [Celery]      Worker iniciando...
start "BSP v48 - Celery Worker" cmd /k "cd /d %BASE% && call %VENV_ACTIVATE% && SET PYTHONPATH=%BASE% && SET PYTHONUNBUFFERED=1 && SET FORKED_BY_MULTIPROCESSING=1 && ECHO. && ECHO ===  BookingScraper Celery Worker  === && ECHO. && python -m celery -A app.celery_app worker --loglevel=info --pool=solo --queues=default,maintenance,monitoring --hostname=worker@%%COMPUTERNAME%%"

REM -- Pausa entre arranques ------------------------------------
timeout /t 2 /nobreak >NUL

REM -- Terminal 3: Celery Beat ----------------------------------
ECHO   [Beat]        Scheduler iniciando...
start "BSP v48 - Celery Beat" cmd /k "cd /d %BASE% && call %VENV_ACTIVATE% && SET PYTHONPATH=%BASE% && SET PYTHONUNBUFFERED=1 && ECHO. && ECHO ===  BookingScraper Celery Beat  === && ECHO. && python -m celery -A app.celery_app beat --loglevel=info --scheduler celery.beat.PersistentScheduler --schedule celerybeat-schedule.db"

ECHO.
ECHO ============================================================
ECHO  Sistema arrancando en 3 terminales independientes.
ECHO.
ECHO  API:     http://127.0.0.1:8000
ECHO  Docs:    http://127.0.0.1:8000/docs
ECHO  Swagger: http://127.0.0.1:8000/redoc
ECHO.
ECHO  Para detener: ejecuta stop_server.bat y stop_celery.bat
ECHO  o cierra las 3 ventanas manualmente.
ECHO ============================================================
ECHO.
ECHO  Esta ventana puede cerrarse.
ECHO ============================================================

ENDLOCAL
