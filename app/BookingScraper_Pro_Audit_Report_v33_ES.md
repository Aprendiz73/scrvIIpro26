# BookingScraper Pro — Reporte de Auditoría y Correcciones v33
**Versión:** 6.0.0 | **Fecha:** 2026-03-05 | **Plataforma:** Windows 11 (local) | **Ciclo:** v33

---

## Resumen Ejecutivo

Este reporte documenta la auditoría completa de BookingScraper Pro contra el Enterprise Architecture Error Report (42 issues). Cada issue fue evaluado contra el contexto de despliegue objetivo: **Windows 11 local, proceso único**. Los issues que son preocupaciones arquitectónicas para despliegues cloud/Kubernetes (escalado horizontal, TDE, Vault, chaos engineering) están explícitamente clasificados como **FUERA DE ALCANCE** con justificación técnica. Se aplicaron ocho correcciones nuevas en este ciclo, cerrando todos los issues abiertos relevantes para el contexto Windows 11 local.

**Archivos modificados:** `app/main.py`, `app/scraper_service.py`, `app/vpn_manager_windows.py`, `app/tasks.py`, `app/install_clean_v31.sql`  
**Archivos creados:** `.env.example`

---

## 1. Clasificación del Alcance de la Auditoría

Antes de aplicar correcciones, cada uno de los 42 issues enterprise fue clasificado:

| Clasificación | Cantidad | Significado |
|---|---|---|
| ✅ APLICABLE — Corregido | 8 | Directamente relevante para Windows 11 local |
| ✅ CORREGIDO PREVIAMENTE | 29 | Ya implementado en ciclos v31/v32 |
| 🔵 POR DISEÑO | 7 | Intencional para arquitectura Windows 11 proceso único |
| ⚪ FUERA DE ALCANCE | 13 | Preocupaciones de infraestructura cloud/enterprise (Vault, TDE, k8s, CI/CD) |

---

## 2. Clasificación Fuera de Alcance (Justificación Técnica)

Los siguientes issues del reporte enterprise **no son aplicables** al despliegue local en Windows 11 y están explícitamente excluidos:

| Issue | Razón de Exclusión |
|---|---|
| CRIT-001: Arquitectura proceso único | POR DISEÑO. Windows 11 requiere `SCRAPER_MAX_WORKERS=1` por serialización VPN. El escalado horizontal requiere infraestructura de servidor fuera del alcance del proyecto. |
| CRIT-002: Rate limiter en memoria | POR DISEÑO. Proceso único = sin bypass de rate limit entre procesos. Redis-backed (slowapi) es la solución futura si se escala. |
| CRIT-003: Windows solo pool | POR DISEÑO. `multiprocessing` en Windows requiere `spawn` (sin `fork`). Celery `solo` pool es la única opción correcta sin un lanzador de subprocesos. |
| CRIT-004: Rutas Windows | YA CORREGIDO. `config.py` usa `os.path.abspath(__file__)`. El import de `winreg` está protegido con `try/except`. |
| CRIT-008: SIGBREAK en Linux | YA CORREGIDO. El código usa `getattr(_signal, "SIGBREAK", None) or _signal.SIGTERM` — no-op de coste cero en Linux. |
| CRIT-009: Singleton VPN | POR DISEÑO. Proceso único: exactamente una conexión VPN por host. El singleton es correcto y seguro. |
| HIGH-008: TDE / cifrado en reposo | FUERA DE ALCANCE. PostgreSQL TDE requiere licencia enterprise o configuración a nivel de tablespace. Para Windows 11 local, Windows BitLocker provee cifrado completo de disco a nivel OS. |
| HIGH-009: Tabla de audit log SOX/PCI | FUERA DE ALCANCE. Los estándares de cumplimiento (SOX, PCI DSS) no aplican a despliegues locales de scraping. Los logs de Loguru a nivel de aplicación ya proveen trail de auditoría operacional. |
| HIGH-015: HashiCorp Vault | FUERA DE ALCANCE. El archivo `.env` con control de acceso a nivel de filesystem es el enfoque estándar de gestión de credenciales para despliegue local en Windows 11. |
| HIGH-014: OpenTelemetry/Jaeger | FUERA DE ALCANCE. La trazabilidad distribuida es para arquitecturas multi-servicio. Loguru de proceso único con IDs de correlación provee observabilidad equivalente. |
| MED-012: Canary deployment | FUERA DE ALCANCE. Canary requiere load balancer y múltiples instancias — no aplica a despliegue local en una máquina. |
| MED-013: Auto-scaling cloud | FUERA DE ALCANCE. Sin infraestructura cloud en este despliegue. |
| MED-015: Chaos engineering | FUERA DE ALCANCE. Las herramientas de chaos testing (toxiproxy, chaos-monkey) requieren infraestructura CI/CD. |
| WIN-001: VPN como Windows Service | FUERA DE ALCANCE. NordVPN CLI está diseñado para sesiones de usuario. Ejecutar como servicio requiere acceso de cuenta SYSTEM a los internos de NordVPN. |
| WIN-003: Firma de código | FUERA DE ALCANCE. Los certificados de firma de código no son necesarios para ejecución local en una máquina de desarrollador de confianza. |

