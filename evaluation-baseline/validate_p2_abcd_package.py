#!/usr/bin/env python3
"""
P2 A/B/C/D package validator for the SICS Human-State Proxy Benchmark Track.

This validator checks the structural and cross-reference integrity of the
public synthetic helper package at sample-data/p2-ai-output-abcd/.

It complements the A/B/C/D consequence evaluator: the evaluator computes
proxy-only comparison scores, while this validator acts as a structural
gatekeeper for required files, condition-label cross-references, condition
field consistency, and boundary flags.

Boundary:
- helper-structure validation only
- synthetic/sample helper files only
- not benchmark validation
- not scientific validation
- not Sal-Meter validation
- not CAIS compliance
- not mediation validation
- not dyadic recovery validation
- not termination-gate accuracy validation
- no raw human data processing
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_DIR = ROOT / "sample-data" / "p2-ai-output-abcd"

CONDITION_CODES = ["A", "B", "C", "D"]

CONDITION_SOURCE_FILES = {
    "A": "condition_A_validating_regulatory.json",
    "B": "condition_B_information_only_neutral.json",
    "C": "condition_C_over_validation_comparator.json",
    "D": "condition_D_minimizing_dismissive.json",
}

REQUIRED_FILES = [
    "README.md",
    "condition_labels.json",
    "condition_A_validating_regulatory.json",
    "condition_B_information_only_neutral.json",
    "condition_C_over_validation_comparator.json",
    "condition_D_minimizing_dismissive.json",
    "expected_evaluator_output.json",
]

REQUIRED_PROXY_ONLY_FIELDS = [
    "overload_delta",
    "recovery_burden_delta",
    "relational_stability_delta",
    "asymmetry_risk",
    "false_recovery_risk",
    "termination_readiness",
    "audit_status",
]

REQUIRED_TRUE_FLAGS = ["synthetic_only", "public_helper_only"]

REQUIRED_FALSE_FLAGS = [
    "real_participant_data",
    "raw_human_data_included",
    "clinical_data_included",
    "diagnostic_data_included",
    "therapeutic_data_included",
    "surveillance_data_included",
    "sal_meter_raw_input_included",
    "cais_trace_data_included",
    "production_intervention_log_included",
]

EXPECTED_OUTPUT_REQUIRED_KEYS = [
    "expected_output_id",
    "boundary_flags",
    "input_files_expected",
    "comparison_conditions",
    "expected_proxy_only_metrics",
    "expected_output_fields_allowed",
]

BOUNDARY_NOTICE = """\
This validator checks P2 A/B/C/D helper-package structure only.

