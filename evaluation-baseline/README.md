# Evaluation Baseline

This folder contains baseline evaluation skeletons and helper-structure validation tools for the **SICS Human-State Proxy Benchmark Track**.

This is a research-stage, non-clinical, non-diagnostic, non-therapeutic benchmark support folder.

It is not the Sal-Meter core signal track.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not validate benchmark performance.

It does not validate scientific truth.

It does not validate mediation effectiveness.

It does not validate human-state measurement.

It does not create clinical, diagnostic, therapeutic, counseling, surveillance, employment, insurance, educational, legal, eligibility, certification, device-readiness, production-deployment, mediation-service, or human-ranking authority.

---

## 1. Purpose

The purpose of this folder is to demonstrate how public synthetic proxy benchmark data may be loaded, checked, split, validated against helper schemas, evaluated through bounded synthetic demo-flow logic, compared through synthetic AI Output A/B consequence logic, and passed into transparent baseline modeling code.

The first goal is not high model performance.

The first goal is an auditable evaluation skeleton.

The second goal is a validator that confirms whether the public synthetic/sample package follows the expected helper structure.

The third goal is a boundary language lint helper that checks public helper files for prohibited or risky wording before public claim drift occurs.

The fourth goal is a P3 helper-schema validator that confirms whether public synthetic dyadic helper files follow the expected Human-State Packet, Dyadic Session Event, and Benchmark Session Container schemas.

The fifth goal is a P4-1 synthetic dyadic recovery delta evaluator that reads the P4-0 synthetic dyadic demo-flow objects and prints a bounded helper-only evaluation summary.

The sixth goal is a synthetic AI Output A/B consequence evaluator that compares two synthetic AI output conditions using bounded synthetic consequence fields only.

**This folder supports:**

- synthetic/sample package validation;
- P3 helper-schema validation;
- P4 synthetic dyadic recovery demo-flow evaluation;
- P4-3 synthetic termination-gate helper evaluation;
- synthetic AI Output A/B consequence evaluation;
- public boundary language checking;
- schema-aligned file checks;
- transparent baseline pipeline scaffolding;
- leakage-safe split demonstration;
- reproducibility helper workflows;
- public/private data boundary discipline;
- future benchmark-support infrastructure.

**This folder does not support:**

- benchmark validation;
- scientific validation;
- clinical interpretation;
- diagnostic scoring;
- therapeutic feedback;
- counseling service;
- legal mediation service;
- surveillance scoring;
- Sal-Meter validation;
- CAIS compliance claims;
- certified benchmark claims;
- mediation validation claims;
- dyadic recovery validation claims;
- termination-gate accuracy validation claims;
- AI output superiority claims for real humans;
- real AI impact validation;
- production closed-loop claims.

## 2. Current files

```text
evaluation-baseline/
  README.md
  requirements.txt
  baseline_pipeline_skeleton.py
  leakage_safe_split_example.py
  validate_sample_package.py
  validate_p3_schemas.py
  evaluate_dyadic_recovery_demo.py
  evaluate_termination_gate_demo.py
  ai_output_ab_consequence_config.json
  synthetic_ab_inputs/
    synthetic_ai_output_ab_001.json
  evaluate_ai_output_ab.py
  demo_output/
    ai_output_ab_demo_report_001.json
  prohibited_terms.json
  boundary_lint.py
```

| File | Role | Status |
|---|---|---|
| `requirements.txt` | Python dependency list for helper scripts | Present |
| `baseline_pipeline_skeleton.py` | Toy baseline pipeline skeleton for synthetic/sample features | Present |
| `leakage_safe_split_example.py` | Demonstration of leakage-aware split logic | Present |
| `validate_sample_package.py` | Structural validator for the original public synthetic sample package | Present |
| `validate_p3_schemas.py` | P3 helper-schema validator for synthetic dyadic helper files | Present |
| `evaluate_dyadic_recovery_demo.py` | P4-1 synthetic dyadic recovery demo-flow evaluator | Present |
| `evaluate_termination_gate_demo.py` | P4-3 synthetic termination gate helper evaluator | Present |
| `ai_output_ab_consequence_config.json` | Configuration for the synthetic AI Output A/B consequence evaluator | Present |
| `synthetic_ab_inputs/synthetic_ai_output_ab_001.json` | Synthetic-only A/B input object for AI output consequence comparison | Present |
| `evaluate_ai_output_ab.py` | Synthetic AI Output A/B consequence evaluator | Present |
| `demo_output/ai_output_ab_demo_report_001.json` | Example bounded A/B consequence evaluator demo report | Present |
| `prohibited_terms.json` | Public boundary prohibited / risky wording list | Present |
| `boundary_lint.py` | Public boundary language lint helper | Present |
| `README.md` | Folder-level documentation and boundary notice | Current file |

---

## 3. Current public helper release status

**Current public helper release:**

```text
v0.1.1 — Post-Validator-Pass Public Helper Package for Human-State Proxy Benchmark Track
```

**Release posture:**

- bounded public helper pre-release;
- post-validator-pass helper-structure package;
- supersedes v0.1.0 for helper-structure validation status;
- manual binary assets: none;
- GitHub may automatically provide source code archives.

**This release status means only:**

- the public synthetic/sample package validator successfully ran on the main branch;
- the repository helper structure is publicly packaged after validator execution;
- the release remains a structure-only public helper pre-release.

**This release status does not mean:**

- benchmark performance is validated;
- scientific truth is validated;
- mediation effectiveness is validated;
- Sal-Meter is validated;
- CAIS compliance is granted;
- any system, model, dataset, dashboard, laboratory, device, repository, schema, session protocol, implementation, or mediation system is certified.

**Data boundary:**

- no raw human data;
- no identifiable human data;
- no clinical data;
- no Sal-Meter input;
- no CAIS-compliance measurement data;
- public examples remain synthetic/sample-structure-only.

