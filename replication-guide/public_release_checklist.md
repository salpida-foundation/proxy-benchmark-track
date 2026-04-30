# Public Release Checklist

This checklist defines whether the public helper repository for the **SICS Human-State Proxy Benchmark Track** is ready for a bounded GitHub helper release.

It checks public helper release readiness.

It does not publish a release by itself.

It does not validate benchmark performance.

It does not validate Sal-Meter.

It does not define CAIS.

It does not grant CAIS compliance.

It does not introduce raw human data.

It does not create diagnostic, clinical, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

---

## Purpose

A public release can look official.

An official-looking release can be misunderstood as validation.

This checklist prevents that drift.

The purpose of this file is to determine whether a GitHub helper release can be published without implying:

- benchmark validation;
- scientific validation;
- Sal-Meter validation;
- CAIS compliance;
- clinical use;
- diagnosis;
- therapy;
- surveillance;
- certification;
- device readiness;
- human ranking;
- raw human data publication.

A release may package helper structure.

A release must not create authority.

---

## Current status

```text
Checklist type: public helper release readiness
Track: SICS Human-State Proxy Benchmark Track
Repository: salpida-foundation/proxy-benchmark-track
Scope: bounded GitHub helper release
Release target: v0.1.0
Release status: not published by this checklist
Validation status: not validated
Sal-Meter status: not present
CAIS compliance status: not granted
Clinical status: not clinical
Diagnostic status: not diagnostic
Therapeutic status: not therapeutic
Surveillance status: not surveillance
Certification status: not certification
Human-ranking status: not human ranking
```

---

## Decision language

Use only the following decision language:

```text
Go
  The repository is ready for a bounded public helper release.

Conditional Go
  The repository is almost ready, but one bounded non-authority correction remains.

Hold
  A required file, boundary, metadata field, audit note, validator condition, DOI reference, or release note is missing.

No-Go
  The repository contains raw human data, identifiable data, clinical data, private user data, Sal-Meter input, CAIS compliance claims, benchmark validation claims, diagnostic claims, therapeutic claims, surveillance claims, certification claims, device-readiness claims, production-intervention claims, or human-ranking claims.
```

Go means the helper release can be published.

Go does not mean the benchmark is validated.

Go does not mean Sal-Meter is validated.

Go does not mean CAIS compliance is granted.

---

## Release identity checklist

```text
[ ] Release target is clearly identified.
[ ] Release title is bounded.
[ ] Release title does not imply validation.
[ ] Release title does not imply certification.
[ ] Release title does not imply CAIS compliance.
[ ] Release title does not imply Sal-Meter validation.
[ ] Release title does not imply clinical use.
[ ] Release title does not imply diagnostic use.
[ ] Release title does not imply therapeutic use.
[ ] Release title does not imply surveillance readiness.
[ ] Release title does not imply human ranking.
```

Recommended release tag:

```text
v0.1.0
```

Recommended release title:

```text
v0.1.0 — Public Helper Structure Readiness
```

Avoid release titles such as:

```text
Validated Human-State Benchmark
Certified CAIS Package
Sal-Meter Ready Release
Clinical Dashboard Release
Closed-Loop Intervention Release
```

---

## Release status checklist

```text
[ ] Release is marked as public helper release.
[ ] Release is marked as research-stage.
[ ] Release is marked as non-clinical.
[ ] Release is marked as non-diagnostic.
[ ] Release is marked as non-therapeutic.
[ ] Release is marked as non-surveillance.
[ ] Release is marked as non-certification.
[ ] Release is marked as non-human-ranking.
[ ] Release is marked as not Sal-Meter.
[ ] Release is marked as not CAIS compliance.
[ ] Release is marked as not benchmark validation.
[ ] Release is marked as not scientific validation.
[ ] Release is marked as not device readiness.
[ ] Release is marked as not production deployment.
[ ] Release is marked as not live intervention.
```

---

## Required release note opening

Use this opening in the release note:

