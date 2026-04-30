#!/usr/bin/env python3
"""
Local Feedback Demo Placeholder

SICS Human-State Proxy Benchmark Track
Closed-Loop Demo-Lite

This script is a local, non-production, synthetic/sample-only placeholder.

It does not collect human data.
It does not connect to sensors.
It does not connect to cameras.
It does not connect to microphones.
It does not process biosignals.
It does not monitor users.
It does not diagnose.
It does not treat.
It does not intervene.
It does not rank people.
It does not validate Sal-Meter.
It does not grant CAIS compliance.
It does not validate benchmark performance.

It only demonstrates the shape of a bounded feedback event log.
"""

from __future__ import annotations

import json
import sys
from typing import Any


TRACK = "SICS Human-State Proxy Benchmark Track"
REPOSITORY = "salpida-foundation/proxy-benchmark-track"
FOLDER = "closed-loop-demo-lite"

BOUNDARY_NOTICE = (
    "Research-stage proxy benchmark helper demo. "
    "Synthetic/sample data only. "
    "Local placeholder only. "
    "Non-production. "
    "Not diagnostic. "
    "Not clinical. "
    "Not therapeutic. "
    "Not surveillance. "
    "Not certification. "
    "Not Sal-Meter. "
    "Not CAIS compliance. "
    "Not human ranking. "
    "No live intervention. "
    "No real-person automation."
)

FINAL_RULE = (
    "The event log may preserve structure. "
    "It must not become evidence, diagnosis, therapy, surveillance, "
    "certification, Sal-Meter validation, CAIS compliance, or human ranking."
)


FALSE_LOG_BOUNDARY_FLAGS = [
    "raw_human_data_present",
    "identifiable_data_present",
    "clinical_data_present",
    "private_user_data_present",
    "sal_meter_input_present",
    "cais_compliance_claim_present",
    "benchmark_validation_claim_present",
    "diagnostic_claim_present",
    "clinical_claim_present",
    "therapeutic_claim_present",
    "surveillance_claim_present",
    "certification_claim_present",
    "employment_claim_present",
    "insurance_claim_present",
    "educational_claim_present",
    "legal_claim_present",
    "eligibility_claim_present",
    "human_ranking_claim_present",
    "person_scoring_claim_present",
    "live_intervention_present",
    "production_automation_present",
]

FALSE_EVENT_BOUNDARY_FLAGS = [
    "raw_human_data_present",
    "identifiable_data_present",
    "clinical_data_present",
    "private_user_data_present",
    "diagnosis_present",
    "therapy_instruction_present",
    "surveillance_score_present",
    "person_score_present",
    "human_ranking_present",
    "sal_meter_input_present",
    "sal_meter_validation_claim_present",
    "cais_compliance_claim_present",
    "benchmark_validation_claim_present",
    "live_intervention_present",
    "production_automation_present",
]


def make_false_flags(flag_names: list[str]) -> dict[str, bool]:
    """Create a dictionary where every prohibited boundary flag is false."""
    return {name: False for name in flag_names}


def build_feedback_event() -> dict[str, Any]:
    """
    Build one synthetic/sample feedback event.

    This is not a real user event.
    This is not a clinical event.
    This is not a Sal-Meter event.
    This is not a CAIS compliance event.
    """

    return {
        "event_id": "SYN-FEEDBACK-EVENT-001",
        "session_id": "SYN-SESSION-001",
        "synthetic_timestamp": "2026-04-30T00:00:01Z",
        "event_type": "synthetic_ai_output_event",
        "source_module": "local_feedback_demo_placeholder",
        "input_status": "synthetic_sample_only",
        "output_status": "structure_only",
        "review_state": "boundary_review_required",
        "boundary_status": "boundary_preserved",
        "synthetic_proxy_field_reference": [
            "synthetic_human_state_cost_proxy",
            "metadata_completeness_status",
            "timestamp_sync_status",
            "leakage_review_status",
            "qc_status"
        ],
        "placeholder_feedback_action": "require_human_review",
        "placeholder_policy_name": "boundary_review_policy",
        "human_review_status": "required_before_interpretation",
        "sal_meter_input_status": "not_present",
        "cais_compliance_status": "not_granted",
        "benchmark_validation_status": "not_validated",
        "future_sal_meter_ab_status": "not_active",
        "future_dyadic_mediation_status": "not_active",
        "operator_note": (
            "Synthetic/sample event only. "
            "No real human data, no diagnosis, no therapy, no surveillance, "
            "no Sal-Meter input, and no CAIS compliance."
        ),
        "audit_note": (
            "This event demonstrates a bounded local feedback event-log "
            "structure only."
        ),
        "event_boundary_flags": make_false_flags(FALSE_EVENT_BOUNDARY_FLAGS)
    }


