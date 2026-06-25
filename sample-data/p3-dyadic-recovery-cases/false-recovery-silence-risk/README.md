# P3 False Recovery / Silence-as-Recovery Risk Synthetic Case

This folder contains a synthetic public-helper case for a P3 `false_recovery` output.

This case is designed to show that silence, politeness, apparent synchrony, reduced visible conflict, or quick session closure must not be treated as dyadic recovery.

A false recovery case occurs when the interaction appears calmer on the surface while underlying burden, withdrawal, pressure, unresolved asymmetry, or erasure risk remains present.

---

## Case role

```text
case_id: p3_false_recovery_silence_risk_001
case_type: false-recovery-silence-risk
expected_recovery_direction: false_recovery
expected_termination_recommendation: continue
```

---

## What this case demonstrates

This synthetic case demonstrates a bounded false-recovery pattern where:

- visible conflict decreases;
- one or both participants become quieter;
- surface politeness increases;
- the AI output may appear calming;
- silence is mistaken for recovery unless explicitly checked;
- one participant may comply under pressure;
- dyadic stabilization is not confirmed;
- termination should not be allowed as true recovery;
- the event should remain open for continued review or audit.

---

## Required distinction

This case exists to make the following distinction clear:

```text
false_recovery ≠ true_recovery
silence ≠ dyadic recovery
politeness ≠ dyadic recovery
reduced visible conflict ≠ dyadic recovery
session closure ≠ dyadic recovery
compliance under pressure ≠ dyadic recovery
```

A dyadic recovery event must not be marked as true recovery when silence or compliance hides unresolved burden.

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
recovery_direction: false_recovery
participant_a_burden_delta: stable or superficially improved direction
participant_b_burden_delta: stable, worsened, or hidden burden direction
asymmetry_risk: medium or high
silence_as_recovery_risk: high
coercion_or_erasure_risk: medium or high
termination_recommendation: continue
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

- the conversation becomes quiet;
- the participants become polite;
- both sides stop objecting;
- the visible conflict decreases;
- the AI output appears calming;
- one participant complies under pressure;
- the session reaches a closure point;
- no immediate escalation is visible;
- the interaction appears synchronized at the surface level.

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
- `dyadic_recovery_event.json` represents a false-recovery / silence-as-recovery risk pattern;
- silence is not treated as recovery by default;
- reduced visible conflict is not treated as recovery by default;
- compliance under pressure is not treated as recovery;
- termination is not allowed as true recovery;
- applicable schema validation passes;
- boundary lint passes.
