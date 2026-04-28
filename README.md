# Proxy Benchmark Track

Research-stage proxy benchmark support track for **Human-State-Aware AI Interaction**.

This repository prepares synchronized multimodal benchmark infrastructure, metadata discipline, leakage-safe evaluation, baseline models, dashboard drafts, and bounded closed-loop interaction demos for future comparison with Sal-Meter core inputs.

**It is not the Sal-Meter core signal track.**

---

## Current status

**research-stage · non-clinical · non-diagnostic · non-therapeutic · non-surveillance · non-coercive · pre-device · pre-certification · pre-compliance · benchmark support only**

This repository is:

- not the Sal-Meter core signal track
- not a Proxy Sal-Meter
- not a CAIS-compliant device implementation
- not a validated consciousness measurement system
- not a clinical, diagnostic, therapeutic, psychiatric, medical, employment, insurance, legal, educational, eligibility, or surveillance system
- not a certification, conformance, or mark-usage surface
- not a place to publish raw human data

Public landing page:

https://salpida.foundation/topics/human-state-aware-ai-interaction/

---

## Canonical / DOI relationship

This repository is a **public technical helper surface** for the SICS Human-State Proxy Benchmark Track.

It accompanies, but does not replace, the following DOI-registered public records:

### Public Boundary & Program Charter v0.1

Defines public boundary, naming rules, prohibited claims, data-publication limits, roadmap logic, GitHub helper status, and Go / Hold / No-Go structure.

- Version DOI: https://doi.org/10.5281/zenodo.19837423
- Concept DOI: https://doi.org/10.5281/zenodo.19837422

### Scientific Rationale and Research Value v0.1

Explains Human-State Cost, AI performance versus human-state impact, measurement-layer simplification, and future Sal-Meter A/B comparison logic.

- Version DOI: https://doi.org/10.5281/zenodo.19837971
- Concept DOI: https://doi.org/10.5281/zenodo.19837970

If this README conflicts with a higher-level DOI-registered SICS / CAIS / Sal-Meter / CCF canonical or public boundary record, the higher-level DOI record prevails automatically.

GitHub helps builders move.

DOI records govern authority.

---

## One sentence

The Proxy Benchmark Track builds the comparison layer around the Sal-Meter kernel program: synchronized human-state proxy data, metadata discipline, leakage-safe evaluation, baseline models, dashboard prototypes, and bounded closed-loop interaction demos.

---

## What this track is

The SICS Human-State Proxy Benchmark Track is a parallel research-stage benchmark support path for Human-State-Aware AI Interaction.

It uses existing proxy signals to build a synchronized benchmark platform before future Sal-Meter I/G-channel inputs become available.

The purpose is to prepare:

- synchronized multimodal capture
- session metadata
- event markers
- state-window labeling
- leakage-safe evaluation
- holdout design
- baseline models
- local dashboards
- replayable notebooks
- bounded real-time feedback loops
- future A/B comparison against Sal-Meter core inputs

The central research question is:

> AI should not be evaluated only by what it produces.  
> It should also be evaluated by what it leaves in the human being.

---

## What this track is not

This repository does not define Sal-Meter.

It does not redefine CAIS.

It does not grant:

- CAIS compliance
- Sal-Meter designation
- certification status
- conformance recognition
- mark entitlement
- authorized-user status
- clinical status
- diagnostic status
- therapeutic status
- medical-device status
- validated commercial-device status

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

It builds synchronized multimodal baselines, leakage-safe evaluation rules, dataset structure, baseline modeling, and closed-loop demos that can later serve as a comparison lane for Sal-Meter inputs.

The proxy track supports the core track.

It does not replace it.

---

## Why this track exists

This track exists for five reasons.

1. To build human-state-aware AI interaction infrastructure before Sal-Meter I/G-channel signals become available.
2. To create a disciplined comparison baseline for future Sal-Meter A/B testing.
3. To fix timestamp, metadata, leakage-prevention, holdout, and baseline modeling architecture early.
4. To enable non-clinical closed-loop demonstration of human-state-aware feedback in software, dashboard, simulator, and local AI interaction environments.
5. To create an independent Human-AI Interaction research lane comparing AI task performance with measurable human-state impact.

