# Proxy Benchmark Track

Research-stage proxy benchmark support track for **Human-State-Aware AI Interaction**.

This repository prepares synchronized multimodal benchmark infrastructure, metadata discipline, leakage-safe evaluation, baseline models, dashboard drafts, and bounded closed-loop interaction demos for future comparison with Sal-Meter core inputs.

This repository is **not** the Sal-Meter core signal track.

It is a public helper surface for the proxy benchmark track.

---

## Canonical / DOI relationship

This repository is a public technical helper surface for the SICS Human-State Proxy Benchmark Track.

It accompanies, but does not replace, the following DOI-registered public records:

- **SICS Human-State Proxy Benchmark Track — Public Boundary and Program Charter v0.1**  
  Version DOI: `10.5281/zenodo.19837423`  
  Concept DOI / all versions DOI: `10.5281/zenodo.19837422`

- **SICS Human-State Proxy Benchmark Track — Scientific Rationale and Research Value v0.1**  
  Version DOI: `10.5281/zenodo.19837971`  
  Concept DOI: `10.5281/zenodo.19837970`

This repository does not define CAIS.

This repository does not define Sal-Meter.

This repository does not grant CAIS compliance.

This repository does not validate Sal-Meter.

This repository does not publish raw human data.

This repository does not replace DOI-registered SICS / CAIS / Sal-Meter / CCF records.

If this repository conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

---

## Current implementation status

This repository is currently in a public helper implementation stage for the SICS Human-State Proxy Benchmark Track.

It provides schema, synthetic/sample data, and validation scaffolding for structure demonstration only.

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
| Raw human data | Not present | Public repository examples must remain synthetic, mock, placeholder, or sample-structure-only |
| Sal-Meter input | Not present | This repository is not Sal-Meter and does not contain Sal-Meter signal data |
| CAIS compliance claim | Not present | This repository does not grant CAIS compliance |
| Benchmark validation | Not present | No model, dataset, dashboard, sensor stack, or benchmark result is validated by this repository |

---

## Repository structure

```text
proxy-benchmark-track/
  README.md
  LICENSE
  CITATION.cff

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

---

## Current validation path

The current public synthetic/sample package can be structurally checked with:

```bash
pip install jsonschema
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

## What this repository supports

This repository supports:

- synchronized multimodal proxy benchmark infrastructure;
- synthetic/sample package structure;
- metadata schema discipline;
- timestamp and event marker discipline;
- leakage-safe split awareness;
- baseline evaluation scaffolding;
- public/private data separation;
- future A/B comparison support with Sal-Meter inputs;
- non-diagnostic Human-State Cost proxy construct examples;
- dashboard and closed-loop demo scaffolding at a later stage.

---

## What this repository does not support

This repository does **not** support:

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

---

## Human-State Cost boundary

Human-State Cost may appear in this repository only as a **non-diagnostic benchmark construct** or synthetic/example field.

It must not be presented as:

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

Permitted phrasing:

```text
Human-State Cost is a non-diagnostic benchmark construct used to compare measurable proxy burdens across AI interaction conditions.
```

Prohibited phrasing:

```text
Human-State Cost diagnoses the user’s psychological or physiological condition.
```

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
The data is real evidence.
The benchmark is validated.
The model is reliable.
The system is diagnostic.
The system is Sal-Meter.
The system is CAIS-compliant.
```

---

## Current milestone

```text
P1-1 Schema completion: done
P1-2 Synthetic sample package: present
P1-3 Synthetic sample validator: present
P1-4 Synthetic session README: done
Raw human data: not present
Sal-Meter input: not present
CAIS compliance claim: not present
Benchmark validation: not present
```

---

## Next implementation step

The next implementation step is to improve validator usability and repository navigation.

Priority order:

```text
1. Confirm validator path and dependency note in evaluation-baseline/README.md
2. Add a short "How to validate the synthetic sample package" section
3. Keep all public examples synthetic/sample-only
4. Do not publish raw human data
5. Prepare dashboard-mockup boundary scaffolding later
6. Prepare closed-loop-demo-lite boundary scaffolding later
```

---

## Naming rule

Use:

- `synthetic`;
- `sample_structure_only`;
- `mock`;
- `placeholder`;
- `research-stage`;
- `non-diagnostic`;
- `benchmark-support`;
- `public helper schema`;
- `public helper package`;
- `proxy benchmark track`.

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

---

## Authority rule

GitHub is a helper surface.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this repository conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

---

## Current status

```text
Research-stage proxy benchmark helper repository.
Synthetic/sample structure validation only.
Not benchmark evidence.
Not Sal-Meter.
Not CAIS compliance.
No raw human data.
```