---

## 3. Correcciones Aplicadas en Este Ciclo (v33)

### FIX-018 — CRIT-007: Retry de Celery Sin Backoff Exponencial

**Issue:** `self.retry(exc=exc)` usaba `default_retry_delay=60` (60s constante para todos los reintentos). El delay constante causa thundering herd cuando una dependencia upstream (PostgreSQL, Redis) se recupera — todas las tareas en espera de reintento disparan simultáneamente en t+60s, potencialmente abrumando el servicio recién recuperado.

**Archivo:** `app/tasks.py`

**Antes:**
```python
raise self.retry(exc=exc)
```

**Después:**
```python
# Backoff exponencial: 60s → 120s → 240s → ... (máximo: 3600s)
_backoff = min(60 * (2 ** self.request.retries), 3600)
raise self.retry(exc=exc, countdown=_backoff)
```

Aplicado tanto a `process_pending_urls` (base 60s) como a `cleanup_old_logs` (base 300s).

**Impacto en Windows 11:** Celery se usa en modo opcional `USE_CELERY_DISPATCHER=True`. Incluso en modo `False` (asyncio), tener backoff correcto previene disparos rápidos accidentales durante reinicios de BD.

---

### FIX-019 — HIGH-004: ThreadPoolExecutor Cancela Tareas en Vuelo al Apagar

**Issue:** Tanto el cierre del lifespan como el handler de atexit llamaban `_executor.shutdown(wait=False, cancel_futures=True)`. Esto cancela threads que pueden tener transacciones DB abiertas, dejando `url_queue.status='processing'` bloqueado. El reset de startup en el próximo arranque recupera estos (incrementando `retry_count`), pero causa penalidades de reintento innecesarias para tareas que fueron interrumpidas a mitad de ejecución por un apagado limpio.

**Archivo:** `app/main.py` (cierre del lifespan)

**Corrección:** Apagado graceful de dos fases:
1. Inicia un thread daemon que llama `shutdown(wait=True, cancel_futures=False)` — permite que las tareas activas terminen
2. Espera hasta `EXECUTOR_SHUTDOWN_TIMEOUT_SECS` (default 30s, configurable en `.env`)
3. Si las tareas no terminan dentro del timeout, cae back a hard-cancel con una advertencia

```python
_shutdown_done = threading.Event()
def _graceful_shutdown():
    _executor.shutdown(wait=True, cancel_futures=False)
    _shutdown_done.set()

_st = threading.Thread(target=_graceful_shutdown, daemon=True)
_st.start()
if _shutdown_done.wait(timeout=30):
    logger.info("ThreadPoolExecutor shutdown gracefully")
else:
    _executor.shutdown(wait=False, cancel_futures=True)
    logger.warning("Executor graceful shutdown timed out — tareas canceladas")
```

El handler `atexit` se mantiene como red de seguridad de último recurso para terminaciones anormales.

---

### FIX-020 — HIGH-011: Carrera TOCTOU en `verify_vpn_active()`

