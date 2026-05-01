# Proxy Benchmark Track

**A research-stage helper repository for measuring what AI leaves behind in the human state.**

> Most AI benchmarks ask whether AI outputs are correct, safe, helpful, or aligned.  
>  
> The Proxy Benchmark Track asks a different question:  
>  
> **What did the AI output leave behind in the human state?**  
>  
> And in a dyadic session:  
>  
> **Did the AI help both people move toward recovery, or did it improve one side while burdening, silencing, or exposing the other?**

---

## One-line thesis

The Proxy Benchmark Track is designed to build a synchronized, consent-based, non-clinical benchmark layer for evaluating how AI outputs affect individual human-state change and dyadic recovery.

It does not only evaluate the AI answer.

It evaluates the trace left after the answer.

---

## What makes this repository different

Most AI evaluation looks at the output.

This repository is built around the consequence.

It asks:

```text
AI Output → Human-State Delta → Dyadic Recovery
```

This means:

- not only whether the AI answer was fluent;
- not only whether the AI answer sounded safe;
- not only whether the AI answer was preferred by a user;
- but whether the AI output left the human being and the dyad in a measurably better, worse, unchanged, mixed, or uncertain state.

The central question is:

```text
What remains in the human state after AI acts?
```

For two-person interaction, the sharper question is:

```text
Did both sides move toward recovery, or did one side become silent, exposed, burdened, coerced, or erased?
```

This is the distinct lane.

This repository is not another chatbot project.

It is a public helper surface for a future human-state-aware AI mediation benchmark.

---

## Current status

**research-stage · non-clinical · non-diagnostic · non-therapeutic · non-surveillance · non-counseling · non-coercive · raw-data-non-public · synthetic-public-data-first · public helper only · pre-validation · pre-device · pre-certification · pre-compliance · benchmark support only**

This repository is:

- not the Sal-Meter core signal track;
- not a Proxy Sal-Meter;
- not a CAIS-compliant device implementation;
- not a validated consciousness measurement system;
- not a clinical, diagnostic, therapeutic, psychiatric, medical, employment, insurance, legal, educational, eligibility, counseling, mediation-service, or surveillance system;
- not a certification, conformance, or mark-usage surface;
- not a closed-loop intervention system;
- not a production monitoring system;
- not a place to publish raw human data.

Public landing page:

```text
https://salpida.foundation/topics/human-state-aware-ai-interaction/
```

---

## P3 helper layer completion statement

The P3 Human-State-Aware AI Mediation helper layer now defines the public helper structure for:

```text
Layer
→ Packet
→ Session Protocol
→ Dyadic Session Flow
→ Baseline
→ Recovery Gate
→ Termination Gate
→ Consent and Data-Sharing Boundary
→ Session Closure / Audit Log
```

Completed P3 helper documents:

```text
docs/human-state-mediation-layer.md
docs/human-state-packet-schema.md
docs/dyadic-recovery-baseline-suite.md
docs/recovery-gate-definition.md
docs/termination-gate-definition.md
docs/human-state-session-protocol.md
docs/dyadic-mediation-session-flow.md
docs/consent-and-data-sharing-boundary.md
```

Completed P3 boundary and release-preparation documents:

```text
docs/p3-final-boundary-audit.md
docs/v0.1.0-public-helper-release-package.md
docs/v0.1.0-github-pre-release-notes-and-publication-gate.md
```

Completed P3 helper schemas:

```text
schemas/human_state_packet.schema.json
schemas/dyadic_session_event.schema.json
schemas/benchmark_session.schema.json
schemas/README.md
```

These helper documents and schemas do not validate a benchmark.

They do not validate Sal-Meter.

They do not grant CAIS compliance.

They do not create a clinical, diagnostic, therapeutic, counseling, legal mediation, surveillance, human-ranking, or production closed-loop system.

They define the public helper structure required for auditable future work.

---

## Canonical / DOI relationship

This repository is a **public technical helper surface**.

It accompanies DOI-registered public records.

It does not replace them.

GitHub helps builders move.

DOI records govern authority.

### Core Proxy Benchmark Track records

#### SICS Human-State Proxy Benchmark Track — Public Boundary and Program Charter v0.1

Defines public boundary, naming rules, prohibited claims, data-publication limits, roadmap logic, GitHub helper status, and Go / Hold / No-Go structure.

```text
Version DOI:
https://doi.org/10.5281/zenodo.19837423

Concept DOI / All Versions DOI:
https://doi.org/10.5281/zenodo.19837422
```

#### SICS Human-State Proxy Benchmark Track — Scientific Rationale and Research Value v0.1

Explains Human-State Cost, AI performance versus human-state impact, measurement-layer simplification, and future Sal-Meter A/B comparison logic.

```text
Version DOI:
https://doi.org/10.5281/zenodo.19837971

Concept DOI / All Versions DOI:
https://doi.org/10.5281/zenodo.19837970
```

### Human-State-Aware AI Mediation document set

#### Human-State Mediation Boundary Standard v0.1

Fixes the outer boundary: consent-based, non-clinical, non-surveillance, raw-data-non-public.

```text
Version DOI:
https://doi.org/10.5281/zenodo.19904289

Concept DOI / All Versions DOI:
https://doi.org/10.5281/zenodo.19904288
```

#### Human-State Packet Minimal Data-Sharing Standard v0.1

Fixes the minimum packet object: summary-only sharing, permission, expiry, confidence, data quality, and raw-data exclusion.

```text
Version DOI:
https://doi.org/10.5281/zenodo.19905541

Concept DOI / All Versions DOI:
https://doi.org/10.5281/zenodo.19905540
```

#### Dyadic Human-State Mediation Benchmark Charter v0.1

Fixes the benchmark objective:

```text
AI Output → Human-State Delta → Dyadic Recovery
```

```text
Version DOI:
https://doi.org/10.5281/zenodo.19906725

Concept DOI / All Versions DOI:
https://doi.org/10.5281/zenodo.19906724
```

#### Human-State Session Protocol v0.1 — Structural Declaration

Fixes the session structure:

```text
Session Creation → Consent Confirmation → Packet Availability Check → Baseline State Summary → AI Output → Post-Output State Summary → Human-State Delta → Recovery Gate → Termination Gate → Session Closure → Audit Log
```

```text
Version DOI:
https://doi.org/10.5281/zenodo.19908379

Concept DOI / All Versions DOI:
https://doi.org/10.5281/zenodo.19908378
```

If this README conflicts with a DOI-registered SICS / CAIS / Sal-Meter / CCF boundary or governance record, the stricter DOI-registered record controls.

---

## The core message

AI should not be evaluated only by what it produces.

It should also be evaluated by what it leaves in the human being.

A system may improve accuracy, speed, productivity, compliance, or user satisfaction while increasing human-state burden.

This repository exists to make that tradeoff visible.

---

## The benchmark chain

```text
AI Output
    ↓
Human-State Delta
    ↓
Dyadic Recovery
    ↓
Recovery Gate / Termination Gate
```

### AI Output

The system records what the AI generated.

Examples:

- generic AI output;
- state-aware AI output;
- private cue;
- shared mediation output;
- pause recommendation;
- clarification request;
- scope narrowing;
- recovery check;
- termination recommendation.

### Human-State Delta

The system observes what changed after the AI output.

Examples:

- toward recovery;
- away from recovery;
- unchanged;
- mixed;
- uncertain;
- insufficient data;
- invalid.

Human-State Delta is not diagnosis.

It is not therapy.

It is not emotion reading.

It is not a human score.

It is a bounded benchmark observation.

### Dyadic Recovery

The benchmark asks whether both sides of the dyad moved toward a session-defined recovery condition.

Recovery is not agreement.

Recovery is not silence.

Recovery is not obedience.

Recovery is not therapy.

Recovery is a bounded session-state condition where continued AI mediation can reduce, pause, or stop.

### Recovery Gate

Recovery Gate asks whether the session-defined recovery condition has been reached.

It prevents false success.

It does not crown AI for speaking well.

It does not treat silence, obedience, agreement, synchrony, or one-sided improvement as automatic recovery.

### Termination Gate

Termination Gate asks whether the session must pause, narrow, or stop.

