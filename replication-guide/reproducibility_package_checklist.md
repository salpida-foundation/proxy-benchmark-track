# Reproducibility Package Checklist

This checklist defines whether the public helper package for the **SICS Human-State Proxy Benchmark Track** is structurally reproducible enough for review.

It checks reproducibility readiness.

It does not validate benchmark performance.

It does not validate Sal-Meter.

It does not define CAIS.

It does not grant CAIS compliance.

It does not introduce raw human data.

It does not create diagnostic, clinical, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

It does not publish a release.

---

## Purpose

A reproducibility package is not a claim of truth.

A reproducibility package is a map.

It allows another reviewer to inspect:

- what files exist;
- why those files exist;
- how synthetic/sample data are structured;
- how metadata are mapped;
- how schemas are aligned;
- how labels are bounded;
- how leakage risks are controlled;
- how dashboard mockups are bounded;
- how closed-loop demo-lite files are bounded;
- how audit notes can be traced;
- what must not be claimed.

This checklist exists so that the repository can be reviewed without drifting into false authority.

---

## Current status

```text
Checklist type: reproducibility package readiness
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
  The public helper package is structurally reviewable and bounded.

Conditional Go
  The package is mostly reviewable, but one bounded correction remains.

Hold
  A required file, metadata element, schema link, audit note, boundary phrase, or validator condition is missing.

No-Go
  The package contains raw human data, identifiable data, clinical data, private user data, Sal-Meter input, CAIS compliance claims, benchmark validation claims, diagnostic claims, therapeutic claims, surveillance claims, certification claims, or human-ranking claims.
```

No-Go is not a moral failure.

No-Go is a locked gate.

Locked gates protect the project.

---

## Package-level checklist

```text
[ ] Root README.md exists.
[ ] LICENSE exists.
[ ] CITATION.cff exists.
[ ] schemas/ exists.
[ ] sample-data/ exists.
[ ] sample-data/synthetic-session-001/ exists.
[ ] evaluation-baseline/ exists.
[ ] protocol-helper/ exists.
[ ] dashboard-mockup/ exists.
[ ] closed-loop-demo-lite/ exists.
[ ] replication-guide/ exists.
[ ] Root README.md explains repository scope.
[ ] Root README.md explains that this is a public helper surface.
[ ] Root README.md states that this repository is not Sal-Meter.
[ ] Root README.md states that this repository does not grant CAIS compliance.
[ ] Root README.md states that this repository does not validate benchmark performance.
[ ] Root README.md states that raw human data do not belong in this repository.
[ ] Root README.md explains canonical DOI authority versus GitHub helper status.
[ ] Root README.md includes current milestone status.
[ ] Root README.md includes public data boundary.
[ ] Root README.md includes release hold conditions.
```

---

## Folder README checklist

Each major folder should contain a README.

```text
[ ] schemas/README.md exists.
[ ] sample-data/README.md exists.
[ ] sample-data/synthetic-session-001/README.md exists.
[ ] evaluation-baseline/README.md exists.
[ ] protocol-helper/README.md exists.
[ ] dashboard-mockup/README.md exists.
[ ] closed-loop-demo-lite/README.md exists.
[ ] replication-guide/README.md exists.
```

Each folder README should answer:

```text
[ ] What is this folder?
[ ] What is this folder not?
[ ] What files belong here?
[ ] What data boundary applies?
[ ] What claims are prohibited?
[ ] What validation is not granted?
[ ] What future use remains inactive or placeholder-only?
```

---

## Public boundary checklist

```text
[ ] The repository is clearly marked as research-stage.
[ ] The repository is clearly marked as public-helper-only.
[ ] The repository is clearly marked as non-clinical.
[ ] The repository is clearly marked as non-diagnostic.
[ ] The repository is clearly marked as non-therapeutic.
[ ] The repository is clearly marked as non-surveillance.
[ ] The repository is clearly marked as non-certification.
[ ] The repository is clearly marked as non-human-ranking.
[ ] It is clear that this repository is not the Sal-Meter core signal track.
[ ] It is clear that this repository is not a Proxy Sal-Meter.
[ ] It is clear that this repository does not define CAIS.
[ ] It is clear that this repository does not grant CAIS compliance.
[ ] It is clear that this repository does not validate Sal-Meter.
[ ] It is clear that this repository does not validate benchmark performance.
[ ] It is clear that this repository does not create a medical device.
[ ] It is clear that this repository does not create a clinical decision-support system.
[ ] It is clear that this repository does not create a therapy system.
[ ] It is clear that this repository does not create a surveillance system.
[ ] It is clear that this repository does not create an employment, insurance, education, legal, eligibility, certification, or human-ranking system.
```

