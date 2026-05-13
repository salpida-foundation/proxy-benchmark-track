#!/usr/bin/env python3
"""
SICS Human-State Proxy Benchmark Track
Phone-only synthetic mediation demo v0.1

This script reads one synthetic-only phone session JSON file,
checks required public-boundary flags, evaluates placeholder
recovery / termination gate logic, and writes a bounded demo report.

This is public-helper-only.

It is not validation.
It is not clinical.
It is not diagnostic.
It is not therapeutic.
It is not counseling.
It is not surveillance.
It is not Sal-Meter.
It is not CAIS compliance.
It is not certification.
It is not device readiness.
It is not production readiness.
It is not production authority.

A closed session must stay closed.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "phone-only-simulator" / "simulator_config.json"


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
    session: Dict[str, Any],
    required_flags: Dict[str, Any],
) -> None:
    """Confirm required safety / public-boundary flags."""
    session_flags = session.get("boundary_flags", {})

    missing_or_mismatched = []

    for key, expected_value in required_flags.items():
        actual_value = session_flags.get(key)

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


def evaluate_recovery_gate(
    recovery_delta: float,
    recovery_gate_config: Dict[str, Any],
) -> str:
    """
    Evaluate a synthetic recovery gate placeholder.

    This is not real recovery validation.
    """
    pass_threshold = float(recovery_gate_config.get("pass_if_recovery_delta_gte", 0.2))
    fail_threshold = float(recovery_gate_config.get("fail_if_recovery_delta_lt", -0.1))

    if recovery_delta >= pass_threshold:
        return "pass"

    if recovery_delta < fail_threshold:
        return "fail"

    return "hold"


def evaluate_termination_gate(
    session: Dict[str, Any],
    termination_gate_config: Dict[str, Any],
) -> str:
    """
    Evaluate a synthetic termination gate placeholder.

    This is not real-world termination-gate accuracy validation.
    """
    flow = session.get("session_flow", {})
    flags = session.get("boundary_flags", {})
    quality = session.get("quality", {})

    if termination_gate_config.get("require_session_closure", True):
        if flow.get("session_closure_status") != "closed":
            return "hold"

    if termination_gate_config.get("require_raw_data_excluded", True):
        if not quality.get("raw_data_excluded", False):
            return "fail"

    if termination_gate_config.get("require_real_participant_data_false", True):
        if flags.get("real_participant_data") is not False:
            return "fail"

    return "pass"


def build_demo_report(
    config: Dict[str, Any],
    session: Dict[str, Any],
    recovery_gate_status: str,
    termination_gate_status: str,
) -> Dict[str, Any]:
    """Build a bounded synthetic demo report."""
    state_deltas = session.get("state_deltas", {})
    flow = session.get("session_flow", {})
    quality = session.get("quality", {})
    ai_output_condition = session.get("ai_output_condition", {})

    return {
        "report_id": "demo_report_001",
        "demo_name": config.get("demo_name", "Phone-only synthetic mediation demo"),
        "demo_version": config.get("demo_version", "v0.1"),
        "track": config.get("track", "SICS Human-State Proxy Benchmark Track"),
        "repository_surface": config.get("repository_surface", "public-helper"),
        "mode": config.get("mode", "synthetic-only"),
        "session_id": session.get("session_id"),
        "synthetic_only": session.get("boundary_flags", {}).get("synthetic_only"),
        "ai_output_condition": ai_output_condition.get("condition_id"),
        "overload_delta": state_deltas.get("overload_delta"),
        "recovery_delta": state_deltas.get("recovery_delta"),
        "relational_stability_delta": state_deltas.get("relational_stability_delta"),
        "termination_readiness_delta": state_deltas.get("termination_readiness_delta"),
        "recovery_gate_status": recovery_gate_status,
        "termination_gate_status": termination_gate_status,
        "session_closure_status": flow.get("session_closure_status"),
        "data_quality_flag": quality.get("data_quality_flag"),
        "raw_data_excluded": quality.get("raw_data_excluded"),
        "boundary_statement": config.get(
            "final_boundary_statement",
            "This demo is synthetic-only and public-helper-only. It is not validation.",
        ),
    }


def print_terminal_summary(report: Dict[str, Any]) -> None:
    """Print the short public-helper terminal summary."""
    print("SICS Human-State Proxy Benchmark Track")
    print("Phone-only synthetic mediation demo v0.1")
    print()
    print(f"Synthetic-only: {str(report.get('synthetic_only')).lower()}")
    print("Real participant data: false")
    print(f"Raw human data included: {str(not report.get('raw_data_excluded')).lower()}")
    print()
    print(f"Session: {report.get('session_id')}")
    print(f"AI output condition: {report.get('ai_output_condition')}")
    print(f"Recovery gate: {report.get('recovery_gate_status')}")
    print(f"Termination gate: {report.get('termination_gate_status')}")
    print(f"Session closure: {report.get('session_closure_status')}")
    print()
    print("This demo is public-helper-only.")
    print("It is not validation.")


def main() -> int:
    """Run the v0.1 synthetic-only phone demo."""
    try:
        config = load_json(CONFIG_PATH)

        input_session_file = REPO_ROOT / config["input_session_file"]
        output_report_file = REPO_ROOT / config["output_report_file"]

        session = load_json(input_session_file)

        assert_required_boundary_flags(
            session=session,
            required_flags=config.get("required_boundary_flags", {}),
        )

        recovery_delta = float(session.get("state_deltas", {}).get("recovery_delta", 0.0))

        recovery_gate_status = evaluate_recovery_gate(
            recovery_delta=recovery_delta,
            recovery_gate_config=config.get("gate_rules", {}).get("recovery_gate", {}),
        )

        termination_gate_status = evaluate_termination_gate(
            session=session,
            termination_gate_config=config.get("gate_rules", {}).get("termination_gate", {}),
        )

        report = build_demo_report(
            config=config,
            session=session,
            recovery_gate_status=recovery_gate_status,
            termination_gate_status=termination_gate_status,
        )

        write_json(output_report_file, report)

        if config.get("terminal_summary", {}).get("print_header", True):
            print_terminal_summary(report)

        print()
        print(f"Demo report written to: {output_report_file.relative_to(REPO_ROOT)}")

        return 0

    except Exception as error:
        print("Phone-only synthetic mediation demo failed.", file=sys.stderr)
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