def build_feedback_log() -> dict[str, Any]:
    """
    Build a synthetic/sample feedback event log.

    The output is intended to match:
    closed-loop-demo-lite/feedback_event_log_schema.json
    """

    return {
        "schema_name": "feedback_event_log_schema",
        "schema_version": "0.1.0",
        "track": TRACK,
        "repository": REPOSITORY,
        "folder": FOLDER,
        "data_status": "synthetic",
        "authority_status": "public-helper-structure-only",
        "boundary_notice": BOUNDARY_NOTICE,
        "log_metadata": {
            "log_id": "SYN-FEEDBACK-LOG-001",
            "session_id": "SYN-SESSION-001",
            "created_at": "2026-04-30T00:00:00Z",
            "created_by": "local_placeholder_script",
            "environment": "local",
            "execution_mode": "local_demo_lite",
            "production_status": "non-production",
            "synthetic_status_declared": True,
            "public_private_boundary": "public_synthetic_sample_only",
            "sal_meter_input_status": "not_present",
            "cais_compliance_status": "not_granted",
            "benchmark_validation_status": "not_validated"
        },
        "boundary_flags": make_false_flags(FALSE_LOG_BOUNDARY_FLAGS),
        "events": [
            build_feedback_event()
        ],
        "final_rule": FINAL_RULE
    }


def require_keys(label: str, value: dict[str, Any], required_keys: list[str]) -> None:
    """Raise a clear error if required keys are missing."""
    missing = [key for key in required_keys if key not in value]

    if missing:
        raise ValueError(f"{label} is missing required keys: {missing}")


def validate_false_flags(label: str, flags: dict[str, Any], required_flags: list[str]) -> None:
    """
    Confirm that all prohibited-claim flags are present and false.

    This is a lightweight internal boundary check.
    It is not scientific validation.
    """

    require_keys(label, flags, required_flags)

    invalid = {
        key: value
        for key, value in flags.items()
        if key in required_flags and value is not False
    }

    if invalid:
        raise ValueError(
            f"{label} contains boundary flags that must remain false: {invalid}"
        )


def validate_boundary_notice(notice: str) -> None:
    """Confirm that the required public boundary phrases are visible."""

    required_phrases = [
        "Research-stage",
        "Synthetic/sample data only",
        "Local placeholder only",
        "Non-production",
        "Not diagnostic",
        "Not clinical",
        "Not therapeutic",
        "Not surveillance",
        "Not certification",
        "Not Sal-Meter",
        "Not CAIS compliance",
        "Not human ranking",
        "No live intervention",
        "No real-person automation",
    ]

    missing = [phrase for phrase in required_phrases if phrase not in notice]

    if missing:
        raise ValueError(
            f"Boundary notice is missing required phrases: {missing}"
        )


def validate_feedback_event(event: dict[str, Any]) -> None:
    """Validate one synthetic/sample feedback event at helper-structure level."""

    required_event_keys = [
        "event_id",
        "session_id",
        "synthetic_timestamp",
        "event_type",
        "source_module",
        "input_status",
        "output_status",
        "review_state",
        "boundary_status",
        "placeholder_feedback_action",
        "human_review_status",
        "sal_meter_input_status",
        "cais_compliance_status",
        "benchmark_validation_status",
        "event_boundary_flags",
        "audit_note",
    ]

    require_keys("feedback_event", event, required_event_keys)

    if event["sal_meter_input_status"] != "not_present":
        raise ValueError("sal_meter_input_status must remain 'not_present'.")

    if event["cais_compliance_status"] != "not_granted":
        raise ValueError("cais_compliance_status must remain 'not_granted'.")

    if event["benchmark_validation_status"] != "not_validated":
        raise ValueError("benchmark_validation_status must remain 'not_validated'.")

    validate_false_flags(
        "event_boundary_flags",
        event["event_boundary_flags"],
        FALSE_EVENT_BOUNDARY_FLAGS,
    )


