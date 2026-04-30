# Replication Guide

This folder contains public helper reproducibility and release-readiness checklists for the **SICS Human-State Proxy Benchmark Track**.

It exists to make the repository reviewable, reproducible in structure, and harder to overclaim.

It is not the Sal-Meter core signal track.

It does not define CAIS.

It does not grant CAIS compliance.

It does not validate Sal-Meter.

It does not validate benchmark performance.

It does not introduce raw human data.

It does not create diagnostic, clinical, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

It does not publish a release.

It does not replace DOI-registered SICS / CAIS / Sal-Meter / CCF authority records.

---

## Purpose

A repository can look complete while still being impossible to review.

A dataset can look clean while still leaking labels.

A dashboard can look scientific while only showing mock fields.

A release can look official while only being a helper surface.

This folder prevents that drift.

The purpose of this replication guide is to define the minimum public-helper review structure required before this repository is treated as release-ready.

This guide checks structure.

It does not validate truth.

This guide checks reviewability.

It does not certify science.

This guide checks boundary discipline.

It does not grant authority.

---

## Current status

```text
Replication guide pack.
Research-stage.
Public helper documentation only.
Structure review only.
Reproducibility readiness only.
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

## Planned files

This folder is expected to contain:

```text
replication-guide/
  README.md
  reproducibility_package_checklist.md
  metadata_completeness_checklist.md
  audit_trail_checklist.md
  public_release_checklist.md
```

---

## File roles

```text
README.md
  Folder-level purpose, scope, boundary, and use order.

reproducibility_package_checklist.md
  Checklist for whether the public helper package is structurally reproducible.

metadata_completeness_checklist.md
  Checklist for session metadata, stream metadata, event markers, labels, QC, splits, and boundary fields.

audit_trail_checklist.md
  Checklist for file mapping, versioning, operator notes, change history, review notes, and evidence traceability.

public_release_checklist.md
  Checklist for whether a GitHub helper release can be published without overclaiming benchmark validation, Sal-Meter validation, CAIS compliance, clinical status, raw human data publication, or certification authority.
```

---

## What this guide checks

This guide checks whether a public helper package is reviewable.

It checks:

- folder structure;
- file presence;
- README clarity;
- schema alignment;
- synthetic/sample data boundary;
- metadata completeness;
- timestamp reviewability;
- event marker reviewability;
- label-window reviewability;
- QC reviewability;
- split reviewability;
- leakage-risk awareness;
- dashboard boundary clarity;
- closed-loop demo-lite boundary clarity;
- audit trail;
- citation boundary;
- DOI authority distinction;
- release-readiness boundary.

It does not check:

- benchmark performance;
- model validity;
- scientific truth;
- Sal-Meter validity;
- CAIS compliance;
- diagnostic validity;
- clinical validity;
- therapeutic validity;
- surveillance readiness;
- certification readiness;
- device readiness;
- human-state truth.

---

## Reproducibility readiness vs validation

Reproducibility readiness means:

```text
Another reviewer can inspect the public helper package, understand the file roles, verify the synthetic/sample structure, follow the metadata map, review the boundary language, and rerun helper-structure checks.
```

Reproducibility readiness does not mean:

```text
The benchmark has been scientifically validated.
The model is valid.
The proxy signals measure consciousness.
The repository validates Sal-Meter.
The repository grants CAIS compliance.
The package is clinical, diagnostic, therapeutic, surveillance-ready, certification-ready, or device-ready.
```

A reproducible map is still a map.

It is not the mountain.

---

## Public helper release readiness vs canonical authority

GitHub release readiness means:

```text
The public helper repository is structured enough to tag and publish a bounded helper release.
```

GitHub release readiness does not mean:

```text
The release becomes the canonical authority.
The release overrides DOI-registered records.
The release grants CAIS compliance.
The release validates Sal-Meter.
The release validates benchmark performance.
The release creates clinical, diagnostic, therapeutic, surveillance, certification, or human-ranking authority.
```

DOI records govern authority.

GitHub helps implementation move.

---

## Required review order

Use this order:

```text
1. Reproducibility package review
2. Metadata completeness review
3. Audit trail review
4. Public release readiness review
5. Root README boundary review
6. Citation / DOI boundary review
7. Final Hold / Go decision
```

Do not reverse the order.

Do not publish a helper release before the release checklist is passed.

Do not publish a helper release while GitHub Actions validator execution remains blocked, if that release depends on the validator.

---

## Relationship to existing folders

This guide reviews the following public helper surfaces:

```text
schemas/
sample-data/
sample-data/synthetic-session-001/
evaluation-baseline/
protocol-helper/
dashboard-mockup/
closed-loop-demo-lite/
.github/workflows/
CITATION.cff
README.md
LICENSE
```

Each folder has a boundary.

The replication guide checks whether those boundaries remain visible.

---

## Minimum public helper package

A minimum public helper package should contain:

```text
README.md
LICENSE
CITATION.cff

