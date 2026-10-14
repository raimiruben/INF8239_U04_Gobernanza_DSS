# Declaración de uso de IA

**Herramienta:** Claude (Anthropic), asistente de IA usado en el chat de claude.ai durante el LAB11.

**Finalidad:** guía paso a paso del laboratorio; explicación de los conceptos del manual y de las reglas que aplican los scripts del proyecto; redacción de los borradores de contenido de `student_inputs/lab11_impact.yml`, `student_inputs/stakeholders.csv`, `student_inputs/risk_register.csv` y `reports/lab11/DECISION_RECORD.md`; diagnóstico de un error del script `scripts/lab11_impact.py`.

**Fragmentos afectados** (los borradores de la IA se adoptaron sin cambios):
- `student_inputs/lab11_impact.yml`: los nueve campos son el borrador propuesto por la IA; no los modifiqué.
- `student_inputs/stakeholders.csv`: beneficio, daño y participación de los cuatro actores son el borrador propuesto por la IA; no los modifiqué.
- `student_inputs/risk_register.csv`: los escenarios, afectados, controles, responsables y evidencias de R01 a R08 son la propuesta de la IA, ajustada a la probabilidad, el impacto y el residual ya fijados en la plantilla; no modifiqué ningún riesgo.
- `reports/lab11/DECISION_RECORD.md`: la estructura y el texto los propuso la IA, incluida la decisión REVIEW, que mantuve sin cambios.
- `scripts/lab11_impact.py`: la corrección de la cadena de texto (una línea con `\n`) fue indicada por la IA y la apliqué manualmente en el editor.

**Verificaciones humanas:**
- Ejecuté las pruebas del proyecto (10 en verde al inicio, y 3 de impacto y privacidad al final) y el script de LAB11, y consulté su salida: `risk_register_scored.csv` y los tres riesgos prioritarios.
- Consulté en el código (`impact.py`, `test_impact.py` y `lab11_impact.py`) cómo se calcula la prioridad (probabilidad por impacto) y qué valida el script.
- Consulté los archivos del caso en los que se basaron los borradores: `README.md`, `docs/DATASET_CARD.md` y `configs/governance.yml`.
- Comprobé con una búsqueda que no quedaban marcadores `REPLACE` en los archivos de LAB11.

**Errores detectados y correcciones:**
- El script `scripts/lab11_impact.py` del proyecto base tenía un error de sintaxis (una cadena de texto partida en varias líneas). La IA no lo advirtió al leer el script por primera vez y se detectó al ejecutarlo; se corrigió y quedó en un commit propio.
- `rmf_summary.json` se genera con texto fijo: no mide controles reales, así que no se usó como evidencia de que los controles funcionan.
- El script sobrescribe `DECISION_RECORD.md` en cada ejecución, por lo que el registro se escribió después de la última ejecución.
- Varias evidencias del registro de riesgos figuran como "pendiente" o "por implementar" porque dependen de LAB12 y LAB13, y no se presentaron como existentes.
- La primera versión de esta declaración (commit `38b3c0b`) se guardó con apartados sin completar y con caracteres de escape en los nombres de archivo. Se detectó con una búsqueda posterior y se corrigió en un commit nuevo.

**Responsabilidad:** asumo la responsabilidad sobre el contenido entregado.
