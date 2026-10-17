# Declaración de uso de IA

**Herramienta:** Claude (Anthropic), asistente de IA usado en el chat de claude.ai durante LAB11, LAB12, LAB13 y los ejercicios E07 y E08 de la Unidad 04.

**Finalidad:** guía paso a paso de los laboratorios; explicación de los conceptos del manual y de las reglas que aplican los scripts del proyecto; redacción de borradores de archivos de contenido y de documentación; escritura de un script de experimento y de pruebas automáticas; búsqueda de fuentes normativas; diagnóstico de errores en dos scripts del proyecto.

## Prompts relevantes (resumidos con mis palabras)

1. "Guíame paso a paso en el LAB11, LAB12 y LAB13 (PowerShell y uv en Windows); te paso las capturas de cada salida."
2. "Redacta los borradores de `lab11_impact.yml`, `stakeholders.csv`, `risk_register.csv` y del registro de decisión, a partir de la plantilla y de los documentos del caso."
3. "Interpreta la auditoría de equidad de LAB12 (global, por grupo e interseccional) y propón la decisión y la advertencia de soporte insuficiente."
4. "Completa `raci.csv`, la Model Card, el Runbook y el postmortem del simulacro con la evidencia de LAB11 y LAB12."
5. "Lee los enunciados de los ejercicios E07 y E08 y dime qué huecos tiene mi repositorio frente a la rúbrica."
6. "Propón un experimento de mitigación (quitar `age_band` o `zone`), pruebas automáticas y un inventario de datos."
7. "Busca y verifica fuentes para separar obligación legal, marco voluntario y recomendación ética."
8. "Prepara los PDF de síntesis de E07 y E08 y la declaración de uso de IA a partir de lo que hicimos."

## Fragmentos afectados

Los borradores de la IA se adoptaron sin cambios, salvo donde se indica.

**LAB11**
- `student_inputs/lab11_impact.yml`, `student_inputs/stakeholders.csv` y `student_inputs/risk_register.csv` (escenarios, afectados, controles, responsables y evidencias de R01 a R08, ajustados a la probabilidad, el impacto y el residual ya fijados en la plantilla): propuestos por la IA.
- `reports/lab11/DECISION_RECORD.md`: texto de LAB11 propuesto por la IA; la versión final de E07 (decisión LIMITAR) también la redactó la IA y yo la adopté.
- `scripts/lab11_impact.py`: corrección de la cadena de texto indicada por la IA y aplicada por mí.

**LAB12**
- `student_inputs/lab12_decision.yml` y `reports/lab12/INTERPRETATION.md`: propuestos por la IA. El criterio de al menos 30 casos de la clase relevante para interpretar un grupo lo propuso la IA, porque el proyecto no define un mínimo.

**LAB13**
- `student_inputs/raci.csv`, `docs/MODEL_CARD.md`, `docs/RUNBOOK.md` y `reports/lab13/INCIDENT_POSTMORTEM.md`: propuestos por la IA a partir de la evidencia de LAB11 y LAB12. La fecha de revisión (2026-11-16), el plazo del postmortem (5 días hábiles) y las fechas y responsables de las acciones correctivas son propuestas de la IA que mantuve.
- `app.py`: la línea final con la decisión humana documentada fue propuesta por la IA y la añadí yo.
- `scripts/simulate_incident.py`: corrección indicada por la IA (comillas triples) y aplicada por mí.

**E07 y E08**
- `scripts/e07_mitigation.py`: la IA escribió el experimento (cuatro variantes del modelo logistic, intervalo bootstrap de la brecha de recall); yo lo ejecuté y revisé la salida.
- `scripts/e07_update_register.py`: la IA escribió la actualización de la columna de evidencias de R01, R03, R04, R05 y R07; yo lo ejecuté.
- `tests/test_artifacts.py` y `docs/data_inventory.csv`: pruebas e inventario propuestos por la IA.
- `docs/LEGAL_FRAMEWORK.md`, `docs/NIST_AI_RMF_MAPPING.md`, `docs/DATASET_CARD.md` y `docs/EVIDENCE_INDEX.md`: redactados por la IA a partir de los archivos del repositorio y de fuentes consultadas por la IA.
- PDF de síntesis de E07 y E08: redactados por la IA a partir de las evidencias del repositorio.

## Decisiones que tomé yo

- La decisión final de E07 es **LIMITAR**. La IA recomendó esa opción con base en los resultados medidos, y yo la elegí entre desplegar, modificar, limitar y no utilizar.
- No cambié el pipeline principal para quitar `age_band`: queda como mejora a decidir por el propietario institucional.

## Verificaciones humanas

- Ejecuté las pruebas del proyecto (15 en verde) y los scripts de LAB11, LAB12, LAB13 y E07, y consulté sus salidas: `risk_register_scored.csv`, las auditorías de los modelos logistic y tree, `deployment_decision.json` y `mitigation_comparison.csv`.
- Consulté en el código cómo se calculan la prioridad de los riesgos, las métricas por grupo, la validación del RACI y las puertas de decisión (`impact.py`, `fairness.py`, `governance.py`, `pipeline.py`, `data.py`, `model.py`).
- Consulté los archivos del caso en los que se basaron los borradores: `README.md`, `docs/DATASET_CARD.md` y `configs/governance.yml`.
- Comprobé con una búsqueda que no quedaban marcadores `REPLACE` en los archivos completados.
- Ejecuté la aplicación Streamlit y revisé las métricas globales y por grupo y las puertas de calidad.

## Errores detectados y correcciones

- `scripts/lab11_impact.py` y `scripts/simulate_incident.py` del proyecto base tenían un error de sintaxis (una cadena de texto partida en varias líneas). La IA no lo advirtió al leer el primero y se detectó al ejecutarlo; ambos se corrigieron.
- `rmf_summary.json` se genera con texto fijo: no mide controles reales, así que no se usó como evidencia.
- `lab11_impact.py` sobrescribe `DECISION_RECORD.md` en cada ejecución, y `simulate_incident.py` hace lo mismo con el postmortem; los documentos finales se copiaron después de la última ejecución.
- Los resultados de LAB12 se guardan en `reports/lab12/<modelo>/`, algo que el manual no indica.
- `validate_raci` solo comprueba que R y A no estén vacíos; no exige un único Accountable por actividad. Se añadió una prueba que lo verifica.
- La decisión automática del script de LAB13 es GO, pero las puertas no evalúan el recall por grupo (G1 queda en 0,653, por debajo del mínimo de 0,68). Por eso la decisión final es LIMITAR (equivale a REVIEW) y la aplicación lo indica.
- La primera versión de la declaración de LAB11 (commit `38b3c0b`) se guardó con apartados sin completar y se corrigió en un commit posterior.
- La señal del simulacro ("recall gap exceeded") está escrita fija en el script y no procede de una medición real.
- Las citas de artículos de la Ley 172-13 provienen de una copia en línea cuyo texto estaba incompleto; no las he contrastado todavía con la Gaceta Oficial.
- Los tiempos de entrenamiento de las variantes del experimento (de 0,015 s a 0,119 s) varían entre ejecuciones y no se usaron para comparar variantes.

**Responsabilidad:** asumo la responsabilidad sobre el contenido entregado.