schemas/
sample-data/
evaluation-baseline/
protocol-helper/
dashboard-mockup/
closed-loop-demo-lite/
replication-guide/
```

A public helper package may be release-ready only when each public folder explains:

- what it is;
- what it is not;
- what files it contains;
- what data boundary applies;
- what claims are prohibited;
- what validation is not granted.

---

## Required boundary phrases

The following phrases should remain visible across public helper materials:

```text
research-stage
public helper
synthetic/sample
non-clinical
non-diagnostic
non-therapeutic
non-surveillance
non-certification
non-human-ranking
not Sal-Meter
not CAIS compliance
not benchmark validation
no raw human data
no identifiable data
no clinical data
structure-only
reviewability
```

---

## Prohibited overclaim language

Do not use:

```text
validated benchmark
validated Sal-Meter
CAIS-compliant package
certified reproducibility
clinical validation
diagnostic validation
therapeutic validation
approved device
commercial readiness
official compliance result
human-state truth validation
consciousness truth score
closed-loop intervention system
production monitoring system
```

Names open doors.

Bad names open dangerous doors.

---

## Data boundary

This guide assumes that the public repository contains only:

```text
synthetic
sample
mock
toy
placeholder
sample-structure-only
non-identifying helper material
```

This public repository must not contain:

```text
raw human biosignals
raw human video
raw human audio
face data
voice data
identifiable participant metadata
private session logs
clinical data
health records
consent forms containing personal information
internal lab packages
Sal-Meter raw input
CAIS compliance dossiers
production feedback logs
```

If any prohibited data is found, public release is Hold.

---

## Metadata review principle

A package that cannot be mapped cannot be reviewed.

A package that cannot be reviewed cannot be treated as reproducible.

A minimum reviewable package should include:

- session ID;
- dataset type;
- synthetic status;
- public/private data boundary;
- schema version;
- stream manifest;
- event markers;
- label windows;
- QC report;
- split definition;
- feature table;
- operator log;
- timestamp source;
- drift or offset note;
- missingness note;
- leakage review note;
- file mapping;
- boundary statement;
- audit note.

---

## Audit trail principle

Every public helper package should answer:

```text
What file exists?
Why does it exist?
What schema does it align with?
What boundary applies?
What changed?
Who reviewed it?
What is still blocked?
What must not be claimed?
```

An audit trail is not decoration.

It is the spine of trust.

---

## Dashboard review principle

A dashboard mockup may show:

```text
synthetic/sample fields
proxy helper fields
review states
metadata status
timestamp status
leakage status
QC status
future placeholder fields
```

A dashboard mockup must not show or imply:

```text
diagnosis
therapy
clinical decision support
surveillance scoring
human ranking
person scoring
Sal-Meter validation
CAIS compliance
certification
```

---

## Closed-loop demo-lite review principle

A closed-loop demo-lite may show:

```text
synthetic/sample feedback event logs
local placeholder flow
review prompts
boundary notices
audit-friendly event structure
human-review-required placeholder state
```

A closed-loop demo-lite must not show or imply:

```text
live intervention
real-time monitoring
production automation
diagnosis
therapy
clinical escalation
surveillance
employee scoring
insurance scoring
legal eligibility scoring
human ranking
Sal-Meter feedback loop
CAIS-compliant loop
```

A loop may show structure.

It must not move a human being.

---

## Validator boundary

A helper validator may confirm:

```text
required files exist
JSON files parse
CSV files parse
schemas are readable
synthetic/sample status is declared
boundary flags are present
basic helper structure is consistent
```

A helper validator must not claim:

```text
benchmark performance validation
scientific validation
Sal-Meter validation
CAIS compliance
clinical validation
diagnostic validation
therapeutic validation
surveillance readiness
certification readiness
device readiness
human-state truth measurement
```

A `PASS` means structure passed.

It does not mean truth passed.

---

## Release readiness rule

A public helper release may be prepared only when:

- root README is updated;
- folder-level READMEs exist;
- schema folder is documented;
- sample-data boundary is documented;
- synthetic-session README exists;
- evaluation-baseline README explains validator use;
- protocol-helper boundary files exist;
- dashboard-mockup boundary files exist;
- closed-loop-demo-lite boundary files exist, if included;
- replication-guide checklists exist;
- CITATION.cff points to DOI-registered public records;
- no raw human data are present;
- no identifiable data are present;
- no clinical data are present;
- no Sal-Meter input is present;
- no CAIS compliance claim is present;
- no benchmark validation claim is present;
- no live intervention claim is present;
- no production automation claim is present;
- no diagnostic, clinical, therapeutic, surveillance, certification, or human-ranking authority is implied.

If GitHub Actions validation is part of the release condition, release remains unpublished until the workflow can run successfully.

---

## Go / Hold / No-Go

Use this decision language:

```text
Go
  Public helper package is structurally reviewable and bounded.

