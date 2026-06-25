#!/usr/bin/env python3
"""
P3 helper-schema validator for the SICS Human-State Proxy Benchmark Track.

This validator checks public synthetic/sample P3 helper files against
public helper schemas.

Boundary:

* helper-schema structure validation only
* synthetic/sample helper files only
* not benchmark validation
* not scientific validation
* not Sal-Meter validation
* not CAIS compliance
* not mediation validation
* not dyadic recovery validation
* not termination-gate accuracy validation
* no raw human data processing
  """

from **future** import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(**file**).resolve().parents[1]

SCHEMA_DIR = ROOT / "schemas"
SAMPLE_DIR = ROOT / "sample-data" / "synthetic-dyadic-session-001"
P3_CASE_DIR = ROOT / "sample-data" / "p3-dyadic-recovery-cases"

BOUNDARY_NOTICE = """
This validator checks P3 helper-schema structure only.

It does not validate benchmark performance.
It does not validate scientific truth.
It does not validate Sal-Meter.
It does not grant CAIS compliance.
It does not validate mediation effectiveness.
It does not validate dyadic recovery.
It does not validate termination-gate accuracy.
It does not validate human-state measurement.
It does not process raw human data.
It does not process identifiable human data.
It does not process clinical data.
It does not process Sal-Meter raw input.
It does not process CAIS compliance dossiers.
"""

BASELINE_TARGETS = [
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
"label": "Dyadic Recovery Event",
"schema": SCHEMA_DIR / "dyadic_recovery_event.schema.json",
"sample": SAMPLE_DIR / "dyadic_recovery_event.json",
},
{
"label": "Benchmark Session Container",
"schema": SCHEMA_DIR / "benchmark_session.schema.json",
"sample": SAMPLE_DIR / "benchmark_session_container.json",
},
]

P3_REQUIRED_CASES = [
{
"folder": "true-recovery-candidate",
"label": "P3 true recovery candidate",
"expected_pattern": "true_recovery_candidate",
},
{
"folder": "asymmetric-recovery",
"label": "P3 asymmetric recovery",
"expected_pattern": "asymmetric_recovery",
},
{
"folder": "false-recovery-silence-risk",
"label": "P3 false recovery silence-risk",
"expected_pattern": "false_recovery_silence_risk",
},
]

P3_REQUIRED_FILES = [
"README.md",
"baseline_packet_A.json",
"baseline_packet_B.json",
"ai_output.json",
"post_output_packet_A.json",
"post_output_packet_B.json",
"dyadic_recovery_event.json",
"audit_log.json",
]

P3_SCHEMA_FILE_MAP = [
{
"filename": "baseline_packet_A.json",
"schema": SCHEMA_DIR / "human_state_packet.schema.json",
"label_suffix": "baseline packet A",
},
{
"filename": "baseline_packet_B.json",
"schema": SCHEMA_DIR / "human_state_packet.schema.json",
"label_suffix": "baseline packet B",
},
{
"filename": "post_output_packet_A.json",
"schema": SCHEMA_DIR / "human_state_packet.schema.json",
"label_suffix": "post-output packet A",
},
{
"filename": "post_output_packet_B.json",
"schema": SCHEMA_DIR / "human_state_packet.schema.json",
"label_suffix": "post-output packet B",
},
{
"filename": "dyadic_recovery_event.json",
"schema": SCHEMA_DIR / "dyadic_recovery_event.schema.json",
"label_suffix": "dyadic recovery event",
},
]

P3_JSON_SYNTAX_ONLY_FILES = [
"ai_output.json",
"audit_log.json",
]

README_BOUNDARY_TERMS = [
"synthetic",
"public-helper",
"raw human data",
"real participant",
]

def load_json(path: Path) -> Any:
if not path.exists():
raise FileNotFoundError(f"Missing file: {path.relative_to(ROOT)}")

```
try:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)
except json.JSONDecodeError as exc:
    raise ValueError(
        f"Invalid JSON in {path.relative_to(ROOT)}: "
        f"line {exc.lineno}, column {exc.colno}: {exc.msg}"
    ) from exc
```

def load_text(path: Path) -> str:
if not path.exists():
raise FileNotFoundError(f"Missing file: {path.relative_to(ROOT)}")

```
return path.read_text(encoding="utf-8")
```

def format_error_path(error_path: Any) -> str:
parts = list(error_path)

```
if not parts:
    return "<root>"

return ".".join(str(part) for part in parts)
```

def validate_sample(label: str, schema_path: Path, sample_path: Path) -> list[str]:
errors: list[str] = []

```
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
```

def run_baseline_required_file_checks() -> list[str]:
errors: list[str] = []

```
required_files = [
    SCHEMA_DIR / "human_state_packet.schema.json",
    SCHEMA_DIR / "dyadic_session_event.schema.json",
    SCHEMA_DIR / "dyadic_recovery_event.schema.json",
    SCHEMA_DIR / "benchmark_session.schema.json",
    SAMPLE_DIR / "README.md",
    SAMPLE_DIR / "human_state_packet_A.json",
    SAMPLE_DIR / "human_state_packet_B.json",
    SAMPLE_DIR / "dyadic_session_event.json",
    SAMPLE_DIR / "dyadic_recovery_event.json",
    SAMPLE_DIR / "benchmark_session_container.json",
]

for path in required_files:
    if not path.exists():
        errors.append(f"Missing required file: {path.relative_to(ROOT)}")

return errors
```

