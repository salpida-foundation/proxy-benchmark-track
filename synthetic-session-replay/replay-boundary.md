# Replay Boundary

This document defines the public boundary for the P4-5 Synthetic Session Replay Skeleton.

It belongs to the SICS Human-State Proxy Benchmark Track.

It is research-stage.

It is synthetic-only.

It is public-helper-only.

It is replay-scaffold-only.

It is not real session replay.

It is not real phone replay.

It is not real transcript replay.

It is not clinical.

It is not diagnostic.

It is not therapeutic.

It is not counseling.

It is not surveillance.

It is not Sal-Meter.

It is not CAIS compliance.

It is not benchmark validation.

It is not scientific validation.

It is not mediation validation.

It is not dyadic recovery validation.

It is not termination-gate accuracy validation.

It is not phone monitoring.

It is not device readiness.

It is not production readiness.

It is not production closed-loop intervention.

A closed session must stay closed.

A replay must not reopen a closed session.

---

## 1. Boundary purpose

The purpose of this boundary document is to prevent replay scaffolding from being mistaken for evidence, validation, certification, monitoring authority, or production authority.

A synthetic replay may show:

```text
what synthetic step followed what synthetic step
what boundary check appeared in the synthetic flow
what gate appeared in the synthetic flow
what closure state appeared in the synthetic flow
what audit-only summary appeared at the end
```

A synthetic replay must not claim:

```text
that a real session occurred
that a real phone call was processed
that a real transcript was processed
that a human state was measured
that recovery was validated
that mediation worked
that a termination gate was accurate
that Sal-Meter was validated
that CAIS compliance was granted
that any system is ready for device or production use
```

---

## 2. Allowed replay materials

Allowed materials in this folder:

```text
synthetic replay manifest
synthetic replay event timeline
synthetic replay boundary notes
synthetic session-flow references
synthetic phone-only simulator references
synthetic audit-only replay summary
public-helper-only replay documentation
```

Allowed source references:

```text
synthetic-session-replay/replay-manifest.json
synthetic-session-replay/replay-event-timeline.json
synthetic-session-replay/replay-boundary.md
phone-only-simulator/README.md
phone-only-simulator/session-flow-wireframe.md
phone-only-simulator/phone-session-state-machine.json
phone-only-simulator/sample-phone-session-script.md
sample-data/synthetic-dyadic-session-001/ai_outputs.json
sample-data/synthetic-dyadic-session-001/dyadic_delta.json
sample-data/synthetic-dyadic-session-001/recovery_gate.json
sample-data/synthetic-dyadic-session-001/termination_gate.json
sample-data/synthetic-dyadic-session-001/audit_log.json
sample-data/synthetic-dyadic-session-001/termination_gate_cases.json
```

Allowed replay actions:

```text
load synthetic manifest
review synthetic timeline
review consent boundary
review packet boundary
review AI output structure
review Human-State Delta structure
review Recovery Gate structure
review Termination Gate structure
confirm closed-session handling
write audit-only summary
```

---

## 3. Prohibited replay materials

Do not include:

- raw human data;
- identifiable human data;
- real participant data;
- real dyadic conflict records;
- real phone recordings;
- real call transcripts;
- real phone-session logs;
- private consent records;
- clinical records;
- health records;
- diagnostic labels;
- therapeutic recommendations;
- counseling notes;
- relationship verdicts;
- human scores;
- human-ranking outputs;
- raw biosignals;
- raw Sal-Meter traces;
- raw CAIS traces;
- CAIS compliance dossiers;
- production intervention logs;
- production monitoring logs;
- device-readiness evidence;
- production-readiness evidence;
- certification evidence.

If a file contains any of the above, it does not belong in this folder.

---

## 4. Prohibited replay claims

Do not claim or imply:

```text
benchmark validation
scientific validation
mediation validation
dyadic recovery validation
termination-gate accuracy validation
phone monitoring validation
Sal-Meter validation
CAIS compliance
clinical readiness
diagnostic readiness
therapeutic readiness
device readiness
production readiness
certification
relationship verdict authority
human-ranking authority
production closed-loop authority
```

Do not use phrases such as:

```text
validated replay system
clinical replay
diagnostic replay
therapeutic replay
counseling replay
production mediation replay
real phone replay
real transcript replay
real-time monitoring replay
relationship verdict replay
human ranking replay
certified replay
validated benchmark replay
validated mediation replay
validated recovery replay
validated termination gate replay
Sal-Meter replay output
CAIS-compliant replay system
device-ready replay system
production-ready replay system
closed-loop intervention replay
```

---

## 5. Closed-session replay rule

A closed session must stay closed.

A replay must not reopen a closed session.

A replay must not continue ordinary mediation after closure.

A replay must not generate a new AI output after closure.

A replay must not transform closure into recovery evidence.

A replay must not transform closure into termination-gate accuracy evidence.

A replay must not transform audit into certification.

Correct boundary sentence:

```text
A synthetic replay may document that a session was closed, but it must not reopen the session, continue mediation, validate recovery, validate termination-gate accuracy, or create production authority.
```

---

## 6. Replay interpretation

A replay PASS or completed replay scaffold may mean only:

```text
The replay manifest is structurally readable.
The replay timeline is structurally readable.
The replay boundary is explicitly stated.
The event order is visible.
The closed-session rule is explicit.
The public data boundary is preserved.
```

It does not mean:

```text
the session was real
the phone call was real
the transcript was real
the human state was measured
the dyad recovered
the mediation succeeded
the termination gate was accurate
the benchmark was validated
the system is clinical
the system is device-ready
the system is production-ready
the system is certified
```

---

## 7. Relationship to P4-4

P4-4 created a phone-only simulator scaffold.

P4-5 creates a synthetic replay scaffold.

P4-4 shows a possible synthetic session flow.

P4-5 shows how that synthetic flow may be reviewed after representation.

P4-5 does not validate P4-4.

P4-5 does not validate the phone-only simulator.

P4-5 does not validate mediation.

P4-5 does not validate dyadic recovery.

P4-5 does not validate termination-gate accuracy.

P4-5 does not validate Sal-Meter.

P4-5 does not grant CAIS compliance.

---

## 8. Public release rule

Before any replay file is treated as public helper material, confirm:

```text
raw_human_data_present == false
identifiable_data_present == false
clinical_data_present == false
real_phone_recording_present == false
real_call_transcript_present == false
real_participant_data_present == false
sal_meter_input_present == false
cais_compliance_claim_present == false
benchmark_validation_claim_present == false
scientific_validation_claim_present == false
mediation_validation_claim_present == false
dyadic_recovery_validation_claim_present == false
termination_gate_accuracy_claim_present == false
phone_monitoring_authority_claim_present == false
device_readiness_claim_present == false
production_readiness_claim_present == false
certification_claim_present == false
relationship_verdict_present == false
human_ranking_claim_present == false
production_closed_loop_claim_present == false
```

If any of these fields are not false, the file does not belong in the public replay scaffold.

---

## 9. Correct boundary sentence

```text
Synthetic session replay may demonstrate public helper replay structure only; it does not create evidence, validation, certification, phone monitoring authority, production authority, relationship verdicts, or human-ranking authority.
```

---

## 10. Final rule

The replay skeleton is a map of a map.

It is not the session.

It is not the phone call.

It is not the person.

It is not the relationship.

It is not recovery.

It is not termination-gate accuracy evidence.

It is not Sal-Meter.

It is not CAIS compliance.

It is not production authority.

A closed session must stay closed.
