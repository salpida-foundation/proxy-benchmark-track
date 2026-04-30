---
name: Boundary correction
about: Report overclaims, naming drift, data-boundary drift, DOI authority confusion, or prohibited language.
title: "[Boundary correction] "
---

# Boundary Correction

Use this issue to report a boundary problem in the SICS Human-State Proxy Benchmark Track public helper repository.

This template is for correcting:

- overclaims;
- naming drift;
- public/private data boundary drift;
- DOI authority confusion;
- prohibited language;
- unintended Sal-Meter implication;
- unintended CAIS compliance implication;
- unintended benchmark validation implication;
- unintended diagnostic, clinical, therapeutic, surveillance, certification, or human-ranking implication.

This issue is not for submitting raw human data.

This issue is not for submitting identifiable data.

This issue is not for submitting clinical data.

This issue is not for submitting Sal-Meter input.

This issue is not for claiming CAIS compliance.

---

## Affected file or location

Provide the file path, section, line, phrase, or repository area.

```text
Example:
README.md / Public release boundary
dashboard-mockup/README.md
closed-loop-demo-lite/feedback_loop_boundary.md
CITATION.cff
Repository About text
```

Affected location:

```text

```

---

## Boundary issue type

Check all that apply.

- [ ] Overclaim
- [ ] Naming drift
- [ ] Public/private data boundary drift
- [ ] DOI authority confusion
- [ ] GitHub helper surface confused with canonical authority
- [ ] Sal-Meter implication
- [ ] CAIS compliance implication
- [ ] Benchmark validation implication
- [ ] Scientific validation implication
- [ ] Clinical implication
- [ ] Diagnostic implication
- [ ] Therapeutic implication
- [ ] Surveillance implication
- [ ] Certification implication
- [ ] Device-readiness implication
- [ ] Production deployment implication
- [ ] Human-ranking implication
- [ ] Other boundary issue

---

## Problematic wording or structure

Paste only the problematic phrase or describe the issue.

Do not paste private data.

Do not paste raw human data.

Do not paste identifiable data.

Do not paste clinical data.

Problematic wording or structure:

```text

```

---

## Why this is a problem

Explain the boundary risk.

Use plain language.

```text
Example:
This phrase may make the repository sound like a validated benchmark, but this repository is only a public helper surface.
```

Explanation:

```text

```

---

## Suggested correction

Suggest safer replacement language.

Use bounded language.

Suggested correction:

```text

```

---

## Required boundary preservation

The correction must preserve all applicable boundaries.

- [ ] Public helper only
- [ ] Research-stage only
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

## Prohibited replacement language

The correction must not introduce any of the following claims.

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

## Authority boundary

Confirm the authority boundary.

- [ ] This correction does not replace DOI-registered SICS / CAIS / Sal-Meter / CCF records.
- [ ] This correction does not create canonical authority.
- [ ] This correction does not reinterpret canonical records.
- [ ] This correction does not grant compliance authority.
- [ ] This correction does not grant certification authority.
- [ ] This correction preserves GitHub as a public helper surface.

---

## Severity

Select one.

- [ ] Minor wording correction
- [ ] Moderate boundary drift
- [ ] Major overclaim risk
- [ ] Critical public/private data risk
- [ ] Critical authority-confusion risk

---

## Proposed decision

Select one.

- [ ] Go — correction is clear and bounded
- [ ] Conditional Go — correction is acceptable after a small wording change
- [ ] Hold — more boundary review is needed
- [ ] No-Go — prohibited data or prohibited authority claim is present

---

## Final boundary sentence

A boundary correction may sharpen the map.

It must not move the mountain.

It must not turn a helper surface into authority.