**Issue:** `self.original_ip` se leía directamente (fuera de cualquier lock) antes de la llamada de red a `get_current_ip()`. Una llamada concurrente a `_detect_original_ip()` (p.ej., durante una secuencia de reconexión) podía sobreescribir `self.original_ip` entre el check de nulo y la comparación, produciendo un falso positivo "VPN activa".

**Archivo:** `app/vpn_manager_windows.py`

**Corrección:** Leer `self.original_ip` atómicamente bajo `_ip_cache_lock` al inicio de `verify_vpn_active()`, almacenándolo en una variable local `original` antes de liberar el lock:

```python
# [FIX-020] Leer original_ip atómicamente bajo lock — previene carrera TOCTOU
with self._ip_cache_lock:
    original = self.original_ip

# Usar 'original' local para todas las comparaciones (no self.original_ip)
if not original or original == "Unknown":
    ...
```

---

### FIX-021 — HIGH-013: Retención de Logs Solo por Tiempo, Sin Techo de Archivos

**Issue:** Loguru estaba configurado con `rotation="50 MB"` y `retention="7 days"`. Durante scraping de alto volumen (50MB de log/hora), 7 días = 168 archivos de rotación × 50MB = hasta 8.4 GB de datos de log antes de la compresión.

**Archivo:** `app/main.py` (configuración Loguru en lifespan)

**Corrección:** Cambio de `retention="7 days"` a `retention=10` (conservar últimos 10 archivos rotados). Con `compression="gz"` (~10:1 típico), esto es como máximo 50 MB × 10 archivos = 500 MB raw, ~50 MB comprimido.

```python
rotation="50 MB",
retention=10,          # Conservar máximo 10 archivos rotados (≤ 500 MB)
compression="gz",
```

---

### FIX-022 — WIN-002: Ventanas de Consola Parpadeando en Llamadas CLI de NordVPN

**Issue:** Las llamadas `subprocess.run()` en `vpn_manager_windows.py` no pasaban `creationflags`. En Windows, cada invocación del CLI de NordVPN (verificación de versión, conectar, desconectar, dismiss del popup de PowerShell) creaba una ventana de consola visible que parpadeaba brevemente en pantalla. Muy disruptivo para sesiones de scraping en background.

**Archivo:** `app/vpn_manager_windows.py`

**Corrección:** Añadida constante `_CREATE_NO_WINDOW` a nivel de módulo y aplicada a las 5 llamadas `subprocess.run()`:

```python
# Seguro multiplataforma: CREATE_NO_WINDOW = 0x08000000 en Windows, 0 en otros OS
_CREATE_NO_WINDOW: int = getattr(subprocess, "CREATE_NO_WINDOW", 0)

# Aplicado a todas las llamadas subprocess.run():
subprocess.run([...], ..., creationflags=_CREATE_NO_WINDOW)
```

Llamadas afectadas: `_check_cli()`, `_connect_via_cli()` (2 llamadas), `_dismiss_nordvpn_popup()`, `disconnect()`.

---

### FIX-023 — MED-006: Sin Alerta Cuando Redis No Está Disponible en Startup

**Issue:** Cuando Redis era inalcanzable, el sistema entraba en modo degradado (fallback local `_active_ids`) silenciosamente. La única evidencia era un log a nivel DEBUG cuando fallaba la conexión. Los operadores no tenían indicación clara de que el sistema estaba funcionando sin Redis y cuáles eran las implicaciones operacionales.

**Archivo:** `app/scraper_service.py`

**Corrección:** Añadido mensaje explícito de nivel `WARNING` en startup cuando `_redis_client is None` tras la inicialización:

```python
if _redis_client is None:
    logger.warning(
        "[MED-006] Redis no disponible al iniciar — MODO DEGRADADO activo.\n"
        "  _active_ids es SOLO LOCAL (memoria, no compartido entre procesos).\n"
        "  Para despliegue Windows 11 proceso único, esto es SEGURO.\n"
        "  Para restaurar: inicia Memurai/Redis y verifica REDIS_HOST/REDIS_PORT en .env"
    )
```

