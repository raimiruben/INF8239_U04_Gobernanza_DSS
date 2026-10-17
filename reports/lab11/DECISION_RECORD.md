# Registro de decisión — Territorial Review DSS (sintético)

**Decisión: LIMITAR (estado de la puerta: REVIEW).** El sistema se usa solo como apoyo a la priorización de la cola de revisión humana, en el contexto educativo con datos sintéticos. No se despliega para uso real ni se usa para ninguna decisión sobre personas. Correspondencia con las etiquetas del curso: GO equivale a desplegar, REVIEW a limitar o modificar, y STOP a no utilizar.

**Responsable:** Dirección del programa de revisión territorial (propietario institucional). **Fecha del registro:** 2026-10-16. **Próxima revisión:** PROPUESTA 2026-11-16, o antes si ocurre un incidente o cambian los datos o el modelo.

## Evidencia
- Propósito, interesados y ocho riesgos puntuados, con prioridad = probabilidad × impacto (`reports/lab11/`).
- Auditoría de LAB12 sobre 160 casos con corte temporal (`reports/lab12/`): el modelo logistic tiene recall global 0,717, brecha de recall 0,138 y brecha de FPR 0,125; el modelo tree supera ambas brechas (0,181 y 0,168).
- Puertas de LAB13 (`reports/lab13/deployment_decision.json`): las cinco puertas automáticas pasan (el script devuelve GO mecánico), con latencia de 0,033 ms por predicción y un modelo de 3,56 KB.
- Experimento de mitigación (`reports/e07/mitigation_comparison.csv`): retirar `age_band` mantiene el recall (0,717) y las tres puertas; retirar `zone` hace fallar la puerta de FPR (brecha 0,327); retirar ambas hace fallar las brechas de recall (0,161) y de FPR (0,245).
- 15 pruebas automáticas en verde y simulacro de incidente con postmortem (`reports/lab13/INCIDENT_POSTMORTEM.md`).

## Por qué limitar y no desplegar
1. El recall de G1 (0,653) está por debajo del mínimo de 0,68 y no mejora en ninguna de las variantes probadas. Las puertas automáticas no evalúan el recall por grupo.
2. Los intervalos son muy anchos: la brecha de recall va de 0,01 a 0,31 con 160 casos, y no se distingue de cero ni del umbral.
3. El control del riesgo R02 (registro de coincidencia o discrepancia del revisor) no está implementado, y esa era la condición para pasar a GO.
4. Los datos son sintéticos: nada de lo medido describe poblaciones reales.

## Por qué no "no utilizar"
La utilidad es real frente a una revisión sin orden (recall de 0,72 frente a unos 0,53 esperados al azar con el mismo volumen), el costo es mínimo y el sistema solo propone un orden que la persona revisora puede ignorar.

## Trade-offs
- Retirar `age_band` quita una variable sensible sin perder recall, pero no cierra la brecha de G1. No se implementa en el pipeline principal para que LAB12 y LAB13 sigan coincidiendo con sus informes; queda como mejora a decidir por el propietario.
- Mantener `zone` sostiene la puerta de FPR, aunque puede actuar como variable proxy del grupo.
- Entre logistic y tree, se prefiere logistic: cumple ambas brechas, es más pequeño y más rápido, aunque la diferencia equivale a unos cuatro casos.

## Incertidumbre (lo que todavía no sabemos)
- Si el déficit de recall de G1 es real o ruido de una muestra pequeña, y si se concentra entre los 30 y 59 años.
- Cómo se comporta el modelo con datos reales y con el tiempo (R03): el monitoreo periódico no está automatizado.

## Tres riesgos prioritarios
1. **R02, sesgo de automatización** (prioridad 9, residual medio). Es el más probable. Su control sigue por implementar.
2. **R01, subpriorización de un grupo protegido o de una banda de edad** (prioridad 8, residual alto). Medido en LAB12 y E07; sigue sin cerrarse la brecha de G1.
3. **R07, uso fuera de alcance** (prioridad 8, residual alto). Depende de la política, de la advertencia visible en la aplicación y de la revisión humana.

## Condición de retiro
Se detiene el uso si en la revisión periódica el recall baja de 0,68, si la brecha de recall o de falsos positivos entre grupos supera 0,16, o si se detecta un uso fuera de alcance. Decide el propietario institucional y queda registrado en este documento.

## Mecanismo de apelación
Toda persona afectada o revisora puede pedir una revisión humana independiente de la prioridad asignada. Un revisor distinto del original responde por escrito en 10 días hábiles. El sistema no puede cerrar ni descartar un caso.

## Próximos pasos
1. Implementar el registro de coincidencia o discrepancia del revisor (R02).
2. Obtener más datos o intervalos de confianza para la brecha de G1.
3. Decidir y justificar por escrito si `age_band` deja de ser variable del modelo.
4. Automatizar el monitoreo periódico y repetir la auditoría antes de cualquier uso real.
