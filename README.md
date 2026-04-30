# Proxy Benchmark Track

Research-stage proxy benchmark support track for **Human-State-Aware AI Interaction**.

This repository prepares a public technical helper surface for synchronized multimodal proxy benchmark infrastructure, metadata discipline, leakage-safe evaluation, synthetic/sample package structure, baseline evaluation scaffolding, dashboard mockup boundaries, and future comparison with Sal-Meter core inputs.

**This repository is not the Sal-Meter core signal track.**

**This repository is not a CAIS-compliant device implementation.**

**This repository is a public helper surface for the proxy benchmark track.**

---

## Current status

**research-stage · non-clinical · non-diagnostic · non-therapeutic · non-surveillance · non-coercive · pre-device · pre-certification · pre-compliance · benchmark support only**

This repository is:

- not the Sal-Meter core signal track;
- not a Proxy Sal-Meter;
- not a CAIS-compliant device implementation;
- not a validated consciousness measurement system;
- not a clinical, diagnostic, therapeutic, psychiatric, medical, employment, insurance, legal, educational, eligibility, or surveillance system;
- not a certification, conformance, or mark-usage surface;
- not a place to publish raw human data.

Public landing page:

https://salpida.foundation/topics/human-state-aware-ai-interaction/

---

## Canonical / DOI relationship

This repository is a **public technical helper surface** for the SICS Human-State Proxy Benchmark Track.

It accompanies, but does not replace, the following DOI-registered public records:

### SICS Human-State Proxy Benchmark Track — Public Boundary and Program Charter v0.1

Defines public boundary, naming rules, prohibited claims, data-publication limits, roadmap logic, GitHub helper status, and Go / Hold / No-Go structure.

- Version DOI: https://doi.org/10.5281/zenodo.19837423
- Concept DOI / all versions DOI: https://doi.org/10.5281/zenodo.19837422

### SICS Human-State Proxy Benchmark Track — Scientific Rationale and Research Value v0.1

Explains Human-State Cost, AI performance versus human-state impact, measurement-layer simplification, and future Sal-Meter A/B comparison logic.

- Version DOI: https://doi.org/10.5281/zenodo.19837971
- Concept DOI / all versions DOI: https://doi.org/10.5281/zenodo.19837970

If this README conflicts with a higher-level DOI-registered SICS / CAIS / Sal-Meter / CCF canonical or public boundary record, the higher-level DOI record prevails automatically.

GitHub helps builders move.

DOI records govern authority.

---

## One sentence

The Proxy Benchmark Track builds a comparison layer around the Sal-Meter kernel program: synchronized human-state proxy data, metadata discipline, leakage-safe evaluation, baseline models, synthetic/sample package structure, dashboard mockup boundaries, and future comparison with Sal-Meter core inputs.

---

## What this track is

The SICS Human-State Proxy Benchmark Track is a parallel research-stage benchmark support path for **Human-State-Aware AI Interaction**.

It uses existing proxy signals to prepare synchronized benchmark infrastructure before future Sal-Meter I/G-channel inputs become available.

The purpose is to prepare:

- synchronized multimodal capture;
- session metadata;
- event markers;
- state-window labeling;
- leakage-safe evaluation;
- holdout design;
- baseline models;
- safe dashboard mockup boundaries;
- replayable validation skeletons;
- bounded real-time feedback-loop demonstrations at a later stage;
- future A/B comparison against Sal-Meter core inputs.

The central research question is:

> AI should not be evaluated only by what it produces.  
> It should also be evaluated by what it leaves in the human being.

---

## What this track is not

This repository does not define Sal-Meter.

It does not redefine CAIS.

It does not grant:

- CAIS compliance;
- Sal-Meter designation;
- certification status;
- conformance recognition;
- mark entitlement;
- authorized-user status;
- clinical status;
- diagnostic status;
- therapeutic status;
- medical-device status;
- validated commercial-device status.

ECG, HRV, EDA, PPG, EEG, eye tracking, webcam markers, interaction timing, behavioral logs, task events, and AI feedback logs do not become Sal-Meter by being combined.

They remain **proxy benchmark signals**.

---

## Core track vs proxy benchmark track

The two tracks are related.

They are not identical.

They must not be publicly merged.

### Sal-Meter Core Track

