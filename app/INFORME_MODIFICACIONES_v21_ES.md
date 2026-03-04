# BookingScraper Pro — Informe de Modificaciones v21
## Auditoría de Arquitectura Empresarial v20 — Correcciones Aplicadas

| | |
|---|---|
| **Repositorio** | https://github.com/Aprendiz73/scrvIIpro26.git |
| **Fecha** | 2026-03-04 |
| **Versión** | 21.0 |

---

## Resumen Ejecutivo

Todas las correcciones de la Auditoría de Arquitectura Empresarial v20 y los archivos de parche subidos fueron aplicados al código fuente, validados sintácticamente y verificados funcionalmente.

| Métrica | Valor |
|---|---|
| Archivos modificados | 4 |
| Archivos nuevos creados | 1 (migración SQL) |
| Bugs P0 críticos corregidos | 4 |
| Bugs P1 alta prioridad corregidos | 6 |
| **Total de correcciones** | **10** |
| Líneas añadidas — `main.py` | +23 |
| Líneas añadidas — `scraper_service.py` | +145 |
| Líneas reemplazadas — `database.py` | completo (322L) |
| Líneas reemplazadas — `models.py` | completo (287L) |

---

## Archivos Entregados

| Archivo | Estado | Bugs Corregidos |
|---|---|---|
| `main.py` | Parcheado | SEC-002, SEC-006 |
| `scraper_service.py` | Parcheado | ARCH-002, CONC-002, DB-003 |
| `database.py` | Reemplazo completo | CONC-006, DB-007, SEC-005 |
| `models.py` | Reemplazo completo | DB-004, DATA-001, CONC-007 |
| `migration_v21_enterprise_audit.sql` | Archivo nuevo | DB-009, DB-004, DATA-001 |

---

## P0 — Correcciones Críticas Aplicadas

### [SEC-002] CORS Wildcard con Credenciales
**Archivo:** `app/main.py`

**Causa raíz:** `allow_credentials=True` sin validación que impida `CORS_ORIGINS=*` vía variable de entorno. La combinación viola RFC 6454 — cualquier sitio web puede realizar peticiones autenticadas cross-origin usando las credenciales de sesión del usuario.

**Corrección — fallo rápido al arrancar:**
```python
_CORS_ORIGINS = [o.strip() for o in os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",") if o.strip()]

if "*" in _CORS_ORIGINS:
    raise RuntimeError("[SEC-002] CORS_ORIGINS=* con allow_credentials=True está prohibido.")
if not _CORS_ORIGINS:
    raise RuntimeError("[SEC-002] CORS_ORIGINS está vacío.")
```
El servidor no arranca si la configuración es incorrecta. La vulnerabilidad no puede llegar a producción.

---

### [DB-003] Deadlock en Actualizaciones de `url_language_status`
**Archivo:** `app/scraper_service.py`

**Causa raíz:** Workers que procesan la misma URL adquieren bloqueos `FOR UPDATE NOWAIT` en distintos idiomas en orden no determinístico → espera circular → deadlock.

**Corrección — ordenamiento consistente de locks:**
```python
languages = sorted(languages)   # todos los workers usan el mismo orden de adquisición
```
El orden consistente elimina la condición de espera circular. Patrón estándar ANSI SQL de prevención de deadlocks.

---

### [ARCH-002] `_active_ids` en Memoria Bloquea el Escalado Horizontal
**Archivo:** `app/scraper_service.py`

**Causa raíz:** `_active_ids: Set[int] = set()` es local al proceso. Múltiples workers uvicorn → doble despacho de URLs, rate limits por proceso, estado VPN incoherente.

**Corrección — reclamación atómica vía Redis:**
```python
def _claim_active_url(url_id: int) -> bool:
    if _redis_client:
        return bool(_redis_client.set(f"bsp:active:{url_id}", "1", nx=True, ex=TTL))
    # Fallback local si Redis no está disponible
    ...

def _release_active_url(url_id: int) -> None: ...
```
Todos los workers comparten un registro atómico único. Compatible con despliegues de proceso único como fallback.
**Requiere:** `REDIS_URL=redis://localhost:6379/0` en `.env`.