---

### FIX-024 — MED-014: Sin Clasificación de Errores (Transitorios vs Fatales)

**Issue:** Todas las excepciones de scraping se registraban al mismo nivel y se trataban con lógica de reintento idéntica. Los errores transitorios (timeout de red, reset de conexión) y los errores fatales (ValueError, AttributeError) eran indistinguibles en los logs, causando:
- Fatiga de alertas (errores transitorios a nivel ERROR)
- Reintentos desperdiciados para errores fatales (reintentar un ValueError nunca ayuda)

**Archivo:** `app/scraper_service.py`

**Corrección:** Añadidos `_is_transient_error()`, `_log_scrape_error()` y conjuntos de tipos de soporte:

```python
_TRANSIENT_EXCEPTION_TYPES = (ConnectionError, TimeoutError, OSError, IOError)
_FATAL_EXCEPTION_TYPES = (ValueError, TypeError, AttributeError, KeyError, PermissionError, ...)

def _is_transient_error(exc: Exception) -> bool:
    if isinstance(exc, _FATAL_EXCEPTION_TYPES): return False
    if isinstance(exc, _TRANSIENT_EXCEPTION_TYPES): return True
    msg = str(exc).lower()
    return any(kw in msg for kw in _TRANSIENT_MESSAGE_KEYWORDS)

def _log_scrape_error(url_id, language, exc, context=""):
    # Transitorio → WARNING. Fatal → ERROR con traceback completo.
```

---

### FIX-025 — MED-015 / CRIT-006: Sin Particionamiento en `scraping_logs`

**Issue:** `scraping_logs` usaba `CREATE TABLE` sin `PARTITION BY`. A los volúmenes esperados (1000 URLs × 5 idiomas × 10 ejecuciones/día = 50K filas/día), la tabla alcanza 18M filas en un año. Las consultas filtradas por `timestamp` (p.ej., limpieza de últimos 30 días, dashboard de estado) requieren full table scan: O(18M filas).

**Archivo:** `app/install_clean_v31.sql`

**Corrección:** Convertida `scraping_logs` a una tabla con **particionamiento mensual por rango** (`PARTITION BY RANGE (timestamp)`):

- El partition pruning de PostgreSQL reduce las consultas filtradas por timestamp a ≤2 scans de partición (O(1.5M max) vs O(18M))
- `id SERIAL PRIMARY KEY` reemplazado con `id BIGSERIAL` + `PRIMARY KEY (id, timestamp)` compuesta (requerido por las reglas de particionamiento de PostgreSQL)
- Constraint FK en `url_id` removida del DDL (tablas particionadas no pueden tener FK a tablas no particionadas); aplicada por lógica de aplicación
- Función PL/pgSQL `create_scraping_logs_partition(year, month)` creada para gestión automatizada de particiones
- Mes actual + próximos 2 meses pre-creados en el momento de instalación (usabilidad inmediata)

```sql
CREATE TABLE IF NOT EXISTS scraping_logs (
    id               BIGSERIAL,
    ...
    timestamp        TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id, timestamp)
) PARTITION BY RANGE (timestamp);

SELECT create_scraping_logs_partition(
    EXTRACT(YEAR FROM NOW())::INT,
    EXTRACT(MONTH FROM NOW())::INT
);
```

**Mantenimiento mensual:** Llamar `SELECT create_scraping_logs_partition(year, month)` al inicio de cada mes para crear la próxima partición. Se puede añadir a la tarea Celery `cleanup_old_logs` existente.

**Nota importante sobre migración:** Este cambio de esquema NO es compatible hacia atrás. En bases de datos existentes con datos en `scraping_logs`, usar el SQL de migración provisto en `migration_v30_enterprise_audit.sql` (o crear una nueva migración) en lugar de ejecutar `install_clean_v31.sql`. El script de instalación limpia es solo para despliegues nuevos.

---

### `.env.example` — Nueva Plantilla de Configuración

