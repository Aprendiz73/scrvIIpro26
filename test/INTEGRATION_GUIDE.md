# GUÍA DE INTEGRACIÓN v6.0 — Control de Completitud por Idioma
## BookingScraper Pro — Arquitectura Empresarial

---

## I. ARCHIVOS ENTREGADOS

| Archivo | Tipo | Descripción |
|---|---|---|
| `completeness_service.py` | NUEVO | Servicio de tracking por idioma, status files, rollback |
| `migration_v2_url_language_status.sql` | NUEVO | Migración PostgreSQL: tabla + índices + vista + constraint |
| `scraper_service_v6_patch.py` | PARCHE | Cambios a aplicar en `scraper_service.py` |
| `tasks_v4_patch.py` | PARCHE | Cambios a aplicar en `tasks.py` |
| `main_endpoints_patch.py` | PARCHE | Nuevos endpoints FastAPI para `main.py` |

---

## II. SECUENCIA DE INTEGRACIÓN (ORDEN OBLIGATORIO)

### Paso 1 — Ejecutar migración SQL

```bash
# En la máquina con acceso a PostgreSQL
psql -U postgres -d booking_scraper -f migration_v2_url_language_status.sql
```

Verificar:
```sql
-- Confirmar tabla creada
SELECT column_name, data_type, column_default
FROM information_schema.columns
WHERE table_name = 'url_language_status'
ORDER BY ordinal_position;

-- Confirmar vista creada
SELECT * FROM vw_url_completeness LIMIT 5;

-- Confirmar constraint en url_queue
SELECT conname FROM pg_constraint
WHERE conrelid = 'url_queue'::regclass;
```

### Paso 2 — Copiar completeness_service.py

```
C:\BookingScraper\app\completeness_service.py
```

### Paso 3 — Modificar scraper_service.py

**3a.** Añadir import (después de `from app.config import settings`):
```python
from app.completeness_service import completeness_service, MAX_LANG_RETRIES
```

**3b.** En `process_batch()`, añadir al inicio del cuerpo:
```python
MAX_BATCH_CAP = 10
if batch_size > MAX_BATCH_CAP:
    logger.warning(f"batch_size={batch_size} > {MAX_BATCH_CAP}, reduciendo")
    batch_size = MAX_BATCH_CAP
```

**3c.** En `scrape_one()`, reemplazar el bloque completo del bucle de idiomas
(desde `# [v3.1] Flag: imágenes descargadas` hasta el `return {...)` final)
con la función `_scrape_one_language_loop_v6` del parche + la llamada indicada.

Ver `scraper_service_v6_patch.py` para el código exacto.

### Paso 4 — Modificar tasks.py

Reemplazar `process_pending_urls()` con la versión del parche.
Añadir `rollback_url_task()`, `get_url_completeness_task()`,
`check_incomplete_urls_task()` del parche.

### Paso 5 — Modificar main.py

Añadir los 3 endpoints del parche `main_endpoints_patch.py`.
Añadir import: `from app.completeness_service import completeness_service`

### Paso 6 — Añadir tarea periódica al beat_schedule (celery_app.py)

```python
"check-incomplete-urls": {
    "task": "app.tasks.check_incomplete_urls_task",
    "schedule": crontab(hour="*/6"),  # cada 6 horas
},
```

---

## III. DISEÑO DE BASE DE DATOS — ANÁLISIS TÉCNICO

### Tabla `url_language_status`

**Normalización**: 3FN cumplida. La PK es `id`. Los atributos `status`,
`retry_count`, `last_error` dependen funcionalmente de `(url_id, language)`.
El UNIQUE constraint en `(url_id, language)` garantiza la integridad
de la clave candidata natural.

**Cardinalidad**: `N_urls × N_idiomas`. Con 5 idiomas habilitados y 10K URLs = 50K filas.
Con 100K URLs = 500K filas. Completamente manejable sin particionamiento.

**Índices diseñados**:

| Índice | Tipo | Columnas | Query que acelera |
|---|---|---|---|
| `ix_uls_url_id` | B-Tree | `url_id` | JOIN con url_queue |
| `ix_uls_url_id_status` | B-Tree (compuesto) | `url_id, status` | Verificación de completitud |
| `ix_uls_failed_updated` | B-Tree parcial | `updated_at WHERE failed` | Alertas de fallos |
| `ix_uls_pending_retry` | B-Tree parcial | `url_id, language WHERE pending AND retry>0` | Reintentos pendientes |

**Plan de ejecución esperado** para la query de completitud:
```sql
SELECT language, status FROM url_language_status WHERE url_id = :id
```
→ `Index Scan on ix_uls_url_id` → sin heap fetch si ix_uls_url_id_status
es un índice covering (incluye `status`).

**Riesgo de locks**: Las operaciones `UPDATE url_language_status` usan
`FOR UPDATE` explícito (en `record_language_failure`) para serializar
actualizaciones concurrentes del mismo idioma. Riesgo de deadlock: mínimo
porque el lock es por fila única `(url_id, language)`.

### Vista `vw_url_completeness`

Consulta segura para dashboard:
```sql
SELECT * FROM vw_url_completeness WHERE langs_failed > 0;
```

Para URLs específicas:
```sql
SELECT * FROM vw_url_completeness WHERE url_id = 417;
```

---

## IV. LÓGICA DE ESTADOS — MÁQUINA DE ESTADOS

### url_language_status.status