**Authority boundary:**

GitHub is a technical helper surface.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this GitHub release conflicts with a DOI-registered canonical record or formally issued SICS determination, the stricter canonical record controls.

---

## 4. Expected sample inputs

This folder currently supports three public synthetic/sample helper packages or helper-flow groups.

**Original synthetic sample package:**

```text
sample-data/synthetic-session-001/
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

This input is synthetic only.

It is not real human data.

It is not benchmark evidence.

It is not Sal-Meter data.

It is not CAIS compliance output.

**P5-1 / P3 synthetic dyadic helper package:**

```text
sample-data/synthetic-dyadic-session-001/
  README.md
  human_state_packet_A.json
  human_state_packet_B.json
  dyadic_session_event.json
  benchmark_session_container.json
```

This input is synthetic only.

It is not real dyadic data.

It is not clinical data.

It is not mediation evidence.

It is not benchmark evidence.

It is not Sal-Meter data.

It is not CAIS compliance output.

**P4-0 / P4-1 synthetic dyadic demo-flow package:**

```text
sample-data/synthetic-dyadic-session-001/
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

This input is synthetic only.

It is a demo-flow helper package.

It is not real dyadic recovery evidence.

It is not mediation validation.

It is not benchmark validation.

It is not scientific validation.

It is not Sal-Meter validation.

It is not CAIS compliance.

It does not contain raw human data.

It does not contain identifiable human data.

It does not contain clinical data.

---

## 5. Schema alignment

**Original synthetic sample package schemas:**

```text
schemas/
  session-metadata.schema.json
  event-markers.schema.json
  streams-manifest.schema.json
  labels.schema.json
  qc-report.schema.json
  features-baseline.schema.json
  splits.schema.json
```

**P5-1 / P3 synthetic dyadic helper schemas:**

```text
schemas/
  human_state_packet.schema.json
  dyadic_session_event.schema.json
  benchmark_session.schema.json
```

**P3 validation mapping:**

```text
sample-data/synthetic-dyadic-session-001/human_state_packet_A.json
  -> schemas/human_state_packet.schema.json

sample-data/synthetic-dyadic-session-001/human_state_packet_B.json
  -> schemas/human_state_packet.schema.json

sample-data/synthetic-dyadic-session-001/dyadic_session_event.json
  -> schemas/dyadic_session_event.schema.json

sample-data/synthetic-dyadic-session-001/benchmark_session_container.json
  -> schemas/benchmark_session.schema.json
```

These schemas validate structure only.

They do not validate scientific truth.

They do not validate human-state inference.

They do not validate dyadic recovery.

They do not validate mediation effectiveness.

They do not validate model reliability.

They do not validate benchmark performance.

They do not validate Sal-Meter input.

They do not validate CAIS compliance.

---

## 6. P4-1 demo-flow evaluation alignment

The P4-1 synthetic dyadic recovery delta evaluator reads:

```text
sample-data/synthetic-dyadic-session-001/ai_outputs.json
sample-data/synthetic-dyadic-session-001/dyadic_delta.json
sample-data/synthetic-dyadic-session-001/recovery_gate.json
sample-data/synthetic-dyadic-session-001/termination_gate.json
sample-data/synthetic-dyadic-session-001/audit_log.json
```

It confirms internal consistency of a synthetic demo-flow chain:

```text
AI Output
-> Human-State Packet A/B
-> Dyadic Delta
-> Recovery Gate
-> Termination Gate
-> Audit Log
```

It checks demo-flow structure only.

It does not validate benchmark performance.

It does not validate scientific truth.

It does not validate mediation effectiveness.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not validate human-state measurement.

It does not process raw human data.

It does not process identifiable human data.

It does not process clinical data.

---

## 7. Dependency installation

From the repository root:

```bash
pip install -r evaluation-baseline/requirements.txt
```

The validators require `jsonschema`.

If `jsonschema` is not already included in the local environment or in `requirements.txt`, install it directly:

```bash
pip install jsonschema
```

Recommended dependency posture:

```text
numpy
pandas
scikit-learn
jsonschema
```

For automated validation, `jsonschema` should be available in the execution environment.

The P4-1 evaluator uses Python standard-library JSON and path handling only, but it should still be run in the same validation environment as the other helper scripts.

---

## 8. How to run validators and helper scripts

| Script | Command | Intended role |
|---|---|---|
| `validate_sample_package.py` | `python evaluation-baseline/validate_sample_package.py` | Original synthetic sample package structure validation |
| `validate_p3_schemas.py` | `python evaluation-baseline/validate_p3_schemas.py` | P3 synthetic dyadic helper-schema validation |
| `evaluate_dyadic_recovery_demo.py` | `python evaluation-baseline/evaluate_dyadic_recovery_demo.py` | P4-1 synthetic dyadic recovery demo-flow evaluation |
| `evaluate_termination_gate_demo.py` | `python evaluation-baseline/evaluate_termination_gate_demo.py` | P4-3 synthetic termination gate helper evaluation |
| `evaluate_ai_output_ab.py` | `python evaluation-baseline/evaluate_ai_output_ab.py` | Synthetic AI Output A/B consequence evaluator |
| `boundary_lint.py` | `python evaluation-baseline/boundary_lint.py` | Public boundary language lint |
| `baseline_pipeline_skeleton.py` | `python evaluation-baseline/baseline_pipeline_skeleton.py` | Toy baseline flow demonstration |
| `leakage_safe_split_example.py` | `python evaluation-baseline/leakage_safe_split_example.py` | Leakage-aware split demonstration |

**Recommended local check sequence:**

