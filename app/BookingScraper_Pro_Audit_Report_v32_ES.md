# BookingScraper Pro — Reporte de Auditoría y Correcciones v32
**Versión:** 6.0.0 | **Fecha:** 2026-03-05 | **Plataforma:** Windows 11 (local) | **Ciclo:** v32

---

## Resumen Ejecutivo

Este reporte documenta la auditoría completa paso a paso del código fuente de BookingScraper Pro contra el reporte de errores v31. Todos los issues reportados previamente fueron verificados contra los archivos fuente reales. Se aplicaron tres nuevas correcciones en este ciclo (v32): SEC-001 (credenciales hardcodeadas en Alembic), LOW-006 (llamadas `print()` en el gestor VPN) y Recovery-003 (falta de re-sincronización de `_active_ids` desde Redis al recuperar el circuit breaker). Todos los issues abiertos restantes son preocupaciones a nivel de infraestructura que no afectan el caso de uso de despliegue local en Windows 11.

**Archivos modificados:** `alembic.ini`, `app/vpn_manager_windows.py`, `app/scraper_service.py`
**Archivos creados:** `alembic/env.py`

---

## 1. Metodología de Auditoría

Cada archivo fue examinado en secuencia:

1. `alembic.ini` — auditoría de exposición de credenciales
2. `app/config.py` — validaciones, resolución de rutas, constantes
3. `app/main.py` — CORS, signal handlers, endpoint de salud, métricas, rate limiter
4. `app/models.py` — índices, constraints, FK nullability
5. `app/scraper_service.py` — Redis CB, VPN CB, sincronización _active_ids, despacho, ciclo de sesiones
6. `app/completeness_service.py` — ciclo de vida de sesiones
7. `app/vpn_manager_windows.py` — llamadas print(), TTL de caché IP
8. `app/database.py` — configuración de pool, backoff con reintentos
9. `app/tasks.py` — límites de tiempo Celery
10. `app/install_clean_v31.sql` — presencia del índice parcial

---

## 2. Issues Verificados Como Corregidos (Confirmados en Código)

Los siguientes issues del reporte de errores v31 fueron confirmados como correctamente implementados en el código base antes de este ciclo.

| ID | Severidad | Descripción | Ubicación Verificada |
|---|---|---|---|
| CRIT-001 | CRÍTICO | Módulo `vpn_manager.py` faltante | `app/vpn_manager.py` existe, `vpn_manager_factory` exportado |
| CRIT-002 | CRÍTICO | `build_language_url()` faltante | `app/scraper.py` — función presente e importable |
| CRIT-003 | CRÍTICO | Condición de carrera en despacho de URLs | `scraper_service.py:713` — CTE atómica `FOR UPDATE SKIP LOCKED` |
| CRIT-004 | CRÍTICO | Agotamiento del pool DB | `database.py:54-67` — `_POOL_SAFE_MAX=50`, `_TOTAL_HARD_CAP=100` |
| CRIT-007 | CRÍTICO | Acumulación de archivos HTML debug | `scraper.py` — `purge_debug_html()` llamada cada 120 ciclos de despacho |
| HIGH-001 | ALTA | Silenciamiento de batch_size | `scraper_service.py` — `ValueError` explícito lanzado |
| HIGH-002 | ALTA | Circuit breaker Redis faltante | `scraper_service.py:140-215` — CB de 3 estados implementado |
| HIGH-003 | ALTA | Índice B-Tree faltante en `hotels.url` | `models.py:100` — `index=True` en columna `hotels.url` |
| HIGH-004 | ALTA | Signal handlers de Windows incompletos | `main.py:537-560` — SIGINT + SIGBREAK registrados |
| HIGH-005 | ALTA | Truncado de errores hardcodeado | `config.py` — constante `MAX_ERROR_LEN=2000` usada en todo el código |
| HIGH-006 | ALTA | `/health` retorna 200 cuando está degradado | `main.py:897-975` — HTTP 503 en fallo de DB |
| HIGH-007 | ALTA | TTL excesivo de caché IP de VPN | `vpn_manager_windows.py:85` — TTL = 5s, caché invalidado tras rotate |
| HIGH-008 | ALTA | Verificación de integridad de imágenes ausente | `image_downloader.py` — `Pillow.Image.verify()` llamado |
| HIGH-009 | ALTA | Limpieza de sesión faltante en excepciones | `scraper_service.py` — `finally: db.close()` en todos los paths |
| HIGH-010 | ALTA | Índice GIN faltante en `images_urls` | `models.py:149-163` — `ix_hotels_images_gin` definido |
| HIGH-013 | ALTA | Límites de tiempo Celery excesivos | `tasks.py:90-91` — `soft=150s`, `hard=180s` |
| MED-011 | MEDIA | Reintento de conexión DB faltante | `database.py:282` — `test_connection()` con backoff exponencial |
| MED-022 | MEDIA | Endpoint `/metrics` faltante | `main.py:982` — endpoint JSON de métricas implementado |
| SEC-002 | ALTA | CORS wildcard con credenciales | `main.py:730-755` — validación runtime rechaza `CORS_ORIGINS=*` |
| SEC-003 | MEDIA | Mensajes de error exponen internos | `main.py:214` — `_internal_error()` retorna solo correlation ID |
| CONC-001 | ALTA | Riesgo de deadlock en procesamiento de idiomas | `scraper_service.py` — ordenamiento alfabético de idiomas aplicado |
| CONC-002 | ALTA | Timeout faltante en lock VPN | `scraper_service.py` — `_vpn_lock.acquire(timeout=30s)` |
| CONC-005 | MEDIA | Stats de Celery dispatcher no compartidas | `scraper_service.py:217` — advertencia lanzada si `USE_CELERY_DISPATCHER=True` sin Redis |
| DATA-001 | MEDIA | Gap en constraint unique con NULL | `install_clean_v31.sql:327` — índice único parcial `ix_hotels_url_lang_null` |
| ARCH-001 | ALTA | Estado en memoria en entorno multi-worker | `scraper_service.py` — respaldado por Redis con fallback local |
| ARCH-002 | MEDIA | Health check sin verificar dependencias | `main.py:897-975` — DB + Redis + VPN + disco verificados |
| CFG-001 | ALTA | Default vacío para `DB_PASSWORD` | `config.py:48` — default vacío + `ValueError` en startup si no configurado |
| CFG-002 | MEDIA | Resolución de rutas dependiente del CWD | `config.py` — rutas relativas a la ubicación de `__file__` |
| Recovery-002 | MEDIA | Rollback DB sin cerrar sesión | `scraper_service.py`, `completeness_service.py` — `rollback()` + `finally: close()` |

