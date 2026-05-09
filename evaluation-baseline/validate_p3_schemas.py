#!/usr/bin/env python3
"""
P3 helper-schema validator for the SICS Human-State Proxy Benchmark Track.

This validator checks public synthetic/sample P3 helper files against
public helper schemas.

Boundary:
- helper-schema structure validation only
- not benchmark validation
- not scientific validation
- not Sal-Meter validation
- not CAIS compliance
- not mediation validation
- no raw human data processing
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]

SCHEMA_DIR = ROOT / "schemas"
SAMPLE_DIR = ROOT / "sample-data" / "synthetic-dyadic-session-001"

BOUNDARY_NOTICE = """\
This validator checks P3 helper-schema structure only.

It does not validate benchmark performance.
It does not validate scientific truth.
It does not validate Sal-Meter.
It does not grant CAIS compliance.
It does not validate mediation effectiveness.
It does not validate human-state measurement.
It does not process raw human data.
It does not process identifiable human data.
It does not process clinical data.
It does not process Sal-Meter raw input.
It does not process CAIS compliance dossiers.
"""

TARGETS = [
    {
        "label": "Human-State Packet A",
        "schema": SCHEMA_DIR / "human_state_packet.schema.json",
        "sample": SAMPLE_DIR / "human_state_packet_A.json",
    },
    {
        "label": "Human-State Packet B",
        "schema": SCHEMA_DIR / "human_state_packet.schema.json",
        "sample": SAMPLE_DIR / "human_state_packet_B.json",
    },
    {
        "label": "Dyadic Session Event",
        "schema": SCHEMA_DIR / "dyadic_session_event.schema.json",
        "sample": SAMPLE_DIR / "dyadic_session_event.json",
    },
    {
        "label": "Benchmark Session Container",
        "schema": SCHEMA_DIR / "benchmark_session.schema.json",
        "sample": SAMPLE_DIR / "benchmark_session_container.json",
    },
]


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path.relative_to(ROOT)}")

    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid JSON in {path.relative_to(ROOT)}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def format_error_path(error_path: Any) -> str:
    parts = list(error_path)

    if not parts:
        return "<root>"

    return ".".join(str(part) for part in parts)


def validate_sample(label: str, schema_path: Path, sample_path: Path) -> list[str]:
    errors: list[str] = []

    try:
        schema = load_json(schema_path)
        instance = load_json(sample_path)
    except Exception as exc:
        return [str(exc)]

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        return [f"Invalid schema in {schema_path.relative_to(ROOT)}: {exc}"]

    validator = Draft202012Validator(
        schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )

    validation_errors = sorted(
        validator.iter_errors(instance),
        key=lambda err: list(err.path),
    )

    for err in validation_errors:
        path_text = format_error_path(err.path)
        errors.append(
            f"{label}: {sample_path.relative_to(ROOT)} -> {path_text}: {err.message}"
        )

    return errors


def run_required_file_checks() -> list[str]:
    errors: list[str] = []

    required_files = [
        SCHEMA_DIR / "human_state_packet.schema.json",
        SCHEMA_DIR / "dyadic_session_event.schema.json",
        SCHEMA_DIR / "benchmark_session.schema.json",
        SAMPLE_DIR / "README.md",
        SAMPLE_DIR / "human_state_packet_A.json",
        SAMPLE_DIR / "human_state_packet_B.json",
        SAMPLE_DIR / "dyadic_session_event.json",
        SAMPLE_DIR / "benchmark_session_container.json",
    ]

    for path in required_files:
        if not path.exists():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")

    return errors


def print_header() -> None:
    print("SICS Human-State Proxy Benchmark Track")
    print("P3 Helper Schema Validator v0.1")
    print()
    print(BOUNDARY_NOTICE)


def print_pass() -> None:
    print("PASS: P3 synthetic dyadic helper files follow the current public helper schemas.")
    print()
    print("Validated files:")
    print()
    for target in TARGETS:
        print(f"- {target['label']}: {target['sample'].relative_to(ROOT)}")
    print()
    print("Boundary status:")
    print("- helper-schema structure validation only")
    print("- no raw human data validation")
    print("- no identifiable data validation")
    print("- no clinical data validation")
    print("- no Sal-Meter input validation")
    print("- no CAIS compliance validation")
    print("- no benchmark performance validation")
    print("- no mediation effectiveness validation")
    print()
    print("A successful P3 helper-schema validation means only:")
    print()
    print("The public synthetic/sample P3 helper files follow the expected helper-schema structure.")
    print()
    print("A successful P3 helper-schema validation does not mean:")
    print()
    print("The benchmark is validated.")
    print("The science is validated.")
    print("The mediation system works.")
    print("The dyadic recovery is real.")
    print("The repository is Sal-Meter.")
    print("The repository is CAIS-compliant.")
    print("The package is clinical, diagnostic, therapeutic, certified, device-ready, or production-ready.")


def print_fail(errors: list[str]) -> None:
    print("FAIL: P3 helper-schema validation failed.")
    print()
    print("Failures:")
    print()
    for error in errors:
        print(f"- {error}")
    print()
    print("Boundary status:")
    print("- FAIL means structure or boundary mismatch only")
    print("- FAIL is not scientific failure")
    print("- FAIL is not benchmark failure")
    print("- FAIL is not Sal-Meter failure")
    print("- FAIL is not CAIS compliance failure")
    print("- FAIL is not mediation effectiveness failure")


def main() -> int:
    print_header()

    errors: list[str] = []

    errors.extend(run_required_file_checks())

    if not errors:
        for target in TARGETS:
            errors.extend(
                validate_sample(
                    label=target["label"],
                    schema_path=target["schema"],
                    sample_path=target["sample"],
                )
            )

    if errors:
        print_fail(errors)
        return 1

    print_pass()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