The Sal-Meter Core Track asks whether a new molecular–electrochemical signal interface can produce stable, repeatable, auditable signal behavior under the CAIS / Sal-Meter kernel program.

Current core execution order:

1. External Layer-0 iodine redox / thiol feasibility
2. SICS Internal Phase 0 — G-only
3. Phase 1 — I-only
4. Phase 2a — Twin Mini-Cell
5. Phase 2b — G+I human pilot
6. LOCK 1 / LOCK 2
7. Future SDK / broader opening

Core technical route:

https://github.com/salpida-foundation/sal-meter-kernel-program

### Proxy Benchmark Track

The Proxy Benchmark Track prepares a comparison and interaction layer.

It builds synchronized multimodal baselines, leakage-safe evaluation rules, dataset structure, baseline modeling, dashboard boundary rules, and future closed-loop demo-lite scaffolding that can later serve as a comparison lane for Sal-Meter inputs.

The proxy track supports the core track.

It does not replace it.

---

## Why this track exists

This track exists for five reasons.

1. To build human-state-aware AI interaction infrastructure before Sal-Meter I/G-channel signals become available.
2. To create a disciplined comparison baseline for future Sal-Meter A/B testing.
3. To fix timestamp, metadata, leakage-prevention, holdout, dashboard, and baseline modeling architecture early.
4. To enable non-clinical closed-loop demonstration of human-state-aware feedback in software, dashboard, simulator, and local AI interaction environments at a later stage.
5. To create an independent Human-AI Interaction research lane comparing AI task performance with measurable human-state impact.

A system may improve accuracy, speed, or productivity while increasing human-state burden.

This track makes that tradeoff visible under bounded, non-diagnostic, research-stage conditions.

---

## Current implementation status

This repository is currently in a public helper implementation stage for the SICS Human-State Proxy Benchmark Track.

It provides schema, synthetic/sample data, validation scaffolding, dashboard mockup boundaries, protocol helper rules, and repository hygiene workflow scaffolding for structure demonstration only.

It does not provide benchmark evidence.

It does not provide raw human data.

It does not provide Sal-Meter input.

It does not grant CAIS compliance.

It does not validate Sal-Meter.

| Work item | Status | Notes |
|---|---|---|
| Governance boundary files | Present | Public/private data boundary and prohibited-claim discipline are represented in the repository |
| Schema completion | Done | `schemas/` contains public helper schemas for metadata, event markers, streams, labels, QC, features, and splits |
| Synthetic sample package | Present | `sample-data/synthetic-session-001/` contains a public synthetic/sample structure package |
| Synthetic session README | Done | The synthetic package includes a local README explaining file roles and boundaries |
| Sample package validator | Present | `evaluation-baseline/validate_sample_package.py` provides helper-structure validation |
| Evaluation baseline README | Done | `evaluation-baseline/README.md` explains validator usage, PASS / FAIL interpretation, dependency installation, and validation boundaries |
| Protocol helper boundary pack | Done | `protocol-helper/` defines label, timestamp, metadata, Human-State Cost, and future Sal-Meter A/B comparison boundaries |
| Dashboard mockup boundary pack | Present | `dashboard-mockup/` defines dashboard claim, field, and wireframe boundaries |
| GitHub Actions validator workflow | Present / Blocked | `.github/workflows/validate-synthetic-sample.yml` exists, but execution is currently blocked by GitHub account-level Actions restriction |
| Citation metadata | Present | `CITATION.cff` points citation toward DOI-registered public boundary records |
| Raw human data | Not present | Public repository examples must remain synthetic, mock, placeholder, or sample-structure-only |
| Sal-Meter input | Not present | This repository is not Sal-Meter and does not contain Sal-Meter signal data |
| CAIS compliance claim | Not present | This repository does not grant CAIS compliance |
| Benchmark validation | Not present | No model, dataset, dashboard, sensor stack, or benchmark result is validated by this repository |
| Release status | Not published | `v0.1.0` is a release-readiness target only until validator execution can run successfully |

---

## Current P1 milestone state

