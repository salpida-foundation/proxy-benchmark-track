# P3 Dyadic Recovery Synthetic Cases

This folder contains synthetic public-helper examples for P3 dyadic recovery case distinction.

These cases are designed to make the following distinctions visible:

- true recovery is not just agreement;
- true recovery is not just silence;
- true recovery is not just politeness;
- true recovery is not just synchrony;
- asymmetric recovery means one side may appear improved while the other becomes more burdened, exposed, silenced, or destabilized;
- false recovery includes silence-as-recovery risk;
- false recovery includes compliance under pressure;
- false recovery includes session closure being mistaken for recovery;
- unresolved or insufficient data must not be forced into recovery.

---

## Planned case folders

```text
sample-data/p3-dyadic-recovery-cases/
  true-recovery-candidate/
  asymmetric-recovery/
  false-recovery-silence-risk/
```

Optional later folders:

```text
sample-data/p3-dyadic-recovery-cases/
  deterioration/
  unresolved-insufficient-data/
```

---

## Required files per case

Each case folder should include:

```text
baseline_packet_A.json
baseline_packet_B.json
ai_output.json
post_output_packet_A.json
post_output_packet_B.json
dyadic_recovery_event.json
audit_log.json
README.md
```

---

## Public boundary

These files are synthetic public-helper examples only.

They do not contain raw human data.

They do not contain identifiable human data.

They do not contain real participant data.

They do not contain real dyadic conflict records.

They do not contain real session records.

They do not contain real phone recordings.

They do not contain real transcripts.

They do not contain clinical records.

They do not create diagnostic labels.

They do not create therapeutic recommendations.

They do not create counseling notes.

They do not create relationship verdicts.

They do not create human scores.

They do not contain Sal-Meter raw traces.

They do not contain CAIS traces.

They do not grant CAIS compliance.

They do not validate real dyadic recovery.

They do not validate mediation effectiveness.

They do not validate human-state measurement.

They do not validate termination-gate accuracy.

They do not create device readiness.

They do not create production readiness.

They do not create certification.

---

## P3 interpretation boundary

P3 is a research-stage proxy gate for distinguishing recovery, deterioration, asymmetric recovery, false recovery, and unresolved cases after an AI output.

P3 does not diagnose emotion.

P3 does not score persons.

P3 does not monitor employees.

P3 does not create relationship verdicts.

P3 does not validate mediation.

P3 does not validate clinical, therapeutic, surveillance, device, or production systems.

---

## Current status

This folder is the parent index for P3 dyadic recovery synthetic cases.

The required case folders will be added in follow-up commits.