A system may improve accuracy, speed, or productivity while increasing human-state burden.

This track makes that tradeoff visible under bounded, non-diagnostic, research-stage conditions.

---

## Human-State Cost

**Human-State Cost** is a non-diagnostic benchmark construct.

It compares measurable proxy burdens left during or after interaction with an AI system.

It may include proxy patterns such as:

- stress load
- delayed recovery
- attention instability
- physiological arousal
- fatigue-like response
- dyadic synchrony disruption
- interaction friction
- dependence-like interaction patterns where ethically appropriate

It must not become:

- a medical score
- a psychiatric score
- a clinical score
- a diagnostic score
- a consciousness score
- an employment score
- an insurance score
- an educational ranking score
- a legal or eligibility score
- OE / RE / EE
- VCE / CRI / CFI
- a CAIS output
- a Sal-Meter output

Correct interpretation:

**Human-State Cost evaluates the interaction condition, not the person.**

---

## Signal families

The proxy stack may include:

- ECG
- HRV
- EDA
- PPG
- EEG
- respiration
- skin temperature
- IMU / motion
- eye / gaze
- blink / webcam markers
- speech timing
- reaction time
- keystroke / interaction timing
- task performance
- behavioral event markers
- AI feedback event logs
- simulator state
- UI / desktop interaction signals
- session labels
- metadata and QC logs

The purpose is not to diagnose a person.

The purpose is to create synchronized benchmark data and controlled interaction baselines.

---

## Reference implementation direction

The initial build should remain:

- local
- lightweight
- auditable
- replayable
- metadata-first
- leakage-aware
- non-clinical
- raw-data protected
- compatible with future Sal-Meter comparison

Suggested stack:

### Acquisition / synchronization

- LSL
- BrainFlow
- timestamp discipline
- event markers
- sync-error logs

### Real-time loop

- Timeflux-style streaming logic
- feedback windows
- state-window markers
- bounded interaction adjustments

### Modeling

- Python
- scikit-learn
- PyTorch
- baseline models
- replayable notebooks
- error analysis
- ablation tests

### Vision / interaction

- webcam feature extraction
- OpenFace-style markers
- optional later Pupil / eye-tracking upgrade
- interaction timing
- UI event markers

### Simulator / demo surface

- CARLA or equivalent simulator surface
- desktop interaction demo
- local AI interaction demo
- dashboard feedback demo-lite

### Dashboard / storage

- lightweight local web UI
- local NAS or secure storage
- versioned metadata store
- non-public raw human data storage
- audit trail discipline

---

## First build targets

### First 30–60 days

Build a lean benchmark spine:

- two or more synchronized proxy signals
- session metadata schema v0.1
- event marker and state-window logging
- raw / interim / processed folder convention
- leakage-control checklist
- first local dashboard draft
- no public raw human data

### First 90 days

Build replayable benchmark v0.1:

- holdout split rule
- leakage-prevention checklist
- baseline time-series model
- error analysis notebook
- reproducibility pack with sample or synthetic data only
- closed-loop demo-lite for UI, desktop, simulator, or local AI interaction feedback

---

## Suggested repository structure

```text
proxy-benchmark-track/
  README.md

  docs/
    current-operating-model.md
    data-boundary.md
    metadata-schema-v0.1.md
    leakage-control-checklist.md
    holdout-split-rule.md
    evaluation-baseline-notes.md
    closed-loop-demo-lite.md
    roles-pbee-mde-hsopm.md
    public-language-boundary.md
    reproducibility-checklist.md

  schemas/
    session-metadata.schema.json
    event-markers.schema.json
    signal-stream.schema.json
    qc-log.schema.json

  sample-data/
    README.md
    synthetic-session-example.csv
    synthetic-event-markers.csv
    synthetic-metadata-example.json

  notebooks/
    README.md
    baseline-model-skeleton.ipynb
    leakage-check-skeleton.ipynb
    error-analysis-skeleton.ipynb

  evaluation-baseline/
    README.md
    metrics.md
    split-rule.md
    baseline-model-spec.md

  dashboard-mockup/
    README.md
    dashboard-wireframe.md

  closed-loop-demo-lite/
    README.md
    feedback-loop-concept.md

  replication-guide/
    README.md
    minimal-reproducibility-pack.md
