"""E07 · Actualiza la columna evidence del registro de riesgos con las rutas reales de LAB12-LAB13 y E07.

Solo cambia evidence de R01, R03, R04, R05 y R07. No toca escenarios, controles, responsables,
probabilidad, impacto ni residual. Es idempotente.
"""
import pandas as pd

PATH = "student_inputs/risk_register.csv"

UPDATES = {
    "R01": (
        "Auditoría de LAB12 (reports/lab12/logistic/fairness_by_group.csv y reports/lab12/INTERPRETATION.md): "
        "brecha de recall 0,138 (IC 95 % de 0,01 a 0,31) y recall de G1 0,653, por debajo de 0,68; "
        "mitigación explorada en reports/e07/mitigation_comparison.csv. La brecha de G1 sigue abierta"
    ),
    "R03": (
        "Evaluación temporal con corte 2026-09-24 (reports/lab12/logistic/global_metrics.json y "
        "reports/lab13/deployment_decision.json). El monitoreo periódico y el reentrenamiento siguen por implementar"
    ),
    "R04": (
        "tests/test_privacy.py (rechazo de la columna name), validación de esquema en src/inf8239_u04/data.py "
        "e inventario docs/data_inventory.csv verificado por tests/test_artifacts.py; "
        "registro de autorización de uso de datos reales (por definir)"
    ),
    "R05": (
        "reports/lab13/deployment_decision.json: latencia 0,033 ms por predicción (máximo 500 ms) "
        "y modelo de 3,56 KB (máximo 1024 KB)"
    ),
    "R07": (
        "configs/governance.yml (usos prohibidos), docs/MODEL_CARD.md (usos fuera de alcance) y aviso visible en app.py; "
        "registro de revisiones humanas previas a intervenciones (por implementar)"
    ),
}

df = pd.read_csv(PATH)
for rid, text in UPDATES.items():
    assert (df["id"] == rid).sum() == 1, rid
    df.loc[df["id"] == rid, "evidence"] = text
df.to_csv(PATH, index=False, encoding="utf-8", lineterminator="\n")
print(df[["id", "evidence"]].to_string())
