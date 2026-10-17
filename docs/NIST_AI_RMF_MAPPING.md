# NIST AI RMF · Correspondencia con las evidencias del repositorio

Sistema: Territorial Review DSS (sintético). Elaborado el 2026-10-16. El marco es voluntario (NIST AI 100-1, enero de 2023). Esta matriz enlaza cada función con evidencias reales y dice qué queda incompleto. `reports/lab11/rmf_summary.json` se genera con texto fijo en el script, así que no se usa como evidencia.

## GOVERN · políticas, roles y rendición de cuentas
| Qué se hizo | Evidencia | Estado |
|---|---|---|
| Finalidad, usos prohibidos y umbrales de retiro | `configs/governance.yml`, `student_inputs/lab11_impact.yml` | Hecho |
| Responsable único por actividad (RACI) | `student_inputs/raci.csv`, `tests/test_artifacts.py` | Hecho y verificado por prueba |
| Runbook de incidentes con autoridad de contención | `docs/RUNBOOK.md` | Hecho |
| Revisión periódica del registro de decisión | `reports/lab11/DECISION_RECORD.md` (fecha de revisión propuesta) | Parcial: no hay un proceso automático |

## MAP · contexto, interesados y riesgos
| Qué se hizo | Evidencia | Estado |
|---|---|---|
| Interesados, beneficios, daños y poder | `student_inputs/stakeholders.csv` | Hecho |
| Ocho riesgos con probabilidad, impacto, control, responsable y residual | `student_inputs/risk_register.csv`, `reports/lab11/risk_register_scored.csv` | Hecho |
| Origen, composición y límites de los datos | `docs/DATASET_CARD.md`, `docs/data_inventory.csv` | Hecho |

## MEASURE · medición del desempeño, la equidad y el costo
| Qué se hizo | Evidencia | Estado |
|---|---|---|
| Desempeño global y por grupo con corte temporal | `reports/lab12/logistic/`, `reports/lab12/tree/` | Hecho |
| Análisis interseccional con advertencia de soporte | `reports/lab12/INTERPRETATION.md` | Hecho (exploratorio) |
| Incertidumbre de la brecha de recall (bootstrap) y variantes de mitigación | `reports/e07/mitigation_comparison.csv`, `scripts/e07_mitigation.py` | Hecho |
| Latencia y tamaño del modelo | `reports/lab13/deployment_decision.json` | Hecho |
| Pruebas automáticas | `tests/` (15 pruebas) | Hecho |

Límites de la medición: 160 casos de prueba, datos sintéticos, intervalo de la brecha de recall de aproximadamente 0,01 a 0,31.

## MANAGE · respuesta, retiro y mejora
| Qué se hizo | Evidencia | Estado |
|---|---|---|
| Condición de retiro y mecanismo de apelación | `reports/lab11/DECISION_RECORD.md` | Hecho |
| Decisión final con trade-offs (LIMITAR) | `reports/lab11/DECISION_RECORD.md`, `reports/e07/mitigation_comparison.csv` | Hecho |
| Simulacro de incidente con postmortem | `reports/lab13/INCIDENT_POSTMORTEM.md`, `docs/RUNBOOK.md` | Hecho (simulado) |
| Control R02: registro de coincidencia o discrepancia del revisor | `student_inputs/risk_register.csv` (R02) | **Pendiente**: no está implementado |
| Monitoreo periódico y reentrenamiento | `docs/RUNBOOK.md` (descrito) | **Pendiente**: no está automatizado |

## Lectura
Las funciones GOVERN, MAP y MEASURE tienen evidencia ejecutable. MANAGE está documentado pero dos controles (R02 y el monitoreo periódico) no están implementados; por eso la decisión es LIMITAR y no desplegar.
