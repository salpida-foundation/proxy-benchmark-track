# Metadata Completeness Checklist

This checklist defines whether the public helper package for the **SICS Human-State Proxy Benchmark Track** contains enough metadata to be structurally reviewable.

It checks metadata completeness.

It does not validate benchmark performance.

It does not validate Sal-Meter.

It does not define CAIS.

It does not grant CAIS compliance.

It does not introduce raw human data.

It does not create diagnostic, clinical, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

It does not publish a release.

---

## Purpose

Metadata is the skeleton of reproducibility.

Without metadata, a file is only a fragment.

Without file mapping, a package cannot be audited.

Without timestamps, a stream cannot be aligned.

Without event markers, a session cannot be interpreted.

Without label-window boundaries, labels can become false truth.

Without public/private boundary fields, a public helper package can drift into unsafe data disclosure.

This checklist exists to make the public helper package inspectable without overclaiming validation.

Metadata completeness means:

```text
A reviewer can understand what each file is, what it represents, how it is bounded, and what it must not be used to claim.
```

Metadata completeness does not mean:

```text
The benchmark is valid.
The model is valid.
The proxy signals measure consciousness.
The repository validates Sal-Meter.
The repository grants CAIS compliance.
The package is clinical, diagnostic, therapeutic, surveillance-ready, certification-ready, or device-ready.
```

---

## Current status

```text
Checklist type: metadata completeness readiness
Track: SICS Human-State Proxy Benchmark Track
Repository: salpida-foundation/proxy-benchmark-track
Scope: public helper structure
Data status: synthetic/sample/mock/placeholder only
Validation status: not validated
Sal-Meter status: not present
CAIS compliance status: not granted
Clinical status: not clinical
Diagnostic status: not diagnostic
Therapeutic status: not therapeutic
Surveillance status: not surveillance
Certification status: not certification
Human-ranking status: not human ranking
Release status: not published by this checklist
```

---

## Decision language

Use only the following decision language:

```text
Go
  Metadata is complete enough for structural public-helper review.

Conditional Go
  Metadata is mostly complete, but one bounded non-authority correction remains.

Hold
  A required metadata field, mapping field, boundary field, timestamp field, schema reference, or audit note is missing.

No-Go
  Metadata contains raw human data, identifiable data, clinical data, private user data, Sal-Meter input, CAIS compliance claims, benchmark validation claims, diagnostic claims, therapeutic claims, surveillance claims, certification claims, or human-ranking claims.
```

No-Go protects the boundary.

Hold protects the evidence.

Go means the map is readable.

Go does not mean the mountain has been reached.

---

## Metadata completeness principle

A public helper package is metadata-complete only when another reviewer can answer:

```text
What is this package?
What is synthetic?
What is sample?
What is mock?
What is placeholder?
What schema applies?
What file maps to what role?
What timestamps exist?
What events exist?
What labels exist?
What streams exist?
What QC notes exist?
What split definitions exist?
What boundary fields are present?
What data are excluded?
What claims are prohibited?
What remains blocked?
What can be reviewed?
What cannot be claimed?
```

If those questions cannot be answered, decision is:

```text
Hold
```

---

## Required metadata layers

The public helper package should make these layers reviewable:

```text
package-level metadata
session-level metadata
stream-level metadata
event-marker metadata
label-window metadata
feature-table metadata
QC metadata
split metadata
operator/audit metadata
dashboard metadata
closed-loop demo-lite metadata
schema reference metadata
public/private boundary metadata
release-readiness metadata
```

Each layer must remain bounded.

No layer may imply benchmark validation, Sal-Meter validation, CAIS compliance, clinical authority, diagnostic authority, therapeutic authority, surveillance authority, certification authority, or human-ranking authority.

---

## Package-level metadata checklist

