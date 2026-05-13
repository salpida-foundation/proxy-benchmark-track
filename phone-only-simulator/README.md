# Phone-only Simulator Boundary

This folder contains a bounded public-helper scaffold and minimal synthetic-only runnable demo for a phone-only session simulator.

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

The purpose of this folder is to demonstrate how a phone-only session may be represented as a public-safe simulator wireframe and minimal runnable synthetic demo.

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

The v0.1 runnable demo extension may show how one synthetic session object is loaded, processed, and converted into a bounded demo report.

It does not process real phone calls.

It does not process raw voice.

It does not process transcripts from real people.

It does not process identifiable human data.

It does not process clinical data.

It does not process Sal-Meter raw input.

It does not process CAIS compliance dossiers.

---

## Current folder role

This folder has two roles:

1. **Static public-helper scaffold**  
   Documentation and state-machine files that describe a synthetic phone-only session flow.

2. **v0.1 runnable synthetic demo**  
   A minimal Python-based helper demo that reads a synthetic session JSON object and generates or confirms a synthetic demo report.

Both roles remain public-helper-only.

Neither role creates validation, certification, clinical use, diagnostic use, therapeutic use, counseling use, surveillance use, Sal-Meter status, CAIS compliance, device readiness, production readiness, or production closed-loop authority.

---

## Current intended files

```text
phone-only-simulator/
  README.md
  session-flow-wireframe.md
  phone-session-state-machine.json
  sample-phone-session-script.md
  simulator_config.json
  synthetic_sessions/
    synthetic_phone_session_001.json
  run_demo.py
  demo_output/
    demo_report_001.json
```

| File | Role | Status |
|---|---|---|
| `README.md` | Folder-level boundary, usage notice, and runnable demo guide | Current file |
| `session-flow-wireframe.md` | Public-safe phone-only session flow wireframe | Existing scaffold |
| `phone-session-state-machine.json` | Synthetic state-machine mockup for session transitions | Existing scaffold |
| `sample-phone-session-script.md` | Synthetic sample phone-session script | Existing scaffold |
| `simulator_config.json` | Minimal configuration for the runnable synthetic demo | v0.1 demo file |
| `synthetic_sessions/synthetic_phone_session_001.json` | Synthetic-only input session object | v0.1 demo file |
| `run_demo.py` | Minimal deterministic demo runner | v0.1 demo file |
| `demo_output/demo_report_001.json` | Example bounded demo output report | v0.1 demo file |

---

## v0.1 Runnable Synthetic Demo Extension

Issue #44 extends this folder from a static public-helper scaffold into a minimal runnable synthetic-only demo.

The v0.1 demo should show how one synthetic phone-only mediation session can move through:

```text
synthetic session input
→ deterministic demo runner
→ recovery gate output
→ termination gate output
→ session closure
→ demo report
```

This runnable extension remains synthetic-only.

It does not use real participant data.

It does not use real phone recordings.

It does not use real call transcripts.

It does not use real session logs.

It does not validate mediation effectiveness.

It does not validate benchmark performance.

It does not validate scientific truth.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not create certification, device readiness, production readiness, or production closed-loop authority.

---

## How to run the v0.1 demo

From the repository root:

```bash
python phone-only-simulator/run_demo.py
```

Expected terminal behavior:

```text
SICS Human-State Proxy Benchmark Track
Phone-only synthetic mediation demo v0.1

Synthetic-only: true
Real participant data: false
Raw human data included: false

Session: synthetic_phone_session_001
Recovery gate: pass
Termination gate: pass
Session closure: closed

This demo is public-helper-only.
It is not validation.
```

The exact wording of the terminal output may change as the helper script evolves, but the boundary must not change.

---

## What the demo output means

The demo output means that a synthetic session object can be read, processed, and summarized through a bounded public-helper session flow.

The demo output may show:

- synthetic session ID;
- synthetic participant labels;
- synthetic AI output condition;
- synthetic overload delta;
- synthetic recovery delta;
- synthetic relational stability delta;
- synthetic recovery gate status;
- synthetic termination gate status;
- synthetic session closure status;
- synthetic demo report creation.

The demo output does not mean that mediation works.

The demo output does not mean that any AI output improves real human recovery.

The demo output does not mean that a real person, real relationship, real phone call, or real human state has been measured.

The demo output does not mean that the termination gate is accurate in the real world.

The demo output does not mean that dyadic recovery has been validated.

The demo output does not mean that the system is ready for clinical, counseling, therapeutic, surveillance, device, or production use.

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
- public-helper-only simulator posture;
- synthetic session input loading;
- synthetic demo report generation;
- deterministic helper-script behavior.

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
- a human-ranking system;
- benchmark validation;
- mediation effectiveness validation;
- dyadic recovery validation;
- termination-gate accuracy validation;
- Sal-Meter validation;
- CAIS compliance;
- certification;
- device readiness;
- production readiness.

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

## v0.1 runnable demo flow

The v0.1 runnable helper flow is:

```text
Load synthetic session JSON
↓
Confirm synthetic-only boundary flags
↓
Read synthetic state deltas
↓
Evaluate recovery gate helper rule
↓
Evaluate termination gate helper rule
↓
Confirm session closure state
↓
Write synthetic demo report
↓
Print public-helper summary
```