---

## Prohibited data checklist

The public helper package must not contain:

```text
[ ] No raw human biosignals.
[ ] No raw human video.
[ ] No raw human audio.
[ ] No face data.
[ ] No voice data.
[ ] No identifiable participant metadata.
[ ] No private session logs.
[ ] No clinical data.
[ ] No health records.
[ ] No consent forms containing personal information.
[ ] No internal lab packages.
[ ] No Sal-Meter raw input.
[ ] No CAIS compliance dossier.
[ ] No production feedback logs.
[ ] No private user data.
```

If any prohibited item is present, decision is:

```text
No-Go
```

---

## Required data-status checklist

Every public sample or mock package should make its data status explicit.

```text
[ ] Sample data are marked synthetic, sample, mock, toy, placeholder, or sample-structure-only.
[ ] Synthetic status is visible in README files.
[ ] Synthetic status is visible in metadata files.
[ ] Synthetic status is visible in validator expectations.
[ ] Synthetic status is visible in dashboard mockup files.
[ ] Synthetic status is visible in closed-loop demo-lite files.
[ ] There is no ambiguous sample data.
[ ] There is no file that could be mistaken for real participant data.
[ ] There is no file that could be mistaken for clinical data.
[ ] There is no file that could be mistaken for Sal-Meter input.
```

---

## Schema package checklist

```text
[ ] schemas/README.md exists.
[ ] session-metadata.schema.json exists.
[ ] streams-manifest.schema.json exists.
[ ] event-markers.schema.json exists.
[ ] labels.schema.json exists.
[ ] qc-report.schema.json exists.
[ ] features-baseline.schema.json exists.
[ ] splits.schema.json exists.
[ ] Each schema is described as public helper structure only.
[ ] Each schema avoids clinical, diagnostic, therapeutic, surveillance, certification, or human-ranking claims.
[ ] Schema names do not imply Sal-Meter validation.
[ ] Schema names do not imply CAIS compliance.
[ ] Schema descriptions do not imply benchmark validation.
[ ] Required fields are reviewable.
[ ] Enum values remain bounded and non-diagnostic.
[ ] Boundary flags remain present where needed.
```

---

## Synthetic sample package checklist

```text
[ ] sample-data/README.md exists.
[ ] sample-data/synthetic-session-001/README.md exists.
[ ] session_metadata.json exists.
[ ] streams_manifest.csv exists.
[ ] events.csv exists.
[ ] labels.csv exists.
[ ] qc_report.json exists.
[ ] features_baseline.csv exists.
[ ] splits.json exists.
[ ] operator_log.md exists.
[ ] session_metadata.json declares synthetic/sample status.
[ ] session_metadata.json includes public/private boundary fields.
[ ] streams_manifest.csv maps synthetic streams clearly.
[ ] events.csv contains synthetic/sample event markers only.
[ ] labels.csv contains non-diagnostic state-window labels only.
[ ] qc_report.json does not imply scientific validation.
[ ] features_baseline.csv contains toy/helper features only.
[ ] splits.json does not imply final benchmark design.
[ ] operator_log.md contains boundary language.
[ ] No sample file contains identifiable data.
[ ] No sample file contains raw human data.
[ ] No sample file contains clinical data.
[ ] No sample file contains Sal-Meter input.
```

---

## Evaluation baseline checklist

```text
[ ] evaluation-baseline/README.md exists.
[ ] requirements.txt exists.
[ ] validate_sample_package.py exists.
[ ] baseline_pipeline_skeleton.py exists.
[ ] leakage_safe_split_example.py exists.
[ ] README explains local validator usage.
[ ] README explains PASS / FAIL meaning.
[ ] README states PASS does not mean benchmark validation.
[ ] README states PASS does not mean scientific validation.
[ ] README states PASS does not mean Sal-Meter validation.
[ ] README states PASS does not mean CAIS compliance.
[ ] README states PASS does not mean diagnostic, clinical, therapeutic, surveillance, certification, or human-ranking authority.
[ ] Validator checks required file presence.
[ ] Validator checks JSON readability.
[ ] Validator checks CSV readability.
[ ] Validator checks schema alignment where applicable.
[ ] Validator checks synthetic/sample status where applicable.
[ ] Validator checks boundary flags where applicable.
[ ] Validator does not validate model performance.
[ ] Validator does not validate benchmark performance.
[ ] Validator does not validate Sal-Meter.
[ ] Validator does not grant CAIS compliance.
```

