# Evaluation Baseline

This folder contains baseline evaluation skeletons and helper-structure validation tools for the **SICS Human-State Proxy Benchmark Track**.

This is a research-stage, non-clinical, non-diagnostic, non-therapeutic benchmark support folder.

It is not the Sal-Meter core signal track.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not create clinical, diagnostic, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

---

## Purpose

The purpose of this folder is to demonstrate how public synthetic proxy benchmark data may be loaded, checked, split, and passed into transparent baseline modeling code.

The first goal is not high model performance.

The first goal is an auditable evaluation skeleton.

The second goal is a validator that confirms whether the public synthetic/sample package follows the expected helper structure.

The third goal is a boundary language lint helper that checks public helper files for prohibited or risky wording before public claim drift occurs.

This folder is designed to support:

- synthetic/sample package validation;
- public boundary language checking;
- schema-aligned file checks;
- transparent baseline pipeline scaffolding;
- leakage-safe split demonstration;
- reproducibility helper workflows;
- public/private data boundary discipline;
- future benchmark-support infrastructure.

It is not designed to support:

- benchmark validation;
- scientific validation;
- clinical interpretation;
- diagnostic scoring;
- therapeutic feedback;
- surveillance scoring;
- Sal-Meter validation;
- CAIS compliance claims;
- certified benchmark claims;
- mediation validation claims;
- production closed-loop claims.

---

## Current files

```text
evaluation-baseline/
  README.md
  requirements.txt
  baseline_pipeline_skeleton.py
  leakage_safe_split_example.py
  validate_sample_package.py
  prohibited_terms.json
  boundary_lint.py
```

| File | Role | Status |
|---|---|---|
| `requirements.txt` | Python dependency list for helper scripts | Present |
| `baseline_pipeline_skeleton.py` | Toy baseline pipeline skeleton for synthetic/sample features | Present |
| `leakage_safe_split_example.py` | Demonstration of leakage-aware split logic | Present |
| `validate_sample_package.py` | Structural validator for the public synthetic sample package | Present |
| `prohibited_terms.json` | Public boundary prohibited / risky wording list | Present |
| `boundary_lint.py` | Public boundary language lint helper | Present |
| `README.md` | Folder-level documentation and boundary notice | Current file |

---

## Expected sample input

The current helper scripts are designed around the public synthetic sample package:

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

It is not CAIS-compliant output.

---

## Schema alignment

The validator checks the sample package against helper schemas in:

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

These schemas validate structure only.

They do not validate scientific truth.

They do not validate human-state inference.

They do not validate model reliability.

They do not validate benchmark performance.

They do not validate Sal-Meter input.

They do not validate CAIS compliance.

---

## Dependency installation

From the repository root:

```bash
pip install -r evaluation-baseline/requirements.txt
```

The validator requires `jsonschema`.

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

---

## How to run the sample package validator

From the repository root:

```bash
python evaluation-baseline/validate_sample_package.py
```

Expected successful output:

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

A successful validator run means only:

```text
The public synthetic/sample package follows the expected helper structure.
```

A successful validator run does not mean:

```text
The data is real evidence.
The benchmark is validated.
The model is reliable.
The system is diagnostic.
The system is Sal-Meter.
The system is CAIS-compliant.
```

---

## Boundary language lint

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
- surveillance readiness;
- certification;
- device-readiness;
- production deployment;
- mediation-service readiness;
- counseling-service readiness;
- relationship scoring;
- or human-ranking authority.

It is a wording hygiene helper.

It is not a benchmark validator.

It is not a science validator.

It is not a Sal-Meter validator.

It is not a CAIS compliance validator.

It is not a mediation validator.

It does not process raw human data.

It does not process identifiable human data.

It does not process clinical data.

It does not process Sal-Meter raw input.

It does not process CAIS compliance dossiers.

---

## How to run boundary language lint

From the repository root:

```bash
python evaluation-baseline/boundary_lint.py
```

Expected clean output:

```text
Boundary language lint completed.

No configured prohibited or risky boundary-language terms were detected.

This result does not validate benchmark performance, scientific truth, Sal-Meter, CAIS compliance, mediation effectiveness, clinical use, diagnostic use, therapeutic use, surveillance readiness, certification, device-readiness, production readiness, or human-state truth measurement.
```

If risky wording is detected, the helper prints:

```text
Boundary language warning detected.
```

and reports:

```text
file path
line number
matched phrase
```

A warning means wording should be reviewed.

A warning does not mean scientific failure.

A warning does not mean benchmark failure.

