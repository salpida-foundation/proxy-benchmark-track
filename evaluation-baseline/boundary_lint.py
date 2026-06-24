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
- not mediation validation
- not dyadic recovery validation
- not termination-gate accuracy validation
- not replay validation
- not phone monitoring validation
- not certification
- not device readiness
- not production readiness
- no raw human data processing

This script checks wording boundary only.
It does not validate science, benchmark performance, mediation effectiveness,
human-state measurement, dyadic recovery, Sal-Meter, CAIS compliance,
clinical status, diagnostic status, therapeutic status, surveillance status,
device readiness, production readiness, or certification.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
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
    "prompts",
    "dashboard-mockup",
    "phone-only-simulator",
    "synthetic-session-replay",
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
    ".py",
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

SKIP_FILES = {
    "prohibited_terms.json",
    "boundary_lint.py",
}

BOUNDARY_NOTICE = """\
This boundary lint helper checks public wording only.

It does not validate benchmark performance.
It does not validate scientific truth.
It does not validate Sal-Meter.
It does not grant CAIS compliance.
It does not validate mediation effectiveness.
It does not validate dyadic recovery.
It does not validate termination-gate accuracy.
It does not validate replay accuracy.
It does not validate phone monitoring.
It does not validate human-state measurement.
It does not process raw human data.
It does not process identifiable human data.
It does not process clinical data.
It does not process Sal-Meter raw input.
It does not process CAIS compliance dossiers.
It does not create certification, device readiness, production readiness, or deployment authority.
"""

ALLOWED_CONTEXT_HEADINGS = [
    "prohibited terms",
    "prohibited claims",
    "must not imply",
    "must not contain",
    "non-goals",
    "non goals",
    "boundary",
    "correct boundary sentence",
    "pass does not mean",
    "this does not validate",
    "this is not",
    "does not mean",
    "not intended to support",
    "prohibited content",
    "public boundary",
    "final boundary",
]

BOUNDARY_NEGATION_MARKERS = [
    "not ",
    "no ",
    "non-",
    "does not",
    "do not",
    "must not",
    "should not",
    "cannot",
    "is not",
    "are not",
    "doesn't",
    "do not create",
    "does not create",
    "does not validate",
    "does not grant",
    "does not authorize",
    "not validate",
    "not validated",
    "not certified",
    "not cais",
    "not sal-meter",
    "not sal meter",
    "not benchmark",
    "not mediation",
    "not clinical",
    "not diagnostic",
    "not therapeutic",
    "not surveillance",
    "not production",
    "not device",
    "not human-ranking",
    "not human ranking",
    "prohibited",
    "boundary",
    "non-goal",
    "non-goals",
]

UNSAFE_POSITIVE_CLAIM_PATTERNS = [
    r"\bthis\s+benchmark\s+is\s+validated\b",
    r"\bbenchmark\s+is\s+validated\b",
    r"\bthis\s+system\s+is\s+cais[-\s]?compliant\b",
    r"\bsystem\s+is\s+cais[-\s]?compliant\b",
    r"\bproxy\s+stack\s+is\s+sal[-\s]?meter\s+ready\b",
    r"\bevaluator\s+proves\s+mediation\s+effectiveness\b",
    r"\bdashboard\s+provides\s+relationship\s+verdicts\b",
    r"\bsimulator\s+supports\s+employee\s+monitoring\b",
    r"\bworkflow\s+certifies\s+production\s+readiness\b",
    r"\bcertifies\s+production\s+readiness\b",
    r"\bgrants\s+cais\s+compliance\b",
    r"\bcreates\s+sal[-\s]?meter\s+status\b",
    r"\bvalidates\s+dyadic\s+recovery\b",
    r"\bvalidates\s+termination[-\s]?gate\s+accuracy\b",
]


@dataclass(frozen=True)
class LintMatch:
    path: Path
    line_no: int
    term: str
    kind: str
    line: str


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

    return sorted(set(clean_terms), key=lambda item: item.lower())


def should_skip_path(path: Path) -> bool:
    parts = set(path.parts)

    if parts.intersection(SKIP_DIRS):
        return True

    if path.name in SKIP_FILES:
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


def compile_term_pattern(term: str) -> re.Pattern[str]:
    escaped = re.escape(term)

    # Use alphanumeric-aware boundaries so short canonical symbols
    # such as OE / RE / EE do not match inside ordinary words.
    pattern = rf"(?<![A-Za-z0-9_]){escaped}(?![A-Za-z0-9_])"

    return re.compile(pattern, flags=re.IGNORECASE)


