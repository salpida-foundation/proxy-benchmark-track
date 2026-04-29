# Protocol Helper

This folder contains public helper rules for the **SICS Human-State Proxy Benchmark Track**.

It exists to make the proxy benchmark track auditable, bounded, and harder to misinterpret.

It is not the Sal-Meter core signal track.

It does not define CAIS.

It does not grant CAIS compliance.

It does not validate Sal-Meter.

It does not validate benchmark performance.

It does not introduce raw human data.

It does not create clinical, diagnostic, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

---

## Purpose

The purpose of this folder is to document helper-level rules for:

- session labeling;
- timestamp and synchronization discipline;
- metadata completeness;
- Human-State Cost proxy construct boundaries;
- future comparison with Sal-Meter core inputs.

These files support structure.

They do not prove scientific validity.

They do not certify a benchmark.

They do not validate any device, model, physiological interpretation, psychological interpretation, clinical interpretation, or consciousness measurement claim.

---

## Public boundary

This folder is public helper documentation only.

It may be used to explain:

- how synthetic/sample sessions should be labeled;
- how event timing should be described;
- how metadata completeness should be checked;
- how leakage risks should be reduced;
- how future Sal-Meter A/B comparison should be bounded;
- how proxy benchmark outputs should be described without overclaiming.

It must not be used to claim:

- benchmark validation;
- Sal-Meter validation;
- CAIS compliance;
- clinical utility;
- diagnostic authority;
- therapeutic effect;
- surveillance readiness;
- certification readiness;
- human truth measurement;
- psychological safety scoring;
- employee monitoring authority;
- legal or eligibility scoring authority.

---

## Planned files

```text
protocol-helper/
  README.md
  session_label_rule.md
  timestamp_sync_rule.md
  metadata_completeness_rule.md
  human_state_cost_construct_note.md
  future_sal_meter_ab_comparison_rule.md
```

| File | Role | Boundary |
|---|---|---|
| `README.md` | Folder-level scope and boundary | Public helper documentation only |
| `session_label_rule.md` | Rules for session labels and condition labels | Labels are non-diagnostic helper labels only |
| `timestamp_sync_rule.md` | Rules for timestamps, event markers, and synchronization notes | Timing discipline only, not physiological truth |
| `metadata_completeness_rule.md` | Required metadata completeness logic | Completeness check only, not validation |
| `human_state_cost_construct_note.md` | Boundary for Human-State Cost proxy construct | Interaction-condition proxy only, not a person score |
| `future_sal_meter_ab_comparison_rule.md` | Future A/B comparison boundary between proxy inputs and Sal-Meter inputs | Future comparison rule only, not current Sal-Meter validation |

---

## Work order

Create the files in this order:

```text
1. protocol-helper/README.md
2. protocol-helper/session_label_rule.md
3. protocol-helper/timestamp_sync_rule.md
4. protocol-helper/metadata_completeness_rule.md
5. protocol-helper/human_state_cost_construct_note.md
6. protocol-helper/future_sal_meter_ab_comparison_rule.md
```

Reason:

```text
README first.
Labels second.
Time third.
Metadata fourth.
Human-State Cost boundary fifth.
Future Sal-Meter A/B comparison last.
```

The folder must lock the language before it expands into dashboards, closed-loop demos, or contributor templates.

---

## Relationship to the proxy benchmark track

The proxy benchmark track is a benchmark-support track.

It prepares infrastructure for:

- synchronized multimodal capture;
- event marker discipline;
- metadata discipline;
- leakage-aware evaluation;
- synthetic/sample package structure;
- baseline model skeletons;
- future comparison against Sal-Meter core inputs.

It does not replace Sal-Meter.

It is not a proxy Sal-Meter.

It is not a Sal-Meter validation pathway.

It is not a CAIS compliance pathway.

---

## Relationship to Sal-Meter

Sal-Meter remains the core signal track.

The proxy benchmark track may later provide comparison infrastructure.

The correct future relationship is:

```text
Proxy benchmark output: comparison baseline.
Sal-Meter core input: future core signal candidate.
A/B comparison: future bounded comparison after proper input availability.
```

The incorrect relationship is:

```text
Proxy benchmark = Sal-Meter.
Proxy signal = CAIS signal.
Proxy score = consciousness measurement.
Synthetic sample = scientific evidence.
Dashboard mockup = validated system.
```

Do not use the incorrect relationship.

---

## Relationship to schemas

This folder complements:

```text
schemas/
```

The schemas describe machine-checkable file structures.

The protocol helper documents describe human-readable rules.

The relationship is:

```text
schemas/ = structural validation helper
protocol-helper/ = rule and boundary explanation helper
```

Neither folder validates benchmark performance.

Neither folder validates Sal-Meter.

Neither folder grants CAIS compliance.

---

## Relationship to sample data

This folder complements:

```text
sample-data/
```

The sample data folder contains synthetic/sample structure examples.

The protocol helper folder explains how those structures should be interpreted.

Correct interpretation:

```text
The sample data demonstrates structure.
The helper rules explain boundaries.
The validator checks file structure.
The baseline folder demonstrates toy processing.
```

Incorrect interpretation:

```text
The sample data proves human-state measurement.
The helper rules prove a benchmark.
The validator proves scientific validity.
The baseline model proves system performance.
```

---

## Relationship to evaluation baseline

This folder complements:

```text
evaluation-baseline/
```

The evaluation baseline folder contains skeleton code and validation helpers.

The protocol helper folder explains the rule boundaries that the evaluation folder should respect.

Correct use:

```text
Use protocol-helper/ to understand what labels, timestamps, metadata, Human-State Cost, and future A/B comparison are allowed to mean.
```

