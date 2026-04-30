---
name: Schema helper request
about: Request a bounded helper-schema addition or correction without implying validation, Sal-Meter status, or CAIS compliance.
title: "[Schema request] "
---

# Schema Helper Request

Use this issue to request a bounded schema addition or correction for the SICS Human-State Proxy Benchmark Track public helper repository.

This template is for:

- helper-schema additions;
- helper-schema corrections;
- field naming corrections;
- enum boundary corrections;
- metadata field corrections;
- synthetic/sample package structure alignment;
- dashboard mockup field alignment;
- closed-loop demo-lite event-log field alignment;
- validator-related schema alignment.

This issue is not for submitting raw human data.

This issue is not for submitting identifiable data.

This issue is not for submitting clinical data.

This issue is not for submitting Sal-Meter input.

This issue is not for claiming CAIS compliance.

This issue is not for claiming benchmark validation.

---

## Affected schema or file

Check all that apply.

- [ ] `schemas/session-metadata.schema.json`
- [ ] `schemas/streams-manifest.schema.json`
- [ ] `schemas/event-markers.schema.json`
- [ ] `schemas/labels.schema.json`
- [ ] `schemas/qc-report.schema.json`
- [ ] `schemas/features-baseline.schema.json`
- [ ] `schemas/splits.schema.json`
- [ ] `closed-loop-demo-lite/feedback_event_log_schema.json`
- [ ] `dashboard-mockup/sample_dashboard_fields.json`
- [ ] `sample-data/synthetic-session-001/session_metadata.json`
- [ ] `sample-data/synthetic-session-001/streams_manifest.csv`
- [ ] `sample-data/synthetic-session-001/events.csv`
- [ ] `sample-data/synthetic-session-001/labels.csv`
- [ ] `sample-data/synthetic-session-001/qc_report.json`
- [ ] `sample-data/synthetic-session-001/features_baseline.csv`
- [ ] `sample-data/synthetic-session-001/splits.json`
- [ ] Other

Affected path:

```text
```

---

## Request type

Check all that apply.

- [ ] Add a helper field
- [ ] Rename a helper field
- [ ] Remove or deprecate a helper field
- [ ] Clarify a field description
- [ ] Clarify an enum value
- [ ] Add a boundary flag
- [ ] Add a public/private data boundary field
- [ ] Add a synthetic/sample status field
- [ ] Add a leakage-risk field
- [ ] Add a timestamp review field
- [ ] Add a metadata completeness field
- [ ] Add an audit-trail field
- [ ] Align schema with sample data
- [ ] Align schema with validator behavior
- [ ] Align schema with dashboard mockup
- [ ] Align schema with closed-loop demo-lite
- [ ] Other bounded schema correction

---

## Current issue

Describe the current schema problem.

Do not paste raw human data.

Do not paste identifiable data.

Do not paste clinical data.

Current issue:

```text

```

---

## Proposed schema change

Describe the proposed field, type, allowed values, or correction.

Keep the request bounded.

Proposed change:

```text

```

---

## Reason for the change

Explain why this improves structure, reviewability, metadata completeness, leakage control, or boundary clarity.

Reason:

```text

```

---

## Boundary check

The proposed schema change must preserve all applicable boundaries.

- [ ] Public helper only
- [ ] Research-stage only
- [ ] Synthetic/sample/mock/placeholder compatible
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

Confirm this request does not require prohibited data.

- [ ] This request does not require raw human biosignals.
- [ ] This request does not require raw human video.
- [ ] This request does not require raw human audio.
- [ ] This request does not require face data.
- [ ] This request does not require voice data.
- [ ] This request does not require identifiable participant metadata.
- [ ] This request does not require private session logs.
- [ ] This request does not require clinical data.
- [ ] This request does not require health records.
- [ ] This request does not require consent forms containing personal information.
- [ ] This request does not require internal lab packages.
- [ ] This request does not require Sal-Meter raw input.
- [ ] This request does not require CAIS compliance dossiers.
- [ ] This request does not require production feedback logs.

---

## Prohibited interpretation check

This schema request must not imply any of the following.

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

## Validator impact

Will this change affect the helper validator?

- [ ] No validator impact
- [ ] Validator may need a field-presence check
- [ ] Validator may need a JSON schema update
- [ ] Validator may need a CSV column check
- [ ] Validator may need a boundary-flag check
- [ ] Validator may need a synthetic/sample status check
- [ ] Unknown

If validator impact exists, describe it:

```text

```

---

## Leakage-risk impact

Could this schema change affect leakage risk?

- [ ] No known leakage-risk impact
- [ ] Possible label leakage risk
- [ ] Possible filename leakage risk
- [ ] Possible timestamp leakage risk
- [ ] Possible metadata leakage risk
- [ ] Possible device/operator/session identity leakage risk
- [ ] Possible dashboard field leakage risk
- [ ] Possible feedback event-log leakage risk
- [ ] Unknown

Leakage-risk note:

```text

```

---

## Authority boundary

Confirm the authority boundary.

- [ ] This request does not replace DOI-registered SICS / CAIS / Sal-Meter / CCF records.
- [ ] This request does not create canonical authority.
- [ ] This request does not reinterpret canonical records.
- [ ] This request does not grant compliance authority.
- [ ] This request does not grant certification authority.
- [ ] This request preserves GitHub as a public helper surface.

---

## Proposed decision

Select one.

- [ ] Go — schema request is bounded and useful
- [ ] Conditional Go — schema request is useful after wording or field-scope correction
- [ ] Hold — more boundary or validator review is needed
- [ ] No-Go — prohibited data or prohibited authority claim is present

---

## Final boundary sentence

A schema may help the map become readable.

It must not turn structure into proof.

It must not turn a helper field into authority.