```bash
pip install -r evaluation-baseline/requirements.txt
pip install jsonschema
python evaluation-baseline/validate_sample_package.py
python evaluation-baseline/validate_p3_schemas.py
python evaluation-baseline/evaluate_dyadic_recovery_demo.py
python evaluation-baseline/evaluate_termination_gate_demo.py
python evaluation-baseline/evaluate_ai_output_ab.py
python evaluation-baseline/boundary_lint.py
python evaluation-baseline/baseline_pipeline_skeleton.py
python evaluation-baseline/leakage_safe_split_example.py
```

**Expected posture:**

The original validator checks synthetic sample package structure.
The P3 validator checks synthetic dyadic helper-schema structure.
The P4-1 evaluator checks synthetic dyadic demo-flow consistency.
The P4-3 evaluator checks synthetic termination-gate helper logic.
The AI Output A/B evaluator checks synthetic consequence comparison logic only.
The boundary lint helper checks public wording.
The baseline skeleton demonstrates flow.
The leakage example demonstrates split discipline.

None of these outputs are benchmark evidence.
None of these outputs are scientific validation.
None of these outputs are mediation validation.
None of these outputs prove real AI impact.
None of these outputs prove one AI output is better for real humans.
None of these outputs grant Sal-Meter validation or CAIS compliance.

---

## 9. Expected successful outputs

**Original sample package validator:**

```text
SICS Human-State Proxy Benchmark Track
Synthetic Sample Package Validator v0.1

PASS: sample-data/synthetic-session-001 follows the current public helper structure.

Boundary status:
- synthetic/sample structure validation only
- no raw human data validation
- no Sal-Meter input validation
- no CAIS compliance validation
- no diagnostic, therapeutic, or clinical validation
- no benchmark performance validation
```

**P3 helper-schema validator:**

```text
SICS Human-State Proxy Benchmark Track
P3 Helper Schema Validator v0.1

PASS: P3 synthetic dyadic helper files follow the current public helper schemas.
```

**P4-1 synthetic dyadic recovery demo evaluator:**

```text
SICS Human-State Proxy Benchmark Track
P4-1 Synthetic Dyadic Recovery Delta Evaluator v0.1

This evaluator checks synthetic demo-flow structure only.

It does not validate benchmark performance.
It does not validate scientific truth.
It does not validate mediation effectiveness.
It does not validate Sal-Meter.
It does not grant CAIS compliance.
It does not validate human-state measurement.
It does not process raw human data.
It does not process identifiable human data.
It does not process clinical data.

PASS: synthetic dyadic recovery demo flow evaluated successfully.

Synthetic demo result:
- dyadic recovery confirmed: false
- one-sided improvement: true
- recovery gate: not_passed
- termination gate: pause_and_close_session
- audit state: closed
- false recovery prevention: active
- public boundary: preserved
```

**P4-3 synthetic termination gate evaluator:**

```text
SICS Human-State Proxy Benchmark Track
P4-3 Synthetic Termination Gate Accuracy Skeleton v0.1

This evaluator checks synthetic termination-gate helper logic only.

It does not validate benchmark performance.
It does not validate scientific truth.
It does not validate mediation effectiveness.
It does not validate Sal-Meter.
It does not grant CAIS compliance.
It does not validate human-state measurement.
It does not process raw human data.
It does not process identifiable human data.
It does not process clinical data.

PASS: synthetic termination-gate helper cases evaluated successfully.

Synthetic termination gate result:
- total cases: 12
- expected decisions present:
  - audit_only
  - close_session
  - narrow_scope
  - pause_session
  - request_consent_refresh
  - request_packet_refresh
  - terminate_session
- closed session stays closed: true
- expired permission blocks ordinary continuation: true
- low confidence blocks recovery declaration: true
- insufficient data quality blocks recovery declaration: true
- private-state exposure risk triggers pause or closure: true
- one-sided improvement is not dyadic recovery: true
- public boundary: preserved
```

**AI Output A/B synthetic consequence evaluator:**

```text
SICS Human-State Proxy Benchmark Track
AI Output A/B consequence evaluator demo v0.1

Synthetic-only: true
Real participant data: false
Raw human data included: false

Comparison: synthetic_ai_output_ab_001
Condition A: generic_ai_response
Condition B: recovery_aware_response

Synthetic score A: -0.72
Synthetic score B: 0.73
Preferred synthetic condition: condition_b
Reason: Condition B has a higher synthetic helper score than Condition A.
Termination gate A: hold
Termination gate B: pass

This evaluator is public-helper-only.
It is not validation.
```

**AI Output A/B evaluator boundary interpretation:**

```text
This output means only that a synthetic A/B comparison object was loaded,
synthetic consequence fields were compared, and a bounded demo report was produced.

It does not mean that one AI output is better for real humans.
It does not validate real AI impact.
It does not validate mediation effectiveness.
It does not validate benchmark performance.
It does not validate scientific truth.
It does not validate Sal-Meter.
It does not grant CAIS compliance.
It does not process raw human data.
It does not process identifiable human data.
It does not process real conversations.
It does not process clinical data.
```

**Boundary lint clean output:**

```text
Boundary language lint completed.

No configured prohibited or risky boundary-language terms were detected.

This result does not validate benchmark performance, scientific truth, Sal-Meter, CAIS compliance, mediation effectiveness, clinical use, diagnostic use, therapeutic use, surveillance readiness, certification, device-readiness, production readiness, or human-state truth measurement.
```

---

## 10. PASS / FAIL interpretation

**A validator PASS means only one of the following:**

```text
The synthetic sample package is internally consistent enough for public helper demonstration.
```
or:
```
The public synthetic/sample P3 helper files follow the expected helper-schema structure.
```
or:
```
The synthetic P4 demo-flow objects are internally consistent enough for public helper demonstration.
```
or:
```
The synthetic P4-3 termination-gate cases are internally consistent enough for public helper demonstration.
```
or:
```
The synthetic AI Output A/B consequence evaluator can compare two synthetic AI output conditions using synthetic consequence fields only.
```