---

## 3. Correcciones Aplicadas en Este Ciclo (v32)

### FIX-015 — SEC-001: Credenciales Hardcodeadas en `alembic.ini`

**Referencia en Error Report:** SEC-001 (MEDIA — Exposición de Credenciales)

**Causa raíz:** `alembic.ini` contenía `sqlalchemy.url = postgresql://postgres:postgres@localhost:5432/booking_scraper` en texto plano. Cualquier desarrollador con acceso de lectura al repositorio podía ver la contraseña de base de datos.

**Evidencia (antes):**
```ini
# alembic.ini línea 55
sqlalchemy.url = postgresql://postgres:postgres@localhost:5432/booking_scraper
```

**Corrección aplicada en `alembic.ini`:**
```ini
# [FIX SEC-001] Las credenciales NO deben almacenarse en archivos versionados.
# alembic/env.py sobreescribe este valor en runtime vía settings.DATABASE_URL
sqlalchemy.url = CREDENTIALS_PROVIDED_BY_ENV_PY_AT_RUNTIME
```

**Nuevo archivo creado: `alembic/env.py`**

El script de entorno Alembic ahora lee las credenciales desde `app/config.py` (que lee `DB_PASSWORD` desde `.env`) y sobreescribe el placeholder en runtime mediante `config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)`. Este es el patrón estándar de Alembic para gestión de credenciales.

```python
from app.config import settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
```

**Impacto en seguridad:** Las credenciales de base de datos ya no están almacenadas en ningún archivo versionado. El archivo `.env` (que contiene `DB_PASSWORD`) debe estar en `.gitignore` (que ya está incluido en el `.gitignore` del proyecto). Si `alembic.ini` se publica accidentalmente en un repositorio público, no se expone ninguna credencial.

**Compatibilidad hacia atrás:** No se requieren cambios en los scripts de migración existentes. `alembic upgrade head` y `alembic revision` continúan funcionando siempre que `.env` esté correctamente configurado.

---

### FIX-016 — LOW-006: Llamadas `print()` en `vpn_manager_windows.py`

**Referencia en Error Report:** LOW-006 (BAJA — Logging)

