@echo off
REM start_redis.bat — Lanza Memurai/Redis como proceso directo
REM BookingScraper Pro v6.0.0 | Windows 11
REM
REM POLITICA: no se instala ningun servicio de Windows.
REM   Memurai se lanza como proceso normal. Vive mientras
REM   su terminal este abierta.
REM
SETLOCAL ENABLEDELAYEDEXPANSION

REM ── 1. Ya activo? ─────────────────────────────────────────────
SET "REDIS_RESP="
FOR /F "usebackq delims=" %%p IN (`redis-cli PING 2^>NUL`) DO (
    IF NOT DEFINED REDIS_RESP SET "REDIS_RESP=%%p"
)
IF /I "!REDIS_RESP!"=="PONG" (
    ECHO [OK] Memurai/Redis ya esta activo y responde PONG.
    GOTO :END
)

REM ── 2. Buscar Memurai ─────────────────────────────────────────
SET "MEMURAI_EXE="
IF EXIST "C:\Program Files\Memurai\memurai.exe"       SET "MEMURAI_EXE=C:\Program Files\Memurai\memurai.exe"
IF NOT DEFINED MEMURAI_EXE IF EXIST "C:\Memurai\memurai.exe" SET "MEMURAI_EXE=C:\Memurai\memurai.exe"

IF DEFINED MEMURAI_EXE (
    ECHO [INFO] Lanzando Memurai como proceso...
    start "BSP - Memurai" cmd /k "!MEMURAI_EXE!"

    REM Esperar PONG hasta 20s
    SET /A WAIT=0
    :wait_pong
    timeout /t 1 /nobreak >NUL
    SET "RESP="
    FOR /F "usebackq delims=" %%p IN (`redis-cli PING 2^>NUL`) DO (
        IF NOT DEFINED RESP SET "RESP=%%p"
    )
    IF /I "!RESP!"=="PONG" (
        ECHO [OK] Memurai activo y responde PONG.
        GOTO :END
    )
    SET /A WAIT+=1
    IF !WAIT! LSS 20 GOTO :wait_pong

    ECHO [ERROR] Memurai no responde tras 20 segundos.
    ECHO         Revisa la ventana "BSP - Memurai" para ver el error.
    PAUSE
    GOTO :END
)

REM ── 3. Fallback: Redis nativo ─────────────────────────────────
IF EXIST "C:\Program Files\Redis\redis-server.exe" (
    ECHO [INFO] Lanzando Redis nativo como proceso...
    start "BSP - Redis" cmd /k "C:\Program Files\Redis\redis-server.exe"
    timeout /t 5 /nobreak >NUL
    redis-cli PING
    GOTO :END
)

REM ── 4. No encontrado ──────────────────────────────────────────
ECHO [ERROR] Memurai ni Redis encontrados.
ECHO         Descarga Memurai: https://www.memurai.com/
PAUSE

:END
ENDLOCAL
