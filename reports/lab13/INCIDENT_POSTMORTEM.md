# Incident simulation

- detected_at: 2026-10-17T00:04:16.777777+00:00
- signal: recall gap exceeded
- containment: REVIEW and safe baseline
- evidence: preserved report and model version
- communication: El Data team informó al Institutional owner y al Operator; Legal revisó el mensaje; se notificó a los representantes de las personas afectadas con qué ocurrió, qué casos pudieron verse afectados y cómo solicitar revisión humana o apelar. No se publicaron datos personales. (Simulado.)
- corrective actions, owners and dates: (1) Investigar la brecha de recall de G1, en particular entre 30 y 59 años, con más datos o intervalos de confianza. Responsable: Data team. Fecha PROPUESTA: 2026-10-30. (2) Decidir y justificar por escrito si `age_band` sigue como predictor. Responsable: Institutional owner. Fecha PROPUESTA: 2026-11-06. (3) Añadir una puerta de recall mínimo por grupo y un mínimo de soporte a la auditoría. Responsable: Data team. Fecha PROPUESTA: 2026-11-13. (4) Repetir la auditoría y la simulación antes de reactivar el sistema. Responsable: Data team; aprobación: Institutional owner. Fecha PROPUESTA: 2026-11-16.

Nota: ejercicio simulado. La señal "recall gap exceeded" está escrita fija en `scripts/simulate_incident.py` y no proviene de una medición real. Las fechas y responsables son propuestos por la IA y deben ser confirmados por el estudiante.
