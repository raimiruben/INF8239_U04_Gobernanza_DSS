# Dataset Card

Synthetic territorial-risk dataset generated with a fixed educational seed. It contains no real persons, locations, rates or official Dominican Republic statistics. Intended only to practice contracts, temporal evaluation, subgroup auditing and governance. Prohibited: operational profiling or inference about real populations.

Archivo: `data/territorial_risk_synthetic.csv`. Inventario por campo: `docs/data_inventory.csv`. Marco normativo: `docs/LEGAL_FRAMEWORK.md`.

## Motivación
Practicar el diseño y la auditoría de un sistema de apoyo a la decisión (DSS) para priorizar casos territoriales sintéticos que luego revisa una persona. El conjunto no sirve para decidir sobre personas reales.

## Composición
- 640 filas y 9 columnas: `case_id`, `received_date`, `zone`, `protected_group`, `age_band`, `previous_incidents`, `infrastructure_score`, `exposure` y `target` (etiqueta binaria).
- `protected_group` tiene dos valores (G1 y G2). En el corte de prueba hay 101 casos de G1 y 59 de G2.
- Cada columna tiene un rol (clave, solo para ordenar, variable del modelo, solo para auditoría o etiqueta) en `docs/data_inventory.csv`; una prueba verifica que el inventario cubra todas las columnas.

## Origen y recolección
Datos generados con una semilla fija; no hay recolección de personas reales. Se pueden regenerar de forma idéntica.

## Validación y preprocesamiento
- Al cargar se valida el esquema: columnas obligatorias, rechazo de identificadores directos (`name`, `document_number`, `email`, `phone`) y etiqueta binaria (`src/inf8239_u04/data.py`).
- Los casos se ordenan por `received_date`. El corte temporal usa el primer 75 % (480 casos, hasta el 2026-09-24) para entrenar y el 25 % posterior (160 casos) para evaluar.
- El modelo usa `zone`, `age_band`, `previous_incidents`, `infrastructure_score` y `exposure`. `case_id`, `received_date`, `protected_group` y `target` no son variables del modelo.

## Usos
- **Previstos:** práctica educativa de evaluación temporal, auditoría por subgrupos y gobernanza.
- **Prohibidos:** perfilado operativo, inferencia sobre poblaciones reales, intervención automática, decisión de elegibilidad y declaración de emergencia.

## Minimización
Solo se conservan las nueve columnas necesarias. `protected_group` se usa para auditar y no entra al modelo. `age_band`, que la política declara sensible, sí entra al modelo; el experimento de mitigación (`reports/e07/mitigation_comparison.csv`) indica que retirarla no reduce el recall, y la decisión de retirarla queda pendiente del propietario institucional.

## Retención
- **Datos sintéticos:** se conservan solo en el repositorio del curso y son regenerables con la semilla fija.
- **Si se reemplazaran por datos reales** (no permitido hoy sin autorización formal, riesgo R04): PROPUESTA del proyecto de conservarlos solo mientras dure la finalidad y bloquearlos o suprimirlos después. El plazo lo fija el propietario institucional con Legal. No se encontró en la Ley 172-13 un plazo de conservación con ese nombre, así que no es una exigencia legal.

## Sesgos y límites
- Es sintético: lo medido no describe poblaciones reales.
- Muestra de prueba pequeña (101 y 59 casos); en G2 solo hay 16 negativos.
- Ninguna celda interseccional de `protected_group` por `age_band` llega a 30 positivos ni a 30 negativos.
- `zone` puede actuar como variable proxy del grupo.

## Mantenimiento
Responsable: Data team. Aprobación: Institutional owner. Fecha de revisión: PROPUESTA 2026-11-16, o antes si cambian los datos o el modelo.
