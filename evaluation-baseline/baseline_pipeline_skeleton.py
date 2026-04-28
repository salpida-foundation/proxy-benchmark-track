"""
Baseline Pipeline Skeleton
SICS Human-State Proxy Benchmark Track

This script demonstrates how a synthetic proxy benchmark feature file may be loaded,
checked, and passed into a transparent baseline evaluation skeleton.

Boundary:
- synthetic / toy / mock data only
- no raw human data
- no clinical, diagnostic, or therapeutic claim
- no Sal-Meter validation claim
- no CAIS compliance claim
"""

from __future__ import annotations

from pathlib import Path
import json
import sys

import pandas as pd

try:
    from sklearn.dummy import DummyClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import balanced_accuracy_score, classification_report
except ImportError as exc:
    raise SystemExit(
        "Missing dependency. Run: pip install -r evaluation-baseline/requirements.txt"
    ) from exc


REPO_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DIR = REPO_ROOT / "sample-data" / "synthetic-session-001"

FEATURES_PATH = SAMPLE_DIR / "features_baseline.csv"
METADATA_PATH = SAMPLE_DIR / "session_metadata.json"
QC_PATH = SAMPLE_DIR / "qc_report.json"


def load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def enforce_public_boundary(metadata: dict, qc_report: dict) -> None:
    dataset_type = metadata.get("dataset_type")
    raw_human_data_public = metadata.get("data_boundary", {}).get("raw_human_data_public")
    raw_human_data_present = qc_report.get("raw_human_data_present")
    identifiable_data_present = qc_report.get("identifiable_data_present")
    clinical_data_present = qc_report.get("clinical_data_present")
    sal_meter_input_present = qc_report.get("sal_meter_input_present")
    cais_compliance_claim_present = qc_report.get("cais_compliance_claim_present")

    if dataset_type != "synthetic":
        raise ValueError(
            "This public baseline skeleton only accepts synthetic sample data."
        )

    if raw_human_data_public is not False:
        raise ValueError("Boundary failure: raw_human_data_public must be false.")

    if raw_human_data_present is not False:
        raise ValueError("Boundary failure: raw human data must not be present.")

    if identifiable_data_present is not False:
        raise ValueError("Boundary failure: identifiable data must not be present.")

    if clinical_data_present is not False:
        raise ValueError("Boundary failure: clinical data must not be present.")

    if sal_meter_input_present is not False:
        raise ValueError("Boundary failure: Sal-Meter input data must not be present.")

    if cais_compliance_claim_present is not False:
        raise ValueError("Boundary failure: CAIS compliance claim must not be present.")


def load_features(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Required feature file not found: {path}")

    df = pd.read_csv(path)

    required_columns = {
        "feature_row_id",
        "session_id",
        "window_label",
        "public_data_status",
    }

    missing = required_columns.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required feature columns: {sorted(missing)}")

    if not (df["public_data_status"] == "synthetic").all():
        raise ValueError("Only synthetic public_data_status rows are allowed here.")

    return df


def run_baseline(df: pd.DataFrame) -> None:
    feature_columns = [
        "synthetic_hrv_index",
        "synthetic_eda_level",
        "synthetic_interaction_latency_ms",
        "synthetic_human_state_cost_proxy",
    ]

    missing_features = [col for col in feature_columns if col not in df.columns]
    if missing_features:
        raise ValueError(f"Missing expected synthetic feature columns: {missing_features}")

    X = df[feature_columns]
    y = df["window_label"]

    print("\n=== Boundary ===")
    print("Synthetic sample only.")
    print("Not evidence.")
    print("Not Sal-Meter validation.")
    print("Not CAIS compliance.")
    print("Not clinical, diagnostic, or therapeutic output.")

    print("\n=== Loaded feature table ===")
    print(df[["feature_row_id", "session_id", "window_label", "public_data_status"]])

    print("\n=== Feature columns ===")
    for col in feature_columns:
        print(f"- {col}")

    unique_classes = y.nunique()
    row_count = len(df)

    if row_count < 6 or unique_classes < 2:
        print("\n=== Baseline model skipped ===")
        print("Reason: too few synthetic rows for a meaningful split.")
        print("This is expected for synthetic-session-001.")
        print("The current file demonstrates structure, not model performance.")
        return

    # For larger synthetic examples only.
    # train_test_split supports arrays or pandas DataFrames and accepts test_size,
    # random_state, shuffle, and stratify parameters.
    stratify_arg = y if unique_classes > 1 else None

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.33,
        random_state=42,
        shuffle=True,
        stratify=stratify_arg,
    )

    model = DummyClassifier(strategy="most_frequent")
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("\n=== Toy baseline output ===")
    print(f"Balanced accuracy: {balanced_accuracy_score(y_test, y_pred):.3f}")
    print("\nClassification report:")
    print(classification_report(y_test, y_pred, zero_division=0))

    print("\nReminder: output from synthetic data is not scientific evidence.")


def main() -> int:
    try:
        metadata = load_json(METADATA_PATH)
        qc_report = load_json(QC_PATH)
        enforce_public_boundary(metadata, qc_report)

        df = load_features(FEATURES_PATH)
        run_baseline(df)

    except Exception as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