It prevents endless mediation.

It protects consent, permission, expiry, data quality, session scope, private state, raw human data, and auditability.

A closed session must stay closed.

---

## What this track is

The SICS Human-State Proxy Benchmark Track is a parallel research-stage benchmark support path for **Human-State-Aware AI Interaction**.

It uses existing proxy signals to prepare synchronized benchmark infrastructure before future Sal-Meter I/G-channel inputs become available.

The purpose is to prepare:

- synchronized multimodal capture;
- session metadata;
- event markers;
- state-window labeling;
- leakage-safe evaluation;
- holdout design;
- baseline models;
- Human-State Packet helper structures;
- Human-State Session Protocol helper structures;
- dyadic mediation session-flow helper structures;
- consent and data-sharing boundary structures;
- Dyadic Recovery Baseline Suite;
- Recovery Gate;
- Termination Gate;
- safe dashboard mockup boundaries;
- local closed-loop demo-lite boundary scaffolding;
- replication and release-readiness checklists;
- contributor issue / PR boundary gates;
- replayable validation skeletons;
- future A/B comparison against Sal-Meter core inputs.

The proxy track supports the core track.

It does not replace it.

---

## What this track is not

This repository does not define Sal-Meter.

It does not redefine CAIS.

It does not grant:

- CAIS compliance;
- Sal-Meter designation;
- certification status;
- conformance recognition;
- mark entitlement;
- authorized-user status;
- clinical status;
- diagnostic status;
- therapeutic status;
- medical-device status;
- counseling-service status;
- legal mediation status;
- validated commercial-device status;
- closed-loop deployment status;
- production monitoring status;
- human-ranking authority.

ECG, HRV, EDA, PPG, EEG, eye tracking, webcam markers, interaction timing, behavioral logs, task events, AI feedback logs, dashboard review states, issue templates, PR templates, and closed-loop demo-lite placeholders do not become Sal-Meter by being combined.

They remain **proxy benchmark signals and helper structures**.

---

## Core track vs proxy benchmark track

The two tracks are related.

They are not identical.

They must not be publicly merged.

### Sal-Meter Core Track

The Sal-Meter Core Track asks whether a new molecular–electrochemical signal interface can produce stable, repeatable, auditable signal behavior under the CAIS / Sal-Meter kernel program.

Current core execution order:

```text
External Layer-0 iodine redox / thiol feasibility
→ SICS Internal Phase 0 — G-only
→ Phase 1 — I-only
→ Phase 2a — Twin Mini-Cell
→ Phase 2b — G+I human pilot
→ LOCK 1 / LOCK 2
→ Future SDK / broader opening
```

Core technical route:

```text
https://github.com/salpida-foundation/sal-meter-kernel-program
```

### Proxy Benchmark Track

The Proxy Benchmark Track prepares the comparison and interaction layer.

It builds synchronized multimodal baselines, leakage-safe evaluation rules, dataset structure, baseline modeling, dashboard boundary rules, closed-loop demo-lite scaffolding, replication checklists, contributor issue / PR boundary gates, and future comparison logic that can later serve as a comparison lane for Sal-Meter inputs.

The proxy track supports the core track.

It does not replace it.

---

## Human-State-Aware AI Mediation helper architecture

The current P3 helper layer defines the public helper spine for future Human-State-Aware AI Mediation work.

The architecture is:

```text
Human-State Mediation Layer
→ Human-State Packet
→ Human-State Session Protocol
→ Dyadic Mediation Session Flow
→ Dyadic Recovery Baseline Suite
→ Recovery Gate
→ Termination Gate
→ Consent and Data-Sharing Boundary
→ Session Closure / Audit Log
```

Completed helper documents:

```text
docs/human-state-mediation-layer.md
docs/human-state-packet-schema.md
docs/dyadic-recovery-baseline-suite.md
docs/recovery-gate-definition.md
docs/termination-gate-definition.md
docs/human-state-session-protocol.md
docs/dyadic-mediation-session-flow.md
docs/consent-and-data-sharing-boundary.md
```

Completed helper schemas:

```text
schemas/human_state_packet.schema.json
schemas/dyadic_session_event.schema.json
schemas/benchmark_session.schema.json
```

Completed P3 boundary and release-preparation documents:

```text
docs/p3-final-boundary-audit.md
docs/v0.1.0-public-helper-release-package.md
docs/v0.1.0-github-pre-release-notes-and-publication-gate.md
```

Completed P3 documents and schemas are helper structures.

No P3 helper file validates a benchmark, validates Sal-Meter, grants CAIS compliance, or authorizes clinical, therapeutic, counseling, legal mediation, surveillance, human-ranking, or production deployment claims.

---

## Long-term milestone

```text
Dyadic Human-State Mediation Benchmark
```

The long-term milestone is not merely to sense individual state.

The long-term milestone is to define how consented human-state summaries can be exchanged between personal agents during a bounded dyadic session so that AI systems can adjust private cues, shared mediation outputs, and recovery termination timing without exposing raw human data.

In plain language:

```text
The goal is not to build AI that speaks better.

The goal is to build the benchmark layer needed to know whether AI leaves people and relationships in a better state.
```

---

## Baseline philosophy

This repository does not treat AI output quality as sufficient evidence.

A polished AI answer can still leave harm behind.

A polite AI answer can still silence one side.

A long AI answer can still overstay.

A helpful AI answer for one participant can still burden the other.

The benchmark must therefore compare human-state-aware mediation against simpler baselines.

### Dyadic Recovery Baseline Suite

The baseline ladder is:

| Level | Baseline | Question |
|---|---|---|
| B0 | Dummy / Chance Baseline | Can the model beat guessing or majority-class prediction? |
| B1 | Individual State Baseline | Can one person’s state alone explain the outcome? |
| B2 | Dyadic Relationship Baseline | Does the relation between both participants add explanatory value? |
| B3 | No-Intervention Baseline | Would the dyad recover naturally without AI intervention? |
| B4 | Generic AI Baseline | Is state-aware AI better than ordinary supportive AI output? |
| B5 | Rule-Based Mediation Baseline | Is the system better than fixed mediation scripts? |
| B6 | Human-State-Aware AI Mediation Model | Does packet-informed AI improve dyadic recovery under bounded conditions? |
| B7 | Recovery / Termination Gate Baseline | Can the system identify when to reduce, pause, or stop mediation? |

Primary outcome:

```text
Dyadic Recovery Delta
```

Secondary outcomes may include:

- individual recovery direction;
- dyadic tension reduction;
- interruption reduction;
- turn-taking balance;
- mutual restatement success;
- recovery asymmetry;
- post-intervention stability;
- termination accuracy;
- mediation overstay rate;
- consent-boundary compliance;
- leakage-safe benchmark score;
- human non-judgment compliance.

---

## Failure-sensitive principles

This benchmark must be sensitive to false recovery.

A session is not successful merely because the AI sounded good.

A session is not successful merely because one participant became quiet.

A session is not successful merely because one participant reported relief.

A session is not successful merely because both participants showed synchrony.

A session is not successful if the AI continues after it should stop.

### Failure conditions include

- one participant improves while the other deteriorates;
- silence is misclassified as recovery;
- synchrony is treated as automatically positive;
- AI output quality is treated as sufficient evidence;
- generic supportive language is mistaken for human-state improvement;
- private state becomes exposed in shared output;
- packet permission is exceeded;
- expired packet is used;
- human score is generated;
- relationship verdict is generated;
- AI fails to stop when termination is required;
- leakage-safe holdout is not satisfied;
- model performance fails to exceed simpler baselines.

The dyad is the unit of interpretation.

One-sided improvement is not dyadic recovery.

---

## Human-State Packet principle

The public benchmark must not exchange raw human data.

It should exchange only bounded summaries.

A Human-State Packet is:

```text
minimal
consent-bound
permission-bound
expiry-bound
confidence-aware
data-quality-aware
session-scoped
sharing-scoped
raw-data-excluding
```

The packet is not the person.

The packet is not the body.

The packet is not the raw signal.

The packet is not diagnosis.

The packet is not a human score.

The packet is not a relationship judgment.

The packet is a minimal state-summary object for bounded interaction adjustment.

---