A warning does not mean clinical failure.

A warning means public-language boundary drift may be present.

---

## Advisory and strict mode

By default, `boundary_lint.py` may be used as an advisory helper.

Advisory mode is useful during early drafting.

Run:

```bash
python evaluation-baseline/boundary_lint.py
```

For CI enforcement, use strict mode:

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

---

## Prohibited terms list

The file:

```text
prohibited_terms.json
```

stores the configured prohibited or risky wording list.

This list is part of the public claim firewall.

It may include expressions such as:

```text
validated mediation
validated human-state benchmark
validated proxy benchmark
CAIS-compliant
CAIS compliant
Sal-Meter validated
validated Sal-Meter
diagnostic
therapeutic
clinical decision
emotion detection
emotion recognition
surveillance
human score
relationship verdict
production closed-loop
certified proxy benchmark
device-ready
production-ready human-state AI
emotion-reading AI
emotion inference system
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

These terms are not always wrong in every context.

They are dangerous when they appear as project claims.

The lint helper exists to force review before public wording drifts beyond the repository boundary.

---

## Boundary lint PASS interpretation

A boundary lint clean run means only:

```text
No configured prohibited or risky boundary-language terms were detected in the scanned public helper files.
```

A boundary lint clean run does not mean:

```text
The benchmark is validated.
The science is validated.
The repository is Sal-Meter.
The repository is CAIS-compliant.
The mediation system works.
The system is clinical, diagnostic, therapeutic, certified, device-ready, or production-ready.
```

---

## Boundary lint FAIL / warning interpretation

A warning usually means one of the following:

- a prohibited term appears in public-facing helper text;
- a risky phrase may imply validation;
- a phrase may imply CAIS compliance;
- a phrase may imply Sal-Meter validation;
- a phrase may imply clinical, diagnostic, therapeutic, surveillance, certification, or production authority;
- a phrase may imply relationship scoring, human ranking, or human-state verdict authority.

A warning is a language-boundary mismatch.

A warning is not scientific evidence.

A warning is not benchmark evidence.

A warning is not clinical evidence.

A warning is not mediation evidence.

---

## What the sample package validator checks

`validate_sample_package.py` checks:

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

---

## What the sample package validator does not check

The validator does not check:

- real physiological validity;
- real psychological validity;
- true human-state inference;
- clinical interpretation;
- diagnostic correctness;
- therapeutic effect;
- model performance;
- benchmark reliability;
- external reproducibility;
- Sal-Meter signal validity;
- CAIS compliance;
- certification readiness;
- device readiness.

The validator may return `PASS` even though the package contains only synthetic/toy values.

That is expected.

The validator exists to verify structure, not truth.

---

## Common PASS interpretation

A `PASS` means:

```text
The synthetic sample package is internally consistent enough for public helper demonstration.
```

A `PASS` does not mean:

```text
The package proves a benchmark.
The package proves human-state measurement.
The package proves AI-state response safety.
The package proves Sal-Meter readiness.
The package proves CAIS compliance.
The package proves scientific validity.
```

---

## Common FAIL causes

A `FAIL` usually means one of the following:

- a required file is missing;
- a JSON file cannot be parsed;
- a CSV file has missing or mismatched column names;
- a schema file is invalid;
- a sample file does not match its schema;
- `dataset_type` is not `synthetic`;
- a required public boundary field is missing;
- a boundary flag expected to be `false` is not false;
- `synthetic_status_declared` is missing or not true;
- the operator log is missing expected boundary phrases;
- filenames, field names, or enum values drifted from the helper schemas.

A `FAIL` is not a scientific failure.

A `FAIL` is a structure or boundary mismatch.

---

## Boundary lint common warning causes

A boundary lint warning usually means one of the following:

- public helper wording may imply a validated benchmark;
- public helper wording may imply scientific validation;
- public helper wording may imply Sal-Meter validation;
- public helper wording may imply CAIS compliance;
- public helper wording may imply clinical, diagnostic, therapeutic, counseling, surveillance, certification, device-readiness, production-deployment, or human-ranking authority;
- public helper wording may imply a relationship verdict or human score;
- public helper wording may imply emotion detection or emotion recognition.

A boundary lint warning is not a scientific failure.

A boundary lint warning is a public language hygiene signal.

---

## Baseline pipeline skeleton

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

Run from the repository root:

```bash
python evaluation-baseline/baseline_pipeline_skeleton.py
```

For the current tiny synthetic sample, the baseline model may be skipped.

That is expected.

The current file demonstrates structure, not model performance.

---

## Leakage-safe split example

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

Run from the repository root:

```bash
python evaluation-baseline/leakage_safe_split_example.py
```

The current synthetic session is intentionally small and visible.

It is for structure demonstration only.

A real benchmark package must use stricter split rules.

---

## Recommended real split hierarchy

For future controlled benchmark work, prefer leakage-safe split rules in this order:

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

## Boundary

Allowed:

- synthetic feature loading;
- toy baseline processing;
- leakage-safe split demonstration;
- schema and file-structure checking;
- public boundary language linting;
- transparent model skeletons;
- reproducibility examples;
- public helper validation;
- non-diagnostic benchmark-support language.

Not allowed:

- raw human data;
- real participant data;
- real webcam data;
- real audio data;
- real face data;
- real voice data;
- identity mapping files;
- private consent records;
- clinical data;
- diagnostic claims;
- therapeutic claims;
- human ranking;
- surveillance scoring;
- Sal-Meter validation claims;
- CAIS compliance claims;
- certified benchmark claims;
- mediation validation claims;
- production closed-loop claims.

---

## Human-State Cost proxy boundary

Synthetic feature files may include a Human-State Cost proxy field.

In this repository, Human-State Cost is only a non-diagnostic benchmark construct example.

It must not be presented as:

```text
a medical score
a psychiatric score
a clinical score
a consciousness score
a psychological safety score
an employee monitoring score
a student ranking score
an insurance risk score
a legal eligibility score
a user dependence diagnosis
a human-ranking measure
a certified benchmark output
a Sal-Meter output
a CAIS output
```

Acceptable language:

```text
Human-State Cost proxy example value
non-diagnostic benchmark construct
synthetic/sample helper field
proxy burden comparison construct
```

Prohibited language:

```text
diagnostic score
clinical score
validated human-state score
certified benchmark output
Sal-Meter result
CAIS-compliant output
consciousness measurement
human truth score
```

Correct boundary sentence:

```text
Human-State Cost evaluates the interaction condition, not the person.
```

---

## How to interpret synthetic results

Synthetic results are allowed to show structure.

Synthetic results are not allowed to imply evidence.

A result from synthetic data may demonstrate:

- file loading;
- schema alignment;
- preprocessing flow;
- baseline code structure;
- leakage-control logic;
- reporting format.

A result from synthetic data must not claim:

- biological validity;
- physiological validity;
- psychological validity;
- clinical validity;
- diagnostic validity;
- benchmark validity;
- Sal-Meter validity;
- CAIS compliance.

---

## Baseline philosophy

Initial baselines should be boring.

Preferred properties:

- transparent;
- reproducible;
- leakage-aware;
- metadata-aware;
- synthetic-safe;
- easy to audit;
- explicit about limitations.

Avoid:

- leaderboard framing;
- deep learning performance claims;
- clinical scoring;
- diagnostic interpretation;
- hidden preprocessing;
- tuning on final holdout data;
- reporting synthetic output as evidence.

---

## Evaluation boundary

A model result from this folder must not be described as:

```text
validated
clinical
diagnostic
therapeutic
certified
CAIS-compliant
Sal-Meter validation
consciousness measurement
human ranking
psychological safety score
AI harm diagnosis
```

Acceptable language:

```text
synthetic baseline skeleton
toy evaluation example
leakage-safe split demonstration
research-stage proxy benchmark helper
non-diagnostic benchmark support
helper-structure validation
public boundary language lint
wording hygiene check
```

---

## GitHub Actions workflow

A workflow file may run the validator automatically from:

```text
.github/workflows/validate-synthetic-sample.yml
```

The intended workflow role is:

```text
Run validate_sample_package.py automatically on push, pull request, or manual dispatch.
```

A later workflow step may also run:

```bash
python evaluation-baseline/boundary_lint.py --strict
```

This strict lint step should be treated as a public wording-boundary gate only.

It must not be described as:

```text
benchmark validation
scientific validation
Sal-Meter validation
CAIS compliance validation
clinical validation
diagnostic validation
therapeutic validation
surveillance readiness
certification readiness
device readiness
production readiness
mediation validation
human-state truth measurement
```

The workflow is a repository hygiene helper.

It is not a benchmark validator.

It is not a Sal-Meter validator.

It is not a CAIS compliance validator.

It is not a clinical validator.

It is not a mediation validator.

It does not create clinical, diagnostic, therapeutic, surveillance, certification, or human-ranking authority.

If GitHub Actions access is restricted at account level, the workflow file may exist while workflow execution remains blocked.

In that case, local validation remains the fallback:

```bash
python evaluation-baseline/validate_sample_package.py
python evaluation-baseline/boundary_lint.py
```

---

## Troubleshooting

### Missing dependency

Possible output:

```text
FAIL: Missing dependency: jsonschema
```

Fix:

```bash
pip install jsonschema
```

Recommended repository fix:

```text
Add jsonschema to evaluation-baseline/requirements.txt
```

---

### Missing sample directory

Possible output:

```text
sample directory not found
```

Check that this folder exists:

```text
sample-data/synthetic-session-001/
```

---

### Missing schema directory

Possible output:

```text
schemas directory not found
```

Check that this folder exists:

```text
schemas/
```

---

### Missing required file

Possible output:

```text
missing required sample file
```

Check that the sample package contains:

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

---

### Boundary flag failure

Possible output:

```text
must be false
```

This means a public boundary field is not locked correctly.

Public sample files must keep these conditions false:

```text
raw_human_data_present == false
identifiable_data_present == false
clinical_data_present == false
sal_meter_input_present == false
cais_compliance_claim_present == false
```

---

### Synthetic status failure

Possible output:

```text
dataset_type should be 'synthetic'
```

For the current public sample package, `dataset_type` must remain:

```text
synthetic
```

---

### Boundary lint warning

Possible output:

```text
Boundary language warning detected.
```

This means one or more configured prohibited or risky terms were found.

Check the printed:

```text
file path
line number
matched phrase
```

Then revise the wording so that the public helper boundary remains clear.

A boundary lint warning is not scientific failure.

A boundary lint warning is not benchmark failure.

A boundary lint warning is a public-language hygiene signal.

---

### Boundary lint clean run

Possible output:

```text
Boundary language lint completed.
```

This means no configured prohibited or risky boundary-language terms were detected.

It does not validate benchmark performance.

It does not validate scientific truth.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not validate mediation effectiveness.

---

## P1-3 issue alignment

This README addresses:

```text
[P1-3] Improve evaluation baseline README and validator usability
```

The issue is complete when this README clearly explains:

- what the validator does;
- how to run the validator;
- how to install dependencies;
- what `PASS` means;
- what `FAIL` usually means;
- what the validator does not validate;
- why the output is helper-structure validation only.

---

## P1-5 release-readiness alignment

This README supports:

```text
[P1-5] Prepare v0.1.0 release readiness package
```

Relevant P1-5 checklist item:

```text
Confirm evaluation-baseline/README.md explains validator usage and PASS / FAIL interpretation
```

This checklist item is satisfied when this file clearly states:

```text
PASS means helper-structure validation only.
FAIL means structure or boundary mismatch.
Neither PASS nor FAIL is scientific validation.
```

---

## P5-0 boundary lint alignment

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
- that boundary lint is not benchmark validation, scientific validation, Sal-Meter validation, CAIS compliance, mediation validation, clinical validation, diagnostic validation, therapeutic validation, surveillance readiness, certification readiness, device readiness, production readiness, or human-state truth measurement.

---

## Recommended local check sequence

From the repository root:

```bash
pip install -r evaluation-baseline/requirements.txt
pip install jsonschema
python evaluation-baseline/validate_sample_package.py
python evaluation-baseline/boundary_lint.py
python evaluation-baseline/baseline_pipeline_skeleton.py
python evaluation-baseline/leakage_safe_split_example.py
```

Expected posture:

```text
The validator checks structure.
The boundary lint helper checks public wording.
The baseline skeleton demonstrates flow.
The leakage example demonstrates split discipline.
None of these outputs are benchmark evidence.
None of these outputs are scientific validation.
None of these outputs grant Sal-Meter validation or CAIS compliance.
```

---

## Authority rule

This folder is a GitHub helper surface.

It is not a canonical authority layer.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this folder conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

---

## Final rule

A result that cannot be replayed is not benchmark evidence.

A result that leaks labels is not evidence.

A result based on synthetic data is structure demonstration, not scientific proof.

A validator `PASS` is a structure signal, not a scientific claim.

A boundary lint clean run is a wording hygiene signal, not scientific validation.

This folder remains:

```text
Research-stage.
Synthetic/sample helper only.
Non-diagnostic.
Non-clinical.
Non-therapeutic.
Not Sal-Meter.
Not CAIS compliance.
Not benchmark evidence.
No raw human data.
No identifiable data.
No clinical data.
No Sal-Meter input.
No CAIS compliance claim.
No mediation validation claim.
No production closed-loop claim.
```
