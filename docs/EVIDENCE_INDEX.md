# Índice de evidencias por criterio de la rúbrica

Repositorio: https://github.com/raimiruben/INF8239_U04_Gobernanza_DSS (etiqueta `u04-lab13`). Para reproducir: `uv sync --frozen`, `uv run pytest -q`.

## Ejercicio 07 · Evaluación de impacto y auditoría de equidad
| Criterio | Evidencia |
|---|---|
| Finalidad, interesados y proporcionalidad | `student_inputs/lab11_impact.yml`, `student_inputs/stakeholders.csv`, `docs/LEGAL_FRAMEWORK.md` |
| Registro de riesgos y NIST AI RMF | `student_inputs/risk_register.csv`, `reports/lab11/risk_register_scored.csv`, `docs/NIST_AI_RMF_MAPPING.md` |
| Auditoría global, por grupo e interseccional | `reports/lab12/logistic/`, `reports/lab12/tree/`, `reports/lab12/INTERPRETATION.md` |
| Mitigación, trade-offs y decisión | `reports/e07/mitigation_comparison.csv`, `scripts/e07_mitigation.py`, `reports/lab11/DECISION_RECORD.md`, `student_inputs/lab12_decision.yml` |
| Pruebas, referencias y declaración de IA | `tests/`, `docs/LEGAL_FRAMEWORK.md` (fuentes), `docs/AI_USE_DECLARATION.md` |

## Ejercicio 08 · Expediente de gobernanza y simulacro
| Criterio | Evidencia |
|---|---|
| Inventario, minimización y retención | `docs/data_inventory.csv`, `docs/DATASET_CARD.md` |
| Datasheet y Model Card trazables | `docs/DATASET_CARD.md`, `docs/MODEL_CARD.md`, `reports/lab13/deployment_decision.json` |
| RACI y traspaso entre roles | `student_inputs/raci.csv`, `tests/test_artifacts.py` |
| Monitoreo, runbook y simulacro | `docs/RUNBOOK.md`, `reports/lab13/INCIDENT_POSTMORTEM.md`, `scripts/simulate_incident.py` |
| Pruebas, Git y calidad documental | `tests/` (15 pruebas), historial de commits y etiqueta `u04-lab13`, `docs/AI_USE_DECLARATION.md` |