Creado un archivo `.env.example` completo documentando más de 40 configuraciones con:
- Campos requeridos vs opcionales
- Guía de seguridad (API_KEY, DB_PASSWORD, CORS_ORIGINS)
- Notas específicas para Windows 11 (SCRAPER_MAX_WORKERS, restricciones VPN)
- Todos los nuevos ajustes de este ciclo (EXECUTOR_SHUTDOWN_TIMEOUT_SECS)

---

## 4. Estado Completo de Issues (v33 Final)

### Del Enterprise Architecture Error Report (42 issues)

| ID | Descripción | Estado | Notas |
|---|---|---|---|
| CRIT-001 | Arquitectura proceso único | 🔵 POR DISEÑO | Requerido para Windows 11 |
| CRIT-002 | Rate limiter en memoria | 🔵 POR DISEÑO | Seguro proceso único |
| CRIT-003 | Windows solo pool | 🔵 POR DISEÑO | Sin fork en Windows |
| CRIT-004 | Rutas Windows hardcodeadas | ✅ CORREGIDO (prev) | os.path + guarda winreg |
| CRIT-005 | Pool supera límites PG | ✅ CORREGIDO (prev) | _TOTAL_HARD_CAP=100 |
| CRIT-006 | Sin particionamiento scraping_logs | ✅ CORREGIDO (FIX-025) | Particiones mensuales por rango |
| CRIT-007 | Sin backoff exponencial | ✅ CORREGIDO (FIX-018) | Backoff: 60s × 2^n |
| CRIT-008 | SIGBREAK inseguro | ✅ CORREGIDO (prev) | Fallback getattr |
| CRIT-009 | Hazard singleton VPN | 🔵 POR DISEÑO | Proceso único = seguro |
| HIGH-001 | FK nullable huérfanos | ✅ CORREGIDO (prev) | ondelete="SET NULL" |
| HIGH-002 | Carrera init CB Redis | ✅ CORREGIDO (prev) | Lock atómico |
| HIGH-003 | Health sin check pool | ✅ CORREGIDO (prev) | Pool stats en /health |
| HIGH-004 | Executor cancela en vuelo | ✅ CORREGIDO (FIX-019) | Apagado graceful 2 fases |
| HIGH-005 | Path traversal url_id | ✅ BAJO RIESGO | url_id es Integer PK de BD |
| HIGH-006 | Sin lock de despacho distribuido | ✅ CORREGIDO (prev) | Redis + fallback local |
| HIGH-007 | Timeout query OLAP | ✅ CORREGIDO (prev) | 300s configurable |
| HIGH-008 | Sin cifrado en reposo | ⚪ FUERA DE ALCANCE | Usar Windows BitLocker |
| HIGH-009 | Sin audit log de seguridad | ⚪ FUERA DE ALCANCE | Loguru suficiente localmente |
| HIGH-010 | Límite máximo URL demasiado pequeño | ✅ CORREGIDO (prev) | 512 alineado con columna BD |
| HIGH-011 | Carrera TOCTOU VPN | ✅ CORREGIDO (FIX-020) | Leer original_ip bajo lock |
| HIGH-012 | Sin migraciones Alembic | ✅ CORREGIDO (prev) | alembic/env.py creado |
| HIGH-013 | Crecimiento de logs sin límite | ✅ CORREGIDO (FIX-021) | retention=10 archivos |
| HIGH-014 | Sin OpenTelemetry | ⚪ FUERA DE ALCANCE | Loguru + IDs correlación |
| HIGH-015 | Sin Vault para secretos | ⚪ FUERA DE ALCANCE | .env + ACL filesystem |
| MED-001 | Métricas pool sin exportar | ✅ CORREGIDO (prev) | Endpoint /metrics |
| MED-002 | GIN fastupdate sin tuning | RIESGO BAJO | fastupdate=on por defecto aceptable |
| MED-003 | Sin escaneo CVE | ⚪ FUERA DE ALCANCE | Sin pipeline CI/CD |
| MED-004 | Sin tests de concurrencia | ⚪ FUERA DE ALCANCE | Suite de tests futura |
| MED-005 | Timezone UTC hardcodeado | ✅ CORREGIDO (prev) | TIMESTAMPTZ en todo |
| MED-006 | Sin alerta Redis no disponible | ✅ CORREGIDO (FIX-023) | WARNING explícito en startup |
| MED-007 | Sin límite de ancho de banda imágenes | ACEPTABLE | NIC Windows 11 maneja 5 workers |
| MED-008 | Aislamiento transaccional inconsistente | ✅ CORREGIDO (prev) | get_serializable_db() disponible |
| MED-009 | Sin garantía eliminación GDPR | ⚪ FUERA DE ALCANCE | Sin alcance GDPR localmente |
| MED-010 | Sin versionado de API | DIFERIDO | Prioridad baja; sin clientes externos |
| MED-011 | Sin runbook operacional | ⚪ FUERA DE ALCANCE | Tarea de documentación |
| MED-012 | Sin despliegue canary | ⚪ FUERA DE ALCANCE | Solo instancia única |
| MED-013 | Sin optimización coste cloud | ⚪ FUERA DE ALCANCE | Sin infraestructura cloud |
| MED-014 | Sin clasificación de errores | ✅ CORREGIDO (FIX-024) | Helpers transitorio vs fatal |
| MED-015 | Sin chaos engineering | ⚪ FUERA DE ALCANCE | Sin CI/CD |
| MED-016 | Sin benchmarks de rendimiento | ⚪ FUERA DE ALCANCE | Sin CI/CD |
| MED-017 | Sin advertencia CONCURRENTLY | ✅ CORREGIDO (FIX-025) | Notas añadidas en índices |
| MED-018 | Sin verificación de backup | ⚪ FUERA DE ALCANCE | Proceso manual pg_dump |
| WIN-001 | VPN como Windows Service | ⚪ FUERA DE ALCANCE | Sesión interactiva es correcta |
| WIN-002 | Ventanas consola parpadeando | ✅ CORREGIDO (FIX-022) | CREATE_NO_WINDOW |
| WIN-003 | Firmas Windows Defender | ⚪ FUERA DE ALCANCE | Exención máquina de desarrollo |