**A PASS does not mean:**

```text
The package proves a benchmark.
The package proves human-state measurement.
The package proves AI-state response safety.
The package proves dyadic recovery.
The package proves mediation effectiveness.
The package proves Sal-Meter readiness.
The package proves CAIS compliance.
The package proves scientific validity.
The package proves one AI output is better for real humans.
The package proves real AI impact.
The package proves real emotional recovery.
The package proves real relationship repair.
```

**A FAIL usually means one of the following:**

- a required file is missing;
- a JSON file cannot be parsed;
- a CSV file has missing or mismatched column names;
- a schema file is invalid;
- a sample file does not match its schema;
- `dataset_type` is not `synthetic`;
- synthetic/sample status is missing;
- a required public boundary field is missing;
- a boundary flag expected to be `false` is not false;
- a boundary flag expected to be `true` is not true;
- `synthetic_status_declared` is missing or not true;
- the operator log is missing expected boundary language;
- filenames, field names, or enum values drifted from the helper schemas;
- P4 demo-flow objects do not preserve expected recovery / termination / audit logic;
- P4-3 termination-gate cases do not preserve expected pause / narrow / close / terminate / audit-only logic;
- the synthetic A/B input cannot be parsed;
- required A/B consequence fields are missing;
- AI Output A or AI Output B is missing required synthetic consequence fields;
- the A/B evaluator cannot compute synthetic helper scores;
- the A/B evaluator cannot generate the A/B demo report;
- an A/B boundary flag expected to be `false` is not false;
- an A/B boundary flag expected to be `true` is not true.

A FAIL is not a scientific failure.

A FAIL is not a benchmark failure.

A FAIL is not a mediation failure.

A FAIL is not an AI superiority failure.

A FAIL is not proof that one AI output is worse for real humans.

A FAIL is a structure, boundary, schema, demo-flow, or synthetic evaluator mismatch.

---

## 11. What each validator checks

**`validate_sample_package.py` checks:**

- required sample package files exist;
- JSON files can be parsed;
- CSV files can be parsed;
- schema files can be loaded;
- JSON files align with their helper schemas;
- CSV rows align with their helper row schemas;
- synthetic status is declared;
- public boundary fields are present;
- raw human data flags are false;
- identifiable data flags are false;
- clinical data flags are false;
- face, voice, video, and audio public-data flags are false where declared;
- Sal-Meter input flags are false;
- CAIS compliance claim flags are false;
- operator log contains expected boundary language.

The validator is a structure gate.

It is not an evidence gate.

It is not a science gate.

It is not a performance gate.

It is not a clinical gate.

It is not a CAIS compliance gate.

**`validate_p3_schemas.py` checks:**

- required P3 schema files exist;
- required synthetic dyadic sample files exist;
- JSON files can be parsed;
- schema files can be parsed;
- schemas are valid Draft 2020-12 JSON Schemas;
- Human-State Packet A validates against `human_state_packet.schema.json`;
- Human-State Packet B validates against `human_state_packet.schema.json`;
- Dyadic Session Event validates against `dyadic_session_event.schema.json`;
- Benchmark Session Container validates against `benchmark_session.schema.json`;
- synthetic/sample status is explicit;
- raw human data exclusion is explicit;
- identifiable data exclusion is explicit;
- clinical data exclusion is explicit;
- Sal-Meter input exclusion is explicit;
- CAIS compliance exclusion is explicit;
- benchmark validation exclusion is explicit;
- mediation validation exclusion is explicit.

The P3 helper-schema validator is a structure gate.

It is not an evidence gate.

It is not a science gate.

It is not a benchmark gate.

It is not a mediation gate.

It is not a Sal-Meter gate.

It is not a CAIS compliance gate.

**`evaluate_dyadic_recovery_demo.py` checks:**

- required P4-0 demo-flow files exist;
- `ai_outputs.json` can be parsed;
- `dyadic_delta.json` can be parsed;
- `recovery_gate.json` can be parsed;
- `termination_gate.json` can be parsed;
- `audit_log.json` can be parsed;
- synthetic/sample status is explicit;
- raw human data exclusion is explicit;
- identifiable data exclusion is explicit;
- clinical data exclusion is explicit;
- Sal-Meter input exclusion is explicit;
- CAIS compliance exclusion is explicit;
- benchmark validation exclusion is explicit;
- mediation validation exclusion is explicit;
- production intervention exclusion is explicit;
- human ranking exclusion is explicit;
- relationship verdict exclusion is explicit;
- dyadic recovery is not marked as true;
- recovery gate is not passed;
- termination gate recommends pause and closure;
- audit log records closed state.

The P4-1 evaluator is a synthetic demo-flow evaluator.

It is not an evidence gate.

It is not a science gate.

It is not a benchmark gate.

It is not a mediation gate.

It is not a Sal-Meter gate.

It is not a CAIS compliance gate.

**`evaluate_termination_gate_demo.py` checks:**

- required P4-3 termination-gate case file exists;
- `termination_gate_cases.json` can be parsed;
- package metadata is explicit;
- synthetic/sample status is explicit;
- raw human data exclusion is explicit;
- identifiable data exclusion is explicit;
- clinical data exclusion is explicit;
- Sal-Meter input exclusion is explicit;
- CAIS compliance exclusion is explicit;
- benchmark validation exclusion is explicit;
- mediation validation exclusion is explicit;
- production intervention exclusion is explicit;
- human ranking exclusion is explicit;
- relationship verdict exclusion is explicit;
- 12 synthetic termination-gate cases exist;
- pause, narrow, close, terminate, refresh, and audit-only decisions are represented;
- closed sessions stay closed;
- expired permission blocks ordinary continuation;
- low confidence blocks recovery declaration;
- insufficient data quality blocks recovery declaration;
- private-state exposure risk triggers pause or closure;
- one-sided improvement is not marked as dyadic recovery.

