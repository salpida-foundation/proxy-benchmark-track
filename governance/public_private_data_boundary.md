# Public / Private Data Boundary

This document defines the public / private data boundary for the SICS Human-State Proxy Benchmark Track.

This repository is a public technical helper surface.

It is not the canonical authority layer.

It is not the Sal-Meter core signal track.

It is not a CAIS-compliant device implementation.

It is not a clinical, diagnostic, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, or human-ranking system.

---

## 1. Purpose

The purpose of this document is to prevent data-boundary drift.

The SICS Human-State Proxy Benchmark Track may use synchronized multimodal proxy signals, metadata, event markers, synthetic examples, dashboard mockups, baseline model skeletons, and closed-loop demo-lite structures.

However, public technical helper materials must not expose raw human data, identifiable participant data, private session logs, clinical records, or internal lab packages.

This boundary exists to keep the repository useful without making it unsafe.

The public repository should show structure.

It should not expose people.

---

## 2. Current status

research-stage · non-clinical · non-diagnostic · non-therapeutic · non-surveillance · non-coercive · pre-device · pre-certification · pre-compliance · benchmark support only

---

## 3. Repository role

This repository may publicly support:

- metadata schema examples
- event marker examples
- synthetic sample-data structure
- toy data examples
- leakage-control documentation
- reproducibility checklists
- baseline model skeletons
- dashboard mockup documentation
- closed-loop demo-lite boundary notes
- future Sal-Meter A/B comparison placeholders

This repository must not publicly contain:

- raw human biosignals
- identifiable participant records
- raw video from real sessions
- raw audio from real sessions
- face data from real sessions
- private session logs
- private health information
- clinical records
- consent forms containing personal information
- internal lab packages
- unpublished human-subject files

---

## 4. Public data classes

The following materials may be public.

### 4.1 Synthetic data

Synthetic data may be published when it is generated for demonstration only and does not come from a real human participant.

Allowed examples:

- synthetic session metadata
- synthetic event markers
- synthetic signal values
- synthetic feature tables
- synthetic split files
- synthetic QC reports
- toy benchmark outputs

Required label:

- The file must clearly state that it is synthetic.

Recommended wording:

Synthetic data only. No real human participant data is included.

---

### 4.2 Toy data

Toy data may be published when it is minimal, artificial, and used only to demonstrate file structure or code behavior.

Allowed examples:

- toy CSV files
- toy JSON files
- toy split examples
- toy baseline outputs
- toy dashboard fields

Toy data must not be presented as evidence.

Toy data must not be presented as benchmark performance.

---

### 4.3 Schema-only examples

Schema-only examples may be published when they define structure without exposing private records.

Allowed examples:

- JSON schemas
- CSV column definitions
- metadata field dictionaries
- event marker templates
- QC report templates
- split-rule templates

Schema-only materials should be treated as public helper documentation.

They do not create canonical authority.

---

### 4.4 Documentation

Documentation may be public when it explains:

- file structure
- metadata logic
- leakage-control logic
- reproducibility logic
- dashboard boundary
- closed-loop demo-lite boundary
- contribution rules
- prohibited claims
- public/private separation

Documentation must not include private operational details that expose real participants, internal security practices, unpublished human data, or confidential laboratory records.

---

## 5. Private data classes

The following materials must remain private unless separately reviewed, approved, de-identified, and authorized under a controlled release pathway.

### 5.1 Raw human biosignals

Private by default:

- ECG
- HRV
- EDA
- PPG
- EEG
- respiration
- skin temperature
- eye-tracking data
- gaze data
- webcam-derived face markers
- audio-derived voice markers
- motion / IMU data
- keystroke timing from real participants
- interaction timing from real participants

Raw human biosignals must not be uploaded to this public repository.

---

### 5.2 Raw video, audio, and face data

Private by default:

- webcam recordings
- facial video
- facial landmarks from identifiable sessions
- eye video
- gaze video
- voice recordings
- raw audio
- speech recordings
- screen recordings involving identifiable users