## Human-State Session principle

A session does not begin silently.

A session begins with consent.

A session runs only within packet permission.

A session closes through a recovery gate or termination gate.

A session that cannot close is not mediation.

It is surveillance drift.

A valid session should follow this structure:

```text
Session Creation
→ Consent Confirmation
→ Packet Availability Check
→ Baseline State Summary
→ AI Output
→ Post-Output State Summary
→ Human-State Delta
→ Recovery Gate
→ Termination Gate
→ Session Closure
→ Audit Log
```

---

## Current implementation status

This repository is currently in a public helper implementation stage for the SICS Human-State Proxy Benchmark Track.

It provides schema, synthetic/sample data, validation scaffolding, dashboard mockup boundaries, protocol helper rules, closed-loop demo-lite boundary scaffolding, replication guide checklists, contributor issue/PR templates, Human-State-Aware AI Mediation helper documents, P3 helper schemas, P3 boundary audit documents, and repository hygiene workflow scaffolding for structure demonstration only.

It does not provide benchmark evidence.

It does not provide raw human data.

It does not provide Sal-Meter input.

It does not grant CAIS compliance.

It does not validate Sal-Meter.

| Work item | Status | Notes |
|---|---|---|
| Governance boundary files | Present | Public/private data boundary and prohibited-claim discipline are represented in the repository |
| Schema completion | Done | `schemas/` contains public helper schemas for metadata, event markers, streams, labels, QC, features, splits, Human-State Packet, Dyadic Session Event, and Benchmark Session Container helper structures |
| Human-State Packet JSON helper schema | Done | `schemas/human_state_packet.schema.json` defines a public helper schema for synthetic Human-State Packets |
| Dyadic Session Event JSON helper schema | Done | `schemas/dyadic_session_event.schema.json` validates one public-safe synthetic/sample dyadic session boundary event |
| Benchmark Session JSON helper schema | Done | `schemas/benchmark_session.schema.json` validates one public-safe synthetic/sample benchmark session container |
| Synthetic sample package | Present | `sample-data/synthetic-session-001/` contains a public synthetic/sample structure package |
| Synthetic session README | Done | The synthetic package includes a local README explaining file roles and boundaries |
| Sample package validator | Present | `evaluation-baseline/validate_sample_package.py` provides helper-structure validation |
| Evaluation baseline README | Done | `evaluation-baseline/README.md` explains validator usage, PASS / FAIL interpretation, dependency installation, and validation boundaries |
| Protocol helper boundary pack | Done | `protocol-helper/` defines label, timestamp, metadata, Human-State Cost, and future Sal-Meter A/B comparison boundaries |
| Dashboard mockup boundary pack | Done | `dashboard-mockup/` defines dashboard claim, field, and wireframe boundaries |
| Closed-loop demo-lite boundary pack | Done | `closed-loop-demo-lite/` defines feedback-loop boundaries, event-log schema, and local placeholder code |
| Replication guide pack | Done | `replication-guide/` defines reproducibility, metadata completeness, audit trail, and public release-readiness checklists |
| Issue / PR template pack | Done | `.github/ISSUE_TEMPLATE/` and `.github/pull_request_template.md` define contributor boundary gates |
| P3 Human-State Mediation Layer | Done | `docs/human-state-mediation-layer.md` defines the interaction-adjustment helper layer |
| P3 Human-State Packet helper document | Done | `docs/human-state-packet-schema.md` defines the human-readable packet boundary |
| P3 Dyadic Recovery Baseline Suite | Done | `docs/dyadic-recovery-baseline-suite.md` defines the B0-B7 baseline ladder |
| P3 Recovery Gate | Done | `docs/recovery-gate-definition.md` defines false recovery prevention and recovery decision boundaries |
| P3 Termination Gate | Done | `docs/termination-gate-definition.md` defines stop, pause, closure, expiry, permission, and overstay boundaries |
| P3 Human-State Session Protocol | Done | `docs/human-state-session-protocol.md` defines a bounded, consent-based, permission-bound, audit-ready session lifecycle |
| P3 Dyadic Mediation Session Flow | Done | `docs/dyadic-mediation-session-flow.md` defines dyadic flow and the rule that one-sided improvement is not dyadic recovery |
| P3 Consent and Data-Sharing Boundary | Done | `docs/consent-and-data-sharing-boundary.md` defines consent, permission, sharing, expiry, withdrawal, public/private data boundary, raw-data-non-public rule, and audit boundary |
| P3 Final Boundary Audit | Done | `docs/p3-final-boundary-audit.md` records the final P3 boundary audit before release packaging |
| v0.1.0 public helper release package | Prepared | `docs/v0.1.0-public-helper-release-package.md` prepares a bounded public helper package for later publication review |
| v0.1.0 GitHub pre-release notes and publication gate | Prepared | `docs/v0.1.0-github-pre-release-notes-and-publication-gate.md` preserves release notes and gate language for later publication action |
| GitHub Actions validator workflow | Present / Blocked | `.github/workflows/validate-synthetic-sample.yml` exists, but execution is currently blocked by GitHub account-level Actions restriction |
| Citation metadata | Present | `CITATION.cff` points citation toward DOI-registered public boundary records |
| Raw human data | Not present | Public repository examples must remain synthetic, mock, placeholder, or sample-structure-only |
| Sal-Meter input | Not present | This repository is not Sal-Meter and does not contain Sal-Meter signal data |
| CAIS compliance claim | Not present | This repository does not grant CAIS compliance |
| Benchmark validation | Not present | No model, dataset, dashboard, sensor stack, feedback loop, template, PR, or benchmark result is validated by this repository |
| Release status | Prepared / Pending P3-17 gate | `v0.1.0` public helper pre-release package is prepared; publication requires P3-17 authorization and must remain a pre-release helper package only |

---

## Current P1 milestone state

| Milestone | Status | Notes |
|---|---|---|
| P1-1 Schema completion | Done | Schema folder contains helper schemas and `schemas/README.md` |
| P1-2 Synthetic sample package validator | Done | Validator file exists under `evaluation-baseline/validate_sample_package.py` |
| P1-3 Evaluation baseline README and validator usability | Done | Evaluation baseline README explains local usage, PASS / FAIL meaning, dependency installation, and validator boundaries |
| P1-4 GitHub Actions validator workflow | Open / Blocked | Workflow exists but cannot currently run because GitHub Actions is disabled at the user-account level |
| P1-5 v0.1.0 release readiness package | Prepared / Gate pending | `v0.1.0` public helper pre-release package is prepared; publication requires P3-17 authorization and does not create benchmark validation, Sal-Meter validation, or CAIS compliance |

---

## Current P2 milestone state

| Milestone | Status | Notes |
|---|---|---|
| P2-1 Protocol helper boundary pack | Done | `protocol-helper/` contains bounded helper rules for labels, timestamps, metadata completeness, Human-State Cost, and future Sal-Meter A/B comparison |
| P2-2 Dashboard mockup boundary pack | Done | `dashboard-mockup/` contains README, claim boundary, sample dashboard fields, and mockup wireframe |
| P2-3 Closed-loop demo-lite boundary pack | Done | `closed-loop-demo-lite/` contains README, feedback-loop boundary, feedback event-log schema, and local placeholder code |
| P2-4 Replication guide pack | Done | `replication-guide/` contains README, reproducibility package checklist, metadata completeness checklist, audit trail checklist, and public release checklist |
| P2-5 Issue / PR template pack | Done | `.github/ISSUE_TEMPLATE/` contains boundary correction, schema request, sample-data issue, and leakage-risk report templates; `.github/pull_request_template.md` defines PR boundary review |

---

## Current P3 milestone state

P3 introduces the Human-State-Aware AI Mediation helper layer.

P3 helper documents and schemas have been completed through P3-11.

P3-12 has aligned this root README with the completed helper documents, helper schemas, and schema-folder README.

P3-13 records the final P3 boundary audit.

P3-14 prepares the `v0.1.0` public helper release package.

P3-15 preserves the exact GitHub pre-release notes and publication gate.

P3-16 tested the GitHub draft path and corrected the process away from unreliable draft dependence.

P3-17 is the final authorization gate for public pre-release publication.

This is still a public helper layer.

