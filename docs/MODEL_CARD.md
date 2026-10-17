# Model Card — Territorial Review DSS (sintético)

Versión evaluada: modelo `logistic` (regresión logística, `class\_weight="balanced"`, `random\_state=42`). Evidencia en `reports/lab12/` y `reports/lab13/`.

## Intended use

Priorizar, para revisión humana, la cola de casos territoriales sintéticos (propósito de `configs/governance.yml`: "Prioritize synthetic cases for human review"). El modelo ordena casos; una persona revisora (Operator) examina la evidencia y toma la decisión. Es una demostración educativa con datos sintéticos.

## Out-of-scope use

Usos prohibidos por la política (`configs/governance.yml`): intervención automática, decisión de elegibilidad y declaración de emergencia. Tampoco debe usarse con datos reales ni personales, ni para estimar estadísticas reales. Los identificadores directos (name, document\_number, email, phone) no forman parte del modelo.

## Data and split

* Datos sintéticos descritos en `docs/DATASET\_CARD.md`: 640 casos.
* Corte temporal: el primer 75 % (480 casos, hasta el 2026-09-24) para entrenar y el 25 % posterior (160 casos) para evaluar.
* Variables del modelo: zone, age\_band, previous\_incidents, infrastructure\_score, exposure. Se excluyen case\_id, received\_date, target y protected\_group.
* `protected\_group` (G1/G2) se usa solo para auditar. `age\_band` entra al modelo aunque la política la declara sensible; esto queda como decisión pendiente del propietario.

## Global and subgroup evaluation

|Medida|Resultado|Puerta|
|-|-|-|
|Exactitud global|0,719|—|
|Recall global|0,717|mínimo 0,68|
|FPR global|0,279|—|
|Recall G1 / G2|0,653 / 0,791|—|
|FPR G1 / G2|0,250 / 0,375|—|
|Brecha de recall|0,138|máximo 0,16|
|Brecha de FPR|0,125|máximo 0,16|

Las puertas automáticas de `scripts/lab13\_governance.py` pasan (GO mecánico). El modelo alternativo `tree` supera ambas brechas (0,181 y 0,168), con el mismo recall global.

Lectura: el recall de G1 (0,653) está por debajo del mínimo de 0,68 y la política del proyecto no lo evalúa por grupo. Los grupos tienen poco soporte (101 casos en G1 y 59 en G2, con solo 16 negativos en G2) y ninguna celda de la intersección protected\_group × age\_band llega a 30 positivos ni a 30 negativos, por lo que las brechas son inestables y el análisis interseccional es solo exploratorio. Una brecha observada es una señal para investigar, no prueba de discriminación causal.

## Green AI evidence

* Modelo pequeño y simple, suficiente para la tarea: 3,56 KB frente a un máximo de 1 024 KB.
* Latencia: 0,033 ms por predicción (máximo 500 ms).
* Entrenamiento: menos de 0,3 s en CPU (0,09 s en LAB13 y 0,24 s en LAB12; varía entre ejecuciones).
* Frente al árbol (7,9 KB, 0,43 s) el modelo logístico es más pequeño, más rápido y cumple las dos brechas, sin perder utilidad.

## Limitations, human oversight and appeal

* Datos sintéticos; la etiqueta no representa un resultado real.
* Muestra de prueba pequeña: la diferencia entre `logistic` y `tree` equivale a unos cuatro casos individuales, por lo que el veredicto de las puertas es frágil.
* `age\_band` (sensible) entra al modelo y `zone` podría actuar como variable proxy.
* Recall de G1 (0,653) por debajo de 0,68; déficit posiblemente concentrado entre los 30 y 59 años, sin evidencia suficiente para afirmarlo.
* Supervisión humana: el modelo solo prioriza. Cada recomendación la revisa una persona (Operator), que puede ignorarla. No hay decisiones automáticas.
* Apelación: toda persona afectada puede solicitar revisión humana; el Operator la atiende y el Institutional owner responde por el resultado (RACI en `student\_inputs/raci.csv`).
* Decisión documentada: **REVIEW**. No pasar a uso real hasta investigar la brecha de G1, obtener más datos o intervalos de confianza y decidir por escrito si `age\_band` debe seguir como predictor.

## Owner and review date

* Responsable (Accountable): Institutional owner.
* Responsable de ejecución (Responsible): Data team.
* Próxima revisión: PROPUESTA 2026-11-16, o antes si ocurre un incidente o cambian los datos o el modelo. (Confirmar o ajustar esta fecha.)



\## Mitigation explored (E07)

Se probaron cuatro variantes del modelo logistic (`reports/e07/mitigation\_comparison.csv`). Retirar `age\_band` mantiene el recall (0,717) y las tres puertas; retirar `zone` hace fallar la puerta de FPR; retirar ambas hace fallar las brechas de recall y de FPR. El recall de G1 (0,653) no mejora en ninguna variante. Decisión final del propietario: LIMITAR (equivale a REVIEW), ver `reports/lab11/DECISION\_RECORD.md`



