# Synthetic Session 001

This folder contains a public synthetic/sample package for the SICS Human-State Proxy Benchmark Track.

It is provided for structure demonstration only.

It does not contain raw human data.

It does not contain identifiable data.

It does not contain clinical data.

It does not contain Sal-Meter input data.

It does not grant CAIS compliance.

It does not validate benchmark performance.

It does not validate Sal-Meter.

It does not create diagnostic, therapeutic, clinical, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

## Purpose

This synthetic session demonstrates how a minimal public helper package may be organized for the Proxy Benchmark Track.

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
- leakage-risk awareness.

This package is not evidence.

This package is not a benchmark result.

This package is not a human-state dataset.

This package is not a Sal-Meter dataset.

This package is not a CAIS-compliant output.

## Folder contents

```text
sample-data/
  synthetic-session-001/
    session_metadata.json
    streams_manifest.csv
    events.csv
    labels.csv
    qc_report.json
    features_baseline.csv
    splits.json
    operator_log.md
```

## File roles

| File | Role | Notes |
|---|---|---|
| `session_metadata.json` | Session-level metadata | Defines session ID, synthetic status, signal list, sync method, data boundary, and leakage review |
| `streams_manifest.csv` | Stream inventory | Lists synthetic streams, sampling rates, sync status, file paths, and stream-level notes |
| `events.csv` | Event markers | Defines timestamped session, baseline, task, AI interaction, feedback, recovery, and session-end markers |
| `labels.csv` | Label windows | Defines non-diagnostic synthetic window labels for baseline, AI interaction, and recovery |
| `features_baseline.csv` | Synthetic feature table | Provides toy/example HRV, EDA, interaction latency, and Human-State Cost proxy values |
| `qc_report.json` | Quality control report | Records synthetic status, stream checks, leakage review, and public release boundary |
| `splits.json` | Split definition | Demonstrates train/validation/test split structure and leakage notes |
| `operator_log.md` | Operator log | Human-readable synthetic session timeline, QC notes, leakage note, and final boundary |

## Schema alignment

This package is aligned with the helper schemas in:

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

The schemas validate structure only.

They do not validate scientific truth.

They do not validate benchmark performance.

They do not validate human-state inference.

They do not validate Sal-Meter input.

They do not validate CAIS compliance.

## Validation

A local validator is provided at:

```text
evaluation-baseline/validate_sample_package.py
```

To run the validator from the repository root:

```bash
pip install jsonschema
python evaluation-baseline/validate_sample_package.py
```

Expected successful result:

```text
PASS: sample-data/synthetic-session-001 follows the current public helper structure.
```

A successful validation means:

```text
The sample package follows the expected public helper structure.
```

A successful validation does not mean:

```text
The data is real evidence.
The benchmark is validated.
The model is reliable.
The system is diagnostic.
The system is Sal-Meter.
The system is CAIS-compliant.
```

## Public boundary

This folder is public because it contains synthetic/sample structure only.

It must not be used to publish or infer:

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
- certification claims;
- human-ranking outputs.

## Human-State Cost proxy boundary

`features_baseline.csv` includes a synthetic Human-State Cost proxy example value.

This is a toy/example benchmark construct field.

It is not:

- a medical score;
- a psychiatric score;
- a clinical score;
- a consciousness score;
- a psychological safety score;
- an employee monitoring score;
- a user dependence diagnosis;
- a human-ranking measure;
- a certified benchmark output;
- a Sal-Meter output;
- a CAIS output.

Permitted interpretation:

```text
This field demonstrates how a non-diagnostic benchmark construct may be represented in a synthetic feature table.
```

Prohibited interpretation:

```text
This field measures or diagnoses the true physiological, psychological, clinical, or consciousness state of a person.
```

## Leakage note

This synthetic package intentionally exposes labels and condition names for demonstration clarity.

A real benchmark package must not rely on filenames, folder names, condition names, device IDs, session order, operator identity, or preprocessing artifacts as hidden labels.

A real benchmark package must enforce leakage-safe rules across:

- participant;
- day;
- device;
- session;
- condition;
- operator;
- preprocessing pipeline;
- train/validation/test split.

## Naming rule

Use:

- `synthetic`;
- `sample`;
- `sample_structure_only`;
- `mock`;
- `placeholder`;
- `research-stage`;
- `non-diagnostic`;
- `benchmark-support`;
- `public helper package`.

Do not use:

- `validated`;
- `certified`;
- `diagnostic`;
- `therapeutic`;
- `clinical`;
- `CAIS-compliant`;
- `Sal-Meter validated`;
- `consciousness measurement`;
- `human truth score`;
- `psychological safety score`;
- `employee monitoring score`.

## Authority rule

This folder is a GitHub helper surface.

It is not a canonical authority layer.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this folder conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

## Current status

```text
Synthetic sample package.
Structure demonstration only.
Not benchmark evidence.
Not Sal-Meter.
Not CAIS compliance.
No raw human data.
```
