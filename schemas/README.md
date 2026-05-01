# Schemas

This folder contains public helper schemas for the SICS Human-State Proxy Benchmark Track.

These schemas are provided to document and validate the structure of the public synthetic/sample package and the P3 Human-State-Aware AI Mediation helper layer.

They are not canonical authority.

They do not define CAIS.

They do not define Sal-Meter.

They do not grant CAIS compliance.

They do not validate Sal-Meter.

They do not validate benchmark performance.

They do not validate mediation.

They do not create diagnostic, therapeutic, clinical, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

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
- Human-State Packet helper structure;
- dyadic session event helper structure;
- benchmark session container helper structure;
- future reproducibility helper workflows.

They are not intended to support:

- raw human data publication;
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
| `human_state_packet.schema.json` | one Human-State Packet helper object | Minimal consent-bound, permission-bound, expiry-bound, confidence-aware, data-quality-aware, session-scoped, sharing-scoped, raw-data-excluding packet structure |
| `dyadic_session_event.schema.json` | one dyadic session event helper object | Public-safe synthetic/sample event object for consent, permission, packet status, private cue, shared output, Human-State Delta A/B, Dyadic Delta, gates, closure, and audit status |
| `benchmark_session.schema.json` | one benchmark session helper container | Public-safe synthetic/sample benchmark session container connecting event references, baseline suite status, gate summaries, leakage review, holdout strategy, audit status, authority status, and final boundary status |

---

## P3 helper schema layer

P3 introduces the Human-State-Aware AI Mediation helper schema layer.

This layer has three object levels:

```text
Human-State Packet
→ Dyadic Session Event
→ Benchmark Session Container
```

These schemas validate helper structure.

They do not validate human state.

They do not validate dyadic recovery.

They do not validate benchmark success.

They do not validate Sal-Meter.

They do not grant CAIS compliance.

---

## Human-State Packet helper schema

`human_state_packet.schema.json` validates a minimal Human-State Packet helper object.

A valid Human-State Packet helper object should remain:

- minimal;
- consent-bound;
- permission-bound;
- expiry-bound;
- confidence-aware;
- data-quality-aware;
- session-scoped;
- sharing-scoped;
- raw-data-excluding.

It may describe bounded state-summary structure.

It must not include:

- raw human data;
- raw biosignals;
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
- Sal-Meter validation claim;
- CAIS compliance claim.

The packet is an interface object.

It is not the body.

---

## Dyadic Session Event helper schema

`dyadic_session_event.schema.json` validates one public-safe synthetic/sample dyadic session boundary event.

It may record:

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

It does not validate mediation.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

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
- final boundary status.

It records the benchmark container.

It does not record the body.

It does not contain raw human data.

It does not expose private state.

It does not validate a benchmark.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not crown a benchmark as validated.

---

## Expected sample package alignment

The original sample package schemas are aligned with the following public synthetic package structure:

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

P3 helper schemas may later support public-safe synthetic helper objects such as:

```text
sample-data/
  synthetic-session-001/
    human_state_packet.example.json
    dyadic_session_event.example.json
    benchmark_session.example.json
```

These examples must remain synthetic, mock, placeholder, or structure-only.

They must not contain real human data.

They must not contain identifiable participant data.

They must not contain real dyadic conflict content.

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
not Sal-Meter
not CAIS compliance
```

Public files must not contain:

- raw human biosignal data;
- raw human video;
- raw face, voice, gaze, or audio data;
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
- Sal-Meter input data;
- raw Sal-Meter traces;
- raw CAIS traces;
- CAIS compliance claims;
- certification claims;
- validated benchmark claims.

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

They do not validate Sal-Meter input.

They do not validate CAIS compliance.

They do not validate clinical, diagnostic, therapeutic, surveillance, employment, insurance, educational, legal, or eligibility use.

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
- `non-surveillance`;
- `benchmark-support`;
- `public helper schema`;
- `raw-data-non-public`;
- `synthetic-public-data-first`.

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
- `human truth score`;
- `consciousness measurement`;
- `psychological safety score`;
- `employee monitoring score`;
- `production-ready`;
- `Sal-Meter-compatible node exists`.

---

## Authority rule

GitHub is a helper surface.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this repository conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

The schemas in this folder help builders move.

They do not create canonical authority.

---

## Current P3 schema state

This folder currently provides structure schemas for the public synthetic/sample package and the P3 Human-State-Aware AI Mediation helper layer.

Status:

```text
Research-stage helper schemas.
Synthetic/sample structure validation only.
P3 helper schema alignment in progress.
human_state_packet.schema.json exists.
dyadic_session_event.schema.json exists.
benchmark_session.schema.json exists.
Not benchmark evidence.
Not validated mediation.
Not Sal-Meter.
Not CAIS compliance.
No raw human data.
```

Completed P3 helper schemas:

```text
schemas/
  human_state_packet.schema.json
  dyadic_session_event.schema.json
  benchmark_session.schema.json
```

The schemas remain public helper schemas only.

No raw human data is allowed.

No benchmark validation is claimed.

No Sal-Meter validation is claimed.

No CAIS compliance is claimed.
