# P3 Asymmetric Recovery Synthetic Case

This folder contains a synthetic public-helper case for a P3 `asymmetric_recovery` output.

This case is designed to show that one-sided relief is not dyadic recovery.

An asymmetric recovery case occurs when one participant appears improved while the other participant becomes more burdened, exposed, silenced, or destabilized after an AI output.

---

## Case role

```text
case_id: p3_asymmetric_recovery_001
case_type: asymmetric-recovery
expected_recovery_direction: asymmetric_recovery
expected_termination_recommendation: pause
```

---

## What this case demonstrates

This synthetic case demonstrates a bounded asymmetric recovery pattern where:

- participant A appears improved;
- participant B becomes more burdened or less stable;
- the dyad does not move into true recovery;
- one-sided relief is not treated as dyadic recovery;
- polite agreement is not treated as dyadic recovery;
- reduced conflict volume is not treated as dyadic recovery;
- session closure is not treated as sufficient evidence of recovery;
- the event should remain open for audit or continuation.

---

## Required distinction

This case exists to make the following distinction clear:

```text
asymmetric_recovery ≠ true_recovery
one-sided relief ≠ dyadic recovery
lower visible conflict ≠ dyadic recovery
polite compliance ≠ dyadic recovery
session closure ≠ dyadic recovery
```

A dyadic recovery event must not be marked as true recovery when only one side improves.

---

## Expected files

This folder should include:

```text
baseline_packet_A.json
baseline_packet_B.json
ai_output.json
post_output_packet_A.json
post_output_packet_B.json
dyadic_recovery_event.json
audit_log.json
README.md
```

---

## Expected synthetic flow

```text
baseline_packet_A.json
baseline_packet_B.json
        ↓
ai_output.json
        ↓
post_output_packet_A.json
post_output_packet_B.json
        ↓
dyadic_recovery_event.json
        ↓
audit_log.json
```

---

## Expected event output

The expected `dyadic_recovery_event.json` should make the following output visible:

```text
recovery_direction: asymmetric_recovery
participant_a_burden_delta: improved direction
participant_b_burden_delta: worsened or burden-increased direction
asymmetry_risk: high
silence_as_recovery_risk: medium or high
coercion_or_erasure_risk: medium or high
termination_recommendation: pause
audit_status: structure_check_passed
```

The exact numeric values may remain synthetic helper values.

They are not person scores.

They are not relationship scores.

They are not clinical scores.

They are not device outputs.

---

## False-recovery guard

This case must not pass as true recovery merely because:

- participant A reports relief;
- participant B becomes quieter;
- the visible conflict decreases;
- the AI output appears balanced;
- both sides use polite language;
- the session reaches a closure point;
- participant B stops objecting;
- a short-term reduction in escalation appears after the AI output.

---

## Public boundary

This folder is a synthetic public-helper example only.

It does not contain raw human data.

It does not contain identifiable human data.

It does not contain real participant data.

It does not contain real dyadic conflict records.

It does not contain real session records.

It does not contain real phone recordings.

It does not contain real transcripts.

It does not contain clinical records.

It does not create diagnostic labels.

It does not create therapeutic recommendations.

It does not create counseling notes.

It does not create relationship verdicts.

It does not create human scores.

It does not contain Sal-Meter raw traces.

It does not contain CAIS traces.

It does not grant CAIS compliance.

It does not validate real dyadic recovery.

It does not validate mediation effectiveness.

It does not validate human-state measurement.

It does not validate termination-gate accuracy.

It does not create device readiness.

It does not create production readiness.

It does not create certification.

---

## Done criteria for this case

This case is complete when:

- all required files exist;
- all files use synthetic-only helper content;
- no raw human data is introduced;
- no real participant data is introduced;
- `dyadic_recovery_event.json` represents an asymmetric recovery pattern;
- participant A shows bounded synthetic improvement;
- participant B shows bounded synthetic burden increase or destabilization;
- asymmetry risk is not low;
- one-sided improvement is not treated as dyadic recovery;
- termination is not allowed as true recovery;
- applicable schema validation passes;
- boundary lint passes.
