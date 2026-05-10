# Phone-only Simulator Boundary

This folder contains a bounded public-helper scaffold for a synthetic phone-only session simulator.

It belongs to the SICS Human-State Proxy Benchmark Track.

It is research-stage.

It is synthetic-only.

It is public-helper-only.

It is not a real phone monitoring system.

It is not a clinical system.

It is not a diagnostic system.

It is not a therapeutic system.

It is not a counseling system.

It is not a mediation-service system.

It is not a surveillance system.

It is not Sal-Meter.

It is not CAIS compliance.

It is not benchmark validation.

It is not mediation validation.

It is not dyadic recovery validation.

It is not termination-gate accuracy validation.

It is not device readiness.

It is not production readiness.

It is not production closed-loop intervention.

A closed session must stay closed.

---

## Purpose

The purpose of this folder is to demonstrate how a phone-only session may be represented as a public-safe simulator wireframe.

The simulator is intended to show structure only.

It may describe how a synthetic session moves through:

```text
Consent
→ Packet Availability Check
→ Baseline State Summary
→ AI Output
→ Human-State Delta
→ Recovery Gate
→ Termination Gate
→ Session Closure
→ Audit Log
```

It does not process real phone calls.

It does not process raw voice.

It does not process transcripts from real people.

It does not process identifiable human data.

It does not process clinical data.

It does not process Sal-Meter raw input.

It does not process CAIS compliance dossiers.

---

## Current intended files

```text
phone-only-simulator/
  README.md
  session-flow-wireframe.md
  phone-session-state-machine.json
  sample-phone-session-script.md
```

| File | Role | Status |
|---|---|---|
| `README.md` | Folder-level boundary and usage notice | Current file |
| `session-flow-wireframe.md` | Public-safe phone-only session flow wireframe | Planned |
| `phone-session-state-machine.json` | Synthetic state-machine mockup for session transitions | Planned |
| `sample-phone-session-script.md` | Synthetic sample phone-session script | Planned |

---

## Scope

This folder may demonstrate:

- phone-only session flow structure;
- consent-first session entry;
- packet availability check;
- synthetic AI output step;
- synthetic Human-State Delta step;
- Recovery Gate placeholder;
- Termination Gate placeholder;
- closed-session handling;
- audit-log boundary;
- public-helper-only simulator posture.

This folder must not create:

- a real phone monitoring system;
- a clinical intake system;
- a diagnostic system;
- a therapeutic system;
- a counseling system;
- a mediation-service system;
- a surveillance system;
- a production closed-loop intervention system;
- a relationship-verdict system;
- a human-ranking system.

---

## Phone-only simulator flow

The intended public helper flow is:

```text
Synthetic Phone Session Created
↓
Consent Confirmed
↓
Packet Availability Checked
↓
Baseline State Summary Available
↓
AI Output Generated
↓
Post-Output Human-State Delta Estimated
↓
Recovery Gate Reviewed
↓
Termination Gate Reviewed
↓
Session Closed or Narrowed
↓
Audit Log Written
```

This is a simulator wireframe.

It is not real mediation.

It is not clinical workflow.

It is not diagnostic triage.

It is not therapeutic intervention.

It is not production deployment.

---

## State-machine boundary

The future `phone-session-state-machine.json` should represent synthetic states only.

Allowed state examples:

```text
session_created
consent_pending
consent_confirmed
packet_unavailable
packet_available
baseline_summary_ready
ai_output_generated
delta_review_pending
recovery_gate_review
termination_gate_review
pause_session
narrow_scope
close_session
terminate_session
audit_log_written
session_closed
```

Forbidden state examples:

```text
diagnosis_ready
therapy_started
clinical_risk_detected
real_time_monitoring_active
relationship_verdict_generated
human_rank_assigned
production_intervention_triggered
sal_meter_validated
cais_compliant
device_ready
certified
```

---

## Closed-session rule

A closed session must stay closed.

A closed session must not be reopened automatically.

A closed session must not continue because the AI has more to say.

A closed session must not continue because one side appears improved.

A closed session must not continue because the simulated output looks persuasive.

A closed session may only be represented as closed, audited, and terminated within the helper scaffold.

Correct boundary sentence:

```text
Once a synthetic phone-only session is closed, the simulator may document closure but must not imply continued mediation, recovery validation, or production intervention.
```

---

## Allowed language

Use:

```text
phone-only simulator wireframe
public helper scaffold
synthetic phone session
sample phone session script
state-machine mockup
session-flow demonstration
consent-first flow
packet availability check
recovery gate placeholder
termination gate placeholder
audit closure
closed-session handling
public-helper-only
synthetic-only
non-clinical
non-diagnostic
non-therapeutic
non-surveillance
non-certification
not Sal-Meter
not CAIS compliance
not production-ready
```

---

## Prohibited language

Do not use:

```text
validated phone mediation system
clinical phone monitoring
diagnostic phone assistant
therapeutic phone agent
counseling service
production mediation service
real-time human monitoring
relationship verdict
human ranking
certified benchmark
validated benchmark
validated mediation
validated recovery
validated termination gate
Sal-Meter output
CAIS-compliant system
device-ready system
production-ready system
closed-loop intervention
```

---

## Public data boundary

This folder must not contain:

- raw human data;
- real phone recordings;
- real call transcripts;
- identifiable participant data;
- real consent records;
- private session logs;
- clinical notes;
- diagnostic labels;
- therapeutic recommendations;
- counseling notes;
- relationship verdicts;
- human scores;
- human-ranking outputs;
- raw Sal-Meter traces;
- raw CAIS traces;
- production intervention logs.

All examples must remain:

```text
synthetic
sample
mock
placeholder
structure-only
non-identifying
raw-data-free
public-helper-only
non-clinical
non-diagnostic
non-therapeutic
non-counseling
non-surveillance
non-certification
non-human-ranking
not Sal-Meter
not CAIS compliance
not benchmark evidence
not mediation evidence
not dyadic recovery evidence
not termination-gate accuracy evidence
not production data
```

---

## Relationship to P4-3

P4-3 created synthetic termination-gate helper cases.

This P4-4 folder extends that work into a public-safe phone-only simulator wireframe.

P4-3 asks whether synthetic termination-gate cases preserve expected helper consistency.

P4-4 asks how a synthetic phone-only session flow may be represented without creating real monitoring, real mediation, or production authority.

P4-4 does not validate P4-3.

P4-4 does not validate termination-gate accuracy.

P4-4 does not validate mediation.

P4-4 does not validate dyadic recovery.

P4-4 does not validate Sal-Meter.

P4-4 does not grant CAIS compliance.

---

## Final rule

The phone-only simulator is a map.

It is not the phone call.

It is not the person.

It is not the relationship.

It is not recovery.

It is not a termination-gate accuracy test.

It is not Sal-Meter.

It is not CAIS compliance.

It is not production authority.