```text
This release packages a bounded public helper structure for the SICS Human-State Proxy Benchmark Track.

It is research-stage, non-clinical, non-diagnostic, non-therapeutic, non-surveillance, non-certification, non-human-ranking, not Sal-Meter, and not CAIS compliance.

It does not validate benchmark performance, scientific truth, Sal-Meter input, CAIS compliance, clinical interpretation, diagnosis, therapy, surveillance, certification, device readiness, production deployment, or human-state truth.
```

---

## Required repository files

```text
[ ] README.md exists.
[ ] LICENSE exists.
[ ] CITATION.cff exists.
[ ] .github/workflows/validate-synthetic-sample.yml exists.
[ ] docs/ exists.
[ ] governance/ exists.
[ ] schemas/ exists.
[ ] sample-data/ exists.
[ ] sample-data/synthetic-session-001/ exists.
[ ] evaluation-baseline/ exists.
[ ] protocol-helper/ exists.
[ ] dashboard-mockup/ exists.
[ ] closed-loop-demo-lite/ exists.
[ ] replication-guide/ exists.
```

If any required folder is missing, decision is:

```text
Hold
```

---

## Root README release checklist

```text
[ ] Root README explains the repository purpose.
[ ] Root README states this is a public technical helper surface.
[ ] Root README states this repository is not the Sal-Meter core signal track.
[ ] Root README states this repository is not a CAIS-compliant device implementation.
[ ] Root README states this repository does not grant CAIS compliance.
[ ] Root README states this repository does not validate benchmark performance.
[ ] Root README states this repository does not publish raw human data.
[ ] Root README states this repository does not contain Sal-Meter input.
[ ] Root README states this repository does not create diagnostic authority.
[ ] Root README states this repository does not create clinical authority.
[ ] Root README states this repository does not create therapeutic authority.
[ ] Root README states this repository does not create surveillance authority.
[ ] Root README states this repository does not create certification authority.
[ ] Root README states this repository does not create human-ranking authority.
[ ] Root README includes DOI authority relationship.
[ ] Root README includes repository structure.
[ ] Root README includes current milestone status.
[ ] Root README includes release hold conditions.
[ ] Root README includes final boundary sentence.
```

---

## Citation and DOI checklist

```text
[ ] CITATION.cff exists.
[ ] CITATION.cff points to DOI-registered public boundary records.
[ ] CITATION.cff includes the public boundary and program charter DOI.
[ ] CITATION.cff includes the scientific rationale and research value DOI.
[ ] README explains that GitHub is a helper surface.
[ ] README explains that DOI records govern authority.
[ ] Release note tells users to cite DOI records, not GitHub as canonical authority.
[ ] Release note does not claim GitHub release is canonical authority.
[ ] Release note does not override DOI-registered SICS / CAIS / Sal-Meter / CCF records.
```

Required authority sentence:

```text
This GitHub release is a public helper surface. DOI-registered records remain the authority layer.
```

---

## License checklist

```text
[ ] LICENSE exists.
[ ] License is visible from the repository root.
[ ] README includes license boundary.
[ ] Release note includes license boundary or refers to README.
[ ] License language does not grant CAIS compliance.
[ ] License language does not grant Sal-Meter designation.
[ ] License language does not grant certification rights.
[ ] License language does not grant mark-usage rights.
[ ] License language does not grant clinical-use rights.
[ ] License language does not grant diagnostic-use rights.
[ ] License language does not grant therapeutic-use rights.
[ ] License language does not grant surveillance-use rights.
[ ] License language does not grant authority to speak for SICS.
[ ] License language does not grant authority to reinterpret DOI-registered records.
```

---

## Public data boundary checklist

```text
[ ] No raw human biosignals are present.
[ ] No raw human video is present.
[ ] No raw human audio is present.
[ ] No face data are present.
[ ] No voice data are present.
[ ] No identifiable participant metadata are present.
[ ] No private session logs are present.
[ ] No clinical data are present.
[ ] No health records are present.
[ ] No consent forms containing personal information are present.
[ ] No internal lab packages are present.
[ ] No Sal-Meter raw input is present.
[ ] No CAIS compliance dossier is present.
[ ] No production feedback logs are present.
[ ] No private user data are present.
```

If any prohibited public data is present, decision is:

```text
No-Go
```

---