```
[pending] ──────────────────→ [scraping] → [completed] ✓
    │                                    → [skipped_existing] ✓
    │
    └──→ (primer fallo) → retry_count=1 → [pending] ──→ [completed] ✓
                                               │
                                               └─→ (segundo fallo) → retry_count=2 → [failed] ✗
```

### url_queue.status con el nuevo estado

```
[pending] → [processing] → [completed]   (todos idiomas OK)
                        → [incomplete]   (algún idioma failed tras max_retries)
                        → [failed]       (error fatal, sin ningún idioma guardado)

[incomplete] → (rollback manual) → [pending] → ...
```

### Archivos de estado

```
Inicio scraping:   in_process.txt  (se crea)
Fin exitoso:       completed.txt   (se crea), in_process.txt (se borra)
Fin con fallos:    incomplete.txt  (se crea), in_process.txt (se borra)
Rollback:          (toda la carpeta hotel_{url_id}/ se elimina)
```

---

## V. ROLLBACK — SECUENCIA DE OPERACIONES

El rollback es la acción más delicada del sistema. La secuencia garantiza
que si el proceso muere en cualquier punto, el sistema queda en estado
recuperable:

```
1. Verificar url_queue.status ≠ 'processing' (bloquear si está en proceso)
2. DELETE hotels WHERE url_id = :url_id
3. DELETE url_language_status WHERE url_id = :url_id
4. UPDATE url_queue SET status='pending', retry_count=0 WHERE id = :url_id
5. COMMIT (punto de no retorno para la BD — estado consistente)
6. shutil.rmtree(hotel_{url_id}/)
```

Si el proceso muere entre pasos 5 y 6: la BD está en estado correcto
(URL en 'pending'), pero queda la carpeta de imágenes huérfana. Al
reiniciar el proceso, la URL se tomará como 'pending' y el scraper
creará una carpeta nueva. La carpeta huérfana debe limpiarse manualmente.

---

## VI. IMPACTO EN ESCALABILIDAD

### Escalabilidad horizontal (múltiples workers)

El `completeness_service` es **stateless** — múltiples workers pueden
llamarlo concurrentemente sin coordinación explícita:

- `initialize_url_processing`: idempotente via `ON CONFLICT DO NOTHING`
- `record_language_success/failure`: usa `FOR UPDATE` en la fila específica → serialización por fila, no por tabla
- `finalize_url`: protegida con `WHERE status NOT IN ('completed')` para TOCTOU

### Escalabilidad vertical

La vista `vw_url_completeness` puede materializarse si el dashboard
genera demasiada carga:
```sql
-- Materializar como MATERIALIZED VIEW si la vista es lenta
CREATE MATERIALIZED VIEW mv_url_completeness AS
SELECT * FROM vw_url_completeness;

REFRESH MATERIALIZED VIEW CONCURRENTLY mv_url_completeness;
```

### Límites esperados

| Métrica | Valor actual | Límite estimado sin rediseño |
|---|---|---|
| URLs en url_queue | 16 | ~500K |
| Filas en url_language_status | 0 | ~2.5M (500K × 5 idiomas) |
| Concurrencia de workers | 1 (max_workers=1) | 10 (con índices actuales) |
| Tiempo de verificación de completitud | <5ms | <50ms hasta 10M filas |

---

## VII. RIESGOS Y MITIGACIÓN

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Crash entre commit BD y borrado de carpeta en rollback | Baja | Medio | Carpeta huérfana; URL en 'pending' → nuevo scraping crea carpeta nueva |
| Worker A y B finalizan la misma URL simultáneamente | Muy baja | Bajo | `WHERE status NOT IN ('completed')` en finalize_url protege la idempotencia |
| url_language_status fuera de sync con hotels | Baja | Bajo | check_completeness() hace validación cruzada con ambas tablas |
| Carpeta de imágenes llena de `in_process.txt` huérfanos (crash a mitad) | Media | Bajo | Al reiniciar, initialize_url_processing() sobreescribe el archivo |
| Rollback ejecutado sobre URL en estado 'processing' | Baja | Alto | API retorna HTTP 409 Conflict; operador debe esperar o detener worker |

---

## VIII. QUERIES DE MONITOREO RECOMENDADAS

```sql
-- URLs incompletas (acción requerida del operador)
SELECT url_id, url, failed_languages, ok_languages
FROM vw_url_completeness
WHERE langs_failed > 0
ORDER BY scraped_at DESC;

-- Idiomas que más fallan (para detectar problemas de VPN o Booking.com)
SELECT language, COUNT(*) AS failures
FROM url_language_status
WHERE status = 'failed'
GROUP BY language
ORDER BY failures DESC;

-- URLs en proceso con archivos de estado (verificar stale processes)
SELECT q.id, q.url, q.status, q.updated_at,
       NOW() - q.updated_at AS tiempo_en_proceso
FROM url_queue q
WHERE q.status = 'processing'
  AND q.updated_at < NOW() - INTERVAL '30 minutes'
ORDER BY q.updated_at;

-- Tasa de éxito por idioma (últimas 24 horas)
SELECT
    language,
    COUNT(*) FILTER (WHERE status = 'completed') AS ok,
    COUNT(*) FILTER (WHERE status = 'failed')    AS failed,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE status = 'completed')
        / NULLIF(COUNT(*), 0), 1
    )                                             AS pct_ok
FROM url_language_status
WHERE updated_at > NOW() - INTERVAL '24 hours'
GROUP BY language
ORDER BY language;
```
