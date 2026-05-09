# Schemas

This folder contains public helper schemas for the **SICS Human-State Proxy Benchmark Track**.

These schemas document and validate the structure of public synthetic/sample helper packages, including the original synthetic sample package and the P3 Human-State-Aware AI Mediation helper layer.

They are helper schemas only.

They are not canonical authority.

They do not define CAIS.

They do not define Sal-Meter.

They do not grant CAIS compliance.

They do not validate Sal-Meter.

They do not validate benchmark performance.

They do not validate scientific truth.

They do not validate mediation.

They do not validate human-state measurement.

They do not create diagnostic, therapeutic, clinical, counseling, surveillance, employment, insurance, educational, legal, eligibility, certification, device-readiness, production-deployment, mediation-service, or human-ranking authority.

---

## Public boundary

The schemas in this folder are for public helper use only.

They are intended to support:

- synthetic/sample data structure checks;
- metadata consistency;
- timestamp and event marker discipline;
- public/private data separation;
- leakage-risk awareness;
- baseline feature table structure;
- QC report structure;
- split definition structure;
- Human-State Packet helper structure;
- dyadic session event helper structure;
- benchmark session container helper structure;
- P3 helper-schema validation;
- future reproducibility helper workflows.

They are not intended to support:

- raw human data publication;
- identifiable human data publication;
- clinical interpretation;
- diagnostic labeling;
- therapeutic feedback;
- counseling service;
- legal mediation service;
- surveillance scoring;
- employment, insurance, educational, legal, or eligibility decisions;
- CAIS compliance claims;
- Sal-Meter validation claims;
- validated benchmark claims;
- validated mediation claims;
- certified benchmark claims;
- production closed-loop intervention.

---

## Schema files

| File | Validates | Public role |
|---|---|---|
| `session-metadata.schema.json` | `session_metadata.json` | Session-level metadata, synthetic status, signal list, data boundary, leakage review |
| `event-markers.schema.json` | one row object from `events.csv` | Timestamped event markers for session, task, AI interaction, feedback, and recovery events |
| `streams-manifest.schema.json` | one row object from `streams_manifest.csv` | Stream inventory, synthetic signal names, sampling rates, sync status, file paths |
| `labels.schema.json` | one row object from `labels.csv` | Non-diagnostic synthetic/session label windows |
| `qc-report.schema.json` | `qc_report.json` | QC status, stream checks, leakage review, public release boundary |
| `features-baseline.schema.json` | one row object from `features_baseline.csv` | Synthetic baseline feature rows and Human-State Cost proxy example values |
| `splits.schema.json` | `splits.json` | Synthetic split definition, leakage notes, and holdout structure demonstration |
| `human_state_packet.schema.json` | one Human-State Packet helper object | Consent-bound, permission-bound, expiry-bound, confidence-aware, data-quality-aware, session-scoped, sharing-scoped, raw-data-excluding packet structure |
| `dyadic_session_event.schema.json` | one dyadic session event helper object | Public-safe synthetic/sample event object for consent, permission, packet status, private cue, shared output, Human-State Delta A/B, Dyadic Delta, gates, closure, and audit status |
| `benchmark_session.schema.json` | one benchmark session helper container | Public-safe synthetic/sample benchmark session container connecting event references, baseline suite status, gate summaries, leakage review, holdout strategy, audit status, authority status, and final boundary status |

---

## P5-1 / P3 helper schema layer

P5-1 extends the repository from document-only helper structure toward machine-checkable P3 helper-schema scaffolding.

The P3 helper layer has three object levels:

```text
Human-State Packet
→ Dyadic Session Event
→ Benchmark Session Container
```

These schemas validate helper structure only.

They do not validate human state.

They do not validate dyadic recovery.

They do not validate benchmark success.

They do not validate scientific truth.

They do not validate mediation effectiveness.

They do not validate Sal-Meter.

They do not grant CAIS compliance.

They do not authorize clinical, diagnostic, therapeutic, counseling, surveillance, employment, insurance, educational, legal, eligibility, certification, device-readiness, production-deployment, mediation-service, or human-ranking use.

---

## Current P5-1 implementation status

Current P5-1 helper-schema files:

```text
schemas/
  human_state_packet.schema.json
  dyadic_session_event.schema.json
  benchmark_session.schema.json
```

Current P5-1 synthetic dyadic sample package:

```text
sample-data/
  synthetic-dyadic-session-001/
    README.md
    human_state_packet_A.json
    human_state_packet_B.json
    dyadic_session_event.json
    benchmark_session_container.json
```

Current P5-1 validator:

```text
evaluation-baseline/validate_p3_schemas.py
```

Current workflow integration:

```text
.github/workflows/validate-synthetic-sample.yml
```

The workflow may run:

```text
validate_sample_package.py
validate_p3_schemas.py
boundary_lint.py
```

This automation checks structure and boundary hygiene only.

It does not validate benchmark performance.

It does not validate scientific truth.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

---

## Human-State Packet helper schema

`human_state_packet.schema.json` validates one public-safe Human-State Packet helper object.

A valid Human-State Packet helper object should remain:

- minimal;
- consent-bound;
- permission-bound;
- expiry-bound;
- confidence-aware;
- data-quality-aware;
- session-scoped;
- sharing-scoped;
- raw-data-excluding;
- synthetic/sample-only when used in this public repository.

It may describe bounded state-summary structure.

It must not include:

- raw human data;
- raw biosignals;
- raw ECG;
- raw EEG;
- raw EDA;
- raw PPG;
- raw voice;
- raw face;
- raw gaze;
- raw video;
- raw transcript;
- identifiable participant data;
- clinical interpretation;
- diagnostic label;
- therapeutic label;
- counseling note;
- legal mediation conclusion;
- relationship verdict;
- human score;
- psychological safety score;
- employment score;
- insurance score;
- educational score;
- legal eligibility score;
- Sal-Meter validation claim;
- CAIS compliance claim;
- certification claim.

Correct boundary sentence:

```text
A Human-State Packet is a consent-bound, session-scoped, expiring state-summary helper object for interaction adjustment only.
```

The packet is an interface object.

It is not the body.

It is not a diagnosis.

It is not a verdict.

It is not Sal-Meter.

It is not CAIS compliance.

---

## Dyadic Session Event helper schema

`dyadic_session_event.schema.json` validates one public-safe synthetic/sample dyadic session boundary event.

It may record:

- schema version;
- event ID;
- dyadic session ID;
- event type;
- timestamp;
- dataset type;
- synthetic status;
- actor role;
- participant scope;
- session scope status;
- consent status;
- permission status;
- packet status;
- sharing scope;
- private cue status;
- shared output status;
- Human-State Delta A;
- Human-State Delta B;
- Dyadic Delta;
- Recovery Gate decision;
- Termination Gate decision;
- closure reason;
- data quality status;
- confidence status;
- boundary flags;
- audit reference;
- final boundary status.

It records the boundary.

It does not record the body.

It does not expose private state.

It does not judge either participant.

It does not assign blame.

It does not decide who is right.

It does not decide who is wrong.

It does not validate mediation.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

Correct boundary sentence:

```text
A Dyadic Session Event describes bounded synthetic session structure, not human truth or relationship judgment.
```

---

## Benchmark Session helper schema

`benchmark_session.schema.json` validates one public-safe synthetic/sample benchmark session container.

It may connect:

- session identity;
- synthetic status;
- benchmark scope;
- benchmark stage;
- session type;
- participant scope;
- modality stack labels;
- dyadic session event references;
- baseline suite status;
- primary outcome label;
- Human-State Delta summary;
- Dyadic Delta summary;
- Recovery Gate summary;
- Termination Gate summary;
- leakage review status;
- holdout strategy;
- data boundary status;
- consent boundary status;
- sharing boundary status;
- audit status;
- public release status;
- authority status;
- boundary flags;
- final boundary status.

It records the benchmark container.

It does not record the body.

It does not contain raw human data.

It does not expose private state.

It does not validate a benchmark.

It does not validate scientific truth.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not crown a benchmark as validated.

Correct boundary sentence:

```text
A Benchmark Session Container demonstrates helper structure only; it is not benchmark evidence.
```

---

## Expected package alignment

The original public synthetic sample package is:

```text
sample-data/
  synthetic-session-001/
    session_metadata.json
    streams_manifest.csv
    events.csv
    labels.csv
    qc_report.json
    features_baseline.csv
    splits.json
    operator_log.md
```

The P5-1 / P3 synthetic dyadic helper package is:

```text
sample-data/
  synthetic-dyadic-session-001/
    README.md
    human_state_packet_A.json
    human_state_packet_B.json
    dyadic_session_event.json
    benchmark_session_container.json
```

