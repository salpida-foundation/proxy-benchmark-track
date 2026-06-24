# P3 True Recovery Candidate Synthetic Case

This folder contains a synthetic public-helper case for a P3 `true_recovery` candidate.

This case is designed to show that true recovery is not merely agreement, silence, politeness, or synchrony.

A true recovery candidate requires both participant-level burden reduction and dyadic-level stabilization after an AI output.

---

## Case role

```text
case_id: p3_true_recovery_candidate_001
case_type: true-recovery-candidate
expected_recovery_direction: true_recovery
expected_termination_recommendation: close
```

---

## What this case demonstrates

This synthetic case demonstrates a bounded recovery candidate where:

- participant A burden decreases;
- participant B burden decreases;
- neither participant is treated as the winner or loser;
- both participants retain voice;
- both participants can restate the other side without erasure;
- the interaction becomes more stable after the AI output;
- silence is not used as the primary recovery signal;
- politeness is not used as the primary recovery signal;
- synchrony is not used as the primary recovery signal;
- one-sided relief is not treated as dyadic recovery.

---

## Required distinction

This case exists to make the following distinction clear:

```text
true_recovery ≠ agreement only
true_recovery ≠ silence only
true_recovery ≠ politeness only
true_recovery ≠ synchrony only
true_recovery ≠ one-sided relief
```

A true recovery candidate must show paired burden reduction and dyadic stabilization.

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
recovery_direction: true_recovery
participant_a_burden_delta: negative or improved direction
participant_b_burden_delta: negative or improved direction
asymmetry_risk: low
silence_as_recovery_risk: low
coercion_or_erasure_risk: low
termination_recommendation: close
audit_status: structure_check_passed
```

The exact numeric values may remain synthetic helper values.

They are not person scores.

They are not relationship scores.

They are not clinical scores.

They are not device outputs.

---

## False-recovery guard

This case must not pass merely because:

- both participants become quiet;
- both participants become polite;
- both participants use similar wording;
- the AI output appears well-written;
- the session ends smoothly;
- one participant reports relief while the other remains burdened;
- one participant is pressured into agreement;
- unresolved tension is hidden by closure.

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
- `dyadic_recovery_event.json` uses `recovery_direction: true_recovery`;
- both participants show bounded synthetic burden reduction;
- asymmetry risk remains low;
- silence-as-recovery risk remains low;
- coercion or erasure risk remains low;
- applicable schema validation passes;
- boundary lint passes.