```text
[ ] Repository name is clear.
[ ] Track name is clear.
[ ] Repository purpose is clear.
[ ] Repository status is marked research-stage.
[ ] Repository status is marked public-helper-only.
[ ] Repository status is marked non-clinical.
[ ] Repository status is marked non-diagnostic.
[ ] Repository status is marked non-therapeutic.
[ ] Repository status is marked non-surveillance.
[ ] Repository status is marked non-certification.
[ ] Repository status is marked non-human-ranking.
[ ] Repository status states not Sal-Meter.
[ ] Repository status states not CAIS compliance.
[ ] Repository status states not benchmark validation.
[ ] Repository status states no raw human data.
[ ] Repository status states no identifiable data.
[ ] Repository status states no clinical data.
[ ] Repository status states no private user data.
[ ] Repository status states no Sal-Meter input.
[ ] Repository status states no production automation.
[ ] Repository status states no live intervention.
[ ] Repository status states GitHub is a helper surface.
[ ] Repository status states DOI records govern authority.
```

---

## Root README metadata checklist

```text
[ ] Root README includes one-sentence purpose.
[ ] Root README includes current status.
[ ] Root README includes canonical / DOI relationship.
[ ] Root README distinguishes Sal-Meter Core Track from Proxy Benchmark Track.
[ ] Root README includes data boundary.
[ ] Root README includes repository structure.
[ ] Root README includes schema helper pack summary.
[ ] Root README includes synthetic sample package summary.
[ ] Root README includes evaluation baseline summary.
[ ] Root README includes protocol helper summary.
[ ] Root README includes dashboard mockup summary.
[ ] Root README includes closed-loop demo-lite summary.
[ ] Root README includes replication guide summary or can be updated to include it.
[ ] Root README includes release hold conditions.
[ ] Root README includes citation guidance.
[ ] Root README includes governance rule.
[ ] Root README includes naming rule.
[ ] Root README includes final boundary sentence.
```

---

## Session metadata checklist

For `sample-data/synthetic-session-001/session_metadata.json` or equivalent session metadata:

```text
[ ] session_id is present.
[ ] dataset_type is present.
[ ] dataset_type is synthetic, sample, mock, toy, placeholder, or sample-structure-only.
[ ] synthetic_status_declared is present.
[ ] synthetic_status_declared is true.
[ ] track name is present.
[ ] repository name is present.
[ ] session purpose is present.
[ ] session status is public-helper-only.
[ ] non-clinical status is present.
[ ] non-diagnostic status is present.
[ ] non-therapeutic status is present.
[ ] non-surveillance status is present.
[ ] non-certification status is present.
[ ] non-human-ranking status is present.
[ ] Sal-Meter input status is present.
[ ] Sal-Meter input status is not_present or future_placeholder_only.
[ ] CAIS compliance status is present.
[ ] CAIS compliance status is not_granted.
[ ] benchmark validation status is present.
[ ] benchmark validation status is not_validated.
[ ] raw human data flag is present.
[ ] raw human data flag is false.
[ ] identifiable data flag is present.
[ ] identifiable data flag is false.
[ ] clinical data flag is present.
[ ] clinical data flag is false.
[ ] private user data flag is present.
[ ] private user data flag is false.
[ ] public/private boundary field is present.
[ ] schema version or schema reference is present.
[ ] creation or sample timestamp field is present.
[ ] operator or generator status is present.
[ ] audit note is present.
```

---

## Stream manifest metadata checklist

For `streams_manifest.csv` or equivalent stream manifest:

```text
[ ] stream_id field is present.
[ ] stream_name field is present.
[ ] stream_type field is present.
[ ] source_module field is present.
[ ] sampling_rate_or_event_rate field is present, if applicable.
[ ] timestamp_source field is present.
[ ] synthetic_status field is present.
[ ] synthetic_status indicates synthetic/sample/mock/placeholder only.
[ ] public_private_boundary field is present.
[ ] raw_human_data_present field is present and false.
[ ] identifiable_data_present field is present and false.
[ ] clinical_data_present field is present and false.
[ ] sal_meter_input_present field is present and false.
[ ] cais_compliance_claim_present field is present and false.
[ ] benchmark_validation_claim_present field is present and false.
[ ] each stream has a readable role.
[ ] each stream has a bounded description.
[ ] no stream name implies diagnosis.
[ ] no stream name implies therapy.
[ ] no stream name implies surveillance.
[ ] no stream name implies human ranking.
[ ] no stream name implies Sal-Meter validation.
[ ] no stream name implies CAIS compliance.
```

---

## Timestamp metadata checklist

