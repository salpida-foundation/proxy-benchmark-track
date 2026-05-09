# Synthetic Dyadic Session 001

This folder contains a public synthetic/sample dyadic helper package for the **SICS Human-State Proxy Benchmark Track**.

It is provided for P3 helper-schema structure demonstration only.

It is not benchmark validation.

It is not scientific validation.

It is not Sal-Meter validation.

It is not CAIS compliance.

It is not mediation validation.

It does not contain raw human data.

It does not contain identifiable human data.

It does not contain clinical data.

It does not contain Sal-Meter input.

It does not contain CAIS compliance dossiers.

It does not create diagnostic, therapeutic, clinical, counseling, surveillance, employment, insurance, educational, legal, eligibility, certification, device-readiness, production-deployment, mediation-service, or human-ranking authority.

---

## Purpose

This package demonstrates a synthetic public-helper structure for the P3 dyadic benchmark scaffold:

```text
Human-State Packet A
Human-State Packet B
Dyadic Session Event
Benchmark Session Container
```

The package is designed to support bounded helper-schema validation for:

- Human-State Packet structure;
- dyadic event structure;
- benchmark session container structure;
- synthetic/sample status declaration;
- raw human data exclusion;
- identifiable data exclusion;
- clinical data exclusion;
- Sal-Meter input exclusion;
- CAIS compliance claim exclusion;
- benchmark validation claim exclusion;
- mediation validation claim exclusion.

This package is not evidence.

This package is not a real dyadic session.

This package is not a human-state dataset.

This package is not a Sal-Meter dataset.

This package is not a CAIS-compliant output.

This package is not a mediation result.

---

## Folder contents

```text
sample-data/
  synthetic-dyadic-session-001/
    README.md
    human_state_packet_A.json
    human_state_packet_B.json
    dyadic_session_event.json
    benchmark_session_container.json
```

---

## File roles

| File | Role | Boundary |
|---|---|---|
| `README.md` | Local package boundary and usage explanation | Public helper documentation only |
| `human_state_packet_A.json` | Synthetic Human-State Packet for participant A | No raw human data, no identity data, no diagnosis, no Sal-Meter input |
| `human_state_packet_B.json` | Synthetic Human-State Packet for participant B | No raw human data, no identity data, no diagnosis, no Sal-Meter input |
| `dyadic_session_event.json` | Synthetic dyadic event object | No relationship verdict, no blame assignment, no mediation validation |
| `benchmark_session_container.json` | Synthetic benchmark session container | Not benchmark validation, not scientific validation, not CAIS compliance |

---

## P3 helper chain

The intended helper chain is:

```text
Human-State Packet A
+
Human-State Packet B
↓
Dyadic Session Event
↓
Benchmark Session Container
```

This chain demonstrates structure only.

It does not prove that a real dyadic recovery occurred.

It does not prove that an AI mediation output worked.

It does not prove human-state measurement.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

---

## Schema alignment

This package is intended to align with the following helper schemas:

```text
schemas/human_state_packet.schema.json
schemas/dyadic_session_event.schema.json
schemas/benchmark_session.schema.json
```

Expected validation mapping:

```text
human_state_packet_A.json
  → schemas/human_state_packet.schema.json

human_state_packet_B.json
  → schemas/human_state_packet.schema.json

dyadic_session_event.json
  → schemas/dyadic_session_event.schema.json

benchmark_session_container.json
  → schemas/benchmark_session.schema.json
```

These schemas validate helper structure only.

They do not validate benchmark performance.

They do not validate scientific truth.

They do not validate human-state measurement.

They do not validate mediation effectiveness.

They do not validate Sal-Meter.

They do not grant CAIS compliance.

---

## Synthetic status

All files in this folder must remain synthetic/sample/helper material only.

Required public posture:

```text
dataset_type: synthetic / sample / mock / placeholder / structure_only
synthetic_status: synthetic_only / sample_only / mock_only / placeholder_only / structure_only / not_real_human_data
raw human data: absent
identifiable data: absent
clinical data: absent
Sal-Meter input: absent
CAIS compliance dossier: absent
benchmark validation claim: absent
mediation validation claim: absent
```

If any future file cannot satisfy this boundary, it does not belong in this public repository.

---

## Human-State Packet boundary

The Human-State Packet files are summary objects only.

They are not:

- the body;
- the raw signal;
- the raw voice;
- the raw face;
- the raw gaze stream;
- the raw video;
- the raw transcript;
- a diagnosis;
- a therapy label;
- a psychiatric label;
- a clinical state;
- a human score;
- a truth score;
- a trust score;
- a guilt score;
- a morality score;
- a psychological safety score;
- an employee risk score;
- a relationship verdict;
- a fault assignment;
- a Sal-Meter trace;
- a CAIS compliance record;
- a certification record.

Correct boundary sentence:

```text
A Human-State Packet is a consent-bound, session-scoped, expiring state-summary helper object for interaction adjustment only.
```

---

## Dyadic Session Event boundary

The Dyadic Session Event file represents a synthetic event in a bounded dyadic session.

It may describe:

- consent status;
- packet availability;
- permission status;
- private cue status;
- shared output status;
- participant A bounded state-summary delta;
- participant B bounded state-summary delta;
- dyadic delta;
- recovery gate decision;
- termination gate decision;
- closure reason;
- audit reference.

It must not describe:

- who is right;
- who is wrong;
- who is guilty;
- who is unsafe;
- who is morally better;
- who should be punished;
- who should be ranked;
- who should be monitored;
- who should be diagnosed;
- who should receive therapy;
- a legal mediation decision;
- a relationship verdict;
- a clinical interpretation;
- a production intervention.