---

## Protocol helper checklist

```text
[ ] protocol-helper/README.md exists.
[ ] session_label_rule.md exists.
[ ] timestamp_sync_rule.md exists.
[ ] metadata_completeness_rule.md exists.
[ ] human_state_cost_construct_note.md exists.
[ ] future_sal_meter_ab_comparison_rule.md exists.
[ ] Session label rules are non-diagnostic.
[ ] Timestamp sync rules distinguish reviewability from validation.
[ ] Metadata completeness rules distinguish completeness from truth.
[ ] Human-State Cost is described as a proxy construct only.
[ ] Human-State Cost is not described as a person score.
[ ] Human-State Cost is not described as clinical, diagnostic, therapeutic, surveillance, or Sal-Meter output.
[ ] Future Sal-Meter A/B comparison remains future placeholder only.
[ ] Future Sal-Meter A/B comparison does not imply current Sal-Meter input.
[ ] Future Sal-Meter A/B comparison does not imply CAIS compliance.
```

---

## Dashboard mockup checklist

```text
[ ] dashboard-mockup/README.md exists.
[ ] dashboard_claim_boundary.md exists.
[ ] sample_dashboard_fields.json exists.
[ ] mockup_wireframe.md exists.
[ ] Dashboard fields are synthetic/sample/helper fields only.
[ ] Dashboard fields do not imply benchmark validation.
[ ] Dashboard fields do not imply Sal-Meter validation.
[ ] Dashboard fields do not imply CAIS compliance.
[ ] Dashboard fields do not imply clinical interpretation.
[ ] Dashboard fields do not imply diagnostic status.
[ ] Dashboard fields do not imply therapeutic feedback.
[ ] Dashboard fields do not imply surveillance scoring.
[ ] Dashboard fields do not imply certification.
[ ] Dashboard fields do not imply human ranking.
[ ] Dashboard wireframe uses review language, not verdict language.
[ ] Dashboard wireframe avoids person scores.
[ ] Dashboard wireframe avoids human truth scores.
[ ] Dashboard wireframe avoids clinical, diagnostic, therapeutic, surveillance, certification, and legal authority.
```

---

## Closed-loop demo-lite checklist

```text
[ ] closed-loop-demo-lite/README.md exists.
[ ] feedback_loop_boundary.md exists.
[ ] feedback_event_log_schema.json exists.
[ ] local_feedback_demo_placeholder.py exists.
[ ] Demo-lite is described as local.
[ ] Demo-lite is described as non-production.
[ ] Demo-lite is described as synthetic/sample-only.
[ ] Demo-lite does not imply live intervention.
[ ] Demo-lite does not imply real-time monitoring.
[ ] Demo-lite does not imply production automation.
[ ] Demo-lite does not imply medical feedback.
[ ] Demo-lite does not imply therapy.
[ ] Demo-lite does not imply diagnosis.
[ ] Demo-lite does not imply surveillance.
[ ] Demo-lite does not imply human ranking.
[ ] Demo-lite does not imply Sal-Meter validation.
[ ] Demo-lite does not imply CAIS compliance.
[ ] Event log schema prohibits raw human data.
[ ] Event log schema prohibits identifiable data.
[ ] Event log schema prohibits clinical data.
[ ] Event log schema prohibits private user data.
[ ] Event log schema prohibits person scoring.
[ ] Placeholder script does not connect to real sensors.
[ ] Placeholder script does not connect to camera or microphone.
[ ] Placeholder script does not process real biosignals.
[ ] Placeholder script does not call production APIs.
[ ] Placeholder script does not automate intervention.
```

---

## Citation and DOI boundary checklist

