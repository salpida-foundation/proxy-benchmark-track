# Contribution Policy

This document defines the contribution policy for the SICS Human-State Proxy Benchmark Track public technical helper repository.

This repository is a research-stage public helper surface.

It is not the canonical authority layer.

It is not the Sal-Meter core signal track.

It is not a CAIS-compliant device implementation.

It is not a clinical, diagnostic, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking system.

---

## 1. Purpose

The purpose of this policy is to keep contributions useful, bounded, auditable, and safe.

This repository may accept contributions that improve:

- documentation clarity
- metadata discipline
- schema structure
- synthetic sample data structure
- leakage-control logic
- reproducibility checklists
- baseline evaluation skeletons
- dashboard mockup boundaries
- closed-loop demo-lite boundaries
- public/private data separation
- prohibited-claim correction
- future Sal-Meter A/B comparison structure

This repository must not accept contributions that introduce:

- raw human data
- private participant data
- clinical or diagnostic claims
- therapeutic claims
- surveillance scoring
- human-ranking logic
- Sal-Meter validation claims
- CAIS compliance claims
- certification claims
- uncontrolled public interpretation drift

The repository should grow by becoming clearer, safer, and more reproducible.

It should not grow by making larger claims.

---

## 2. Current repository status

research-stage · non-clinical · non-diagnostic · non-therapeutic · non-surveillance · non-coercive · pre-device · pre-certification · pre-compliance · benchmark support only

---

## 3. Repository role

This repository supports:

- synchronized multimodal benchmark design
- metadata schema examples
- event marker examples
- synthetic sample-data structure
- leakage-safe evaluation helpers
- reproducibility checklists
- baseline model skeletons
- dashboard mockups
- closed-loop demo-lite planning
- future comparison with Sal-Meter I/G-channel inputs

This repository does not:

- define CAIS
- define Sal-Meter
- validate Sal-Meter
- grant CAIS compliance
- grant certification
- grant mark-usage rights
- publish raw human data
- create clinical, diagnostic, therapeutic, surveillance, employment, insurance, legal, educational, eligibility, or human-ranking authority

---

## 4. Who should contribute

Good-fit contributors include people who can improve one bounded layer.

### PBEE-type contributions

Physiological Biosignal & Edge Engineering contributors may help with:

- stream manifest examples
- LSL / BrainFlow / Timeflux helper notes
- device dropout fields
- sync-error fields
- timestamp quality structure
- signal QC notes
- edge inference placeholder structure

### MDE-type contributions

Machine Learning / Data Engineering contributors may help with:

- metadata schemas
- synthetic sample data
- leakage-safe split examples
- baseline model skeletons
- error-analysis templates
- reproducibility packs
- feature table examples
- validation of JSON / CSV structures

### HSOPM-type contributions

Human-Session Operations / Protocol Management contributors may help with:

- operator log templates
- session flow helpers
- consent-boundary wording
- participant-code rules
- public/private data separation
- session metadata completeness
- deviation log templates

### EStL-type contributions

Evidence & Statistical Traceability contributors may help with:

- leakage checklist review
- holdout design
- audit trail structure
- metadata completeness rules
- reproducibility checklists
- boundary correction
- public wording control

### ESL-type contributions

Experimental Stability Lead contributors may review future A/B comparison readiness, but this repository is not the core molecular-electrochemical signal track.

The Sal-Meter core signal path remains separate.

---

## 5. Accepted contribution types

The following contributions are welcome.

### Documentation improvements

Accepted:

- clearer wording
- typo fixes
- broken link fixes
- stronger boundary language
- simpler explanation of repository purpose
- better separation between core track and proxy track
- better public/private data wording

Not accepted:

- claim inflation
- speculative clinical framing
- Sal-Meter equivalence language
- CAIS compliance language
- promotional claims without evidence

---

### Schema improvements

Accepted:

- JSON schema improvements
- CSV column definitions
- field naming corrections
- metadata completeness improvements
- event marker refinements
- QC report structure improvements
- split file structure improvements

Not accepted:

- schemas that imply clinical scoring
- schemas that expose direct identifiers
- schemas that embed private labels
- schemas that imply Sal-Meter validation
- schemas that imply CAIS compliance

---

### Synthetic sample-data improvements

Accepted:

- synthetic session examples
- toy event marker files
- mock metadata examples
- synthetic QC reports
- synthetic baseline feature tables
- synthetic split files
- toy operator logs

Not accepted:

- raw human biosignals
- real participant data
- real video
- real audio
- face data
- clinical records
- private session logs
- consent forms with personal information
- internal lab packages

Every public sample file must clearly state whether it is:

```text
synthetic
toy
mock
schema-only
```

---

### Leakage-control improvements

Accepted:

- leakage-risk examples
- holdout split improvements
- train / validation / test separation guidance
- participant-holdout suggestions
- device-holdout suggestions
- day-holdout suggestions
- condition-holdout suggestions
- warning examples for hidden labels

Not accepted:

- performance claims without leakage review
- final-holdout tuning
- shortcuts that embed labels in filenames
- split logic that leaks participant, device, day, or condition information

---

### Dashboard mockup improvements

Accepted dashboard concepts:

- stream status
- timestamp quality
- packet loss
- session phase
- event marker timing
- proxy trend
- QC status
- synthetic Human-State Cost trend as a non-diagnostic benchmark construct

Not accepted dashboard concepts:

- diagnosis
- clinical stress score
- psychological safety score
- consciousness truth score
- employee ranking
- student ranking
- insurance score
- legal eligibility score
- Sal-Meter validation status
- CAIS compliance status

---

### Closed-loop demo-lite improvements

Accepted:

- reversible feedback timing
- UI pacing adjustment
- local interaction pacing
- simulator event adjustment
- non-coercive feedback
- human-overridable interaction control
- synthetic feedback event logs

Not accepted:

- therapy
- diagnosis
- medical intervention
- stress treatment
- psychiatric monitoring
- coercive nudging
- behavioral control
- employee monitoring
- student monitoring
- clinical safety management

Closed-loop means interaction feedback.

It does not mean clinical intervention.

---

## 6. Not accepted under any condition

The following are not accepted in this repository:

- raw human data
- identifiable participant records
- real face data
- real voice data
- raw video from real sessions
- raw audio from real sessions
- clinical records
- medical records
- psychiatric records
- consent forms containing personal information
- private session logs
- internal lab packages
- unpublished human-subject data
- passwords
- API keys
- storage credentials
- private dataset links
- private participant schedules
- real location logs
- device serial numbers tied to real participants
- claims of Sal-Meter validation
- claims of CAIS compliance
- claims of clinical validity
- claims of diagnostic validity
- claims of therapeutic effect
- claims of certification or authorization
- human ranking systems
- surveillance scoring systems

If a contribution contains any of the above, it should be rejected or removed.

---

## 7. Public language rule

Use bounded language.

Preferred language:

```text
research-stage
proxy benchmark track
benchmark support
human-state-aware interaction
synchronized multimodal benchmark
metadata discipline
leakage-safe evaluation
baseline models
closed-loop demo-lite
Human-State Cost as non-diagnostic benchmark construct
future comparison with Sal-Meter inputs
public technical helper surface
```

Avoid and remove prohibited language:

```text
Proxy Sal-Meter
non-molecular Sal-Meter
validated Sal-Meter
certified Sal-Meter
CAIS-compliant proxy stack
CAIS-compliant device
validated consciousness measurement
clinical stress system
diagnostic stress system
therapeutic feedback system
psychological safety score
employee wellbeing monitoring system
student ranking system
insurance risk score
human-state diagnosis
AI harm diagnosis
medical device
commercial validated device
```

---

## 8. Human-State Cost contribution rule

Human-State Cost is a non-diagnostic benchmark construct.

Contributors may discuss Human-State Cost only as a way to compare bounded interaction conditions.

Allowed:

```text
Human-State Cost may compare proxy burden between interaction condition A and interaction condition B.
Human-State Cost is a non-diagnostic benchmark construct.
Human-State Cost is not a score for ranking human beings.
```