Correct boundary sentence:

```text
A Dyadic Session Event describes bounded synthetic session structure, not human truth or relationship judgment.
```

---

## Benchmark Session Container boundary

The Benchmark Session Container connects synthetic packets and events into one public-safe helper package.

It may declare:

- benchmark session ID;
- session ID;
- synthetic status;
- helper benchmark scope;
- helper benchmark stage;
- session type;
- modality stack;
- event schema reference;
- session event references;
- baseline suite status;
- primary helper outcome;
- human-state delta summary;
- dyadic delta summary;
- recovery gate summary;
- termination gate summary;
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

It must not declare:

- benchmark validation;
- scientific validation;
- Sal-Meter validation;
- CAIS compliance;
- mediation validation;
- clinical readiness;
- diagnostic readiness;
- therapeutic readiness;
- counseling readiness;
- surveillance readiness;
- certification readiness;
- device readiness;
- production readiness.

Correct boundary sentence:

```text
A Benchmark Session Container demonstrates helper structure only; it is not benchmark evidence.
```

---

## Public data boundary

This folder may include:

- synthetic JSON examples;
- sample helper structures;
- mock state-summary fields;
- synthetic event references;
- synthetic audit references;
- public boundary declarations;
- schema-aligned helper objects.

This folder must not include:

- raw human data;
- identifiable human data;
- private participant data;
- real dyadic conflict records;
- private consent records;
- raw biosignal files;
- raw ECG;
- raw EEG;
- raw EDA;
- raw PPG;
- raw video;
- raw audio;
- raw face data;
- raw voice data;
- raw gaze streams;
- raw transcripts;
- clinical records;
- diagnostic labels;
- therapeutic interpretations;
- counseling interpretations;
- legal mediation decisions;
- employment eligibility decisions;
- insurance eligibility decisions;
- educational eligibility decisions;
- legal eligibility decisions;
- Sal-Meter raw input;
- CAIS compliance dossiers;
- production feedback logs.

---

## Required boundary flags

Each synthetic helper object should preserve boundary flags equivalent to:

```text
raw_human_data_present == false
identifiable_data_present == false
clinical_data_present == false
diagnostic_claim_present == false
therapeutic_claim_present == false
counseling_claim_present == false
surveillance_claim_present == false
sal_meter_validation_claim_present == false
cais_compliance_claim_present == false
benchmark_validation_claim_present == false
mediation_validation_claim_present == false
production_intervention_claim_present == false
human_ranking_claim_present == false
relationship_verdict_present == false
synthetic_public_data_confirmed == true
```

---

## Validation

A future P3 helper-schema validator may be provided at:

```text
evaluation-baseline/validate_p3_schemas.py
```

Expected validation role:

```text
Validate P3 helper-schema structure only.
```

Expected validation targets:

```text
sample-data/synthetic-dyadic-session-001/human_state_packet_A.json
sample-data/synthetic-dyadic-session-001/human_state_packet_B.json
sample-data/synthetic-dyadic-session-001/dyadic_session_event.json
sample-data/synthetic-dyadic-session-001/benchmark_session_container.json
```

Expected schemas:

```text
schemas/human_state_packet.schema.json
schemas/dyadic_session_event.schema.json
schemas/benchmark_session.schema.json
```

A successful P3 helper-schema validation means only:

```text
The synthetic P3 helper files follow the expected public helper schema structure.
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

## Naming rule

Use:

```text
synthetic
sample
mock
placeholder
structure_only
public helper
helper-schema validation
research-stage
non-clinical
non-diagnostic
non-therapeutic
non-counseling
non-surveillance
non-certification
non-human-ranking
not Sal-Meter
not CAIS compliance
not benchmark validation
not mediation validation
no raw human data
```

Do not use:

```text
validated proxy benchmark
validated human-state benchmark
validated mediation benchmark
validated dyadic recovery system
CAIS-compliant proxy release
Sal-Meter validated
certified proxy benchmark
production mediation system
validated closed-loop intervention
emotion-reading AI
employee monitoring AI
student monitoring AI
relationship scoring system
human quality score
human ranking system
AI harm detector
human-state detector
clinical stress system
diagnostic stress system
therapeutic feedback system
psychological safety score
insurance risk score
legal eligibility score
educational eligibility score
```

---

## Relation to existing synthetic sample package

This folder is separate from:

```text
sample-data/synthetic-session-001/
```

The existing `synthetic-session-001` package demonstrates a single synthetic session package using CSV/JSON helper files.

This folder demonstrates a P3 dyadic helper package using schema-aligned JSON objects.

The two folders should not be merged.

They serve different helper purposes.

---

## Authority rule

This folder is a GitHub helper surface.

It is not a canonical authority layer.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this folder conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

---

## Current status

```text
Synthetic dyadic helper package.
Structure demonstration only.
Not benchmark evidence.
Not scientific validation.
Not mediation validation.
Not Sal-Meter.
Not CAIS compliance.
No raw human data.
No identifiable data.
No clinical data.
No diagnostic label.
No therapeutic claim.
No certification claim.
No production closed-loop claim.
```

---

## Final rule

This package demonstrates structure.

It does not disclose human data.

It does not prove benchmark performance.

It does not validate mediation.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not create diagnostic, therapeutic, clinical, counseling, surveillance, employment, insurance, educational, legal, eligibility, certification, device-readiness, production-deployment, mediation-service, or human-ranking authority.

The packet is not the person.

The event is not the relationship.

The container is not the truth.

The structure is a map.

It is not the mountain.