| Milestone | Status | Notes |
|---|---|---|
| P1-1 Schema completion | Done | Schema folder contains helper schemas and `schemas/README.md` |
| P1-2 Synthetic sample package validator | Done | Validator file exists under `evaluation-baseline/validate_sample_package.py` |
| P1-3 Evaluation baseline README and validator usability | Done | Evaluation baseline README explains local usage and boundary interpretation |
| P1-4 GitHub Actions validator workflow | Open / Blocked | Workflow exists but cannot currently run because GitHub Actions is disabled at the user-account level |
| P1-5 v0.1.0 release readiness package | In progress / Hold publication | Repository is being checked for bounded public helper release readiness; actual release must remain unpublished until P1-4 can run successfully |

---

## Current P2 milestone state

| Milestone | Status | Notes |
|---|---|---|
| P2-1 Protocol helper boundary pack | Done | `protocol-helper/` contains bounded helper rules for labels, timestamps, metadata completeness, Human-State Cost, and future Sal-Meter A/B comparison |
| P2-2 Dashboard mockup boundary pack | Ready to close after root README update | `dashboard-mockup/` contains README, claim boundary, sample dashboard fields, and mockup wireframe |
| P2-3 Closed-loop demo-lite boundary pack | Not started | Should begin only after P2-2 is closed |
| P2-4 Replication guide pack | Not started | Should follow closed-loop demo-lite or release-readiness stabilization |
| P2-5 Issue / PR template pack | Not started | Should be created after core public helper folders are stable |

---

## Repository structure

```text
proxy-benchmark-track/
  README.md
  LICENSE
  CITATION.cff

  .github/
    workflows/
      validate-synthetic-sample.yml

  docs/
    data-boundary.md
    leakage-control-checklist.md
    metadata-schema-v0.1.md
    public-language-boundary.md

  governance/
    README.md
    claims_boundary.md
    public_private_data_boundary.md

  schemas/
    README.md
    session-metadata.schema.json
    streams-manifest.schema.json
    event-markers.schema.json
    labels.schema.json
    qc-report.schema.json
    features-baseline.schema.json
    splits.schema.json

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

  evaluation-baseline/
    README.md
    requirements.txt
    validate_sample_package.py
    baseline_pipeline_skeleton.py
    leakage_safe_split_example.py

  protocol-helper/
    README.md
    session_label_rule.md
    timestamp_sync_rule.md
    metadata_completeness_rule.md
    human_state_cost_construct_note.md
    future_sal_meter_ab_comparison_rule.md

  dashboard-mockup/
    README.md
    dashboard_claim_boundary.md
    sample_dashboard_fields.json
    mockup_wireframe.md
```

If an exact file is not present in the repository, that file name should be treated as a planned or helper-reference path until created.

---

## Public helper surfaces

This repository contains public helper surfaces.

A public helper surface may:

- describe scope;
- explain boundaries;
- provide synthetic/sample data structures;
- define helper schemas;
- demonstrate validator logic;
- demonstrate leakage-aware split thinking;
- show dashboard mockup boundaries;
- prepare future contributor orientation.

A public helper surface must not:

- create canonical authority;
- replace DOI-registered records;
- publish raw human data;
- publish identifiable data;
- publish clinical data;
- imply Sal-Meter validation;
- imply CAIS compliance;
- imply benchmark validation;
- imply diagnostic, therapeutic, clinical, surveillance, certification, or human-ranking authority.

---

## Data boundary

Public examples in this repository must remain:

- synthetic;
- sample;
- mock;
- placeholder;
- toy;
- sample-structure-only;
- non-identifying.

This repository must not contain:

- raw human biosignals;
- raw human video;
- raw human audio;
- face data;
- voice data;
- identifiable participant metadata;
- private session logs;
- clinical data;
- health records;
- consent files containing personal information;
- internal lab packages;
- Sal-Meter raw input;
- CAIS compliance dossiers.

Raw human data belongs outside this public repository.

Private data requires separate governance, consent, access control, and audit structure.

---

## Schema helper pack

`schemas/` contains public helper schemas for synthetic/sample package structure.

The schemas are provided to document and validate structure.

They are not canonical authority.

They do not define CAIS.

They do not define Sal-Meter.

They do not grant CAIS compliance.

They do not validate Sal-Meter.

They do not validate benchmark performance.

They do not create diagnostic, therapeutic, clinical, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

Current schema helper files:

```text
schemas/
  README.md
  session-metadata.schema.json
  streams-manifest.schema.json
  event-markers.schema.json
  labels.schema.json
  qc-report.schema.json
  features-baseline.schema.json
  splits.schema.json
```