This flow is deterministic and synthetic.

It is not adaptive real-world mediation.

It is not live monitoring.

It is not real-time intervention.

It is not proof that an AI response caused recovery.

---

## Synthetic session requirements

The synthetic session input should include, at minimum:

- synthetic session ID;
- synthetic participant labels such as `person_a` and `person_b`;
- synthetic conflict scenario label;
- synthetic AI output condition;
- baseline summary values;
- post-output summary values;
- overload delta;
- recovery delta;
- relational stability delta;
- confidence score;
- data quality flag;
- raw data excluded flag;
- session closure flag;
- termination gate input.

The synthetic session must clearly state:

```text
synthetic_only = true
real_participant_data = false
raw_human_data_included = false
real_phone_recording_included = false
real_call_transcript_included = false
clinical_data_included = false
```

---

## Demo report requirements

The generated demo report should include:

- session ID;
- synthetic-only declaration;
- AI output condition;
- overload delta;
- recovery delta;
- relational stability delta;
- recovery gate status;
- termination gate status;
- session closure status;
- data quality flag;
- boundary statement.

The generated demo report must not include:

- real names;
- phone numbers;
- real recordings;
- real call transcripts;
- real session logs;
- clinical notes;
- diagnostic labels;
- therapeutic interpretation;
- counseling interpretation;
- surveillance language;
- Sal-Meter raw input;
- CAIS trace data;
- production intervention logs.

---

## State-machine boundary

The `phone-session-state-machine.json` file should represent synthetic states only.

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

## Recovery gate boundary

The recovery gate in this folder is a synthetic helper placeholder.

It may represent a public-helper rule such as:

```text
recovery_gate = pass
recovery_gate = hold
recovery_gate = fail
```

It must not be described as:

```text
validated recovery
real recovery
clinical recovery
therapeutic recovery
relationship repair
mental health improvement
mediation success
```

Correct boundary sentence:

```text
The recovery gate in this folder is a synthetic helper output only and does not validate real human recovery or mediation effectiveness.
```

---

## Termination gate boundary

The termination gate in this folder is a synthetic helper placeholder.

It may represent whether a synthetic session should be closed, paused, narrowed, or terminated within the helper flow.

It must not be described as:

```text
validated termination accuracy
real-world safety decision
clinical triage
therapeutic stopping rule
production intervention trigger
```

Correct boundary sentence:

```text
The termination gate in this folder is a synthetic helper output only and does not validate real-world termination-gate accuracy.
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
runnable synthetic demo
synthetic session input
deterministic demo runner
synthetic demo report
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
non-counseling
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

## Relationship to Issue #44

Issue #44 extends this folder toward a minimal runnable synthetic demo.

Issue #44 does not change the public-helper boundary.

Issue #44 does not convert this folder into validation.

Issue #44 does not create benchmark validation.

Issue #44 does not create mediation effectiveness validation.

Issue #44 does not create real phone monitoring.

Issue #44 does not create real session replay.

Issue #44 does not create Sal-Meter validation.

Issue #44 does not grant CAIS compliance.

Issue #44 does not create certification, device readiness, production readiness, or production closed-loop authority.

---

## Minimal v0.1 completion checklist

The v0.1 runnable demo is minimally complete when:

- [ ] `simulator_config.json` exists;
- [ ] `synthetic_sessions/synthetic_phone_session_001.json` exists;
- [ ] `run_demo.py` exists;
- [ ] `demo_output/demo_report_001.json` exists;
- [ ] `run_demo.py` can read the synthetic session input;
- [ ] `run_demo.py` can generate or confirm a demo report;
- [ ] demo report includes recovery gate and termination gate status;
- [ ] demo report includes session closure status;
- [ ] all demo files remain synthetic-only;
- [ ] no real participant data is added;
- [ ] no real phone recordings are added;
- [ ] no real call transcripts are added;
- [ ] no real session logs are added;
- [ ] no clinical, diagnostic, therapeutic, counseling, or surveillance claim is introduced;
- [ ] no Sal-Meter validation claim is introduced;
- [ ] no CAIS compliance claim is introduced;
- [ ] no benchmark validation claim is introduced;
- [ ] no mediation effectiveness validation claim is introduced;
- [ ] no production authority claim is introduced.

---

## Future optional extensions

Optional future helper extensions may include:

- a small test file for `run_demo.py`;
- a GitHub Actions workflow that runs the demo script;
- additional synthetic sessions;
- additional synthetic AI output conditions;
- additional demo reports;
- schema alignment with existing public helper schemas.

These optional extensions must remain synthetic-only and public-helper-only.

They must not introduce real participant data, raw human data, real phone recordings, real call transcripts, real session logs, clinical data, diagnostic interpretation, therapeutic interpretation, counseling interpretation, surveillance capability, Sal-Meter validation, CAIS compliance, certification, device readiness, production readiness, or production closed-loop authority.

---

## Final rule

The phone-only simulator is a map.

It is not the phone call.

It is not the person.

It is not the relationship.

It is not recovery.

It is not a termination-gate accuracy test.

It is not benchmark validation.

It is not mediation validation.

It is not Sal-Meter.

It is not CAIS compliance.

It is not production authority.

Raw human data must not enter the public repository.

A closed session must stay closed.
