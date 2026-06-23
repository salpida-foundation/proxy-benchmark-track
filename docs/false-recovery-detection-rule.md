# False Recovery Detection Rule

## Status

Research-stage public helper document.

This document defines the false-recovery detection rule for the Human-State Proxy Benchmark Track.

It is public-helper-only.

It is synthetic/sample-first.

It is raw-data-non-public.

It is non-clinical.

It is non-diagnostic.

It is non-therapeutic.

It is non-counseling.

It is non-surveillance.

It is not Sal-Meter.

It is not Proxy Sal-Meter.

It is not CAIS compliance.

It is not benchmark validation.

It is not mediation validation.

It is not dyadic recovery validation.

It is not termination-gate accuracy validation.

It is not device readiness.

It is not production readiness.

---

## Purpose

The false-recovery detection rule prevents a synthetic or controlled helper system from treating surface calm as recovery.

False recovery occurs when the session appears improved but the bounded dyadic condition has not actually moved toward recovery.

This rule exists because AI output can sound helpful while leaving one participant burdened, silenced, exposed, coerced, or erased.

---

## Core principle

A session is not successful merely because:

- the AI sounded good
- one participant became quiet
- one participant reported relief
- both participants sounded calmer
- both participants showed synchrony
- the visible conflict decreased
- the session closed
- the evaluator produced a favorable helper output

False recovery must be detected before any stronger helper claim is made.

---

## False recovery definition

False recovery is a bounded helper state where apparent improvement masks unresolved or worsening dyadic burden.

False recovery may occur when:

- silence is treated as recovery
- compliance is treated as recovery
- politeness is treated as recovery
- reduced interruption is treated as recovery
- one-sided relief is treated as dyadic repair
- one participant withdraws
- one participant becomes more exposed
- one participant carries more recovery burden
- agreement occurs without repair
- closure is mistaken for recovery
- audit is mistaken for validation

False recovery is not success.

---

## Silence-as-recovery risk

Silence must not be interpreted as recovery by default.

Silence may mean:

- recovery
- fatigue
- withdrawal
- fear
- resignation
- overload
- coercion
- confusion
- strategic non-response
- loss of trust
- refusal to continue

Silence requires boundary-sensitive interpretation.

Silence alone is not evidence.

---

## One-sided relief rule

One-sided relief is not dyadic recovery.

If one participant appears improved while the other becomes more burdened, exposed, silenced, or destabilized, the correct classification is not true recovery.

Possible classifications include:

- asymmetric_recovery
- false_recovery
- deterioration
- unresolved

The dyad is the unit of interpretation.

---

## Compliance risk rule

Compliance must not be treated as recovery by default.

Compliance may reflect:

- pressure
- fatigue
- avoidance
- resignation
- fear of escalation
- desire to end the session
- loss of agency
- one-sided burden transfer

If compliance appears without repair, the helper system must check false-recovery risk.

---

## Surface calm rule

Surface calm is not enough.

A calmer interaction may still contain:

- unresolved burden
- private-state exposure
- hidden asymmetry
- coercion or erasure risk
- loss of consent clarity
- packet-permission drift
- premature closure
- one-sided recovery burden

Surface calm may support review.

It must not automatically produce recovery classification.

---

## Closure rule

Session closure is not recovery by itself.

A session may close because:

- recovery was reached
- consent expired
- packet permission expired
- the session became unsafe
- the scope became unclear
- data quality became insufficient
- continuation would over-intervene
- audit-only status was safer

A closed session must stay closed.

A replay must not reopen a closed session.

A replay must not continue mediation after closure.

A replay must not generate new AI output after closure.

A replay must not convert closure into recovery evidence.

A replay must not convert audit into certification.

---

## False recovery triggers

A helper system should flag false-recovery risk when one or more of the following appear:

- visible conflict decreases but recovery burden does not improve
- one participant becomes silent after AI output
- one participant improves while the other deteriorates
- one participant appears relieved while the other becomes more exposed
- relational stability does not improve
- asymmetry risk remains medium or high
- silence-as-recovery risk remains medium or high
- coercion_or_erasure_risk remains medium or high
- termination is recommended but the session continues
- packet permission is exceeded
- packet expiry is ignored
- audit-only status is treated as intervention authority
- shared output exposes private-state cues

These are helper triggers only.

They are not clinical markers.

They are not diagnostic markers.

They are not therapeutic markers.

They are not validated psychological measures.

---

## Suggested helper fields

A false-recovery helper object may include:

- recovery_direction
- asymmetry_risk
- silence_as_recovery_risk
- coercion_or_erasure_risk
- participant_a_burden_delta
- participant_b_burden_delta
- termination_recommendation
- audit_status
- boundary_status

Allowed recovery_direction values may include:

- true_recovery
- deterioration
- asymmetric_recovery
- false_recovery
- unresolved

Allowed termination_recommendation values may include:

- continue
- narrow
- pause
- close
- audit_only
- refresh_packet

These values are helper categories only.

They are not evidence of real dyadic recovery.

They are not validation.

---

## PASS / REVISE / FAIL helper interpretation

A synthetic helper case may PASS when:

- required files are present
- raw human data is excluded
- real participant data is excluded
- false-recovery risk is represented
- asymmetry risk is represented
- silence-as-recovery risk is represented
- termination recommendation is bounded
- audit status is present
- no prohibited claims are introduced

A synthetic helper case may require REVISE when:

- false-recovery risk is underspecified
- asymmetry risk is unclear
- silence is treated ambiguously
- termination recommendation is unclear
- audit status is missing
- boundary language is incomplete

A synthetic helper case must FAIL when:

- raw human data is included
- identifiable participant data is included
- real session records are included
- clinical interpretation is introduced
- diagnostic interpretation is introduced
- therapeutic recommendation is introduced
- counseling recommendation is introduced
- surveillance framing is introduced
- person scoring is introduced
- relationship verdict is introduced
- Sal-Meter validation is claimed
- CAIS compliance is claimed
- certification is claimed
- production readiness is claimed

---

## Prohibited interpretations

The false-recovery rule must not be described as:

- emotion diagnosis
- person scoring
- relationship scoring
- relationship verdict
- employee monitoring
- surveillance
- clinical validation
- diagnostic validation
- therapeutic validation
- counseling validation
- mediation validation
- dyadic recovery validation
- termination-gate accuracy validation
- benchmark validation
- Sal-Meter validation
- CAIS compliance
- certification
- device readiness
- production readiness
- production closed-loop authority

---

## Correct boundary sentence

The false-recovery detection rule may define public-helper conditions for identifying false recovery, asymmetric recovery, silence-as-recovery risk, and unresolved dyadic burden in synthetic or controlled helper settings, but it does not create evidence, validation, certification, Sal-Meter status, CAIS compliance, mediation authority, surveillance authority, production authority, relationship verdicts, or human-ranking authority.
