@echo off
REM inicio_rapido.bat -- Arranca BookingScraper Pro v6.0.0 completo
REM Abre terminales independientes para cada servicio:
REM   Terminal 0 — Memurai (Redis)          si no esta activo
REM   Terminal 1 — API FastAPI              http://127.0.0.1:8000
REM   Terminal 2 — Celery Worker
REM   Terminal 3 — Celery Beat
REM
REM POLITICA: ningun servicio de Windows se instala ni se usa.
REM   Memurai y demas procesos se lanzan directamente como proceso.
REM   Todos los procesos viven mientras sus terminales esten abiertas.
REM
REM BookingScraper Pro v6.0.0 | Windows 11
REM Ejecutar desde C:\BookingScraper
SETLOCAL ENABLEDELAYEDEXPANSION

SET "BASE=%~dp0"
SET PYTHONPATH=%BASE%
SET PYTHONUNBUFFERED=1

ECHO ============================================================
ECHO  BookingScraper Pro v6.0.0 - Inicio Rapido
ECHO ============================================================
ECHO.

REM ── 1. Entorno virtual ────────────────────────────────────────
SET "VENV_ACTIVATE="
IF EXIST "%BASE%.venv\Scripts\activate.bat" (
    SET "VENV_ACTIVATE=%BASE%.venv\Scripts\activate.bat"
    ECHO [1/5] Entorno virtual detectado: .venv
) ELSE IF EXIST "%BASE%venv\Scripts\activate.bat" (
    SET "VENV_ACTIVATE=%BASE%venv\Scripts\activate.bat"
    ECHO [1/5] Entorno virtual detectado: venv
) ELSE (
    ECHO [ERROR] No se encontro entorno virtual.
    ECHO         Ejecuta: python -m venv .venv
    PAUSE & EXIT /B 1
)

REM ── 2. .env ───────────────────────────────────────────────────
IF NOT EXIST "%BASE%.env" (
    ECHO [ERROR] Archivo .env no encontrado.
    ECHO         Ejecuta: copy _env .env
    PAUSE & EXIT /B 1
)
ECHO [2/5] .env encontrado OK

REM ── 3. Memurai / Redis ────────────────────────────────────────
ECHO [3/5] Verificando Memurai/Redis...
SET "REDIS_OK=0"
SET "REDIS_RESP="
FOR /F "usebackq delims=" %%p IN (`redis-cli PING 2^>NUL`) DO (
    IF NOT DEFINED REDIS_RESP SET "REDIS_RESP=%%p"
)
IF /I "!REDIS_RESP!"=="PONG" (
    ECHO   OK - Memurai ya activo ^(PONG recibido^).
    SET "REDIS_OK=1"
)

IF "!REDIS_OK!"=="0" (
    REM -- Buscar ejecutable Memurai en rutas conocidas
    SET "MEMURAI_EXE="
    IF EXIST "C:\Program Files\Memurai\memurai.exe"       SET "MEMURAI_EXE=C:\Program Files\Memurai\memurai.exe"
    IF NOT DEFINED MEMURAI_EXE IF EXIST "C:\Memurai\memurai.exe" SET "MEMURAI_EXE=C:\Memurai\memurai.exe"

    IF DEFINED MEMURAI_EXE (
        ECHO   INFO - Lanzando Memurai como proceso...
        REM FIX-MEMURAI-001: sin cmd /k, Memurai no tiene consola host y termina
        REM   silenciosamente. La terminal cmd /k lo mantiene vivo y muestra errores.
        start "BSP - Memurai" cmd /k "!MEMURAI_EXE!"

        REM -- Esperar hasta 20s que Memurai responda PONG
        SET /A WAIT=0
        :wait_redis
        timeout /t 1 /nobreak >NUL
        SET "REDIS_RESP2="
        FOR /F "usebackq delims=" %%p IN (`redis-cli PING 2^>NUL`) DO (
            IF NOT DEFINED REDIS_RESP2 SET "REDIS_RESP2=%%p"
        )
        IF /I "!REDIS_RESP2!"=="PONG" (
            ECHO   OK - Memurai activo y responde PONG.
            SET "REDIS_OK=1"
            GOTO :redis_done
        )
        SET /A WAIT+=1
        IF !WAIT! LSS 20 GOTO :wait_redis

        ECHO   ERROR - Memurai no responde tras 20 segundos.
        ECHO          Revisa la ventana "BSP - Memurai" para ver el error.
        PAUSE & EXIT /B 1
    ) ELSE (
        REM -- Fallback: buscar Redis nativo
        SET "REDIS_EXE="
        IF EXIST "C:\Program Files\Redis\redis-server.exe" SET "REDIS_EXE=C:\Program Files\Redis\redis-server.exe"
        IF DEFINED REDIS_EXE (
            ECHO   INFO - Lanzando Redis nativo como proceso...
            start "BSP - Redis" cmd /k "!REDIS_EXE!"
            timeout /t 5 /nobreak >NUL
            redis-cli PING >NUL 2>&1 && SET "REDIS_OK=1"
            IF "!REDIS_OK!"=="1" (
                ECHO   OK - Redis nativo activo.
            ) ELSE (
                ECHO   ERROR - Redis no responde. Instala Memurai: https://www.memurai.com/
                PAUSE & EXIT /B 1
            )
        ) ELSE (
            ECHO   ERROR - Memurai ni Redis encontrados en rutas conocidas.
            ECHO          Instala Memurai: https://www.memurai.com/
            PAUSE & EXIT /B 1
        )
    )
)

