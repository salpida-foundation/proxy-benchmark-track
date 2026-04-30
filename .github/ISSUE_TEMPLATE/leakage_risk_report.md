---
name: Leakage risk report
about: Report possible leakage through labels, filenames, timestamps, metadata, identities, dashboard fields, or feedback event logs.
title: "[Leakage risk] "
---

# Leakage Risk Report

Use this issue to report a possible leakage risk in the SICS Human-State Proxy Benchmark Track public helper repository.

This template is for reporting possible leakage through:

- labels;
- filenames;
- folder names;
- timestamps;
- metadata fields;
- session identity;
- device identity;
- operator identity;
- preprocessing artifacts;
- dashboard fields;
- feedback event logs;
- split definitions;
- train / validation / test contamination.

This issue is not for submitting raw human data.

This issue is not for submitting identifiable data.

This issue is not for submitting clinical data.

This issue is not for submitting Sal-Meter input.

This issue is not for claiming CAIS compliance.

This issue is not for claiming benchmark validation.

---

## Affected file or location

Check all that apply.

- [ ] `sample-data/synthetic-session-001/session_metadata.json`
- [ ] `sample-data/synthetic-session-001/streams_manifest.csv`
- [ ] `sample-data/synthetic-session-001/events.csv`
- [ ] `sample-data/synthetic-session-001/labels.csv`
- [ ] `sample-data/synthetic-session-001/qc_report.json`
- [ ] `sample-data/synthetic-session-001/features_baseline.csv`
- [ ] `sample-data/synthetic-session-001/splits.json`
- [ ] `sample-data/synthetic-session-001/operator_log.md`
- [ ] `evaluation-baseline/leakage_safe_split_example.py`
- [ ] `evaluation-baseline/baseline_pipeline_skeleton.py`
- [ ] `evaluation-baseline/validate_sample_package.py`
- [ ] `protocol-helper/session_label_rule.md`
- [ ] `protocol-helper/timestamp_sync_rule.md`
- [ ] `protocol-helper/metadata_completeness_rule.md`
- [ ] `dashboard-mockup/sample_dashboard_fields.json`
- [ ] `dashboard-mockup/mockup_wireframe.md`
- [ ] `closed-loop-demo-lite/feedback_event_log_schema.json`
- [ ] `closed-loop-demo-lite/local_feedback_demo_placeholder.py`
- [ ] Other

Affected path:

---

## Leakage risk type

Check all that apply.

- [ ] Label leakage through filenames
- [ ] Label leakage through folder names
- [ ] Label leakage through timestamps
- [ ] Label leakage through metadata fields
- [ ] Label leakage through session identity
- [ ] Label leakage through participant-like identity
- [ ] Label leakage through device identity
- [ ] Label leakage through operator identity
- [ ] Label leakage through preprocessing artifacts
- [ ] Label leakage through dashboard-visible fields
- [ ] Label leakage through feedback event logs
- [ ] Train / validation / test contamination
- [ ] Holdout contamination
- [ ] Target variable appears in feature fields
- [ ] Target variable appears in QC fields
- [ ] Target variable appears in split definitions
- [ ] Target variable appears in audit notes
- [ ] Other leakage risk

---

## Problem description

Describe the suspected leakage risk.

Do not paste raw human data.

Do not paste identifiable data.

Do not paste clinical data.

Problem description:

---

## Why this could create leakage

Explain how a model, dashboard, validator, reviewer, or future benchmark process could accidentally infer the target label, condition, or review state from an unintended field.

Use plain language.

Why this could create leakage:

---

## Example of the risky field or pattern

Paste only safe public helper text.

Do not paste private data.

Do not paste raw human data.

Do not paste identifiable data.

Do not paste clinical data.

Risky field or pattern:

---

## Expected safe structure

Describe the safer structure.

Expected safe structure:

---

## Proposed correction

Describe the proposed correction.

The correction should reduce leakage risk while preserving public-helper boundaries.

Proposed correction:

---

## Boundary check

The report must preserve all applicable boundaries.

