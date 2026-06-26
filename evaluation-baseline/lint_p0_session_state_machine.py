#!/usr/bin/env python3
"""
lint_p0_session_state_machine.py
---------------------------------
Schema hygiene + boundary lint for p0-session-infrastructure/session_state_machine.json

NOT research validation. NOT benchmark validation. NOT mediation validation.
This checks JSON structure, required states, transitions, boundary flags,
missing-data action structure, negative case files, and prohibited CLAIM patterns.

Prohibited CLAIM patterns (not words): e.g. "validated mediation" is banned,
but "not validated mediation" or "no validated mediation" is safe.

Usage:
    python evaluation-baseline/lint_p0_session_state_machine.py

Exit codes: 0 = PASS | 1 = FAIL
"""

import json
import sys
import re
from pathlib import Path

SCHEMA_FILE = Path("p0-session-infrastructure/session_state_machine.json")
NEGATIVE_CASES_DIR = Path("p0-session-infrastructure/synthetic-negative-cases")

REQUIRED_STATES = [
    "INIT", "CONSENT", "BASELINE", "AI_OUTPUT",
    "DELTA", "RECOVERY_GATE", "TERMINATION", "CLOSURE", "AUDIT"
]

REQUIRED_BOUNDARY_FLAGS = [
    "synthetic_only",
    "real_participant_data_prohibited",
    "no_human_subjects_in_this_file",
    "future_human_subject_research_requires_irb",
]

EXPECTED_NEGATIVE_CASES = {
    "missing_participant_id.json": "HALT_AND_FLAG",
    "missing_condition_id.json": "HALT_AND_FLAG",
    "missing_t1_timestamp.json": "HALT_AND_FLAG",
    "invalid_transition_recovery_to_ai_output.json": "TRANSITION_REJECTED",
    "boundary_violation_real_data_flag.json": "BOUNDARY_VIOLATION_FLAGGED",
}

# Prohibited CLAIM patterns (regex). Preceded by "not", "non-", "no " = safe.
# We match the prohibited phrase only when NOT preceded by a negation.
PROHIBITED_CLAIMS = [
    r"(?<!not )(?<!non-)(?<!no )validated mediation",
    r"mediation validated",
    r"(?<!not )(?<!non-)(?<!no )CAIS compliant",
    r"Sal-Meter ready",
    r"(?<!not )(?<!non-)(?<!no )validated benchmark",
    r"diagnostic system",
    r"therapeutic system",
    r"clinical decision",
    r"raw human data included",
    r"real participant data included",
    r"production readiness confirmed",
    r"device readiness confirmed",
]


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def check_json_valid(path):
    try:
        load(path)
        return True, "JSON syntax valid"
    except json.JSONDecodeError as e:
        return False, f"JSON parse error: {e}"


def check_required_states(schema):
    states = schema.get("states", {})
    missing = [s for s in REQUIRED_STATES if s not in states]
    if missing:
        return False, f"Missing required states: {missing}"
    return True, f"All {len(REQUIRED_STATES)} required states present"


def check_transitions(schema):
    states = schema.get("states", {})
    errors = []
    for name, defn in states.items():
        has_allowed = "transitions" in defn or "allowed_transitions" in defn
        has_forbidden = "forbidden_from" in defn or "forbidden_transitions" in defn
        if not has_allowed:
            errors.append(f"{name}: missing transitions/allowed_transitions")
        if not has_forbidden:
            errors.append(f"{name}: missing forbidden_from/forbidden_transitions")
    if errors:
        return False, "; ".join(errors)
    return True, "All states have transition definitions"


def check_boundary_flags(schema):
    flags = schema.get("boundary_flags", {})
    missing = [f for f in REQUIRED_BOUNDARY_FLAGS if f not in flags]
    false_flags = [f for f in REQUIRED_BOUNDARY_FLAGS if flags.get(f) is False]
    errors = []
    if missing:
        errors.append(f"Missing boundary flags: {missing}")
    if false_flags:
        errors.append(f"Boundary flags must be true but are false: {false_flags}")
    if errors:
        return False, " | ".join(errors)
    return True, f"All {len(REQUIRED_BOUNDARY_FLAGS)} boundary flags present and true"


def check_p0_technical_check_map(schema):
    p0 = schema.get("p0_technical_check", schema.get("p0_technical_check_map", {}))
    required_prefixes = [f"check_{i}_" for i in range(1, 8)]
    missing = [r for r in required_prefixes if not any(k.startswith(r) for k in p0)]
    if missing:
        return False, f"Missing P0 technical check entries: {missing}"
    return True, "All 7 P0 technical check entries mapped"