```text
[ ] Timestamp field exists for each event-like file.
[ ] Timestamp format is documented.
[ ] Timestamp source is documented.
[ ] Timestamp unit is documented.
[ ] Timestamp timezone or reference convention is documented where applicable.
[ ] Synthetic timestamp status is documented.
[ ] Known offsets are documented or marked not_applicable.
[ ] Known drift is documented or marked not_applicable.
[ ] Missing timestamp status is documented.
[ ] Timestamp alignment status is documented.
[ ] Timestamp review status is documented.
[ ] Timestamp metadata does not imply signal validation.
[ ] Timestamp metadata does not imply benchmark validation.
[ ] Timestamp metadata does not imply real-time monitoring readiness.
[ ] Timestamp metadata does not imply production deployment.
```

Timestamp completeness means the sequence can be reviewed.

It does not mean the signal is true.

---

## Event marker metadata checklist

For `events.csv` or equivalent event marker file:

```text
[ ] event_id field is present.
[ ] session_id field is present.
[ ] event_type field is present.
[ ] event_timestamp field is present.
[ ] event_source field is present.
[ ] synthetic_status field is present.
[ ] public_private_boundary field is present.
[ ] event_description field is present or intentionally omitted with explanation.
[ ] event_type values are bounded.
[ ] event_type values are non-diagnostic.
[ ] event_type values are non-clinical.
[ ] event_type values are non-therapeutic.
[ ] event_type values are non-surveillance.
[ ] event_type values are non-certification.
[ ] event_type values are non-human-ranking.
[ ] event_type values do not imply Sal-Meter input.
[ ] event_type values do not imply CAIS compliance.
[ ] event_type values do not imply benchmark validation.
[ ] no event marker contains raw human data.
[ ] no event marker contains identifiable data.
[ ] no event marker contains clinical data.
```

Allowed event language:

```text
synthetic_input_event
synthetic_ai_output_event
synthetic_proxy_field_snapshot
dashboard_review_state
boundary_check
placeholder_feedback_policy
feedback_event_log_entry
human_review_required
interpretation_hold
```

Prohibited event language:

```text
diagnosis_detected
therapy_triggered
clinical_alert
surveillance_score
person_risk_detected
employee_failed
patient_status
Sal-Meter_validated
CAIS_compliant
human_truth_confirmed
```

---

## Label metadata checklist

For `labels.csv` or equivalent label file:

```text
[ ] label_id field is present.
[ ] session_id field is present.
[ ] label_name field is present.
[ ] label_type field is present.
[ ] start_timestamp field is present.
[ ] end_timestamp field is present.
[ ] label_source field is present.
[ ] synthetic_status field is present.
[ ] public_private_boundary field is present.
[ ] label_boundary_note field is present.
[ ] labels are non-diagnostic.
[ ] labels are non-clinical.
[ ] labels are non-therapeutic.
[ ] labels are non-surveillance.
[ ] labels are non-certification.
[ ] labels are non-human-ranking.
[ ] labels do not imply Sal-Meter input.
[ ] labels do not imply CAIS compliance.
[ ] labels do not imply benchmark validation.
[ ] labels do not encode participant identity.
[ ] labels do not encode condition through filenames.
[ ] labels do not leak target values through metadata fields.
[ ] label windows are reviewable.
[ ] overlapping label windows are explained or avoided.
[ ] ambiguous label windows are marked for review.
```

Allowed label style:

```text
synthetic_condition_label
sample_interaction_window
proxy_state_window
review_state
boundary_state
```

Prohibited label style:

```text
diagnostic_label
clinical_label
therapeutic_response
surveillance_status
employee_score
patient_score
legal_status
human_truth_score
consciousness_score
Sal-Meter_result
CAIS_result
```

---

## Feature table metadata checklist

For `features_baseline.csv` or equivalent feature table:

```text
[ ] feature_row_id field is present.
[ ] session_id field is present.
[ ] window_id field is present, if applicable.
[ ] feature_set_name field is present.
[ ] feature_version field is present.
[ ] feature_source field is present.
[ ] synthetic_status field is present.
[ ] public_private_boundary field is present.
[ ] feature_boundary_note field is present.
[ ] no feature contains raw human data.
[ ] no feature contains identifiable data.
[ ] no feature contains clinical data.
[ ] no feature contains Sal-Meter input.
[ ] no feature contains CAIS compliance output.
[ ] features are marked as toy/helper/synthetic/sample where applicable.
[ ] feature names do not imply diagnosis.
[ ] feature names do not imply therapy.
[ ] feature names do not imply surveillance.
[ ] feature names do not imply certification.
[ ] feature names do not imply human ranking.
[ ] feature names do not imply Sal-Meter validation.
[ ] feature names do not imply CAIS compliance.
```