It is not benchmark validation.

It is not Sal-Meter validation.

It is not CAIS compliance.

| Milestone | Status | Notes |
|---|---|---|
| P3-1 Human-State Mediation Layer | Done | `docs/human-state-mediation-layer.md` defines the public helper concept connecting AI Output, Human-State Delta, Dyadic Recovery, Human-State Packet, Recovery Gate, and Termination Gate |
| P3-2 Human-State Packet helper document | Done | `docs/human-state-packet-schema.md` defines the packet as a consent-bound, permission-bound, expiry-bound, confidence-aware, data-quality-aware, session-scoped, sharing-scoped, raw-data-excluding state-summary object |
| P3-2 Human-State Packet JSON helper schema | Done | `schemas/human_state_packet.schema.json` defines the machine-readable helper structure for public synthetic/sample packet examples |
| P3-3 Dyadic Recovery Baseline Suite B0-B7 | Done | `docs/dyadic-recovery-baseline-suite.md` defines baseline comparison logic from chance through recovery/termination gate baselines |
| P3-4 Recovery Gate Definition | Done | `docs/recovery-gate-definition.md` defines the gate for preventing false recovery and determining when mediation can reduce, pause, or stop |
| P3-4 Termination Gate Definition | Done | `docs/termination-gate-definition.md` defines the gate for consent withdrawal, permission expiry, data quality failure, high uncertainty, overstay prevention, session closure, and auditability |
| P3-6 Human-State Session Protocol | Done | `docs/human-state-session-protocol.md` defines a bounded, consent-based, permission-bound, audit-ready session lifecycle |
| P3-7 Dyadic Mediation Session Flow | Done | `docs/dyadic-mediation-session-flow.md` defines the dyadic session flow and preserves the rule that one-sided improvement is not dyadic recovery |
| P3-8 Consent and Data-Sharing Boundary | Done | `docs/consent-and-data-sharing-boundary.md` defines consent, permission, sharing, expiry, withdrawal, public/private data boundary, raw-data-non-public rule, and audit boundary |
| P3-9 Dyadic Session Event JSON helper schema | Done | `schemas/dyadic_session_event.schema.json` validates one public-safe synthetic/sample dyadic session boundary event |
| P3-10 Benchmark Session JSON helper schema | Done | `schemas/benchmark_session.schema.json` validates one public-safe synthetic/sample benchmark session container |
| P3-11 Schemas README alignment | Done | `schemas/README.md` now distinguishes packet object, dyadic session event object, and benchmark session container |
| P3-12 Root README alignment | Done | Root README has been aligned with completed P3 helper documents and schemas |
| P3-13 Final P3 boundary audit | Done | `docs/p3-final-boundary-audit.md` records the final P3 boundary audit before any release packaging |
| P3-14 v0.1.0 public helper release package | Done | `docs/v0.1.0-public-helper-release-package.md` prepares the bounded release package without publishing a GitHub Release |
| P3-15 GitHub pre-release notes and publication gate | Done | `docs/v0.1.0-github-pre-release-notes-and-publication-gate.md` preserves release notes and publication gate language |
| P3-16 GitHub pre-release draft correction | Done | GitHub draft dependence was treated as unreliable; publication must proceed only through a separate P3-17 authorization gate |
| P3-17 Public pre-release publication authorization | Gate pending | P3-17 must authorize any `v0.1.0` public pre-release publication action |

### Completed P3 helper documents

```text
docs/
  human-state-mediation-layer.md
  human-state-packet-schema.md
  dyadic-recovery-baseline-suite.md
  recovery-gate-definition.md
  termination-gate-definition.md
  human-state-session-protocol.md
  dyadic-mediation-session-flow.md
  consent-and-data-sharing-boundary.md
```

### Completed P3 boundary and release-preparation documents

```text
docs/
  p3-final-boundary-audit.md
  v0.1.0-public-helper-release-package.md
  v0.1.0-github-pre-release-notes-and-publication-gate.md
```

### Completed P3 helper schemas

```text
schemas/
  human_state_packet.schema.json
  dyadic_session_event.schema.json
  benchmark_session.schema.json
  README.md
```

### P3 helper architecture

```text
AI Output
→ Human-State Packet
→ Human-State Session Protocol
→ Dyadic Mediation Session Flow
→ Human-State Delta A/B
→ Dyadic Delta
→ Recovery Gate
→ Termination Gate
→ Consent and Data-Sharing Boundary
→ Session Closure
→ Audit Log
```

The Consent and Data-Sharing Boundary controls what may cross the arrows.

### Object distinction

#### Human-State Packet

A Human-State Packet is a minimal consent-bound, permission-bound, expiry-bound, confidence-aware, data-quality-aware, session-scoped, sharing-scoped, raw-data-excluding state-summary object.

It is not the body.

It is not diagnosis.

It is not Sal-Meter.

It is not CAIS compliance.

#### Dyadic Session Event

A Dyadic Session Event is a public-safe synthetic/sample event object that records boundary events such as consent, permission, packet status, sharing scope, private cue status, shared output status, Human-State Delta A/B, Dyadic Delta, gate decisions, closure, and audit status.

It records the boundary.

It does not record the body.

#### Benchmark Session Container

A Benchmark Session Container is a public-safe synthetic/sample container that connects event references, baseline suite status, gate summaries, leakage review, holdout strategy, audit status, public release status, authority status, and final boundary status.

It records the benchmark container.

It does not validate the benchmark.

### P3 public boundary

P3 remains:

```text
research-stage
non-clinical
non-diagnostic
non-therapeutic
non-surveillance
non-counseling
raw-data-non-public
synthetic-public-data-first
public helper only
not Sal-Meter
not CAIS compliance
not validated benchmark
not validated mediation
not production closed-loop intervention
```

P3 does not authorize:

```text
validated product
validated benchmark
validated mediation
certified benchmark
CAIS compliance
Sal-Meter validation
Sal-Meter-compatible node exists
clinical readiness
diagnostic readiness
therapeutic readiness
counseling service
legal mediation service
surveillance readiness
production deployment
human ranking
relationship verdict
official consciousness signal
ground-truth signal
```

### Schema layer summary

The schema layer now includes:

```text
Human-State Packet helper schema
Dyadic Session Event helper schema
Benchmark Session helper schema
```

Schemas validate public helper structure.

They do not validate the human body.

They do not validate Sal-Meter.

They do not grant CAIS compliance.

They do not crown a benchmark as validated.

### Release boundary

A production release is not ready.

A validated benchmark release is not ready.

A Sal-Meter release is not ready.

A CAIS-compliant release is not ready.

A `v0.1.0` public helper pre-release package has been prepared.

The `v0.1.0` public helper pre-release may proceed only through the P3-17 publication authorization gate.

If published, it must remain:

```text
research-stage
public helper only
synthetic/sample-data-first
raw-data-non-public
non-clinical
non-diagnostic
non-therapeutic
non-surveillance
non-counseling
pre-validation
pre-device
pre-certification
pre-compliance
not Sal-Meter
not CAIS compliance
not validated benchmark
not validated mediation
not production closed-loop intervention
```

GitHub Actions validation remains a known workflow blocker.

That blocker does not create validation.

That blocker does not create CAIS compliance.

That blocker does not create Sal-Meter validation.

That blocker does not authorize production use.

Raw human data must not enter the public repository.

A closed session must stay closed.

---

## Repository structure

