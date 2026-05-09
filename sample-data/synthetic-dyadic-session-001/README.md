# Synthetic Dyadic Session 001

This folder contains a public synthetic/sample dyadic helper package for the **SICS Human-State Proxy Benchmark Track**.

It is provided for P3 helper-schema structure demonstration and P4-0 synthetic dyadic demo-flow illustration only.

It is not benchmark validation.

It is not scientific validation.

It is not Sal-Meter validation.

It is not CAIS compliance.

It is not mediation validation.

It does not contain raw human data.

It does not contain identifiable human data.

It does not contain clinical data.

It does not contain Sal-Meter input.

It does not contain CAIS compliance dossiers.

It does not create diagnostic, therapeutic, clinical, counseling, surveillance, employment, insurance, educational, legal, eligibility, certification, device-readiness, production-deployment, mediation-service, or human-ranking authority.

---

## Purpose

This package demonstrates a synthetic public-helper structure for the P3 dyadic benchmark scaffold and the P4-0 synthetic dyadic demo chain.

The P3 helper scaffold is:

```text
Human-State Packet A
Human-State Packet B
Dyadic Session Event
Benchmark Session Container
```

The P4-0 synthetic dyadic demo chain is:

```text
AI Output
→ Human-State Packet A/B
→ Dyadic Delta
→ Recovery Gate
→ Termination Gate
→ Audit Log
```

The package is designed to support bounded helper-schema and demo-flow illustration for:

- Human-State Packet structure;
- dyadic event structure;
- benchmark session container structure;
- synthetic AI output object structure;
- synthetic dyadic delta object structure;
- synthetic recovery gate object structure;
- synthetic termination gate object structure;
- synthetic audit log object structure;
- synthetic/sample status declaration;
- raw human data exclusion;
- identifiable data exclusion;
- clinical data exclusion;
- Sal-Meter input exclusion;
- CAIS compliance claim exclusion;
- benchmark validation claim exclusion;
- mediation validation claim exclusion;
- production closed-loop claim exclusion.

This package is not evidence.

This package is not a real dyadic session.

This package is not a human-state dataset.

This package is not a Sal-Meter dataset.

This package is not a CAIS-compliant output.

This package is not a mediation result.

This package is not a production closed-loop intervention.

---

## Folder contents

```text
sample-data/
  synthetic-dyadic-session-001/
    README.md
    human_state_packet_A.json
    human_state_packet_B.json
    dyadic_session_event.json
    benchmark_session_container.json
    ai_outputs.json
    dyadic_delta.json
    recovery_gate.json
    termination_gate.json
    audit_log.json
```

---

## File roles

| File | Role | Boundary |
|---|---|---|
| `README.md` | Local package boundary and usage explanation | Public helper documentation only |
| `human_state_packet_A.json` | Synthetic Human-State Packet for participant A | No raw human data, no identity data, no diagnosis, no Sal-Meter input |
| `human_state_packet_B.json` | Synthetic Human-State Packet for participant B | No raw human data, no identity data, no diagnosis, no Sal-Meter input |
| `dyadic_session_event.json` | Synthetic dyadic event object | No relationship verdict, no blame assignment, no mediation validation |
| `benchmark_session_container.json` | Synthetic benchmark session container | Not benchmark validation, not scientific validation, not CAIS compliance |
| `ai_outputs.json` | Synthetic AI output examples | Mock AI outputs only, no real conversation, no private user content |
| `dyadic_delta.json` | Synthetic dyadic delta object | Structure-only delta summary, not recovery evidence |
| `recovery_gate.json` | Synthetic recovery gate object | Prevents false recovery in demo flow, not mediation validation |
| `termination_gate.json` | Synthetic termination gate object | Demonstrates pause/close logic, not production intervention |
| `audit_log.json` | Synthetic audit log object | Demonstrates traceability of the demo chain, not certification |

---

## P3 helper chain

The P3 helper chain is:

```text
Human-State Packet A
+
Human-State Packet B
↓
Dyadic Session Event
↓
Benchmark Session Container
```

This chain demonstrates structure only.

It does not prove that a real dyadic recovery occurred.

It does not prove that an AI mediation output worked.

It does not prove human-state measurement.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

---

## P4-0 synthetic dyadic demo flow

The P4-0 demo flow illustrates how synthetic helper objects can be linked into a public-safe dyadic mediation-style chain:

```text
AI Output
→ Human-State Delta A/B
→ Dyadic Delta
→ Recovery Gate
→ Termination Gate
→ Audit Log
```

This flow is represented by:

```text
ai_outputs.json
dyadic_delta.json
recovery_gate.json
termination_gate.json
audit_log.json
```

The intended interpretation is:

```text
Synthetic AI output is generated.
Synthetic participant packet summaries are referenced.
Synthetic dyadic delta is observed.
Recovery gate prevents false recovery.
Termination gate pauses or closes the session.
Audit log records the helper chain.
```

This is a demo-flow scaffold only.

It is not benchmark validation.

It is not scientific validation.

It is not mediation validation.

It is not Sal-Meter validation.

It is not CAIS compliance.

It is not a production closed-loop intervention.

It does not process raw human data.

It does not process identifiable human data.

It does not process clinical data.

---

## P4-0 demo object chain

The P4-0 object chain is:

```text
ai_outputs.json
  → dyadic_delta.json
  → recovery_gate.json
  → termination_gate.json
  → audit_log.json
```

Reference relationship:

```text
ai_outputs.json
  contains:
    synthetic_ai_output_001
    synthetic_ai_output_002
    synthetic_ai_output_003

dyadic_delta.json
  references:
    synthetic_ai_output_002
    hsp_synthetic_A_001
    hsp_synthetic_B_001
    DSE-SYNTHETIC-001
    BMS-SYNTHETIC-001

recovery_gate.json
  references:
    synthetic_ai_output_002
    synthetic_ai_output_003
    synthetic_dyadic_delta_001
    synthetic_recovery_gate_001
    DSE-SYNTHETIC-001
    BMS-SYNTHETIC-001

termination_gate.json
  references:
    synthetic_ai_output_003
    synthetic_dyadic_delta_001
    synthetic_recovery_gate_001
    synthetic_termination_gate_001
    synthetic_closure_001
    DSE-SYNTHETIC-001
    BMS-SYNTHETIC-001

audit_log.json
  references:
    hsp_synthetic_A_001
    hsp_synthetic_B_001
    synthetic_ai_output_002
    synthetic_dyadic_delta_001
    synthetic_recovery_gate_001
    synthetic_termination_gate_001
    synthetic_closure_001
    DSE-SYNTHETIC-001
    BMS-SYNTHETIC-001
```

This reference chain demonstrates auditability.

It does not demonstrate scientific proof.

It does not demonstrate benchmark success.

It does not demonstrate mediation effectiveness.

It does not demonstrate Sal-Meter validation.

It does not demonstrate CAIS compliance.

---

## P4-0 demo flow interpretation

The synthetic demo illustrates a failure-sensitive dyadic pattern:

```text
Participant A moves toward recovery.
Participant B remains reduced in engagement.
Dyadic recovery is not confirmed.
Recovery Gate does not pass.
Termination Gate recommends pause and closure.
Audit Log records the closure.
```

Correct interpretation:

```text
The demo chain shows why one-sided improvement should not be treated as dyadic recovery.
```

Incorrect interpretation:

```text
The AI mediated the conflict successfully.
The dyad recovered.
The relationship was resolved.
The benchmark is validated.
The mediation system is validated.
The repository is Sal-Meter.
The repository is CAIS-compliant.
```

---

## Schema alignment

This package is intended to align with the following helper schemas:

```text
schemas/human_state_packet.schema.json
schemas/dyadic_session_event.schema.json
schemas/benchmark_session.schema.json
```

Expected P3 validation mapping:

```text
human_state_packet_A.json
  → schemas/human_state_packet.schema.json

human_state_packet_B.json
  → schemas/human_state_packet.schema.json

dyadic_session_event.json
  → schemas/dyadic_session_event.schema.json

benchmark_session_container.json
  → schemas/benchmark_session.schema.json
```

These schemas validate helper structure only.

They do not validate benchmark performance.

They do not validate scientific truth.

They do not validate human-state measurement.

They do not validate mediation effectiveness.

They do not validate Sal-Meter.

They do not grant CAIS compliance.

---

## P4-0 demo files and schema boundary

The following P4-0 demo files are public-safe synthetic helper objects:

```text
ai_outputs.json
dyadic_delta.json
recovery_gate.json
termination_gate.json
audit_log.json
```

Unless and until dedicated schemas are added for these files, they should be interpreted as demo-flow helper objects.