A feature table may demonstrate structure.

It must not pretend to measure truth.

---

## QC metadata checklist

For `qc_report.json` or equivalent QC report:

```text
[ ] qc_report_id is present.
[ ] session_id is present.
[ ] qc_version is present.
[ ] qc_scope is present.
[ ] qc_scope is helper-structure-only.
[ ] synthetic_status is present.
[ ] public_private_boundary is present.
[ ] missingness summary is present or marked not_applicable.
[ ] timestamp review is present or marked not_applicable.
[ ] stream review is present or marked not_applicable.
[ ] event marker review is present or marked not_applicable.
[ ] label review is present or marked not_applicable.
[ ] feature review is present or marked not_applicable.
[ ] split review is present or marked not_applicable.
[ ] leakage review is present or marked not_applicable.
[ ] dashboard boundary review is present or marked not_applicable.
[ ] closed-loop demo-lite boundary review is present or marked not_applicable.
[ ] Sal-Meter input status is present.
[ ] CAIS compliance status is present.
[ ] benchmark validation status is present.
[ ] QC report does not claim scientific validation.
[ ] QC report does not claim benchmark validation.
[ ] QC report does not claim Sal-Meter validation.
[ ] QC report does not claim CAIS compliance.
[ ] QC report does not claim clinical, diagnostic, therapeutic, surveillance, certification, or human-ranking authority.
```

QC means review quality.

QC does not mean scientific proof.

---

## Split metadata checklist

For `splits.json` or equivalent split definition file:

```text
[ ] split_id is present.
[ ] split_version is present.
[ ] session_id or package_id reference is present.
[ ] split_scope is present.
[ ] split_scope is helper-demonstration-only or equivalent.
[ ] synthetic_status is present.
[ ] train split is present if applicable.
[ ] validation split is present if applicable.
[ ] test split is present if applicable.
[ ] holdout note is present or marked not_applicable.
[ ] leakage review note is present.
[ ] participant-level leakage note is present or marked not_applicable.
[ ] session-level leakage note is present or marked not_applicable.
[ ] timestamp leakage note is present or marked not_applicable.
[ ] file-name leakage note is present or marked not_applicable.
[ ] metadata leakage note is present or marked not_applicable.
[ ] dashboard leakage note is present or marked not_applicable.
[ ] feedback-log leakage note is present or marked not_applicable.
[ ] split file does not imply final benchmark design.
[ ] split file does not imply model validation.
[ ] split file does not imply Sal-Meter validation.
[ ] split file does not imply CAIS compliance.
```

A split can protect evidence.

A bad split can destroy it.

---

## Operator log metadata checklist

For `operator_log.md` or equivalent operator/audit note:

```text
[ ] operator log exists.
[ ] operator log identifies package status.
[ ] operator log identifies synthetic/sample status.
[ ] operator log identifies public/private boundary.
[ ] operator log identifies what was generated.
[ ] operator log identifies what was not collected.
[ ] operator log identifies raw human data status.
[ ] operator log identifies identifiable data status.
[ ] operator log identifies clinical data status.
[ ] operator log identifies Sal-Meter input status.
[ ] operator log identifies CAIS compliance status.
[ ] operator log identifies benchmark validation status.
[ ] operator log identifies known limitations.
[ ] operator log identifies known blockers.
[ ] operator log identifies prohibited claims.
[ ] operator log avoids diagnostic language.
[ ] operator log avoids therapeutic language.
[ ] operator log avoids surveillance language.
[ ] operator log avoids certification language.
[ ] operator log avoids human-ranking language.
```

An operator log is not decoration.

It is the memory of the package.

---

## Dashboard metadata checklist

For `dashboard-mockup/` files:

```text
[ ] Dashboard folder README exists.
[ ] Dashboard claim boundary exists.
[ ] Sample dashboard field metadata exists.
[ ] Mockup wireframe exists.
[ ] Dashboard fields are synthetic/sample/helper fields only.
[ ] Dashboard fields include field_name or equivalent.
[ ] Dashboard fields include field_role or equivalent.
[ ] Dashboard fields include data_status or equivalent.
[ ] Dashboard fields include display_boundary or equivalent.
[ ] Dashboard fields include prohibited_claims or equivalent.
[ ] Dashboard fields include Sal-Meter status.
[ ] Dashboard fields include CAIS compliance status.
[ ] Dashboard fields include benchmark validation status.
[ ] Dashboard fields do not imply diagnosis.
[ ] Dashboard fields do not imply therapy.
[ ] Dashboard fields do not imply surveillance.
[ ] Dashboard fields do not imply certification.
[ ] Dashboard fields do not imply human ranking.
[ ] Dashboard fields do not imply Sal-Meter validation.
[ ] Dashboard fields do not imply CAIS compliance.
```

A dashboard is powerful because it looks final.

Therefore its metadata must say what it is not.

---

## Closed-loop demo-lite metadata checklist

For `closed-loop-demo-lite/` files:

```text
[ ] Closed-loop demo-lite folder README exists.
[ ] Feedback loop boundary exists.
[ ] Feedback event log schema exists.
[ ] Local feedback demo placeholder exists.
[ ] Feedback log metadata includes log_id.
[ ] Feedback log metadata includes session_id.
[ ] Feedback log metadata includes created_at.
[ ] Feedback log metadata includes created_by.
[ ] Feedback log metadata includes environment.
[ ] Feedback log metadata includes execution_mode.
[ ] Feedback log metadata includes production_status.
[ ] Feedback log metadata includes synthetic_status_declared.
[ ] Feedback log metadata includes public_private_boundary.
[ ] Feedback log metadata includes Sal-Meter input status.
[ ] Feedback log metadata includes CAIS compliance status.
[ ] Feedback log metadata includes benchmark validation status.
[ ] Feedback event metadata includes event_id.
[ ] Feedback event metadata includes event_type.
[ ] Feedback event metadata includes review_state.
[ ] Feedback event metadata includes boundary_status.
[ ] Feedback event metadata includes placeholder_feedback_action.
[ ] Feedback event metadata includes human_review_status.
[ ] Feedback event metadata includes audit_note.
[ ] Feedback event metadata prohibits raw human data.
[ ] Feedback event metadata prohibits identifiable data.
[ ] Feedback event metadata prohibits clinical data.
[ ] Feedback event metadata prohibits private user data.
[ ] Feedback event metadata prohibits person scoring.
[ ] Feedback event metadata prohibits live intervention.
[ ] Feedback event metadata prohibits production automation.
```

The loop may show a path.

It must not move a human being.

---

## Schema reference checklist

```text
[ ] Each structured JSON file has a schema reference or a documented schema relationship.
[ ] Each CSV file has an expected column list.
[ ] Each schema path is readable.
[ ] Schema names match file names where expected.
[ ] Schema descriptions preserve public-helper boundary.
[ ] Schema enum values avoid clinical, diagnostic, therapeutic, surveillance, certification, and human-ranking language.
[ ] Schema required fields are documented.
[ ] Schema validation is described as helper-structure validation only.
[ ] Schema validation is not described as benchmark validation.
[ ] Schema validation is not described as Sal-Meter validation.
[ ] Schema validation is not described as CAIS compliance.
```

---

## File mapping checklist

```text
[ ] Every major file has a role.
[ ] Every major file has a boundary.
[ ] Every major file has a source or generation note.
[ ] Every major file has a synthetic/sample status where applicable.
[ ] Every major file has a schema relationship where applicable.
[ ] Every major file has a review status where applicable.
[ ] Every major file has an audit note where applicable.
[ ] No major file is unexplained.
[ ] No major file has ambiguous authority.
[ ] No major file implies validation beyond its scope.
```

Recommended file mapping fields:

```text
file_path
file_role
data_status
schema_reference
public_private_boundary
review_status
known_limitations
prohibited_claims
audit_note
```

---

## Public/private boundary metadata checklist

