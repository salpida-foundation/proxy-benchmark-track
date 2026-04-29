# Proxy Benchmark Track

Research-stage proxy benchmark support track for **Human-State-Aware AI Interaction**.

This repository prepares a public technical helper surface for synchronized multimodal proxy benchmark infrastructure, metadata discipline, leakage-safe evaluation, synthetic/sample package structure, baseline evaluation scaffolding, and future comparison with Sal-Meter core inputs.

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

The Proxy Benchmark Track builds a comparison layer around the Sal-Meter kernel program: synchronized human-state proxy data, metadata discipline, leakage-safe evaluation, baseline models, synthetic/sample package structure, and future comparison with Sal-Meter core inputs.

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
- local dashboards at a later stage;
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

It builds synchronized multimodal baselines, leakage-safe evaluation rules, dataset structure, baseline modeling, and future closed-loop demo-lite scaffolding that can later serve as a comparison lane for Sal-Meter inputs.

The proxy track supports the core track.

It does not replace it.

---

## Why this track exists

This track exists for five reasons.

1. To build human-state-aware AI interaction infrastructure before Sal-Meter I/G-channel signals become available.
2. To create a disciplined comparison baseline for future Sal-Meter A/B testing.
3. To fix timestamp, metadata, leakage-prevention, holdout, and baseline modeling architecture early.
4. To enable non-clinical closed-loop demonstration of human-state-aware feedback in software, dashboard, simulator, and local AI interaction environments at a later stage.
5. To create an independent Human-AI Interaction research lane comparing AI task performance with measurable human-state impact.

A system may improve accuracy, speed, or productivity while increasing human-state burden.

This track makes that tradeoff visible under bounded, non-diagnostic, research-stage conditions.

---

## Current implementation status

This repository is currently in a public helper implementation stage for the SICS Human-State Proxy Benchmark Track.

It provides schema, synthetic/sample data, validation scaffolding, and repository hygiene workflow scaffolding for structure demonstration only.

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
| P1-5 v0.1.0 release readiness package | In progress | Repository is being checked for bounded public helper release readiness |

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
    claims_boundary.md
    public_private_data_boundary.md
    prohibited_claims.md

  schemas/
    README.md
    session-metadata.schema.json
    event-markers.schema.json
    streams-manifest.schema.json
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
    baseline_pipeline_skeleton.py
    leakage_safe_split_example.py
    requirements.txt
    validate_sample_package.py
