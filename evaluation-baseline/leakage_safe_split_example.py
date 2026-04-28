"""
Leakage-Safe Split Example
SICS Human-State Proxy Benchmark Track

This script demonstrates split-boundary thinking for synthetic proxy benchmark data.

Boundary:
- synthetic structure demonstration only
- no raw human data
- no clinical, diagnostic, therapeutic, surveillance, or human-ranking claim
- no Sal-Meter validation claim
- no CAIS compliance claim
"""

from __future__ import annotations

from pathlib import Path
import json
import sys

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DIR = REPO_ROOT / "sample-data" / "synthetic-session-001"

FEATURES_PATH = SAMPLE_DIR / "features_baseline.csv"
SPLITS_PATH = SAMPLE_DIR / "splits.json"


LEAKAGE_RISK_CHECKS = [
    "Labels must not be embedded in filenames.",
    "Labels must not be embedded in folder names.",
    "Labels must not be recoverable from session order.",
    "Participant identity must not leak across train and test splits.",
    "Device identity must not become a shortcut label.",
    "Operator identity must not become a shortcut label.",
    "Day or date must not become a shortcut label.",
    "Preprocessing must be fixed before final evaluation.",
    "Final holdout must not be tuned on.",
    "Excluded sessions must be logged.",
    "Failed or partial sessions must be recorded.",
]


def load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_features(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Required feature file not found: {path}")
    return pd.read_csv(path)


def check_public_status(df: pd.DataFrame) -> None:
    if "public_data_status" not in df.columns:
        raise ValueError("Missing public_data_status column.")

    if not (df["public_data_status"] == "synthetic").all():
        raise ValueError("This example only accepts synthetic data rows.")


def inspect_split_file(split_info: dict) -> None:
    print("\n=== Split file boundary ===")
    print(f"Dataset type: {split_info.get('dataset_type')}")
    print(f"Split role: {split_info.get('split_file_role')}")
    print(f"Split strategy: {split_info.get('split_strategy')}")
    print(f"Raw human data present: {split_info.get('raw_human_data_present')}")

    if split_info.get("dataset_type") != "synthetic":
        raise ValueError("This public example only accepts synthetic split files.")

    if split_info.get("raw_human_data_present") is not False:
        raise ValueError("Raw human data must not be present.")

    print("\n=== Declared splits ===")
    splits = split_info.get("splits", {})
    for split_name in ["train", "validation", "test"]:
        print(f"{split_name}: {splits.get(split_name, [])}")


def print_leakage_risk_checks() -> None:
    print("\n=== Leakage risk checklist ===")
    for item in LEAKAGE_RISK_CHECKS:
        print(f"- {item}")


def inspect_current_sample(df: pd.DataFrame) -> None:
    print("\n=== Current synthetic feature rows ===")
    display_columns = [
        "feature_row_id",
        "session_id",
        "window_label",
        "public_data_status",
    ]
    available_columns = [col for col in display_columns if col in df.columns]
    print(df[available_columns])

    session_count = df["session_id"].nunique() if "session_id" in df.columns else 0
    row_count = len(df)

    print("\n=== Current sample limitation ===")
    print(f"Row count: {row_count}")
    print(f"Unique session count: {session_count}")

    if session_count < 3:
        print("This sample is too small for a real leakage-safe benchmark split.")
        print("That is expected. This folder demonstrates structure only.")


def recommended_real_split_strategy() -> None:
    print("\n=== Recommended future split hierarchy ===")
    print("For future non-public or controlled benchmark work, prefer:")
    print("1. participant holdout")
    print("2. day holdout")
    print("3. device holdout")
    print("4. session holdout")
    print("5. condition holdout")
    print("6. operator holdout")
    print("\nDo not tune on the final holdout set.")


def final_boundary() -> None:
    print("\n=== Final boundary ===")
    print("Synthetic structure demonstration only.")
    print("Not benchmark evidence.")
    print("Not Sal-Meter validation.")
    print("Not CAIS compliance.")
    print("Not clinical, diagnostic, or therapeutic output.")
    print("Not a human-ranking or surveillance system.")


def main() -> int:
    try:
        df = load_features(FEATURES_PATH)
        check_public_status(df)

        split_info = load_json(SPLITS_PATH)
        inspect_split_file(split_info)

        print_leakage_risk_checks()
        inspect_current_sample(df)
        recommended_real_split_strategy()
        final_boundary()

    except Exception as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
