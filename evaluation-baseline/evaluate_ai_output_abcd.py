#!/usr/bin/env python3
"""
SICS Human-State Proxy Benchmark Track
AI Output A/B/C/D consequence evaluator v0.3

This script reads the canonical synthetic P2 AI Output A/B/C/D package:

  sample-data/p2-ai-output-abcd/

It checks required public-helper files, verifies boundary flags, extracts
proxy-only consequence fields, ranks the four synthetic conditions, computes a
synthetic C-trap flag, compares the synthetic expected evaluator output, writes a
bounded helper report, and prints a terminal summary.

It is aligned to docs/pilot-design/proxy-benchmark-pilot-design-v1.1.md (section 5)
and is a parallel helper to evaluate_ai_output_ab.py; it leaves the older A/B
evaluator and its package untouched.

This is public-helper-only.

It is not validation.
It is not clinical.
It is not diagnostic.
It is not therapeutic.
It is not counseling.
It is not surveillance.
It is not mediation effectiveness validation.
It is not benchmark validation.
It is not scientific truth validation.
It is not Sal-Meter.
It is not CAIS compliance.
It is not certification.
It is not device readiness.
It is not production readiness.
It is not production authority.

A synthetic score must not be converted into a real human judgment.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = (
    REPO_ROOT
    / "evaluation-baseline"
    / "ai_output_abcd_consequence_config.json"
)


RISK_ORDER = {
    "low": 0,
    "low_medium": 0.5,
    "medium": 1,
    "medium_high": 1.5,
    "high": 2,
    "unknown": 1,
    "unresolved": 1
}

TERMINATION_ORDER = {
    "continue": 0,
    "hold": 0,
    "narrow": 1,
    "pause": 1,
    "close": 2,
    "audit_only": 2,
    "terminate": 2,
    "refresh_packet": 1
}


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.write("\n")


def assert_required_files(package_dir: Path, required_files: List[str]) -> List[str]:
    missing = []

    for filename in required_files:
        path = package_dir / filename
        if not path.exists():
            missing.append(filename)

    if missing:
        raise FileNotFoundError(
            "P2 A/B/C/D package missing required files: " + ", ".join(missing)
        )

    return required_files


def assert_boundary_flags(filename: str, data: Dict[str, Any]) -> None:
    flags = data.get("boundary_flags", {})

    required_true = {
        "synthetic_only": True,
        "public_helper_only": True
    }

    required_false = {
        "real_participant_data": False,
        "raw_human_data_included": False,
        "real_conversation_included": False,
        "real_phone_recording_included": False,
        "real_call_transcript_included": False,
        "real_session_log_included": False,
        "clinical_data_included": False,
        "diagnostic_data_included": False,
        "therapeutic_data_included": False,
        "counseling_data_included": False,
        "surveillance_data_included": False,
        "sal_meter_raw_input_included": False,
        "cais_trace_data_included": False,
        "production_intervention_log_included": False
    }

    errors = []

    for key, expected in required_true.items():
        actual = flags.get(key)
        if actual is not expected:
            errors.append(
                {
                    "file": filename,
                    "flag": key,
                    "expected": expected,
                    "actual": actual
                }
            )

    for key, expected in required_false.items():
        actual = flags.get(key)
        if actual is not expected:
            errors.append(
                {
                    "file": filename,
                    "flag": key,
                    "expected": expected,
                    "actual": actual
                }
            )

    if errors:
        raise ValueError(
            "Boundary flag check failed: "
            + json.dumps(errors, indent=2, ensure_ascii=False)
        )


def load_package(config: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    package_dir = REPO_ROOT / config["input_package_dir"]
    required_files = config["required_files"]

    assert_required_files(package_dir, required_files)

    loaded = {}

    for filename in required_files:
        path = package_dir / filename

        if filename.endswith(".json"):
            loaded[filename] = load_json(path)

    for filename, data in loaded.items():
        assert_boundary_flags(filename, data)

    return loaded


def extract_condition_metrics(
    package_data: Dict[str, Dict[str, Any]],
    condition_files: Dict[str, str]
) -> Dict[str, Dict[str, Any]]:
    metrics = {}

    for condition_id, filename in condition_files.items():
        data = package_data[filename]
        fields = data.get("proxy_only_consequence_fields")

        if not isinstance(fields, dict):
            raise ValueError(
                f"{filename} does not contain proxy_only_consequence_fields"
            )

        metrics[condition_id] = fields

    return metrics


def assert_allowed_fields_only(
    metrics: Dict[str, Dict[str, Any]],
    allowed_fields: List[str]
) -> None:
    allowed = set(allowed_fields)
    errors = []

    for condition_id, fields in metrics.items():
        field_set = set(fields.keys())

        extra = sorted(field_set - allowed)
        missing = sorted(allowed - field_set)

        if extra or missing:
            errors.append(
                {
                    "condition": condition_id,
                    "extra_fields": extra,
                    "missing_fields": missing
                }
            )

    if errors:
        raise ValueError(
            "Proxy-only field check failed: "
            + json.dumps(errors, indent=2, ensure_ascii=False)
        )


def assert_no_prohibited_output_fields(
    metrics: Dict[str, Dict[str, Any]],
    prohibited_fields: List[str]
) -> None:
    prohibited = set(prohibited_fields)
    violations = []

    for condition_id, fields in metrics.items():
        for key in fields.keys():
            if key in prohibited:
                violations.append(
                    {
                        "condition": condition_id,
                        "prohibited_field": key
                    }
                )

    if violations:
        raise ValueError(
            "Prohibited output field detected: "
            + json.dumps(violations, indent=2, ensure_ascii=False)
        )


def numeric(value: Any) -> float:
    return float(value)


def risk_penalty(value: Any) -> float:
    return float(RISK_ORDER.get(str(value), 1))


def termination_score(value: Any) -> float:
    return float(TERMINATION_ORDER.get(str(value), 0))


def compute_condition_score(fields: Dict[str, Any]) -> float:
    """
    Synthetic helper score.

    Higher is better.

    This is not a validated psychological, clinical, therapeutic,
    counseling, mediation, dyadic-recovery, or human-state metric.
    """
    overload_component = -1.0 * numeric(fields.get("overload_delta", 0.0))
    recovery_component = numeric(fields.get("recovery_burden_delta", 0.0))
    stability_component = numeric(fields.get("relational_stability_delta", 0.0))
    asymmetry_component = -0.2 * risk_penalty(fields.get("asymmetry_risk"))
    false_recovery_component = -0.2 * risk_penalty(
        fields.get("false_recovery_risk")
    )
    termination_component = 0.1 * termination_score(
        fields.get("termination_readiness")
    )

    return (
        overload_component
        + recovery_component
        + stability_component
        + asymmetry_component
        + false_recovery_component
        + termination_component
    )


def build_code_to_id(
    package_data: Dict[str, Dict[str, Any]],
    condition_files: Dict[str, str]
) -> Dict[str, str]:
    """
    Map each condition code (A/B/C/D) to its canonical condition_id, read from
    each condition file's own `condition_id` field. Falls back to the file stem.
    """
    code_to_id = {}

    for code, filename in condition_files.items():
        data = package_data.get(filename, {})
        condition_id = data.get("condition_id") or filename.replace(".json", "")
        code_to_id[code] = condition_id

    return code_to_id


def rank_conditions(
    metrics: Dict[str, Dict[str, Any]],
    code_to_id: Dict[str, str]
) -> Tuple[List[Dict[str, Any]], str, str]:
    ranked = []

    for condition_code, fields in metrics.items():
        score = compute_condition_score(fields)
        ranked.append(
            {
                "condition_code": condition_code,
                "condition_id": code_to_id.get(condition_code, condition_code),
                "synthetic_helper_score": round(score, 6),
                "metrics": fields
            }
        )

    ranked.sort(
        key=lambda item: item["synthetic_helper_score"],
        reverse=True
    )

    preferred = ranked[0]["condition_id"] if ranked else "unresolved"
    lowest = ranked[-1]["condition_id"] if ranked else "unresolved"

    return ranked, preferred, lowest


def detect_c_trap(
    metrics: Dict[str, Dict[str, Any]],
    code_to_id: Dict[str, str]
) -> Tuple[bool, List[str]]:
    """
    Synthetic C-trap detector (Finding 2).

    A condition is a synthetic 'C trap' when its SURFACE metrics look mild or
    non-deteriorating (overload not worsening, relational stability not worsening)
    while its false_recovery_risk is HIGH. This encodes 'feels good != improves
    state' for regression checking only. An openly deteriorating condition
    (e.g. high overload, falling stability) is NOT a trap because its surface is
    not reassuring.

    This is not a validated psychological, clinical, mediation, or human-state
    metric.
    """
    trapped: List[str] = []

    for condition_code, fields in metrics.items():
        false_recovery_high = str(fields.get("false_recovery_risk")) == "high"
        surface_not_worse = (
            numeric(fields.get("overload_delta", 0.0)) <= 0.0
            and numeric(fields.get("relational_stability_delta", 0.0)) >= 0.0
        )

        if false_recovery_high and surface_not_worse:
            trapped.append(code_to_id.get(condition_code, condition_code))

    return (len(trapped) > 0), trapped


def compare_expected(
    metrics: Dict[str, Dict[str, Any]],
    preferred_condition: str,
    lowest_condition: str,
    c_trap_flag: bool,
    expected: Dict[str, Any]
) -> Tuple[str, List[str]]:
    messages = []

    expected_metrics = expected.get("expected_proxy_only_metrics", {})
    expected_result = expected.get("expected_comparison_result", {})
    expected_preferred = expected_result.get("preferred_synthetic_condition")
    expected_lowest = expected_result.get("lowest_position")
    expected_c_trap = expected_result.get("c_trap_flag")

    for condition_id, expected_fields in expected_metrics.items():
        actual_fields = metrics.get(condition_id)

        if actual_fields is None:
            messages.append(f"Missing actual metrics for {condition_id}")
            continue

        for field_name, expected_value in expected_fields.items():
            actual_value = actual_fields.get(field_name)

            if actual_value != expected_value:
                messages.append(
                    f"{condition_id}.{field_name} expected "
                    f"{expected_value!r}, got {actual_value!r}"
                )

    if preferred_condition != expected_preferred:
        messages.append(
            f"Preferred condition expected {expected_preferred!r}, "
            f"got {preferred_condition!r}"
        )

    if expected_lowest is not None and lowest_condition != expected_lowest:
        messages.append(
            f"Lowest condition expected {expected_lowest!r}, "
            f"got {lowest_condition!r}"
        )

    if expected_c_trap is not None and c_trap_flag != expected_c_trap:
        messages.append(
            f"C-trap flag expected {expected_c_trap!r}, got {c_trap_flag!r}"
        )

    if messages:
        return "REVISE", messages

    return "PASS", ["Expected synthetic helper output matched."]


def build_report(
    config: Dict[str, Any],
    metrics: Dict[str, Dict[str, Any]],
    ranked: List[Dict[str, Any]],
    preferred_condition: str,
    lowest_condition: str,
    c_trap_flag: bool,
    c_trap_conditions: List[str],
    helper_result: str,
    result_messages: List[str],
    expected: Dict[str, Any]
) -> Dict[str, Any]:
    return {
        "report_id": "p2_ai_output_abcd_evaluator_result",
        "evaluator_name": config.get("evaluator_name"),
        "evaluator_version": config.get("evaluator_version"),
        "track": config.get("track"),
        "repository_surface": config.get("repository_surface"),
        "mode": config.get("mode"),
        "input_package_dir": config.get("input_package_dir"),
        "helper_result": helper_result,
        "preferred_synthetic_condition": preferred_condition,
        "lowest_synthetic_condition": lowest_condition,
        "c_trap_flag": c_trap_flag,
        "c_trap_conditions": c_trap_conditions,
        "ranked_conditions": ranked,
        "proxy_only_metrics": metrics,
        "expected_preferred_synthetic_condition": expected
        .get("expected_comparison_result", {})
        .get("preferred_synthetic_condition"),
        "expected_lowest_position": expected
        .get("expected_comparison_result", {})
        .get("lowest_position"),
        "expected_c_trap_flag": expected
        .get("expected_comparison_result", {})
        .get("c_trap_flag"),
        "result_messages": result_messages,
        "allowed_proxy_only_fields": config.get("allowed_proxy_only_fields"),
        "non_claims": {
            "not_validation": True,
            "not_real_ai_impact_validation": True,
            "not_real_human_state_measurement": True,
            "not_benchmark_validation": True,
            "not_mediation_validation": True,
            "not_dyadic_recovery_validation": True,
            "not_termination_gate_accuracy_validation": True,
            "not_sal_meter": True,
            "not_cais_compliance": True,
            "not_certification": True,
            "not_device_readiness": True,
            "not_production_readiness": True,
            "not_production_authority": True
        },
        "boundary_statement": (
            "This evaluator reads a synthetic public-helper P2 AI Output "
            "A/B/C/D package and compares proxy-only helper metrics. It does "
            "not create evidence, validation, certification, Sal-Meter status, "
            "CAIS compliance, mediation authority, phone monitoring authority, "
            "replay validation authority, production authority, relationship "
            "verdicts, or human-ranking authority."
        )
    }


def print_terminal_summary(report: Dict[str, Any]) -> None:
    print("SICS Human-State Proxy Benchmark Track")
    print("AI Output A/B/C/D consequence evaluator v0.3")
    print()
    print(f"Input package: {report.get('input_package_dir')}")
    print(f"Helper result: {report.get('helper_result')}")
    print(
        "Preferred synthetic condition: "
        f"{report.get('preferred_synthetic_condition')}"
    )
    print(
        "Lowest synthetic condition: "
        f"{report.get('lowest_synthetic_condition')}"
    )
    print(
        "C-trap flag: "
        f"{report.get('c_trap_flag')} "
        f"(conditions: {report.get('c_trap_conditions')})"
    )
    print()
    print("Ranked conditions:")

    for item in report.get("ranked_conditions", []):
        print(
            "- "
            + item["condition_id"]
            + f" | synthetic_helper_score={item['synthetic_helper_score']}"
        )

    print()
    print("This evaluator is public-helper-only.")
    print("It is synthetic-only.")
    print("It is not validation.")
    print("It is not Sal-Meter.")
    print("It is not CAIS compliance.")
    print("It is not production readiness.")


def main() -> int:
    try:
        config = load_json(CONFIG_PATH)

        package_data = load_package(config)

        condition_files = config["condition_files"]
        expected_output_file = config["expected_output_file"]
        allowed_fields = config["allowed_proxy_only_fields"]
        prohibited_fields = config.get("prohibited_output_fields", [])

        metrics = extract_condition_metrics(
            package_data=package_data,
            condition_files=condition_files
        )

        assert_allowed_fields_only(metrics, allowed_fields)
        assert_no_prohibited_output_fields(metrics, prohibited_fields)

        expected = package_data[expected_output_file]

        code_to_id = build_code_to_id(package_data, condition_files)

        ranked, preferred_condition, lowest_condition = rank_conditions(
            metrics, code_to_id
        )

        c_trap_flag, c_trap_conditions = detect_c_trap(metrics, code_to_id)

        helper_result, result_messages = compare_expected(
            metrics=metrics,
            preferred_condition=preferred_condition,
            lowest_condition=lowest_condition,
            c_trap_flag=c_trap_flag,
            expected=expected
        )

        report = build_report(
            config=config,
            metrics=metrics,
            ranked=ranked,
            preferred_condition=preferred_condition,
            lowest_condition=lowest_condition,
            c_trap_flag=c_trap_flag,
            c_trap_conditions=c_trap_conditions,
            helper_result=helper_result,
            result_messages=result_messages,
            expected=expected
        )

        output_report_file = REPO_ROOT / config["output_report_file"]
        write_json(output_report_file, report)

        print_terminal_summary(report)
        print()
        print(f"Report written to: {output_report_file.relative_to(REPO_ROOT)}")

        if helper_result != "PASS":
            return 1

        return 0

    except Exception as error:
        failure_report = {
            "report_id": "p2_ai_output_abcd_evaluator_result",
            "helper_result": "FAIL",
            "error": str(error),
            "boundary_statement": (
                "Failure indicates helper-structure or regression inconsistency "
                "only. It does not create evidence, validation, certification, "
                "Sal-Meter status, CAIS compliance, device readiness, or "
                "production readiness."
            )
        }

        try:
            config = load_json(CONFIG_PATH)
            output_report_file = REPO_ROOT / config.get(
                "output_report_file",
                "evaluation-baseline/demo_output/"
                "p2_ai_output_abcd_evaluator_result.json"
            )
            write_json(output_report_file, failure_report)
        except Exception:
            pass

        print("AI Output A/B/C/D consequence evaluator failed.", file=sys.stderr)
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
