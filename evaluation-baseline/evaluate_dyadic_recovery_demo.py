#!/usr/bin/env python3
"""
P4-1 synthetic dyadic recovery delta evaluator.

SICS Human-State Proxy Benchmark Track

This evaluator reads the P4-0 synthetic dyadic demo-flow helper objects and
prints a bounded helper-only evaluation summary.

Boundary:
- synthetic demo-flow evaluation only
- not benchmark validation
- not scientific validation
- not mediation validation
- not Sal-Meter validation
- not CAIS compliance
- no raw human data processing
- no identifiable human data processing
- no clinical data processing
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

SAMPLE_DIR = ROOT / "sample-data" / "synthetic-dyadic-session-001"

REQUIRED_FILES = {
    "ai_outputs": SAMPLE_DIR / "ai_outputs.json",
    "dyadic_delta": SAMPLE_DIR / "dyadic_delta.json",
    "recovery_gate": SAMPLE_DIR / "recovery_gate.json",
    "termination_gate": SAMPLE_DIR / "termination_gate.json",
    "audit_log": SAMPLE_DIR / "audit_log.json",
}

OPTIONAL_CONTEXT_FILES = {
    "human_state_packet_A": SAMPLE_DIR / "human_state_packet_A.json",
    "human_state_packet_B": SAMPLE_DIR / "human_state_packet_B.json",
    "dyadic_session_event": SAMPLE_DIR / "dyadic_session_event.json",
    "benchmark_session_container": SAMPLE_DIR / "benchmark_session_container.json",
}

BOUNDARY_NOTICE = """\
This evaluator checks synthetic demo-flow structure only.

It does not validate benchmark performance.
It does not validate scientific truth.
It does not validate mediation effectiveness.
It does not validate Sal-Meter.
It does not grant CAIS compliance.
It does not validate human-state measurement.
It does not process raw human data.
It does not process identifiable human data.
It does not process clinical data.
"""

EXPECTED_FALSE_BOUNDARY_FLAGS = [
    "raw_human_data_present",
    "identifiable_data_present",
    "clinical_data_present",
    "private_session_log_present",
    "real_dyadic_conflict_present",
    "raw_audio_present",
    "raw_video_present",
    "raw_transcript_present",
    "raw_biosignal_present",
    "sal_meter_input_present",
    "cais_compliance_dossier_present",
    "diagnostic_claim_present",
    "therapeutic_claim_present",
    "counseling_claim_present",
    "surveillance_claim_present",
    "legal_mediation_claim_present",
    "benchmark_validation_claim_present",
    "scientific_validation_claim_present",
    "mediation_validation_claim_present",
    "sal_meter_validation_claim_present",
    "cais_compliance_claim_present",
    "production_intervention_claim_present",
    "human_ranking_claim_present",
    "relationship_verdict_present",
]

AI_OUTPUT_EXPECTED_FALSE_FLAGS = [
    "raw_human_data_present",
    "identifiable_data_present",
    "clinical_data_present",
    "private_session_log_present",
    "sal_meter_input_present",
    "cais_compliance_claim_present",
    "benchmark_validation_claim_present",
    "scientific_validation_claim_present",
    "mediation_validation_claim_present",
    "production_intervention_claim_present",
    "human_ranking_claim_present",
    "relationship_verdict_present",
]


def rel(path: Path) -> str:
    """Return repository-relative path text."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_json(path: Path) -> Any:
    """Load a JSON file and return parsed data."""
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {rel(path)}")

    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid JSON in {rel(path)}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def get_path(data: Any, path: str) -> Any:
    """
    Read a dotted path from nested dict/list data.

    Supports:
    - dict keys: a.b.c
    - list indexes: items.0.name
    """
    current = data

    for part in path.split("."):
        if isinstance(current, dict):
            if part not in current:
                raise KeyError(path)
            current = current[part]
            continue

        if isinstance(current, list):
            try:
                index = int(part)
            except ValueError as exc:
                raise KeyError(path) from exc

            try:
                current = current[index]
            except IndexError as exc:
                raise KeyError(path) from exc
            continue

        raise KeyError(path)

    return current


