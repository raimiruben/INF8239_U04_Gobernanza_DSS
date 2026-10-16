# LAB12 · Interpretación de la auditoría de equidad

Sistema: Territorial Review DSS (sintético). Datos de prueba: 160 casos posteriores al 2026-09-24 (corte temporal). Los resultados están en `reports/lab12/logistic/` y `reports/lab12/tree/`.

## 1. Comparación de los dos modelos

| Medida | logistic | tree | Puerta (`configs/governance.yml`) |
|---|---|---|---|
| Exactitud global | 0,719 | 0,706 | |
| Recall global | 0,717 | 0,717 | mínimo 0,68 |
| FPR global | 0,279 | 0,309 | |
| Recall G1 / G2 | 0,653 / 0,791 | 0,633 / 0,814 | |
| FPR G1 / G2 | 0,250 / 0,375 | 0,269 / 0,438 | |
| Brecha de recall | 0,138 (cumple) | 0,181 (no cumple) | máximo 0,16 |
| Brecha de FPR | 0,125 (cumple) | 0,168 (no cumple) | máximo 0,16 |
| Tiempo de entrenamiento | 0,24 s | 0,43 s | |
| Tamaño del modelo | 3,6 KB | 7,9 KB | máximo 1 024 KB |

**Lectura.** La utilidad es prácticamente la misma (mismo recall global; el árbol tiene menos exactitud y más falsos positivos). Con las puertas del proyecto, logistic cumple ambas brechas y tree falla las dos, y además el árbol cuesta más tiempo y tamaño sin mejorar nada. Por eso se prefiere logistic como opción suficiente. Pero la diferencia entre los dos modelos equivale a cuatro casos individuales (en G1, 32 frente a 31 positivos detectados y 13 frente a 14 falsos positivos; en G2, 34 frente a 35 y 6 frente a 7), de modo que el veredicto de las puertas es frágil y no se apoya solo en la equidad: también cuentan la utilidad y el costo.

**Frente a una alternativa no predictiva.** Si se revisara al azar el mismo 53 % de los casos que selecciona el modelo, se esperaría un recall de alrededor de 0,53 y una tasa de falsos positivos de alrededor de 0,53. El modelo logra 0,72 y 0,28. Es una expectativa teórica (supone que el orden de llegada no se relaciona con el riesgo), no una medición.

## 2. Advertencias de soporte insuficiente

El proyecto no define un mínimo de observaciones para interpretar un grupo. Aquí se adopta como criterio exigir al menos **30 casos de la clase relevante**: positivos para interpretar el recall y negativos para interpretar la tasa de falsos positivos. Los positivos y negativos por celda se reconstruyeron a partir de las tasas de `fairness_intersectional.csv` (los valores salen enteros y suman los 49 y 43 positivos de cada grupo).

| Grupo | Casos | Positivos | Negativos | Recall (logistic) | FPR (logistic) | Soporte |
|---|---|---|---|---|---|---|
| G1 (total) | 101 | 49 | 52 | 0,653 | 0,250 | suficiente |
| G2 (total) | 59 | 43 | 16 | 0,791 | 0,375 | insuficiente para FPR (16 negativos) |
| G1 · 18-29 | 18 | 4 | 14 | 0,75 | 0,14 | insuficiente |
| G1 · 30-44 | 24 | 16 | 8 | 0,56 | 0,13 | insuficiente |
| G1 · 45-59 | 35 | 17 | 18 | 0,59 | 0,39 | insuficiente |
| G1 · 60+ | 24 | 12 | 12 | 0,83 | 0,25 | insuficiente |
| G2 · 18-29 | 11 | 8 | 3 | 0,88 | 0,00 | insuficiente |
| G2 · 30-44 | 14 | 12 | 2 | 0,67 | 0,50 | insuficiente |
| G2 · 45-59 | 8 | 6 | 2 | 1,00 | 0,00 | insuficiente |
| G2 · 60+ | 26 | 17 | 9 | 0,76 | 0,56 | insuficiente |

**Consecuencias.** Ninguna celda interseccional alcanza 30 positivos ni 30 negativos, así que el análisis por `protected_group` y `age_band` es solo exploratorio y no se usa para decidir. Algunas tasas ni siquiera son estimaciones: un FPR de 0,00 en G2 · 45-59 son 0 falsos positivos sobre 2 negativos. A nivel de grupo, el recall tiene soporte (49 y 43 positivos), pero la tasa de falsos positivos de G2 descansa en solo 16 negativos, por lo que su brecha es frágil. Los grupos no se ocultan: se informan con su advertencia.

**Pista para investigar.** El déficit de recall de G1 parece concentrarse entre los 30 y los 59 años (19 de 33 positivos detectados, 0,58, frente a 0,72 global). Con 33 positivos el margen de error es de unos 0,17, así que no se puede afirmar que sea distinto del promedio.

## 3. Por qué una brecha observada no prueba discriminación causal

- **Es una diferencia observada en una muestra pequeña.** La brecha de recall (0,138) tiene un margen de error de aproximadamente ±0,18, de modo que no se distingue de cero ni del umbral de 0,16.
- **Puede deberse a la composición de los grupos**, por ejemplo a diferencias en la distribución por edad, zona o historial de incidentes entre G1 y G2, y no a un trato distinto por parte del sistema.
- **Las variables que sí entran al modelo pueden transmitir información del grupo** (zone como variable proxy y age_band, declarada sensible en la política), aunque `protected_group` se haya excluido.
- **Los datos son sintéticos**, y la etiqueta `target` no representa un resultado real.
- Para hablar de causa haría falta un diseño que controle los factores de confusión y más datos. Lo que sí implica una brecha es una **señal para investigar** (revisar los datos, el umbral y las consecuencias) antes de desplegar, no una conclusión.

## 4. Acción humana

**Recomendación: REVIEW.** El modelo logistic puede usarse únicamente para priorizar la cola de revisión humana; no decide ni interviene. Antes de cualquier uso real, el propietario institucional debe:

1. Investigar la brecha de recall de G1 (en particular entre 30 y 59 años) con más datos o intervalos de confianza.
2. Decidir y justificar por escrito si `age_band` debe seguir siendo predictor.
3. Confirmar en LAB13 las puertas de desempeño, equidad, latencia y costo.