The P4-3 evaluator is a synthetic termination-gate helper evaluator.

It is not an evidence gate.

It is not a science gate.

It is not a benchmark gate.

It is not a mediation gate.

It is not a Sal-Meter gate.

It is not a CAIS compliance gate.

**`evaluate_ai_output_ab.py` checks:**

- required A/B evaluator config exists;
- required synthetic A/B input exists;
- JSON files can be parsed;
- synthetic/sample status is explicit;
- raw human data exclusion is explicit;
- real participant data exclusion is explicit;
- real conversation exclusion is explicit;
- real phone recording exclusion is explicit;
- real call transcript exclusion is explicit;
- real session log exclusion is explicit;
- clinical data exclusion is explicit;
- diagnostic data exclusion is explicit;
- therapeutic data exclusion is explicit;
- counseling data exclusion is explicit;
- surveillance data exclusion is explicit;
- Sal-Meter input exclusion is explicit;
- CAIS compliance exclusion is explicit;
- benchmark validation exclusion is explicit;
- mediation validation exclusion is explicit;
- scientific truth validation exclusion is explicit;
- AI Output A has synthetic consequence fields;
- AI Output B has synthetic consequence fields;
- synthetic overload deltas can be compared;
- synthetic recovery deltas can be compared;
- synthetic relational stability deltas can be compared;
- synthetic termination gate statuses can be compared;
- synthetic helper scores can be computed;
- a synthetic preferred condition can be generated;
- the A/B demo report can be written.

The AI Output A/B evaluator is a synthetic consequence comparison helper.

It is not an evidence gate.

It is not a science gate.

It is not a benchmark gate.

It is not a mediation gate.

It is not a Sal-Meter gate.

It is not a CAIS compliance gate.

It does not prove that one AI output is better for real humans.

It does not validate real AI impact.

It does not validate real human-state measurement.

It does not create a relationship verdict.

It does not create human ranking.

---

## 12. Helper object boundaries

**Human-State Packet helper boundary**

The P3 Human-State Packet examples are:

```text
sample-data/synthetic-dyadic-session-001/human_state_packet_A.json
sample-data/synthetic-dyadic-session-001/human_state_packet_B.json
```

They are summary helper objects only.

They are not:

- the body;
- raw biosignal data;
- raw ECG;
- raw EEG;
- raw EDA;
- raw PPG;
- raw voice;
- raw face;
- raw gaze;
- raw video;
- raw transcript;
- a diagnosis;
- a therapy label;
- a psychiatric label;
- a clinical state;
- a human score;
- a truth score;
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

**Dyadic Session Event helper boundary**

The P3 Dyadic Session Event example is:

```text
sample-data/synthetic-dyadic-session-001/dyadic_session_event.json
```

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

**Benchmark Session Container boundary**

The P3 Benchmark Session Container example is:

```text
sample-data/synthetic-dyadic-session-001/benchmark_session_container.json
```

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

**P4-1 dyadic recovery demo boundary**

The P4-1 evaluator reads:

```text
ai_outputs.json
dyadic_delta.json
recovery_gate.json
termination_gate.json
audit_log.json
```

It may report:

- dyadic recovery confirmed: false;
- one-sided improvement: true;
- recovery gate: not_passed;
- termination gate: pause_and_close_session;
- audit state: closed;
- false recovery prevention: active;
- public boundary: preserved.

It must not report:

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

**P4-3 termination gate demo boundary**

The P4-3 evaluator reads:

```text
termination_gate_cases.json
```

It may report:

- total synthetic cases;
- expected termination-gate decisions;
- closed session stays closed;
- expired permission blocks ordinary continuation;
- low confidence blocks recovery declaration;
- insufficient data quality blocks recovery declaration;
- private-state exposure risk triggers pause or closure;
- one-sided improvement is not dyadic recovery;
- public boundary preserved.

It must not report:

- real mediation accuracy;
- validated termination accuracy;
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
A P4-3 evaluator result is a synthetic termination-gate helper consistency signal, not benchmark evidence.
```

---

## 13. Boundary language lint

The file:

```text
boundary_lint.py
```

is a public boundary language lint helper.

It scans public helper files for prohibited or risky wording that may imply:

- benchmark validation;
- scientific validation;
- Sal-Meter validation;
- CAIS compliance;
- clinical authority;
- diagnostic authority;
- therapeutic authority;
- counseling authority;
- surveillance readiness;
- certification;
- device-readiness;
- production deployment;
- mediation-service readiness;
- counseling-service readiness;
- relationship scoring;
- relationship verdict authority;
- human-ranking authority;
- validated dyadic recovery;
- validated termination accuracy;
- production closed-loop intervention.

It is a wording hygiene helper.

It is not a benchmark validator.

It is not a science validator.

It is not a Sal-Meter validator.

It is not a CAIS compliance validator.

It is not a mediation validator.

It is not a dyadic recovery validator.

It is not a termination-gate accuracy validator.

It is not a production-readiness validator.

It does not process raw human data.

It does not process identifiable human data.

It does not process clinical data.

It does not process Sal-Meter raw input.

It does not process CAIS compliance dossiers.

It does not evaluate real mediation effectiveness.

It does not evaluate real dyadic recovery.

It does not evaluate real termination accuracy.

It only checks whether public helper wording may drift beyond the permitted boundary.

**Advisory mode:**

```bash
python evaluation-baseline/boundary_lint.py
```

**Strict mode:**

```bash
python evaluation-baseline/boundary_lint.py --strict
```

Strict mode should fail the run if configured prohibited or risky wording is detected.

Use strict mode carefully.

Some prohibited terms may appear inside boundary documents as examples of what not to say.

If that happens, either revise the text context or later add explicit allow-list handling.

Do not use strict mode to imply scientific validation.

Do not use strict mode to imply benchmark validation.

Do not use strict mode to imply Sal-Meter validation.

Do not use strict mode to imply CAIS compliance.

Do not use strict mode to imply mediation validation.

Do not use strict mode to imply dyadic recovery validation.

Do not use strict mode to imply termination-gate accuracy validation.

Do not use strict mode to imply device readiness.

Do not use strict mode to imply production readiness.

Do not use strict mode to imply certification.

---

## 14. Boundary lint interpretation

**A boundary lint clean run means only:**

```text
No configured prohibited or risky boundary-language terms were detected in the scanned public helper files.
```

**A boundary lint clean run does not mean:**

```text
The benchmark is validated.
The science is validated.
The repository is Sal-Meter.
The repository is CAIS compliance output.
The mediation system works.
The dyadic recovery logic is validated.
The termination-gate logic is validated.
The system is clinical, diagnostic, therapeutic, certified, device-ready, or production-ready.
The system is authorized for production closed-loop intervention.
```

**A boundary lint warning usually means one of the following:**

- a prohibited term appears in public-facing helper text;
- a risky phrase may imply validation;
- a phrase may imply CAIS compliance;
- a phrase may imply Sal-Meter validation;
- a phrase may imply clinical, diagnostic, therapeutic, surveillance, certification, or production authority;
- a phrase may imply relationship scoring, human ranking, or human-state verdict authority;
- a phrase may imply dyadic recovery validation;
- a phrase may imply termination-gate accuracy validation;
- a phrase may imply mediation validation;
- a phrase may imply production closed-loop intervention.

A warning is a language-boundary mismatch.

A warning is not scientific evidence.

A warning is not benchmark evidence.

A warning is not clinical evidence.

A warning is not mediation evidence.

A warning is not dyadic recovery evidence.

A warning is not termination-gate accuracy evidence.

A warning is not Sal-Meter evidence.

A warning is not CAIS compliance evidence.

---

## 15. Baseline and leakage helper posture

**Baseline pipeline skeleton**

The file:

```text
baseline_pipeline_skeleton.py
```

is a toy baseline pipeline skeleton.

It may be used to demonstrate:

- loading synthetic feature rows;
- loading synthetic metadata;
- loading synthetic QC boundary declarations;
- enforcing public boundary fields;
- separating synthetic feature columns;
- sketching a transparent baseline flow;
- identifying where leakage-safe split logic belongs.

It must not be used to claim:

- validated model performance;
- real human-state classification;
- clinical interpretation;
- diagnostic status;
- Sal-Meter validation;
- CAIS compliance.

For the current tiny synthetic sample, the baseline model may be skipped.

That is expected.

The current file demonstrates structure, not model performance.

**Leakage-safe split example**

The file:

```text
leakage_safe_split_example.py
```

is a helper demonstration of leakage-aware split thinking.

It supports the principle that real benchmark evaluation must avoid hidden leakage through:

- participant identity;
- day/session order;
- device identity;
- operator identity;
- condition labels;
- filenames;
- preprocessing artifacts;
- train/validation/test contamination.

Recommended real split hierarchy:

```text
1. participant holdout
2. day holdout
3. device holdout
4. session holdout
5. condition holdout
6. operator holdout
```

Do not tune on the final holdout set.

Do not use filenames, folder names, condition names, session order, device IDs, or operator IDs as hidden labels.

---

## 16. Evaluation boundary

A model result, validator result, or evaluator result from this folder must not be described as:

```text
validated
clinical
diagnostic
therapeutic
certified
CAIS-compliance output
Sal-Meter validation
mediation validation
dyadic recovery validation
termination-gate accuracy validation
consciousness measurement
human ranking
psychological safety score
AI harm diagnosis
production closed-loop intervention
```

Acceptable language:

```text
synthetic baseline skeleton
toy evaluation example
leakage-safe split demonstration
research-stage proxy benchmark helper
non-diagnostic benchmark support
helper-structure validation
P3 helper-schema validation
P4 synthetic demo-flow evaluation
P4-3 synthetic termination-gate helper evaluation
public boundary language lint
wording hygiene check
```

Synthetic results are allowed to show structure.

Synthetic results are not allowed to imply evidence.

A result from synthetic data may demonstrate:

- file loading;
- schema alignment;
- preprocessing flow;
- baseline code structure;
- leakage-control logic;
- reporting format;
- P3 helper-schema mapping;
- P4 demo-flow consistency;
- P4-3 termination-gate helper consistency;
- boundary flag discipline.

A result from synthetic data must not claim:

- biological validity;
- physiological validity;
- psychological validity;
- clinical validity;
- diagnostic validity;
- therapeutic validity;
- benchmark validity;
- mediation validity;
- dyadic recovery validity;
- termination-gate accuracy validity;
- Sal-Meter validity;
- CAIS compliance;
- production readiness;
- certification readiness.

---

## 17. GitHub Actions workflow

A workflow file may run validation automatically from:

```text
.github/workflows/validate-synthetic-sample.yml
```

The intended workflow role is:

```text
Run validate_sample_package.py automatically on push, pull request, or manual dispatch.
Run validate_p3_schemas.py automatically as a P3 helper-schema validation step.
Run evaluate_dyadic_recovery_demo.py automatically as a P4 synthetic dyadic demo-flow evaluation step.
Run evaluate_termination_gate_demo.py automatically as a P4-3 synthetic termination-gate helper evaluation step.
Run boundary_lint.py as a public wording-boundary helper.
```

Current intended workflow sequence:

```text
Run synthetic sample package validator
Run P3 helper schema validator
Run P4 synthetic dyadic recovery demo evaluator
Run P4 termination gate demo evaluator
Run boundary language lint
```

This workflow is a repository hygiene helper.

It is not a benchmark validator.

It is not a Sal-Meter validator.

It is not a CAIS compliance validator.

It is not a clinical validator.

It is not a mediation validator.

It is not a dyadic recovery validator.

It is not a termination-gate accuracy validator.

It does not create clinical, diagnostic, therapeutic, surveillance, certification, device-readiness, production-readiness, relationship-verdict, production closed-loop, or human-ranking authority.

**Current workflow posture:**

- the workflow may run on push, pull request, or manual dispatch;
- a successful run confirms public helper-structure validation only;
- a successful run may confirm synthetic demo-flow consistency only;
- a successful run may confirm synthetic termination-gate helper consistency only;
- a successful run may confirm wording-boundary hygiene only;
- a successful run does not validate benchmark performance, scientific truth, Sal-Meter, CAIS compliance, mediation effectiveness, dyadic recovery, termination-gate accuracy, clinical use, diagnostic use, therapeutic use, surveillance readiness, certification, device readiness, production readiness, or human-state truth measurement.

If GitHub Actions access is ever restricted again at account level, the workflow file may exist while workflow execution remains blocked.

In that case, local validation remains the fallback:

```bash
python evaluation-baseline/validate_sample_package.py
python evaluation-baseline/validate_p3_schemas.py
python evaluation-baseline/evaluate_dyadic_recovery_demo.py
python evaluation-baseline/evaluate_termination_gate_demo.py
python evaluation-baseline/boundary_lint.py
```

---

## 18. Troubleshooting

| Symptom | Common cause | Fix |
|---|---|---|
| `FAIL: Missing dependency: jsonschema` | Missing dependency | Run `pip install jsonschema` and ensure `jsonschema` is in `evaluation-baseline/requirements.txt` |
| `sample directory not found` | Missing original sample folder | Check `sample-data/synthetic-session-001/` |
| `Missing required file: sample-data/synthetic-dyadic-session-001/...` | Missing P3/P4 dyadic sample file | Check `sample-data/synthetic-dyadic-session-001/` |
| `schemas directory not found` | Missing schema folder | Check `schemas/` |
| `missing required sample file` | Missing original synthetic sample file | Check required files under `sample-data/synthetic-session-001/` |
| `FAIL: P3 helper-schema validation failed.` | JSON/schema mismatch or boundary flag mismatch | Check required fields, enums, ID patterns, and boundary flags |
| `FAIL: synthetic dyadic recovery demo evaluation failed.` | P4 demo-flow mismatch | Check P4 JSON files, synthetic status, recovery gate, termination gate, and audit state |
| `FAIL: synthetic termination-gate helper evaluation failed.` | P4-3 termination-gate case mismatch | Check `termination_gate_cases.json`, expected decisions, boundary flags, closed-session logic, permission expiry logic, data-quality logic, private-state exposure logic, and recovery declaration exclusion |
| `must be false` | Boundary flag not locked | Confirm public boundary fields remain false where required |
| `dataset_type should be 'synthetic'` | Dataset type drift | Keep current public sample packages synthetic |
| `Boundary language warning detected.` | Risky public wording | Review file path, line number, and matched phrase |

**Required original sample files:**

```text
session_metadata.json
streams_manifest.csv
events.csv
labels.csv
qc_report.json
features_baseline.csv
splits.json
operator_log.md
```

**Required P3 files:**

```text
README.md
human_state_packet_A.json
human_state_packet_B.json
dyadic_session_event.json
benchmark_session_container.json
```

**Required P4 files:**

```text
ai_outputs.json
dyadic_delta.json
recovery_gate.json
termination_gate.json
audit_log.json
```

**Required P4-3 files:**

```text
termination_gate_cases.json
```

**Required P3 schemas:**

```text
schemas/human_state_packet.schema.json
schemas/dyadic_session_event.schema.json
schemas/benchmark_session.schema.json
```

**Required P4-3 evaluator:**

```text
evaluation-baseline/evaluate_termination_gate_demo.py
```

---

## 19. Issue and milestone alignment

**P1-3 alignment**

This README addresses:

```text
[P1-3] Improve evaluation baseline README and validator usability
```

The issue is complete when this README clearly explains:

- what the validator does;
- how to run the validator;
- how to install dependencies;
- what PASS means;
- what FAIL usually means;
- what the validator does not validate;
- why the output is helper-structure validation only.

**P1-5 / v0.1.1 alignment**

This README historically supported:

```text
[P1-5] Prepare v0.1.0 release readiness package
```

Current release alignment:

```text
v0.1.1 supersedes v0.1.0 for helper-structure validation status.
v0.1.1 remains a bounded public helper pre-release.
v0.1.1 remains structure-only, synthetic/sample-only, non-clinical, non-diagnostic, non-therapeutic, non-surveillance, non-certification, not Sal-Meter, and not CAIS compliance.
```

Relevant P1-5 checklist item:

```text
Confirm evaluation-baseline/README.md explains validator usage and PASS / FAIL interpretation.
```

This checklist item is satisfied when this file clearly states:

```text
PASS means helper-structure validation only.
FAIL means structure or boundary mismatch.
Neither PASS nor FAIL is scientific validation.
```

**P5-0 alignment**

This README supports:

```text
[P5-0] Add boundary language lint
```

This alignment is satisfied when this file clearly states:

- what `boundary_lint.py` does;
- how to run boundary language lint;
- how advisory mode differs from strict mode;
- where prohibited terms are stored;
- what a clean lint run means;
- what a lint warning means;
- that boundary lint is wording hygiene only;
- that boundary lint is not benchmark validation, scientific validation, Sal-Meter validation, CAIS compliance, mediation validation, dyadic recovery validation, termination-gate accuracy validation, clinical validation, diagnostic validation, therapeutic validation, surveillance readiness, certification readiness, device readiness, production readiness, or human-state truth measurement.

**P5-1 alignment**

This README supports:

```text
[P5-1] Extend validator to P3 helper schemas
```

This alignment is satisfied when this file clearly states:

- what `validate_p3_schemas.py` does;
- how to run the P3 helper-schema validator;
- which P3 files are checked;
- which P3 schemas are used;
- what P3 validator PASS means;
- what P3 validator FAIL means;
- that P3 helper-schema validation is helper-structure validation only.

**P4-1 alignment**

This README supports:

```text
[P4-1] Add dyadic recovery delta evaluator
```

This alignment is satisfied when this file clearly states:

- what `evaluate_dyadic_recovery_demo.py` does;
- how to run the P4-1 evaluator;
- which P4-0 files are read;
- what P4-1 evaluator PASS means;
- what P4-1 evaluator FAIL means;
- that P4-1 evaluation is synthetic demo-flow evaluation only.

**P4-3 alignment**

This README supports:

```text
[P4-3] Add termination gate accuracy skeleton
```

This alignment is satisfied when this file clearly states:

- what `evaluate_termination_gate_demo.py` does;
- how to run the P4-3 evaluator;
- which P4-3 files are read;
- what P4-3 evaluator PASS means;
- what P4-3 evaluator FAIL means;
- that P4-3 evaluation is synthetic termination-gate helper evaluation only;
- that closed sessions must stay closed;
- that expired permission blocks ordinary continuation;
- that low confidence and insufficient data quality block recovery declaration;
- that private-state exposure risk triggers pause or closure;
- that one-sided improvement is not dyadic recovery;
- that P4-3 does not validate benchmark performance, scientific truth, mediation effectiveness, Sal-Meter, CAIS compliance, clinical readiness, diagnostic readiness, therapeutic readiness, device readiness, production readiness, certification, relationship verdicts, or human ranking.

---

## 20. Current status

**Current P5-1 status:**

```text
validate_sample_package.py exists.
validate_p3_schemas.py exists.
boundary_lint.py exists.
synthetic-session-001 exists.
synthetic-dyadic-session-001 exists.
P3 helper schema sample files exist.
GitHub Actions P3 validator step added.
GitHub Actions helper workflow may confirm public helper-structure validation only.
Synthetic/sample structure demonstration only.
P3 helper-schema validation only.
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