Conditional Go
  Package is mostly ready but one bounded non-authority correction remains.

Hold
  A required file, boundary, metadata element, audit trail, or validator condition is missing.

No-Go
  The package contains raw human data, identifiable data, clinical data, Sal-Meter input, CAIS compliance claims, benchmark validation claims, diagnostic claims, therapeutic claims, surveillance claims, certification claims, or human-ranking claims.
```

No-Go is not failure.

No-Go is a locked gate.

Locked gates protect the mountain.

---

## Review checklist

Before treating the repository as release-ready, check:

```text
[ ] Is the repository clearly marked as research-stage?
[ ] Is the repository clearly marked as public helper surface?
[ ] Is the repository clearly marked as non-clinical?
[ ] Is the repository clearly marked as non-diagnostic?
[ ] Is the repository clearly marked as non-therapeutic?
[ ] Is the repository clearly marked as non-surveillance?
[ ] Is the repository clearly marked as non-certification?
[ ] Is the repository clearly marked as non-human-ranking?
[ ] Is it clear that this is not Sal-Meter?
[ ] Is it clear that this does not define CAIS?
[ ] Is it clear that this does not grant CAIS compliance?
[ ] Is it clear that this does not validate benchmark performance?
[ ] Are raw human data excluded?
[ ] Are identifiable data excluded?
[ ] Are clinical data excluded?
[ ] Are private user data excluded?
[ ] Are Sal-Meter inputs excluded?
[ ] Are DOI authority boundaries clear?
[ ] Are GitHub helper boundaries clear?
[ ] Are release boundaries clear?
[ ] Are validator boundaries clear?
[ ] Are dashboard boundaries clear?
[ ] Are closed-loop demo-lite boundaries clear?
[ ] Are metadata completeness expectations visible?
[ ] Are audit trail expectations visible?
[ ] Are leakage-risk warnings visible?
```

---

## P2-4 issue alignment

This file implements:

```text
[P2-4] Add replication guide pack
```

It satisfies:

```text
Create replication-guide/README.md
```

---

## Completion status

```text
Replication guide folder README.
Research-stage.
Public helper documentation only.
Structure review only.
Reproducibility readiness only.
Not benchmark validation.
Not scientific validation.
Not Sal-Meter.
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

Reproducibility is the bridge.

Validation is the crossing.

This guide builds the bridge.

It does not claim that the crossing has already happened.
