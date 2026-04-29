# Schemas

This folder contains public helper schemas for the SICS Human-State Proxy Benchmark Track.

These schemas are provided to document and validate the structure of the public synthetic/sample package.

They are not canonical authority.

They do not define CAIS.

They do not define Sal-Meter.

They do not grant CAIS compliance.

They do not validate Sal-Meter.

They do not validate benchmark performance.

They do not create diagnostic, therapeutic, clinical, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

## Public boundary

The schemas in this folder are for public helper use only.

They are intended to support:

- synthetic/sample data structure checks;
- metadata consistency;
- timestamp and event marker discipline;
- public/private data separation;
- leakage-risk awareness;
- baseline feature table structure;
- QC report structure;
- future reproducibility helper workflows.

They are not intended to support:

- raw human data publication;
- clinical interpretation;
- diagnostic labeling;
- therapeutic feedback;
- surveillance scoring;
- employment, insurance, educational, legal, or eligibility decisions;
- CAIS compliance claims;
- Sal-Meter validation claims;
- certified benchmark claims.

## Schema files

| File | Validates | Public role |
|---|---|---|
| `session-metadata.schema.json` | `session_metadata.json` | Session-level metadata, synthetic status, signal list, data boundary, leakage review |
| `event-markers.schema.json` | one row object from `events.csv` | Timestamped event markers for session, task, AI interaction, feedback, and recovery events |
| `streams-manifest.schema.json` | one row object from `streams_manifest.csv` | Stream inventory, synthetic signal names, sampling rates, sync status, file paths |
| `labels.schema.json` | one row object from `labels.csv` | Non-diagnostic synthetic/session label windows |
| `qc-report.schema.json` | `qc_report.json` | QC status, stream checks, leakage review, public release boundary |
| `features-baseline.schema.json` | one row object from `features_baseline.csv` | Synthetic baseline feature rows and Human-State Cost proxy example values |
| `splits.schema.json` | `splits.json` | Synthetic split definition, leakage notes, and holdout structure demonstration |

## Expected sample package alignment

The schemas are aligned with the following public synthetic package structure:

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

## Important distinction

These schemas validate structure.

They do not validate scientific truth.

They do not validate human-state inference.

They do not validate Human-State Cost as a certified score.

They do not validate Sal-Meter input.

They do not validate CAIS compliance.

They do not validate clinical, diagnostic, therapeutic, surveillance, employment, insurance, educational, legal, or eligibility use.

## Synthetic/sample data only

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

## Human-State Cost boundary

Human-State Cost may appear in this repository only as a non-diagnostic benchmark construct or synthetic/example field.

It must not be presented as:

- a medical score;
- a psychiatric score;
- a clinical score;
- a consciousness score;
- a psychological safety score;
- an AI harm diagnosis;
- a toxicity diagnosis;
- an employee wellbeing score;
- a user dependence diagnosis;
- a human-ranking measure;
- a certified benchmark output;
- a Sal-Meter output;
- a CAIS output.

Permitted phrasing:

```text
Human-State Cost is a non-diagnostic benchmark construct used to compare measurable proxy burdens across AI interaction conditions.
```

Prohibited phrasing:

```text
Human-State Cost diagnoses the user’s psychological or physiological condition.
```

## Validation posture

These schemas are designed for early public helper validation.

They may be used to check whether a synthetic/sample file has the expected fields, naming conventions, boundary markers, and public release constraints.

They should not be used as proof that a dataset, model, dashboard, lab, device, software stack, or research result is validated.

A valid file means:

```text
The file follows the expected helper structure.
```

A valid file does not mean:

```text
The data is real evidence.
The benchmark is validated.
The model is reliable.
The system is diagnostic.
The system is Sal-Meter.
The system is CAIS-compliant.
```

## Naming rule

Use:

- `synthetic`;
- `sample_structure_only`;
- `mock`;
- `placeholder`;
- `research-stage`;
- `non-diagnostic`;
- `benchmark-support`;
- `public helper schema`.

Do not use:

- `validated`;
- `certified`;
- `diagnostic`;
- `therapeutic`;
- `clinical`;
- `CAIS-compliant`;
- `Sal-Meter validated`;
- `human truth score`;
- `consciousness measurement`;
- `psychological safety score`;
- `employee monitoring score`.

## Authority rule

GitHub is a helper surface.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this repository conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

## Current status

This folder currently provides structure schemas for the public synthetic/sample package.

Status:

```text
Research-stage helper schemas.
Synthetic/sample structure validation only.
Not benchmark evidence.
Not Sal-Meter.
Not CAIS compliance.
No raw human data.
```