**Current P3 dyadic sample package:**

```text
sample-data/
  synthetic-dyadic-session-001/
    README.md
    human_state_packet_A.json
    human_state_packet_B.json
    dyadic_session_event.json
    benchmark_session_container.json
```

**Current P3 validator:**

```text
evaluation-baseline/validate_p3_schemas.py
```

**Current P4-1 status:**

```text
evaluate_dyadic_recovery_demo.py exists.
synthetic-dyadic-session-001 exists.
P4-0 demo-flow files exist.
GitHub Actions P4 evaluator step added.
GitHub Actions helper workflow may confirm public helper-structure validation only.
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

**Current P4-0 / P4-1 dyadic demo-flow package:**

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

**Current P4-1 evaluator:**

```text
evaluation-baseline/evaluate_dyadic_recovery_demo.py
```

**Current P4-1 demo-flow result:**

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

**Current P4-3 status:**

```text
evaluate_termination_gate_demo.py exists.
termination_gate_cases.json exists.
GitHub Actions P4-3 evaluator step added.
GitHub Actions helper workflow may confirm public helper-structure validation only.
Synthetic termination-gate helper evaluation only.
Not benchmark evidence.
Not scientific validation.
Not mediation validation.
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

**Current P4-3 termination gate case package:**

```text
sample-data/
  synthetic-dyadic-session-001/
    termination_gate_cases.json
```

