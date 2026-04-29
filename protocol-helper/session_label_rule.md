# Session Label Rule

This document defines session label and condition label rules for the **SICS Human-State Proxy Benchmark Track**.

It is a public helper rule document.

It is not the Sal-Meter core signal track.

It does not define CAIS.

It does not grant CAIS compliance.

It does not validate Sal-Meter.

It does not validate benchmark performance.

It does not create diagnostic, therapeutic, clinical, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

---

## Purpose

The purpose of this document is to prevent labels from becoming claims.

Labels are necessary for organizing synthetic/sample sessions and future research-stage benchmark sessions.

Labels are dangerous when they are treated as truth.

This document defines what labels may mean, what labels must not mean, and how labels should be used without leakage, overclaiming, or clinical interpretation.

---

## Core rule

A label is a helper marker.

A label is not a diagnosis.

A label is not a clinical state.

A label is not a psychological truth.

A label is not a consciousness measurement.

A label is not a human ranking.

A label is not Sal-Meter validation.

A label is not CAIS compliance.

Correct sentence:

```text
The label identifies a synthetic/sample or research-stage benchmark condition.
```

Incorrect sentence:

```text
The label proves the participant's human state.
```

---

## Label classes

The proxy benchmark track may use several label classes.

Each class must remain bounded.

```text
session_id              = session identifier
participant_code        = coded or synthetic participant identifier
dataset_type            = dataset boundary class
session_label           = high-level session description
condition_label         = within-session condition marker
event_type              = time/event marker type
target_label            = optional modeling target in a private research setting
public_data_status      = public/private/synthetic boundary marker
```

None of these labels are diagnostic labels.

None of these labels are clinical labels.

None of these labels are Sal-Meter labels.

None of these labels are CAIS compliance labels.

---

## Session ID rule

`session_id` identifies a session package.

For public synthetic/sample files, use a clearly synthetic pattern.

Example:

```text
SYN-SESSION-001
SYN-SESSION-002
SYN-SESSION-003
```

Allowed meaning:

```text
This is a synthetic/sample session identifier.
```

Not allowed meaning:

```text
This identifies a real participant session.
This identifies a clinically meaningful session.
This identifies a validated benchmark session.
```

---

## Participant code rule

`participant_code` must not contain direct identifiers.

Allowed examples:

```text
SYN-PARTICIPANT-001
PSEUDO-P001
CODED-P001
```

Not allowed examples:

```text
real name
email address
phone number
medical record number
birth date
face ID
voice ID
government ID
clinic chart number
```

For public repository materials, participant codes should be synthetic or non-identifying mock codes only.

---

## Dataset type rule

`dataset_type` defines the dataset boundary.

Allowed values for public helper use:

```text
synthetic
sample
sample_structure_only
mock
placeholder
```

Values that require private governance and must not be casually uploaded to this public repository:

```text
private-human
internal-test
pilot-human
lab-human
real-participant
```

If a dataset includes raw human data, identifiable data, clinical data, face data, voice data, or video data, it must not be uploaded to this public repository.

---

## Session label rule

`session_label` describes the high-level session purpose.

Allowed examples for public synthetic/sample use:

```text
synthetic_ai_interaction_demo
synthetic_baseline_demo
synthetic_task_recovery_demo
synthetic_feedback_demo
sample_structure_demo
not_applicable
```

Allowed meaning:

```text
This label describes the public synthetic/sample session structure.
```

Not allowed meaning:

```text
This label proves human-state measurement.
This label proves AI harm.
This label proves clinical stress.
This label proves emotional safety.
This label proves consciousness state.
This label proves Sal-Meter performance.
```

---

## Condition label rule

`condition_label` marks a within-session condition or time window.

Recommended public synthetic/sample values:

```text
synthetic_baseline
synthetic_task_ai_interaction
synthetic_feedback
synthetic_recovery
synthetic_exploratory
not_applicable
```

Allowed meaning:

```text
This condition label identifies a synthetic/sample benchmark window.
```

Not allowed meaning:

```text
This condition label diagnoses a person.
This condition label proves stress.
This condition label proves recovery.
This condition label proves psychological harm.
This condition label proves AI safety.
This condition label proves Sal-Meter validity.
```

---

## Event type rule

`event_type` marks an event or time boundary.

Recommended event types:

```text
session_start
baseline_start
task_start
ai_interaction_start
feedback_event
task_end
recovery_start
session_end
annotation
deviation
```

Allowed meaning:

```text
The event type marks timing or operator context.
```

Not allowed meaning:

```text
The event type proves physiological transition.
The event type proves emotional transition.
The event type proves consciousness transition.
The event type proves therapeutic response.
The event type proves AI causality.
```