def is_heading_line(line: str) -> bool:
    stripped = line.strip().lower()
    stripped = stripped.strip("#").strip()
    stripped = stripped.strip("*").strip()
    stripped = stripped.strip("-").strip()

    if not stripped:
        return False

    return any(marker in stripped for marker in ALLOWED_CONTEXT_HEADINGS)


def has_boundary_negation(line: str) -> bool:
    lowered = line.lower()
    return any(marker in lowered for marker in BOUNDARY_NEGATION_MARKERS)


def is_allowed_boundary_context(lines: list[str], index: int) -> bool:
    current = lines[index]

    if has_boundary_negation(current):
        return True

    # Allow prohibited terms under a nearby explicit boundary / prohibited-claims section.
    window_start = max(0, index - 6)
    context_window = lines[window_start : index + 1]

    if any(is_heading_line(line) for line in context_window):
        return True

    return False


def find_unsafe_positive_claims(path: Path, lines: list[str]) -> list[LintMatch]:
    matches: list[LintMatch] = []

    for line_no, line in enumerate(lines, start=1):
        lowered = line.lower()

        for pattern in UNSAFE_POSITIVE_CLAIM_PATTERNS:
            if re.search(pattern, lowered, flags=re.IGNORECASE):
                if not is_allowed_boundary_context(lines, line_no - 1):
                    matches.append(
                        LintMatch(
                            path=path,
                            line_no=line_no,
                            term=pattern,
                            kind="unsafe_positive_claim",
                            line=line.strip(),
                        )
                    )

    return matches


def scan_file(path: Path, terms: list[str]) -> list[LintMatch]:
    matches: list[LintMatch] = []

    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        print(f"Warning: could not read {path}: {exc}", file=sys.stderr)
        return matches

    lines = text.splitlines()

    matches.extend(find_unsafe_positive_claims(path, lines))

    compiled_terms = [(term, compile_term_pattern(term)) for term in terms]

    for index, line in enumerate(lines):
        for term, pattern in compiled_terms:
            if pattern.search(line):
                if is_allowed_boundary_context(lines, index):
                    continue

                matches.append(
                    LintMatch(
                        path=path,
                        line_no=index + 1,
                        term=term,
                        kind="prohibited_term",
                        line=line.strip(),
                    )
                )

    return matches


def print_warning(matches: list[LintMatch]) -> None:
    print("Boundary language violation detected.")
    print()
    print("This repository is a public helper surface only.")
    print()
    print(
        "Detected wording may imply benchmark validation, scientific validation, "
        "Sal-Meter validation, CAIS compliance, clinical authority, diagnostic authority, "
        "therapeutic authority, surveillance readiness, certification, device-readiness, "
        "production deployment, mediation-service readiness, counseling-service readiness, "
        "phone monitoring authority, replay validation authority, or human-ranking authority."
    )
    print()
    print("Matched terms / patterns:")
    print()

    for match in matches:
        rel_path = match.path.relative_to(ROOT)
        print(f"- {rel_path}:{match.line_no} -> {match.kind}: {match.term}")
        if match.line:
            print(f"  line: {match.line}")

    print()
    print("Please revise the wording to preserve the public helper boundary.")
    print()
    print(BOUNDARY_NOTICE)


def print_pass() -> None:
    print("Boundary language lint completed.")
    print()
    print("No configured prohibited or risky boundary-language violations were detected.")
    print()
    print(
        "This result does not validate benchmark performance, scientific truth, "
        "Sal-Meter, CAIS compliance, mediation effectiveness, dyadic recovery, "
        "termination-gate accuracy, clinical use, diagnostic use, therapeutic use, "
        "surveillance readiness, certification, device-readiness, production readiness, "
        "phone monitoring authority, replay validation authority, or human-state truth measurement."
    )
    print()
    print(BOUNDARY_NOTICE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan public helper files for prohibited boundary-language terms."
    )

    parser.add_argument(
        "--warn-only",
        action="store_true",
        help="Exit with code 0 even if prohibited or risky terms are detected.",
    )

    parser.add_argument(
        "--strict",
        action="store_true",
        help="Deprecated compatibility flag. The lint now fails by default unless --warn-only is used.",
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

    all_matches: list[LintMatch] = []

    for file_path in iter_scan_files(scan_targets):
        all_matches.extend(scan_file(file_path, terms))

    if all_matches:
        print_warning(all_matches)
        return 0 if args.warn_only else 1

    print_pass()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