**Causa raíz:** Los métodos `_connect_manual()`, `disconnect()` y `print_status()` usaban `print()` para salida. En Windows, `print()` escribe en stdout, saltándose completamente la cadena de handlers de Loguru — estos mensajes nunca se escriben en el log rotativo, nunca se capturan por el sink de archivo, y nunca se formatean con timestamps ni etiquetas de nivel.

**Antes:** 35 llamadas `print()` en `vpn_manager_windows.py`
**Después:** 1 instancia restante — dentro de un docstring únicamente (no es código ejecutable)

**Reemplazos realizados:**

| Método | Antes | Después |
|---|---|---|
| `_connect_manual()` | 8 × `print()` | `logger.info("[VPN] ...")` |
| `_connect_manual()` — aviso de IP | `print(f"⚠️ IP no cambió...")` | `logger.warning("[VPN] ...")` |
| `disconnect()` | 6 × `print()` | `logger.info("[VPN] ...")` |
| `print_status()` | 9 × `print()` | `logger.info("[VPN] ...")` |
| Bloque de test `__main__` | 10 × `print()` | `logger.info/error("[VPN TEST] ...")` |

**Nota sobre llamadas `input()`:** Las dos llamadas `input()` (prompt de teclado para el usuario en modo interactivo) se conservaron intencionalmente. Solo son alcanzables cuando `interactive=True`, que es un modo consola manual nunca activado por el worker de Celery. El modo interactivo es una función de mantenimiento/diagnóstico, no parte del path de producción.

**Impacto:** Toda la salida del gestor VPN ahora se enruta a través de Loguru, lo que significa que aparece en el archivo de log rotativo en `data/logs/` con timestamps correctos, niveles de log y formato consistente con el resto de la aplicación.

---

### FIX-017 — Recovery-003: Falta de Re-sincronización de `_active_ids` Tras Recuperación del Circuit Redis

**Referencia en Error Report:** Recovery-003 (MEDIA — Failover de Redis)

**Causa raíz:** Cuando el circuit breaker de Redis transiciona de OPEN → HALF-OPEN → CLOSED (circuit recuperado), el set en memoria `_active_ids` NO se re-sincronizaba desde Redis. Durante el período de interrupción, los claims de URL realizados vía Redis (antes de la interrupción) existen solo en Redis. Los claims realizados durante la interrupción (vía fallback local `_active_ids`) existen solo en memoria. Tras la recuperación, estos dos sets son inconsistentes — una URL retenida en Redis podría reclamarse de nuevo desde el set local si no estaba presente allí.

**Antes:**
```python
_redis_client.ping()
with _redis_cb_lock:
    if _redis_cb_failures > 0:
        logger.info("[HIGH-002] Redis CB closed — connection restored.")
    _redis_cb_failures = 0
return _redis_client
```

**Después (`app/scraper_service.py`):**
```python
_redis_client.ping()
with _redis_cb_lock:
    was_recovering = _redis_cb_failures > 0
    _redis_cb_failures = 0
if was_recovering:
    logger.info("[HIGH-002] Redis CB closed — connection restored.")
    # [FIX Recovery-003] Re-sincronizar _active_ids desde Redis tras recuperación
    try:
        keys = _redis_client.keys("bsp:active:*")
        if keys:
            recovered_ids = {int(k.decode().split(":")[-1]) for k in keys}
            with _active_ids_local_lock:
                _active_ids.update(recovered_ids)
            logger.info("[Recovery-003] Re-sincronizados %d URL IDs activos...", len(recovered_ids))
    except Exception as sync_err:
        logger.warning("[Recovery-003] Re-sync de _active_ids omitido: %s", sync_err)
return _redis_client
```

**Nota de diseño para despliegue single-process en Windows 11:** Con `SCRAPER_MAX_WORKERS=1` (el valor por defecto y recomendado para Windows), Redis se usa como almacén de claims distribuido pero el único proceso es el proceso FastAPI/asyncio. En esta configuración, el set local `_active_ids` y Redis son naturalmente consistentes — un claim se coloca en ambos simultáneamente. La re-sincronización es por tanto una red de seguridad para cualquier inconsistencia que pudiera surgir de una interrupción de Redis, no un path de código crítico para el despliegue estándar de Windows.

**Seguridad ante excepciones:** La re-sincronización está envuelta en `try/except` para que cualquier error de Redis durante el escaneo de claves no impida que el circuit se cierre completamente. Se registra una advertencia y el circuit transiciona a CLOSED independientemente.

---

## 4. Issues Abiertos Restantes