```text
proxy-benchmark-track/
  README.md
  LICENSE
  CITATION.cff

  .github/
    ISSUE_TEMPLATE/
      boundary_correction.md
      schema_request.md
      sample_data_issue.md
      leakage_risk_report.md

    workflows/
      validate-synthetic-sample.yml

    pull_request_template.md

  docs/
    current-operating-model.md
    data-boundary.md
    leakage-control-checklist.md
    metadata-schema-v0.1.md
    public-language-boundary.md
    reproducibility-checklist.md

    # P3 completed helper documents
    human-state-mediation-layer.md
    human-state-packet-schema.md
    dyadic-recovery-baseline-suite.md
    recovery-gate-definition.md
    termination-gate-definition.md
    human-state-session-protocol.md
    dyadic-mediation-session-flow.md
    consent-and-data-sharing-boundary.md

    # P3 completed boundary and release-preparation documents
    p3-final-boundary-audit.md
    v0.1.0-public-helper-release-package.md
    v0.1.0-github-pre-release-notes-and-publication-gate.md

  governance/
    README.md
    claims_boundary.md
    public_private_data_boundary.md

  schemas/
    README.md
    session-metadata.schema.json
    streams-manifest.schema.json
    event-markers.schema.json
    labels.schema.json
    qc-report.schema.json
    features-baseline.schema.json
    splits.schema.json

    # P3 completed helper schemas
    human_state_packet.schema.json
    dyadic_session_event.schema.json
    benchmark_session.schema.json

  sample-data/
    README.md

    synthetic-session-001/
      README.md
      session_metadata.json
      streams_manifest.csv
      events.csv
      labels.csv
      qc_report.json
      features_baseline.csv
      splits.json
      operator_log.md

  evaluation-baseline/
    README.md
    requirements.txt
    validate_sample_package.py
    baseline_pipeline_skeleton.py
    leakage_safe_split_example.py

  protocol-helper/
    README.md
    session_label_rule.md
    timestamp_sync_rule.md
    metadata_completeness_rule.md
    human_state_cost_construct_note.md
    future_sal_meter_ab_comparison_rule.md

  dashboard-mockup/
    README.md
    dashboard_claim_boundary.md
    sample_dashboard_fields.json
    mockup_wireframe.md

  closed-loop-demo-lite/
    README.md
    feedback_loop_boundary.md
    feedback_event_log_schema.json
    local_feedback_demo_placeholder.py

  replication-guide/
    README.md
    reproducibility_package_checklist.md
    metadata_completeness_checklist.md
    audit_trail_checklist.md
    public_release_checklist.md
```

This repository structure documents helper surfaces.

It does not create canonical authority.

It does not create benchmark validation.

It does not create Sal-Meter validation.

It does not create CAIS compliance.

If the live repository structure and this README diverge, the live repository should be corrected through an auditable issue / PR / commit path.

---

## Public helper surfaces

This repository contains public helper surfaces.

A public helper surface may:

- describe scope;
- explain boundaries;
- provide synthetic/sample data structures;
- define helper schemas;
- demonstrate validator logic;
- demonstrate leakage-aware split thinking;
- show dashboard mockup boundaries;
- show closed-loop demo-lite boundaries;
- show replication and release-readiness checklists;
- provide issue and pull request boundary templates;
- prepare future contributor orientation;
- define Human-State-Aware AI Mediation helper structure.

A public helper surface must not:

- create canonical authority;
- replace DOI-registered records;
- publish raw human data;
- publish identifiable data;
- publish clinical data;
- imply Sal-Meter validation;
- imply CAIS compliance;
- imply benchmark validation;
- imply closed-loop intervention readiness;
- imply contributor submissions create authority;
- imply diagnostic, therapeutic, clinical, surveillance, certification, counseling, mediation-service, or human-ranking authority.

---

## Data boundary

Public examples in this repository must remain:

- synthetic;
- sample;
- mock;
- placeholder;
- toy;
- sample-structure-only;
- non-identifying.

This repository must not contain:

- raw human biosignals;
- raw human video;
- raw human audio;
- face data;
- voice data;
- identifiable participant metadata;
- private session logs;
- real dyadic conflict records;
- clinical data;
- health records;
- consent files containing personal information;
- internal lab packages;
- Sal-Meter raw input;
- CAIS compliance dossiers;
- production feedback logs.

Raw human data belongs outside this public repository.

Private data requires separate governance, consent, access control, and audit structure.

---

## Human-State Packet boundary

Allowed public packet examples:

```text
synthetic packet
sample packet
simulated packet
mock packet
schema example
dashboard example
public documentation example
```

Prohibited public packet content:

```text
raw ECG
raw EEG
raw EDA
raw PPG
raw voice
raw face
raw gaze
raw video
raw transcript
raw CAIS trace
raw Sal-Meter trace
legal name
phone number
email address
diagnosis
therapy label
human score
relationship verdict
political profile
religious profile
ideological profile
```

A packet may support interaction adjustment.

It must not expose the body.

---

## Session protocol boundary

A valid Human-State Session must have:

- session creation;
- consent confirmation;
- role confirmation;
- scope confirmation;
- packet availability check;
- packet permission check;
- packet expiry check;
- baseline state summary;
- AI output record;
- post-output state summary;
- Human-State Delta;
- recovery gate;
- termination gate;
- session closure;
- audit log.

A session fails if:

- it starts without consent;
- it uses a packet without permission;
- it uses an expired packet;
- private cue becomes shared output without permission;
- raw data enters shared channel;
- AI output judges a participant;
- diagnostic or therapeutic claims occur;
- silence is misread as recovery;
- one-sided improvement is counted as recovery;
- recovery is reached but AI continues unnecessarily;
- termination is required but ignored;
- audit log is missing.

A session that cannot close is not a Human-State Session.

It is surveillance drift.

---

## Recovery Gate boundary

Recovery Gate is a bounded, auditable session-level decision point that determines whether a Human-State-Aware AI Mediation session has reached a condition where AI mediation can reduce, pause, or terminate.

Recovery Gate does not prove healing.

Recovery Gate does not prove agreement.

Recovery Gate does not prove therapy.

Recovery Gate prevents false success.

Recovery Gate must not treat the following as automatic recovery:

- AI fluency;
- politeness;
- silence;
- obedience;
- agreement;
- user satisfaction;
- one-sided improvement;
- synchrony.

Recovery Gate may output:

```text
recovery_reached
recovery_not_reached
recovery_uncertain
false_positive_risk
false_negative_risk
pause_recommended
reduce_mediation_recommended
terminate_recommended
human_review_required
invalid_due_to_data_quality
invalid_due_to_permission
invalid_due_to_scope
```

Recovery Gate must preserve consent, permission, expiry, data quality, confidence, sharing scope, non-judgment, and raw-data-non-public boundaries.

---

## Termination Gate boundary

Termination Gate is a bounded, auditable session-level decision point that determines when a Human-State-Aware AI Mediation session must pause, narrow, or stop.

Termination is not failure.

Termination is a boundary function.

A system that cannot stop is not mature.

Termination Gate may be triggered by:

- consent withdrawal;
- packet permission expiry;
- data quality failure;
- session scope violation;
- high uncertainty;
- participant stop request;
- recovery reached;
- raw data exposure risk;
- private state exposure risk;
- non-judgment failure;
- prohibited output;
- mediation overstay;
- missing audit trail;
- Sal-Meter / CAIS overclaim risk.

Termination Gate may output:

```text
continue_allowed
pause_required
narrow_scope_required
private_cue_only
shared_output_blocked
terminate_required
terminate_recommended
human_review_required
packet_channel_closed
session_closed
audit_required
invalid_session
```

A closed session must stay closed.

---

## Consent and data-sharing boundary

Consent is not permanent.

Permission is not unlimited.

Sharing is not automatic.

A Human-State Packet is not the body.

Private state is not social evidence.

Raw human data must not enter the public repository.

A valid consent and data-sharing boundary must preserve:

- session-bound consent;
- purpose-bound consent;
- revocable consent;
- non-coercive consent;
- consent scope;
- consent duration;
- consent withdrawal;
- packet permission;
- packet expiry;
- private cue permission;
- shared output permission;
- public/private data separation;
- raw-data-non-public boundary;
- audit log boundary.

No consent, no session.

No permission, no packet use.

No sharing scope, no shared output.

No expiry rule, no continued mediation.

A closed session must stay closed.

---

## Schema helper pack

`schemas/` contains public helper schemas for synthetic/sample package structure.

The schemas are provided to document and validate public helper structure.

They are not canonical authority.

They do not define CAIS.

They do not define Sal-Meter.

They do not grant CAIS compliance.

They do not validate Sal-Meter.

They do not validate benchmark performance.

Current schema helper files:

```text
schemas/
  README.md
  session-metadata.schema.json
  streams-manifest.schema.json
  event-markers.schema.json
  labels.schema.json
  qc-report.schema.json
  features-baseline.schema.json
  splits.schema.json
  human_state_packet.schema.json
  dyadic_session_event.schema.json
  benchmark_session.schema.json
```