## Synthetic/sample status checklist

```text
[ ] Public sample data are marked synthetic, sample, mock, toy, placeholder, or sample-structure-only.
[ ] sample-data/README.md states no raw human data belongs in the repository.
[ ] sample-data/synthetic-session-001/README.md states the package is synthetic/sample only.
[ ] session metadata declares synthetic status.
[ ] operator log declares synthetic/sample status.
[ ] dashboard mockup fields declare synthetic/sample/helper status.
[ ] closed-loop demo-lite files declare synthetic/sample status.
[ ] No sample file is ambiguous.
[ ] No file could be mistaken for a real participant record.
[ ] No file could be mistaken for a clinical record.
[ ] No file could be mistaken for Sal-Meter input.
```

---

## Schema release checklist

```text
[ ] schemas/README.md exists.
[ ] session-metadata.schema.json exists.
[ ] streams-manifest.schema.json exists.
[ ] event-markers.schema.json exists.
[ ] labels.schema.json exists.
[ ] qc-report.schema.json exists.
[ ] features-baseline.schema.json exists.
[ ] splits.schema.json exists.
[ ] Schema README states schemas are public helper only.
[ ] Schema README states schemas do not define CAIS.
[ ] Schema README states schemas do not validate Sal-Meter.
[ ] Schema README states schemas do not grant CAIS compliance.
[ ] Schema README states schemas do not validate benchmark performance.
[ ] Schema fields avoid diagnostic claims.
[ ] Schema fields avoid clinical claims.
[ ] Schema fields avoid therapeutic claims.
[ ] Schema fields avoid surveillance claims.
[ ] Schema fields avoid certification claims.
[ ] Schema fields avoid human-ranking claims.
```

---