def check_missing_data_action(schema):
    states = schema.get("states", {})
    errors = []
    for state_name, defn in states.items():
        if "missing_data_action" in defn:
            action = defn["missing_data_action"]
            if isinstance(action, str):
                errors.append(
                    f"{state_name}.missing_data_action is a plain string '{action}' — "
                    f"must be dict with required_metadata_missing/optional_metadata_missing"
                )
            elif isinstance(action, dict):
                if "required_metadata_missing" not in action:
                    errors.append(f"{state_name}.missing_data_action missing 'required_metadata_missing'")
                elif action["required_metadata_missing"] != "HALT_AND_FLAG":
                    errors.append(
                        f"{state_name}.missing_data_action.required_metadata_missing "
                        f"= '{action['required_metadata_missing']}' (expected HALT_AND_FLAG)"
                    )
    if errors:
        return False, " | ".join(errors)
    return True, "missing_data_action structure correct (required=HALT_AND_FLAG)"


def check_negative_cases_exist():
    errors = []
    for fname in EXPECTED_NEGATIVE_CASES:
        if not (NEGATIVE_CASES_DIR / fname).exists():
            errors.append(f"Missing: {fname}")
    if errors:
        return False, "Negative case files missing: " + ", ".join(errors)
    return True, f"All {len(EXPECTED_NEGATIVE_CASES)} negative case files present"


def check_negative_case_outcomes():
    errors = []
    for fname, expected in EXPECTED_NEGATIVE_CASES.items():
        path = NEGATIVE_CASES_DIR / fname
        if not path.exists():
            continue
        try:
            data = load(path)
            meta = data.get("_fixture_meta", data)
            actual = meta.get("expected_outcome")
            if actual != expected:
                errors.append(f"{fname}: expected_outcome='{actual}' (want '{expected}')")
        except Exception as e:
            errors.append(f"{fname}: load error — {e}")
    if errors:
        return False, " | ".join(errors)
    return True, "All negative case expected_outcomes correct"


def check_prohibited_claims(schema):
    schema_str = json.dumps(schema, ensure_ascii=False)
    found = []
    for pattern in PROHIBITED_CLAIMS:
        if re.search(pattern, schema_str, re.IGNORECASE):
            found.append(pattern)
    if found:
        return False, f"Prohibited claim patterns detected: {found}"
    return True, "No prohibited claim patterns detected"


def run_all_checks():
    results = []

    valid, msg = check_json_valid(SCHEMA_FILE)
    results.append(("1. JSON syntax", valid, msg))
    if not valid:
        return results

    schema = load(SCHEMA_FILE)

    checks = [
        ("2. Required states (9)", check_required_states(schema)),
        ("3. Transition definitions", check_transitions(schema)),
        ("4. Boundary flags", check_boundary_flags(schema)),
        ("5. P0 technical check map (7)", check_p0_technical_check_map(schema)),
        ("6. missing_data_action structure", check_missing_data_action(schema)),
        ("7. Negative case files exist (5)", check_negative_cases_exist()),
        ("8. Negative case expected_outcomes", check_negative_case_outcomes()),
        ("9. Prohibited claim patterns", check_prohibited_claims(schema)),
    ]
    for name, (ok, msg) in checks:
        results.append((name, ok, msg))

    return results


def main():
    print(f"\nP0 Session State Machine Lint")
    print(f"File: {SCHEMA_FILE}")
    print(f"Negative cases: {NEGATIVE_CASES_DIR}")
    print("=" * 60)
    print("NOTE: This is schema hygiene + boundary lint only.")
    print("      Not research validation. Not benchmark validation.")
    print("=" * 60 + "\n")

    if not SCHEMA_FILE.exists():
        print(f"FAIL: Schema file not found: {SCHEMA_FILE}")
        sys.exit(1)

    results = run_all_checks()
    all_passed = True

    for name, ok, msg in results:
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}")
        if not ok:
            print(f"       -> {msg}")
            all_passed = False

    print()
    print("=" * 60)
    if all_passed:
        print("Overall: PASS")
        print("P0 session infrastructure lint clean.")
        print("(This does not validate human-subject research, mediation,")
        print(" benchmarks, Sal-Meter, or CAIS compliance.)")
        sys.exit(0)
    else:
        print("Overall: FAIL — see items above")
        sys.exit(1)


if __name__ == "__main__":
    main()
