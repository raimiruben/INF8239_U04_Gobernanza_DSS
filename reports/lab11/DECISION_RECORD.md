# Decision record

# Registro de decisión — Territorial Review DSS (sintético)

**Decisión: REVIEW (revisar).** Se continúa únicamente hasta la auditoría de LAB12. El sistema no se usa para ninguna decisión mientras no cumpla las compuertas de `configs/governance.yml`.

**Responsable:** Dirección del programa de revisión territorial (propietario institucional).

## Evidencia disponible
- Propósito, interesados y ocho riesgos puntuados, con prioridad = probabilidad × impacto (`reports/lab11/`).
- Datos sintéticos válidos (640 filas, 9 columnas) y pruebas en verde.
- Política de usos prohibidos y umbrales de retiro en `configs/governance.yml`.

## Incertidumbre (lo que todavía no sabemos)
- No hay mediciones del modelo: ni recall, ni brechas por grupo, ni latencia. Los riesgos R01, R03 y R05 dependen de ellas (LAB12).
- Varios controles están "por implementar" (registro de coincidencia o discrepancia del revisor, revisión humana previa a toda intervención).
- Los datos son sintéticos: nada de lo medido describe poblaciones reales.

## Tres riesgos prioritarios
1. **R02, sesgo de automatización (prioridad 9, residual medio).** Es el más probable y puede convertir una ayuda en un decisor de hecho. Su control (registro de discrepancias y auditoría de una muestra) aún no existe, así que hoy no hay evidencia de que funcione.
2. **R01, subpriorización de un grupo protegido o una banda de edad (prioridad 8, residual alto).** Es el daño más grave: atención tardía a personas de esos grupos. El control clave es la auditoría por subgrupos de LAB12 (brecha máxima de 0,16). El residual sigue alto porque las brechas se estiman con datos sintéticos y muestras pequeñas por grupo.
3. **R07, uso fuera de alcance (prioridad 8, residual alto).** No es un riesgo técnico sino de uso: la prioridad podría emplearse para decidir elegibilidad, intervención o emergencia. Ningún control técnico lo elimina del todo; depende de la política, de las advertencias y de la revisión humana.

## Condición de retiro
Se detiene el uso si el recall baja de 0,68, si la brecha de recall o de falsos positivos entre grupos supera 0,16, o si se detecta un uso fuera de alcance. Decide el propietario institucional y queda registrado en este documento.

## Mecanismo de apelación
Toda persona afectada o revisora puede pedir una revisión humana independiente; un revisor distinto responde por escrito en 10 días hábiles. El sistema no puede cerrar ni descartar un caso.

## Próximos pasos
1. LAB12: auditar el modelo por subgrupos y medir recall, brechas, latencia y tamaño.
2. Actualizar la evidencia del registro de riesgos con las rutas reales.
3. Volver a decidir: GO solo si se cumplen las compuertas y existe el control de R02; STOP si alguna se incumple de forma persistente.



