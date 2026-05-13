#!/usr/bin/env python3
"""
SICS Human-State Proxy Benchmark Track
AI Output A/B consequence evaluator demo v0.1

This script reads one synthetic-only AI Output A/B comparison JSON file,
checks required public-boundary flags, computes placeholder synthetic
consequence scores, selects a synthetic preferred condition, and writes
a bounded demo report.

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
from typing import Any, Dict, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "evaluation-baseline" / "ai_output_ab_consequence_config.json"


def load_json(path: Path) -> Dict[str, Any]:
    """Load a JSON file as a dictionary."""
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, data: Dict[str, Any]) -> None:
    """Write a dictionary as pretty-printed JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.write("\n")


def assert_required_boundary_flags(
    comparison: Dict[str, Any],
    required_flags: Dict[str, Any],
) -> None:
    """Confirm required safety / public-boundary flags."""
    comparison_flags = comparison.get("boundary_flags", {})
    missing_or_mismatched = []

    for key, expected_value in required_flags.items():
        actual_value = comparison_flags.get(key)

        if actual_value != expected_value:
            missing_or_mismatched.append(
                {
                    "flag": key,
                    "expected": expected_value,
                    "actual": actual_value,
                }
            )

    if missing_or_mismatched:
        raise ValueError(
            "Boundary flag check failed: "
            + json.dumps(missing_or_mismatched, indent=2)
        )


def compute_synthetic_score(
    consequence_fields: Dict[str, Any],
    weights: Dict[str, float],
) -> float:
    """
    Compute a synthetic helper score.

    Default formula:
    score = (-1 * overload_delta) + recovery_delta + relational_stability_delta

    This score is not a validated psychological, clinical, therapeutic,
    counseling, mediation, or human-state metric.
    """
    overload_delta = float(consequence_fields.get("overload_delta", 0.0))
    recovery_delta = float(consequence_fields.get("recovery_delta", 0.0))
    relational_stability_delta = float(
        consequence_fields.get("relational_stability_delta", 0.0)
    )

    return (
        float(weights.get("overload_delta", -1.0)) * overload_delta
        + float(weights.get("recovery_delta", 1.0)) * recovery_delta
        + float(weights.get("relational_stability_delta", 1.0))
        * relational_stability_delta
    )


def compare_conditions(
    condition_a: Dict[str, Any],
    condition_b: Dict[str, Any],
    score_a: float,
    score_b: float,
) -> Tuple[str, str]:
    """Select a synthetic preferred condition using deterministic helper logic."""
    fields_a = condition_a.get("synthetic_consequence_fields", {})
    fields_b = condition_b.get("synthetic_consequence_fields", {})

    if score_b > score_a:
        return (
            "condition_b",
            "Condition B has a higher synthetic helper score than Condition A.",
        )

    if score_a > score_b:
        return (
            "condition_a",
            "Condition A has a higher synthetic helper score than Condition B.",
        )

    # Deterministic tie-breakers.
    overload_a = float(fields_a.get("overload_delta", 0.0))
    overload_b = float(fields_b.get("overload_delta", 0.0))

    if overload_b < overload_a:
        return (
            "condition_b",
            "Scores tied; Condition B has lower synthetic overload delta.",
        )

    if overload_a < overload_b:
        return (
            "condition_a",
            "Scores tied; Condition A has lower synthetic overload delta.",
        )

    recovery_a = float(fields_a.get("recovery_delta", 0.0))
    recovery_b = float(fields_b.get("recovery_delta", 0.0))

    if recovery_b > recovery_a:
        return (
            "condition_b",
            "Scores tied; Condition B has higher synthetic recovery delta.",
        )

    if recovery_a > recovery_b:
        return (
            "condition_a",
            "Scores tied; Condition A has higher synthetic recovery delta.",
        )

    termination_a = fields_a.get("termination_gate_status")
    termination_b = fields_b.get("termination_gate_status")

    if termination_b == "pass" and termination_a != "pass":
        return (
            "condition_b",
            "Scores tied; Condition B has pass termination gate status.",
        )

    if termination_a == "pass" and termination_b != "pass":
        return (
            "condition_a",
            "Scores tied; Condition A has pass termination gate status.",
        )

    return (
        "tie",
        "Synthetic helper scores and deterministic tie-breakers did not identify a preferred condition.",
    )