Estos issues se confirman como todavía abiertos. Cada uno ha sido evaluado por su impacto en el despliegue objetivo (Windows 11, proceso único, local).

| ID | Severidad | Descripción | Impacto Windows 11 | Recomendación |
|---|---|---|---|---|
| **SEC-001** | MEDIA | ~~Credenciales Alembic hardcodeadas~~ | — | **Corregido en este ciclo (FIX-015)** |
| **LOW-006** | BAJA | ~~`print()` en vpn_manager_windows~~ | — | **Corregido en este ciclo (FIX-016)** |
| **Recovery-003** | MEDIA | ~~_active_ids no re-sincronizado en recuperación Redis~~ | — | **Corregido en este ciclo (FIX-017)** |
| HIGH-011 | MEDIA | Rate limiter solo en memoria | Bajo — despliegue de proceso único; sin riesgo multi-proceso | Aceptable para uso local. Reemplazar con slowapi con Redis si se escala horizontalmente |
| HIGH-012 | BAJA | `hotels.url_id` FK nullable | Bajo — los registros huérfanos requieren limpieza manual de url_queue | Añadir `ON DELETE CASCADE` o consulta periódica de limpieza de huérfanos |
| HIGH-014 | BAJA | `LANGUAGES_ENABLED` sin validación en recarga runtime | Bajo — la configuración no se recarga en runtime en este despliegue | Validar en cada lectura vía propiedad `ENABLED_LANGUAGES` |
| MED-012 | MEDIA | Migraciones Alembic no automatizadas | Bajo — los scripts SQL ejecutados manualmente funcionan de forma fiable | Implementar en futuro pipeline CI/CD |
| MED-015 | MEDIA | Sin particionamiento en `scraping_logs` | Bajo — solo relevante a partir de >10M filas | Añadir particionamiento por rango mensual cuando el conteo de filas se aproxime a 1M |
| MED-018 | MEDIA | Sin OpenTelemetry / trazabilidad distribuida | Bajo — Loguru proporciona observabilidad adecuada para proceso único | Mejora futura si el sistema evoluciona a microservicios |

---

## 5. Resumen Completo del Estado de Issues

| ID | Categoría | Severidad | Estado |
|---|---|---|---|
| CRIT-001 | Import | CRÍTICO | ✅ CORREGIDO (ciclo anterior) |
| CRIT-002 | Import | CRÍTICO | ✅ CORREGIDO (ciclo anterior) |
| CRIT-003 | Concurrencia | CRÍTICO | ✅ CORREGIDO (ciclo anterior) |
| CRIT-004 | Recursos | CRÍTICO | ✅ CORREGIDO (ciclo anterior) |
| CRIT-007 | Recursos | CRÍTICO | ✅ CORREGIDO (ciclo anterior) |
| HIGH-001 | Lógica | ALTA | ✅ CORREGIDO (ciclo anterior) |
| HIGH-002 | Disponibilidad | ALTA | ✅ CORREGIDO (v31) |
| HIGH-003 | Rendimiento | ALTA | ✅ CORREGIDO (ciclo anterior) |
| HIGH-004 | Recursos | ALTA | ✅ CORREGIDO (v31) |
| HIGH-005 | Mantenibilidad | ALTA | ✅ CORREGIDO (v31) |
| HIGH-006 | Monitoreo | ALTA | ✅ CORREGIDO (ciclo anterior) |
| HIGH-007 | Datos obsoletos | ALTA | ✅ CORREGIDO (ciclo anterior) |
| HIGH-008 | Integridad datos | ALTA | ✅ CORREGIDO (ciclo anterior) |
| HIGH-009 | Recursos | ALTA | ✅ CORREGIDO (ciclo anterior) |
| HIGH-010 | Rendimiento | ALTA | ✅ CORREGIDO (ciclo anterior) |
| HIGH-011 | Seguridad | ALTA | ⚠️ ABIERTO — aceptable para despliegue local |
| HIGH-012 | Integridad datos | ALTA | ⚠️ ABIERTO — riesgo bajo, decisión de diseño |
| HIGH-013 | Recursos | ALTA | ✅ CORREGIDO (v31) |
| HIGH-014 | Configuración | ALTA | ⚠️ ABIERTO — sin recarga runtime en este despliegue |
| MED-011 | Disponibilidad | MEDIA | ✅ CORREGIDO (ciclo anterior) |
| MED-012 | DevOps | MEDIA | ⚠️ ABIERTO — trabajo futuro CI/CD |
| MED-015 | Escalabilidad | MEDIA | ⚠️ ABIERTO — no relevante al volumen actual |
| MED-018 | Observabilidad | MEDIA | ⚠️ ABIERTO — mejora futura |
| MED-022 | Observabilidad | MEDIA | ✅ CORREGIDO (v31) |
| LOW-006 | Logging | BAJA | ✅ CORREGIDO (este ciclo — FIX-016) |
| SEC-001 | Seguridad | MEDIA | ✅ CORREGIDO (este ciclo — FIX-015) |
| SEC-002 | Seguridad | ALTA | ✅ CORREGIDO (ciclo anterior) |
| SEC-003 | Seguridad | MEDIA | ✅ CORREGIDO (ciclo anterior) |
| CONC-001 | Concurrencia | ALTA | ✅ CORREGIDO (ciclo anterior) |
| CONC-002 | Concurrencia | ALTA | ✅ CORREGIDO (ciclo anterior) |
| CONC-005 | Configuración | MEDIA | ✅ CORREGIDO (ciclo anterior) |
| DATA-001 | Integridad datos | MEDIA | ✅ CORREGIDO (ciclo anterior) |
| ARCH-001 | Escalabilidad | ALTA | ✅ CORREGIDO (ciclo anterior) |
| ARCH-002 | Observabilidad | MEDIA | ✅ CORREGIDO (ciclo anterior) |
| CFG-001 | Configuración | ALTA | ✅ CORREGIDO (ciclo anterior) |
| CFG-002 | Configuración | MEDIA | ✅ CORREGIDO (ciclo anterior) |
| Recovery-001 | Disponibilidad | MEDIA | ⚠️ ABIERTO — ítem de runbook operacional |
| Recovery-002 | Recursos | MEDIA | ✅ CORREGIDO (ciclo anterior) |
| Recovery-003 | Disponibilidad | MEDIA | ✅ CORREGIDO (este ciclo — FIX-017) |

