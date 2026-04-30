# Pull Request Boundary Review

Thank you for contributing to the SICS Human-State Proxy Benchmark Track public helper repository.

This repository is research-stage, public-helper-only, non-clinical, non-diagnostic, non-therapeutic, non-surveillance, non-certification, non-human-ranking, not Sal-Meter, and not CAIS compliance.

This pull request must preserve that boundary.

---

## Summary

Describe the change in plain language.

- What does this PR change?
- Why is the change needed?
- Which files or folders are affected?

Summary:

---

## Linked issue

Link the related issue, if any.

Related issue:

- [ ] No linked issue
- [ ] Boundary correction issue
- [ ] Schema request issue
- [ ] Sample data issue
- [ ] Leakage risk report
- [ ] Other issue

Issue link or number:

---

## Change type

Check all that apply.

- [ ] Documentation update
- [ ] Boundary language correction
- [ ] Schema helper update
- [ ] Synthetic/sample data structure update
- [ ] Evaluation baseline update
- [ ] Validator update
- [ ] Protocol helper update
- [ ] Dashboard mockup update
- [ ] Closed-loop demo-lite update
- [ ] Replication guide update
- [ ] Issue template update
- [ ] Pull request template update
- [ ] GitHub Actions workflow update
- [ ] Citation / DOI reference update
- [ ] License or governance wording update
- [ ] Other bounded public-helper change

---

## Affected areas

Check all that apply.

- [ ] README.md
- [ ] CITATION.cff
- [ ] LICENSE
- [ ] docs/
- [ ] governance/
- [ ] schemas/
- [ ] sample-data/
- [ ] sample-data/synthetic-session-001/
- [ ] evaluation-baseline/
- [ ] protocol-helper/
- [ ] dashboard-mockup/
- [ ] closed-loop-demo-lite/
- [ ] replication-guide/
- [ ] .github/ISSUE_TEMPLATE/
- [ ] .github/pull_request_template.md
- [ ] .github/workflows/
- [ ] Repository About text or topics
- [ ] Other

Affected files:

---

## Public helper boundary

This PR must remain public-helper-only.

- [ ] This PR is research-stage.
- [ ] This PR is public-helper-only.
- [ ] This PR is non-clinical.
- [ ] This PR is non-diagnostic.
- [ ] This PR is non-therapeutic.
- [ ] This PR is non-surveillance.
- [ ] This PR is non-certification.
- [ ] This PR is non-human-ranking.
- [ ] This PR is not Sal-Meter.
- [ ] This PR does not define CAIS.
- [ ] This PR does not grant CAIS compliance.
- [ ] This PR does not validate Sal-Meter.
- [ ] This PR does not validate benchmark performance.
- [ ] This PR does not create device readiness.
- [ ] This PR does not create production deployment.
- [ ] This PR does not create live intervention.

---

## Data boundary

This PR must not introduce prohibited data.

- [ ] No raw human biosignals are added.
- [ ] No raw human video is added.
- [ ] No raw human audio is added.
- [ ] No face data are added.
- [ ] No voice data are added.
- [ ] No identifiable participant metadata are added.
- [ ] No private session logs are added.
- [ ] No clinical data are added.
- [ ] No health records are added.
- [ ] No consent forms containing personal information are added.
- [ ] No internal lab packages are added.
- [ ] No Sal-Meter raw input is added.
- [ ] No CAIS compliance dossier is added.
- [ ] No production feedback logs are added.
- [ ] No private user data are added.

If this PR includes sample files, confirm:

- [ ] All sample files are synthetic, sample, mock, toy, placeholder, or sample-structure-only.
- [ ] Sample files cannot be mistaken for real participant data.
- [ ] Sample files cannot be mistaken for clinical data.
- [ ] Sample files cannot be mistaken for Sal-Meter input.

---

## Claim boundary

This PR must not introduce prohibited claims.

- [ ] No benchmark validation claim is introduced.
- [ ] No scientific validation claim is introduced.
- [ ] No Sal-Meter validation claim is introduced.
- [ ] No CAIS compliance claim is introduced.
- [ ] No clinical validation claim is introduced.
- [ ] No diagnostic validation claim is introduced.
- [ ] No therapeutic validation claim is introduced.
- [ ] No surveillance readiness claim is introduced.
- [ ] No certification readiness claim is introduced.
- [ ] No device readiness claim is introduced.
- [ ] No commercial readiness claim is introduced.
- [ ] No production intervention claim is introduced.
- [ ] No human-state truth validation claim is introduced.
- [ ] No human-ranking claim is introduced.
- [ ] No person score is introduced.
- [ ] No legal eligibility score is introduced.
- [ ] No insurance score is introduced.
- [ ] No employment score is introduced.
- [ ] No education score is introduced.

---

## Required language review

Use bounded language.

