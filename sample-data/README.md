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
- P4-3 synthetic termination-gate helper cases;
- synthetic pause / narrow / close / terminate decision examples;
- synthetic closed-session handling examples;
- synthetic permission-expiry handling examples;
- synthetic low-confidence and insufficient-data-quality examples;
- synthetic private-state exposure risk examples;
- synthetic one-sided improvement caution examples;
- schema demonstration files;
- generated examples for notebooks;
- non-identifying mock data;
- public helper files for structure demonstration.

The purpose is structure demonstration.

The purpose is not scientific proof.

The purpose is not benchmark validation.

The purpose is not mediation validation.

The purpose is not dyadic recovery validation.

The purpose is not termination-gate accuracy validation.

The purpose is not Sal-Meter validation.

The purpose is not CAIS compliance.

The purpose is not clinical, diagnostic, therapeutic, counseling, surveillance, certification, device-readiness, production-readiness, relationship-verdict, production closed-loop, or human-ranking authority.

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
    termination_gate_cases.json
```

The current public sample package map includes:

```text
Original synthetic session package
P3 synthetic dyadic helper package
P4-0 / P4-1 synthetic dyadic demo-flow package
P4-3 synthetic termination-gate helper case package
```

All listed files are public helper examples only.

They are synthetic.

They are structure-demonstration files.

They are not raw human data.

They are not identifiable human data.

They are not clinical data.

They are not Sal-Meter data.

They are not CAIS-compliance output.

They are not benchmark evidence.

They are not mediation evidence.

They are not dyadic recovery evidence.

They are not termination-gate accuracy evidence.

They are not production data.

---

## Package roles

| Folder | Role | Boundary |
|---|---|---|
| `synthetic-session-001/` | Original public synthetic/sample package for session metadata, streams, events, labels, QC, features, splits, and operator log | Structure demonstration only |
| `synthetic-dyadic-session-001/` | P5-1 / P3 synthetic dyadic helper package for Human-State Packet A/B, Dyadic Session Event, and Benchmark Session Container | Helper-schema validation only |
| `synthetic-dyadic-session-001/` | P4-0 / P4-1 synthetic dyadic demo-flow package for AI Output, Dyadic Delta, Recovery Gate, Termination Gate, and Audit Log | Synthetic demo-flow consistency only |
| `synthetic-dyadic-session-001/` | P4-3 synthetic termination-gate helper case package for pause, narrow, close, terminate, refresh, and audit-only decision examples | Synthetic termination-gate helper consistency only |

These packages are synthetic.

They are not real human data.

They are not identifiable human data.

They are not clinical data.

They are not Sal-Meter data.

They are not CAIS-compliance output.

They are not benchmark evidence.

They are not mediation evidence.

They are not dyadic recovery evidence.

They are not termination-gate accuracy evidence.

They are not production data.

They do not create clinical, diagnostic, therapeutic, counseling, surveillance, certification, device-readiness, production-readiness, relationship-verdict, production closed-loop, or human-ranking authority.

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

This package contains three public-safe synthetic layers:

```text
P3 helper-schema objects
P4-0 / P4-1 synthetic demo-flow objects
P4-3 synthetic termination-gate helper cases
```

All layers are synthetic.

All layers are helper-only.

No layer is benchmark evidence.

No layer is scientific validation.

No layer is mediation validation.

No layer is dyadic recovery validation.

No layer is termination-gate accuracy validation.

No layer is Sal-Meter validation.

No layer grants CAIS compliance.

**Layer summary:**

| Layer | Files | Boundary |
|---|---|---|
| P3 helper-schema layer | `human_state_packet_A.json`, `human_state_packet_B.json`, `dyadic_session_event.json`, `benchmark_session_container.json` | Helper-schema validation only |
| P4-0 / P4-1 synthetic demo-flow layer | `ai_outputs.json`, `dyadic_delta.json`, `recovery_gate.json`, `termination_gate.json`, `audit_log.json` | Synthetic demo-flow consistency only |
| P4-3 synthetic termination-gate helper layer | `termination_gate_cases.json` | Synthetic termination-gate helper consistency only |

This package must not be interpreted as:

```text
real dyadic data
clinical data
mediation evidence
benchmark evidence
dyadic recovery evidence
termination-gate accuracy evidence
Sal-Meter data
CAIS compliance output
production data
relationship verdict data
human-ranking data
```

Correct boundary sentence:

```text
The synthetic-dyadic-session-001 package demonstrates bounded helper structure only; it is not evidence, validation, Sal-Meter, or CAIS compliance.
```

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

## P4-3 synthetic termination-gate helper layer

The P4-3 layer demonstrates bounded synthetic termination-gate helper cases.

It is intended to show:

```text
Consent / Permission / Packet Quality / Session Scope
↓
Termination Gate Case
↓
Expected Helper Decision
↓
Boundary Preservation