def run_p3_case_required_file_checks() -> list[str]:
errors: list[str] = []

```
if not P3_CASE_DIR.exists():
    return [f"Missing required directory: {P3_CASE_DIR.relative_to(ROOT)}"]

for case in P3_REQUIRED_CASES:
    case_dir = P3_CASE_DIR / case["folder"]

    if not case_dir.exists():
        errors.append(f"Missing required P3 case folder: {case_dir.relative_to(ROOT)}")
        continue

    for filename in P3_REQUIRED_FILES:
        path = case_dir / filename
        if not path.exists():
            errors.append(f"Missing required P3 case file: {path.relative_to(ROOT)}")

return errors
```

def run_p3_case_readme_boundary_checks() -> list[str]:
errors: list[str] = []

```
for case in P3_REQUIRED_CASES:
    readme_path = P3_CASE_DIR / case["folder"] / "README.md"

    try:
        text = load_text(readme_path).lower()
    except Exception as exc:
        errors.append(str(exc))
        continue

    for term in README_BOUNDARY_TERMS:
        if term not in text:
            errors.append(
                f"{case['label']}: {readme_path.relative_to(ROOT)} "
                f"does not contain expected boundary term: {term}"
            )

return errors
```

def run_p3_case_json_syntax_checks() -> list[str]:
errors: list[str] = []

```
for case in P3_REQUIRED_CASES:
    case_dir = P3_CASE_DIR / case["folder"]

    for filename in P3_JSON_SYNTAX_ONLY_FILES:
        path = case_dir / filename
        try:
            load_json(path)
        except Exception as exc:
            errors.append(str(exc))

return errors
```

def run_p3_case_schema_checks() -> list[str]:
errors: list[str] = []

```
for case in P3_REQUIRED_CASES:
    case_dir = P3_CASE_DIR / case["folder"]

    for target in P3_SCHEMA_FILE_MAP:
        sample_path = case_dir / target["filename"]
        label = f"{case['label']} {target['label_suffix']}"

        errors.extend(
            validate_sample(
                label=label,
                schema_path=target["schema"],
                sample_path=sample_path,
            )
        )

return errors
```

def require_event_value(
errors: list[str],
label: str,
event: dict[str, Any],
path: list[str],
expected: Any,
) -> None:
current: Any = event

```
try:
    for part in path:
        current = current[part]
except Exception:
    errors.append(f"{label}: missing expected event field: {'.'.join(path)}")
    return

if current != expected:
    errors.append(
        f"{label}: expected {'.'.join(path)} to be {expected!r}, got {current!r}"
    )
```

def require_event_value_in(
errors: list[str],
label: str,
event: dict[str, Any],
path: list[str],
expected_values: set[Any],
) -> None:
current: Any = event

```
try:
    for part in path:
        current = current[part]
except Exception:
    errors.append(f"{label}: missing expected event field: {'.'.join(path)}")
    return

if current not in expected_values:
    errors.append(
        f"{label}: expected {'.'.join(path)} to be one of "
        f"{sorted(expected_values)!r}, got {current!r}"
    )
```

def require_event_flag(
errors: list[str],
label: str,
event: dict[str, Any],
expected_flag: str,
) -> None:
flags = (
event.get("false_recovery_check", {})
.get("false_recovery_flags", [])
)

```
if expected_flag not in flags:
    errors.append(
        f"{label}: expected false_recovery_flags to include {expected_flag!r}"
    )
```

def run_p3_case_pattern_checks() -> list[str]:
errors: list[str] = []