```

This structure is intentionally small.

Do not build a large public platform before metadata, synchronization, leakage control, and data boundary rules are stable.

---

## Current validation path

The current public synthetic/sample package can be structurally checked locally with:

```bash
pip install -r evaluation-baseline/requirements.txt
python evaluation-baseline/validate_sample_package.py
```

Expected successful output:

```text
PASS: sample-data/synthetic-session-001 follows the current public helper structure.
```

This means only:

```text
The public synthetic/sample package follows the expected helper structure.
```

It does not mean:

```text
The data is real evidence.
The benchmark is validated.
The model is reliable.
The system is diagnostic.
The system is Sal-Meter.
The system is CAIS-compliant.
```

---

## GitHub Actions status

A GitHub Actions workflow file has been added:

```text
.github/workflows/validate-synthetic-sample.yml
```

The workflow is intended to run the synthetic sample package validator automatically.

Current status:

```text
Workflow file: present
Workflow name: Validate Synthetic Sample Package
Repository-level Actions setting: Allow all actions and reusable workflows
Execution status: blocked by GitHub account-level Actions restriction
```

Until GitHub Actions access is restored, validation should be treated as local/manual helper-structure validation only.

This does not affect the repository boundary.

It does not validate benchmark performance.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not create diagnostic, therapeutic, clinical, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

---

## v0.1.0 release readiness posture

`v0.1.0` is the first bounded public helper release target.

It should not be published until the following are true:

- root `README.md` reflects current implementation status;
- `schemas/README.md` explains schema scope and boundary;
- `sample-data/synthetic-session-001/README.md` explains the synthetic package boundary;
- `evaluation-baseline/README.md` explains validator usage and PASS / FAIL interpretation;
- `CITATION.cff` points to the correct public DOI records;
- repository About text is aligned with the public DOI boundary;
- repository Topics do not imply Sal-Meter validation, CAIS compliance, clinical use, or diagnostic authority;
- no raw human data, identifiable data, clinical data, Sal-Meter input, or CAIS compliance claim is present;
- repository language remains research-stage, non-clinical, non-diagnostic, non-therapeutic;
- GitHub Actions can run the synthetic sample package validator successfully.

Do not publish a release while P1-4 remains blocked.

---

## What this repository supports

This repository supports:

- synchronized multimodal proxy benchmark infrastructure;
- synthetic/sample package structure;
- metadata schema discipline;
- timestamp and event marker discipline;
- leakage-safe split awareness;
- baseline evaluation scaffolding;
- public/private data separation;
- helper-structure validation;
- future A/B comparison support with Sal-Meter inputs;
- non-diagnostic Human-State Cost proxy construct examples;
- dashboard and closed-loop demo scaffolding at a later stage.

---

## What this repository does not support

This repository does not support:

- raw human data publication;
- clinical interpretation;
- diagnostic labeling;
- therapeutic claims;
- surveillance scoring;
- employment, insurance, educational, legal, or eligibility decisions;
- CAIS compliance claims;
- Sal-Meter validation claims;
- certified benchmark claims;
- human-ranking outputs;
- psychological safety scoring;
- consciousness measurement claims.

---

## Public data boundary

Public repository examples must remain synthetic, mock, placeholder, or sample-structure-only.

Public files must not contain:

- raw human biosignal data;
- raw human video;
- raw face, voice, or audio data;
- direct identifiers;
- identity mapping files;
- private consent records;
- clinical interpretation;
- diagnostic labels;
- therapeutic recommendations;
- Sal-Meter input data;
- CAIS compliance claims;
- certification claims.

Boundary sentence:

> No raw human data belongs in this repository.

---

## Human-State Cost boundary

**Human-State Cost** may appear in this repository only as a non-diagnostic benchmark construct or synthetic/example field.

It may be used to compare measurable proxy burdens across AI interaction conditions.

It must not be presented as:

- a medical score;
- a psychiatric score;
- a clinical score;
- a diagnostic score;
- a consciousness score;
- a psychological safety score;
- an employee monitoring score;
- a student ranking score;
- an insurance risk score;
- a legal or eligibility score;
- a user dependence diagnosis;
- a human-ranking measure;
- a certified benchmark output;
- a Sal-Meter output;
- a CAIS output.

Correct interpretation:

```text
Human-State Cost evaluates the interaction condition, not the person.
```

Permitted phrasing:

```text
Human-State Cost is a non-diagnostic benchmark construct used to compare measurable proxy burdens across AI interaction conditions.
```

Prohibited phrasing:

```text
Human-State Cost diagnoses the user’s psychological or physiological condition.
```

---

## Minimum metadata discipline

Every future session-level benchmark package should be structured so that another reviewer can understand:

- what was recorded;
- when it was recorded;
- how streams were synchronized;
- which device generated each stream;
- what event markers were used;
- what state windows were labeled;
- what preprocessing version was applied;
- what data was excluded;
- why any exclusion occurred;
- what split strategy was used;
- what leakage risks were checked;
- what model version was used;
- what evaluation script version was used.

Minimum metadata families:

- session fields;
- participant-code fields;
- signal fields;
- event fields;
- quality fields;
- data-path fields;
- preprocessing fields;
- evaluation fields;
- reviewer fields;
- deviation fields.

No direct identifiers should be stored in public materials.

---

## Leakage control

The Proxy Benchmark Track must prevent models from learning shortcuts instead of meaningful signal structure.

Basic requirements:

- separate train, validation, and test sessions;
- avoid hidden labels in filenames, timestamps, folder names, device IDs, operator IDs, or session order;
- keep preprocessing rules fixed before evaluation;
- document all exclusions;
- record failed and partial sessions;
- keep raw data separate from processed data;
- keep public sample data synthetic or non-identifying;
- do not tune models on final holdout sets;
- do not remove failed runs without a logged reason.

Preferred holdout options:

- participant holdout;
- day holdout;
- device holdout;
- session holdout;
- condition holdout;
- operator holdout.

Minimum reporting:

- split strategy;
- leakage risks checked;
- missing data handling;
- excluded sessions;
- model version;
- preprocessing version;
- evaluation script version;
- metric definition;
- known limitations.

Red flags:

- unusually high accuracy without physiological plausibility;
- model performance driven by session order;
- condition labels embedded in filenames;
- preprocessing performed after viewing labels;
- same participant appearing in both train and test splits without disclosure;
- manual exclusion of inconvenient samples without logged reason.

---

## Evaluation baseline

Initial benchmark models should be simple, replayable, and intentionally boring.

Preferred first baseline:

- fixed preprocessing;
- fixed feature windows;
- transparent feature extraction;
- train / validation / test split;
- leakage review before final scoring;
- balanced accuracy or other pre-declared metrics where appropriate;
- error analysis;
- negative-result reporting;
- limitation notes.

Do not optimize for impressive scores before the leakage boundary is stable.

The first goal is not leaderboard performance.

The first goal is an auditable benchmark spine.

---

## Validation posture

The helper schemas and validator in this repository validate structure only.

They may be used to check whether a synthetic/sample file has the expected fields, naming conventions, boundary markers, and public release constraints.

They should not be used as proof that a dataset, model, dashboard, lab, device, software stack, or research result is validated.

A valid file means:

```text
The file follows the expected helper structure.
```

A valid file does not mean:

```text
The data is evidence.
The benchmark is validated.
The model is reliable.
The system is diagnostic.
The system is Sal-Meter.
The system is CAIS-compliant.
```

---

## Closed-loop demo-lite

The closed-loop demo-lite is a future bounded software demonstration layer.

It may show:

- stream capture;
- event marker logging;
- simple state-window estimation;
- dashboard visualization;
- feedback timing adjustment;
- UI pacing change;
- simulator response adjustment;
- local AI interaction pacing.

It must not claim:

- therapy;
- diagnosis;
- clinical monitoring;
- psychological safety scoring;
- medical stress detection;
- human ranking;
- employee surveillance;
- student evaluation;
- legal eligibility assessment;
- Sal-Meter validation;
- CAIS compliance.

Closed-loop means interaction feedback.

It does not mean clinical intervention.

---

## Roles this repository should attract

### PBEE

**Physiological Biosignal & Edge Engineering**

Good fit for contributors who can:

- connect wearable sensors;
- stream time-series data;
- stabilize real-time acquisition;
- handle LSL / BrainFlow / Timeflux-style flows;
- document sensor QC;
- build edge inference loops;
- track sync errors and device dropouts.

### MDE

**Machine Learning / Data Engineering**

Good fit for contributors who can:

- design dataset schemas;
- prevent leakage;
- build baseline models;
- manage holdout splits;
- write replayable notebooks;
- create evaluation skeletons;
- build error-analysis reports;
- maintain reproducibility packs.

### HSOPM

**Human-Session Operations / Protocol Management**

Good fit for contributors who can:

- manage consent pathways;
- schedule sessions;
- document participant flow;
- maintain session labels;
- protect raw human data;
- enforce metadata completeness;
- track deviations and exclusions.

### ESL / EStL boundary

ESL and EStL belong primarily to the **Sal-Meter core track**.

- ESL owns physical consistency in the core signal path.
- EStL owns evidence consistency, metadata discipline, QC, leakage prevention, audit trail, and reproducibility discipline.

They may review future A/B integration.

They do not redefine the proxy track.

The proxy track does not redefine the molecular core.

---

## What is open now

Open now:

- proxy benchmark README alignment;
- metadata schema discipline;
- data-boundary discipline;
- leakage-control checklist;
- synthetic sample data structure;
- baseline-model skeleton;
- synthetic sample package validator;
- GitHub Actions validator workflow scaffold;
- release-readiness preparation;
- PBEE / MDE / HSOPM contributor mapping.

Not open now:

- raw human data publication;
- public participant dataset release;
- clinical use;
- diagnostic use;
- therapeutic use;
- CAIS compliance claim;
- Sal-Meter designation claim;
- certified benchmark claim;
- broad Sal-Meter competition framing;
- validated commercial-device language.

---

## Future expansion queue

The following folders may be added after `v0.1.0` readiness is locked:

```text
protocol-helper/
  session_label_rule.md
  timestamp_sync_rule.md
  metadata_completeness_rule.md
  human_state_cost_construct_note.md
  future_sal_meter_ab_comparison_rule.md