These two folders serve different helper purposes.

They should not be merged.

The original `synthetic-session-001` package demonstrates a public synthetic session package using CSV/JSON helper files.

The `synthetic-dyadic-session-001` package demonstrates a P3 dyadic helper package using schema-aligned JSON objects.

---

## P3 validation mapping

The P3 validator should use the following mapping:

```text
sample-data/synthetic-dyadic-session-001/human_state_packet_A.json
  → schemas/human_state_packet.schema.json

sample-data/synthetic-dyadic-session-001/human_state_packet_B.json
  → schemas/human_state_packet.schema.json

sample-data/synthetic-dyadic-session-001/dyadic_session_event.json
  → schemas/dyadic_session_event.schema.json

sample-data/synthetic-dyadic-session-001/benchmark_session_container.json
  → schemas/benchmark_session.schema.json
```

A successful P3 helper-schema validation means only:

```text
The public synthetic/sample P3 helper files follow the expected helper-schema structure.
```

A successful P3 helper-schema validation does not mean:

```text
The benchmark is validated.
The science is validated.
The mediation system works.
The dyadic recovery is real.
The repository is Sal-Meter.
The repository is CAIS-compliant.
The package is clinical.
The package is diagnostic.
The package is therapeutic.
The package is certified.
The package is device-ready.
The package is production-ready.
```

---

## Public synthetic/sample rule

Public repository examples must remain:

```text
synthetic
sample
mock
placeholder
structure-only
non-identifying
raw-data-free
not benchmark evidence
not scientific validation
not mediation validation
not Sal-Meter
not CAIS compliance
```

Public files must not contain:

- raw human biosignal data;
- raw human video;
- raw face data;
- raw voice data;
- raw gaze data;
- raw audio data;
- raw transcript;
- direct identifiers;
- identity mapping files;
- private consent records;
- real dyadic conflict records;
- clinical interpretation;
- diagnostic labels;
- therapeutic recommendations;
- counseling notes;
- legal mediation conclusions;
- relationship verdicts;
- human scores;
- psychological safety scores;
- employment monitoring scores;
- insurance eligibility scores;
- educational eligibility scores;
- legal eligibility scores;
- Sal-Meter input data;
- raw Sal-Meter traces;
- raw CAIS traces;
- CAIS compliance claims;
- certification claims;
- validated benchmark claims;
- validated mediation claims;
- production closed-loop claims.

Public examples may show structure.

They must not expose real persons.

They must not expose real dyads.

They must not expose the body.

---

## Important distinction

These schemas validate structure.

They do not validate scientific truth.

They do not validate human-state inference.

They do not validate Human-State Cost as a certified score.

They do not validate dyadic recovery.

They do not validate Recovery Gate success.

They do not validate Termination Gate maturity.

They do not validate mediation effectiveness.

They do not validate Sal-Meter input.

They do not validate CAIS compliance.

They do not validate clinical, diagnostic, therapeutic, counseling, surveillance, employment, insurance, educational, legal, or eligibility use.

A valid schema object means:

```text
The object follows the expected public helper structure.
```

A valid schema object does not mean:

```text
The data is real evidence.
The benchmark is validated.
The model is reliable.
The session is therapeutic.
The system is diagnostic.
The system is Sal-Meter.
The system is CAIS-compliant.
The system is ready for production.
```

---

## Schema validation can check

Schema validation can check:

- field presence;
- field type;
- allowed enum values;
- missing required fields;
- undefined leakage fields;
- public-safe synthetic status;
- boundary flags;
- object-level structure;
- reference naming patterns;
- public helper status;
- raw-data absence flags;
- overclaim absence flags.

Schema validation can help prevent uncontrolled structure drift.

Schema validation can help contributors avoid boundary mistakes.

Schema validation can help automation reject public-unsafe objects.

---

## Schema validation cannot prove

Schema validation cannot prove:

- clinical validity;
- therapeutic benefit;
- dyadic recovery;
- benchmark success;
- model quality;
- human-state truth;
- Sal-Meter validity;
- CAIS compliance;
- production readiness;
- safety in real deployment;
- legal sufficiency;
- ethical approval;
- IRB approval.

A schema can guard the gate.

It cannot declare the kingdom proven.

---

## Human-State Cost boundary

Human-State Cost may appear in this repository only as a non-diagnostic benchmark construct or synthetic/example field.

