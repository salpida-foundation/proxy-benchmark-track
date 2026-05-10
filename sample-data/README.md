# Sample Data Boundary

This folder is reserved for public synthetic, toy, mock, placeholder, or non-identifying sample-structure data only.

No raw human data belongs in this repository.

This folder exists to demonstrate file structure, metadata discipline, schema alignment, helper-schema validation, leakage awareness, demo-flow consistency, and public release boundaries for the **SICS Human-State Proxy Benchmark Track**.

It does not provide benchmark evidence.

It does not validate scientific truth.

It does not validate mediation effectiveness.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not create clinical, diagnostic, therapeutic, counseling, surveillance, employment, insurance, educational, legal, eligibility, certification, device-readiness, production-deployment, mediation-service, or human-ranking authority.

---

## Scope

This folder may contain public sample packages that demonstrate:

- synthetic session structure;
- synthetic dyadic session structure;
- synthetic event markers;
- synthetic metadata examples;
- synthetic stream manifests;
- synthetic label windows;
- synthetic QC reports;
- toy feature tables;
- split-file examples;
- operator-log examples;
- Human-State Packet helper examples;
- Dyadic Session Event helper examples;
- Benchmark Session Container helper examples;
- P4-0 synthetic dyadic demo-flow objects;
- P4-1 synthetic dyadic recovery demo-flow evaluation inputs;
- schema demonstration files;
- generated examples for notebooks;
- non-identifying mock data;
- public helper files for structure demonstration.

The purpose is structure demonstration.

The purpose is not scientific proof.

The purpose is not benchmark validation.

The purpose is not mediation validation.

The purpose is not Sal-Meter validation.

The purpose is not CAIS compliance.

---

## Current sample packages

Current public sample packages:

```text
sample-data/
  README.md

  synthetic-session-001/
    README.md
    session_metadata.json
    streams_manifest.csv
    events.csv
    labels.csv
    qc_report.json
    features_baseline.csv
    splits.json
    operator_log.md

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

## Package roles

| Folder | Role | Boundary |
|---|---|---|
| `synthetic-session-001/` | Original public synthetic/sample package for session metadata, streams, events, labels, QC, features, splits, and operator log | Structure demonstration only |
| `synthetic-dyadic-session-001/` | P5-1 / P3 synthetic dyadic helper package for Human-State Packet A/B, Dyadic Session Event, and Benchmark Session Container | Helper-schema validation only |
| `synthetic-dyadic-session-001/` | P4-0 / P4-1 synthetic dyadic demo-flow package for AI Output, Dyadic Delta, Recovery Gate, Termination Gate, and Audit Log | Synthetic demo-flow consistency only |

These packages are synthetic.

They are not real human data.

They are not clinical data.

They are not Sal-Meter data.

They are not CAIS-compliance output.

They are not benchmark evidence.

They are not mediation evidence.

They are not production data.

---

## `synthetic-session-001/`

This package demonstrates a minimal public helper package using mixed CSV and JSON helper files.

It is intended to show:

- session-level metadata structure;
- stream inventory structure;
- event marker structure;
- label window structure;
- synthetic baseline feature structure;
- QC report structure;
- split definition structure;
- operator log structure;
- public/private data boundary language;
- leakage-risk awareness;
- helper-structure validation readiness.

Current file map:

```text
sample-data/
  synthetic-session-001/
    README.md
    session_metadata.json
    streams_manifest.csv
    events.csv
    labels.csv
    qc_report.json
    features_baseline.csv
    splits.json
    operator_log.md
```

This package is checked by:

```text
evaluation-baseline/validate_sample_package.py
```

A successful validation means only:

```text
The public synthetic/sample package follows the expected helper structure.
```

It does not mean:

```text
The benchmark is validated.
The science is validated.
The model is reliable.
The system is diagnostic.
The system is Sal-Meter.
The system is CAIS-compliant.
```

---

## `synthetic-dyadic-session-001/`

This package contains two public-safe synthetic layers:

```text
P3 helper-schema objects
P4-0 / P4-1 synthetic demo-flow objects
```

Both layers are synthetic.

Both layers are helper-only.

Neither layer is benchmark evidence.

Neither layer is scientific validation.

Neither layer is mediation validation.

Neither layer is Sal-Meter validation.

Neither layer grants CAIS compliance.

---

## P3 helper-schema layer

The P3 helper-schema layer demonstrates schema-aligned JSON objects.

It is intended to show:

```text
Human-State Packet A
+
Human-State Packet B
↓
Dyadic Session Event
↓
Benchmark Session Container
```

Current P3 file map:

```text
sample-data/
  synthetic-dyadic-session-001/
    README.md
    human_state_packet_A.json
    human_state_packet_B.json
    dyadic_session_event.json
    benchmark_session_container.json