The schema pack supports:

- synthetic/sample data structure checks;
- metadata consistency;
- timestamp and event marker discipline;
- public/private data separation;
- leakage-risk awareness;
- helper validation.

It does not support:

- benchmark validation;
- Sal-Meter validation;
- CAIS compliance validation;
- diagnostic validation;
- clinical validation;
- therapeutic validation;
- surveillance validation;
- certification validation;
- human-ranking validation.

---

## Synthetic sample package

`sample-data/synthetic-session-001/` contains a public synthetic/sample package.

It is provided for structure demonstration only.

It does not contain raw human data.

It does not contain identifiable data.

It does not contain clinical data.

It does not contain Sal-Meter input data.

It does not grant CAIS compliance.

It does not validate benchmark performance.

It does not validate Sal-Meter.

It does not create diagnostic, therapeutic, clinical, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

Current synthetic package:

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

This package demonstrates:

- session-level metadata structure;
- stream inventory structure;
- event marker structure;
- label window structure;
- synthetic baseline feature structure;
- QC report structure;
- split definition structure;
- operator log structure;
- public/private data boundary language;
- leakage-risk awareness.

A public sample package is a lantern.

It lights the path.

It is not the mountain.

---

## Evaluation baseline

`evaluation-baseline/` contains baseline evaluation skeletons and helper-structure validation tools.

It is a research-stage, non-clinical, non-diagnostic, non-therapeutic benchmark support folder.

It is not the Sal-Meter core signal track.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not create clinical, diagnostic, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

Current files:

```text
evaluation-baseline/
  README.md
  requirements.txt
  baseline_pipeline_skeleton.py
  leakage_safe_split_example.py
  validate_sample_package.py
```

Purpose:

- load public synthetic proxy benchmark data;
- check structure;
- check required files;
- check JSON parsing;
- check CSV parsing;
- check schema alignment;
- check synthetic status;
- check public boundary fields;
- check operator log boundary language;
- demonstrate leakage-aware split logic;
- provide transparent baseline scaffolding.

It does not validate:

- model performance;
- benchmark performance;
- scientific truth;
- clinical state;
- diagnostic labels;
- therapeutic feedback;
- Sal-Meter input;
- CAIS compliance;
- certification readiness;
- device readiness.

---

## How to run the local validator

From the repository root:

```bash
pip install -r evaluation-baseline/requirements.txt
python evaluation-baseline/validate_sample_package.py
```

Expected successful output:

```text
PASS: sample-data/synthetic-session-001 follows the current public helper structure.
```

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
```

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

## GitHub Actions validator workflow

A GitHub Actions workflow file exists at:

```text
.github/workflows/validate-synthetic-sample.yml
```

The intended workflow name is:

```text
Validate Synthetic Sample Package
```

The intended workflow role is to run:

```bash
python evaluation-baseline/validate_sample_package.py
```

Current blocker:

```text
Failed to queue workflow run: Bad request - Actions has been disabled for this user.
```

Repository-level Actions settings have already been checked and saved as:

```text
Allow all actions and reusable workflows
```

Therefore, P1-4 remains open until GitHub restores Actions access and the workflow can run successfully.

This workflow is a repository hygiene and helper-structure validation workflow only.

It does not validate:

- benchmark performance;
- scientific validity;
- Sal-Meter input;
- Sal-Meter validation;
- CAIS compliance;
- diagnostic labels;
- clinical interpretation;
- therapeutic feedback;
- surveillance readiness;
- certification readiness;
- device readiness;
- human-state truth measurement.

---

## Protocol helper boundary pack

`protocol-helper/` contains public helper rules for the SICS Human-State Proxy Benchmark Track.

It exists to make the proxy benchmark track auditable, bounded, and harder to misinterpret.

It is not the Sal-Meter core signal track.

It does not define CAIS.

It does not grant CAIS compliance.

It does not validate Sal-Meter.

It does not validate benchmark performance.

It does not introduce raw human data.

It does not create clinical, diagnostic, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

Current files:

```text
protocol-helper/
  README.md
  session_label_rule.md
  timestamp_sync_rule.md
  metadata_completeness_rule.md
  human_state_cost_construct_note.md
  future_sal_meter_ab_comparison_rule.md
```

File roles:

```text
README.md
  Folder-level purpose, scope, and boundary.