Incorrect use:

```text
Use protocol-helper/ as evidence that a model, sensor, dashboard, Sal-Meter input, or CAIS implementation has been validated.
```

---

## Core helper principles

### 1. Labels are not diagnoses

Session labels and condition labels are helper labels.

They are not clinical labels.

They are not diagnostic labels.

They are not mental-health labels.

They are not consciousness labels.

They are not safety labels.

They are not eligibility labels.

They exist to organize synthetic/sample or research-stage benchmark structure.

---

### 2. Timestamps are not physiology

Timestamps support alignment.

They do not prove biological causality.

They do not prove psychological causality.

They do not prove consciousness-state transition.

They do not prove AI effect.

They only document when something was recorded, marked, or aligned.

---

### 3. Metadata completeness is not validation

Metadata completeness means the required descriptive fields are present.

It does not mean:

- the data are scientifically valid;
- the model is reliable;
- the sensor is validated;
- the session is clinically meaningful;
- the benchmark is ready for certification;
- the output is Sal-Meter;
- the output is CAIS compliance.

Metadata completeness is a filing discipline.

It is not a truth claim.

---

### 4. Human-State Cost is not a person score

Human-State Cost is a proxy construct for benchmark-support use.

It evaluates an interaction condition.

It must not be used to rank people.

It must not be used as a clinical score.

It must not be used as a diagnostic score.

It must not be used as a psychological safety score.

It must not be used as an employment, insurance, educational, legal, or eligibility score.

Correct sentence:

```text
Human-State Cost evaluates the interaction condition, not the person.
```

---

### 5. Future Sal-Meter A/B comparison is not open yet

Future Sal-Meter A/B comparison is a later comparison boundary.

It is not currently a validated bridge.

It is not current CAIS compliance.

It is not current Sal-Meter validation.

It is not a claim that proxy data are equivalent to Sal-Meter data.

Correct sentence:

```text
Future Sal-Meter A/B comparison may be defined only after Sal-Meter core inputs are available under the proper boundary, metadata, and audit conditions.
```

---

## Required language

Use:

```text
research-stage
public helper
synthetic/sample
proxy benchmark support
non-diagnostic
non-clinical
non-therapeutic
non-surveillance
non-coercive
metadata discipline
leakage-aware
structure demonstration
future comparison boundary
```

Do not use:

```text
validated
certified
diagnostic
therapeutic
clinical
CAIS-compliant
Sal-Meter validated
consciousness measurement
human truth score
psychological safety score
employee monitoring score
medical device
clinical decision support
surveillance score
eligibility score
```

---

## Minimum public-data rule

No raw human data belongs in this folder.

No identifiable participant data belongs in this folder.

No clinical data belongs in this folder.

No face data belongs in this folder.

No raw voice data belongs in this folder.

No raw video data belongs in this folder.

No private session logs belong in this folder.

No consent forms containing personal information belong in this folder.

No unpublished human-subject package belongs in this folder.

---

## Minimum metadata rule

Every future sample or demonstration package should make the following boundary visible:

```text
dataset_type
public_data_status
raw_human_data_present
identifiable_data_present
clinical_data_present
sal_meter_input_present
cais_compliance_claim_present
synthetic_status_declared
leakage_review
final_boundary
```

The purpose is not to make a claim stronger.

The purpose is to prevent a weak claim from escaping.

---

## Minimum leakage rule

A future benchmark package must not allow labels to leak through:

- filenames;
- folder names;
- session order;
- participant IDs;
- operator IDs;
- device IDs;
- condition labels;
- timestamp artifacts;
- preprocessing artifacts;
- public/private split mistakes.

Leakage control is not optional.

A result that leaks labels is not evidence.

---

## Minimum audit rule

A future benchmark package should preserve:

- raw input file inventory;
- processed file inventory;
- schema version;
- preprocessing version;
- split version;
- model version;
- operator log;
- QC report;
- deviation log;
- public release boundary;
- reproducibility checklist.

Audit trail is the skeleton of trust.

Without audit trail, performance is noise wearing a crown.

---

## P2-1 issue alignment

This folder implements:

```text
[P2-1] Add protocol helper boundary pack
```

P2-1 is complete when this folder contains bounded helper documents that clarify:

- session label rules;
- timestamp and synchronization discipline;
- metadata completeness;
- Human-State Cost construct limits;
- future Sal-Meter A/B comparison boundaries.

---

## Completion checklist

P2-1 checklist:

```text
[ ] Create protocol-helper/README.md
[ ] Create protocol-helper/session_label_rule.md
[ ] Create protocol-helper/timestamp_sync_rule.md
[ ] Create protocol-helper/metadata_completeness_rule.md
[ ] Create protocol-helper/human_state_cost_construct_note.md
[ ] Create protocol-helper/future_sal_meter_ab_comparison_rule.md
```

This README satisfies:

```text
Create protocol-helper/README.md
```

The remaining files should be created one by one.

---

## Authority rule

This folder is a GitHub helper surface.

It is not a canonical authority layer.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this folder conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

---

## Current status

```text
Protocol helper folder.
Research-stage.
Public helper documentation only.
Not benchmark evidence.
Not Sal-Meter.
Not CAIS compliance.
No raw human data.
No identifiable data.
No clinical data.
No diagnostic authority.
No therapeutic authority.
No certification authority.
```

---

## Final rule

A rule that cannot prevent overclaiming is not a rule.

A label that becomes a diagnosis has failed.

A timestamp that becomes causality has failed.

Metadata that becomes validation has failed.

A proxy score that ranks a person has failed.

A future comparison that pretends to be current validation has failed.

This folder exists to keep the proxy benchmark track bounded before it grows.
