# Marco normativo: obligación legal, marco voluntario y recomendación ética

Sistema: Territorial Review DSS (sintético). Elaborado el 2026-10-16. Este documento distingue tres tipos de fuente porque no obligan por igual.

> **Alcance.** Los datos del proyecto son sintéticos (ver `docs/DATASET_CARD.md`): no contienen personas, lugares ni estadísticas reales. Por eso la obligación legal **no se aplica hoy** a este conjunto de datos, pero se documenta qué exigiría si se usaran datos reales.

## 1. Obligación legal (obliga si hubiera datos personales reales)

**Fuente:** Ley núm. 172-13 sobre Protección Integral de los Datos Personales (República Dominicana), promulgada el 13 de diciembre de 2013.

| Referencia | Qué establece | Cómo lo atiende el proyecto | Evidencia |
|---|---|---|---|
| Art. 1 (objeto) | Protección integral de los datos personales asentados en archivos y registros. | El esquema rechaza identificadores directos (`name`, `document_number`, `email`, `phone`). | `src/inf8239_u04/data.py`, `tests/test_privacy.py` |
| Art. 5 (principios) | Licitud, calidad, lealtad, finalidad y seguridad del tratamiento (datos ciertos, adecuados, pertinentes y no excesivos). | Finalidad escrita y usos prohibidos; solo se conservan las 9 columnas necesarias; inventario con minimización por campo. | `configs/governance.yml`, `docs/data_inventory.csv`, `tests/test_artifacts.py` |
| Art. 6 (definiciones) | Define dato personal y dato sensible (opiniones políticas, convicciones religiosas, afiliación sindical, salud y vida sexual, entre otros). | La política del proyecto trata `protected_group` y `age_band` como sensibles. Es una decisión del proyecto, no necesariamente la lista legal. | `configs/governance.yml` |
| Arts. 10 y 14 (acceso y rectificación) | Derecho a acceder a los datos propios y a que se rectifiquen, actualicen o supriman. | Mecanismo de apelación: revisión humana independiente con respuesta escrita en 10 días hábiles. | `student_inputs/lab11_impact.yml`, `docs/RUNBOOK.md` |
| Arts. 17 a 24 (hábeas data) | Vía judicial para exigir acceso, rectificación o supresión. | No aplicable al conjunto sintético; si hubiera datos reales, Legal debe revisar este canal. | `student_inputs/raci.csv` (Legal como Consulted) |

**Límites de esta lectura.**
- Los números de artículo salen de una copia de la ley consultada en línea; el texto leído se interrumpía en el Art. 83 y tenía erratas. Antes de citar un artículo en el informe, hay que contrastarlo con la versión de la Gaceta Oficial.
- No se encontró en el texto consultado un principio de plazo de conservación con ese nombre. Por eso el plazo de retención de datos reales en este proyecto **no es una exigencia legal** sino una propuesta del proyecto que decide el propietario institucional con Legal.
- Este documento no es asesoría legal.

## 2. Marco voluntario

**Fuente:** NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, 26 de enero de 2023. Es de uso voluntario: no obliga a nadie.

Se usa para organizar la gestión de riesgos en cuatro funciones (Govern, Map, Measure, Manage). La correspondencia con evidencias del repositorio está en `docs/NIST_AI_RMF_MAPPING.md`.

## 3. Recomendación ética

**Fuente:** UNESCO, *Recommendation on the Ethics of Artificial Intelligence*, adoptada en noviembre de 2021 por los 193 Estados miembros. Es un instrumento de recomendación.

| Principio de la Recomendación | Cómo se refleja en el proyecto | Evidencia |
|---|---|---|
| Proporcionalidad y no hacer daño | Se limita el uso a priorizar la cola de revisión humana; se prohíben intervención automática, elegibilidad y declaración de emergencia. | `configs/governance.yml`, `reports/lab11/DECISION_RECORD.md` |
| Equidad y no discriminación | Auditoría por grupo e interseccional, brechas de recall y de FPR con umbral, y experimento de mitigación. | `reports/lab12/`, `reports/e07/mitigation_comparison.csv` |
| Supervisión y determinación humanas | La persona revisora decide; el sistema solo propone el orden; el sistema no puede cerrar ni descartar un caso. | `student_inputs/lab11_impact.yml`, `docs/MODEL_CARD.md` |
| Transparencia y explicabilidad | Model Card, Dataset Card, interpretación de la auditoría y aviso visible en la app. | `docs/`, `app.py` |
| Responsabilidad y rendición de cuentas | RACI con un único Accountable por actividad (verificado por prueba) y runbook con simulacro. | `student_inputs/raci.csv`, `docs/RUNBOOK.md` |
| Privacidad y protección de datos | Datos sintéticos, minimización y rechazo de identificadores directos. | `docs/data_inventory.csv`, `tests/test_privacy.py` |
| Sostenibilidad | Modelo suficiente: 3,56 KB, entrenamiento en menos de 0,3 s, sin hardware especial. | `reports/lab13/deployment_decision.json` |

## 4. Qué es política del proyecto (ni ley ni recomendación externa)

Los usos prohibidos, los umbrales de las puertas (recall mínimo 0,68, brechas máximas 0,16, latencia 500 ms, tamaño 1 024 KB) y la condición de retiro son reglas de la política del proyecto (`configs/governance.yml`). Las fija el propietario institucional; no vienen de la ley ni de NIST ni de UNESCO.

## Fuentes

- Ley núm. 172-13 sobre protección de datos de carácter personal (texto consultado: https://drlawyer.com/espanol/leyes/ley-172-13-sobre-proteccion-de-datos-de-caracter-personal/; otras copias: https://pwc.com/ia/es/servicios/Regulacion-Legal/RD-Ley-172-13%20.pdf y https://bdi.com.do/media/lx0bzgfe/ley-sobre-proteccion-datos-caracter-personal.pdf). Contrastar con la Gaceta Oficial.
- NIST AI RMF 1.0: https://www.nist.gov/itl/ai-risk-management-framework (PDF: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf).
- UNESCO, Recommendation on the Ethics of Artificial Intelligence: https://www.unesco.org/en/artificial-intelligence/recommendation-ethics