Allowed language:

- [ ] public helper
- [ ] research-stage
- [ ] synthetic/sample
- [ ] structure review
- [ ] reviewability
- [ ] metadata completeness
- [ ] audit trail
- [ ] leakage risk
- [ ] release readiness
- [ ] not validation
- [ ] not Sal-Meter
- [ ] not CAIS compliance
- [ ] not diagnostic
- [ ] not clinical
- [ ] not therapeutic
- [ ] not surveillance
- [ ] not certification
- [ ] not human ranking

Do not use:

- [ ] validated benchmark
- [ ] validated Sal-Meter
- [ ] CAIS-compliant package
- [ ] certified reproducibility
- [ ] clinical validation
- [ ] diagnostic validation
- [ ] therapeutic validation
- [ ] approved device
- [ ] commercial readiness
- [ ] official compliance result
- [ ] human-state truth validation
- [ ] production intervention
- [ ] surveillance-ready system

---

## DOI / authority boundary

DOI-registered records remain the authority layer.

- [ ] This PR does not replace DOI-registered SICS / CAIS / Sal-Meter / CCF records.
- [ ] This PR does not create canonical authority.
- [ ] This PR does not reinterpret canonical records.
- [ ] This PR does not grant compliance authority.
- [ ] This PR does not grant certification authority.
- [ ] This PR preserves GitHub as a public helper surface.
- [ ] If citation or DOI text changed, the DOI authority boundary remains clear.
- [ ] If README authority language changed, DOI records still prevail over helper files.

Citation / DOI notes:

---

## Validation versus readiness

This PR must distinguish readiness from validation.

- [ ] Structure readiness is not described as scientific validation.
- [ ] Metadata completeness is not described as truth.
- [ ] Audit trail readiness is not described as evidence validation.
- [ ] Public helper release readiness is not described as canonical authority.
- [ ] Validator PASS is not described as benchmark validation.
- [ ] Validator PASS is not described as Sal-Meter validation.
- [ ] Validator PASS is not described as CAIS compliance.
- [ ] Dashboard mockup is not described as measurement validation.
- [ ] Closed-loop demo-lite is not described as intervention readiness.
- [ ] Replication guide is not described as scientific proof.

---

## Leakage-risk review

Check whether this PR introduces or reduces leakage risk.

- [ ] No known leakage-risk impact.
- [ ] Possible label leakage through filenames reviewed.
- [ ] Possible label leakage through folder names reviewed.
- [ ] Possible label leakage through timestamps reviewed.
- [ ] Possible label leakage through metadata fields reviewed.
- [ ] Possible label leakage through session identity reviewed.
- [ ] Possible label leakage through device identity reviewed.
- [ ] Possible label leakage through operator identity reviewed.
- [ ] Possible leakage through dashboard fields reviewed.
- [ ] Possible leakage through feedback event logs reviewed.
- [ ] Possible split contamination reviewed.
- [ ] Possible holdout contamination reviewed.
- [ ] Target variable is not present in feature fields.
- [ ] Target variable is not present in QC fields.
- [ ] Target variable is not present in split definitions.
- [ ] Target variable is not present in audit notes.

Leakage-risk notes:

---

## Schema impact

Does this PR affect schemas?

- [ ] No schema impact.
- [ ] Schema file added.
- [ ] Schema file modified.
- [ ] Schema README updated.
- [ ] Sample data updated to match schema.
- [ ] Validator updated to match schema.
- [ ] Dashboard fields updated to match schema.
- [ ] Closed-loop demo-lite event-log schema updated.
- [ ] Schema change requires separate review.

Schema notes:

---

## Sample-data impact

Does this PR affect sample data?

- [ ] No sample-data impact.
- [ ] Synthetic/sample file added.
- [ ] Synthetic/sample file modified.
- [ ] Synthetic/sample README updated.
- [ ] Session metadata updated.
- [ ] Stream manifest updated.
- [ ] Event markers updated.
- [ ] Labels updated.
- [ ] QC report updated.
- [ ] Feature table updated.
- [ ] Splits updated.
- [ ] Operator log updated.
- [ ] Sample-data change requires validator review.

Sample-data notes:

---

## Dashboard impact

Does this PR affect dashboard mockups?

- [ ] No dashboard impact.
- [ ] Dashboard README updated.
- [ ] Dashboard claim boundary updated.
- [ ] Sample dashboard fields updated.
- [ ] Mockup wireframe updated.
- [ ] Dashboard language remains mockup-only.
- [ ] Dashboard language remains non-diagnostic.
- [ ] Dashboard language remains non-clinical.
- [ ] Dashboard language remains non-therapeutic.
- [ ] Dashboard language remains non-surveillance.
- [ ] Dashboard language remains non-certification.
- [ ] Dashboard language remains non-human-ranking.
- [ ] Dashboard does not imply Sal-Meter validation.
- [ ] Dashboard does not imply CAIS compliance.