```

This package is checked by:

```text
evaluation-baseline/validate_p3_schemas.py
```

Expected schema mapping:

```text
human_state_packet_A.json
  -> schemas/human_state_packet.schema.json

human_state_packet_B.json
  -> schemas/human_state_packet.schema.json

dyadic_session_event.json
  -> schemas/dyadic_session_event.schema.json

benchmark_session_container.json
  -> schemas/benchmark_session.schema.json
```

A successful P3 helper-schema validation means only:

```text
The public synthetic/sample P3 helper files follow the expected helper-schema structure.
```

It does not mean:

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

## P4-0 / P4-1 synthetic demo-flow layer

The P4-0 / P4-1 layer demonstrates a bounded synthetic dyadic recovery demo-flow.

It is intended to show:

```text
AI Output
↓
Human-State Packet A/B
↓
Dyadic Delta
↓
Recovery Gate
↓
Termination Gate
↓
Audit Log
```

Current P4-0 / P4-1 file map:

```text
sample-data/
  synthetic-dyadic-session-001/
    ai_outputs.json
    dyadic_delta.json
    recovery_gate.json
    termination_gate.json
    audit_log.json
```

This package is checked by:

```text
evaluation-baseline/evaluate_dyadic_recovery_demo.py
```

A successful P4-1 synthetic dyadic recovery demo-flow evaluation means only:

```text
The synthetic dyadic demo-flow objects are internally consistent enough for public helper demonstration.
```

It does not mean:

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

Current synthetic demo result posture:

```text
dyadic recovery confirmed: false
one-sided improvement: true
recovery gate: not_passed
termination gate: pause_and_close_session
audit state: closed
false recovery prevention: active
public boundary: preserved
```

This result is a synthetic demo-flow consistency signal only.

It is not benchmark validation.

It is not scientific validation.

It is not mediation validation.

It is not Sal-Meter validation.

It is not CAIS compliance.

---

## Allowed here

Allowed materials:

- synthetic session examples;
- synthetic dyadic session examples;
- synthetic event markers;
- synthetic metadata examples;
- synthetic stream manifests;
- synthetic label windows;
- synthetic QC reports;
- toy feature tables;
- synthetic split definitions;
- operator-log examples without human identifiers;
- Human-State Packet helper examples;
- Dyadic Session Event helper examples;
- Benchmark Session Container helper examples;
- P4-0 synthetic demo-flow examples;
- AI Output helper examples;
- Dyadic Delta helper examples;
- Recovery Gate helper examples;
- Termination Gate helper examples;
- Audit Log helper examples;
- schema demonstration files;
- non-identifying mock data;
- generated examples for notebooks;
- public helper files for structure demonstration.

---

## Not allowed here

Do not upload:

- raw human biosignals;
- raw human video;
- raw human audio;
- raw human face data;
- raw human voice data;
- raw gaze streams;
- raw transcripts;
- webcam recordings;
- identifiable participant metadata;
- participant identity mapping files;
- private session logs;
- private consent records;
- consent forms containing personal information;
- health records;
- clinical records;
- diagnostic labels;
- therapeutic recommendations;
- counseling notes;
- legal mediation conclusions;
- relationship verdicts;
- blame assignments;
- human scores;
- psychological safety scores;
- employment monitoring scores;
- insurance eligibility scores;
- educational eligibility scores;
- legal eligibility scores;
- private lab packages;
- unpublished human-subject files;
- Sal-Meter input data;
- raw Sal-Meter traces;
- raw CAIS traces;
- CAIS compliance claims;
- Sal-Meter validation claims;
- benchmark validation claims;
- mediation validation claims;
- certification claims;
- production closed-loop claims.

---

## Public release rule

Before any file is added to this folder, confirm:

```text
raw_human_data_present == false
identifiable_data_present == false
clinical_data_present == false
sal_meter_input_present == false
cais_compliance_claim_present == false
benchmark_validation_claim_present == false
mediation_validation_claim_present == false
production_intervention_claim_present == false
human_ranking_claim_present == false
relationship_verdict_present == false
```

If any of the above cannot be confirmed, the file does not belong in this public repository.

---

## Required note inside sample files

Every sample file should clearly indicate whether it is:

```text
synthetic
sample
sample_structure_only
toy
mock
placeholder
structure_only
synthetic_only
demo_flow_only
helper_only
```

Avoid filenames, folder names, row IDs, or metadata values that could be mistaken for real participant data.

Avoid hidden label leakage through:

- filenames;
- folder names;
- device IDs;
- operator IDs;
- condition names;
- row ordering;
- session ordering;
- preprocessing artifacts.

A public sample file should demonstrate structure without creating false evidence.

---

## Relationship to schemas

The original sample files in `synthetic-session-001/` should align with the public helper schemas in:

```text
schemas/
  session-metadata.schema.json
  streams-manifest.schema.json
  event-markers.schema.json
  labels.schema.json
  qc-report.schema.json
  features-baseline.schema.json
  splits.schema.json