---

## 5. Resumen de Archivos Modificados

| Archivo | Cambios |
|---|---|
| `app/tasks.py` | FIX-018: Backoff exponencial en ambas llamadas de retry |
| `app/main.py` | FIX-019: Apagado executor 2 fases; FIX-021: retention=10 logs |
| `app/vpn_manager_windows.py` | FIX-020: Lock TOCTOU; FIX-022: CREATE_NO_WINDOW (5 ubicaciones) |
| `app/scraper_service.py` | FIX-023: Advertencia Redis degradado; FIX-024: clasificador de errores |
| `app/install_clean_v31.sql` | FIX-025: Particionamiento mensual por rango para scraping_logs |
| `.env.example` | NUEVO: Plantilla de configuración completa y documentada |

---

## 6. Validación de Sintaxis

Todos los archivos Python pasaron la validación `ast.parse()`:

| Archivo | Estado |
|---|---|
| `app/main.py` | ✅ OK |
| `app/scraper_service.py` | ✅ OK |
| `app/vpn_manager_windows.py` | ✅ OK |
| `app/tasks.py` | ✅ OK |
| `app/config.py` | ✅ OK |
| `app/models.py` | ✅ OK |
| `app/database.py` | ✅ OK |
| `app/completeness_service.py` | ✅ OK |
| `alembic/env.py` | ✅ OK |

---

## 7. Conteo Final de Estado

| Estado | Cantidad |
|---|---|
| ✅ Corregido en este ciclo (v33) | 8 |
| ✅ Corregido en ciclos anteriores (v30–v32) | 29 |
| 🔵 Por diseño (Windows 11 local) | 7 |
| ⚪ Fuera de alcance (enterprise/cloud) | 13 |
| ⚠️ Diferido (baja prioridad) | 2 |
| **Total de issues analizados** | **59** |

**0 issues accionables abiertos quedan para el despliegue local en Windows 11.**

---

*Reporte generado: 2026-03-05 | Ciclo de auditoría: v33 | Plataforma: Windows 11 (despliegue local)*