```text
[ ] Public files are marked public-helper-only.
[ ] Public files contain synthetic/sample/mock/placeholder data only.
[ ] Public files exclude raw human data.
[ ] Public files exclude identifiable data.
[ ] Public files exclude clinical data.
[ ] Public files exclude private user data.
[ ] Public files exclude Sal-Meter raw input.
[ ] Public files exclude CAIS compliance dossiers.
[ ] Public files exclude production feedback logs.
[ ] Private-data handling is not implied by public helper files.
[ ] If future private data are referenced, they are marked as separate-governance only.
```

Public means visible.

Visible means bounded.

---

## Required negative flags

Where applicable, metadata should explicitly set these to false:

```text
raw_human_data_present: false
identifiable_data_present: false
clinical_data_present: false
private_user_data_present: false
sal_meter_input_present: false
cais_compliance_claim_present: false
benchmark_validation_claim_present: false
diagnostic_claim_present: false
clinical_claim_present: false
therapeutic_claim_present: false
surveillance_claim_present: false
certification_claim_present: false
employment_claim_present: false
insurance_claim_present: false
educational_claim_present: false
legal_claim_present: false
eligibility_claim_present: false
human_ranking_claim_present: false
person_scoring_claim_present: false
live_intervention_present: false
production_automation_present: false
```

Silence is not enough.

A false flag is a locked gate.

---

## Metadata missingness checklist

```text
[ ] Missing metadata fields are listed.
[ ] Missing fields are classified as critical, major, minor, or not_applicable.
[ ] Critical missing fields trigger Hold.
[ ] Boundary-related missing fields trigger Hold or No-Go.
[ ] Data-status missing fields trigger Hold.
[ ] Public/private boundary missing fields trigger Hold.
[ ] Sal-Meter input status missing fields trigger Hold.
[ ] CAIS compliance status missing fields trigger Hold.
[ ] Benchmark validation status missing fields trigger Hold.
[ ] Missingness is not hidden.
[ ] Missingness is not rebranded as flexibility.
```

A missing boundary is not a detail.

A missing boundary is a door left open.

---

## Critical metadata fields

The following are critical:

```text
data_status
synthetic_status_declared
public_private_boundary
raw_human_data_present
identifiable_data_present
clinical_data_present
private_user_data_present
sal_meter_input_present
cais_compliance_claim_present
benchmark_validation_claim_present
diagnostic_claim_present
therapeutic_claim_present
surveillance_claim_present
certification_claim_present
human_ranking_claim_present
```

If any critical field is missing from a file where it applies, decision is:

```text
Hold
```

If any critical field indicates a prohibited claim or prohibited data in the public repository, decision is:

```text
No-Go
```

---

## Metadata completeness decision block

Use this block after review:

```text
Metadata completeness review decision:

Decision:
Go / Conditional Go / Hold / No-Go

Reason:
[brief reason]

Critical missing metadata:
[list fields or "None"]

Boundary risks:
[list risks or "None"]

Public/private data risk:
None / Hold / No-Go

Sal-Meter boundary:
Not present / Future placeholder only / Risk found

CAIS boundary:
Not granted / Risk found

Benchmark validation boundary:
Not validated / Risk found

Release implication:
Ready for audit trail review / Hold release / No-Go release

Authority note:
This metadata review does not validate benchmark performance, Sal-Meter, CAIS compliance, clinical use, diagnosis, therapy, surveillance, certification, or human ranking.
```

---

## P2-4 issue alignment

This file implements:

```text
[P2-4] Add replication guide pack
```

It satisfies:

```text
Create replication-guide/metadata_completeness_checklist.md
```

---

## Completion status

```text
Metadata completeness checklist.
Research-stage.
Public helper documentation only.
Structure review only.
Metadata reviewability only.
Not benchmark validation.
Not scientific validation.
Not Sal-Meter validation.
Not CAIS compliance.
No raw human data.
No identifiable data.
No clinical data.
No diagnostic authority.
No therapeutic authority.
No surveillance authority.
No certification authority.
No human-ranking authority.
No release publication.
```

---

## Final rule

Metadata is the spine.

If the spine is missing, the body cannot stand.

This checklist confirms whether the spine is visible.

It does not claim the body is alive.