---

## Target label rule

`target_label` may exist in private research-stage modeling work.

It must not be treated as a human truth label.

For public synthetic/sample files, target labels should be visibly synthetic, mock, or demonstration-only.

Allowed public examples:

```text
synthetic_baseline
synthetic_task_ai_interaction
synthetic_recovery
synthetic_feedback
mock_class_a
mock_class_b
not_applicable
```

Not allowed public examples:

```text
depressed
anxious
suicidal
safe
unsafe
truthful
lying
manipulated
compliant
noncompliant
fit_for_work
unfit_for_work
high_risk_person
low_value_person
```

Target labels must never become a human-ranking system.

---

## Human-State Cost label boundary

Human-State Cost is a proxy benchmark construct.

It is not a person score.

It is not a diagnosis.

It is not a psychological safety score.

It is not a consciousness score.

It is not a workplace monitoring score.

It is not a legal, insurance, educational, employment, or eligibility score.

Correct sentence:

```text
Human-State Cost is a bounded proxy construct for comparing interaction conditions.
```

Incorrect sentence:

```text
Human-State Cost measures the value, truth, health, safety, or consciousness level of a person.
```

---

## Dyadic and mediation label boundary

Future dyadic or mediation-related labels may be defined only as long-term research-stage benchmark helper labels.

They must not be used as:

```text
legal mediation labels
therapy labels
counseling labels
relationship diagnosis labels
fault attribution labels
who-is-right labels
conflict blame labels
risk-to-others labels
fitness labels
eligibility labels
surveillance labels
```

Allowed future direction:

```text
dyadic_simulation_demo
synthetic_conflict_scenario
synthetic_mediation_output_a
synthetic_mediation_output_b
synthetic_recovery_window
not_applicable
```

Allowed meaning:

```text
The label marks a synthetic or low-risk simulated interaction condition for benchmark structure.
```

Not allowed meaning:

```text
The label decides who is right.
The label diagnoses the relationship.
The label provides legal mediation.
The label provides therapy.
The label ranks people.
```

---

## Public label visibility rule

Public synthetic/sample packages may expose labels visibly for demonstration clarity.

For example:

```text
labels_visible_for_demo: true
```

This is allowed only because the public sample package is synthetic.

In real benchmark work, visible labels may cause leakage.

Therefore, real benchmark packages must control whether labels are visible to:

```text
model training code
feature extraction code
operator logs
file names
folder names
session ordering
metadata fields
dashboard views
public releases
```

A public demo may show structure.

A real benchmark must prevent leakage.

---

## Leakage rule

Labels must not leak through:

```text
file names
folder names
session order
participant IDs
operator IDs
device IDs
condition labels
timestamp artifacts
preprocessing artifacts
manual notes
dashboard fields
release notes
public sample names
```

Bad examples:

```text
participant_001_stressed.csv
session_002_recovery_success.csv
task_high_conflict_subject_A.json
safe_user_group_features.csv
clinical_anxiety_label.csv
```

Better examples:

```text
session_001_features.csv
session_002_features.csv
split_train.csv
split_test.csv
event_markers.csv
labels_private.csv
```

For public synthetic/sample packages, labels may be visible only because the package is explicitly synthetic and marked as structure demonstration.

---

## Label placement rule

Labels should be placed in dedicated label files or clearly defined metadata fields.

Recommended structure:

```text
sample-data/
  synthetic-session-001/
    session_metadata.json
    events.csv
    labels.csv
    splits.json
```

Recommended principle:

```text
Labels should be visible enough for audit, but not accidentally embedded in features.
```

Labels must not be hidden inside:

```text
feature column names
raw signal file names
device names
operator names
participant codes
timestamps
folder names
model artifact names
```

---

## Label naming style

Use lowercase snake_case where possible.

Recommended:

```text
synthetic_baseline
synthetic_task_ai_interaction
synthetic_feedback
synthetic_recovery
sample_structure_only
not_applicable
```

Avoid:

```text
StressDetected
RealAnxiety
TrueConsciousness
SafeEmployee
BadUser
PatientRisk
ValidatedState
CAISCompliant
SalMeterPositive
```

Naming should reduce claim inflation.

A label name should not smuggle a conclusion.

---

## Allowed language

Use:

```text
session label
condition label
event marker
synthetic label
sample label
helper label
non-diagnostic label
research-stage label
benchmark-support label
structure demonstration label
proxy construct label
```

Do not use:

```text
diagnostic label
clinical label
therapeutic label
validated state
certified class
consciousness label
truth label
human value label
psychological safety label
employee score
eligibility score
CAIS-compliant label
Sal-Meter validation label
```

