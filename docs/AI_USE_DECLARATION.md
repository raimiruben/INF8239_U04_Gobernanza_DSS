\# Declaración de uso de IA



\*\*Herramienta:\*\* Claude (Anthropic), asistente de IA usado en el chat de claude.ai durante el LAB11.



\*\*Finalidad:\*\* explicación de los conceptos del manual y de las reglas que aplican los scripts del proyecto; borradores de contenido para `student\\\_inputs/lab11\\\_impact.yml`, `student\\\_inputs/stakeholders.csv`, `student\\\_inputs/risk\\\_register.csv` y `reports/lab11/DECISION\\\_RECORD.md`; diagnóstico de un error del script `scripts/lab11\\\_impact.py`.



\*\*Fragmentos afectados:\*\*

\- `student\\\_inputs/lab11\\\_impact.yml`: los nueve campos partieron de un borrador de la IA. \[Escriba qué campos cambió o reescribió.]

\- `student\\\_inputs/stakeholders.csv`: beneficio, daño y participación de los cuatro actores partieron de un borrador. \[Escriba qué cambió.]

\- `student\\\_inputs/risk\\\_register.csv`: los escenarios, afectados, controles, responsables y evidencias de R01 a R08 partieron de una propuesta de la IA, ajustada a la probabilidad, el impacto y el residual ya fijados en la plantilla. \[Escriba qué riesgos modificó o sustituyó.]

\- `reports/lab11/DECISION\\\_RECORD.md`: la estructura y el texto base los propuso la IA, incluida la decisión REVIEW. \[Escriba si mantuvo o cambió la decisión y por qué.]

\- `scripts/lab11\\\_impact.py`: la corrección de la cadena de texto (una línea con `\\\\n`) fue indicada por la IA.



\*\*Verificaciones humanas:\*\*

\- Ejecuté las pruebas (10 en verde al inicio y 3 en verde de impacto y privacidad al final) y el script, y leí el resultado en `risk\\\_register\\\_scored.csv`.

\- Comprobé en el código que la prioridad es probabilidad por impacto y que los tres riesgos prioritarios son R02, R01 y R07.

\- Comprobé que no quedan marcadores `REPLACE` en los archivos entregados.

\- \[Escriba qué más verificó usted: por ejemplo, si contrastó los escenarios con los datos y la política del caso.]



\*\*Errores detectados y correcciones:\*\*

\- El script `scripts/lab11\\\_impact.py` del proyecto base tenía un error de sintaxis (una cadena de texto partida en varias líneas). Se detectó al ejecutarlo; se corrigió y quedó en un commit propio.

\- `rmf\\\_summary.json` se genera con texto fijo: no mide controles reales, así que no se usó como evidencia de que los controles funcionan.

\- El script sobrescribe `DECISION\\\_RECORD.md` en cada ejecución, por lo que el registro se escribió después de la última ejecución.

\- Varias evidencias del registro de riesgos figuran como "pendiente" o "por implementar" porque dependen de LAB12 y LAB13, y no se presentaron como existentes.