- [ ] Public helper only
- [ ] Research-stage only
- [ ] Synthetic/sample/mock/placeholder only
- [ ] Non-clinical
- [ ] Non-diagnostic
- [ ] Non-therapeutic
- [ ] Non-surveillance
- [ ] Non-certification
- [ ] Non-human-ranking
- [ ] Not Sal-Meter
- [ ] Not CAIS compliance
- [ ] Not benchmark validation
- [ ] Not scientific validation
- [ ] No raw human data
- [ ] No identifiable data
- [ ] No clinical data
- [ ] No private user data
- [ ] No live intervention
- [ ] No production automation
- [ ] DOI records remain the authority layer
- [ ] GitHub remains a public helper surface

---

## Data boundary confirmation

Confirm this issue does not include prohibited data.

- [ ] This issue does not include raw human biosignals.
- [ ] This issue does not include raw human video.
- [ ] This issue does not include raw human audio.
- [ ] This issue does not include face data.
- [ ] This issue does not include voice data.
- [ ] This issue does not include identifiable participant metadata.
- [ ] This issue does not include private session logs.
- [ ] This issue does not include clinical data.
- [ ] This issue does not include health records.
- [ ] This issue does not include consent forms containing personal information.
- [ ] This issue does not include internal lab packages.
- [ ] This issue does not include Sal-Meter raw input.
- [ ] This issue does not include CAIS compliance dossiers.
- [ ] This issue does not include production feedback logs.

---

## Leakage severity

Select one.

- [ ] Minor — wording or example could be clearer
- [ ] Moderate — a field may unintentionally reveal label information
- [ ] Major — current structure could compromise benchmark evaluation
- [ ] Critical — public data, identity, clinical, Sal-Meter, or authority boundary risk exists
- [ ] Unknown — requires review

---

## Split impact

Could this risk affect train / validation / test separation?

- [ ] No known split impact
- [ ] Possible train / validation leakage
- [ ] Possible train / test leakage
- [ ] Possible validation / test leakage
- [ ] Possible holdout contamination
- [ ] Possible session-level leakage
- [ ] Possible participant-like leakage
- [ ] Possible timestamp leakage
- [ ] Unknown

Split impact note:

---

## Validator impact

Should the helper validator check this risk?

- [ ] No validator impact
- [ ] Add filename leakage check
- [ ] Add folder-name leakage check
- [ ] Add metadata leakage check
- [ ] Add timestamp leakage warning
- [ ] Add target-in-feature check
- [ ] Add dashboard-field leakage check
- [ ] Add feedback-log leakage check
- [ ] Add split contamination check
- [ ] Unknown

Validator impact note:

---

## Prohibited interpretation check

This leakage report must not imply any of the following.

- [ ] Validated benchmark
- [ ] Validated Sal-Meter
- [ ] CAIS-compliant package
- [ ] Certified reproducibility
- [ ] Clinical validation
- [ ] Diagnostic validation
- [ ] Therapeutic validation
- [ ] Approved device
- [ ] Commercial readiness
- [ ] Official compliance result
- [ ] Human-state truth validation
- [ ] Production intervention
- [ ] Surveillance-ready system
- [ ] Human-ranking score
- [ ] Person score
- [ ] Legal eligibility score
- [ ] Insurance score
- [ ] Employment score
- [ ] Education score

---

## Authority boundary

Confirm the authority boundary.

- [ ] This report does not replace DOI-registered SICS / CAIS / Sal-Meter / CCF records.
- [ ] This report does not create canonical authority.
- [ ] This report does not reinterpret canonical records.
- [ ] This report does not grant compliance authority.
- [ ] This report does not grant certification authority.
- [ ] This report preserves GitHub as a public helper surface.

---

## Proposed decision

Select one.

- [ ] Go — leakage-risk correction is clear and bounded
- [ ] Conditional Go — correction is acceptable after a small wording or field-scope change
- [ ] Hold — more leakage, metadata, schema, or validator review is needed
- [ ] No-Go — prohibited data, prohibited leakage, or prohibited authority claim is present

---

## Final boundary sentence

A leakage report protects the road.

It does not prove the destination.

It keeps the benchmark from mistaking shortcuts for signal.