It does not validate benchmark performance.
It does not validate scientific truth.
It does not validate Sal-Meter.
It does not grant CAIS compliance.
It does not validate mediation effectiveness.
It does not validate dyadic recovery.
It does not validate termination-gate accuracy.
It does not process raw human data.
"""


def load_json(path: Path) -> Dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def check_required_files() -> List[str]:
    errors: List[str] = []
    for filename in REQUIRED_FILES:
        if not (PACKAGE_DIR / filename).exists():
            errors.append(f"missing required file: {filename}")
    return errors


def check_boundary_flags(source: str, flags: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for flag in REQUIRED_TRUE_FLAGS:
        if flags.get(flag) is not True:
            errors.append(f"{source}: boundary flag '{flag}' must be true")
    for flag in REQUIRED_FALSE_FLAGS:
        if flags.get(flag) is not False:
            errors.append(f"{source}: boundary flag '{flag}' must be false")
    return errors


def check_condition_labels(labels: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    conditions = labels.get("conditions", {})

    for code in CONDITION_CODES:
        if code not in conditions:
            errors.append(f"condition_labels: missing condition '{code}'")
            continue
        entry = conditions[code]

        if entry.get("condition_code") != code:
            errors.append(
                f"condition_labels[{code}]: condition_code mismatch "
                f"(got {entry.get('condition_code')!r})"
            )

        expected_source = CONDITION_SOURCE_FILES[code]
        if entry.get("source_file") != expected_source:
            errors.append(
                f"condition_labels[{code}]: source_file mismatch "
                f"(got {entry.get('source_file')!r}, expected {expected_source!r})"
            )
        elif not (PACKAGE_DIR / expected_source).exists():
            errors.append(
                f"condition_labels[{code}]: source_file does not exist: {expected_source}"
            )

    if "boundary_flags" in labels:
        errors.extend(check_boundary_flags("condition_labels", labels["boundary_flags"]))
    else:
        errors.append("condition_labels: missing boundary_flags")

    return errors


def check_condition_file(code: str, labels_entry: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    filename = CONDITION_SOURCE_FILES[code]
    path = PACKAGE_DIR / filename
    if not path.exists():
        return [f"condition {code}: file not found: {filename}"]

    data = load_json(path)

    if data.get("condition_code") != code:
        errors.append(
            f"{filename}: condition_code mismatch (got {data.get('condition_code')!r})"
        )

    expected_role = f"condition_{code.lower()}"
    if data.get("condition_role") != expected_role:
        errors.append(
            f"{filename}: condition_role mismatch "
            f"(got {data.get('condition_role')!r}, expected {expected_role!r})"
        )

    label_id = labels_entry.get("condition_id")
    if data.get("condition_id") != label_id:
        errors.append(
            f"{filename}: condition_id mismatch with condition_labels "
            f"(file {data.get('condition_id')!r} vs label {label_id!r})"
        )

    proxy_fields = data.get("proxy_only_consequence_fields", {})
    present = set(proxy_fields.keys())
    expected = set(REQUIRED_PROXY_ONLY_FIELDS)
    extra = sorted(present - expected)
    missing = sorted(expected - present)
    if extra:
        errors.append(f"{filename}: unexpected proxy-only fields: {extra}")
    if missing:
        errors.append(f"{filename}: missing proxy-only fields: {missing}")

    if "boundary_flags" in data:
        errors.extend(check_boundary_flags(filename, data["boundary_flags"]))
    else:
        errors.append(f"{filename}: missing boundary_flags")

    return errors


def check_expected_output() -> List[str]:
    errors: List[str] = []
    path = PACKAGE_DIR / "expected_evaluator_output.json"
    if not path.exists():
        return ["missing expected_evaluator_output.json"]
    data = load_json(path)
    for key in EXPECTED_OUTPUT_REQUIRED_KEYS:
        if key not in data:
            errors.append(f"expected_evaluator_output.json: missing key '{key}'")
    if "boundary_flags" in data:
        errors.extend(
            check_boundary_flags("expected_evaluator_output.json", data["boundary_flags"])
        )
    return errors


def validate_package() -> List[str]:
    if not PACKAGE_DIR.exists():
        return [f"package directory not found: {PACKAGE_DIR}"]

    errors: List[str] = []
    errors.extend(check_required_files())

    labels_path = PACKAGE_DIR / "condition_labels.json"
    if labels_path.exists():
        labels = load_json(labels_path)
        errors.extend(check_condition_labels(labels))
        conditions = labels.get("conditions", {})
        for code in CONDITION_CODES:
            entry = conditions.get(code, {})
            errors.extend(check_condition_file(code, entry))
    else:
        errors.append("condition_labels.json not found; cannot cross-check conditions")

    errors.extend(check_expected_output())
    return errors


def main() -> int:
    errors = validate_package()

    if errors:
        print("FAIL: sample-data/p2-ai-output-abcd package integrity check failed.")
        print("")
        for error in errors:
            print(f"  - {error}")
        print("")
        print(BOUNDARY_NOTICE)
        return 1

    print("PASS: sample-data/p2-ai-output-abcd package structure and "
          "cross-references are consistent.")
    print("")
    print(BOUNDARY_NOTICE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
