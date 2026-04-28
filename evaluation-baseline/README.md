# Evaluation Baseline

This folder contains baseline evaluation skeletons for the SICS Human-State Proxy Benchmark Track.

This is a research-stage, non-clinical, non-diagnostic, non-therapeutic benchmark support folder.

It is not the Sal-Meter core signal track.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not create clinical, diagnostic, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

---

## Purpose

The purpose of this folder is to demonstrate how synthetic proxy benchmark data may be loaded, checked, split, and passed into transparent baseline modeling code.

The first goal is not high model performance.

The first goal is an auditable evaluation skeleton.

---

## Current files

```text
evaluation-baseline/
  README.md
  requirements.txt
  baseline_pipeline_skeleton.py
  leakage_safe_split_example.py
```

---

## Expected sample input

The current skeleton expects the synthetic sample package:

```text
sample-data/synthetic-session-001/
  session_metadata.json
  features_baseline.csv
  labels.csv
  splits.json
  qc_report.json
```

This input is synthetic only.

It is not real human data.

It is not benchmark evidence.

It is not Sal-Meter data.

It is not CAIS-compliant output.

---

## Boundary

Allowed:

- synthetic feature loading
- toy baseline processing
- leakage-safe split demonstration
- schema and file-structure checking
- transparent model skeletons
- reproducibility examples

Not allowed:

- raw human data
- real participant data
- real webcam data
- real audio data
- face data
- clinical data
- diagnostic claims
- therapeutic claims
- human ranking
- surveillance scoring
- Sal-Meter validation claims
- CAIS compliance claims

---

## How to run locally

From the repository root:

```bash
pip install -r evaluation-baseline/requirements.txt
python evaluation-baseline/baseline_pipeline_skeleton.py
python evaluation-baseline/leakage_safe_split_example.py
```

The current synthetic sample contains only a tiny number of rows.

Therefore, the scripts are designed to demonstrate structure and safety checks, not meaningful model performance.

---

## Baseline philosophy

Initial baselines should be boring.

Preferred properties:

- transparent
- reproducible
- leakage-aware
- metadata-aware
- synthetic-safe
- easy to audit
- explicit about limitations

Avoid:

- leaderboard framing
- deep learning performance claims
- clinical scoring
- diagnostic interpretation
- hidden preprocessing
- tuning on final holdout data
- reporting synthetic output as evidence

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
```

---

## Final rule

A result that cannot be replayed is not benchmark evidence.

A result that leaks labels is not evidence.

A result based on synthetic data is structure demonstration, not scientific proof.