The schema pack supports:

- synthetic/sample data structure checks;
- metadata consistency;
- timestamp and event marker discipline;
- public/private data separation;
- leakage-risk awareness;
- helper validation;
- Human-State Packet structure demonstration;
- Dyadic Session Event boundary-event demonstration;
- Benchmark Session Container structure demonstration.

It does not support:

- benchmark validation;
- Sal-Meter validation;
- CAIS compliance validation;
- diagnostic validation;
- clinical validation;
- therapeutic validation;
- surveillance validation;
- certification validation;
- human-ranking validation.

The schema layer now includes:

```text
Human-State Packet
→ Dyadic Session Event
→ Benchmark Session Container
```

A schema validates structure.

It does not validate the human body.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not crown a benchmark as validated.

---

## Synthetic sample package

`sample-data/synthetic-session-001/` contains a public synthetic/sample package.

It is provided for structure demonstration only.

It does not contain raw human data.

It does not contain identifiable data.

It does not contain clinical data.

It does not contain Sal-Meter input data.

It does not grant CAIS compliance.

It does not validate benchmark performance.

It does not validate Sal-Meter.

Current synthetic package:

```text
sample-data/synthetic-session-001/
  README.md
  session_metadata.json
  streams_manifest.csv
  events.csv
  labels.csv
  qc_report.json
  features_baseline.csv
  splits.json
  operator_log.md
```

This package demonstrates:

- session-level metadata structure;
- stream inventory structure;
- event marker structure;
- label window structure;
- synthetic baseline feature structure;
- QC report structure;
- split definition structure;
- operator log structure;
- public/private data boundary language;
- leakage-risk awareness.

A public sample package is a lantern.

It lights the path.

It is not the mountain.

---

## Evaluation baseline

`evaluation-baseline/` contains baseline evaluation skeletons and helper-structure validation tools.

It is a research-stage, non-clinical, non-diagnostic, non-therapeutic benchmark support folder.

Current files:

```text
evaluation-baseline/
  README.md
  requirements.txt
  baseline_pipeline_skeleton.py
  leakage_safe_split_example.py
  validate_sample_package.py
```

Purpose:

- load public synthetic proxy benchmark data;
- check structure;
- check required files;
- check JSON parsing;
- check CSV parsing;
- check schema alignment;
- check synthetic status;
- check public boundary fields;
- check operator log boundary language;
- demonstrate leakage-aware split logic;
- provide transparent baseline scaffolding.

It does not validate:

- model performance;
- benchmark performance;
- scientific truth;
- clinical state;
- diagnostic labels;
- therapeutic feedback;
- Sal-Meter input;
- CAIS compliance;
- certification readiness;
- device readiness.

---

## How to run the local validator

From the repository root:

```bash
pip install -r evaluation-baseline/requirements.txt
python evaluation-baseline/validate_sample_package.py
```

Expected successful output:

```text
PASS: sample-data/synthetic-session-001 follows the current public helper structure.
```

A `PASS` means:

```text
The synthetic sample package is internally consistent enough for public helper demonstration.
```

A `PASS` does not mean:

```text
The package proves a benchmark.
The package proves human-state measurement.
The package proves AI-state response safety.
The package proves Sal-Meter readiness.
The package proves CAIS compliance.
```

A `FAIL` usually means one of the following:

- a required file is missing;
- a JSON file cannot be parsed;
- a CSV file has missing or mismatched column names;
- a schema file is invalid;
- a sample file does not match its schema;
- `dataset_type` is not `synthetic`;
- a required public boundary field is missing;
- a boundary flag expected to be `false` is not false;
- `synthetic_status_declared` is missing or not true;
- the operator log is missing expected boundary phrases;
- filenames, field names, or enum values drifted from the helper schemas.

A `FAIL` is not a scientific failure.

A `FAIL` is a structure or boundary mismatch.

---

## GitHub Actions validator workflow

A GitHub Actions workflow file exists at:

```text
.github/workflows/validate-synthetic-sample.yml
```

The intended workflow name is:

```text
Validate Synthetic Sample Package
```

The intended workflow role is to run:

```bash
python evaluation-baseline/validate_sample_package.py
```

Current blocker:

```text
Failed to queue workflow run: Bad request - Actions has been disabled for this user.
```

Repository-level Actions settings have already been checked and saved as:

```text
Allow all actions and reusable workflows
```

Therefore, P1-4 remains open until GitHub restores Actions access and the workflow can run successfully.

This workflow is a repository hygiene and helper-structure validation workflow only.

It does not validate:

- benchmark performance;
- scientific validity;
- Sal-Meter input;
- Sal-Meter validation;
- CAIS compliance;
- diagnostic labels;
- clinical interpretation;
- therapeutic feedback;
- surveillance readiness;
- certification readiness;
- device readiness;
- human-state truth measurement.

The Actions blocker is a workflow-execution blocker.

It is not benchmark evidence.

It is not a CAIS compliance condition.

It is not Sal-Meter validation.

It must not be used as proof of readiness.

---

## Protocol helper boundary pack

`protocol-helper/` contains public helper rules for the SICS Human-State Proxy Benchmark Track.

Current files:

```text
protocol-helper/
  README.md
  session_label_rule.md
  timestamp_sync_rule.md
  metadata_completeness_rule.md
  human_state_cost_construct_note.md
  future_sal_meter_ab_comparison_rule.md
```

The protocol helper pack supports:

- label discipline;
- timestamp discipline;
- metadata completeness;
- leakage awareness;
- Human-State Cost construct boundaries;
- future Sal-Meter A/B comparison boundaries;
- non-diagnostic benchmark helper language.

It does not support:

- clinical labels;
- diagnostic labels;
- therapeutic feedback;
- surveillance scoring;
- human ranking;
- person scoring;
- Sal-Meter validation claims;
- CAIS compliance claims.

---

## Dashboard mockup boundary pack

`dashboard-mockup/` contains public helper dashboard mockup boundary documents.

Current files:

```text
dashboard-mockup/
  README.md
  dashboard_claim_boundary.md
  sample_dashboard_fields.json
  mockup_wireframe.md
```

The dashboard mockup boundary pack supports:

```text
safe dashboard language
synthetic/sample field display
non-diagnostic visualization
non-clinical visualization
non-therapeutic visualization
non-surveillance visualization
non-certification visualization
non-human-ranking visualization
future Sal-Meter A/B placeholder boundary
future dyadic / conflict mediation placeholder boundary
```

It does not support:

```text
validated dashboard claims
clinical dashboard claims
diagnostic dashboard claims
therapeutic dashboard claims
surveillance dashboard claims
employee monitoring claims
insurance scoring claims
legal eligibility claims
human-ranking claims
CAIS compliance claims
Sal-Meter validation claims
```

A dashboard may show a window.

It must not become a courtroom.

It may show a proxy.

It must not become a person score.

---

## Closed-loop demo-lite boundary pack

`closed-loop-demo-lite/` contains public helper documents and placeholder code for a bounded local feedback-loop demonstration surface.

Current files:

```text
closed-loop-demo-lite/
  README.md
  feedback_loop_boundary.md
  feedback_event_log_schema.json
  local_feedback_demo_placeholder.py
```

The closed-loop demo-lite boundary pack supports:

```text
local placeholder structure
synthetic/sample feedback event logs
dashboard-to-log structure demonstration
AI-output event marker examples
synthetic proxy-field review examples
bounded feedback-policy placeholder logic
human-review-required placeholder states
boundary-preserving event logs
audit-friendly local demo structure
```

It does not support:

```text
live intervention
real-time monitoring
production automation
diagnosis
therapy
clinical decision support
medical feedback
surveillance scoring
employee monitoring
insurance scoring
education scoring
legal eligibility scoring
human ranking
person scoring
Sal-Meter feedback loop
CAIS-compliant loop
certified closed-loop system
deployed intervention system
```

A feedback loop may show a path.

It must not move a human being.

A log may remember structure.

It must not become evidence.

A placeholder may point to a future.

It must not pretend that future has arrived.

---

## Replication guide boundary pack