def expect_equal(
    errors: list[str],
    file_label: str,
    data: Any,
    field_path: str,
    expected: Any,
) -> None:
    """Assert that a nested field equals the expected value."""
    try:
        actual = get_path(data, field_path)
    except KeyError:
        errors.append(f"{file_label}: missing field `{field_path}`")
        return

    if actual != expected:
        errors.append(
            f"{file_label}: `{field_path}` expected {expected!r}, got {actual!r}"
        )


def expect_present(
    errors: list[str],
    file_label: str,
    data: Any,
    field_path: str,
) -> None:
    """Assert that a nested field exists and is not empty."""
    try:
        actual = get_path(data, field_path)
    except KeyError:
        errors.append(f"{file_label}: missing field `{field_path}`")
        return

    if actual is None or actual == "":
        errors.append(f"{file_label}: `{field_path}` is empty")


def check_dataset_status(errors: list[str], file_label: str, data: Any) -> None:
    """Check synthetic/sample status fields where present."""
    if isinstance(data, dict) and "dataset_type" in data:
        if data.get("dataset_type") != "synthetic":
            errors.append(
                f"{file_label}: `dataset_type` expected 'synthetic', got {data.get('dataset_type')!r}"
            )

    if isinstance(data, dict) and "synthetic_status" in data:
        if data.get("synthetic_status") != "synthetic_only":
            errors.append(
                f"{file_label}: `synthetic_status` expected 'synthetic_only', got {data.get('synthetic_status')!r}"
            )


def check_boundary_dict(
    errors: list[str],
    file_label: str,
    boundary: Any,
    expected_false_flags: list[str],
) -> None:
    """Check that boundary flags are explicit and false."""
    if not isinstance(boundary, dict):
        errors.append(f"{file_label}: boundary object is missing or not an object")
        return

    if boundary.get("synthetic_public_example") is not True:
        errors.append(
            f"{file_label}: `boundary.synthetic_public_example` expected True"
        )

    for flag in expected_false_flags:
        if flag not in boundary:
            errors.append(f"{file_label}: missing boundary flag `{flag}`")
            continue

        if boundary.get(flag) is not False:
            errors.append(
                f"{file_label}: boundary flag `{flag}` expected False, got {boundary.get(flag)!r}"
            )


def check_top_level_boundary(errors: list[str], file_label: str, data: Any) -> None:
    """Check top-level boundary object."""
    if not isinstance(data, dict):
        errors.append(f"{file_label}: JSON root is not an object")
        return

    check_boundary_dict(
        errors=errors,
        file_label=file_label,
        boundary=data.get("boundary"),
        expected_false_flags=EXPECTED_FALSE_BOUNDARY_FLAGS,
    )

    if data.get("final_boundary_status") != "synthetic_helper_only":
        errors.append(
            f"{file_label}: `final_boundary_status` expected 'synthetic_helper_only', got {data.get('final_boundary_status')!r}"
        )


def check_ai_outputs(errors: list[str], data: Any) -> None:
    """Check ai_outputs.json structure and boundary flags."""
    file_label = "ai_outputs.json"

    check_dataset_status(errors, file_label, data)

    expect_equal(errors, file_label, data, "synthetic_status", "synthetic_only")
    expect_present(errors, file_label, data, "ai_outputs")

    outputs = data.get("ai_outputs")
    if not isinstance(outputs, list) or not outputs:
        errors.append(f"{file_label}: `ai_outputs` must be a non-empty list")
        return

    required_output_ids = {
        "synthetic_ai_output_001",
        "synthetic_ai_output_002",
        "synthetic_ai_output_003",
    }

    seen_output_ids = set()

    for index, output in enumerate(outputs):
        output_label = f"{file_label}: ai_outputs[{index}]"

        if not isinstance(output, dict):
            errors.append(f"{output_label}: item is not an object")
            continue

        output_id = output.get("ai_output_id")
        if output_id:
            seen_output_ids.add(output_id)
        else:
            errors.append(f"{output_label}: missing `ai_output_id`")

        synthetic_context = output.get("synthetic_prompt_context")
        if not isinstance(synthetic_context, dict):
            errors.append(f"{output_label}: missing `synthetic_prompt_context`")
        else:
            for flag in [
                "contains_real_conversation",
                "contains_private_user_statement",
                "contains_identifiable_data",
            ]:
                if synthetic_context.get(flag) is not False:
                    errors.append(
                        f"{output_label}: `synthetic_prompt_context.{flag}` expected False"
                    )

        check_boundary_dict(
            errors=errors,
            file_label=output_label,
            boundary=output.get("boundary"),
            expected_false_flags=AI_OUTPUT_EXPECTED_FALSE_FLAGS,
        )

    missing_ids = required_output_ids - seen_output_ids
    if missing_ids:
        errors.append(f"{file_label}: missing expected AI output IDs: {sorted(missing_ids)}")