**Current P4-3 evaluator:**

```text
evaluation-baseline/evaluate_termination_gate_demo.py
```

**Current P4-3 helper result posture:**

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

## 21. Authority rule

This folder is a GitHub helper surface.

It is not a canonical authority layer.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this folder conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

---

## 22. Final rule

A result that cannot be replayed is not benchmark evidence.

A result that leaks labels is not evidence.

A result based on synthetic data is structure demonstration, not scientific proof.

A validator PASS is a structure signal, not a scientific claim.

A P3 helper-schema validator PASS is a helper-structure signal, not benchmark validation.

A P4-1 evaluator PASS is a synthetic demo-flow consistency signal, not benchmark validation.

A P4-3 evaluator PASS is a synthetic termination-gate helper consistency signal, not benchmark validation.

A boundary lint clean run is a wording hygiene signal, not scientific validation.

This folder remains:

```text
Research-stage.
Synthetic/sample helper only.
Non-diagnostic.
Non-clinical.
Non-therapeutic.
Non-counseling.
Non-surveillance.
Non-certification.
Non-human-ranking.
Not Sal-Meter.
Not CAIS compliance.
Not benchmark evidence.
Not scientific validation.
Not mediation validation.
Not dyadic recovery validation.
Not termination-gate accuracy validation.
No raw human data.
No identifiable data.
No clinical data.
No Sal-Meter input.
No CAIS compliance claim.
No benchmark validation claim.
No mediation validation claim.
No dyadic recovery validation claim.
No termination-gate accuracy validation claim.
No device-readiness claim.
No production-readiness claim.
No certification claim.
No relationship verdict.
No human-ranking claim.
No production closed-loop claim.
```

The sample is not evidence.

The schema is not truth.

The validator is not authority.

The evaluator is not proof.

The workflow is not certification.

The recovery gate does not crown recovery.

The termination gate does not prove accuracy.

The gate may open.

The gate may pause.

The gate may close.

A closed session must stay closed.

It does not crown the kingdom.
