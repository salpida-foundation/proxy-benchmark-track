# Sample Data Boundary

This folder is reserved for public synthetic, toy, mock, placeholder, or non-identifying sample-structure data only.

No raw human data belongs in this repository.

This folder exists to demonstrate file structure, metadata discipline, schema alignment, and public release boundaries for the SICS Human-State Proxy Benchmark Track.

It does not provide benchmark evidence.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not create clinical, diagnostic, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

---

## Scope

This folder may contain public sample packages that demonstrate:

- synthetic session structure;
- synthetic event markers;
- synthetic metadata examples;
- synthetic stream manifests;
- synthetic label windows;
- synthetic QC reports;
- toy feature tables;
- split-file examples;
- operator-log examples;
- schema demonstration files;
- generated examples for notebooks;
- non-identifying mock data.

The purpose is structure demonstration.

The purpose is not scientific proof.

---

## Current sample package

Current public sample package:

```text
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
```

This package is synthetic.

It is not real human data.

It is not clinical data.

It is not Sal-Meter data.

It is not CAIS-compliant output.

It is not benchmark evidence.

---

## Allowed here

Allowed materials:

- synthetic session examples;
- synthetic event markers;
- synthetic metadata examples;
- synthetic stream manifests;
- synthetic label windows;
- synthetic QC reports;
- toy feature tables;
- synthetic split definitions;
- operator-log examples without human identifiers;
- schema demonstration files;
- non-identifying mock data;
- generated examples for notebooks;
- public helper files for structure demonstration.

---

## Not allowed here

Do not upload:

- raw human biosignals;
- raw human video;
- raw human audio;
- face data;
- voice data;
- webcam recordings;
- identifiable participant metadata;
- participant identity mapping files;
- private session logs;
- consent forms containing personal information;
- health records;
- clinical records;
- diagnostic labels;
- therapeutic recommendations;
- private lab packages;
- unpublished human-subject files;
- Sal-Meter input data;
- CAIS compliance claims;
- certification claims.

---

## Public release rule

Before any file is added to this folder, confirm:

```text
raw_human_data_present == false
identifiable_data_present == false
clinical_data_present == false
sal_meter_input_present == false
cais_compliance_claim_present == false
```

If any of the above cannot be confirmed, the file does not belong in this public repository.

---

## Naming convention

Suggested naming:

```text
synthetic-session-example.csv
synthetic-event-markers.csv
synthetic-metadata-example.json
synthetic-streams-manifest.csv
synthetic-labels.csv
synthetic-qc-report.json
toy-baseline-output.csv
mock-dashboard-fields.json
sample-structure-only.json
```

Use names that make the public boundary visible.

Do not publish ambiguous data.

---

## Required note inside sample files

Every sample file should clearly indicate whether it is:

```text
synthetic
sample_structure_only
toy
mock
placeholder
```

Avoid filenames, folder names, row IDs, or metadata values that could be mistaken for real participant data.

---

## Boundary language

Use:

```text
synthetic sample package
sample structure demonstration
toy example
mock data
public helper file
non-identifying example
schema demonstration
```

Do not use:

```text
validated dataset
clinical dataset
diagnostic dataset
real participant dataset
Sal-Meter dataset
CAIS-compliant dataset
certified benchmark dataset
human-state diagnosis
psychological safety score
consciousness measurement
```

---

## Leakage caution

Even synthetic files should not teach bad benchmark habits.

Avoid:

- labels hidden in filenames;
- labels hidden in folder names;
- labels hidden in device IDs;
- labels hidden in operator IDs;
- session order that trivially reveals condition;
- public files that imply real physiological evidence;
- synthetic labels presented as scientific truth.

A public sample file should demonstrate structure without creating false evidence.

---

## Relationship to schemas

The sample files in this folder should align with the public helper schemas in:

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

Schema alignment means:

```text
The file follows the expected helper structure.
```

Schema alignment does not mean:

```text
The data is real evidence.
The benchmark is validated.
The model is reliable.
The system is diagnostic.
The system is Sal-Meter.
The system is CAIS-compliant.
```

---

## Final rule

Public sample data exists to demonstrate structure.

It does not exist to disclose private human records.

It does not exist to prove benchmark performance.

It does not exist to validate Sal-Meter.

It does not exist to grant CAIS compliance.
