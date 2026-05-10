#!/usr/bin/env python3
"""
SICS Human-State Proxy Benchmark Track
P4-3 Synthetic Termination Gate Accuracy Skeleton v0.1

This evaluator checks synthetic termination-gate helper logic only.

It does not validate benchmark performance.
It does not validate scientific truth.
It does not validate mediation effectiveness.
It does not validate Sal-Meter.
It does not grant CAIS compliance.
It does not validate human-state measurement.
It does not process raw human data.
It does not process identifiable human data.
It does not process clinical data.
It does not create clinical, diagnostic, therapeutic, counseling, surveillance,
certification, device-readiness, production-readiness, relationship-verdict,
or human-ranking authority.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = REPO_ROOT / "sample-data" / "synthetic-dyadic-session-001" / "termination_gate_cases.json"

REQUIRED_BOUNDARY_FALSE_FLAGS = [
    "raw_human_data_present",
    "identifiable_data_present",
    "clinical_data_present",
    "sal_meter_input_present",
    "cais_compliance_claim_present",
    "benchmark_validation_claim_present",
    "mediation_validation_claim_present",
    "production_intervention_claim_present",
    "human_ranking_claim_present",
    "relationship_verdict_present",
]

REQUIRED_FINAL_TRUE_FLAGS = [
    "synthetic_helper_case_set_only",
    "not_benchmark_evidence",
    "not_scientific_validation",
    "not_mediation_validation",
    "not_sal_meter_validation",
    "not_cais_compliance",
    "not_clinical",
    "not_diagnostic",
    "not_therapeutic",
    "not_production_ready",
    "not_certification",
    "not_human_ranking",
    "not_relationship_verdict",
]

REQUIRED_DECISIONS = {
    "pause_session",
    "narrow_scope",
    "close_session",
    "terminate_session",
    "audit_only",
}

EXPECTED_CASES = {
    "tg_case_001_consent_withdrawn": {
        "expected_decision": "terminate_session",
        "expected_reason": "consent_withdrawn",
        "must_not_continue": True,
        "must_not_declare_recovery": True,
        "must_close": True,
    },
    "tg_case_002_permission_expired": {
        "expected_decision": "request_consent_refresh",
        "expected_reason": "permission_expired",
        "must_not_continue": True,
        "must_not_declare_recovery": True,
    },
    "tg_case_003_low_confidence": {
        "expected_decision": "pause_session",
        "expected_reason": "low_confidence_high_uncertainty",
        "must_not_continue": True,
        "must_not_declare_recovery": True,
    },
    "tg_case_004_insufficient_data_quality": {
        "expected_decision": "request_packet_refresh",
        "expected_reason": "insufficient_data_quality",
        "must_not_continue": True,
        "must_not_declare_recovery": True,
    },
    "tg_case_006_private_state_exposure_risk": {
        "expected_decision": "pause_session",
        "expected_reason": "private_state_exposure_risk",
        "must_not_continue": True,
        "must_not_declare_recovery": True,
    },
    "tg_case_009_session_already_closed": {
        "expected_decision": "audit_only",
        "expected_reason": "closed_session_must_stay_closed",
        "must_not_continue": True,
        "must_not_declare_recovery": True,
        "must_close": True,
        "shared_output_disallowed": True,
    },
    "tg_case_011_one_sided_improvement": {
        "expected_decision": "pause_session",
        "expected_reason": "one_sided_improvement_not_dyadic_recovery",
        "must_not_continue": True,
        "must_not_declare_recovery": True,
    },
    "tg_case_012_recovery_gate_not_passed": {
        "expected_decision": "pause_session",
        "expected_reason": "recovery_gate_not_passed",
        "must_not_continue": True,
        "must_not_declare_recovery": True,
    },
}


class ValidationFailure(Exception):
    """Raised when the synthetic termination gate helper package fails validation."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ValidationFailure(f"Missing required file: {path.relative_to(REPO_ROOT)}")

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        raise ValidationFailure(f"Invalid JSON in {path.relative_to(REPO_ROOT)}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValidationFailure("termination_gate_cases.json must contain a JSON object at top level.")

    return data


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationFailure(message)


def validate_boundary_flags(data: dict[str, Any]) -> None:
    boundary_flags = data.get("boundary_flags")
    require(isinstance(boundary_flags, dict), "Missing or invalid boundary_flags object.")

    for flag in REQUIRED_BOUNDARY_FALSE_FLAGS:
        require(
            boundary_flags.get(flag) is False,
            f"Boundary flag must be false: boundary_flags.{flag}",
        )

    final_boundary_status = data.get("final_boundary_status")
    require(isinstance(final_boundary_status, dict), "Missing or invalid final_boundary_status object.")

    for flag in REQUIRED_FINAL_TRUE_FLAGS:
        require(
            final_boundary_status.get(flag) is True,
            f"Final boundary status must be true: final_boundary_status.{flag}",
        )


def validate_package_metadata(data: dict[str, Any]) -> None:
    require(data.get("package_id") == "sics_p4_3_synthetic_termination_gate_cases_v0_1", "Unexpected package_id.")
    require(data.get("package_version") == "0.1", "Unexpected package_version.")
    require(data.get("milestone") == "P4-3", "Unexpected milestone.")
    require(data.get("dataset_type") == "synthetic", "dataset_type must be synthetic.")
    require(data.get("synthetic_status") == "synthetic_only", "synthetic_status must be synthetic_only.")
    require(data.get("sample_scope") == "public_helper_only", "sample_scope must be public_helper_only.")

    boundary_status = data.get("boundary_status")
    require(isinstance(boundary_status, dict), "Missing or invalid boundary_status object.")

    required_true = [
        "research_stage",
        "public_helper_only",
        "synthetic_only",
        "non_clinical",
        "non_diagnostic",
        "non_therapeutic",
        "non_counseling",
        "non_surveillance",
        "non_certification",
        "non_human_ranking",
        "not_sal_meter",
        "not_cais_compliance",
        "not_benchmark_validation",
        "not_mediation_validation",
        "not_production_closed_loop",
    ]

    for key in required_true:
        require(boundary_status.get(key) is True, f"boundary_status.{key} must be true.")


def validate_cases(data: dict[str, Any]) -> dict[str, Any]:
    cases = data.get("termination_gate_cases")
    require(isinstance(cases, list), "termination_gate_cases must be a list.")
    require(len(cases) == 12, "termination_gate_cases must contain exactly 12 synthetic cases.")

    allowed_decisions = data.get("allowed_expected_decisions")
    require(isinstance(allowed_decisions, list), "allowed_expected_decisions must be a list.")
    allowed_decisions_set = set(allowed_decisions)

    case_by_id: dict[str, dict[str, Any]] = {}

    for case in cases:
        require(isinstance(case, dict), "Each termination gate case must be an object.")

        case_id = case.get("case_id")
        require(isinstance(case_id, str) and case_id, "Each case must have a non-empty case_id.")
        require(case_id not in case_by_id, f"Duplicate case_id detected: {case_id}")

        trigger_type = case.get("trigger_type")
        require(isinstance(trigger_type, str) and trigger_type, f"{case_id}: trigger_type is required.")

        input_state = case.get("input_state")
        require(isinstance(input_state, dict), f"{case_id}: input_state must be an object.")

        expected_decision = case.get("expected_decision")
        require(
            expected_decision in allowed_decisions_set,
            f"{case_id}: expected_decision is not in allowed_expected_decisions.",
        )

        expected_reason = case.get("expected_reason")
        require(isinstance(expected_reason, str) and expected_reason, f"{case_id}: expected_reason is required.")

        expected_boundary = case.get("expected_boundary")
        require(isinstance(expected_boundary, dict), f"{case_id}: expected_boundary must be an object.")

        require(
            expected_boundary.get("recovery_declaration_allowed") is False,
            f"{case_id}: recovery_declaration_allowed must be false.",
        )
        require(
            expected_boundary.get("audit_log_required") is True,
            f"{case_id}: audit_log_required must be true.",
        )

        case_by_id[case_id] = case

    for case_id, expected in EXPECTED_CASES.items():
        require(case_id in case_by_id, f"Missing expected synthetic case: {case_id}")
        case = case_by_id[case_id]
        boundary = case["expected_boundary"]

        require(
            case.get("expected_decision") == expected["expected_decision"],
            f"{case_id}: expected_decision should be {expected['expected_decision']}.",
        )
        require(
            case.get("expected_reason") == expected["expected_reason"],
            f"{case_id}: expected_reason should be {expected['expected_reason']}.",
        )

        if expected.get("must_not_continue"):
            require(
                boundary.get("continue_mediation_allowed") is False,
                f"{case_id}: continue_mediation_allowed must be false.",
            )

        if expected.get("must_not_declare_recovery"):
            require(
                boundary.get("recovery_declaration_allowed") is False,
                f"{case_id}: recovery_declaration_allowed must be false.",
            )

        if expected.get("must_close"):
            require(
                boundary.get("session_must_close") is True,
                f"{case_id}: session_must_close must be true.",
            )

        if expected.get("shared_output_disallowed"):
            require(
                boundary.get("shared_mediation_output_allowed") is False,
                f"{case_id}: shared_mediation_output_allowed must be false.",
            )

    decisions_present = {case.get("expected_decision") for case in cases}
    missing_decisions = REQUIRED_DECISIONS - decisions_present
    require(
        not missing_decisions,
        f"Missing required expected decisions: {', '.join(sorted(missing_decisions))}",
    )

    return {
        "total_cases": len(cases),
        "decisions_present": sorted(decisions_present),
        "case_ids": sorted(case_by_id.keys()),
    }


def validate_expected_summary(data: dict[str, Any]) -> None:
    summary = data.get("expected_summary")
    require(isinstance(summary, dict), "Missing or invalid expected_summary object.")

    require(summary.get("total_cases") == 12, "expected_summary.total_cases must be 12.")
    require(summary.get("must_include_pause") is True, "expected_summary.must_include_pause must be true.")
    require(summary.get("must_include_narrow_scope") is True, "expected_summary.must_include_narrow_scope must be true.")
    require(summary.get("must_include_close") is True, "expected_summary.must_include_close must be true.")
    require(summary.get("must_include_terminate") is True, "expected_summary.must_include_terminate must be true.")
    require(summary.get("must_include_audit_only") is True, "expected_summary.must_include_audit_only must be true.")
    require(
        summary.get("closed_session_must_stay_closed") is True,
        "expected_summary.closed_session_must_stay_closed must be true.",
    )
    require(
        summary.get("expired_permission_cannot_continue_ordinary_mediation") is True,
        "expected_summary.expired_permission_cannot_continue_ordinary_mediation must be true.",
    )
    require(
        summary.get("low_confidence_blocks_recovery_declaration") is True,
        "expected_summary.low_confidence_blocks_recovery_declaration must be true.",
    )
    require(
        summary.get("insufficient_data_quality_blocks_recovery_declaration") is True,
        "expected_summary.insufficient_data_quality_blocks_recovery_declaration must be true.",
    )
    require(
        summary.get("private_state_exposure_risk_triggers_pause_or_closure") is True,
        "expected_summary.private_state_exposure_risk_triggers_pause_or_closure must be true.",
    )
    require(
        summary.get("one_sided_improvement_is_not_dyadic_recovery") is True,
        "expected_summary.one_sided_improvement_is_not_dyadic_recovery must be true.",
    )


def print_success(case_summary: dict[str, Any]) -> None:
    print("SICS Human-State Proxy Benchmark Track")
    print("P4-3 Synthetic Termination Gate Accuracy Skeleton v0.1")
    print()
    print("This evaluator checks synthetic termination-gate helper logic only.")
    print()
    print("It does not validate benchmark performance.")
    print("It does not validate scientific truth.")
    print("It does not validate mediation effectiveness.")
    print("It does not validate Sal-Meter.")
    print("It does not grant CAIS compliance.")
    print("It does not validate human-state measurement.")
    print("It does not process raw human data.")
    print("It does not process identifiable human data.")
    print("It does not process clinical data.")
    print()
    print("PASS: synthetic termination-gate helper cases evaluated successfully.")
    print()
    print("Synthetic termination gate result:")
    print(f"- total cases: {case_summary['total_cases']}")
    print("- expected decisions present:")
    for decision in case_summary["decisions_present"]:
        print(f"  - {decision}")
    print("- closed session stays closed: true")
    print("- expired permission blocks ordinary continuation: true")
    print("- low confidence blocks recovery declaration: true")
    print("- insufficient data quality blocks recovery declaration: true")
    print("- private-state exposure risk triggers pause or closure: true")
    print("- one-sided improvement is not dyadic recovery: true")
    print("- public boundary: preserved")


def main() -> int:
    try:
        data = load_json(CASES_PATH)
        validate_package_metadata(data)
        validate_boundary_flags(data)
        case_summary = validate_cases(data)
        validate_expected_summary(data)
        print_success(case_summary)
        return 0
    except ValidationFailure as exc:
        print("SICS Human-State Proxy Benchmark Track")
        print("P4-3 Synthetic Termination Gate Accuracy Skeleton v0.1")
        print()
        print("FAIL: synthetic termination-gate helper evaluation failed.")
        print()
        print(str(exc))
        print()
        print("This is a structure or boundary mismatch.")
        print("It is not scientific failure.")
        print("It is not benchmark failure.")
        print("It is not mediation failure.")
        print("It is not Sal-Meter failure.")
        print("It is not CAIS compliance failure.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