They are not P3 schema compliance objects.

They are not benchmark validation objects.

They are not scientific validation objects.

They are not mediation validation objects.

They are not production intervention objects.

They are subject to public boundary review and boundary language linting.

---

## Synthetic status

All files in this folder must remain synthetic/sample/helper material only.

Required public posture:

```text
dataset_type: synthetic / sample / mock / placeholder / structure_only
synthetic_status: synthetic_only / sample_only / mock_only / placeholder_only / structure_only / not_real_human_data
raw human data: absent
identifiable data: absent
clinical data: absent
Sal-Meter input: absent
CAIS compliance dossier: absent
benchmark validation claim: absent
mediation validation claim: absent
production intervention claim: absent
```

If any future file cannot satisfy this boundary, it does not belong in this public repository.

---

## Human-State Packet boundary

The Human-State Packet files are summary objects only.

They are not:

- the body;
- the raw signal;
- the raw voice;
- the raw face;
- the raw gaze stream;
- the raw video;
- the raw transcript;
- a diagnosis;
- a therapy label;
- a psychiatric label;
- a clinical state;
- a human score;
- a truth score;
- a trust score;
- a guilt score;
- a morality score;
- a psychological safety score;
- an employee risk score;
- a relationship verdict;
- a fault assignment;
- a Sal-Meter trace;
- a CAIS compliance record;
- a certification record.

Correct boundary sentence:

```text
A Human-State Packet is a consent-bound, session-scoped, expiring state-summary helper object for interaction adjustment only.
```

---

## AI Output boundary

The AI output file contains synthetic mock AI outputs only.

It may include:

- synthetic AI output ID;
- mock output text;
- output condition;
- output stage;
- output visibility;
- intended helper function;
- synthetic observation window;
- linked synthetic packet references;
- linked synthetic event references;
- boundary flags.

It must not include:

- real user conversation;
- private user statements;
- identifiable participant data;
- clinical interpretation;
- diagnosis;
- therapy;
- counseling instruction;
- legal mediation decision;
- relationship verdict;
- production intervention instruction;
- surveillance instruction;
- human ranking;
- Sal-Meter output;
- CAIS compliance claim.

Correct boundary sentence:

```text
A synthetic AI output is a mock stimulus for helper-flow demonstration only.
```

---

## Dyadic Delta boundary

The Dyadic Delta file represents synthetic change between two bounded packet summaries.

It may include:

- participant A synthetic delta;
- participant B synthetic delta;
- dyadic direction;
- recovery asymmetry;
- one-sided improvement flag;
- false recovery risk;
- silence risk;
- private state exposure risk;
- recommended next gate.

It must not include:

- real physiological inference;
- real psychological inference;
- clinical interpretation;
- emotion detection;
- diagnosis;
- therapy recommendation;
- relationship verdict;
- human score;
- blame assignment;
- legal conclusion;
- benchmark validation claim;
- mediation validation claim.

Correct boundary sentence:

```text
A Dyadic Delta summarizes synthetic helper-state movement; it is not proof of recovery.
```

---

## Dyadic Session Event boundary

The Dyadic Session Event file represents a synthetic event in a bounded dyadic session.

It may describe:

- consent status;
- packet availability;
- permission status;
- private cue status;
- shared output status;
- participant A bounded state-summary delta;
- participant B bounded state-summary delta;
- dyadic delta;
- recovery gate decision;
- termination gate decision;
- closure reason;
- audit reference.

It must not describe:

- who is right;
- who is wrong;
- who is guilty;
- who is unsafe;
- who is morally better;
- who should be punished;
- who should be ranked;
- who should be monitored;
- who should be diagnosed;
- who should receive therapy;
- a legal mediation decision;
- a relationship verdict;
- a clinical interpretation;
- a production intervention.

Correct boundary sentence:

```text
A Dyadic Session Event describes bounded synthetic session structure, not human truth or relationship judgment.
```

---

## Recovery Gate boundary

The Recovery Gate file represents a synthetic decision point.

It may include:

- recovery gate status;
- participant A recovery check;
- participant B recovery check;
- dyadic recovery check;
- false recovery check;
- silence check;
- private state exposure check;
- consent scope check;
- packet permission check;
- data quality check;
- recommended next action.

It must not include:

- declaration that the dyad truly recovered;
- clinical decision;
- therapeutic decision;
- counseling decision;
- relationship verdict;
- human ranking;
- proof that mediation worked;
- benchmark validation;
- Sal-Meter validation;
- CAIS compliance.

Correct boundary sentence:

```text
A Recovery Gate prevents false recovery; it does not prove recovery.
```

---

## Termination Gate boundary

The Termination Gate file represents a synthetic pause/stop/close decision point.

It may include:

- termination gate status;
- consent withdrawal check;
- permission expiry check;
- data quality check;
- recovery uncertainty check;
- one-sided improvement check;
- silence misread check;
- overstay check;
- auditability check;
- closure packet.

It must not include:

- production intervention authority;
- automated real-world stop instruction;
- clinical stop instruction;
- therapeutic stop instruction;
- legal mediation authority;
- surveillance control;
- relationship verdict;
- human ranking;
- benchmark validation;
- mediation validation.

Correct boundary sentence:

```text
A Termination Gate protects closure; it is not production control.
```

---

## Audit Log boundary

The Audit Log file records the synthetic helper-chain trace.

It may include:

- session start;
- packet availability;
- AI output recorded;
- dyadic delta recorded;
- recovery gate review;
- termination gate review;
- session closure;
- object references;
- boundary checks;
- audit findings.

It must not include:

- real session logs;
- private participant data;
- raw conversation;
- raw audio;
- raw video;
- raw biosignals;
- clinical records;
- legal records;
- production logs;
- certification records;
- relationship verdicts;
- human rankings.

Correct boundary sentence:

```text
An Audit Log records synthetic helper-chain traceability; it is not certification.
```

---

## Benchmark Session Container boundary

The Benchmark Session Container connects synthetic packets and events into one public-safe helper package.

It may declare:

- benchmark session ID;
- session ID;
- synthetic status;
- helper benchmark scope;
- helper benchmark stage;
- session type;
- modality stack;
- event schema reference;
- session event references;
- baseline suite status;
- primary helper outcome;
- human-state delta summary;
- dyadic delta summary;
- recovery gate summary;
- termination gate summary;
- leakage review status;
- holdout strategy;
- data boundary status;
- consent boundary status;
- sharing boundary status;
- audit status;
- public release status;
- authority status;
- boundary flags;
- final boundary status.

It must not declare:

- benchmark validation;
- scientific validation;
- Sal-Meter validation;
- CAIS compliance;
- mediation validation;
- clinical readiness;
- diagnostic readiness;
- therapeutic readiness;
- counseling readiness;
- surveillance readiness;
- certification readiness;
- device readiness;
- production readiness.

Correct boundary sentence:

```text
A Benchmark Session Container demonstrates helper structure only; it is not benchmark evidence.
```

---

## Public data boundary

This folder may include:

- synthetic JSON examples;
- sample helper structures;
- mock state-summary fields;
- synthetic AI output examples;
- synthetic dyadic delta examples;
- synthetic recovery gate examples;
- synthetic termination gate examples;
- synthetic audit log examples;
- synthetic event references;
- synthetic audit references;
- public boundary declarations;
- schema-aligned helper objects.

This folder must not include:

- raw human data;
- identifiable human data;
- private participant data;
- real dyadic conflict records;
- private consent records;
- raw biosignal files;
- raw ECG;
- raw EEG;
- raw EDA;
- raw PPG;
- raw video;
- raw audio;
- raw face data;
- raw voice data;
- raw gaze streams;
- raw transcripts;
- clinical records;
- diagnostic labels;
- therapeutic interpretations;
- counseling interpretations;
- legal mediation decisions;
- employment eligibility decisions;
- insurance eligibility decisions;
- educational eligibility decisions;
- legal eligibility decisions;
- Sal-Meter raw input;
- CAIS compliance dossiers;
- production feedback logs.

---

## Required boundary flags

Each synthetic helper object should preserve boundary flags equivalent to:

```text
raw_human_data_present == false
identifiable_data_present == false
clinical_data_present == false
diagnostic_claim_present == false
therapeutic_claim_present == false
counseling_claim_present == false
surveillance_claim_present == false
sal_meter_validation_claim_present == false
cais_compliance_claim_present == false
benchmark_validation_claim_present == false
scientific_validation_claim_present == false
mediation_validation_claim_present == false
production_intervention_claim_present == false
human_ranking_claim_present == false
relationship_verdict_present == false
synthetic_public_data_confirmed == true
```