These materials create heightened privacy and identity risk.

They must not be published in this repository.

---

### 5.3 Participant records

Private by default:

- name
- email address
- phone number
- address
- resident registration number
- medical record number
- date of birth
- workplace
- school
- exact location
- signed consent form
- payment record
- appointment record
- session scheduling record
- private contact record

No direct identifier belongs in this public repository.

---

### 5.4 Clinical or health records

Private by default:

- medical history
- diagnosis
- medication list
- psychiatric information
- treatment records
- laboratory test records
- medical images
- clinician notes
- hospital records
- insurance records
- health questionnaire responses

This repository is not a medical, clinical, diagnostic, or therapeutic repository.

Clinical or health records must not be uploaded.

---

### 5.5 Internal lab packages

Private by default:

- raw lab data package
- internal QC logs
- internal deviation logs
- internal audit trail
- operator identity records
- internal review comments
- unpublished benchmark data
- contractor deliverables
- unpublished external-lab data
- raw pilot data
- internal participant session exports

Internal lab packages must remain outside the public repository unless a separate public-release review approves a synthetic or non-identifying derivative.

---

## 6. Public release rule

A file may be public only if it satisfies all of the following:

1. It contains no direct identifier.
2. It contains no raw human data.
3. It contains no real face, voice, video, or audio data.
4. It contains no clinical or diagnostic data.
5. It contains no private session log.
6. It contains no unpublished internal lab package.
7. It is clearly labeled as synthetic, toy, mock, schema-only, or public documentation.
8. It does not imply Sal-Meter validation.
9. It does not imply CAIS compliance.
10. It does not create clinical, diagnostic, therapeutic, surveillance, eligibility, or human-ranking use.

If any of the above conditions fail, the file must not be published in this repository.

---

## 7. Naming rule

Public files should use names that make their data status obvious.

Preferred:

- synthetic-session-001
- synthetic-event-markers.csv
- synthetic-metadata-example.json
- toy-baseline-output.csv
- mock-dashboard-fields.json
- schema-example.json

Avoid:

- real-session-001
- participant-001
- subject-raw
- patient-data
- stress-diagnosis
- clinical-score
- sal-meter-validation
- cais-compliant-output
- human-ranking-output

File names should not contain hidden labels that could create leakage.

---

## 8. Folder rule

### Public folders

The following folders may contain public helper materials:

- docs/
- governance/
- schemas/
- sample-data/
- evaluation-baseline/
- protocol-helper/
- dashboard-mockup/
- closed-loop-demo-lite/
- replication-guide/

### Public sample-data folder

The sample-data/ folder may contain:

- synthetic data
- toy data
- mock data
- schema demonstrations
- non-identifying example files

The sample-data/ folder must not contain raw human data.

### Private storage

Private raw data, if ever collected under appropriate governance, must be stored outside this public repository.

This repository should not disclose the location, credentials, access tokens, or security details of any private storage system.

---

## 9. De-identification warning

De-identification does not automatically make human data safe for public release.

Physiological time-series, face data, voice data, eye-tracking data, behavioral timing, and interaction logs can remain sensitive even after names are removed.

Therefore:

- de-identified raw human data must not be uploaded to this repository by default
- pseudonymized human data must not be uploaded to this repository by default
- coded participant data must not be uploaded to this repository by default
- aggregated human-derived outputs require separate review before release

The default public posture is synthetic-first.

---

## 10. Human-State Cost boundary

Human-State Cost, if referenced in this repository, is a non-diagnostic benchmark construct.

It may compare interaction conditions.

It must not rank, diagnose, classify, score, or govern human beings.

Correct use:

- comparing AI interaction condition A versus condition B
- comparing proxy burden across bounded non-clinical sessions
- evaluating whether a feedback loop reduces avoidable proxy burden

Incorrect use:

- diagnosing stress
- ranking people
- scoring psychological safety
- classifying consciousness
- evaluating employment suitability
- evaluating insurance risk
- creating educational eligibility
- creating medical or psychiatric conclusions