:redis_done

REM ── 4. PostgreSQL ─────────────────────────────────────────────
ECHO [4/5] Verificando PostgreSQL...
SET "PG_TMPFILE=%TEMP%\pg_ready_%RANDOM%.tmp"
pg_isready -h localhost -p 5432 > "!PG_TMPFILE!" 2>&1
SET "PG_RESP="
FOR /F "usebackq tokens=* delims=" %%q IN ("!PG_TMPFILE!") DO (
    IF NOT DEFINED PG_RESP SET "PG_RESP=%%q"
)
IF EXIST "!PG_TMPFILE!" DEL "!PG_TMPFILE!" >NUL 2>&1
ECHO !PG_RESP! | findstr /i "accepting aceptando" >NUL 2>&1
IF !ERRORLEVEL! NEQ 0 (
    ECHO   ERROR - PostgreSQL no responde en localhost:5432
    ECHO          Inicia el servicio: net start postgresql-x64-16
    PAUSE & EXIT /B 1
)
ECHO   OK - PostgreSQL activo en localhost:5432

REM ── 5. Lanzar servicios de la aplicacion ──────────────────────
ECHO [5/5] Abriendo terminales de servicio...
ECHO.

REM Terminal 1: API FastAPI
ECHO   [API]    http://127.0.0.1:8000
start "BSP - API Server" cmd /k "cd /d %BASE% && call %VENV_ACTIVATE% && SET PYTHONPATH=%BASE% && SET PYTHONUNBUFFERED=1 && ECHO. && ECHO ===  BookingScraper API  === && ECHO. && python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --workers 1 --log-level info --access-log"

timeout /t 2 /nobreak >NUL

REM Terminal 2: Celery Worker
ECHO   [Celery] Worker iniciando...
start "BSP - Celery Worker" cmd /k "cd /d %BASE% && call %VENV_ACTIVATE% && SET PYTHONPATH=%BASE% && SET PYTHONUNBUFFERED=1 && SET FORKED_BY_MULTIPROCESSING=1 && ECHO. && ECHO ===  BookingScraper Celery Worker  === && ECHO. && python -m celery -A app.celery_app worker --loglevel=info --pool=solo --queues=default,maintenance,monitoring --hostname=worker@%%COMPUTERNAME%%"

timeout /t 2 /nobreak >NUL

REM Terminal 3: Celery Beat
ECHO   [Beat]   Scheduler iniciando...
start "BSP - Celery Beat" cmd /k "cd /d %BASE% && call %VENV_ACTIVATE% && SET PYTHONPATH=%BASE% && SET PYTHONUNBUFFERED=1 && ECHO. && ECHO ===  BookingScraper Celery Beat  === && ECHO. && python -m celery -A app.celery_app beat --loglevel=info --scheduler celery.beat.PersistentScheduler --schedule celerybeat-schedule.db"

ECHO.
ECHO ============================================================
ECHO  Sistema arrancando en terminales independientes.
ECHO.
ECHO  API:     http://127.0.0.1:8000
ECHO  Docs:    http://127.0.0.1:8000/docs
ECHO  Swagger: http://127.0.0.1:8000/redoc
ECHO.
ECHO  Para detener: stop_server.bat  y  stop_celery.bat
ECHO  o cierra las terminales manualmente.
ECHO ============================================================
ECHO.
ECHO  Esta ventana puede cerrarse.
ECHO ============================================================

ENDLOCAL
