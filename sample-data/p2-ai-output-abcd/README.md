# P2 AI Output A/B/C/D Consequence Comparison Package

This folder contains a synthetic-only public helper package for the P2 AI Output
**A/B/C/D** consequence comparison, aligned to
`docs/pilot-design/proxy-benchmark-pilot-design-v1.1.md` (section 5).

It supports the P2 AI Output consequence evaluator helper.

It is not real human data. It is not real participant data. It is not a real
conversation, phone recording, transcript, or session log. It is not clinical,
diagnostic, therapeutic, counseling, or surveillance data. It is not Sal-Meter
input. It is not CAIS trace data. It is not benchmark validation, mediation
validation, certification, device readiness, or production readiness.

---

## Purpose

This package provides bounded synthetic input files for comparing **four** fixed
AI output conditions (A/B/C/D) by downstream proxy-only consequence fields.

The package is intended to support:

- synthetic AI Output A/B/C/D comparison
- condition-label regression checking against the v1.1 design
- C-trap pattern regression checking (surface-positive but high false-recovery risk)
- public-helper-only regression checking

It must not be used as evidence of real-world AI impact, dyadic recovery,
mediation effectiveness, or clinical / diagnostic / therapeutic / counseling /
surveillance / Sal-Meter / CAIS-compliance / device-readiness / production-readiness status.

---

## Conditions (fixed A/B/C/D)

| Code | IRB official name | Public label | Expected effect |
|---|---|---|---|
| A | Validating-regulatory response | validating, state-regulating style | state improvement |
| B | Information-only neutral response | information-only neutral style | small change |
| C | Over-validation comparator | uncritical-agreement / over-validating style (low-risk comparator) | short-term mood up, clarity not recovered (C trap) |
| D | Minimizing-dismissive response | low-validation / minimizing style (bounded comparator) | state deterioration |

**Condition C** uses permitted IRB descriptors only (uncritical-agreement,
over-validating, low-cognitive-clarification, non-adaptive but low-risk comparator)
and carries mandatory safeguards (low-intensity scenarios only, single-response
exposure ≤2 min, immediate recovery text, distress check ≥5 → halt + coordinator,
session-end debrief).

**Condition D** is a low-validation comparator, **not** an intentional harm
condition. It excludes ridicule, blame, humiliation, crisis dismissal,
medical/legal/financial advice, and personally targeted negative language. All
distress-check rules apply equally.

---

## Required files

- `README.md`
- `condition_labels.json`
- `condition_A_validating_regulatory.json`
- `condition_B_information_only_neutral.json`
- `condition_C_over_validation_comparator.json`
- `condition_D_minimizing_dismissive.json`
- `expected_evaluator_output.json`

---

## Allowed proxy-only evaluator fields

- `overload_delta`
- `recovery_burden_delta`
- `relational_stability_delta`
- `asymmetry_risk`
- `false_recovery_risk`
- `termination_readiness`
- `audit_status`

These are synthetic helper fields. They are not validated clinical, psychological,
therapeutic, diagnostic, counseling, surveillance, mediation, or human-state metrics.

> **Synthetic value note:** all metric values in this package are synthetic
> illustrative placeholders chosen only to mirror the v1.1 expected-effect
> direction for regression checking. They are not empirical measurements.

---

## Prohibited evaluator outputs

This package must not introduce or rely on: OE, RE, EE, VCE, CRI, CFI,
CAIS compliance, Sal-Meter readiness, validated benchmark, validated mediation,
certified status, clinical validation, diagnostic use, therapeutic use,
employee monitoring, emotion diagnosis, person scoring, relationship verdict,
production mediation, or production readiness.

---

## Boundary flags

All files in this folder must remain: synthetic-only, public-helper-only,
raw-data-free, non-identifying, non-clinical, non-diagnostic, non-therapeutic,
non-counseling, non-surveillance, non-certification, non-human-ranking,
not Sal-Meter, not Proxy Sal-Meter, not CAIS compliance, not benchmark validation,
not mediation validation, not dyadic recovery validation, not device readiness,
not production readiness.

---

## Correct boundary sentence

The P2 AI Output A/B/C/D synthetic comparison package may support synthetic
public-helper regression checking for proxy-only AI output consequence comparison,
but it does not create evidence, validation, certification, Sal-Meter status,
CAIS compliance, mediation authority, phone monitoring authority, replay
validation authority, production authority, relationship verdicts, or
human-ranking authority.
