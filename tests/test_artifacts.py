import pandas as pd

from inf8239_u04.data import features, load_data
from inf8239_u04.governance import validate_raci

SEPARATORS = (" and ", ",", ";", "/", " y ")
ROLES = {"key", "split_only", "feature", "audit_only", "label"}


def test_raci_has_exactly_one_accountable_per_activity():
    raci = pd.read_csv("student_inputs/raci.csv")
    validate_raci(raci)
    assert raci["activity"].is_unique
    for accountable in raci["A"]:
        assert not any(s in f" {accountable} " for s in SEPARATORS), accountable


def test_raci_has_a_responsible_for_each_activity():
    raci = pd.read_csv("student_inputs/raci.csv")
    assert (raci["R"].astype(str).str.strip() != "").all()


def test_inventory_covers_every_dataset_column():
    inv = pd.read_csv("docs/data_inventory.csv")
    assert inv["field"].is_unique
    assert set(inv["field"]) == set(load_data().columns)


def test_inventory_documents_minimization_and_retention():
    inv = pd.read_csv("docs/data_inventory.csv")
    assert set(inv["role"]) <= ROLES
    for col in ["role", "sensitivity", "minimization", "retention"]:
        assert inv[col].notna().all()
        assert (inv[col].astype(str).str.strip() != "").all()


def test_inventory_features_match_the_model_features():
    inv = pd.read_csv("docs/data_inventory.csv")
    model_features = set(features(load_data()).columns)
    assert set(inv.loc[inv["role"] == "feature", "field"]) == model_features
    excluded = set(inv.loc[inv["role"] != "feature", "field"])
    assert not (excluded & model_features)