```
for case in P3_REQUIRED_CASES:
    case_dir = P3_CASE_DIR / case["folder"]
    event_path = case_dir / "dyadic_recovery_event.json"
    label = case["label"]

    try:
        event = load_json(event_path)
    except Exception as exc:
        errors.append(str(exc))
        continue

    pattern = case["expected_pattern"]

    if pattern == "true_recovery_candidate":
        require_event_value(
            errors,
            label,
            event,
            ["human_state_delta", "participant_a_direction"],
            "improved",
        )
        require_event_value(
            errors,
            label,
            event,
            ["human_state_delta", "participant_b_direction"],
            "improved",
        )
        require_event_value(
            errors,
            label,
            event,
            ["human_state_delta", "dyadic_direction"],
            "toward_recovery",
        )
        require_event_value(
            errors,
            label,
            event,
            ["human_state_delta", "recovery_asymmetry"],
            "none_detected",
        )
        require_event_value(
            errors,
            label,
            event,
            ["dyadic_recovery_assessment", "recovery_label"],
            "recovery_candidate",
        )
        require_event_value(
            errors,
            label,
            event,
            ["dyadic_recovery_assessment", "termination_allowed"],
            True,
        )
        require_event_value(
            errors,
            label,
            event,
            ["false_recovery_check", "false_recovery_detected"],
            False,
        )

    elif pattern == "asymmetric_recovery":
        require_event_value(
            errors,
            label,
            event,
            ["human_state_delta", "participant_a_direction"],
            "improved",
        )
        require_event_value(
            errors,
            label,
            event,
            ["human_state_delta", "participant_b_direction"],
            "worsened",
        )
        require_event_value(
            errors,
            label,
            event,
            ["human_state_delta", "dyadic_direction"],
            "mixed",
        )
        require_event_value_in(
            errors,
            label,
            event,
            ["human_state_delta", "recovery_asymmetry"],
            {
                "participant_a_only_improved",
                "participant_b_only_improved",
                "one_improved_one_worsened",
                "unknown",
            },
        )
        require_event_value(
            errors,
            label,
            event,
            ["dyadic_recovery_assessment", "termination_allowed"],
            False,
        )
        require_event_value(
            errors,
            label,
            event,
            ["false_recovery_check", "false_recovery_detected"],
            True,
        )
        require_event_flag(errors, label, event, "one_sided_recovery")
        require_event_flag(errors, label, event, "one_improved_one_worsened")

    elif pattern == "false_recovery_silence_risk":
        require_event_value(
            errors,
            label,
            event,
            ["human_state_delta", "dyadic_direction"],
            "mixed",
        )
        require_event_value(
            errors,
            label,
            event,
            ["dyadic_recovery_assessment", "recovery_label"],
            "false_recovery",
        )
        require_event_value(
            errors,
            label,
            event,
            ["dyadic_recovery_assessment", "termination_allowed"],
            False,
        )
        require_event_value(
            errors,
            label,
            event,
            ["false_recovery_check", "false_recovery_detected"],
            True,
        )
        require_event_flag(
            errors,
            label,
            event,
            "silence_misclassified_as_recovery",
        )
        require_event_flag(
            errors,
            label,
            event,
            "synchrony_overinterpreted",
        )

    else:
        errors.append(f"{label}: unknown expected pattern: {pattern}")

return errors
```

def print_header() -> None:
print("SICS Human-State Proxy Benchmark Track")
print("P3 Helper Schema Validator v0.2")
print()
print(BOUNDARY_NOTICE)

def print_pass() -> None:
print("PASS: P3 synthetic helper files follow the current public helper schemas.")
print()
print("Validated baseline sample files:")
print()

```
for target in BASELINE_TARGETS:
    print(f"- {target['label']}: {target['sample'].relative_to(ROOT)}")

print()
print("Validated P3 dyadic recovery case files:")
print()

for case in P3_REQUIRED_CASES:
    case_dir = P3_CASE_DIR / case["folder"]
    print(f"- {case['label']}: {case_dir.relative_to(ROOT)}")

    for target in P3_SCHEMA_FILE_MAP:
        print(f"  - schema check: {target['filename']}")

    for filename in P3_JSON_SYNTAX_ONLY_FILES:
        print(f"  - JSON syntax check: {filename}")

    print("  - README boundary text check")
    print("  - synthetic case pattern check")

print()
print("Boundary status:")
print("- helper-schema structure validation only")
print("- synthetic/sample case pattern checks only")
print("- no raw human data validation")
print("- no identifiable data validation")
print("- no clinical data validation")
print("- no Sal-Meter input validation")
print("- no CAIS compliance validation")
print("- no benchmark performance validation")
print("- no mediation effectiveness validation")
print("- no dyadic recovery validation")
print("- no termination-gate accuracy validation")
print()
print("A successful P3 helper-schema validation means only:")
print()
print("The public synthetic/sample P3 helper files follow the expected helper structure.")
print()
print("A successful P3 helper-schema validation does not mean:")
print()
print("- benchmark performance has been established")
print("- scientific truth has been established")
print("- mediation effectiveness has been established")
print("- dyadic recovery has been established in real use")
print("- termination-gate accuracy has been established")
print("- the repository is Sal-Meter")
print("- CAIS compliance has been granted")
print("- clinical, diagnostic, therapeutic, device, production, or certification status exists")
```

def print_fail(errors: list[str]) -> None:
print("FAIL: P3 helper-schema validation failed.")
print()
print("Failures:")
print()

```
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
print("- FAIL is not dyadic recovery failure")
print("- FAIL is not termination-gate accuracy failure")
```

def main() -> int:
print_header()

```
errors: list[str] = []

errors.extend(run_baseline_required_file_checks())
errors.extend(run_p3_case_required_file_checks())

if not errors:
    for target in BASELINE_TARGETS:
        errors.extend(
            validate_sample(
                label=target["label"],
                schema_path=target["schema"],
                sample_path=target["sample"],
            )
        )

    errors.extend(run_p3_case_schema_checks())
    errors.extend(run_p3_case_json_syntax_checks())
    errors.extend(run_p3_case_readme_boundary_checks())
    errors.extend(run_p3_case_pattern_checks())

if errors:
    print_fail(errors)
    return 1

print_pass()
return 0
```

if **name** == "**main**":
raise SystemExit(main())