dashboard-mockup/
  README.md
  dashboard_claim_boundary.md
  mockup_wireframe.md
  sample_dashboard_fields.json

closed-loop-demo-lite/
  README.md
  feedback_loop_boundary.md
  feedback_event_log_schema.json
  local_feedback_demo_placeholder.py

replication-guide/
  README.md
  reproducibility_package_checklist.md
  metadata_completeness_checklist.md
  audit_trail_checklist.md
  public_release_checklist.md

.github/
  ISSUE_TEMPLATE/
    boundary_correction.md
    schema_request.md
    sample_data_issue.md
    leakage_risk_report.md
  pull_request_template.md
```

These are future helper surfaces only.

They should not be added in a way that implies Sal-Meter validation, CAIS compliance, clinical use, diagnostic authority, or benchmark certification.

---

## Public language boundary

Use:

```text
research-stage
proxy benchmark track
benchmark support
human-state-aware interaction
synchronized multimodal benchmark
metadata discipline
leakage-safe evaluation
baseline models
synthetic/sample helper structure
closed-loop demo-lite
Human-State Cost as non-diagnostic benchmark construct
future comparison with Sal-Meter inputs
```

Do not use:

```text
Proxy Sal-Meter
non-molecular Sal-Meter
validated Sal-Meter
certified Sal-Meter
CAIS-compliant proxy stack
CAIS-compliant device
validated consciousness measurement
clinical stress system
diagnostic stress system
therapeutic feedback system
psychological safety score
employee wellbeing monitoring system
student ranking system
insurance risk score
human-state diagnosis
AI harm diagnosis
medical device
commercial validated device
```

---

## Permitted public sentence

SICS Human-State Proxy Benchmark Track is a research-stage, non-diagnostic, non-therapeutic benchmark support platform for synchronized multimodal human-state proxy sensing, metadata discipline, leakage-safe evaluation, baseline modeling, helper-structure validation, bounded AI feedback research, Human-State Cost comparison, and future comparison with Sal-Meter I/G-channel inputs.

---

## Never shorten this into an overclaim

Do not call this:

- Proxy Sal-Meter;
- non-molecular Sal-Meter;
- CAIS-compliant proxy stack;
- certified benchmark;
- validated consciousness measurement;
- diagnostic stress system;
- psychological safety score;
- Human-State Cost score;
- AI harm diagnosis;
- employee wellbeing monitoring system.

The proxy benchmark track is useful because it is bounded.

Its power comes from restraint.

---

## Useful public links

### Public landing page

https://salpida.foundation/topics/human-state-aware-ai-interaction/

### Current program status

https://salpida.foundation/status/

### Sal-Meter core track

https://salpida.foundation/topics/sal-meter/

### CAIS topic

https://salpida.foundation/topics/cais/

### For PIs

https://salpida.foundation/for-pis/

### Publications hub

https://salpida.foundation/publications/

### Main GitHub organization

https://github.com/salpida-foundation

### Sal-Meter Kernel Program

https://github.com/salpida-foundation/sal-meter-kernel-program

---

## Recommended reading order

1. Human-State-Aware AI Interaction public landing page  
   https://salpida.foundation/topics/human-state-aware-ai-interaction/

2. Current program status  
   https://salpida.foundation/status/

3. Public Boundary & Program Charter v0.1  
   https://doi.org/10.5281/zenodo.19837423

4. Scientific Rationale and Research Value v0.1  
   https://doi.org/10.5281/zenodo.19837971

5. Sal-Meter Core Track  
   https://salpida.foundation/topics/sal-meter/

6. Sal-Meter Kernel Program GitHub  
   https://github.com/salpida-foundation/sal-meter-kernel-program

---

## Contribution posture

This repository is not yet a broad open development platform.

Useful contributions should be bounded and practical.

Good first contributions:

- improve metadata schema clarity;
- add synthetic sample data;
- add leakage-risk examples;
- add dashboard mockup notes after the release-readiness boundary is stable;
- add baseline notebook skeletons after validator structure is stable;
- add reproducibility checklist items;
- improve public boundary wording;
- identify ambiguous claims and correct them.

Poor first contributions:

- broad philosophy essays;
- clinical claims;
- diagnostic claims;
- therapeutic claims;
- raw human data uploads;
- unbounded partnership pitches;
- claims that proxy signals are Sal-Meter;
- claims that this repository creates CAIS compliance.

---

## Contact

For serious bounded-fit inquiries:

contact@salpida.foundation

Suggested subject lines:

```text
Proxy benchmark support inquiry — [Name / Team]
```

```text
PBEE candidate inquiry — [Name]
```

```text
MDE candidate inquiry — [Name]
```

```text
HSOPM candidate inquiry — [Name]
```

Your first message should include:

1. who you are;
2. which role or layer you fit;
3. one capability you can actually own;
4. one uncertainty you can reduce;
5. whether a 30–90 day benchmark skeleton path is realistic;
6. whether non-public raw human data handling rules are acceptable.

Do not send a broad partnership pitch first.

Send one bounded capability.

---

## License

Unless otherwise stated, public helper materials in this repository are intended to align with:

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

**Proxy first as benchmark. Sal-Meter later as core input. Claims never ahead of evidence.**

This repository exists to prepare the comparison layer without confusing it with the molecular–electrochemical Sal-Meter core.