def check_dyadic_delta(errors: list[str], data: Any) -> None:
    """Check dyadic_delta.json demo logic."""
    file_label = "dyadic_delta.json"

    check_dataset_status(errors, file_label, data)
    check_top_level_boundary(errors, file_label, data)

    expect_equal(
        errors,
        file_label,
        data,
        "dyadic_delta_summary.one_sided_improvement",
        True,
    )
    expect_equal(
        errors,
        file_label,
        data,
        "dyadic_delta_summary.two_sided_recovery_confirmed",
        False,
    )
    expect_equal(
        errors,
        file_label,
        data,
        "dyadic_delta_summary.dyadic_direction",
        "mixed",
    )
    expect_present(
        errors,
        file_label,
        data,
        "dyadic_delta_summary.false_recovery_risk",
    )
    expect_equal(
        errors,
        file_label,
        data,
        "dyadic_delta_summary.recommended_next_gate",
        "recovery_gate_review",
    )

    expect_equal(
        errors,
        file_label,
        data,
        "linked_refs.ai_output_primary",
        "synthetic_ai_output_002",
    )
    expect_equal(
        errors,
        file_label,
        data,
        "linked_refs.human_state_packet_A",
        "hsp_synthetic_A_001",
    )
    expect_equal(
        errors,
        file_label,
        data,
        "linked_refs.human_state_packet_B",
        "hsp_synthetic_B_001",
    )


def check_recovery_gate(errors: list[str], data: Any) -> None:
    """Check recovery_gate.json demo logic."""
    file_label = "recovery_gate.json"

    check_dataset_status(errors, file_label, data)
    check_top_level_boundary(errors, file_label, data)

    expect_equal(
        errors,
        file_label,
        data,
        "gate_decision.recovery_gate_status",
        "not_passed",
    )
    expect_equal(
        errors,
        file_label,
        data,
        "gate_decision.recovery_decision",
        "do_not_mark_recovered",
    )
    expect_equal(
        errors,
        file_label,
        data,
        "gate_decision.requires_termination_gate_review",
        True,
    )
    expect_equal(
        errors,
        file_label,
        data,
        "input_summary.two_sided_recovery_confirmed",
        False,
    )
    expect_equal(
        errors,
        file_label,
        data,
        "input_summary.one_sided_improvement",
        True,
    )


def check_termination_gate(errors: list[str], data: Any) -> None:
    """Check termination_gate.json demo logic."""
    file_label = "termination_gate.json"

    check_dataset_status(errors, file_label, data)
    check_top_level_boundary(errors, file_label, data)

    expect_equal(
        errors,
        file_label,
        data,
        "gate_decision.termination_gate_status",
        "passed",
    )
    expect_equal(
        errors,
        file_label,
        data,
        "gate_decision.termination_decision",
        "pause_and_close_session",
    )
    expect_equal(
        errors,
        file_label,
        data,
        "gate_decision.continue_mediation_allowed",
        False,
    )
    expect_equal(
        errors,
        file_label,
        data,
        "gate_decision.closure_required",
        True,
    )
    expect_equal(
        errors,
        file_label,
        data,
        "gate_decision.audit_log_required",
        True,
    )
    expect_equal(
        errors,
        file_label,
        data,
        "gate_decision.new_session_required_for_future_continuation",
        True,
    )


