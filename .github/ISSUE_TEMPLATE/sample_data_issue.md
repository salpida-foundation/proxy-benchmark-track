---
name: Synthetic/sample data issue
about: Report a bounded synthetic/sample data structure problem without submitting raw, identifiable, clinical, or Sal-Meter data.
title: "[Sample data issue] "
---

# Synthetic / Sample Data Issue

Use this issue to report a structure problem in the public synthetic/sample data package for the SICS Human-State Proxy Benchmark Track.

This template is for:

- missing synthetic/sample files;
- malformed JSON files;
- malformed CSV files;
- missing required columns;
- missing boundary fields;
- ambiguous synthetic/sample status;
- sample package validator failures;
- schema alignment problems;
- operator log boundary problems;
- public/private data boundary problems.

This issue is not for submitting raw human data.

This issue is not for submitting identifiable data.

This issue is not for submitting clinical data.

This issue is not for submitting Sal-Meter input.

This issue is not for claiming CAIS compliance.

This issue is not for claiming benchmark validation.

---

## Affected file

Check all that apply.

- [ ] `sample-data/README.md`
- [ ] `sample-data/synthetic-session-001/README.md`
- [ ] `sample-data/synthetic-session-001/session_metadata.json`
- [ ] `sample-data/synthetic-session-001/streams_manifest.csv`
- [ ] `sample-data/synthetic-session-001/events.csv`
- [ ] `sample-data/synthetic-session-001/labels.csv`
- [ ] `sample-data/synthetic-session-001/qc_report.json`
- [ ] `sample-data/synthetic-session-001/features_baseline.csv`
- [ ] `sample-data/synthetic-session-001/splits.json`
- [ ] `sample-data/synthetic-session-001/operator_log.md`
- [ ] `evaluation-baseline/validate_sample_package.py`
- [ ] Related schema file
- [ ] Other

Affected path:

---

## Issue type

Check all that apply.

- [ ] Required file missing
- [ ] JSON parse issue
- [ ] CSV parse issue
- [ ] Missing required field
- [ ] Missing required column
- [ ] Schema mismatch
- [ ] Ambiguous synthetic/sample status
- [ ] Missing public/private boundary field
- [ ] Missing negative boundary flag
- [ ] Missing operator log boundary language
- [ ] Validator failure
- [ ] Leakage-risk concern
- [ ] File naming problem
- [ ] Dashboard field mismatch
- [ ] Closed-loop demo-lite event-log mismatch
- [ ] Other bounded sample-data issue

---

## Problem description

Describe the problem.

Do not paste raw human data.

Do not paste identifiable data.

Do not paste clinical data.

Problem description:

---

## Expected structure

Describe what the expected synthetic/sample structure should be.

Expected structure:

---

## Actual structure

Describe what currently appears in the file or package.

Paste only safe public helper text.

Do not paste private, raw, identifiable, clinical, or Sal-Meter data.

Actual structure:

---

## Validator output

If the helper validator produced an error, paste the safe error message here.

Do not paste private data.

Validator output:

---

## Boundary check

The issue must preserve all applicable boundaries.

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

## Synthetic/sample status

Check what applies.

- [ ] The affected file is clearly synthetic.
- [ ] The affected file is clearly sample data.
- [ ] The affected file is clearly mock data.
- [ ] The affected file is clearly toy data.
- [ ] The affected file is clearly placeholder data.
- [ ] The affected file has ambiguous data status.
- [ ] The affected file could be mistaken for real human data.
- [ ] The affected file could be mistaken for clinical data.
- [ ] The affected file could be mistaken for Sal-Meter input.

If ambiguous, explain:

---

## Leakage-risk check

Could this issue create or reveal leakage risk?

- [ ] No known leakage-risk concern
- [ ] Possible label leakage through filenames
- [ ] Possible label leakage through folder names
- [ ] Possible label leakage through timestamps
- [ ] Possible label leakage through metadata
- [ ] Possible label leakage through session identity
- [ ] Possible label leakage through device identity
- [ ] Possible label leakage through operator identity
- [ ] Possible leakage through dashboard fields
- [ ] Possible leakage through feedback event logs
- [ ] Unknown

Leakage-risk note:

---

## Proposed correction

Describe the proposed safe correction.

The correction must remain public-helper-only and synthetic/sample-only.

Proposed correction:

---

## Validator impact

Will this correction affect the helper validator?

- [ ] No validator impact
- [ ] Validator may need required-file update
- [ ] Validator may need JSON parse update
- [ ] Validator may need CSV column update
- [ ] Validator may need schema alignment update
- [ ] Validator may need synthetic/sample status check
- [ ] Validator may need boundary-flag check
- [ ] Unknown

Validator impact note:

---

## Prohibited interpretation check

This issue must not imply any of the following.

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

- [ ] This issue does not replace DOI-registered SICS / CAIS / Sal-Meter / CCF records.
- [ ] This issue does not create canonical authority.
- [ ] This issue does not reinterpret canonical records.
- [ ] This issue does not grant compliance authority.
- [ ] This issue does not grant certification authority.
- [ ] This issue preserves GitHub as a public helper surface.

---

## Proposed decision

Select one.

- [ ] Go — sample-data correction is clear and bounded
- [ ] Conditional Go — correction is acceptable after a small wording or field-scope change
- [ ] Hold — more boundary, schema, or validator review is needed
- [ ] No-Go — prohibited data or prohibited authority claim is present

---

## Final boundary sentence

A sample file may show structure.

It must not disclose people.

It must not turn a helper package into evidence.