Dashboard notes:

---

## Closed-loop demo-lite impact

Does this PR affect closed-loop demo-lite files?

- [ ] No closed-loop demo-lite impact.
- [ ] Closed-loop demo-lite README updated.
- [ ] Feedback loop boundary updated.
- [ ] Feedback event-log schema updated.
- [ ] Local placeholder script updated.
- [ ] Demo-lite remains local.
- [ ] Demo-lite remains non-production.
- [ ] Demo-lite remains synthetic/sample-only.
- [ ] Demo-lite does not perform real intervention.
- [ ] Demo-lite does not perform real-time monitoring.
- [ ] Demo-lite does not perform diagnosis.
- [ ] Demo-lite does not provide therapy.
- [ ] Demo-lite does not create surveillance.
- [ ] Demo-lite does not rank humans.
- [ ] Demo-lite does not validate Sal-Meter.
- [ ] Demo-lite does not grant CAIS compliance.

Closed-loop demo-lite notes:

---

## Validator impact

Does this PR affect the helper validator?

- [ ] No validator impact.
- [ ] Validator file changed.
- [ ] Workflow file changed.
- [ ] Required file check changed.
- [ ] JSON parse check changed.
- [ ] CSV column check changed.
- [ ] Schema alignment check changed.
- [ ] Synthetic/sample status check changed.
- [ ] Boundary-flag check changed.
- [ ] Leakage-risk check changed.
- [ ] Validator documentation changed.

Validator notes:

---

## GitHub Actions status

If this PR affects `.github/workflows/`, confirm:

- [ ] Workflow remains helper-structure-only.
- [ ] Workflow does not validate benchmark performance.
- [ ] Workflow does not validate scientific truth.
- [ ] Workflow does not validate Sal-Meter.
- [ ] Workflow does not grant CAIS compliance.
- [ ] Workflow does not validate clinical interpretation.
- [ ] Workflow does not validate diagnosis.
- [ ] Workflow does not validate therapy.
- [ ] Workflow does not validate surveillance readiness.
- [ ] Workflow does not validate certification readiness.
- [ ] Workflow does not validate device readiness.

Current known blocker, if still applicable:

- [ ] GitHub Actions may still be blocked by account-level restriction.
- [ ] Release remains on Hold if validator execution is required and cannot run.

---

## Release impact

Does this PR affect release readiness?

- [ ] No release-readiness impact.
- [ ] Improves release-readiness documentation.
- [ ] Improves boundary clarity.
- [ ] Improves metadata completeness.
- [ ] Improves audit trail.
- [ ] Improves public/private data boundary.
- [ ] Improves leakage-risk control.
- [ ] Improves validator readiness.
- [ ] Requires P1-4 validator status review.
- [ ] Requires P1-5 release-readiness review.
- [ ] Release must remain unpublished until required blockers are resolved.

Release notes:

---

## Local checks

Run applicable checks.

- [ ] Not applicable.
- [ ] README rendered correctly.
- [ ] Markdown preview checked.
- [ ] JSON syntax checked.
- [ ] CSV structure checked.
- [ ] Schema alignment checked.
- [ ] Local validator run.
- [ ] GitHub Actions workflow reviewed.
- [ ] No prohibited data present.
- [ ] No prohibited claims present.

Local check output or notes:

---

## Reviewer checklist

Reviewer should confirm:

- [ ] Scope is clear.
- [ ] Affected files are listed.
- [ ] Public/private data boundary is preserved.
- [ ] Claim boundary is preserved.
- [ ] DOI authority boundary is preserved.
- [ ] Validation-versus-readiness distinction is preserved.
- [ ] Leakage risk is reviewed.
- [ ] Sample data remain synthetic/sample/mock/placeholder only.
- [ ] No raw human data are introduced.
- [ ] No identifiable data are introduced.
- [ ] No clinical data are introduced.
- [ ] No private user data are introduced.
- [ ] No Sal-Meter input is introduced.
- [ ] No CAIS compliance claim is introduced.
- [ ] No benchmark validation claim is introduced.
- [ ] No diagnostic, clinical, therapeutic, surveillance, certification, or human-ranking authority is introduced.
- [ ] Release impact is clear.

---

## Proposed merge decision

Select one.

- [ ] Go — PR is bounded and ready to merge.
- [ ] Conditional Go — PR is acceptable after a small bounded correction.
- [ ] Hold — more boundary, metadata, leakage, validator, or authority review is needed.
- [ ] No-Go — prohibited data or prohibited authority claim is present.

---

## Final boundary sentence

A pull request may improve the scaffold.

It must not move the mountain.

It must not turn helper structure into validation.

It must not turn GitHub into canonical authority.