It must not be presented as:

- a medical score;
- a psychiatric score;
- a clinical score;
- a consciousness score;
- a psychological safety score;
- an AI harm diagnosis;
- a toxicity diagnosis;
- an employee wellbeing score;
- a user dependence diagnosis;
- a human-ranking measure;
- a certified benchmark output;
- a Sal-Meter output;
- a CAIS output.

Permitted phrasing:

```text
Human-State Cost is a non-diagnostic benchmark construct used to compare measurable proxy burdens across AI interaction conditions.
```

Prohibited phrasing:

```text
Human-State Cost diagnoses the user’s psychological or physiological condition.
```

Correct boundary sentence:

```text
Human-State Cost evaluates the interaction condition, not the person.
```

---

## Naming rule

Use:

- `synthetic`;
- `sample_structure_only`;
- `mock`;
- `placeholder`;
- `structure_only`;
- `research-stage`;
- `non-clinical`;
- `non-diagnostic`;
- `non-therapeutic`;
- `non-counseling`;
- `non-surveillance`;
- `non-certification`;
- `non-human-ranking`;
- `benchmark-support`;
- `public helper schema`;
- `helper-schema validation`;
- `raw-data-non-public`;
- `synthetic-public-data-first`;
- `not Sal-Meter`;
- `not CAIS compliance`;
- `not benchmark validation`;
- `not mediation validation`;
- `no raw human data`.

Do not use:

- `validated`;
- `certified`;
- `diagnostic`;
- `therapeutic`;
- `clinical`;
- `CAIS-compliant`;
- `Sal-Meter validated`;
- `validated benchmark`;
- `validated mediation`;
- `validated dyadic recovery system`;
- `human truth score`;
- `consciousness measurement`;
- `psychological safety score`;
- `employee monitoring score`;
- `production-ready`;
- `device-ready`;
- `emotion-reading AI`;
- `relationship scoring system`;
- `human ranking system`.

---

## GitHub Actions alignment

The current workflow may run schema-related helper checks from:

```text
.github/workflows/validate-synthetic-sample.yml
```

The P3 helper-schema validator is:

```text
evaluation-baseline/validate_p3_schemas.py
```

The intended P3 validation role is:

```text
Check P3 helper-schema structure only.
```

The intended workflow posture is:

```text
Run existing synthetic sample package validator.
Run P3 helper schema validator.
Run boundary language lint.
```

These checks are repository hygiene helpers.

They are not benchmark validators.

They are not scientific validators.

They are not Sal-Meter validators.

They are not CAIS compliance validators.

They are not mediation validators.

---

## Authority rule

GitHub is a helper surface.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this repository conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

The schemas in this folder help builders move.

They do not create canonical authority.

---

## Current P5-1 schema state

This folder currently provides structure schemas for the public synthetic/sample package and the P3 Human-State-Aware AI Mediation helper layer.

Status:

```text
Research-stage helper schemas.
Synthetic/sample structure validation only.
P5-1 P3 helper schema alignment active.
human_state_packet.schema.json exists.
dyadic_session_event.schema.json exists.
benchmark_session.schema.json exists.
sample-data/synthetic-dyadic-session-001 exists.
evaluation-baseline/validate_p3_schemas.py exists.
GitHub Actions P3 validator step added.
Not benchmark evidence.
Not scientific validation.
Not validated mediation.
Not Sal-Meter.
Not CAIS compliance.
No raw human data.
No identifiable human data.
No clinical data.
```

Completed P3 helper schemas:

```text
schemas/
  human_state_packet.schema.json
  dyadic_session_event.schema.json
  benchmark_session.schema.json
```

Current P3 synthetic helper package:

```text
sample-data/
  synthetic-dyadic-session-001/
    README.md
    human_state_packet_A.json
    human_state_packet_B.json
    dyadic_session_event.json
    benchmark_session_container.json
```

The schemas remain public helper schemas only.

No raw human data is allowed.

No benchmark validation is claimed.

No Sal-Meter validation is claimed.

No CAIS compliance is claimed.

---

## Final rule

A schema can validate structure.

A schema cannot validate truth.

A schema can guard public helper boundaries.

A schema cannot crown scientific evidence.

A schema can reduce drift.

A schema cannot grant authority.

The packet is not the person.

The event is not the relationship.

The container is not the benchmark.

The schema is a gate.

It is not the kingdom.