def build_demo_report(
    config: Dict[str, Any],
    comparison: Dict[str, Any],
    score_a: float,
    score_b: float,
    preferred_condition: str,
    preference_reason: str,
) -> Dict[str, Any]:
    """Build a bounded synthetic A/B consequence demo report."""
    ai_outputs = comparison.get("ai_outputs", {})
    condition_a = ai_outputs.get("condition_a", {})
    condition_b = ai_outputs.get("condition_b", {})

    fields_a = condition_a.get("synthetic_consequence_fields", {})
    fields_b = condition_b.get("synthetic_consequence_fields", {})
    quality = comparison.get("quality", {})

    return {
        "report_id": "ai_output_ab_demo_report_001",
        "evaluator_name": config.get(
            "evaluator_name", "AI Output A/B consequence evaluator"
        ),
        "evaluator_version": config.get("evaluator_version", "v0.1"),
        "track": config.get("track", "SICS Human-State Proxy Benchmark Track"),
        "repository_surface": config.get("repository_surface", "public-helper"),
        "mode": config.get("mode", "synthetic-only"),
        "comparison_id": comparison.get("comparison_id"),
        "synthetic_only": comparison.get("boundary_flags", {}).get("synthetic_only"),
        "condition_a_id": condition_a.get("output_condition_id"),
        "condition_b_id": condition_b.get("output_condition_id"),
        "overload_delta_a": fields_a.get("overload_delta"),
        "overload_delta_b": fields_b.get("overload_delta"),
        "recovery_delta_a": fields_a.get("recovery_delta"),
        "recovery_delta_b": fields_b.get("recovery_delta"),
        "relational_stability_delta_a": fields_a.get("relational_stability_delta"),
        "relational_stability_delta_b": fields_b.get("relational_stability_delta"),
        "termination_gate_status_a": fields_a.get("termination_gate_status"),
        "termination_gate_status_b": fields_b.get("termination_gate_status"),
        "synthetic_score_a": round(score_a, 6),
        "synthetic_score_b": round(score_b, 6),
        "preferred_synthetic_condition": preferred_condition,
        "preference_reason": preference_reason,
        "data_quality_flag": quality.get("data_quality_flag"),
        "raw_data_excluded": quality.get("raw_data_excluded"),
        "boundary_statement": config.get(
            "final_boundary_statement",
            "This evaluator is synthetic-only and public-helper-only. It is not validation.",
        ),
        "non_claims": {
            "not_validation": True,
            "not_benchmark_validation": True,
            "not_mediation_effectiveness_validation": True,
            "not_scientific_truth_validation": True,
            "not_sal_meter_validation": True,
            "not_cais_compliance": True,
            "not_certification": True,
            "not_device_readiness": True,
            "not_production_readiness": True,
            "not_production_closed_loop_authority": True
        }
    }


def print_terminal_summary(report: Dict[str, Any]) -> None:
    """Print the short public-helper terminal summary."""
    print("SICS Human-State Proxy Benchmark Track")
    print("AI Output A/B consequence evaluator demo v0.1")
    print()
    print(f"Synthetic-only: {str(report.get('synthetic_only')).lower()}")
    print("Real participant data: false")
    print(f"Raw human data included: {str(not report.get('raw_data_excluded')).lower()}")
    print()
    print(f"Comparison: {report.get('comparison_id')}")
    print(f"Condition A: {report.get('condition_a_id')}")
    print(f"Condition B: {report.get('condition_b_id')}")
    print()
    print(f"Synthetic score A: {report.get('synthetic_score_a')}")
    print(f"Synthetic score B: {report.get('synthetic_score_b')}")
    print(f"Preferred synthetic condition: {report.get('preferred_synthetic_condition')}")
    print(f"Reason: {report.get('preference_reason')}")
    print(f"Termination gate A: {report.get('termination_gate_status_a')}")
    print(f"Termination gate B: {report.get('termination_gate_status_b')}")
    print()
    print("This evaluator is public-helper-only.")
    print("It is not validation.")


def main() -> int:
    """Run the v0.1 synthetic-only AI Output A/B consequence evaluator."""
    try:
        config = load_json(CONFIG_PATH)

        input_file = REPO_ROOT / config["input_file"]
        output_report_file = REPO_ROOT / config["output_report_file"]

        comparison = load_json(input_file)

        assert_required_boundary_flags(
            comparison=comparison,
            required_flags=config.get("required_boundary_flags", {}),
        )

        ai_outputs = comparison.get("ai_outputs", {})
        condition_a = ai_outputs.get("condition_a", {})
        condition_b = ai_outputs.get("condition_b", {})

        fields_a = condition_a.get("synthetic_consequence_fields", {})
        fields_b = condition_b.get("synthetic_consequence_fields", {})

        weights = config.get("scoring_rule", {}).get("weights", {})

        score_a = compute_synthetic_score(fields_a, weights)
        score_b = compute_synthetic_score(fields_b, weights)

        preferred_condition, preference_reason = compare_conditions(
            condition_a=condition_a,
            condition_b=condition_b,
            score_a=score_a,
            score_b=score_b,
        )

        report = build_demo_report(
            config=config,
            comparison=comparison,
            score_a=score_a,
            score_b=score_b,
            preferred_condition=preferred_condition,
            preference_reason=preference_reason,
        )

        write_json(output_report_file, report)

        if config.get("terminal_summary", {}).get("print_header", True):
            print_terminal_summary(report)

        print()
        print(f"Demo report written to: {output_report_file.relative_to(REPO_ROOT)}")

        return 0

    except Exception as error:
        print("AI Output A/B consequence evaluator demo failed.", file=sys.stderr)
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
