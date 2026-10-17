# Declaración de uso de IA

**Herramienta:** Claude (Anthropic), asistente de IA usado en el chat de claude.ai durante LAB11, LAB12 y LAB13.

**Finalidad:** guía paso a paso de los laboratorios; explicación de los conceptos del manual y de las reglas que aplican los scripts del proyecto; redacción de borradores de los archivos de contenido; diagnóstico de errores en dos scripts del proyecto.

## LAB11 · Evaluación de impacto

**Fragmentos afectados** (los borradores de la IA se adoptaron sin cambios):
- `student_inputs/lab11_impact.yml`: los nueve campos son el borrador propuesto por la IA; no los modifiqué.
- `student_inputs/stakeholders.csv`: beneficio, daño y participación de los cuatro actores son el borrador propuesto por la IA; no los modifiqué.
- `student_inputs/risk_register.csv`: los escenarios, afectados, controles, responsables y evidencias de R01 a R08 son la propuesta de la IA, ajustada a la probabilidad, el impacto y el residual ya fijados en la plantilla; no modifiqué ningún riesgo.
- `reports/lab11/DECISION_RECORD.md`: la estructura y el texto los propuso la IA, incluida la decisión REVIEW, que mantuve sin cambios.
- `scripts/lab11_impact.py`: la corrección de la cadena de texto (una línea con `\n`) fue indicada por la IA y la apliqué manualmente en el editor.

## LAB12 · Auditoría de equidad

**Fragmentos afectados:**
- `student_inputs/lab12_decision.yml`: los seis campos son el borrador propuesto por la IA a partir de los resultados de la auditoría; no los modifiqué.
- `reports/lab12/INTERPRETATION.md`: la estructura, la tabla de soporte por grupo y el texto los propuso la IA; no los modifiqué. El criterio de al menos 30 casos de la clase relevante para interpretar un grupo fue propuesto por la IA, porque el proyecto no define un mínimo.

## LAB13 · Gobernanza y DSS responsable

**Fragmentos afectados:**
- `student_inputs/raci.csv`: las siete actividades y los roles (Data team, Institutional owner, Operator, Legal, Affected representatives) son el borrador propuesto por la IA; no los modifiqué.
- `docs/MODEL_CARD.md` y `docs/RUNBOOK.md`: el texto lo propuso la IA a partir de la evidencia de LAB11 y LAB12 y de los resultados de LAB13; no lo modifiqué. La fecha de revisión de la Model Card (2026-11-16) y el plazo del postmortem (5 días hábiles) fueron propuestos por la IA y los mantuve.
- `reports/lab13/INCIDENT_POSTMORTEM.md`: la redacción de la comunicación y de las acciones correctivas, con sus responsables y fechas, la propuso la IA; no la modifiqué. El ejercicio es una simulación.
- `app.py`: la línea final que muestra la decisión humana documentada (REVIEW) fue propuesta por la IA y la añadí manualmente.
- `scripts/simulate_incident.py`: la corrección (comillas triples en el texto de varias líneas) fue indicada por la IA y la apliqué manualmente en el editor.

## Verificaciones humanas

- Ejecuté las pruebas del proyecto (10 en verde) y los scripts de LAB11, LAB12 y LAB13, y consulté sus salidas: `risk_register_scored.csv`, las auditorías de los modelos logistic y tree, y `deployment_decision.json`.
- Consulté en el código cómo se calculan la prioridad de los riesgos, las métricas por grupo, la validación del RACI y las puertas de decisión (`impact.py`, `fairness.py`, `governance.py`, `pipeline.py`).
- Consulté los archivos del caso en los que se basaron los borradores: `README.md`, `docs/DATASET_CARD.md` y `configs/governance.yml`.
- Comprobé con una búsqueda que no quedaban marcadores `REPLACE` en los archivos completados.
- Ejecuté la aplicación Streamlit y revisé las métricas globales y por grupo y las puertas de calidad.

## Errores detectados y correcciones

- `scripts/lab11_impact.py` y `scripts/simulate_incident.py` del proyecto base tenían un error de sintaxis (una cadena de texto partida en varias líneas). La IA no lo advirtió al leer el primero y se detectó al ejecutarlo; ambos se corrigieron.
- `rmf_summary.json` se genera con texto fijo: no mide controles reales, así que no se usó como evidencia de que los controles funcionan.
- `lab11_impact.py` sobrescribe `DECISION_RECORD.md` en cada ejecución, y `simulate_incident.py` hace lo mismo con el postmortem; los documentos se escribieron después de la última ejecución.
- Los resultados de LAB12 se guardan en `reports/lab12/<modelo>/`, no en la raíz de `reports/lab12/`, algo que el manual no indica.
- `validate_raci` solo comprueba que R y A no estén vacíos; no exige un único Accountable por actividad. El RACI se revisó manualmente para cumplir esa regla.
- La decisión automática del script de LAB13 es GO (las cinco puertas pasan), pero las puertas no evalúan el recall por grupo (G1 queda en 0,653, por debajo del mínimo de 0,68), el soporte de los grupos es pequeño y `age_band`, declarada sensible, entra al modelo. Por eso la decisión humana documentada es REVIEW, y la aplicación lo indica de forma visible.
- La primera versión de esta declaración para LAB11 (commit `38b3c0b`) se guardó con apartados sin completar y con caracteres de escape en los nombres de archivo. Se detectó con una búsqueda posterior y se corrigió en un commit nuevo.
- La señal del simulacro de incidente ("recall gap exceeded") está escrita fija en el script y no procede de una medición real.

**Responsabilidad:** asumo la responsabilidad sobre el contenido entregado.