```

Current P4-3 file map:

```text
sample-data/
  synthetic-dyadic-session-001/
    termination_gate_cases.json
```

This package is checked by:

```text
evaluation-baseline/evaluate_termination_gate_demo.py
```

A successful P4-3 synthetic termination-gate helper evaluation means only:

```text
The synthetic termination-gate helper cases are internally consistent enough for public helper demonstration.
```

It may demonstrate synthetic helper decisions such as:

- pause session;
- narrow scope;
- close session;
- terminate session;
- request consent refresh;
- request packet refresh;
- audit-only handling.

It confirms only bounded helper expectations such as:

- closed sessions stay closed;
- expired permission blocks ordinary continuation;
- low confidence blocks recovery declaration;
- insufficient data quality blocks recovery declaration;
- private-state exposure risk triggers pause or closure;
- one-sided improvement is not dyadic recovery.

It does not mean:

```text
The benchmark is validated.
The science is validated.
The mediation system works.
The termination gate is accurate.
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

Current synthetic termination-gate helper posture:

```text
total cases: 12
expected decisions present:
  - audit_only
  - close_session
  - narrow_scope
  - pause_session
  - request_consent_refresh
  - request_packet_refresh
  - terminate_session
closed session stays closed: true
expired permission blocks ordinary continuation: true
low confidence blocks recovery declaration: true
insufficient data quality blocks recovery declaration: true
private-state exposure risk triggers pause or closure: true
one-sided improvement is not dyadic recovery: true
public boundary: preserved
```

This result is a synthetic termination-gate helper consistency signal only.

It is not benchmark validation.

It is not scientific validation.

It is not mediation validation.

It is not termination-gate accuracy validation.

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
- P4-1 synthetic dyadic recovery demo-flow examples;
- P4-3 synthetic termination-gate helper case examples;
- AI Output helper examples;
- Dyadic Delta helper examples;
- Recovery Gate helper examples;
- Termination Gate helper examples;
- Audit Log helper examples;
- synthetic pause-session examples;
- synthetic narrow-scope examples;
- synthetic close-session examples;
- synthetic terminate-session examples;
- synthetic consent-refresh examples;
- synthetic packet-refresh examples;
- synthetic audit-only examples;
- synthetic closed-session handling examples;
- synthetic permission-expiry handling examples;
- synthetic low-confidence handling examples;
- synthetic insufficient-data-quality handling examples;
- synthetic private-state exposure risk examples;
- synthetic one-sided improvement caution examples;
- schema demonstration files;
- non-identifying mock data;
- generated examples for notebooks;
- public helper files for structure demonstration.

Allowed materials must remain:

- synthetic;
- public-helper-only;
- non-identifying;
- non-clinical;
- non-diagnostic;
- non-therapeutic;
- non-counseling;
- non-surveillance;
- non-certification;
- non-human-ranking;
- not Sal-Meter;
- not CAIS compliance;
- not benchmark evidence;
- not mediation evidence;
- not dyadic recovery evidence;
- not termination-gate accuracy evidence;
- not production data.

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
- scientific validation claims;
- mediation validation claims;
- dyadic recovery validation claims;
- termination-gate accuracy claims;
- device-readiness claims;
- production-readiness claims;
- certification claims;
- production closed-loop claims;
- relationship scoring outputs;
- relationship verdict outputs;
- human-ranking outputs;
- human-state verdict outputs;
- clinical decision outputs;
- diagnostic decision outputs;
- therapeutic decision outputs;
- counseling-service outputs;
- surveillance outputs;
- employment decision outputs;
- insurance decision outputs;
- educational eligibility outputs;
- legal eligibility outputs.

This folder must not contain files that imply:

```text
real human data
clinical evidence
diagnostic evidence
therapeutic evidence
scientific validation
benchmark validation
mediation validation
dyadic recovery validation
termination-gate accuracy validation
Sal-Meter validation
CAIS compliance
device readiness
production readiness
certification readiness
relationship verdict authority
human-ranking authority
```
production closed-loop intervention

If a file contains any of the above, it does not belong in this public sample-data folder.

Correct boundary sentence:

```text
Public sample data may demonstrate structure, but it must not create evidence, validation, certification, production authority, relationship verdicts, or human-ranking authority.
```

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
scientific_validation_claim_present == false
mediation_validation_claim_present == false
dyadic_recovery_validation_claim_present == false
termination_gate_accuracy_claim_present == false
production_intervention_claim_present == false
device_readiness_claim_present == false
production_readiness_claim_present == false
certification_claim_present == false
human_ranking_claim_present == false
relationship_verdict_present == false
human_state_verdict_present == false
clinical_decision_present == false
diagnostic_decision_present == false
therapeutic_decision_present == false
counseling_service_claim_present == false
surveillance_claim_present == false
employment_decision_present == false
insurance_decision_present == false
educational_eligibility_decision_present == false
legal_eligibility_decision_present == false
```

If any of the above cannot be confirmed, the file does not belong in this public repository.

Before publication, every sample-data file must remain:

```text
synthetic
public-helper-only
non-identifying
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
not scientific evidence
not mediation evidence
not dyadic recovery evidence
not termination-gate accuracy evidence
not production data
```

A public sample-data file may demonstrate:

- structure;
- file naming;
- metadata discipline;
- helper-schema alignment;
- demo-flow consistency;
- termination-gate helper consistency;
- public/private boundary discipline;
- leakage caution;
- validation-script compatibility.

A public sample-data file must not create:

- evidence;
- validation;
- certification;
- device readiness;
- production readiness;
- production closed-loop authority;
- clinical authority;
- diagnostic authority;
- therapeutic authority;
- counseling authority;
- surveillance authority;
- relationship verdict authority;
- human-ranking authority.

Correct boundary sentence:

```text
A file may enter sample-data only if it demonstrates public helper structure without creating evidence, validation, certification, production authority, relationship verdicts, or human-ranking authority.
```

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
termination_gate_helper_only
termination_gate_cases_only
public_helper_only
```

Every sample file should also make clear what it is not.

Recommended negative boundary fields or notes include:

```text
not_real_human_data
not_identifiable_data
not_clinical_data
not_diagnostic_data
not_therapeutic_data
not_counseling_data
not_surveillance_data
not_sal_meter_data
not_cais_compliance_output
not_benchmark_evidence
not_scientific_evidence
not_mediation_evidence
not_dyadic_recovery_evidence
not_termination_gate_accuracy_evidence
not_device_ready
not_production_ready
not_certified
not_relationship_verdict
not_human_ranking
not_production_closed_loop
```

For P4-3 termination-gate helper cases, the file should clearly indicate:

```text
dataset_type == synthetic
synthetic_status == synthetic_only
sample_scope == public_helper_only
```

The P4-3 case file may demonstrate:

- expected helper decisions;
- pause-session examples;
- narrow-scope examples;
- close-session examples;
- terminate-session examples;
- consent-refresh examples;
- packet-refresh examples;
- audit-only examples;
- closed-session handling;
- permission-expiry handling;
- low-confidence handling;
- insufficient-data-quality handling;
- private-state exposure risk handling;
- one-sided improvement caution.

The P4-3 case file must not imply:

- real mediation accuracy;
- validated termination-gate accuracy;
- benchmark validation;
- scientific validation;
- mediation validation;
- dyadic recovery validation;
- Sal-Meter validation;
- CAIS compliance;
- clinical readiness;
- diagnostic readiness;
- therapeutic readiness;
- device readiness;
- production readiness;
- certification;
- relationship verdict authority;
- human-ranking authority;
- production closed-loop authority.

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

Correct boundary sentence:

```text
A sample file may show how a helper object is shaped, but it must not claim that the helper object proves a real human state, mediation outcome, recovery outcome, termination accuracy, Sal-Meter validation, or CAIS compliance.
```

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

The P4-3 synthetic termination-gate helper cases are checked by the evaluator:

```text
evaluation-baseline/evaluate_termination_gate_demo.py
```

Current P4-3 case file:

```text
sample-data/
  synthetic-dyadic-session-001/
    termination_gate_cases.json
```

Schema alignment means:

```text
The file follows the expected helper structure.
```

P3 helper-schema alignment means:

```text
The public synthetic/sample P3 helper files follow the expected helper-schema structure.
```

P4-0 / P4-1 demo-flow evaluator alignment means:

```text
The synthetic demo-flow objects preserve expected helper consistency and boundary logic.
```

P4-3 termination-gate evaluator alignment means:

```text
The synthetic termination-gate helper cases preserve expected pause, narrow, close, terminate, refresh, audit-only, and boundary-preservation logic.
```