---

## Label review checklist

Before adding or modifying labels, check:

```text
[ ] Does the label avoid clinical language?
[ ] Does the label avoid diagnostic language?
[ ] Does the label avoid therapeutic language?
[ ] Does the label avoid surveillance language?
[ ] Does the label avoid person-ranking language?
[ ] Does the label avoid Sal-Meter validation claims?
[ ] Does the label avoid CAIS compliance claims?
[ ] Does the label avoid certification language?
[ ] Is the label clearly synthetic/sample when used publicly?
[ ] Could the label leak through filenames, folders, timestamps, or metadata?
[ ] Is the label necessary for structure, audit, or reproducibility?
```

If the label creates more claim risk than audit value, do not use it.

---

## Example: acceptable public synthetic label file

```csv
label_id,session_id,window_label,label_value,label_source,public_data_status,note
SYN-LBL-001,SYN-SESSION-001,synthetic_baseline,0,synthetic,synthetic,Structure demonstration only.
SYN-LBL-002,SYN-SESSION-001,synthetic_task_ai_interaction,1,synthetic,synthetic,Structure demonstration only.
SYN-LBL-003,SYN-SESSION-001,synthetic_recovery,0,synthetic,synthetic,Structure demonstration only.
```

This is acceptable only because it is clearly synthetic.

It must not be described as benchmark evidence.

---

## Example: unacceptable label file

```csv
participant_id,diagnosis,truth_score,employee_safety_score,cais_status,sal_meter_validated
P001,anxiety,0.91,unsafe,compliant,true
```

This is not allowed.

It creates diagnostic, human-ranking, CAIS compliance, and Sal-Meter validation claims.

---

## Relationship to schemas

This rule document complements schema files such as:

```text
schemas/labels.schema.json
schemas/session-metadata.schema.json
schemas/event-markers.schema.json
schemas/splits.schema.json
```

The schemas check structure.

This document explains meaning boundaries.

Neither the schemas nor this document validate benchmark performance.

Neither the schemas nor this document validate Sal-Meter.

Neither the schemas nor this document grant CAIS compliance.

---

## Relationship to sample data

Public sample data should use labels only to demonstrate structure.

Correct interpretation:

```text
The public synthetic label demonstrates how a label field may be represented.
```

Incorrect interpretation:

```text
The public synthetic label proves that the system can detect a human state.
```

Public sample data is a map.

It is not the territory.

---

## Relationship to evaluation baseline

Evaluation baseline code may load labels for toy processing.

That does not mean the label is scientifically valid.

That does not mean the model is reliable.

That does not mean the benchmark is validated.

That does not mean Sal-Meter works.

That does not mean CAIS compliance exists.

Correct interpretation:

```text
The baseline code demonstrates how labels may be loaded and split in a leakage-aware way.
```

Incorrect interpretation:

```text
The baseline code proves that the label captures a true human state.
```

---

## Future private benchmark rule

If future private human-subject data are collected, label governance must be stricter than public synthetic examples.

At minimum, future private benchmark work must define:

```text
label source
label timing
label visibility
label masking
label access control
label audit trail
label leakage review
label revision history
label dispute process
label release boundary
```

Private labels must not be published casually.

Raw human data and identifiable labels must not be uploaded to this public repository.

---

## Prohibited label uses

Labels must not be used for:

```text
medical diagnosis
psychiatric diagnosis
clinical triage
therapy selection
legal judgment
employment decision
insurance decision
educational eligibility
credit scoring
surveillance scoring
human ranking
truth detection
policing
disciplinary action
relationship blame assignment
certification claim
CAIS compliance claim
Sal-Meter validation claim
```

This repository does not create such authority.

---

## P2-1 issue alignment

This file implements:

```text
[P2-1] Add protocol helper boundary pack
```

It satisfies:

```text
Create protocol-helper/session_label_rule.md
```

---

## Completion status

```text
Protocol helper file.
Session label rule.
Research-stage.
Public helper documentation only.
Non-diagnostic labels only.
Not benchmark evidence.
Not Sal-Meter.
Not CAIS compliance.
No raw human data.
No identifiable data.
No clinical authority.
No diagnostic authority.
No therapeutic authority.
No surveillance authority.
No certification authority.
No human-ranking authority.
```

---

## Final rule

A label must help audit structure.

A label must not become a verdict.

A label must not become a diagnosis.

A label must not become a person score.

A label must not become a compliance mark.

A label must not pretend to be Sal-Meter.

A label must not turn a proxy benchmark into a human judgment machine.

If a label cannot remain bounded, do not use it.