Not allowed:

```text
Human-State Cost diagnoses people.
Human-State Cost measures consciousness.
Human-State Cost ranks human quality.
Human-State Cost is a clinical stress score.
Human-State Cost proves AI harm.
Human-State Cost validates Sal-Meter.
Human-State Cost is VCE / CRI / CFI.
```

Human-State Cost evaluates interaction conditions.

It does not judge the person.

---

## 9. Future Sal-Meter comparison rule

This repository may prepare a future comparison lane for Sal-Meter I/G-channel inputs.

Contributors may write:

```text
future comparison with Sal-Meter inputs
future A/B comparison surface
proxy baseline for later comparison
benchmark support layer
```

Contributors must not write:

```text
proxy data validates Sal-Meter
proxy stack is Sal-Meter
non-molecular Sal-Meter
CAIS-compliant proxy benchmark
Sal-Meter-equivalent proxy system
Sal-Meter validation complete
```

The proxy benchmark track prepares comparison structure.

It does not become the molecular-electrochemical core.

---

## 10. Data contribution rule

Before contributing any data-like file, confirm:

- [ ] The file is synthetic, toy, mock, schema-only, or public documentation.
- [ ] The file contains no raw human signal.
- [ ] The file contains no direct identifier.
- [ ] The file contains no real face, voice, video, audio, or location data.
- [ ] The file contains no clinical or health information.
- [ ] The file contains no private session log.
- [ ] The file contains no unpublished internal lab package.
- [ ] The file does not imply diagnosis, treatment, monitoring, or human ranking.
- [ ] The file does not imply Sal-Meter validation.
- [ ] The file does not imply CAIS compliance.
- [ ] The file clearly states whether it is synthetic, toy, mock, or schema-only.

If any item is uncertain, do not contribute the file.

---

## 11. Issue contribution rule

Good issues should be specific.

Good issue examples:

```text
Boundary correction: README sentence may imply Sal-Meter equivalence
Schema request: add field for timestamp_source in event markers
Leakage risk: condition label appears in synthetic filename
Sample data issue: synthetic file does not state synthetic status
Dashboard boundary: mockup label could imply clinical stress score
```

Weak issues:

```text
Make this more scientific
Add AI model
Use real data
Make it clinically useful
Validate Sal-Meter
Make it CAIS-compliant
```

Every issue should include:

1. the file or section involved
2. the problem
3. the risk category
4. proposed corrected language or structure
5. whether the issue involves data, claims, leakage, or metadata

---

## 12. Pull request rule

Good pull requests should be small, bounded, and reviewable.

A pull request should preferably change one layer at a time:

- one schema improvement
- one documentation correction
- one leakage-control improvement
- one synthetic sample-data addition
- one dashboard boundary improvement
- one baseline skeleton improvement

Avoid large mixed pull requests that combine:

- schema changes
- dashboard changes
- claims changes
- sample data changes
- baseline code changes
- public language changes

Boundary-sensitive repositories need small changes.

Small changes can be audited.

---

## 13. Pull request checklist

Before submitting a pull request, confirm:

- [ ] I did not add raw human data.
- [ ] I did not add identifiable participant data.
- [ ] I did not add real face, voice, video, or audio data.
- [ ] I did not add clinical or health records.
- [ ] I did not add private session logs.
- [ ] I did not imply diagnosis, treatment, or clinical monitoring.
- [ ] I did not imply human ranking or surveillance scoring.
- [ ] I did not call the proxy stack Sal-Meter.
- [ ] I did not claim CAIS compliance.
- [ ] I did not claim certification.
- [ ] I did not imply completed Sal-Meter validation.
- [ ] I did not present Human-State Cost as a human score.
- [ ] I preserved DOI authority over GitHub helper language.
- [ ] I used synthetic, toy, mock, or schema-only examples where applicable.
- [ ] I updated related documentation if I changed a schema or sample file.

---

## 14. Commit message guidance

Use short, clear commit messages.

Examples:

```text
Add synthetic event marker example
Refine public data boundary
Fix prohibited claim wording
Add timestamp source field
Clarify Human-State Cost boundary
Add leakage-safe split note
Add dashboard claim boundary
Add closed-loop demo-lite boundary
```

Avoid vague commit messages:

```text
update
fix stuff
new file
more data
better version
```

A commit message should say what boundary or structure changed.

---

## 15. Review priorities

Maintainers should review in this order:

1. raw human data risk
2. private identifier risk
3. clinical / diagnostic / therapeutic claim risk
4. Sal-Meter confusion risk
5. CAIS compliance confusion risk
6. Human-State Cost misuse risk
7. leakage risk
8. metadata completeness
9. reproducibility
10. readability

A contribution that is technically useful but boundary-unsafe should be rejected or rewritten.

---

## 16. Boundary correction process

If a contribution introduces claim drift, correct it using this pattern:

```text
Correction:
The SICS Human-State Proxy Benchmark Track is a research-stage, non-diagnostic, non-therapeutic benchmark support platform.

It is not the Sal-Meter core signal track.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not publish raw human data.

It does not create clinical, diagnostic, therapeutic, surveillance, employment, insurance, legal, educational, eligibility, or human-ranking authority.
```

Boundary correction is not cosmetic.

It is repository governance.

---

## 17. Security and private information rule

Do not commit:

- passwords
- access tokens
- API keys
- private URLs
- participant schedules
- private storage paths
- internal NAS details
- cloud credentials
- private dataset credentials
- private email lists
- personal contact lists
- internal contract terms
- unpublished laboratory deliverables

This repository should not reveal private operations.

Public helper structure is enough.

---

## 18. AI-generated contribution rule

AI tools may be used for drafting, editing, structuring, or code skeleton assistance.

However, AI-generated contributions must be reviewed for:

- claim inflation
- clinical wording
- Sal-Meter confusion
- CAIS compliance confusion
- raw data risk
- hidden identifiers
- leakage risks
- invented citations
- overconfident performance claims

AI-generated text must not be merged without human review.

AI assistance does not create authority.

---

## 19. Fork and derivative contribution rule

Forks and derivatives may adapt public helper materials under the applicable license.

However, forks and derivatives must not claim:

- official SICS approval
- CAIS compliance
- Sal-Meter designation
- certification
- clinical readiness
- diagnostic validity
- therapeutic validity
- commercial-device validation
- authorized-user status
- mark usage rights

A fork may state:

```text
This is a derivative or fork of the SICS Human-State Proxy Benchmark Track public technical helper repository.

This fork does not grant CAIS compliance, Sal-Meter designation, certification, or clinical status.
```

---

## 20. Contributor identity and affiliation

Contributors should not imply that they represent SICS, Salpida Foundation, CAIS, Sal-Meter, or the repository maintainer unless explicitly authorized.

A contribution does not create:

- employment relationship
- contractor status
- institutional authority
- certification authority
- publication approval
- mark usage rights
- access to private data
- access to internal lab records
- access to Sal-Meter core data

Contributions are public technical helper contributions only.

---

## 21. What to do first

Good first contribution paths:

1. Fix unclear wording.
2. Improve metadata schema clarity.
3. Add synthetic examples.
4. Add leakage-risk examples.
5. Add reproducibility checklist items.
6. Add dashboard boundary notes.
7. Add closed-loop demo-lite boundary notes.
8. Add issue templates.
9. Add PR checklist improvements.
10. Add sample-data documentation.

Do not begin by proposing real human data upload.

Do not begin by proposing clinical use.

Do not begin by proposing Sal-Meter validation.

---

## 22. Authority rule

This repository is a public technical helper surface.

DOI-registered SICS / CAIS / Sal-Meter / CCF records govern authority.

If this document conflicts with a higher-level DOI-registered canonical or public boundary record, the higher-level DOI-registered record prevails automatically.

---

## 23. Final contribution principle

Make the repository more useful by making it more bounded.

Make the benchmark stronger by making the evidence cleaner.

Make the project safer by keeping public structure separate from private human data.

Proxy first as benchmark.

Sal-Meter later as core input.

Claims never ahead of evidence.