session_label_rule.md
  Rules for session labels, condition labels, non-diagnostic state-window labels, and prohibited label drift.

timestamp_sync_rule.md
  Rules for timestamp discipline, stream alignment, drift reporting, and sync-boundary language.

metadata_completeness_rule.md
  Rules for mandatory metadata completeness, missingness, file mapping, raw/helper package reviewability, and audit trail.

human_state_cost_construct_note.md
  Bounded definition of Human-State Cost as a research-stage proxy construct, not a diagnosis, person score, or Sal-Meter signal.

future_sal_meter_ab_comparison_rule.md
  Rules for future proxy/core comparison once Sal-Meter inputs exist under separate governance.
```

The protocol helper pack supports:

- label discipline;
- timestamp discipline;
- metadata completeness;
- leakage awareness;
- Human-State Cost construct boundaries;
- future Sal-Meter A/B comparison boundaries;
- non-diagnostic benchmark helper language.

It does not support:

- clinical labels;
- diagnostic labels;
- therapeutic feedback;
- surveillance scoring;
- human ranking;
- person scoring;
- Sal-Meter validation claims;
- CAIS compliance claims.

---

## Dashboard mockup boundary pack

`dashboard-mockup/` contains public helper dashboard mockup boundary documents for the SICS Human-State Proxy Benchmark Track.

This folder exists to keep future dashboard views bounded, readable, and hard to overinterpret.

It is a public helper visualization boundary.

It is not the Sal-Meter core signal track.

It does not define CAIS.

It does not grant CAIS compliance.

It does not validate Sal-Meter.

It does not validate benchmark performance.

It does not introduce raw human data.

It does not create diagnostic, clinical, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

Current files:

```text
dashboard-mockup/
  README.md
  dashboard_claim_boundary.md
  sample_dashboard_fields.json
  mockup_wireframe.md
```

File roles:

```text
README.md
  Folder-level purpose, scope, and boundary.

dashboard_claim_boundary.md
  Allowed and prohibited dashboard claim language.

sample_dashboard_fields.json
  Synthetic/sample dashboard field definitions and boundary flags.

mockup_wireframe.md
  Text-only dashboard layout showing safe display structure.
```

The dashboard mockup boundary pack supports:

```text
safe dashboard language
synthetic/sample field display
non-diagnostic visualization
non-clinical visualization
non-therapeutic visualization
non-surveillance visualization
non-certification visualization
non-human-ranking visualization
future Sal-Meter A/B placeholder boundary
future dyadic / conflict mediation placeholder boundary
```

It does not support:

```text
validated dashboard claims
clinical dashboard claims
diagnostic dashboard claims
therapeutic dashboard claims
surveillance dashboard claims
employee monitoring claims
insurance scoring claims
legal eligibility claims
human-ranking claims
CAIS compliance claims
Sal-Meter validation claims
```

Current dashboard status:

```text
Dashboard mockup boundary pack: present
Dashboard claim boundary: present
Sample dashboard fields: present
Mockup wireframe: present
Raw human data: not present
Sal-Meter input: not present
CAIS compliance claim: not present
Benchmark validation claim: not present
Diagnostic / clinical / therapeutic authority: not present
Surveillance / certification / human-ranking authority: not present
```

A dashboard may show a window.

It must not become a courtroom.

It may show a proxy.

It must not become a person score.

---

## Human-State Cost boundary

Human-State Cost may appear in this repository only as a bounded, research-stage proxy construct.

It must not be presented as:

```text
a medical score
a psychiatric score
a clinical score
a consciousness score
a psychological safety score
an employee monitoring score
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
Human-State Cost Proxy Field
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

Human-State Cost must not become a person score.

Human-State Cost must not become diagnosis.

Human-State Cost must not become surveillance.

Human-State Cost must not become Sal-Meter.

Human-State Cost must not become CAIS compliance.

---

## Dyadic / conflict mediation boundary

Future dyadic or conflict mediation work may be referenced only as a bounded research-stage proxy benchmark direction.

Allowed future wording:

```text
Synthetic dyadic interaction mockup
Conflict Mediation Benchmark Preview
Future dyadic proxy benchmark placeholder
```

Required boundary:

```text
Not legal mediation.
Not therapy.
Not counseling.
Not relationship diagnosis.
Not fault assignment.
Not who-is-right determination.
Not who-is-wrong determination.
Not surveillance.
Not human ranking.
Not Sal-Meter.
Not CAIS compliance.
```

Not allowed wording:

```text
This dashboard decides who is right.
This dashboard identifies the unsafe partner.
This dashboard diagnoses the relationship.
This dashboard provides therapy.
This dashboard assigns blame.
This dashboard ranks people in conflict.
```

Dyadic dashboard mockups may compare interaction conditions.

They must not judge humans.

---

## Future Sal-Meter A/B comparison boundary

This repository may later support future A/B comparison between proxy benchmark features and Sal-Meter core inputs.

That future comparison is not active.

No Sal-Meter input is present in this repository.

No CAIS compliance is granted.

No Sal-Meter validation is claimed.

Allowed placeholder language:

```text
future_sal_meter_input_placeholder
future_proxy_core_comparison_placeholder
not_present
not_public
not_validated_here
future_placeholder_only
hold_until_separate_governance
```

Prohibited placeholder language:

```text
validated_sal_meter_input
CAIS_compliant_signal
official_consciousness_signal
ground_truth_signal
diagnostic_sal_meter_result
```

Future comparison must remain future until separate governance, data rights, consent, raw data handling, audit trail, and validation rules exist.

---

## Leakage-control principles

This repository treats leakage control as a first-class benchmark requirement.

A model, dashboard, or evaluation pipeline must not learn labels from hidden shortcuts such as:

- participant identity;
- day or session order;
- condition names;
- filenames;
- folder names;
- device identity;
- operator identity;
- preprocessing artifacts;
- timestamp artifacts;
- metadata fields that encode labels;
- train/validation/test contamination;
- dashboard-visible labels leaking into model input.

Synthetic data may expose labels for demonstration.

Real benchmark data must not.

A result that leaks labels is not evidence.

---

## Metadata completeness principles

A benchmark package must be reviewable.

A reviewable package needs:

- session ID;
- dataset type;
- synthetic or human-data status;
- public/private data boundary;
- stream manifest;
- event markers;
- label windows;
- feature table;
- QC report;
- split definition;
- operator log;
- schema version;
- timestamp source;
- known offsets;
- drift notes;
- missingness notes;
- leakage review notes;
- file mapping;
- audit trail;
- raw data handover boundary, if applicable under private governance.

A package without metadata cannot be audited.

A package that cannot be audited cannot become benchmark evidence.

---

## Baseline pipeline skeleton

The file:

```text
evaluation-baseline/baseline_pipeline_skeleton.py
```

is a toy baseline pipeline skeleton.

It may be used to demonstrate:

- loading synthetic feature rows;
- joining synthetic labels;
- separating features and labels;
- sketching a transparent baseline flow;
- identifying where leakage-safe split logic belongs.

It must not be used to claim:

- validated model performance;
- real human-state classification;
- clinical interpretation;
- diagnostic status;
- Sal-Meter validation;
- CAIS compliance.

---

## Leakage-safe split example

The file:

```text
evaluation-baseline/leakage_safe_split_example.py
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

The current synthetic session is intentionally small and visible.

It is for structure demonstration only.

A real benchmark package must use stricter split rules.

---

## Dashboard display boundary

Allowed dashboard language:

```text
synthetic sample
mock field
toy example
proxy benchmark helper
research-stage view
structure demonstration
non-diagnostic display
non-clinical display
non-therapeutic display
non-surveillance display
not Sal-Meter
not CAIS compliance
```

Prohibited dashboard language:

```text
validated
certified
clinical
diagnostic
therapeutic
approved
compliant
CAIS-compliant
Sal-Meter validated
consciousness measurement
human truth score
psychological safety score
employee monitoring score
risk score
eligibility score
legal score
insurance score
```

A dashboard must not make weak evidence look strong.

A dashboard must not turn proxy fields into person scores.

A dashboard must not turn synthetic/sample data into scientific proof.

---

## Suggested local stack

This repository is currently a public helper documentation and scaffold repository.

Potential future proxy benchmark implementation may use:

- LSL for stream synchronization;
- BrainFlow for biosignal interface abstraction;
- Timeflux for real-time signal pipelines;
- Python for data loading and evaluation;
- scikit-learn for transparent baseline models;
- PyTorch for later modeling experiments, if justified;
- OpenFace or equivalent public vision-proxy tools for bounded, non-identifying examples only;
- CARLA for simulator-linked interaction scenarios;
- lightweight local web UI for dashboard mockups;
- local NAS and versioned metadata store for private raw-data governance, if future human data are collected under separate approval.

This stack is not required for the current public helper package.

This stack does not validate the benchmark.

This stack does not create Sal-Meter.

This stack does not grant CAIS compliance.

---

## Public release boundary

A public release must not be published until:

- public helper boundary language is stable;
- synthetic/sample data boundaries are clear;
- schema references are correct;
- evaluator / validator documentation is clear;
- dashboard boundaries are visible;
- `CITATION.cff` points to DOI-registered public records;
- `README.md` clearly states the repository is a helper surface;
- no raw human data are present;
- no identifiable data are present;
- no clinical data are present;
- no Sal-Meter input is present;
- no CAIS compliance claim is present;
- no diagnostic, clinical, therapeutic, surveillance, certification, or human-ranking authority is implied;
- GitHub Actions validator workflow can run successfully, if the release depends on that validator.

Current release status:

```text
v0.1.0 release-readiness target only.
Actual GitHub Release: not published.
Publication hold reason: P1-4 GitHub Actions validator workflow is blocked by account-level Actions restriction.
```

---

## Citation guidance

If you use this repository, cite the DOI-registered public boundary record rather than treating GitHub as the canonical authority.

Preferred public boundary record:

```text
SICS Human-State Proxy Benchmark Track — Public Boundary and Program Charter v0.1
Version DOI: 10.5281/zenodo.19837423
Concept DOI: 10.5281/zenodo.19837422
```

Scientific rationale record:

```text
SICS Human-State Proxy Benchmark Track — Scientific Rationale and Research Value v0.1
Version DOI: 10.5281/zenodo.19837971
Concept DOI: 10.5281/zenodo.19837970
```

This GitHub repository is a public technical helper surface.

It is not the authority layer.

---

## Governance rule

Public helper materials may explain.

They must not overrule DOI-registered records.

Public helper materials may guide implementation.

They must not create compliance.

Public helper materials may demonstrate structure.

They must not claim validation.

Public helper materials may recruit builders.

They must not imply clinical, therapeutic, diagnostic, surveillance, certification, or human-ranking authority.

---

## Naming rule

Use:

```text
proxy benchmark track
Human-State Proxy Benchmark Track
Human-State-Aware AI Interaction
research-stage helper
synthetic sample package
dashboard mockup boundary
helper-structure validator
future Sal-Meter A/B comparison placeholder
```

Do not use:

```text
validated Sal-Meter
CAIS-compliant device
clinical dashboard
diagnostic dashboard
therapeutic dashboard
certified benchmark
official consciousness measurement
human truth score
employee monitoring score
psychological safety score
```

Names are gates.

Bad names open bad doors.

---

## Contributor boundary

Potential contributors should first understand:

1. whether you are working on a public helper surface;
2. whether you are handling synthetic/sample data only;
3. whether any raw human data are involved;
4. whether your work could be mistaken for diagnosis, therapy, surveillance, certification, or human ranking;
5. whether your work implies Sal-Meter validation;
6. whether your work implies CAIS compliance;
7. whether the relevant DOI-registered boundary record is preserved.

Do not send broad partnership material first.

Send one bounded capability.

---

## Current open holds

```text
P1-4 remains open:
  GitHub Actions workflow exists but is blocked by account-level Actions restriction.

P1-5 remains open:
  v0.1.0 release readiness is prepared, but release must remain unpublished until P1-4 can run successfully.

P2-2 can be closed after:
  root README.md is updated to reference dashboard-mockup/ as a public helper visualization boundary.
```

---

## License

Unless otherwise stated, public helper materials in this repository are provided under:

**Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**

This license does not grant:

- CAIS compliance;
- Sal-Meter designation;
- certification rights;
- mark-usage rights;
- clinical-use rights;
- diagnostic-use rights;
- therapeutic-use rights;
- authority to speak for SICS;
- authority to reinterpret DOI-registered canonical records.

---

## Final boundary sentence

This repository is a public helper surface.

It is a scaffold, not a verdict.

It is a map, not the mountain.

It prepares future comparison.

It does not claim that future comparison has already been validated.