## Sample package release checklist

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
[ ] Sample package is marked synthetic/sample only.
[ ] Sample package does not include raw human data.
[ ] Sample package does not include identifiable data.
[ ] Sample package does not include clinical data.
[ ] Sample package does not include private user data.
[ ] Sample package does not include Sal-Meter input.
[ ] Sample package does not claim CAIS compliance.
[ ] Sample package does not claim benchmark validation.
[ ] Sample package does not claim scientific validation.
```

---

## Evaluation baseline release checklist

```text
[ ] evaluation-baseline/README.md exists.
[ ] requirements.txt exists.
[ ] validate_sample_package.py exists.
[ ] baseline_pipeline_skeleton.py exists.
[ ] leakage_safe_split_example.py exists.
[ ] README explains validator usage.
[ ] README explains PASS / FAIL interpretation.
[ ] README states PASS does not mean benchmark validation.
[ ] README states PASS does not mean scientific validation.
[ ] README states PASS does not mean Sal-Meter validation.
[ ] README states PASS does not mean CAIS compliance.
[ ] README states PASS does not mean clinical, diagnostic, therapeutic, surveillance, certification, device, or human-ranking readiness.
[ ] Validator is described as helper-structure validation only.
[ ] Baseline pipeline is described as skeleton only.
[ ] Leakage-safe split example is described as helper demonstration only.
```

---

## GitHub Actions release checklist

```text
[ ] .github/workflows/validate-synthetic-sample.yml exists.
[ ] Workflow appears in the Actions tab.
[ ] Workflow name is Validate Synthetic Sample Package.
[ ] Workflow runs evaluation-baseline/validate_sample_package.py.
[ ] Workflow is limited to helper-structure checks.
[ ] Workflow does not validate benchmark performance.
[ ] Workflow does not validate scientific truth.
[ ] Workflow does not validate Sal-Meter.
[ ] Workflow does not grant CAIS compliance.
[ ] Workflow does not validate clinical interpretation.
[ ] Workflow does not validate diagnosis.
[ ] Workflow does not validate therapy.
[ ] Workflow does not validate surveillance readiness.
[ ] Workflow does not validate certification readiness.
[ ] Workflow does not validate device readiness.
[ ] Workflow can run successfully before release publication, if this release depends on validator execution.
```

Known current blocker:

```text
Failed to queue workflow run: Bad request - Actions has been disabled for this user.
```

If this blocker remains active, release decision is:

```text
Hold
```

---

## Protocol helper release checklist

```text
[ ] protocol-helper/README.md exists.
[ ] session_label_rule.md exists.
[ ] timestamp_sync_rule.md exists.
[ ] metadata_completeness_rule.md exists.
[ ] human_state_cost_construct_note.md exists.
[ ] future_sal_meter_ab_comparison_rule.md exists.
[ ] Session labels remain non-diagnostic.
[ ] Timestamp rules distinguish alignment from validation.
[ ] Metadata completeness rules distinguish completeness from truth.
[ ] Human-State Cost remains a proxy construct only.
[ ] Human-State Cost is not presented as a person score.
[ ] Human-State Cost is not presented as diagnosis.
[ ] Human-State Cost is not presented as therapy.
[ ] Human-State Cost is not presented as surveillance.
[ ] Human-State Cost is not presented as Sal-Meter.
[ ] Human-State Cost is not presented as CAIS compliance.
[ ] Future Sal-Meter A/B comparison remains inactive placeholder only.
```

---

## Dashboard mockup release checklist

```text
[ ] dashboard-mockup/README.md exists.
[ ] dashboard_claim_boundary.md exists.
[ ] sample_dashboard_fields.json exists.
[ ] mockup_wireframe.md exists.
[ ] Dashboard is marked as mockup.
[ ] Dashboard is marked as public helper visualization boundary.
[ ] Dashboard fields are synthetic/sample/helper fields only.
[ ] Dashboard does not imply benchmark validation.
[ ] Dashboard does not imply scientific validation.
[ ] Dashboard does not imply Sal-Meter validation.
[ ] Dashboard does not imply CAIS compliance.
[ ] Dashboard does not imply diagnosis.
[ ] Dashboard does not imply clinical interpretation.
[ ] Dashboard does not imply therapy.
[ ] Dashboard does not imply surveillance.
[ ] Dashboard does not imply certification.
[ ] Dashboard does not imply human ranking.
[ ] Dashboard does not imply person scoring.
[ ] Dashboard does not imply legal, insurance, employment, education, or eligibility authority.
```

---

## Closed-loop demo-lite release checklist

```text
[ ] closed-loop-demo-lite/README.md exists.
[ ] feedback_loop_boundary.md exists.
[ ] feedback_event_log_schema.json exists.
[ ] local_feedback_demo_placeholder.py exists.
[ ] Closed-loop demo-lite is marked local.
[ ] Closed-loop demo-lite is marked non-production.
[ ] Closed-loop demo-lite is marked synthetic/sample-only.
[ ] Closed-loop demo-lite is marked helper-structure-only.
[ ] Closed-loop demo-lite does not imply live intervention.
[ ] Closed-loop demo-lite does not imply real-time monitoring.
[ ] Closed-loop demo-lite does not imply production automation.
[ ] Closed-loop demo-lite does not imply medical feedback.
[ ] Closed-loop demo-lite does not imply diagnosis.
[ ] Closed-loop demo-lite does not imply therapy.
[ ] Closed-loop demo-lite does not imply surveillance.
[ ] Closed-loop demo-lite does not imply certification.
[ ] Closed-loop demo-lite does not imply human ranking.
[ ] Closed-loop demo-lite does not imply Sal-Meter validation.
[ ] Closed-loop demo-lite does not imply CAIS compliance.
[ ] Placeholder script does not connect to sensors.
[ ] Placeholder script does not connect to camera.
[ ] Placeholder script does not connect to microphone.
[ ] Placeholder script does not process real biosignals.
[ ] Placeholder script does not call production APIs.
[ ] Placeholder script does not automate intervention.
```

---

## Replication guide release checklist

```text
[ ] replication-guide/README.md exists.
[ ] reproducibility_package_checklist.md exists.
[ ] metadata_completeness_checklist.md exists.
[ ] audit_trail_checklist.md exists.
[ ] public_release_checklist.md exists.
[ ] Replication guide distinguishes reproducibility readiness from scientific validation.
[ ] Replication guide distinguishes metadata completeness from truth.
[ ] Replication guide distinguishes audit trail readiness from evidence validation.
[ ] Replication guide distinguishes GitHub helper release readiness from DOI authority.
[ ] Replication guide does not publish a release by itself.
[ ] Replication guide does not claim benchmark validation.
[ ] Replication guide does not claim Sal-Meter validation.
[ ] Replication guide does not claim CAIS compliance.
[ ] Replication guide does not claim clinical, diagnostic, therapeutic, surveillance, certification, or human-ranking authority.
```

---

## Release note required boundaries

The release note must state:

```text
[ ] This is a public helper release.
[ ] This is research-stage.
[ ] This is non-clinical.
[ ] This is non-diagnostic.
[ ] This is non-therapeutic.
[ ] This is non-surveillance.
[ ] This is non-certification.
[ ] This is non-human-ranking.
[ ] This is not Sal-Meter.
[ ] This does not define CAIS.
[ ] This does not grant CAIS compliance.
[ ] This does not validate Sal-Meter.
[ ] This does not validate benchmark performance.
[ ] This does not publish raw human data.
[ ] This does not publish identifiable data.
[ ] This does not publish clinical data.
[ ] This does not publish private user data.
[ ] This does not deploy live feedback.
[ ] This does not deploy production automation.
[ ] DOI-registered records remain the authority layer.
```

---

## Prohibited release note language

Do not use:

```text
validated benchmark
validated Sal-Meter
CAIS-compliant release
certified package
certified benchmark
clinical validation
diagnostic validation
therapeutic validation
approved device
commercial readiness
official compliance result
human-state truth validation
consciousness truth score
production intervention system
surveillance-ready system
closed-loop intervention system
human safety score
employee risk score
patient score
```

If any prohibited phrase appears, decision is:

```text
Hold
```

If the phrase is making an actual prohibited claim, decision is:

```text
No-Go
```

---

## Required release note draft

Use this release note draft if the release is eventually published:

```text
# v0.1.0 — Public Helper Structure Readiness

