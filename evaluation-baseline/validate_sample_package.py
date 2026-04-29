#!/usr/bin/env python3
"""
SICS Human-State Proxy Benchmark Track
Synthetic Sample Package Validator v0.1

Purpose:
    Validate the public synthetic/sample package structure against helper schemas.

This script checks:
    - required file presence;
    - JSON parse validity;
    - CSV parse validity;
    - JSON Schema alignment;
    - synthetic/public boundary fields;
    - absence of raw human data, Sal-Meter input, and CAIS compliance claims.

This script does NOT validate:
    - benchmark performance;
    - scientific truth;
    - human-state inference;
    - diagnostic or clinical status;
    - Sal-Meter input;
    - CAIS compliance;
    - certification or device readiness.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError, ValidationError
except ImportError as exc:
    print("FAIL: Missing dependency: jsonschema")
    print("Install it with:")
    print("  pip install jsonschema")
    raise SystemExit(1) from exc


REQUIRED_SAMPLE_FILES = [
    "session_metadata.json",
    "streams_manifest.csv",
    "events.csv",
    "labels.csv",
    "qc_report.json",
    "features_baseline.csv",
    "splits.json",
    "operator_log.md",
]

JSON_SCHEMA_MAP = {
    "session_metadata.json": "session-metadata.schema.json",
    "qc_report.json": "qc-report.schema.json",
    "splits.json": "splits.schema.json",
}

CSV_SCHEMA_MAP = {
    "events.csv": "event-markers.schema.json",
    "labels.csv": "labels.schema.json",
    "streams_manifest.csv": "streams-manifest.schema.json",
    "features_baseline.csv": "features-baseline.schema.json",
}

BOUNDARY_FALSE_PATHS = [
    ("session_metadata.json", ["data_boundary", "raw_human_data_public"]),
    ("session_metadata.json", ["data_boundary", "identifiable_data_public"]),
    ("session_metadata.json", ["data_boundary", "clinical_data_public"]),
    ("session_metadata.json", ["data_boundary", "sal_meter_input_present"]),
    ("session_metadata.json", ["data_boundary", "cais_compliance_claim_present"]),
    ("qc_report.json", ["raw_human_data_present"]),
    ("qc_report.json", ["identifiable_data_present"]),
    ("qc_report.json", ["clinical_data_present"]),
    ("qc_report.json", ["face_voice_video_audio_present"]),
    ("qc_report.json", ["sal_meter_input_present"]),
    ("qc_report.json", ["cais_compliance_claim_present"]),
    ("splits.json", ["raw_human_data_present"]),
]

BOUNDARY_TRUE_PATHS = [
    ("session_metadata.json", ["synthetic_status_declared"]),
    ("session_metadata.json", ["data_boundary", "public_release_allowed"]),
    ("qc_report.json", ["synthetic_status_declared"]),
    ("qc_report.json", ["leakage_review", "reviewed"]),
]

OPERATOR_LOG_REQUIRED_PHRASES = [
    "synthetic",
    "raw human data",
    "clinical",
    "Sal-Meter",
    "CAIS",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_schema(schema_path: Path) -> Dict[str, Any]:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    return schema


def read_csv_rows(csv_path: Path) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError(f"{csv_path} has no header row.")

        for row in reader:
            cleaned: Dict[str, str] = {}
            for key, value in row.items():
                if key is None:
                    continue
                clean_key = key.strip()
                clean_value = "" if value is None else value.strip()
                cleaned[clean_key] = clean_value
            rows.append(cleaned)

    if not rows:
        raise ValueError(f"{csv_path} has no data rows.")

    return rows


def compact_error_path(error: ValidationError) -> str:
    if not error.path:
        return "<root>"
    return ".".join(str(part) for part in error.path)


def validate_instance(instance: Any, schema: Dict[str, Any]) -> List[str]:
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))

    messages = []
    for error in errors:
        messages.append(f"{compact_error_path(error)}: {error.message}")
    return messages


def validate_csv_rows(rows: Iterable[Dict[str, str]], schema: Dict[str, Any]) -> List[str]:
    all_errors: List[str] = []
    validator = Draft202012Validator(schema)

    required_fields = set(schema.get("required", []))

    for index, row in enumerate(rows, start=2):  # CSV line 1 is header.
        normalized: Dict[str, str] = {}

        for key, value in row.items():
            if value == "" and key not in required_fields:
                continue
            normalized[key] = value

        errors = sorted(validator.iter_errors(normalized), key=lambda e: list(e.path))
        for error in errors:
            all_errors.append(
                f"line {index}, {compact_error_path(error)}: {error.message}"
            )

    return all_errors


def get_nested_value(data: Dict[str, Any], path: List[str]) -> Any:
    current: Any = data
    for part in path:
        if not isinstance(current, dict) or part not in current:
            raise KeyError(".".join(path))
        current = current[part]
    return current


def check_boundary_flags(sample_dir: Path) -> List[str]:
    errors: List[str] = []

    loaded_json: Dict[str, Dict[str, Any]] = {}
    for filename in JSON_SCHEMA_MAP:
        loaded_json[filename] = load_json(sample_dir / filename)

    for filename, path in BOUNDARY_FALSE_PATHS:
        try:
            value = get_nested_value(loaded_json[filename], path)
        except KeyError:
            errors.append(f"{filename}: missing boundary field {'.'.join(path)}")
            continue

        if value is not False:
            errors.append(f"{filename}: {'.'.join(path)} must be false, got {value!r}")

    for filename, path in BOUNDARY_TRUE_PATHS:
        try:
            value = get_nested_value(loaded_json[filename], path)
        except KeyError:
            errors.append(f"{filename}: missing boundary field {'.'.join(path)}")
            continue

        if value is not True:
            errors.append(f"{filename}: {'.'.join(path)} must be true, got {value!r}")

    dataset_type = loaded_json["session_metadata.json"].get("dataset_type")
    if dataset_type != "synthetic":
        errors.append(
            f"session_metadata.json: dataset_type should be 'synthetic', got {dataset_type!r}"
        )

    qc_dataset_type = loaded_json["qc_report.json"].get("dataset_type")
    if qc_dataset_type != "synthetic":
        errors.append(
            f"qc_report.json: dataset_type should be 'synthetic', got {qc_dataset_type!r}"
        )

    split_dataset_type = loaded_json["splits.json"].get("dataset_type")
    if split_dataset_type != "synthetic":
        errors.append(
            f"splits.json: dataset_type should be 'synthetic', got {split_dataset_type!r}"
        )

    return errors


def check_operator_log(sample_dir: Path) -> List[str]:
    errors: List[str] = []
    path = sample_dir / "operator_log.md"
    text = path.read_text(encoding="utf-8")

    lowered = text.lower()

    for phrase in OPERATOR_LOG_REQUIRED_PHRASES:
        if phrase.lower() not in lowered:
            errors.append(f"operator_log.md: missing expected boundary phrase: {phrase}")

    return errors


def check_required_files(sample_dir: Path) -> List[str]:
    errors: List[str] = []

    for filename in REQUIRED_SAMPLE_FILES:
        if not (sample_dir / filename).exists():
            errors.append(f"missing required sample file: {filename}")

    return errors


def validate_package() -> Tuple[bool, List[str]]:
    root = repo_root()
    sample_dir = root / "sample-data" / "synthetic-session-001"
    schemas_dir = root / "schemas"

    errors: List[str] = []

    if not sample_dir.exists():
        return False, [f"sample directory not found: {sample_dir}"]

    if not schemas_dir.exists():
        return False, [f"schemas directory not found: {schemas_dir}"]

    errors.extend(check_required_files(sample_dir))

    if errors:
        return False, errors

    # Validate JSON files against object schemas.
    for data_filename, schema_filename in JSON_SCHEMA_MAP.items():
        data_path = sample_dir / data_filename
        schema_path = schemas_dir / schema_filename

        try:
            data = load_json(data_path)
            schema = load_schema(schema_path)
            validation_errors = validate_instance(data, schema)
            errors.extend([f"{data_filename}: {msg}" for msg in validation_errors])
        except (json.JSONDecodeError, SchemaError, ValidationError, OSError) as exc:
            errors.append(f"{data_filename}: {exc}")

    # Validate CSV rows against row-object schemas.
    for csv_filename, schema_filename in CSV_SCHEMA_MAP.items():
        csv_path = sample_dir / csv_filename
        schema_path = schemas_dir / schema_filename

        try:
            rows = read_csv_rows(csv_path)
            schema = load_schema(schema_path)
            validation_errors = validate_csv_rows(rows, schema)
            errors.extend([f"{csv_filename}: {msg}" for msg in validation_errors])
        except (ValueError, SchemaError, ValidationError, OSError) as exc:
            errors.append(f"{csv_filename}: {exc}")

    # Boundary checks that go beyond schema shape.
    try:
        errors.extend(check_boundary_flags(sample_dir))
    except (json.JSONDecodeError, OSError, KeyError) as exc:
        errors.append(f"boundary check failed: {exc}")

    try:
        errors.extend(check_operator_log(sample_dir))
    except OSError as exc:
        errors.append(f"operator_log.md: {exc}")

    return len(errors) == 0, errors


def main() -> int:
    ok, errors = validate_package()

    print("SICS Human-State Proxy Benchmark Track")
    print("Synthetic Sample Package Validator v0.1")
    print("")

    if ok:
        print("PASS: sample-data/synthetic-session-001 follows the current public helper structure.")
        print("")
        print("Boundary status:")
        print("- synthetic/sample structure validation only")
        print("- no raw human data validation")
        print("- no Sal-Meter input validation")
        print("- no CAIS compliance validation")
        print("- no diagnostic, therapeutic, or clinical validation")
        print("- no benchmark performance validation")
        return 0

    print("FAIL: sample package validation found issues.")
    print("")
    for index, error in enumerate(errors, start=1):
        print(f"{index}. {error}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