```

The P5-1 / P3 dyadic helper files in `synthetic-dyadic-session-001/` should align with:

```text
schemas/
  human_state_packet.schema.json
  dyadic_session_event.schema.json
  benchmark_session.schema.json
```

The P4-0 / P4-1 synthetic demo-flow files are checked by the evaluator:

```text
evaluation-baseline/evaluate_dyadic_recovery_demo.py
```

Schema alignment means:

```text
The file follows the expected helper structure.
```

Demo-flow evaluator alignment means:

```text
The synthetic demo-flow objects preserve expected helper consistency and boundary logic.
```

Schema or evaluator alignment does not mean:

```text
The data is real evidence.
The benchmark is validated.
The model is reliable.
The mediation system works.
The dyadic recovery is real.
The system is diagnostic.
The system is Sal-Meter.
The system is CAIS-compliant.
```

---

## Validation

Current validation helpers:

```text
evaluation-baseline/validate_sample_package.py
evaluation-baseline/validate_p3_schemas.py
evaluation-baseline/evaluate_dyadic_recovery_demo.py
evaluation-baseline/boundary_lint.py
```

Intended workflow posture:

```text
Run existing synthetic sample package validator.
Run P3 helper schema validator.
Run P4 synthetic dyadic recovery demo-flow evaluator.
Run boundary language lint.
```

These checks are repository hygiene helpers.

They are not benchmark validators.

They are not scientific validators.

They are not Sal-Meter validators.

They are not CAIS compliance validators.

They are not mediation validators.

They do not create clinical, diagnostic, therapeutic, counseling, surveillance, certification, device-readiness, production-deployment, or human-ranking authority.

---

## Human-State Packet boundary

A Human-State Packet example in this folder is a bounded public helper object.

It is not:

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

## Dyadic Session Event boundary

A Dyadic Session Event example in this folder is a bounded public helper object.

It may describe:

- consent status;
- permission status;
- packet status;
- sharing scope;
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

## Benchmark Session Container boundary

A Benchmark Session Container example in this folder is a public-safe synthetic/sample helper object.

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

## P4-1 dyadic recovery demo boundary

A P4-1 synthetic dyadic recovery demo result in this folder is a bounded public helper result.

It may describe:

- AI output helper structure;
- synthetic dyadic delta summary;
- one-sided improvement;
- false recovery prevention;
- recovery gate status;
- termination gate status;
- audit closure status;
- public boundary preservation.

It must not describe:

- real dyadic recovery;
- validated mediation;
- benchmark validation;
- scientific validation;
- Sal-Meter validation;
- CAIS compliance;
- clinical usefulness;
- diagnostic readiness;
- therapeutic readiness;
- device readiness;
- production readiness;
- relationship verdict;
- human ranking.

Correct boundary sentence:

```text
A P4-1 evaluator result is a synthetic demo-flow consistency signal, not benchmark evidence.
```

---

## Human-State Cost proxy boundary

Synthetic sample files may include Human-State Cost only as a non-diagnostic benchmark construct or synthetic/example field.

It must not be presented as:

- a medical score;
- a psychiatric score;
- a clinical score;
- a consciousness score;
- a psychological safety score;
- an employee monitoring score;
- a student ranking score;
- an insurance risk score;
- a legal eligibility score;
- a user dependence diagnosis;
- a human-ranking measure;
- a certified benchmark output;
- a Sal-Meter output;
- a CAIS output.

Permitted interpretation:

```text
This field demonstrates how a non-diagnostic benchmark construct may be represented in a synthetic helper structure.
```

Prohibited interpretation:

```text
This field measures or diagnoses the true physiological, psychological, clinical, or consciousness state of a person.
```

Correct boundary sentence:

```text
Human-State Cost evaluates the interaction condition, not the person.
```

---

## Leakage caution

Even synthetic files should not teach bad benchmark habits.

Avoid:

- labels hidden in filenames;
- labels hidden in folder names;
- labels hidden in device IDs;
- labels hidden in operator IDs;
- session order that trivially reveals condition;
- public files that imply real physiological evidence;
- synthetic labels presented as scientific truth.

A real benchmark package must enforce leakage-safe rules across:

- participant;
- day;
- device;
- session;
- condition;
- operator;
- preprocessing pipeline;
- train/validation/test split.

This folder should therefore be read as:

```text
A demonstration of public helper structure.
```

It should not be read as:

```text
A benchmark dataset.
A validated model input.
A scientific result.
A Sal-Meter validation package.
A CAIS-compliant package.
```

---

## Boundary language

Use:

```text
synthetic sample package
sample structure demonstration
toy example
mock data
public helper file
non-identifying example
schema demonstration
helper-schema validation
synthetic demo-flow consistency
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
validated dataset
clinical dataset
diagnostic dataset
real participant dataset
Sal-Meter dataset
CAIS-compliant dataset
certified benchmark dataset
validated mediation dataset
validated dyadic recovery dataset
human-state diagnosis
psychological safety score
consciousness measurement
emotion-reading AI
relationship scoring system
human quality score
human ranking system
AI harm detector
production-ready human-state AI
```

---

## Naming convention

Suggested naming:

```text
synthetic-session-example.csv
synthetic-event-markers.csv
synthetic-metadata-example.json
synthetic-streams-manifest.csv
synthetic-labels.csv
synthetic-qc-report.json
toy-baseline-output.csv
mock-dashboard-fields.json
sample-structure-only.json
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