Human-State Cost belongs to benchmark comparison.

It does not belong to human judgment.

---

## 11. Dashboard boundary

Public dashboard mockups may display:

- stream status
- timestamp quality
- packet loss
- session phase
- event marker timing
- proxy trend
- QC status
- synthetic Human-State Cost trend as a non-diagnostic benchmark construct

Public dashboard mockups must not display:

- diagnosis
- clinical stress score
- psychological safety score
- consciousness truth score
- human ranking score
- employment score
- insurance score
- medical status
- Sal-Meter validation status
- CAIS compliance status

Dashboard mockups are technical helper surfaces.

They are not decision systems.

---

## 12. Closed-loop demo-lite boundary

Closed-loop demo-lite materials may demonstrate:

- reversible feedback timing
- UI pacing adjustment
- local interaction pacing
- simulator event adjustment
- non-coercive feedback
- human-overridable interaction control
- synthetic feedback event logs

Closed-loop demo-lite materials must not claim:

- therapy
- diagnosis
- medical intervention
- stress treatment
- psychiatric monitoring
- coercive nudging
- behavioral control
- employee monitoring
- student monitoring
- clinical safety management

Closed-loop means interaction feedback.

It does not mean clinical intervention.

---

## 13. Future Sal-Meter A/B comparison boundary

This repository may prepare future comparison structure for Sal-Meter I/G-channel inputs.

It must not imply that Sal-Meter input data is already available.

It must not imply that Sal-Meter has already been validated by this proxy stack.

It must not imply that proxy signals are Sal-Meter signals.

Permitted language:

- future comparison with Sal-Meter inputs
- future A/B comparison surface
- benchmark support layer
- proxy baseline for later comparison

Prohibited language:

- proxy data validates Sal-Meter
- proxy stack is Sal-Meter
- non-molecular Sal-Meter
- CAIS-compliant proxy benchmark
- Sal-Meter-equivalent proxy system

The proxy benchmark track prepares a comparison lane.

It does not become the core signal track.

---

## 14. Review before release

Before any new public data-like file is committed, ask:

1. Is this synthetic, toy, mock, schema-only, or documentation?
2. Does it contain any real human signal?
3. Does it contain any identifier?
4. Does it contain any face, voice, video, audio, or location information?
5. Does it contain private session logs?
6. Does it contain clinical or health information?
7. Does it imply diagnosis, treatment, monitoring, or human ranking?
8. Does it imply Sal-Meter validation?
9. Does it imply CAIS compliance?
10. Is the public boundary clearly stated?

If any answer creates uncertainty, do not publish the file.

---

## 15. Contributor rule

Contributors must not submit:

- raw human data
- private human-subject data
- clinical data
- health records
- real participant video
- real participant audio
- face data
- identifiable metadata
- private session logs
- internal lab packages
- claim-inflating dashboard outputs
- Sal-Meter validation claims
- CAIS compliance claims

Contributors may submit:

- schema improvements
- synthetic examples
- documentation improvements
- leakage-risk reports
- reproducibility checklists
- dashboard boundary suggestions
- mock event logs
- toy evaluation code
- public-language corrections

---

## 16. Incident rule

If private or prohibited data is accidentally committed:

1. Stop further public use of the file.
2. Remove the file from the repository.
3. Notify the repository maintainer.
4. Review whether commit history cleanup is required.
5. Document the incident internally.
6. Replace the file only with synthetic or schema-only material.
7. Add a boundary correction note if public wording caused the mistake.

Do not normalize accidental publication.

Boundary failure must be treated as a structural issue.

---

## 17. Authority rule

This repository is a public technical helper surface.

It does not override DOI-registered SICS / CAIS / Sal-Meter / CCF records.

If this document conflicts with a higher-level DOI-registered canonical or public boundary record, the higher-level DOI-registered record prevails automatically.

---

## 18. Final boundary

Public means structure, not exposure.

Private means human record, not hidden weakness.

The purpose of this repository is to make benchmark architecture understandable without making human data public.

No raw human data belongs in this repository.
