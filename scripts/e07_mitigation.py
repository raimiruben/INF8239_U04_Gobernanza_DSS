"""E07 · Experimento de mitigación: quitar variables sensibles o proxy del modelo logistic.

Compara cuatro variantes con el mismo corte temporal, la misma semilla y los mismos umbrales de
configs/governance.yml. Añade un intervalo bootstrap de la brecha de recall y un criterio propuesto
(recall mínimo por grupo). No guarda modelos. Salida: reports/e07/mitigation_comparison.csv
"""
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from inf8239_u04.data import load_data, temporal_split
from inf8239_u04.fairness import audit, gap
from inf8239_u04.governance import load_config

NUM = ["previous_incidents", "infrastructure_score", "exposure"]
VARIANTS = {
    "baseline (zone + age_band)": ["zone", "age_band"],
    "sin age_band": ["zone"],
    "sin zone": ["age_band"],
    "sin zone ni age_band": [],
}
BOOTSTRAPS = 1000


def build(cat):
    parts = [("num", StandardScaler(), NUM)]
    if cat:
        parts.insert(0, ("cat", OneHotEncoder(handle_unknown="ignore"), cat))
    est = LogisticRegression(max_iter=1200, class_weight="balanced", random_state=42)
    return make_pipeline(ColumnTransformer(parts), est)


def group_rates(y, p, g):
    rec, fpr = {}, {}
    for grp in np.unique(g):
        pos = (g == grp) & (y == 1)
        neg = (g == grp) & (y == 0)
        rec[grp] = p[pos].mean() if pos.any() else np.nan
        fpr[grp] = p[neg].mean() if neg.any() else np.nan
    return rec, fpr


def spread(d):
    v = np.array(list(d.values()), dtype=float)
    return float(np.nanmax(v) - np.nanmin(v))


def bootstrap_gap(y, p, g, rng):
    vals = []
    for _ in range(BOOTSTRAPS):
        idx = rng.integers(0, len(y), len(y))
        rec, _ = group_rates(y[idx], p[idx], g[idx])
        vals.append(spread(rec))
    return float(np.nanpercentile(vals, 2.5)), float(np.nanpercentile(vals, 97.5))


def main():
    gates = load_config()["gates"]
    train, test = temporal_split(load_data())
    y = test.target.to_numpy()
    g = test.protected_group.to_numpy()
    rows = []
    for name, cat in VARIANTS.items():
        cols = cat + NUM
        model = build(cat)
        start = time.perf_counter()
        model.fit(train[cols], train.target)
        seconds = time.perf_counter() - start
        pred = model.predict(test[cols])
        overall, by_group, _ = audit(test.target, pred, test.protected_group)
        rec_gap = gap(by_group, "recall")
        fpr_gap = gap(by_group, "fpr")
        lo, hi = bootstrap_gap(y, np.asarray(pred), g, np.random.default_rng(42))
        min_group_recall = float(by_group["recall"].min())
        row = {
            "variant": name,
            "features": ", ".join(cols),
            "accuracy": round(float(overall["accuracy"]), 3),
            "recall": round(float(overall["recall"]), 3),
            "recall_G1": round(float(by_group.loc["G1", "recall"]), 3),
            "recall_G2": round(float(by_group.loc["G2", "recall"]), 3),
            "fpr_G1": round(float(by_group.loc["G1", "fpr"]), 3),
            "fpr_G2": round(float(by_group.loc["G2", "fpr"]), 3),
            "recall_gap": round(rec_gap, 3),
            "recall_gap_ci95": f"{lo:.2f}-{hi:.2f}",
            "fpr_gap": round(fpr_gap, 3),
            "train_seconds": round(seconds, 3),
            "gate_recall": bool(overall["recall"] >= gates["min_recall"]),
            "gate_recall_gap": bool(rec_gap <= gates["max_recall_gap"]),
            "gate_fpr_gap": bool(fpr_gap <= gates["max_fpr_gap"]),
            "proposed_min_group_recall_ok": bool(min_group_recall >= gates["min_recall"]),
        }
        rows.append(row)
    out = Path("reports/e07")
    out.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(rows)
    df.to_csv(out / "mitigation_comparison.csv", index=False, encoding="utf-8")
    with pd.option_context("display.max_columns", None, "display.width", 250):
        print(df.drop(columns=["features"]).to_string(index=False))
    print(f"\nGuardado en {out / 'mitigation_comparison.csv'}")


if __name__ == "__main__":
    main()
