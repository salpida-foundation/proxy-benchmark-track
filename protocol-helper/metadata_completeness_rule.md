# Metadata Completeness Rule

This document defines metadata completeness rules for the **SICS Human-State Proxy Benchmark Track**.

It is a public helper rule document.

It is not the Sal-Meter core signal track.

It does not define CAIS.

It does not grant CAIS compliance.

It does not validate Sal-Meter.

It does not validate benchmark performance.

It does not create diagnostic, therapeutic, clinical, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

---

## Purpose

The purpose of this document is to prevent metadata completeness from becoming a validation claim.

Metadata is necessary for auditability.

Metadata is dangerous when completeness is treated as truth.

This document defines what metadata completeness may mean, what it must not mean, and how completeness should be used in a bounded research-stage public helper repository.

---

## Core rule

Metadata completeness means that required descriptive fields are present, parseable, and reviewable.

Metadata completeness does not mean that the data are scientifically valid.

Metadata completeness does not mean that the benchmark is validated.

Metadata completeness does not mean that a model is reliable.

Metadata completeness does not mean that a sensor is validated.

Metadata completeness does not mean that Sal-Meter has been validated.

Metadata completeness does not mean CAIS compliance.

Correct sentence:

```text
The metadata package is complete enough for helper-structure review.
```

Incorrect sentence:

```text
The metadata package proves the benchmark is valid.
```

---

## Metadata completeness is filing discipline

Metadata completeness is a filing discipline.

It supports:

- reproducibility;
- audit trail;
- reviewability;
- leakage checks;
- public/private boundary checks;
- schema alignment;
- future comparison readiness.

It does not create:

- diagnostic authority;
- clinical interpretation;
- therapeutic authority;
- surveillance authority;
- certification authority;
- device readiness;
- CAIS compliance;
- Sal-Meter validation;
- human-state truth measurement.

A complete file can still be scientifically weak.

An incomplete file cannot be trusted.

---

## Minimum metadata principle

Every public synthetic/sample package should answer five questions:

```text
What is this file?
Where does it belong?
What does it contain?
What does it not contain?
What claims are not being made?
```

If metadata cannot answer these questions, the package is not ready for public helper use.

---

## Required public boundary fields

Every public synthetic/sample package should include explicit boundary fields.

Recommended minimum fields:

```text
schema_version
session_id
dataset_type
public_data_status
synthetic_status_declared
raw_human_data_present
identifiable_data_present
clinical_data_present
sal_meter_input_present
cais_compliance_claim_present
benchmark_validation_claim_present
diagnostic_claim_present
therapeutic_claim_present
surveillance_claim_present
certification_claim_present
human_ranking_claim_present
release_note
final_boundary
```

These fields do not validate the data.

They prevent claim drift.

---

## Required session identity fields

Every session package should include:

```text
session_id
dataset_type
session_date
session_start
session_end
participant_code
condition_label
task_context
```

For public synthetic/sample files, these should remain synthetic, mock, placeholder, or sample-structure-only.

Example:

```json
{
  "session_id": "SYN-SESSION-001",
  "dataset_type": "synthetic",
  "session_date": "2026-04-28",
  "participant_code": "SYN-PARTICIPANT-001",
  "condition_label": "synthetic_ai_interaction_demo",
  "task_context": "Synthetic demonstration of a bounded Human-State-Aware AI interaction benchmark session."
}
```

Allowed meaning:

```text
The session identity is documented for helper-structure review.
```

Not allowed meaning:

```text
The session identity proves a real human-state measurement.
```

---

## Required signal inventory fields

Every signal stream should be documented.

Recommended fields:

```text
signal_name
device
sampling_rate_hz
timestamp_source
sync_method
quality_flag
dropout_note
drift_note
file_path
```

For public synthetic/sample files, signal streams should be clearly synthetic or mock.

Example:

```json
{
  "signal_name": "synthetic_eda",
  "device": "synthetic_generator",
  "sampling_rate_hz": 32,
  "timestamp_source": "synthetic_clock",
  "sync_method": "synthetic_timestamp_alignment",
  "quality_flag": "pass",
  "dropout_note": "No real signal. Synthetic demonstration only.",
  "drift_note": "No real clock drift. Synthetic demonstration only."
}
```

Allowed meaning:

```text
The signal stream is described for helper-structure review.
```