def check_audit_log(errors: list[str], data: Any) -> None:
    """Check audit_log.json demo logic."""
    file_label = "audit_log.json"

    check_dataset_status(errors, file_label, data)
    check_top_level_boundary(errors, file_label, data)

    expect_equal(
        errors,
        file_label,
        data,
        "audit_checks.session_closed",
        True,
    )
    expect_equal(
        errors,
        file_label,
        data,
        "audit_checks.new_session_required_for_continuation",
        True,
    )
    expect_equal(
        errors,
        file_label,
        data,
        "audit_findings.recovery_status",
        "not_confirmed",
    )
    expect_equal(
        errors,
        file_label,
        data,
        "audit_findings.termination_status",
        "pause_and_close",
    )
    expect_equal(
        errors,
        file_label,
        data,
        "audit_findings.final_public_state",
        "closed",
    )
    expect_equal(
        errors,
        file_label,
        data,
        "audit_findings.false_recovery_prevention",
        "active",
    )

    audit_chain = data.get("audit_chain")
    if not isinstance(audit_chain, list) or not audit_chain:
        errors.append(f"{file_label}: `audit_chain` must be a non-empty list")
        return

    step_types = {
        item.get("step_type")
        for item in audit_chain
        if isinstance(item, dict)
    }

    required_steps = {
        "session_start",
        "packet_availability",
        "ai_output_recorded",
        "dyadic_delta_recorded",
        "recovery_gate_review",
        "termination_gate_review",
        "session_closure",
    }

    missing_steps = required_steps - step_types
    if missing_steps:
        errors.append(
            f"{file_label}: missing expected audit step types: {sorted(missing_steps)}"
        )


def run_required_file_checks() -> list[str]:
    """Check that required and optional context files exist."""
    errors: list[str] = []

    for path in REQUIRED_FILES.values():
        if not path.exists():
            errors.append(f"Missing required file: {rel(path)}")

    for path in OPTIONAL_CONTEXT_FILES.values():
        if not path.exists():
            errors.append(f"Missing optional context file: {rel(path)}")

    return errors


def load_required_files(errors: list[str]) -> dict[str, Any]:
    """Load all required P4-0 demo-flow files."""
    loaded: dict[str, Any] = {}

    for label, path in REQUIRED_FILES.items():
        try:
            loaded[label] = load_json(path)
        except Exception as exc:
            errors.append(str(exc))

    return loaded


def print_header() -> None:
    print("SICS Human-State Proxy Benchmark Track")
    print("P4-1 Synthetic Dyadic Recovery Delta Evaluator v0.1")
    print()
    print(BOUNDARY_NOTICE)


def print_pass() -> None:
    print("PASS: synthetic dyadic recovery demo flow evaluated successfully.")
    print()
    print("Synthetic demo result:")
    print("- dyadic recovery confirmed: false")
    print("- one-sided improvement: true")
    print("- recovery gate: not_passed")
    print("- termination gate: pause_and_close_session")
    print("- audit state: closed")
    print("- false recovery prevention: active")
    print("- public boundary: preserved")
    print()
    print("Validated demo-flow files:")
    for path in REQUIRED_FILES.values():
        print(f"- {rel(path)}")
    print()
    print("Interpretation:")
    print(
        "This result means only that the synthetic demo-flow objects are internally consistent enough for public helper demonstration."
    )
    print()
    print("It does not mean:")
    print("- the benchmark is validated")
    print("- the science is validated")
    print("- the mediation system works")
    print("- the dyadic recovery is real")
    print("- the repository is Sal-Meter")
    print("- the repository is CAIS-compliant")
    print(
        "- the package is clinical, diagnostic, therapeutic, certified, device-ready, or production-ready"
    )


def print_fail(errors: list[str]) -> None:
    print("FAIL: synthetic dyadic recovery demo evaluation failed.")
    print()
    print("Failures:")
    print()

    for error in errors:
        print(f"- {error}")

    print()
    print("A failure means structure or boundary mismatch only.")
    print()
    print("It does not mean scientific failure.")
    print("It does not mean benchmark failure.")
    print("It does not mean mediation failure.")
    print("It does not mean Sal-Meter failure.")
    print("It does not mean CAIS compliance failure.")


def main() -> int:
    print_header()

    errors: list[str] = []

    errors.extend(run_required_file_checks())

    loaded = load_required_files(errors)

    if not errors:
        check_ai_outputs(errors, loaded["ai_outputs"])
        check_dyadic_delta(errors, loaded["dyadic_delta"])
        check_recovery_gate(errors, loaded["recovery_gate"])
        check_termination_gate(errors, loaded["termination_gate"])
        check_audit_log(errors, loaded["audit_log"])

    if errors:
        print_fail(errors)
        return 1

    print_pass()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