Schema or evaluator alignment may demonstrate:

- file structure;
- field naming discipline;
- helper-schema compatibility;
- demo-flow consistency;
- termination-gate helper consistency;
- public boundary flag discipline;
- non-identifying synthetic package structure.

Schema or evaluator alignment does not mean:

```text
The data is real evidence.
The benchmark is validated.
The model is reliable.
The mediation system works.
The dyadic recovery is real.
The termination gate is accurate.
The system is diagnostic.
The system is therapeutic.
The system is device-ready.
The system is production-ready.
The system is certified.
The system is Sal-Meter.
The system is CAIS-compliant.
The package creates relationship verdict authority.
The package creates human-ranking authority.
The package creates production closed-loop authority.
```

Correct boundary sentence:

```text
Schema and evaluator alignment demonstrate helper-structure consistency only; they do not create evidence, validation, certification, Sal-Meter status, CAIS compliance, or production authority.
```

---

## Validation

Current validation helpers:

```text
evaluation-baseline/validate_sample_package.py
evaluation-baseline/validate_p3_schemas.py
evaluation-baseline/evaluate_dyadic_recovery_demo.py
evaluation-baseline/evaluate_termination_gate_demo.py
evaluation-baseline/boundary_lint.py
```

Intended workflow posture:

```text
Run existing synthetic sample package validator.
Run P3 helper schema validator.
Run P4 synthetic dyadic recovery demo-flow evaluator.
Run P4-3 synthetic termination-gate helper evaluator.
Run boundary language lint.
```

The original sample package validator checks:

```text
sample-data/synthetic-session-001/
```

The P3 helper-schema validator checks:

```text
sample-data/synthetic-dyadic-session-001/
  human_state_packet_A.json
  human_state_packet_B.json
  dyadic_session_event.json
  benchmark_session_container.json
```

The P4-1 synthetic dyadic recovery demo-flow evaluator checks:

```text
sample-data/synthetic-dyadic-session-001/
  ai_outputs.json
  dyadic_delta.json
  recovery_gate.json
  termination_gate.json
  audit_log.json
```

The P4-3 synthetic termination-gate helper evaluator checks:

```text
sample-data/synthetic-dyadic-session-001/
  termination_gate_cases.json
```

These checks are repository hygiene helpers.

They are structure checks.

They are boundary checks.

They are helper-consistency checks.

They are not benchmark validators.

They are not scientific validators.

They are not Sal-Meter validators.

They are not CAIS compliance validators.

They are not mediation validators.

They are not dyadic recovery validators.

They are not termination-gate accuracy validators.

They do not create clinical, diagnostic, therapeutic, counseling, surveillance, certification, device-readiness, production-readiness, production-deployment, relationship-verdict, or human-ranking authority.

A successful validation run may mean only:

```text
The public synthetic/sample helper files follow expected helper structure.
The P3 helper-schema objects follow expected helper-schema structure.
The P4-1 synthetic demo-flow objects preserve expected helper consistency.
The P4-3 synthetic termination-gate helper cases preserve expected helper consistency.
Boundary wording remains within the configured public-helper boundary.
```

A successful validation run does not mean:

```text
The benchmark is validated.
The science is validated.
The mediation system works.
Dyadic recovery is validated.
Termination-gate accuracy is validated.
The repository is Sal-Meter.
The repository is CAIS-compliant.
The package is clinical.
The package is diagnostic.
The package is therapeutic.
The package is certified.
The package is device-ready.
The package is production-ready.
The package creates relationship verdict authority.
The package creates human-ranking authority.
The package creates production closed-loop authority.
```

Correct boundary sentence:

```text
Validation helpers may confirm public helper structure and synthetic consistency only; they do not create evidence, benchmark validation, mediation validation, Sal-Meter validation, CAIS compliance, certification, or production authority.
```

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
synthetic termination-gate helper consistency
termination-gate helper case
pause-session example
narrow-scope example
close-session example
terminate-session example
consent-refresh example
packet-refresh example
audit-only example
closed-session handling
permission-expiry handling
low-confidence handling
insufficient-data-quality handling
private-state exposure risk handling
one-sided improvement caution
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
not scientific validation
not mediation validation
not dyadic recovery validation
not termination-gate accuracy validation
not device readiness
not production readiness
not certification
no raw human data
no identifiable human data
no clinical data
no relationship verdict
no human ranking
no production closed-loop claim
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
validated termination-gate dataset
termination-gate accuracy evidence
termination-gate accuracy validation
human-state diagnosis
psychological safety score
consciousness measurement
emotion-reading AI
relationship scoring system
relationship verdict system
human quality score
human ranking system
AI harm detector
production-ready human-state AI
device-ready mediation system
certified mediation system
production closed-loop mediation system
clinical decision dataset
diagnostic decision dataset
therapeutic decision dataset
counseling-service dataset
surveillance dataset
employment decision dataset
insurance eligibility dataset
educational eligibility dataset
legal eligibility dataset
```

Correct boundary sentence:

```text
Use language that makes the file visibly synthetic, public-helper-only, non-diagnostic, non-validation, non-Sal-Meter, non-CAIS, non-production, non-verdict, and non-human-ranking.
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
termination_gate_cases.json
```

P4-3 termination-gate helper case files should use names that make the boundary visible.

Recommended P4-3 naming patterns:

```text
termination_gate_cases.json
synthetic_termination_gate_cases.json
termination_gate_helper_cases.json
sample_termination_gate_cases.json
synthetic_pause_close_cases.json
synthetic_closed_session_cases.json
synthetic_permission_expiry_cases.json
synthetic_low_confidence_cases.json
synthetic_private_state_exposure_cases.json
synthetic_one_sided_improvement_cases.json
```

Avoid ambiguous names such as:

```text
termination_accuracy.json
validated_gate_cases.json
real_mediation_cases.json
clinical_termination_cases.json
dyadic_recovery_truth.json
relationship_outcomes.json
human_ranking_cases.json
production_gate_cases.json
```

Use names that make the public boundary visible.

Use names that make synthetic status visible.

Use names that make helper-only status visible.

Do not publish ambiguous data.

Do not publish names that imply real human data, benchmark evidence, mediation validation, dyadic recovery validation, termination-gate accuracy validation, Sal-Meter validation, CAIS compliance, device readiness, production readiness, certification, relationship verdicts, human ranking, or production closed-loop authority.

Correct boundary sentence:

```text
A sample-data filename should make synthetic helper structure visible and should not imply evidence, validation, accuracy, certification, production authority, relationship verdicts, or human-ranking authority.
```

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

## Current P4-3 status

Current status:

```text
synthetic-dyadic-session-001 exists.
termination_gate_cases.json exists.
evaluate_termination_gate_demo.py exists.
GitHub Actions P4-3 evaluator step added.
Synthetic termination-gate helper evaluation only.
Not benchmark evidence.
Not scientific validation.
Not mediation validation.
Not dyadic recovery validation.
Not termination-gate accuracy validation.
Not Sal-Meter.
Not CAIS compliance.
No raw human data.
No identifiable data.
No clinical data.
No diagnostic label.
No therapeutic claim.
No certification claim.
No device-readiness claim.
No production-readiness claim.
No production closed-loop claim.
No relationship verdict.
No human-ranking claim.
```

Current P4-3 termination-gate helper case package:

```text
sample-data/
  synthetic-dyadic-session-001/
    termination_gate_cases.json
```

Current P4-3 evaluator:

```text
evaluation-baseline/evaluate_termination_gate_demo.py
```

Current P4-3 helper result posture:

```text
total cases: 12
expected decisions present:
  - audit_only
  - close_session
  - narrow_scope
  - pause_session
  - request_consent_refresh
  - request_packet_refresh
  - terminate_session
closed session stays closed: true
expired permission blocks ordinary continuation: true
low confidence blocks recovery declaration: true
insufficient data quality blocks recovery declaration: true
private-state exposure risk triggers pause or closure: true
one-sided improvement is not dyadic recovery: true
public boundary: preserved
```

This result is a synthetic termination-gate helper consistency signal only.

It is not benchmark validation.

It is not scientific validation.

It is not mediation validation.

It is not dyadic recovery validation.

It is not termination-gate accuracy validation.

It is not Sal-Meter validation.

It is not CAIS compliance.

---

## Final rule

Public sample data exists to demonstrate structure.

It does not exist to disclose private human records.

It does not exist to prove benchmark performance.

It does not exist to validate mediation.

It does not exist to validate dyadic recovery.

It does not exist to validate termination-gate accuracy.

It does not exist to validate Sal-Meter.

It does not exist to grant CAIS compliance.

It does not exist to certify device readiness.

It does not exist to certify production readiness.

It does not exist to authorize production closed-loop intervention.

The packet is not the person.

The event is not the relationship.

The container is not the truth.

The demo-flow is not recovery.

The termination-gate case is not accuracy evidence.

The sample is a map.

It is not the mountain.

A closed session must stay closed.