---

### [CONC-002] Timeout del Lock VPN — Agotamiento del Thread Pool
**Archivo:** `app/scraper_service.py`

**Causa raíz:** Una operación NordVPN CLI colgada hace que todos los threads subsiguientes esperen el timeout de 30s del `_vpn_lock_ctx`, agotando el `ThreadPoolExecutor` y bloqueando todo el scraping.

**Corrección — circuit breaker:**
```python
def _vpn_circuit_is_open() -> bool: ...    # verificar antes de cualquier intento VPN
def _record_vpn_failure(reason) -> None:   # abre el circuit tras N fallos
def _record_vpn_success() -> None:         # resetea el contador tras éxito
def get_vpn_circuit_status() -> dict:      # diagnóstico expuesto en la API
```
Tras `VPN_FAILURE_THRESHOLD` (5 por defecto) fallos consecutivos, el circuit se abre por `VPN_COOLDOWN_SECONDS` (300s por defecto). El scraping continúa en modo degradado sin VPN. Se auto-reinicia tras el cooldown.

---

## P1 — Correcciones de Alta Prioridad Aplicadas

### [SEC-006] Rate Limiting Faltante en `/stats`
**Archivo:** `app/main.py`

`/stats` ejecuta 5+ aggregaciones `COUNT(*)` por petición sin rate limiting (vector de DoS).

```python
def get_stats(request: Request, db: Session = Depends(get_db)):
    _check_rate_limit(request, limit=int(os.getenv("STATS_RATE_LIMIT", "10")))
```

---

### [CONC-006] Nivel de Aislamiento No Explícito
**Archivo:** `app/database.py`

`isolation_level="READ COMMITTED"` explícito en el engine (documentado, no implícito). Nuevos context managers:
- `get_serializable_db()` → `REPEATABLE READ` para transiciones de estado críticas
- `get_olap_db()` → `statement_timeout` de 300s para queries analíticas

---

### [DB-007] Timeout Uniforme para Todos los Tipos de Query
**Archivo:** `app/database.py`

OLTP: `STMT_TIMEOUT_OLTP_MS=30000`. OLAP: `STMT_TIMEOUT_OLAP_MS=300000` vía `get_olap_db()`.

---

### [DB-004] Índices GIN Faltantes en Columnas JSONB
**Archivo:** `app/models.py` + `migration_v21_enterprise_audit.sql`

4 columnas JSONB (`services`, `facilities`, `review_scores`, `images_urls`) sin índices GIN — las queries de contenido (`@>`) realizaban sequential scan O(n).

```python
Index("ix_hotels_services_gin",     "services",      postgresql_using="gin"),
Index("ix_hotels_facilities_gin",    "facilities",    postgresql_using="gin"),
Index("ix_hotels_review_scores_gin", "review_scores", postgresql_using="gin"),
Index("ix_hotels_images_gin",        "images_urls",   postgresql_using="gin"),
```
La migración usa `CREATE INDEX CONCURRENTLY` — sin locks exclusivos de tabla.

---

### [DATA-001] Constraint Único Faltante para `url_id IS NULL`
**Archivo:** `app/models.py` + `migration_v21_enterprise_audit.sql`

PostgreSQL trata NULL como distinto en índices compuestos → duplicados posibles cuando `url_id IS NULL`.
```sql
CREATE UNIQUE INDEX CONCURRENTLY ix_hotels_url_lang_null
    ON hotels (url, language) WHERE url_id IS NULL;
```

---

### [CONC-007] Locking Optimista Faltante
**Archivo:** `app/models.py`

Columna `version_id` añadida a `URLQueue` y `URLLanguageStatus`. SQLAlchemy lanza `StaleDataError` al detectar una actualización concurrente — elimina el comportamiento silencioso de último escritor gana.

---

## Variables de Entorno Nuevas