---

## Validation

The P3 helper-schema validator is provided at:

```text
evaluation-baseline/validate_p3_schemas.py
```

Expected validation role:

```text
Validate P3 helper-schema structure only.
```

Expected P3 validation targets:

```text
sample-data/synthetic-dyadic-session-001/human_state_packet_A.json
sample-data/synthetic-dyadic-session-001/human_state_packet_B.json
sample-data/synthetic-dyadic-session-001/dyadic_session_event.json
sample-data/synthetic-dyadic-session-001/benchmark_session_container.json
```

Expected schemas:

```text
schemas/human_state_packet.schema.json
schemas/dyadic_session_event.schema.json
schemas/benchmark_session.schema.json
```

A successful P3 helper-schema validation means only:

```text
The synthetic P3 helper files follow the expected public helper schema structure.
```

A successful P3 helper-schema validation does not mean:

```text
The benchmark is validated.
The science is validated.
The mediation system works.
The dyadic recovery is real.
The repository is Sal-Meter.
The repository is CAIS-compliant.
The package is clinical.
The package is diagnostic.
The package is therapeutic.
The package is certified.
The package is device-ready.
The package is production-ready.
```

---

## P4-0 demo-flow validation boundary

The P4-0 files currently demonstrate public-safe demo-flow structure.

```text
ai_outputs.json
dyadic_delta.json
recovery_gate.json
termination_gate.json
audit_log.json
```

They may be checked by:

```text
boundary_lint.py
manual JSON review
future demo-flow validator
```

Until a dedicated demo-flow validator is added, these files should not be described as validated.

They are synthetic helper examples only.

---

## Naming rule

Use:

```text
synthetic
sample
mock
placeholder
structure_only
public helper
helper-schema validation
demo-flow illustration
research-stage
non-clinical
non-diagnostic
non-therapeutic
non-counseling
non-surveillance
non-certification
non-human-ranking
not Sal-Meter
not CAIS compliance
not benchmark validation
not mediation validation
no raw human data
```

Do not use:

```text
validated proxy benchmark
validated human-state benchmark
validated mediation benchmark
validated dyadic recovery system
CAIS-compliant proxy release
Sal-Meter validated
certified proxy benchmark
production mediation system
validated closed-loop intervention
emotion-reading AI
employee monitoring AI
student monitoring AI
relationship scoring system
human quality score
human ranking system
AI harm detector
human-state detector
clinical stress system
diagnostic stress system
therapeutic feedback system
psychological safety score
insurance risk score
legal eligibility score
educational eligibility score
```

---

## Relation to existing synthetic sample package

This folder is separate from:

```text
sample-data/synthetic-session-001/
```

The existing `synthetic-session-001` package demonstrates a single synthetic session package using CSV/JSON helper files.

This folder demonstrates a P3/P4-0 dyadic helper package using schema-aligned JSON objects and demo-flow JSON objects.

The two folders should not be merged.

They serve different helper purposes.

---

## Authority rule

This folder is a GitHub helper surface.

It is not a canonical authority layer.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this folder conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

---

## Current status

```text
Synthetic dyadic helper package.
P3 helper-schema structure demonstration.
P4-0 synthetic dyadic demo-flow illustration.
Not benchmark evidence.
Not scientific validation.
Not mediation validation.
Not Sal-Meter.
Not CAIS compliance.
No raw human data.
No identifiable data.
No clinical data.
No diagnostic label.
No therapeutic claim.
No certification claim.
No production closed-loop claim.
```

Current P3 files:

```text
human_state_packet_A.json
human_state_packet_B.json
dyadic_session_event.json
benchmark_session_container.json
```

Current P4-0 demo files:

```text
ai_outputs.json
dyadic_delta.json
recovery_gate.json
termination_gate.json
audit_log.json
```

---

## Final rule

This package demonstrates structure.

It does not disclose human data.

It does not prove benchmark performance.

It does not validate mediation.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not create diagnostic, therapeutic, clinical, counseling, surveillance, employment, insurance, educational, legal, eligibility, certification, device-readiness, production-deployment, mediation-service, or human-ranking authority.

The packet is not the person.

The AI output is not the truth.

The delta is not proof.

The gate is not therapy.

The audit log is not certification.

The event is not the relationship.

The container is not the truth.

The structure is a map.

It is not the mountain.