Use names that make the public boundary visible.

Do not publish ambiguous data.

---

## Authority rule

This folder is a GitHub helper surface.

It is not a canonical authority layer.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this folder conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

---

## Current P5-1 status

Current status:

```text
synthetic-session-001 exists.
synthetic-dyadic-session-001 exists.
P3 helper schema sample files exist.
validate_p3_schemas.py exists.
GitHub Actions P3 validator step added.
Synthetic/sample structure demonstration only.
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

Current P3 dyadic sample package:

```text
sample-data/
  synthetic-dyadic-session-001/
    README.md
    human_state_packet_A.json
    human_state_packet_B.json
    dyadic_session_event.json
    benchmark_session_container.json
```

---

## Current P4-1 status

Current status:

```text
synthetic-dyadic-session-001 exists.
P4-0 demo-flow files exist.
evaluate_dyadic_recovery_demo.py exists.
GitHub Actions P4 evaluator step added.
Synthetic demo-flow evaluation only.
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

Current P4-0 / P4-1 dyadic demo-flow package:

```text
sample-data/
  synthetic-dyadic-session-001/
    ai_outputs.json
    dyadic_delta.json
    recovery_gate.json
    termination_gate.json
    audit_log.json
```

Current P4-1 evaluator:

```text
evaluation-baseline/evaluate_dyadic_recovery_demo.py
```

Current P4-1 demo-flow result:

```text
dyadic recovery confirmed: false
one-sided improvement: true
recovery gate: not_passed
termination gate: pause_and_close_session
audit state: closed
false recovery prevention: active
public boundary: preserved
```

This result is a synthetic demo-flow consistency signal only.

It is not benchmark validation.

It is not scientific validation.

It is not mediation validation.

It is not Sal-Meter validation.

It is not CAIS compliance.

---

## Final rule

Public sample data exists to demonstrate structure.

It does not exist to disclose private human records.

It does not exist to prove benchmark performance.

It does not exist to validate mediation.

It does not exist to validate Sal-Meter.

It does not exist to grant CAIS compliance.

The packet is not the person.

The event is not the relationship.

The container is not the truth.

The demo-flow is not recovery.

The sample is a map.

It is not the mountain.