`replication-guide/` contains public helper reproducibility and release-readiness checklists.

Current files:

```text
replication-guide/
  README.md
  reproducibility_package_checklist.md
  metadata_completeness_checklist.md
  audit_trail_checklist.md
  public_release_checklist.md
```

The replication guide supports:

```text
structure review
reproducibility readiness review
metadata completeness review
audit trail review
public helper release-readiness review
Go / Conditional Go / Hold / No-Go decision language
DOI authority versus GitHub helper distinction
validation versus readiness distinction
```

It does not support:

```text
benchmark validation
scientific validation
Sal-Meter validation
CAIS compliance
clinical validation
diagnostic validation
therapeutic validation
surveillance readiness
certification readiness
device readiness
commercial readiness
production deployment
human-state truth validation
human ranking
```

Reproducibility is the bridge.

Validation is the crossing.

This guide builds the bridge.

It does not claim that the crossing has already happened.

---

## Contributor issue / PR boundary gate pack

`.github/ISSUE_TEMPLATE/` and `.github/pull_request_template.md` contain contributor-facing boundary gates.

Current files:

```text
.github/
  ISSUE_TEMPLATE/
    boundary_correction.md
    schema_request.md
    sample_data_issue.md
    leakage_risk_report.md

  pull_request_template.md
```

The contributor template pack supports:

```text
boundary correction requests
schema helper requests
synthetic/sample data issue reports
leakage-risk reports
pull request boundary review
public/private data review
DOI authority review
validation-versus-readiness review
prohibited-claim review
release impact review
```

It does not support:

```text
raw human data submission
identifiable data submission
clinical data submission
private user data submission
Sal-Meter input submission
CAIS compliance submission
benchmark validation claims
scientific validation claims
clinical validation claims
diagnostic validation claims
therapeutic validation claims
surveillance readiness claims
certification readiness claims
device readiness claims
human-ranking claims
production deployment claims
```

Issue templates are gates.

Pull request templates are locks.

The gate allows correction.

The lock prevents false authority.

---

## Human-State Cost boundary

Human-State Cost may appear in this repository only as a bounded, research-stage proxy construct.

It must not be presented as:

```text
a medical score
a psychiatric score
a clinical score
a consciousness score
a psychological safety score
an employee monitoring score
a user dependence diagnosis
a human-ranking measure
a certified benchmark output
a Sal-Meter output
a CAIS output
```

Acceptable language:

```text
Human-State Cost proxy example value
non-diagnostic benchmark construct
synthetic/sample helper field
proxy burden comparison construct
Human-State Cost Proxy Field
```

Prohibited language:

```text
diagnostic score
clinical score
validated human-state score
certified benchmark output
Sal-Meter result
CAIS-compliant output
consciousness measurement
human truth score
```

Human-State Cost must not become a person score.

Human-State Cost must not become diagnosis.

Human-State Cost must not become surveillance.

Human-State Cost must not become Sal-Meter.

Human-State Cost must not become CAIS compliance.

---

## Dyadic / conflict mediation boundary

Future dyadic or conflict mediation work may be referenced only as a bounded research-stage proxy benchmark direction.

Allowed future wording:

```text
Synthetic dyadic interaction mockup
Conflict Mediation Benchmark Preview
Future dyadic proxy benchmark placeholder
Synthetic dyadic feedback event example
Bounded review state
AI Output → Human-State Delta → Dyadic Recovery
Dyadic Recovery Baseline Suite
Recovery Gate
Termination Gate
```

Required boundary:

```text
Not legal mediation.
Not therapy.
Not counseling.
Not relationship diagnosis.
Not fault assignment.
Not who-is-right determination.
Not who-is-wrong determination.
Not surveillance.
Not human ranking.
Not Sal-Meter.
Not CAIS compliance.
```

Not allowed wording:

```text
This dashboard decides who is right.
This feedback loop decides who is right.
This dashboard identifies the unsafe partner.
This loop identifies the unsafe partner.
This dashboard diagnoses the relationship.
This loop provides therapy.
This loop assigns blame.
This system ranks people in conflict.
AI resolves conflict.
AI heals relationships.
AI provides counseling.
```

Dyadic dashboard mockups or demo-lite event logs may compare synthetic interaction windows.

They must not judge humans.

---

## Future Sal-Meter A/B comparison boundary

This repository may later support future A/B comparison between proxy benchmark features and Sal-Meter core inputs.

That future comparison is not active.

No Sal-Meter input is present in this repository.

No CAIS compliance is granted.

No Sal-Meter validation is claimed.

Allowed placeholder language:

```text
future_sal_meter_input_placeholder
future_proxy_core_comparison_placeholder
not_present
not_public
not_validated_here
future_placeholder_only
hold_until_separate_governance
future candidate pathway
future Sal-Meter-derived input candidate pathway
```

Prohibited placeholder language:

```text
validated_sal_meter_input
CAIS_compliant_signal
official_consciousness_signal
ground_truth_signal
diagnostic_sal_meter_result
Sal-Meter feedback loop
Sal-Meter intervention loop
Sal-Meter-compatible node exists
```

Future comparison must remain future until separate governance, data rights, consent, raw data handling, audit trail, and validation rules exist.

---

## Leakage-control principles

This repository treats leakage control as a first-class benchmark requirement.

A model, dashboard, feedback-loop placeholder, release-readiness review, pull request, issue report, or evaluation pipeline must not learn labels from hidden shortcuts such as:

- participant identity;
- dyad identity;
- day or session order;
- condition names;
- filenames;
- folder names;
- device identity;
- operator identity;
- preprocessing artifacts;
- timestamp artifacts;
- metadata fields that encode labels;
- dashboard-visible labels leaking into model input;
- feedback-log fields leaking the target label;
- train/validation/test contamination.

Synthetic data may expose labels for demonstration.

Real benchmark data must not.

A result that leaks labels is not evidence.

---

## Metadata completeness principles

A benchmark package must be reviewable.

A reviewable package needs:

- session ID;
- dataset type;
- synthetic or human-data status;
- public/private data boundary;
- stream manifest;
- event markers;
- label windows;
- feature table;
- QC report;
- split definition;
- operator log;
- schema version;
- timestamp source;
- known offsets;
- drift notes;
- missingness notes;
- leakage review notes;
- dashboard boundary notes;
- closed-loop demo-lite boundary notes, if applicable;
- feedback event-log boundary, if applicable;
- issue / PR boundary notes, if applicable;
- file mapping;
- audit trail;
- raw data handover boundary, if applicable under private governance.

A package without metadata cannot be audited.

A package that cannot be audited cannot become benchmark evidence.

---

## Audit trail principles

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

Every contribution should answer:

```text
Which issue or PR introduced this change?
Which boundary did it preserve?
Which data did it exclude?
Which authority did it not create?
Which validation did it not claim?
```

An audit trail is not decoration.

It is the spine of trust.

---

## Suggested local stack

This repository is currently a public helper documentation and scaffold repository.

Potential future proxy benchmark implementation may use:

- LSL for stream synchronization;
- BrainFlow for biosignal interface abstraction;
- Timeflux for real-time signal pipelines;
- Python for data loading and evaluation;
- scikit-learn for transparent baseline models;
- PyTorch for later modeling experiments, if justified;
- OpenFace or equivalent public vision-proxy tools for bounded, non-identifying examples only;
- CARLA for simulator-linked interaction scenarios;
- lightweight local web UI for dashboard mockups;
- local NAS and versioned metadata store for private raw-data governance, if future human data are collected under separate approval.

This stack is not required for the current public helper package.

This stack does not validate the benchmark.

This stack does not create Sal-Meter.

This stack does not grant CAIS compliance.

This stack does not create a production closed-loop intervention system.

---

## Public release boundary

A public helper pre-release must not be published until:

- public helper boundary language is stable;
- synthetic/sample data boundaries are clear;
- schema references are correct;
- evaluator / validator documentation is clear;
- dashboard boundaries are visible;
- closed-loop demo-lite boundaries are visible, if included;
- replication guide checklists are visible;
- issue / PR boundary templates are visible;
- audit trail expectations are visible;
- public release checklist is passed;
- `CITATION.cff` points to DOI-registered public records;
- `README.md` clearly states the repository is a helper surface;
- no raw human data are present;
- no identifiable data are present;
- no clinical data are present;
- no real dyadic conflict records are present;
- no Sal-Meter input is present;
- no CAIS compliance claim is present;
- no benchmark validation claim is present;
- no diagnostic, clinical, therapeutic, surveillance, certification, counseling, mediation-service, or human-ranking authority is implied;
- no live intervention or production automation is implied;
- GitHub pre-release status is selected, if a GitHub Release is published;
- no binary assets are attached unless separately approved;
- P3-17 closes with Go.

Current release status:

```text
v0.1.0 public helper pre-release package: prepared.
Actual GitHub Release: not yet published in this README state.
Publication gate: P3-17 final authorization required.
Publication mode, if authorized: GitHub pre-release.
Binary assets: none unless separately approved.
```

GitHub Actions validator status:

```text
P1-4 GitHub Actions validator workflow remains blocked by account-level Actions restriction.
This is a workflow-execution blocker.
It is not benchmark validation.
It is not Sal-Meter validation.
It is not CAIS compliance.
It does not authorize production use.
```

The `v0.1.0` public helper pre-release, if published, must remain a helper package.

It must not become a validation claim.

It must not become a compliance claim.

It must not become a device claim.

It must not become a clinical claim.

---

## Citation guidance

If you use this repository, cite the DOI-registered public boundary records rather than treating GitHub as the canonical authority.

Preferred public boundary record:

```text
SICS Human-State Proxy Benchmark Track — Public Boundary and Program Charter v0.1
Version DOI: https://doi.org/10.5281/zenodo.19837423
Concept DOI: https://doi.org/10.5281/zenodo.19837422
```

Scientific rationale record:

```text
SICS Human-State Proxy Benchmark Track — Scientific Rationale and Research Value v0.1
Version DOI: https://doi.org/10.5281/zenodo.19837971
Concept DOI: https://doi.org/10.5281/zenodo.19837970
```

Human-State-Aware AI Mediation record set:

```text
Human-State Mediation Boundary Standard v0.1
Version DOI: https://doi.org/10.5281/zenodo.19904289
Concept DOI: https://doi.org/10.5281/zenodo.19904288

Human-State Packet Minimal Data-Sharing Standard v0.1
Version DOI: https://doi.org/10.5281/zenodo.19905541
Concept DOI: https://doi.org/10.5281/zenodo.19905540

Dyadic Human-State Mediation Benchmark Charter v0.1
Version DOI: https://doi.org/10.5281/zenodo.19906725
Concept DOI: https://doi.org/10.5281/zenodo.19906724

Human-State Session Protocol v0.1 — Structural Declaration
Version DOI: https://doi.org/10.5281/zenodo.19908379
Concept DOI: https://doi.org/10.5281/zenodo.19908378
```

This GitHub repository is a public technical helper surface.

It is not the authority layer.

---

## Governance rule

Public helper materials may explain.

They must not overrule DOI-registered records.

Public helper materials may guide implementation.

They must not create compliance.

Public helper materials may demonstrate structure.

They must not claim validation.

Public helper materials may support release-readiness review.

They must not publish authority.

Public helper materials may receive contributor requests.

They must not convert contributor requests into validation claims.

Public helper materials may recruit builders.

They must not imply clinical, therapeutic, diagnostic, surveillance, certification, intervention, counseling, mediation-service, legal mediation, or human-ranking authority.

---

## Naming rule

Use:

```text
proxy benchmark track
Human-State Proxy Benchmark Track
Human-State-Aware AI Interaction
Human-State-Aware AI Mediation Benchmark
Dyadic Human-State Mediation Benchmark
AI Output → Human-State Delta → Dyadic Recovery
Human-State Packet
Human-State Session Protocol
Human-State Mediation Layer
Dyadic Recovery Baseline Suite
Recovery Gate
Termination Gate
Consent and Data-Sharing Boundary
research-stage helper
synthetic sample package
dashboard mockup boundary
closed-loop demo-lite
local feedback demo placeholder
replication guide
reproducibility package checklist
metadata completeness checklist
audit trail checklist
public release checklist
boundary correction issue template
schema request issue template
sample data issue template
leakage risk report issue template
pull request boundary review template
helper-structure validator
future Sal-Meter A/B comparison placeholder
future Sal-Meter-derived input candidate pathway
```

Do not use:

```text
validated Sal-Meter
CAIS-compliant device
CAIS-compliant mediation layer
clinical dashboard
diagnostic dashboard
therapeutic dashboard
clinical feedback loop
therapeutic feedback loop
certified benchmark
certified closed-loop system
official consciousness measurement
human truth score
employee monitoring score
psychological safety score
certified reproducibility
commercial readiness
AI resolves conflict
AI heals relationships
AI provides therapy
AI provides counseling
AI provides legal mediation
AI decides who is right
AI identifies the problem person
Sal-Meter-compatible node exists
```

Names are gates.

Bad names open bad doors.

---

## Contributor boundary

Potential contributors should first understand:

1. whether you are working on a public helper surface;
2. whether you are handling synthetic/sample data only;
3. whether any raw human data are involved;
4. whether your work could be mistaken for diagnosis, therapy, counseling, surveillance, certification, intervention, legal mediation, or human ranking;
5. whether your work implies Sal-Meter validation;
6. whether your work implies CAIS compliance;
7. whether the relevant DOI-registered boundary record is preserved;
8. whether the appropriate issue template is being used;
9. whether a pull request preserves public/private data boundary, prohibited-claim discipline, DOI authority distinction, and validation-versus-readiness distinction.

Issue templates are gates.

Pull request templates are locks.

Do not send broad partnership material first.

Send one bounded capability.

---

## Current open holds

```text
P1-4 remains open:
  GitHub Actions workflow exists but is blocked by account-level Actions restriction.

P1-4 meaning:
  Workflow execution is blocked.
  Benchmark validation is not claimed.
  Sal-Meter validation is not claimed.
  CAIS compliance is not claimed.

P1-5 release readiness:
  v0.1.0 public helper pre-release package has been prepared.
  Publication may proceed only if P3-17 closes with Go.
  Publication must use GitHub pre-release status.
  Publication must not attach binary assets unless separately approved.
  Publication must not imply validation, compliance, production readiness, or clinical use.

P3 helper layer:
  P3 helper documents are completed through P3-15.
  P3 release publication authorization remains gated by P3-17.
  P3 does not validate a benchmark.
  P3 does not validate Sal-Meter.
  P3 does not grant CAIS compliance.

No raw human data is authorized.

No identity-bearing data is authorized.

No real dyadic conflict records are authorized.

No raw Sal-Meter traces are authorized.

No raw CAIS traces are authorized.
```

---

## License

Unless otherwise stated, public helper materials in this repository are provided under:

**Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**

This license does not grant:

- CAIS compliance;
- Sal-Meter designation;
- certification rights;
- mark-usage rights;
- clinical-use rights;
- diagnostic-use rights;
- therapeutic-use rights;
- counseling-use rights;
- legal-mediation-use rights;
- intervention-use rights;
- surveillance-use rights;
- authority to speak for SICS;
- authority to reinterpret DOI-registered canonical records.

---

## Final boundary sentence

This repository is a public helper surface.

It is a scaffold, not a verdict.

It is a map, not the mountain.

It prepares future comparison.

It prepares future packet discipline.

It prepares future session discipline.

It prepares future dyadic recovery benchmark discipline.

It prepares future consent and data-sharing discipline.

It prepares future recovery-gate discipline.

It prepares future termination-gate discipline.

It prepares future feedback-loop discipline.

It prepares reproducibility and release-readiness review.

It prepares contributor boundary gates.

It does not claim that future comparison has already been validated.

It does not claim that a closed loop is ready to act on human beings.

It does not claim that issue or PR templates create scientific authority.

It does not claim that a public release would create scientific, clinical, CAIS, or Sal-Meter authority.

The benchmark does not crown the AI for speaking well.

It asks what changed in the human state.

It asks whether the dyad moved toward recovery.

It asks whether the AI stopped when it should stop.

If the session can no longer continue without crossing a boundary, the gate must close.

A closed session must stay closed.
