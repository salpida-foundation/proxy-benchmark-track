# Proxy Benchmark Track

Research-stage proxy benchmark support track for **Human-State-Aware AI Interaction**.

This repository supports the Sal-Meter / CAIS kernel program by preparing synchronized multimodal benchmark infrastructure, metadata discipline, leakage-safe evaluation, baseline models, and future comparison surfaces.

It is **not** the Sal-Meter core signal track.

---

## Current status

**research-stage · non-clinical · non-diagnostic · non-therapeutic · benchmark support only**

This repository is:

- not the Sal-Meter core signal track
- not a CAIS-compliant device implementation
- not a validated substitute for Sal-Meter
- not a clinical, diagnostic, or therapeutic tool
- not a certification or compliance surface
- not a place to publish raw human data

The public landing page is here:

https://salpida.foundation/topics/human-state-aware-ai-interaction/

---

## What this track is

The Proxy Benchmark Track is a parallel support track for human-state-aware interaction research.

It uses existing proxy signals to build a benchmark platform before Sal-Meter molecular inputs are available for comparison.

The purpose is to prepare:

- synchronized multimodal capture
- session metadata
- event markers
- state-window labeling
- leakage-safe evaluation
- baseline models
- real-time feedback loops
- future A/B comparison against Sal-Meter core inputs

---

## What this track is not

This repository does not define Sal-Meter.

It does not redefine CAIS.

It does not grant:

- CAIS compliance
- Sal-Meter designation
- certification status
- mark entitlement
- authorized-user status
- clinical status
- diagnostic status
- therapeutic status

ECG, HRV, EDA, PPG, EEG, eye tracking, webcam markers, interaction timing, and behavioral signals do not become Sal-Meter by being combined.

They remain proxy benchmark signals.

---

## Core track vs proxy benchmark track

### Sal-Meter core track

The Sal-Meter core track asks whether a new molecular-electrochemical interface can produce stable, repeatable, state-relevant signal structure under the CAIS / Sal-Meter kernel program.

Current core path:

1. External Layer-0 iodine redox / thiol feasibility
2. SICS Internal Phase 0
3. Phase 1
4. Phase 2a
5. Phase 2b
6. LOCK 1 / LOCK 2
7. Future SDK / broader opening

### Proxy benchmark track

The proxy track prepares a comparison and interaction layer.

It builds synchronized multimodal baselines, leakage-safe evaluation rules, and closed-loop demos that can later serve as a comparison lane for Sal-Meter inputs.

The proxy track supports the core track.

It does not replace it.

---

## Signal families

The proxy stack may include:

- ECG
- HRV
- EDA
- PPG
- temperature
- IMU
- EEG
- eye / gaze
- webcam markers
- keystroke / interaction timing
- event markers
- simulator state
- UI / desktop interaction signals

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
- compatible with future Sal-Meter comparison

Suggested stack:

### Acquisition / sync

- LSL
- BrainFlow
- timestamp discipline
- event markers

### Real-time loop

- Timeflux-style streaming logic
- feedback windows
- state-window markers

### Modeling

- Python
- scikit-learn
- PyTorch
- baseline models
- replayable notebooks
- error analysis

### Vision / interaction

- webcam feature extraction
- OpenFace-style markers
- optional later Pupil / eye-tracking upgrade
- interaction timing

### Dashboard / storage

- lightweight local dashboard
- local NAS or secure storage
- versioned metadata
- non-public raw human data storage

---

## First build targets

### First 30-60 days

Build a lean benchmark spine:

- two or more synchronized proxy signals
- session metadata schema v0.1
- event marker and state-window logging
- raw / interim / processed folder convention
- local dashboard draft
- no public raw human data

### First 90 days

Build replayable benchmark v0.1:

- holdout split rule
- leakage-prevention checklist
- baseline time-series model
- error analysis notebook
- reproducibility pack with sample or synthetic data only
- closed-loop demo-lite for UI, desktop, simulator, or robot feedback

---

## Data boundary

Raw human data must not be published in this repository.

Public materials should use:

- sample data
- synthetic data
- schema-only examples
- documentation
- example code
- non-identifiable toy datasets

Do not upload:

- raw human biosignals
- identifiable participant records
- consent forms with personal information
- private session logs
- private health records
- uncontrolled video / audio / face data
- internal lab data packages

---

## Who this repository is for

### PBEE

Proxy Biosignal / Edge Engineer.

Good fit for people who can connect wearable sensors, stream time-series data, stabilize real-time loops, and document device ingestion.

### MDE

Machine Learning / Data Engineer.

Good fit for people who can design schemas, prevent leakage, build baseline models, manage holdouts, and create reproducible evaluation notebooks.

### HSOPM

Human-Session Operations / Protocol Manager.

Good fit for people who can manage consent, session scheduling, documentation, participant flow, and non-public human-data handling.

---

## Suggested repository structure

```text
proxy-benchmark-track/
  README.md
  docs/
    current-operating-model.md
    metadata-schema-v0.1.md
    leakage-control-checklist.md
    holdout-split-rule.md
    data-boundary.md
    roles-pbee-mde-hsopm.md
  sample-data/
    README.md
    synthetic-session-example.csv
    synthetic-metadata-example.json
  evaluation-baseline/
    README.md
    baseline-model-notebook.md
  closed-loop-demo-lite/
    README.md
  replication-guide/
    README.md
```

This structure is intentionally small.

Do not build a large public platform before metadata, synchronization, leakage control, and data boundary rules are stable.

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

### Publications hub

https://salpida.foundation/publications/

### Main GitHub organization

https://github.com/salpida-foundation

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
future comparison with Sal-Meter inputs
```

Do not use:

```text
Sal-Meter
validated Sal-Meter
certified Sal-Meter
CAIS-compliant device
clinical use
diagnostic use
therapeutic tool
medical device
proxy stack as Sal-Meter
human-state diagnosis
```

---

## Contact

For serious bounded-fit inquiries:

contact@salpida.foundation

Use one of these subject lines:

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

1. who you are
2. which role or layer you fit
3. one capability you can actually own
4. one uncertainty you can reduce
5. whether a 30-90 day benchmark skeleton path is realistic
6. whether non-public raw human data handling rules are acceptable

Do not send a broad partnership pitch first.

Send one bounded capability.

---

## Final boundary sentence

**Proxy first as benchmark. Sal-Meter later as core input. Claims never ahead of evidence.**

This repository exists to prepare the comparison layer without confusing it with the molecular-electrochemical Sal-Meter core.