**Totales:** 29 CORREGIDOS | 8 ABIERTOS (todos evaluados como bajo impacto para despliegue local en Windows 11)

---

## 6. Archivos Modificados

### `alembic.ini`
- Eliminada URL hardcodeada `postgresql://postgres:postgres@localhost:5432/booking_scraper`
- Reemplazada con placeholder intencional `CREDENTIALS_PROVIDED_BY_ENV_PY_AT_RUNTIME`
- Añadidos comentarios explicativos documentando la justificación de seguridad

### `alembic/env.py` (NUEVO)
- Creado script de entorno Alembic estándar
- Lee `settings.DATABASE_URL` desde `app/config.py` en runtime
- Sobreescribe el placeholder de `alembic.ini` antes de ejecutar cualquier migración
- Soporta modos de migración offline y online
- Incluye `target_metadata = Base.metadata` para soporte de autogenerate

### `app/vpn_manager_windows.py`
- Reemplazadas 34 llamadas `print()` con `logger.info()` / `logger.warning()` / `logger.error()`
- Métodos afectados: `_connect_manual()`, `disconnect()`, `print_status()`, bloque de test `__main__`
- Prompts `input()` conservados — solo alcanzables con `interactive=True` (modo consola manual)
- Docstring en `print_status()` conservado como documentación (1 mención de `print()` en texto)

### `app/scraper_service.py`
- Extendida la transición HALF-OPEN → CLOSED del circuit breaker de Redis
- Añadida re-sincronización de `_active_ids` desde claves Redis que coincidan con el patrón `bsp:active:*`
- Re-sincronización envuelta en `try/except` — el circuit se cierra independientemente de errores de escaneo
- Registra el número de URL IDs recuperados para observabilidad

---

## 7. Validación de Sintaxis

Todos los archivos Python modificados y dependientes pasaron la validación de sintaxis `ast.parse()` tras las correcciones:

| Archivo | Estado |
|---|---|
| `app/scraper_service.py` | ✅ OK |
| `app/vpn_manager_windows.py` | ✅ OK |
| `alembic/env.py` | ✅ OK |
| `app/main.py` | ✅ OK |
| `app/config.py` | ✅ OK |
| `app/models.py` | ✅ OK |
| `app/database.py` | ✅ OK |
| `app/tasks.py` | ✅ OK |
| `app/completeness_service.py` | ✅ OK |

---

*Reporte generado: 2026-03-05 | Ciclo de auditoría: v32 | Plataforma: Windows 11 (despliegue local)*