This release packages a bounded public helper structure for the SICS Human-State Proxy Benchmark Track.

It is research-stage, non-clinical, non-diagnostic, non-therapeutic, non-surveillance, non-certification, non-human-ranking, not Sal-Meter, and not CAIS compliance.

This release does not validate benchmark performance, scientific truth, Sal-Meter input, CAIS compliance, clinical interpretation, diagnosis, therapy, surveillance, certification, device readiness, production deployment, or human-state truth.

Included public helper components:

- root README.md with repository scope, current status, public boundary, and DOI authority relationship;
- CITATION.cff pointing to DOI-registered public records;
- LICENSE;
- governance boundary files;
- public language boundary files;
- schemas/ helper schemas;
- sample-data/ synthetic/sample package;
- evaluation-baseline/ helper validator and baseline skeletons;
- protocol-helper/ boundary rules;
- dashboard-mockup/ boundary files;
- closed-loop-demo-lite/ boundary files and local placeholder script;
- replication-guide/ review checklists.

Data boundary:

- no raw human data;
- no identifiable data;
- no clinical data;
- no private user data;
- no Sal-Meter input;
- no CAIS compliance dossier;
- no production feedback logs.

Authority boundary:

This GitHub release is a public helper surface. DOI-registered records remain the authority layer.

Known limitations:

- This is not benchmark validation.
- This is not Sal-Meter validation.
- This is not CAIS compliance.
- This is not a medical, diagnostic, therapeutic, clinical, surveillance, certification, employment, insurance, educational, legal, eligibility, or human-ranking system.

Release decision:

Go / Conditional Go / Hold / No-Go
```

Do not publish this draft until the release decision is Go.

---

## Release blocker checklist

```text
[ ] GitHub Actions account-level blocker resolved, if validator execution is required.
[ ] Validate Synthetic Sample Package workflow can run, if release depends on workflow execution.
[ ] Validator result is PASS, if release depends on validator execution.
[ ] No critical README boundary is missing.
[ ] No critical folder README is missing.
[ ] No critical schema file is missing.
[ ] No critical synthetic sample file is missing.
[ ] No critical evaluation baseline file is missing.
[ ] No critical protocol helper file is missing.
[ ] No critical dashboard mockup file is missing.
[ ] No critical closed-loop demo-lite file is missing.
[ ] No critical replication guide file is missing.
[ ] No prohibited data are present.
[ ] No prohibited claims are present.
```

If any blocker remains unresolved, release decision is:

```text
Hold
```

---

## Final pre-release review checklist

```text
[ ] Root README reviewed.
[ ] CITATION.cff reviewed.
[ ] LICENSE reviewed.
[ ] governance/ reviewed.
[ ] docs/ reviewed.
[ ] schemas/ reviewed.
[ ] sample-data/ reviewed.
[ ] evaluation-baseline/ reviewed.
[ ] protocol-helper/ reviewed.
[ ] dashboard-mockup/ reviewed.
[ ] closed-loop-demo-lite/ reviewed.
[ ] replication-guide/ reviewed.
[ ] Repository About text reviewed.
[ ] Repository topics reviewed.
[ ] Release title reviewed.
[ ] Release note reviewed.
[ ] DOI authority wording reviewed.
[ ] Public/private boundary reviewed.
[ ] Prohibited data reviewed.
[ ] Prohibited claims reviewed.
[ ] Known blockers reviewed.
[ ] Release decision recorded.
```

---

## Go / Hold / No-Go release decision

### Go

Use Go only when:

```text
[ ] Required files are present.
[ ] Required boundaries are visible.
[ ] No prohibited data are present.
[ ] No prohibited claims are present.
[ ] DOI authority is clear.
[ ] GitHub helper status is clear.
[ ] Release note is bounded.
[ ] Validator condition is satisfied, if required.
```

### Conditional Go

Use Conditional Go only when:

```text
[ ] All critical safety boundaries are preserved.
[ ] One minor non-authority correction remains.
[ ] The correction is clearly listed.
[ ] Release is not published until the correction is completed.
```

### Hold

Use Hold when:

```text
[ ] A required helper file is missing.
[ ] A required README boundary is missing.
[ ] A required metadata field is missing.
[ ] A required audit note is missing.
[ ] GitHub Actions validator cannot run when validator execution is required.
[ ] Release note is incomplete.
[ ] DOI authority distinction is unclear.
[ ] Public/private boundary is unclear.
```

### No-Go

Use No-Go when:

```text
[ ] Raw human data are present.
[ ] Identifiable data are present.
[ ] Clinical data are present.
[ ] Private user data are present.
[ ] Sal-Meter input is present without separate governance.
[ ] CAIS compliance claim is present.
[ ] Benchmark validation claim is present.
[ ] Diagnostic claim is present.
[ ] Therapeutic claim is present.
[ ] Surveillance claim is present.
[ ] Certification claim is present.
[ ] Device-readiness claim is present.
[ ] Production-intervention claim is present.
[ ] Human-ranking claim is present.
```

---

## Release decision block

Use this block before publishing:

```text
Public helper release decision:

Release tag:
v0.1.0

Release title:
v0.1.0 — Public Helper Structure Readiness

Decision:
Go / Conditional Go / Hold / No-Go

Reason:
[brief reason]

Critical blockers:
[list blockers or "None"]

Boundary risks:
[list risks or "None"]

Data-publication risk:
None / Hold / No-Go

GitHub Actions status:
PASS / Blocked / Not required for this release

Sal-Meter boundary:
Not present / Future placeholder only / Risk found

CAIS boundary:
Not granted / Risk found

Benchmark validation boundary:
Not validated / Risk found

DOI authority note:
DOI-registered records remain the authority layer. GitHub is a public helper surface only.

Final publication instruction:
Publish / Do not publish
```

---

## P2-4 issue alignment

This file implements:

```text
[P2-4] Add replication guide pack
```

It satisfies:

```text
Create replication-guide/public_release_checklist.md
```

---

## Completion status

```text
Public release checklist.
Research-stage.
Public helper documentation only.
Release-readiness review only.
Not release publication.
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
No production intervention.
```

---

## Final rule

A release is a bell.

It tells the world something is ready to be seen.

It must not tell the world something has been proven.

This checklist decides whether the bell may ring.

It does not declare the mountain conquered.