Not allowed meaning:

```text
The signal stream is physiologically validated.
```

---

## Required event marker fields

Every event marker file should document event structure.

Recommended fields:

```text
event_id
session_id
event_type
event_timestamp
event_source
event_description
operator_confirmed
condition_label
```

Allowed meaning:

```text
The event marker is available for timing and audit review.
```

Not allowed meaning:

```text
The event marker proves physiological causality, psychological causality, AI causality, recovery, harm, or consciousness transition.
```

---

## Required label metadata fields

Every label file should document label boundary.

Recommended fields:

```text
label_id
session_id
window_label
label_value
label_source
public_data_status
note
```

Allowed meaning:

```text
The label is documented as a helper marker.
```

Not allowed meaning:

```text
The label is a diagnosis, clinical state, consciousness measurement, Sal-Meter result, CAIS compliance marker, or human-ranking score.
```

---

## Required split metadata fields

Every split file should document how data are separated.

Recommended fields:

```text
split_id
split_strategy
train_sessions
validation_sessions
test_sessions
holdout_sessions
leakage_reviewed
known_leakage_risks
label_visibility
operator_visibility
participant_holdout_applied
session_holdout_applied
device_holdout_applied
time_holdout_applied
note
```

Allowed meaning:

```text
The split structure is documented for leakage-aware review.
```

Not allowed meaning:

```text
The split proves that the model result is scientifically valid.
```

---

## Required QC metadata fields

Every QC report should include:

```text
qc_id
session_id
schema_version_checked
required_files_present
json_parse_passed
csv_parse_passed
metadata_complete
timestamp_format_checked
label_boundary_checked
sync_boundary_checked
leakage_reviewed
raw_human_data_absent
identifiable_data_absent
clinical_data_absent
sal_meter_input_absent
cais_compliance_claim_absent
diagnostic_claim_absent
therapeutic_claim_absent
surveillance_claim_absent
certification_claim_absent
human_ranking_claim_absent
final_qc_status
deviation_note
```

Allowed meaning:

```text
QC indicates whether the helper package passes the defined structural checks.
```

Not allowed meaning:

```text
QC proves benchmark validity, Sal-Meter validity, CAIS compliance, diagnostic authority, clinical authority, therapeutic authority, or certification readiness.
```

---

## Required public release fields

Every public release or public sample package should include:

```text
release_status
public_release_allowed
raw_human_data_public
identifiable_data_public
clinical_data_public
sal_meter_input_public
cais_compliance_claim_public
benchmark_validation_claim_public
release_note
license
authority_note
```

Allowed meaning:

```text
The public release boundary is documented.
```

Not allowed meaning:

```text
The public release is a validated benchmark, validated Sal-Meter implementation, certified device, or CAIS-compliant output.
```

---

## Completeness status values

Recommended values:

```text
complete
partial
missing
not_applicable
unknown
review_required
```

Use carefully.

`complete` means:

```text
The required helper fields are present and reviewable.
```

`complete` does not mean:

```text
The data are true.
The benchmark is valid.
The model is reliable.
The sensor is validated.
The system is Sal-Meter.
The output is CAIS-compliant.
```

---

## Public data status values

Recommended values:

```text
synthetic
sample
sample_structure_only
mock
placeholder
public_helper
not_public
private_restricted
```

For this public repository, preferred values are:

```text
synthetic
sample
sample_structure_only
mock
placeholder
public_helper
```

Avoid uploading anything that requires:

```text
private_restricted
```

unless the file contains only a non-sensitive description and no raw or identifiable data.

---

## Boundary booleans

Boundary booleans should be explicit.

Required public helper values:

```json
{
  "raw_human_data_present": false,
  "identifiable_data_present": false,
  "clinical_data_present": false,
  "sal_meter_input_present": false,
  "cais_compliance_claim_present": false,
  "benchmark_validation_claim_present": false,
  "diagnostic_claim_present": false,
  "therapeutic_claim_present": false,
  "surveillance_claim_present": false,
  "certification_claim_present": false,
  "human_ranking_claim_present": false
}
```

These fields are gates.

If any value is `true`, the file is not appropriate for the current public helper boundary unless a separate governance decision explicitly permits it.

---

## File inventory rule

Every package should list expected files.

For the current public synthetic sample package, expected files include:

```text
sample-data/synthetic-session-001/
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

The file inventory allows review.

The file inventory does not validate performance.

---

## Schema alignment rule

A metadata package should identify which schemas it aligns with.

Relevant schema files may include:

```text
schemas/session-metadata.schema.json
schemas/streams-manifest.schema.json
schemas/event-markers.schema.json
schemas/labels.schema.json
schemas/qc-report.schema.json
schemas/features-baseline.schema.json
schemas/splits.schema.json
```

Schema alignment means:

```text
The file follows the expected helper structure.
```

Schema alignment does not mean:

```text
The file is scientific evidence.
The benchmark is validated.
The system is Sal-Meter.
The system is CAIS-compliant.
```

---

## Completeness versus validation

Completeness is not validation.

Completeness asks:

```text
Are the required fields present?
Are the fields parseable?
Are the fields interpretable?
Are the boundaries explicit?
Are the files reviewable?
```

Validation asks deeper questions:

```text
Is the signal real?
Is the model reliable?
Is the effect reproducible?
Is the benchmark meaningful?
Is the measurement stable?
Is the interpretation justified?
```

This repository currently supports completeness checks.

It does not claim validation.

---

## Completeness versus evidence

A complete synthetic package is structure demonstration.

It is not scientific evidence.

A complete public helper package may support:

```text
documentation clarity
schema testing
validator testing
baseline skeleton testing
public onboarding
review readiness
```

It must not be described as:

```text
human-subject evidence
physiological evidence
clinical evidence
Sal-Meter evidence
CAIS-compliant evidence
validated benchmark evidence
```

---

## Completeness versus reliability

A complete metadata package does not prove reliability.

Reliability requires repeated performance under controlled conditions.

Completeness only shows that the audit structure is present.

Correct sentence:

```text
The metadata completeness check passed for helper-structure review.
```

Incorrect sentence:

```text
The benchmark is reliable because the metadata are complete.
```

---

## Completeness versus reproducibility

Metadata completeness supports reproducibility.

It does not guarantee reproducibility.

A reproducibility-ready package should also include:

```text
raw input inventory
processed file inventory
schema versions
preprocessing version
split version
model version
operator log
QC report
deviation log
environment notes
dependency list
public release boundary
```

Completeness is the door.

Reproducibility is the room.

---

## Completeness versus leakage safety

Metadata completeness does not guarantee leakage safety.

A complete metadata package can still leak labels through:

```text
file names
folder names
session order
participant codes
operator IDs
device IDs
condition labels
timestamp patterns
preprocessing artifacts
dashboard fields
release notes
```

Leakage review must be explicit.

Recommended fields:

```text
leakage_reviewed
known_leakage_risks
labels_visible_for_demo
label_visibility
split_strategy
holdout_strategy
```

A complete package that leaks labels is not evidence.

---

## Minimum metadata completeness checklist

Before publishing a public helper package, check:

```text
[ ] schema_version is present
[ ] dataset_type is present
[ ] public_data_status is present
[ ] synthetic_status_declared is present when applicable
[ ] session_id is present when applicable
[ ] file inventory is present
[ ] timestamp source is declared when applicable
[ ] sync method is declared when applicable
[ ] label boundary is declared when applicable
[ ] split strategy is declared when applicable
[ ] leakage review is declared when applicable
[ ] QC status is declared when applicable
[ ] operator log boundary is clear when applicable
[ ] raw_human_data_present is explicitly false for public helper files
[ ] identifiable_data_present is explicitly false for public helper files
[ ] clinical_data_present is explicitly false for public helper files
[ ] sal_meter_input_present is explicitly false for current proxy sample files
[ ] cais_compliance_claim_present is explicitly false
[ ] diagnostic_claim_present is explicitly false
[ ] therapeutic_claim_present is explicitly false
[ ] surveillance_claim_present is explicitly false
[ ] certification_claim_present is explicitly false
[ ] human_ranking_claim_present is explicitly false
[ ] final_boundary is present
```

If the boundary fields are missing, the metadata are not complete.

---

## Public helper package example

```json
{
  "schema_version": "0.1",
  "session_id": "SYN-SESSION-001",
  "dataset_type": "synthetic",
  "public_data_status": "synthetic",
  "synthetic_status_declared": true,
  "raw_human_data_present": false,
  "identifiable_data_present": false,
  "clinical_data_present": false,
  "sal_meter_input_present": false,
  "cais_compliance_claim_present": false,
  "benchmark_validation_claim_present": false,
  "diagnostic_claim_present": false,
  "therapeutic_claim_present": false,
  "surveillance_claim_present": false,
  "certification_claim_present": false,
  "human_ranking_claim_present": false,
  "release_note": "Synthetic demonstration file only. No raw human data, no participant identifiers, no clinical data, no Sal-Meter input, and no CAIS compliance claim.",
  "final_boundary": "Synthetic sample metadata only. Not benchmark evidence. Not Sal-Meter validation. Not CAIS compliance. Not clinical data."
}
```

This is acceptable because it is explicit.

It is still not evidence.

---

## Unacceptable metadata example

```json
{
  "session_id": "P001",
  "condition_label": "anxiety_detected",
  "diagnosis": "anxiety",
  "sal_meter_validated": true,
  "cais_compliant": true,
  "employee_safety_score": 0.82
}
```

This is not allowed.

It creates diagnostic, Sal-Meter validation, CAIS compliance, and human-ranking claims.

---

## Operator log completeness rule

Operator logs should document what happened without adding prohibited interpretation.

Recommended operator log sections:

```text
session context
file inventory
synthetic/public boundary
event marker confirmation
deviation note
dropout note
QC note
release boundary
```

Operator logs should not contain:

```text
participant name
clinical interpretation
diagnosis
therapy recommendation
relationship blame
employment judgment
insurance judgment
education judgment
legal judgment
human ranking
Sal-Meter validation claim
CAIS compliance claim
```

Operator logs are audit notes.

They are not verdicts.

---

## Deviation metadata rule

Deviations should be documented.

Recommended fields:

```text
deviation_detected
deviation_type
deviation_time
deviation_source
deviation_note
impact_on_metadata
impact_on_sync
impact_on_labels
impact_on_splits
impact_on_public_release
```

A deviation note does not invalidate the file automatically.

A hidden deviation weakens the entire package.

---

## Unknown field rule

Unknown fields should be declared as unknown, not silently omitted.

Use:

```text
unknown
not_applicable
review_required
```

Do not use fake precision.

Bad example:

```text
drift_estimate_ms: 0
```

when drift was not measured.

Better example:

```text
drift_estimate_ms: unknown
drift_note: "No real device clock. Synthetic sample only."
```

Honest uncertainty is stronger than false certainty.

---

## Versioning rule

Every public helper package should document versions.

Recommended version fields:

```text
schema_version
metadata_version
preprocessing_version
model_version
split_version
validator_version
release_version
```

Versioning does not prove validity.

Versioning makes change auditable.

A package without versions is a fogged mirror.

---

## Authority rule

Metadata completeness does not create canonical authority.

This GitHub repository is a helper surface.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this file conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

---

## Relationship to schemas

This document complements:

```text
schemas/
```

The schemas define machine-checkable structure.

This document defines human-readable completeness and boundary rules.

The relationship is:

```text
schemas/ = structural validation helper
metadata_completeness_rule.md = completeness and boundary interpretation helper
```

Neither validates benchmark performance.

Neither validates Sal-Meter.

Neither grants CAIS compliance.

---

## Relationship to sample data

This document complements:

```text
sample-data/
```

Public sample data must remain synthetic, mock, placeholder, or sample-structure-only.

Correct interpretation:

```text
The sample data metadata demonstrate how completeness fields may be represented.
```

Incorrect interpretation:

```text
The sample data metadata prove a real human-state benchmark.
```

---

## Relationship to evaluation baseline

This document complements:

```text
evaluation-baseline/
```

The evaluation baseline validator may check whether required files and fields exist.

That validator checks helper structure.

It does not validate scientific performance.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

Correct interpretation:

```text
The validator reports whether the public synthetic/sample package follows the expected helper structure.
```

Incorrect interpretation:

```text
The validator proves that the benchmark works.
```

---

## Relationship to labels

This document complements:

```text
protocol-helper/session_label_rule.md
```

Metadata completeness must include label boundary fields.

A complete label file must make clear that labels are:

```text
helper labels
synthetic/sample labels when public
non-diagnostic labels
non-clinical labels
non-Sal-Meter labels
non-CAIS-compliance labels
```

Labels that lack boundary metadata should be treated as unsafe.

---

## Relationship to timestamps

This document complements:

```text
protocol-helper/timestamp_sync_rule.md
```

Metadata completeness must include timestamp and synchronization fields when timing matters.

Required timing metadata may include:

```text
timestamp_source
sync_method
sync_quality_flag
drift_note
dropout_note
latency_note
timezone_convention
```

A complete timestamp file does not prove causality.

It only supports auditability.

---

## Human-State Cost metadata boundary

If Human-State Cost proxy fields are used, metadata must state that the construct is bounded.

Required boundary statements:

```text
not a person score
not a diagnosis
not a clinical score
not a psychological safety score
not an employee score
not a legal score
not an insurance score
not an educational score
not an eligibility score
not a consciousness score
not a Sal-Meter output
not CAIS compliance
```

Correct sentence:

```text
Human-State Cost metadata describes a bounded proxy construct for comparing interaction conditions.
```

Incorrect sentence:

```text
Human-State Cost metadata scores the person.
```

---

## Future Sal-Meter A/B comparison metadata boundary

Future Sal-Meter A/B comparison is not open in this public helper repository.

If future comparison becomes available, metadata must clearly separate:

```text
proxy stream metadata
Sal-Meter input metadata
shared event marker metadata
clock source metadata
sync method metadata
raw data boundary
public/private boundary
audit trail
comparison boundary
```

Even then, metadata completeness will not prove Sal-Meter validity.

It will only support comparison review.

---

## Dyadic and mediation metadata boundary

Future dyadic or mediation benchmark metadata must not create legal, clinical, therapeutic, counseling, relationship diagnosis, blame assignment, surveillance, or human-ranking authority.

Required boundary statements:

```text
not legal mediation
not therapy
not counseling
not relationship diagnosis
not fault assignment
not who-is-right determination
not surveillance scoring
not human ranking
not eligibility scoring
```

Correct sentence:

```text
Dyadic metadata describes a simulated or research-stage interaction condition.
```

Incorrect sentence:

```text
Dyadic metadata proves who is right or who is unsafe.
```

---

## Public repository exclusion rule

The following must not be uploaded to this public repository:

```text
raw human biosignals
raw human video
raw human audio
face data
voice data
identifiable participant metadata
private session logs
consent forms containing personal information
health records
clinical records
internal lab human-subject packages
unpublished private human-subject data
Sal-Meter raw input data
CAIS compliance dossiers
```

This public repository is a helper surface.

It is not a data vault.

---

## Metadata release checklist

Before any public release, check:

```text
[ ] No raw human data are present
[ ] No identifiable data are present
[ ] No clinical data are present
[ ] No Sal-Meter input is present
[ ] No CAIS compliance claim is present
[ ] No diagnostic claim is present
[ ] No therapeutic claim is present
[ ] No surveillance claim is present
[ ] No certification claim is present
[ ] No human-ranking claim is present
[ ] Metadata completeness is described as helper-structure completeness only
[ ] Validator output is described as helper-structure validation only
[ ] Release notes do not claim benchmark validation
[ ] Release notes do not claim Sal-Meter validation
[ ] Release notes do not claim CAIS compliance
[ ] DOI authority boundary remains clear
```

If any item fails, hold release.

---

## P2-1 issue alignment

This file implements:

```text
[P2-1] Add protocol helper boundary pack
```

It satisfies:

```text
Create protocol-helper/metadata_completeness_rule.md
```

---

## Completion status

```text
Protocol helper file.
Metadata completeness rule.
Research-stage.
Public helper documentation only.
Completeness discipline only.
Not benchmark evidence.
Not Sal-Meter.
Not CAIS compliance.
No raw human data.
No identifiable data.
No clinical authority.
No diagnostic authority.
No therapeutic authority.
No surveillance authority.
No certification authority.
No human-ranking authority.
```

---

## Final rule

Metadata must make the file reviewable.

Metadata must not make the claim louder.

Completeness is not truth.

Completeness is not validation.

Completeness is not compliance.

Completeness is not Sal-Meter.

Completeness is not CAIS.

A complete false claim is still false.

A complete weak package is still weak.

The purpose of metadata is to keep the evidence path visible before anyone mistakes a shadow for a signal.
