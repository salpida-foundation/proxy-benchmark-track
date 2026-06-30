> ## ⚠️ DEPRECATED — superseded by the A/B/C/D package
> This A/B (two-condition) package is **retained for backward compatibility only**.
> The current P2 design uses **four conditions (A/B/C/D)**, aligned to
> `docs/pilot-design/proxy-benchmark-pilot-design-v1.1.md` (section 5).
>
> - Current package: `sample-data/p2-ai-output-abcd/`
> - Current evaluator: `evaluation-baseline/evaluate_ai_output_abcd.py`
> - Current config: `evaluation-baseline/ai_output_abcd_consequence_config.json`
>
> This folder, its `evaluate_ai_output_ab.py` evaluator, and its config are **not deleted**;
> they remain runnable for regression history. New work should target the A/B/C/D package.
> This deprecation notice is wording/pointer hygiene only. It is **not** validation,
> certification, Sal-Meter status, CAIS compliance, or production readiness.

---

# P2 AI Output A/B Synthetic Comparison Package

This folder contains a synthetic-only public helper package for AI Output A/B consequence comparison.

It supports the P2 AI Output A/B evaluator helper.

It is not real human data.

It is not real participant data.

It is not a real conversation.

It is not a real phone recording.

It is not a real transcript.

It is not a real session log.

It is not clinical data.

It is not diagnostic data.

It is not therapeutic data.

It is not counseling data.

It is not surveillance data.

It is not Sal-Meter input.

It is not CAIS trace data.

It is not benchmark validation.

It is not mediation validation.

It is not real AI impact validation.

It is not real human-state measurement validation.

It is not certification.

It is not device readiness.

It is not production readiness.

It is not production authority.

---

## Purpose

This package provides bounded synthetic input files for comparing two or more AI output conditions by downstream proxy-only consequence fields.

The package is intended to support:

- synthetic AI Output A/B comparison
- generic AI baseline comparison
- rule-based mediation baseline comparison
- state-aware output candidate comparison
- synthetic baseline packet review
- synthetic post-output packet review
- expected evaluator output review
- public-helper-only regression checking

It must not be used as evidence of real-world AI impact.

It must not be used as evidence of dyadic recovery.

It must not be used as evidence of mediation effectiveness.

It must not be used as evidence of clinical, diagnostic, therapeutic, counseling, surveillance, Sal-Meter, CAIS compliance, device-readiness, production-readiness, or certification status.

---

## Required files

This package should contain:

- `generic_ai_baseline.json`
- `rule_based_mediation_baseline.json`
- `state_aware_output_candidate.json`
- `synthetic_baseline_packet.json`
- `synthetic_post_output_packet_A.json`
- `synthetic_post_output_packet_B.json`
- `expected_evaluator_output.json`
- `README.md`

---

## Allowed proxy-only evaluator fields

The evaluator output should remain limited to proxy-only helper fields such as:

- `overload_delta`
- `recovery_burden_delta`
- `relational_stability_delta`
- `asymmetry_risk`
- `false_recovery_risk`
- `termination_readiness`
- `audit_status`

These fields are synthetic helper fields.

They are not validated clinical, psychological, therapeutic, diagnostic, counseling, surveillance, mediation, or human-state metrics.

---

## Prohibited evaluator outputs

This package must not introduce or rely on:

- OE
- RE
- EE
- VCE
- CRI
- CFI
- CAIS compliance
- Sal-Meter readiness
- validated benchmark
- validated mediation
- certified status
- clinical validation
- diagnostic use
- therapeutic use
- employee monitoring
- emotion diagnosis
- person scoring
- relationship verdict
- production mediation
- production readiness

---

## File roles

### `generic_ai_baseline.json`

Represents a synthetic generic AI output baseline.

It is used only as a comparison condition.

It does not represent a real AI deployment or a validated baseline.

### `rule_based_mediation_baseline.json`

Represents a synthetic fixed-rule mediation-script baseline.

It is used only as a comparison condition.

It does not represent legal mediation, counseling, therapy, or validated mediation effectiveness.

### `state_aware_output_candidate.json`

Represents a synthetic state-aware output candidate.

It is the candidate condition for comparison.

It does not prove state-awareness.

It does not validate real human-state measurement.

It does not validate mediation effectiveness.

### `synthetic_baseline_packet.json`

Represents a synthetic bounded pre-output state-summary helper packet.

It does not contain raw human data.

It does not identify a person.

It does not diagnose a state.

It does not score a human.

It does not judge a relationship.

### `synthetic_post_output_packet_A.json`

Represents a synthetic bounded post-output helper packet for condition A.

It does not contain real participant data.

It does not contain raw biosignals.

It does not contain clinical or diagnostic records.

### `synthetic_post_output_packet_B.json`

Represents a synthetic bounded post-output helper packet for condition B.

It does not contain real participant data.

It does not contain raw biosignals.

It does not contain clinical or diagnostic records.

### `expected_evaluator_output.json`

Represents the expected synthetic helper output for regression checking.

It does not validate real-world impact.

It does not validate benchmark performance.

It does not validate dyadic recovery.

It does not validate mediation.

---

## Boundary flags

All files in this folder must remain:

- synthetic-only
- public-helper-only
- raw-data-free
- non-identifying
- non-clinical
- non-diagnostic
- non-therapeutic
- non-counseling
- non-surveillance
- non-certification
- non-human-ranking
- not Sal-Meter
- not Proxy Sal-Meter
- not CAIS compliance
- not benchmark validation
- not mediation validation
- not dyadic recovery validation
- not termination-gate accuracy validation
- not device readiness
- not production readiness

---

## Correct boundary sentence

The P2 AI Output A/B synthetic comparison package may support synthetic public-helper regression checking for proxy-only AI output consequence comparison, but it does not create evidence, validation, certification, Sal-Meter status, CAIS compliance, mediation authority, phone monitoring authority, replay validation authority, production authority, relationship verdicts, or human-ranking authority.