```text
[ ] CITATION.cff exists.
[ ] CITATION.cff points to DOI-registered public boundary records.
[ ] CITATION.cff does not treat GitHub as canonical authority.
[ ] README explains DOI authority versus GitHub helper status.
[ ] README includes DOI references for public boundary and scientific rationale records.
[ ] Helper files do not override DOI-registered records.
[ ] Helper files do not reinterpret canonical authority.
[ ] Helper files preserve the public helper boundary.
```

---

## GitHub Actions workflow checklist

```text
[ ] .github/workflows/validate-synthetic-sample.yml exists.
[ ] Workflow name is visible as Validate Synthetic Sample Package.
[ ] Workflow runs validate_sample_package.py.
[ ] Workflow is limited to helper-structure checks only.
[ ] Workflow does not validate benchmark performance.
[ ] Workflow does not validate scientific truth.
[ ] Workflow does not validate Sal-Meter.
[ ] Workflow does not grant CAIS compliance.
[ ] Workflow does not validate diagnostic labels.
[ ] Workflow does not validate clinical interpretation.
[ ] Workflow does not validate therapeutic feedback.
[ ] Workflow does not validate surveillance readiness.
[ ] Workflow does not validate certification readiness.
[ ] Workflow does not validate device readiness.
[ ] Workflow can run successfully before release publication, if release depends on workflow execution.
```

Current known blocker:

```text
Failed to queue workflow run: Bad request - Actions has been disabled for this user.
```

If this blocker remains active, release publication decision is:

```text
Hold
```

---

## Leakage-risk checklist

```text
[ ] Labels are not leaked through filenames.
[ ] Labels are not leaked through folder names.
[ ] Labels are not leaked through session IDs.
[ ] Labels are not leaked through participant IDs.
[ ] Labels are not leaked through operator IDs.
[ ] Labels are not leaked through device IDs.
[ ] Labels are not leaked through timestamps.
[ ] Labels are not leaked through preprocessing artifacts.
[ ] Labels are not leaked through dashboard-visible target fields.
[ ] Labels are not leaked through feedback event logs.
[ ] Train/validation/test separation is described as future strict requirement.
[ ] Leakage-safe split logic is described as helper demonstration only.
[ ] Current synthetic examples are not presented as real benchmark evidence.
```

A package with leakage is not evidence.

A package with hidden leakage is worse than a failed result.

---

## Reproducibility readiness checklist

```text
[ ] A reviewer can identify all major folders.
[ ] A reviewer can identify all required files.
[ ] A reviewer can understand the role of each file.
[ ] A reviewer can distinguish synthetic/sample data from real data.
[ ] A reviewer can distinguish structure checks from scientific validation.
[ ] A reviewer can distinguish GitHub helper status from DOI authority.
[ ] A reviewer can identify what is currently blocked.
[ ] A reviewer can identify what must not be claimed.
[ ] A reviewer can run or inspect the helper validator.
[ ] A reviewer can inspect schemas.
[ ] A reviewer can inspect sample package structure.
[ ] A reviewer can inspect dashboard boundary files.
[ ] A reviewer can inspect closed-loop demo-lite boundary files.
[ ] A reviewer can inspect protocol helper files.
[ ] A reviewer can inspect citation metadata.
[ ] A reviewer can inspect release-readiness status.
```

If these are true, the package may be structurally reviewable.

It still does not become validated.

---

## Release-readiness implication

This checklist may support release readiness only when all critical items pass.

It does not publish the release.

It does not approve the release.

It does not certify the package.

It does not grant CAIS compliance.

It does not validate Sal-Meter.

It only supports a bounded readiness decision.

---

## Decision output block

Use this block after review:

```text
Reproducibility package review decision:

Decision:
Go / Conditional Go / Hold / No-Go

Reason:
[brief reason]

Critical blockers:
[list blockers or "None"]

Boundary risks:
[list risks or "None"]

Release implication:
Ready for public helper release review / Hold release / No-Go release

Authority note:
This review does not validate benchmark performance, Sal-Meter, CAIS compliance, clinical use, diagnosis, therapy, surveillance, certification, or human ranking.
```

---

## P2-4 issue alignment

This file implements:

```text
[P2-4] Add replication guide pack
```

It satisfies:

```text
Create replication-guide/reproducibility_package_checklist.md
```

---

## Completion status

```text
Reproducibility package checklist.
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

## Final rule

A reproducible package lets others retrace the road.

It does not prove the destination.

This checklist confirms whether the road is visible.

It does not claim the mountain has been reached.