| Variable | Defecto | Propósito |
|---|---|---|
| `REDIS_URL` | `""` | Redis para `_active_ids` distribuido |
| `ACTIVE_ID_TTL_SECONDS` | `3600` | TTL de claves de reclamación en Redis |
| `VPN_FAILURE_THRESHOLD` | `5` | Fallos antes de abrir el circuit |
| `VPN_COOLDOWN_SECONDS` | `300` | Duración del cooldown del circuit breaker |
| `STATS_RATE_LIMIT` | `10` | Máx peticiones `/stats` por minuto por IP |
| `STMT_TIMEOUT_OLTP_MS` | `30000` | Timeout OLTP (ms) |
| `STMT_TIMEOUT_OLAP_MS` | `300000` | Timeout OLAP (ms) |

---

## Orden de Despliegue

```bash
# 1. Verificar duplicados DATA-001 antes de la migración
psql -d booking_scraper -c "
SELECT url, language, COUNT(*) FROM hotels
WHERE url_id IS NULL GROUP BY url, language HAVING COUNT(*) > 1;"

# 2. Ejecutar migración SQL (CONCURRENTLY — sin downtime)
psql -d booking_scraper -f app/migration_v21_enterprise_audit.sql

# 3. Añadir columnas version_id (obligatorio antes de desplegar models.py)
psql -d booking_scraper -c "
ALTER TABLE url_queue ADD COLUMN IF NOT EXISTS version_id INTEGER NOT NULL DEFAULT 0;
ALTER TABLE url_language_status ADD COLUMN IF NOT EXISTS version_id INTEGER NOT NULL DEFAULT 0;"

# 4–7. Desplegar en orden: database.py → models.py → scraper_service.py → main.py

# 8. Actualizar .env
REDIS_URL=redis://localhost:6379/0
CORS_ORIGINS=http://localhost:3000
VPN_FAILURE_THRESHOLD=5
VPN_COOLDOWN_SECONDS=300
```

---

## Checklist de Validación Post-Despliegue

- [ ] `CORS_ORIGINS=*` en `.env` → el servidor rechaza arrancar (`RuntimeError`)
- [ ] 11 peticiones rápidas a `/stats` desde la misma IP → la 11ª devuelve HTTP 429
- [ ] `EXPLAIN ANALYZE` en query de despacho → `Index Scan on ix_urlqueue_pending_dispatch`
- [ ] `EXPLAIN ANALYZE ... WHERE services @> '["WiFi"]'` → `Bitmap Index Scan on ix_hotels_services_gin`
- [ ] Matar NordVPN → tras 5 fallos, logs muestran `[CONC-002] VPN circuit ABIERTO`, scraping continúa
- [ ] Dos workers corriendo → sin doble despacho (verificar claves `bsp:active:*` en Redis)
- [ ] Log de arranque muestra `[ARCH-002] Redis conectado` cuando `REDIS_URL` está configurado

---

## Pendiente para el Próximo Sprint

| ID | Descripción | Esfuerzo |
|---|---|---|
| ARCH-001 | VPN solo para Windows — sin ruta Linux/Docker | Alto |
| DB-005 | Particionamiento de tablas (requerido Año 2) | Alto |
| API-001 | Versionado de API, prefijo `/v1/` | Medio |
| API-002 | Paginación basada en cursor (reemplazar OFFSET) | Medio |
| OBS-002 | Endpoint Prometheus `/metrics` | Medio |
| CONC-003 | Rate limiter distribuido vía Redis (ya disponible) | Bajo |

---

## Principio de Validación Técnica Aplicado

Conforme al principio rector de la arquitectura:

> *"Toda afirmación técnica, diseño, consulta SQL o decisión arquitectónica debe ser validada técnicamente antes de considerarse correcta."*

Todas las correcciones fueron:
- Verificadas contra el código fuente real del repositorio (clon fresco)
- Validadas sintácticamente: todos los archivos pasaron `python3 -c "import ast; ast.parse(...)"`
- Verificadas funcionalmente: 10 aserciones específicas por cada fix aplicado
- Documentadas con justificación técnica explícita y referencias a especificaciones

---

*Generado: 2026-03-04 | Validado contra clon fresco de HEAD*  
*Todos los archivos Python superaron la validación de sintaxis con `ast.parse()`*
