#!/usr/bin/env python3
"""
Boundary language lint helper for the SICS Human-State Proxy Benchmark Track.

This helper scans public-facing helper files for prohibited or risky wording.

Boundary:
- helper wording hygiene only
- not benchmark validation
- not scientific validation
- not Sal-Meter validation
- not CAIS compliance
- no raw human data processing
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]

TERMS_FILE = ROOT / "evaluation-baseline" / "prohibited_terms.json"

DEFAULT_SCAN_TARGETS = [
    "README.md",
    "docs",
    "governance",
    "schemas",
    "sample-data",
    "evaluation-baseline",
    "protocol-helper",
    "dashboard-mockup",
    "closed-loop-demo-lite",
    ".github",
]

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".yml",
    ".yaml",
    ".csv",
}

SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
    ".venv",
    "venv",
}

BOUNDARY_NOTICE = """\
This boundary lint helper checks public wording only.

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


def load_prohibited_terms(path: Path) -> list[str]:
    if not path.exists():
        raise FileNotFoundError(f"Missing prohibited terms file: {path}")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    terms = data.get("prohibited_terms")

    if not isinstance(terms, list):
        raise ValueError("prohibited_terms.json must contain a list under 'prohibited_terms'.")

    clean_terms = []

    for term in terms:
        if isinstance(term, str) and term.strip():
            clean_terms.append(term.strip())

    if not clean_terms:
        raise ValueError("No prohibited terms were found in prohibited_terms.json.")

    return clean_terms


def should_skip_path(path: Path) -> bool:
    parts = set(path.parts)

    if parts.intersection(SKIP_DIRS):
        return True

    if path.name == "prohibited_terms.json":
        return True

    if path.name == "boundary_lint.py":
        return True

    return False


def iter_scan_files(targets: Iterable[str]) -> Iterable[Path]:
    for target in targets:
        path = ROOT / target

        if not path.exists():
            continue

        if should_skip_path(path):
            continue

        if path.is_file():
            if path.suffix.lower() in TEXT_SUFFIXES:
                yield path
            continue

        for child in path.rglob("*"):
            if child.is_file() and child.suffix.lower() in TEXT_SUFFIXES:
                if not should_skip_path(child):
                    yield child


def scan_file(path: Path, terms: list[str]) -> list[tuple[Path, int, str]]:
    matches: list[tuple[Path, int, str]] = []

    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        print(f"Warning: could not read {path}: {exc}", file=sys.stderr)
        return matches

    lowered_lines = text.lower().splitlines()

    for line_no, line in enumerate(lowered_lines, start=1):
        for term in terms:
            if term.lower() in line:
                matches.append((path, line_no, term))

    return matches


def print_warning(matches: list[tuple[Path, int, str]]) -> None:
    print("Boundary language warning detected.")
    print()
    print("This repository is a public helper surface only.")
    print()
    print(
        "Detected wording may imply benchmark validation, scientific validation, "
        "Sal-Meter validation, CAIS compliance, clinical authority, diagnostic authority, "
        "therapeutic authority, surveillance readiness, certification, device-readiness, "
        "production deployment, mediation-service readiness, counseling-service readiness, "
        "or human-ranking authority."
    )
    print()
    print("Matched terms:")
    print()

    for path, line_no, term in matches:
        rel_path = path.relative_to(ROOT)
        print(f"- {rel_path}:{line_no} -> {term}")

    print()
    print("Please revise the wording to preserve the public helper boundary.")
    print()
    print(BOUNDARY_NOTICE)


def print_pass() -> None:
    print("Boundary language lint completed.")
    print()
    print("No configured prohibited or risky boundary-language terms were detected.")
    print()
    print(
        "This result does not validate benchmark performance, scientific truth, "
        "Sal-Meter, CAIS compliance, mediation effectiveness, clinical use, diagnostic use, "
        "therapeutic use, surveillance readiness, certification, device-readiness, "
        "production readiness, or human-state truth measurement."
    )
    print()
    print(BOUNDARY_NOTICE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan public helper files for prohibited boundary-language terms."
    )

    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 1 if prohibited or risky terms are detected.",
    )

    parser.add_argument(
        "--terms-file",
        default=str(TERMS_FILE),
        help="Path to prohibited_terms.json.",
    )

    parser.add_argument(
        "targets",
        nargs="*",
        default=DEFAULT_SCAN_TARGETS,
        help="Files or directories to scan. Defaults to public helper paths.",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    terms = load_prohibited_terms(Path(args.terms_file))

    scan_targets = args.targets or DEFAULT_SCAN_TARGETS

    all_matches: list[tuple[Path, int, str]] = []

    for file_path in iter_scan_files(scan_targets):
        all_matches.extend(scan_file(file_path, terms))

    if all_matches:
        print_warning(all_matches)
        return 1 if args.strict else 0

    print_pass()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
