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
```

This structure is intentionally small.

Do not build a large public platform before metadata, synchronization, leakage control, and data boundary rules are stable.

---

## Data boundary

Raw human data must not be published in this repository.

Public materials should use:

- synthetic data
- sample data
- schema-only examples
- documentation
- example code
- toy datasets
- non-identifiable demonstration files

Do not upload:

- raw human biosignals
- identifiable participant records
- consent forms with personal information
- private session logs
- private health records
- phone numbers
- email addresses
- resident numbers
- addresses
- medical record identifiers
- raw video from real sessions
- raw audio from real sessions
- face data from real sessions
- uncontrolled human-subject datasets
- internal lab data packages

Boundary sentence:

> No raw human data belongs in this repository.

---

## Minimum metadata discipline

Every future session-level benchmark package should be structured so that another reviewer can understand:

- what was recorded
- when it was recorded
- how streams were synchronized
- which device generated each stream
- what event markers were used
- what state windows were labeled
- what preprocessing version was applied
- what data was excluded
- why any exclusion occurred
- what split strategy was used
- what leakage risks were checked
- what model version was used
- what evaluation script version was used

Minimum metadata families:

- session fields
- participant-code fields
- signal fields
- event fields
- quality fields
- data-path fields
- preprocessing fields
- evaluation fields
- reviewer fields
- deviation fields

No direct identifiers should be stored in public materials.

---

## Leakage control

The Proxy Benchmark Track must prevent models from learning shortcuts instead of meaningful signal structure.

Basic requirements:

- separate train, validation, and test sessions
- avoid hidden labels in filenames, timestamps, folder names, device IDs, operator IDs, or session order
- keep preprocessing rules fixed before evaluation
- document all exclusions
- record failed and partial sessions
- keep raw data separate from processed data
- keep public sample data synthetic or non-identifying
- do not tune models on final holdout sets
- do not remove failed runs without a logged reason

Preferred holdout options:

- participant holdout
- day holdout
- device holdout
- session holdout
- condition holdout
- operator holdout

Minimum reporting:

- split strategy
- leakage risks checked
- missing data handling
- excluded sessions
- model version
- preprocessing version
- evaluation script version
- metric definition
- known limitations

Red flags:

- unusually high accuracy without physiological plausibility
- model performance driven by session order
- condition labels embedded in filenames
- preprocessing performed after viewing labels
- same participant appearing in both train and test splits without disclosure
- manual exclusion of inconvenient samples without logged reason

---

## Evaluation baseline

Initial benchmark models should be simple, replayable, and intentionally boring.

Preferred first baseline:

- fixed preprocessing
- fixed feature windows
- transparent feature extraction
- train / validation / test split
- leakage review before final scoring
- balanced accuracy or other pre-declared metrics where appropriate
- error analysis
- negative-result reporting
- limitation notes

Do not optimize for impressive scores before the leakage boundary is stable.

The first goal is not leaderboard performance.

The first goal is an auditable benchmark spine.

---

## Closed-loop demo-lite

The closed-loop demo-lite is a bounded software demonstration.

It may show:

- stream capture
- event marker logging
- simple state-window estimation
- dashboard visualization
- feedback timing adjustment
- UI pacing change
- simulator response adjustment
- local AI interaction pacing

It must not claim:

- therapy
- diagnosis
- clinical monitoring
- psychological safety scoring
- medical stress detection
- human ranking
- employee surveillance
- student evaluation
- legal eligibility assessment
- Sal-Meter validation
- CAIS compliance

Closed-loop means interaction feedback.

It does not mean clinical intervention.

---

## Roles this repository should attract

### PBEE

**Physiological Biosignal & Edge Engineering**

Good fit for contributors who can:

- connect wearable sensors
- stream time-series data
- stabilize real-time acquisition
- handle LSL / BrainFlow / Timeflux-style flows
- document sensor QC
- build edge inference loops
- track sync errors and device dropouts

### MDE

**Machine Learning / Data Engineering**

Good fit for contributors who can:

- design dataset schemas
- prevent leakage
- build baseline models
- manage holdout splits
- write replayable notebooks
- create evaluation skeletons
- build error-analysis reports
- maintain reproducibility packs

### HSOPM

**Human-Session Operations / Protocol Management**

Good fit for contributors who can:

- manage consent pathways
- schedule sessions
- document participant flow
- maintain session labels
- protect raw human data
- enforce metadata completeness
- track deviations and exclusions

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

- proxy benchmark README alignment
- metadata schema drafting
- data-boundary discipline
- leakage-control checklist
- synthetic sample data structure
- baseline-model skeleton
- dashboard mockup
- closed-loop demo-lite design
- PBEE / MDE / HSOPM contributor mapping

Not open now:

- raw human data publication
- public participant dataset release
- clinical use
- diagnostic use
- therapeutic use
- CAIS compliance claim
- Sal-Meter designation claim
- certified benchmark claim
- broad Sal-Meter competition framing
- validated commercial-device language

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

SICS Human-State Proxy Benchmark Track is a research-stage, non-diagnostic, non-therapeutic benchmark support platform for synchronized multimodal human-state sensing, metadata discipline, leakage-safe evaluation, baseline modeling, dashboard prototyping, bounded AI feedback research, Human-State Cost comparison, and future comparison with Sal-Meter I/G-channel inputs.

---

## Never shorten this into an overclaim

Do not call this:

- Proxy Sal-Meter
- non-molecular Sal-Meter
- CAIS-compliant proxy stack
- certified benchmark
- validated consciousness measurement
- diagnostic stress system
- psychological safety score
- Human-State Cost score
- AI harm diagnosis
- employee wellbeing monitoring system

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

- improve metadata schema clarity
- add synthetic sample data
- add leakage-risk examples
- add dashboard mockup notes
- add baseline notebook skeletons
- add reproducibility checklist items
- improve public boundary wording
- identify ambiguous claims and correct them

Poor first contributions:

- broad philosophy essays
- clinical claims
- diagnostic claims
- therapeutic claims
- raw human data uploads
- unbounded partnership pitches
- claims that proxy signals are Sal-Meter
- claims that this repository creates CAIS compliance

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

1. who you are
2. which role or layer you fit
3. one capability you can actually own
4. one uncertainty you can reduce
5. whether a 30–90 day benchmark skeleton path is realistic
6. whether non-public raw human data handling rules are acceptable

Do not send a broad partnership pitch first.

Send one bounded capability.

---

## License

Unless otherwise stated, public helper materials in this repository are intended to align with:

**Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**

This license does not grant:

- CAIS compliance
- Sal-Meter designation
- certification rights
- mark-usage rights
- clinical-use rights
- diagnostic-use rights
- therapeutic-use rights
- authority to speak for SICS
- authority to reinterpret DOI-registered canonical records

---

## Final boundary sentence

**Proxy first as benchmark. Sal-Meter later as core input. Claims never ahead of evidence.**

This repository exists to prepare the comparison layer without confusing it with the molecular–electrochemical Sal-Meter core.