def validate_feedback_log(log: dict[str, Any]) -> None:
    """
    Validate the synthetic/sample feedback log at helper-structure level.

    This is not benchmark validation.
    This is not scientific validation.
    This is not Sal-Meter validation.
    This is not CAIS compliance validation.
    """

    required_log_keys = [
        "schema_name",
        "schema_version",
        "track",
        "repository",
        "folder",
        "data_status",
        "authority_status",
        "boundary_notice",
        "log_metadata",
        "boundary_flags",
        "events",
        "final_rule",
    ]

    require_keys("feedback_log", log, required_log_keys)

    if log["schema_name"] != "feedback_event_log_schema":
        raise ValueError("schema_name must be 'feedback_event_log_schema'.")

    if log["schema_version"] != "0.1.0":
        raise ValueError("schema_version must be '0.1.0'.")

    if log["track"] != TRACK:
        raise ValueError(f"track must be '{TRACK}'.")

    if log["repository"] != REPOSITORY:
        raise ValueError(f"repository must be '{REPOSITORY}'.")

    if log["folder"] != FOLDER:
        raise ValueError(f"folder must be '{FOLDER}'.")

    if log["data_status"] not in {
        "synthetic",
        "sample",
        "mock",
        "toy",
        "placeholder",
        "sample-structure-only",
    }:
        raise ValueError("data_status must remain synthetic/sample/mock/toy/placeholder.")

    if log["authority_status"] != "public-helper-structure-only":
        raise ValueError("authority_status must remain public-helper-structure-only.")

    validate_boundary_notice(log["boundary_notice"])

    validate_false_flags(
        "boundary_flags",
        log["boundary_flags"],
        FALSE_LOG_BOUNDARY_FLAGS,
    )

    log_metadata = log["log_metadata"]

    require_keys(
        "log_metadata",
        log_metadata,
        [
            "log_id",
            "session_id",
            "created_at",
            "created_by",
            "environment",
            "execution_mode",
            "production_status",
            "synthetic_status_declared",
            "public_private_boundary",
            "sal_meter_input_status",
            "cais_compliance_status",
            "benchmark_validation_status",
        ],
    )

    if log_metadata["production_status"] != "non-production":
        raise ValueError("production_status must remain 'non-production'.")

    if log_metadata["synthetic_status_declared"] is not True:
        raise ValueError("synthetic_status_declared must be true.")

    if log_metadata["sal_meter_input_status"] != "not_present":
        raise ValueError("log_metadata.sal_meter_input_status must remain 'not_present'.")

    if log_metadata["cais_compliance_status"] != "not_granted":
        raise ValueError("log_metadata.cais_compliance_status must remain 'not_granted'.")

    if log_metadata["benchmark_validation_status"] != "not_validated":
        raise ValueError("log_metadata.benchmark_validation_status must remain 'not_validated'.")

    if not isinstance(log["events"], list) or not log["events"]:
        raise ValueError("events must be a non-empty list.")

    for event in log["events"]:
        validate_feedback_event(event)

    if log["final_rule"] != FINAL_RULE:
        raise ValueError("final_rule has drifted from the required boundary.")


def print_boundary_notice() -> None:
    """Print the public boundary notice before any demo output."""

    print("=" * 79)
    print("SICS HUMAN-STATE PROXY BENCHMARK TRACK")
    print("CLOSED-LOOP DEMO-LITE — LOCAL PLACEHOLDER")
    print("=" * 79)
    print(BOUNDARY_NOTICE)
    print("=" * 79)


def print_usage() -> None:
    """Print minimal command help."""

    print("Usage:")
    print("  python closed-loop-demo-lite/local_feedback_demo_placeholder.py")
    print("  python closed-loop-demo-lite/local_feedback_demo_placeholder.py --json-only")
    print()
    print("This script prints a synthetic/sample feedback event log only.")
    print("It does not collect, process, monitor, diagnose, treat, or intervene.")


def main(argv: list[str]) -> int:
    """Run the local synthetic/sample placeholder demo."""

    if "--help" in argv or "-h" in argv:
        print_usage()
        return 0

    log = build_feedback_log()
    validate_feedback_log(log)

    output = json.dumps(log, indent=2, ensure_ascii=False)

    if "--json-only" in argv:
        print(output)
        return 0

    print_boundary_notice()
    print()
    print("Helper-structure check: PASS")
    print()
    print("Meaning:")
    print(
        "The synthetic/sample feedback event log follows the intended local "
        "demo-lite helper structure."
    )
    print()
    print("Does not mean:")
    print("- benchmark performance validation")
    print("- scientific validation")
    print("- Sal-Meter validation")
    print("- CAIS compliance")
    print("- diagnosis")
    print("- therapy")
    print("- surveillance readiness")
    print("- certification readiness")
    print("- human ranking")
    print("- live intervention")
    print("- production automation")
    print()
    print("Synthetic/sample feedback event log:")
    print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
