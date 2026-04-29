# Future Sal-Meter A/B Comparison Rule

This document defines the future A/B comparison boundary between the **SICS Human-State Proxy Benchmark Track** and future **Sal-Meter core signal inputs**.

It is a public helper rule document.

It is not the Sal-Meter core signal track.

It does not define CAIS.

It does not grant CAIS compliance.

It does not validate Sal-Meter.

It does not validate benchmark performance.

It does not open Sal-Meter inputs for public use.

It does not create diagnostic, therapeutic, clinical, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

---

## Purpose

The purpose of this document is to prevent future comparison language from becoming premature validation.

The proxy benchmark track may later provide a comparison surface for Sal-Meter core signal inputs.

That future comparison is not active in this repository.

This document defines what future A/B comparison may mean, what it must not mean, and which boundaries must remain locked before any comparison is described publicly.

---

## Core rule

A/B comparison means comparing two bounded signal or benchmark streams under a documented structure.

A/B comparison does not mean validation.

A/B comparison does not mean diagnosis.

A/B comparison does not mean device readiness.

A/B comparison does not mean CAIS compliance.

A/B comparison does not mean Sal-Meter has been validated.

A/B comparison does not mean Human-State Cost is a human truth score.

Correct sentence:

```text
Future Sal-Meter A/B comparison may compare proxy benchmark streams with Sal-Meter core inputs under a separate bounded comparison design.
```

Incorrect sentence:

```text
This repository validates Sal-Meter by comparing proxy data with Sal-Meter data.
```

---

## Current status

Current status:

```text
Future comparison boundary only.
No Sal-Meter input in this repository.
No CAIS compliance claim.
No benchmark validation claim.
No clinical claim.
No diagnostic claim.
No therapeutic claim.
No surveillance claim.
No certification claim.
No human-ranking claim.
```

This repository currently provides:

```text
proxy benchmark helper structure
public synthetic/sample package
schemas
metadata discipline
leakage-safe evaluation skeletons
protocol helper rules
dashboard and closed-loop planning boundaries
future comparison preparation language
```

It does not provide:

```text
Sal-Meter core signal data
I-channel data
G-channel data
CAIS compliance output
clinical output
validated benchmark output
human-subject raw data
diagnostic labels
therapeutic feedback
device certification
```

---

## Two-track separation

The project must maintain two separate tracks.

```text
Track A: Sal-Meter core signal track
Track B: Proxy benchmark track
```

Track A is the Sal-Meter core signal track.

Track B is the proxy benchmark track.

Track B does not become Track A.

Track B does not replace Track A.

Track B does not validate Track A.

Track B may later provide comparison context for Track A only if Track A inputs become available under separate bounded governance.

---

## Sal-Meter core signal track boundary

The Sal-Meter core signal track concerns future molecular/electrochemical core inputs.

It is separate from this proxy benchmark repository.

This repository does not contain:

```text
Sal-Meter raw signal traces
Sal-Meter processed signal outputs
I-channel signal data
G-channel signal data
aptamer signal data
electrochemical core signal files
human pilot Sal-Meter files
CAIS compliance packages
Sal-Meter device readiness packages
```

If such data exist in the future, they must be handled under a separate private or governed data boundary.

They must not be casually uploaded to this public helper repository.

---

## Proxy benchmark track boundary

The proxy benchmark track concerns synchronized multimodal benchmark infrastructure.

It may include or plan for:

```text
ECG
HRV
EDA
PPG
EEG
eye tracking
gaze
webcam-derived proxy features
AI interaction logs
simulator events
operator markers
metadata schemas
leakage-safe split examples
baseline model skeletons
dashboard mockups
closed-loop demo-lite placeholders
```

These are proxy benchmark components.

They are not Sal-Meter.

They are not CAIS compliance.

They are not clinical outputs.

They are not diagnostic outputs.

They are not human truth measurements.

---

## Future A/B comparison definition

For this repository, future A/B comparison means:

```text
A bounded research-stage comparison between proxy benchmark fields and future Sal-Meter core input fields, using shared session windows, shared event markers, documented metadata, leakage review, and audit trail.
```

It does not mean:

```text
clinical validation
device validation
CAIS compliance
Sal-Meter certification
consciousness measurement validation
diagnostic validation
therapeutic validation
surveillance readiness
human-ranking authority
```

---

## A-side and B-side terminology

Recommended terminology:

```text
A-side = proxy benchmark stream
B-side = future Sal-Meter core input stream
```

Alternative wording:

```text
proxy-side
core-side
```

Avoid wording that implies validation:

```text
validated side
true side
ground truth side
diagnostic side
certified side
official CAIS side
human truth side
```

Neither side should be described as ground truth without separate canonical justification.

---

## Current allowed A-side examples

Allowed current A-side examples in this public repository:

```text
synthetic HRV-like feature
synthetic EDA-like feature
synthetic interaction latency
synthetic event marker
synthetic label window
synthetic Human-State Cost proxy field
synthetic split file
synthetic QC report
toy baseline model output
```

Allowed interpretation:

```text
These fields demonstrate helper structure for the proxy benchmark track.
```

Not allowed interpretation:

```text
These fields prove human-state measurement.
```

---

## Future B-side placeholder examples

Future B-side placeholders may be described only as placeholders.

Allowed placeholder language:

```text
future Sal-Meter core input
future I-channel input
future G-channel input
future Sal-Meter comparison field
future bounded core-side signal field
not currently present
not publicly released
not validated here
```

Not allowed placeholder language:

```text
validated Sal-Meter input
CAIS-compliant signal
certified signal
official consciousness signal
diagnostic Sal-Meter result
therapeutic signal
human truth signal
```

A placeholder is a doorframe.

It is not the room.

---

## Required future comparison prerequisites

Future A/B comparison must not be described as active until the following are present:

```text
documented Sal-Meter core input boundary
proxy-side data boundary
shared session ID rule
shared event marker rule
timestamp synchronization rule
metadata completeness rule
label visibility rule
leakage review rule
raw data handover boundary
public/private data boundary
QC report rule
audit trail rule
comparison report boundary
publication boundary
claims and terminology review
```

If any of these are missing, comparison remains only a future design boundary.

---

## Required comparison metadata

Any future A/B comparison package must include metadata for both sides.

Recommended metadata fields:

```text
comparison_id
comparison_status
comparison_date
dataset_type
public_data_status
proxy_session_id
sal_meter_session_id
shared_session_id
shared_event_marker_id
proxy_streams_present
sal_meter_inputs_present
timestamp_source_proxy
timestamp_source_sal_meter
sync_method
known_offset_ms
drift_reviewed
dropout_reviewed
latency_reviewed
label_visibility
leakage_reviewed
split_strategy
holdout_strategy
raw_human_data_present
identifiable_data_present
clinical_data_present
diagnostic_claim_present
therapeutic_claim_present
surveillance_claim_present
certification_claim_present
human_ranking_claim_present
sal_meter_validation_claim_present
cais_compliance_claim_present
final_boundary
```

Metadata makes comparison reviewable.

Metadata does not make comparison valid.

---

## Required boundary booleans

A future public helper comparison record must keep boundary fields explicit.

For this repository, required values remain:

```json
{
  "raw_human_data_present": false,
  "identifiable_data_present": false,
  "clinical_data_present": false,
  "diagnostic_claim_present": false,
  "therapeutic_claim_present": false,
  "surveillance_claim_present": false,
  "certification_claim_present": false,
  "human_ranking_claim_present": false,
  "sal_meter_validation_claim_present": false,
  "cais_compliance_claim_present": false
}
```

If any value becomes `true`, the file does not belong in this public helper repository without separate governance.

---

## Public repository exclusion rule

Do not upload the following to this public repository:

```text
raw Sal-Meter signal data
raw I-channel signal data
raw G-channel signal data
raw human biosignals
raw human video
raw human audio
face data
voice data
identifiable participant metadata
private session logs
clinical records
health records
consent forms containing personal information
internal lab human-subject packages
CAIS compliance dossiers
device validation dossiers
unpublished human-subject data
```

This repository is a helper surface.

It is not a raw data vault.

---

## Shared session ID rule

Future A/B comparison requires a shared session mapping rule.

Recommended fields:

```text
proxy_session_id
sal_meter_session_id
shared_session_id
mapping_method
mapping_reviewed
mapping_note
```

Allowed meaning:

```text
The proxy-side and core-side records are mapped for review.
```

Not allowed meaning:

```text
The mapping proves that the two systems measure the same true human state.
```

Mapping is alignment.

Mapping is not validation.

---

## Shared event marker rule

Future A/B comparison requires shared event markers.

Recommended fields:

```text
shared_event_marker_id
event_type
event_timestamp_proxy
event_timestamp_sal_meter
event_source
known_offset_ms
offset_correction_applied
sync_quality_flag
event_note
```

Allowed meaning:

```text
The event marker supports cross-stream timing comparison.
```

Not allowed meaning:

```text
The event marker proves physiological, psychological, AI, therapeutic, or consciousness causality.
```

---

## Timestamp synchronization rule

Future A/B comparison must follow:

```text
protocol-helper/timestamp_sync_rule.md
```

Minimum requirements:

```text
clock source declared
timestamp format declared
timezone convention declared
sync method declared
known offset documented
drift reviewed
dropout reviewed
latency reviewed
deviation logged
```

Timestamp synchronization supports audit.

Timestamp synchronization does not validate Sal-Meter.

Timestamp synchronization does not validate the proxy benchmark.

Timestamp synchronization does not prove causality.

---

## Metadata completeness rule

Future A/B comparison must follow:

```text
protocol-helper/metadata_completeness_rule.md
```

Minimum requirements:

```text
required fields present
required files present
schema version declared
public/private boundary declared
raw data boundary declared
label boundary declared
leakage review declared
QC status declared
authority boundary declared
```

Metadata completeness supports review.

Metadata completeness does not prove validity.

---

## Session label rule

Future A/B comparison must follow:

```text
protocol-helper/session_label_rule.md
```

Labels must remain bounded.

Labels must not become:

```text
diagnosis
clinical state
therapeutic state
truth label
consciousness label
human ranking
CAIS compliance marker
Sal-Meter validation marker
```

Labels may mark windows.

Labels must not judge people.

---

## Human-State Cost construct rule

Future A/B comparison may reference:

```text
protocol-helper/human_state_cost_construct_note.md
```

Human-State Cost may be used as a proxy-side construct.

It must not be used as:

```text
person score
clinical score
diagnostic score
therapeutic score
surveillance score
certification score
CAIS score
Sal-Meter score
consciousness score
```

Correct sentence:

```text
Human-State Cost may serve as a proxy-side comparison construct.
```

Incorrect sentence:

```text
Human-State Cost validates Sal-Meter.
```

---

## Comparison matrix structure

A future A/B comparison matrix may use this conceptual structure:

```text
comparison_id
shared_session_id
window_label
proxy_feature_set
proxy_human_state_cost_field
future_sal_meter_input_field
sync_quality_flag
metadata_complete
leakage_reviewed
qc_status
comparison_note
```

This is a structure.

It is not a result.

It is not validation.

---

## Example future comparison row

Acceptable placeholder example:

```csv
comparison_id,shared_session_id,window_label,proxy_feature_set,future_sal_meter_input_field,sync_quality_flag,metadata_complete,leakage_reviewed,comparison_note
SYN-COMP-001,SYN-SESSION-001,synthetic_task_ai_interaction,synthetic_proxy_features,future_sal_meter_input_placeholder,review,true,true,Future placeholder only. No Sal-Meter data present.
```

Allowed interpretation:

```text
This row demonstrates future comparison structure.
```

Not allowed interpretation:

```text
This row compares real proxy data with validated Sal-Meter data.
```

---

## Placeholder rule

Placeholder fields must be visibly labeled.

Use:

```text
placeholder
future_placeholder
not_present
not_applicable
not_public
future_sal_meter_input_placeholder
```

Do not use:

```text
validated_signal
official_signal
ground_truth
certified_input
CAIS_compliant_input
SalMeter_validated
```

A placeholder must not masquerade as data.

---

## Ground truth rule

Do not call Sal-Meter input `ground truth` unless a separate canonical governance record explicitly authorizes that term.

Do not call proxy benchmark output `ground truth`.

Do not call Human-State Cost `ground truth`.

Avoid:

```text
truth signal
human truth
consciousness truth
validated state
true state label
```

Use:

```text
comparison field
proxy-side field
core-side field
bounded input
research-stage signal candidate
```

Truth is not declared by naming.

Truth is earned by evidence.

---

## Validation boundary

A future A/B comparison may support validation work.

It does not automatically validate anything.

Validation would require separate evidence such as:

```text
predefined hypothesis
locked analysis plan
raw data package
metadata completeness
repeatability
independent review
leakage control
holdout protection
negative control logic
cross-session stability
cross-site reproducibility where applicable
claims review
publication boundary review
```

This repository does not currently provide that validation.

---

## Correlation boundary

A correlation between proxy-side fields and future Sal-Meter inputs would not prove validation by itself.

Correct sentence:

```text
The comparison reports an observed association between proxy-side and core-side fields under bounded conditions.
```

Incorrect sentence:

```text
The correlation proves Sal-Meter measures consciousness.
```

Correlation is a clue.

Correlation is not a crown.

---

## Agreement boundary

Agreement between proxy-side and future Sal-Meter-side fields would not prove clinical or diagnostic validity.

Correct sentence:

```text
The two streams show agreement under the defined comparison window.
```

Incorrect sentence:

```text
The two streams confirm the participant's true human state.
```

Agreement is not diagnosis.

Agreement is not CAIS compliance.

Agreement is not certification.

---

## Disagreement boundary

Disagreement between proxy-side and future Sal-Meter-side fields must not be treated as failure without analysis.

Possible meanings include:

```text
proxy construct limitation
core signal limitation
timestamp mismatch
label mismatch
window mismatch
metadata gap
drift
dropout
leakage
operator error
condition instability
unknown cause
```

Disagreement is information.

It is not shame.

Negative results may be structurally useful.

---

## Leakage boundary

Future A/B comparison is vulnerable to leakage.

Leakage may occur through:

```text
shared session IDs
file names
folder names
event order
timestamp patterns
condition labels
operator notes
device batch effects
split design
dashboard display
release notes
public sample naming
```

Required review:

```text
session leakage reviewed
timestamp leakage reviewed
label leakage reviewed
operator leakage reviewed
device leakage reviewed
split leakage reviewed
dashboard leakage reviewed
release leakage reviewed
```

A comparison that leaks is not evidence.

---

## Holdout boundary

Future A/B comparison must protect holdout data.

Recommended split structure:

```text
training
validation
test
holdout
public synthetic sample
private restricted data
```

Holdout data must not be used for:

```text
feature selection
threshold tuning
label adjustment
posthoc narrative optimization
dashboard tuning
claim strengthening
```

A holdout seen too early is no longer a holdout.

---

## Raw data handover boundary

Future A/B comparison requires a raw data handover rule.

Minimum package:

```text
raw proxy stream inventory
raw Sal-Meter stream inventory, if available
processed file inventory
event marker inventory
metadata package
QC report
operator log
deviation log
split file
analysis script
environment note
readme boundary note
```

Raw data handover does not mean public release.

Private human data must remain under private governance.

---

## Public release boundary

Future A/B comparison reports must not publish raw human data in this public repository.

Public releases may include:

```text
synthetic examples
sample-structure files
redacted schemas
boundary notes
non-sensitive helper documentation
mock dashboard fields
toy validation logs
public release notes
```

Public releases must not include:

```text
identifiable data
raw human data
clinical data
private Sal-Meter data
private proxy data
participant-level raw files
consent files with personal information
medical records
```

Public clarity is not public exposure.

---

## Dashboard boundary

Future dashboards may display A/B comparison only as bounded helper visualization.

Required dashboard disclaimer:

```text
Research-stage proxy/core comparison view.
Not diagnostic.
Not clinical.
Not therapeutic.
Not surveillance.
Not certification.
Not CAIS compliance.
Not Sal-Meter validation.
Not human ranking.
```

A dashboard can make weak evidence look strong.

This repository must not do that.

---

## Closed-loop boundary

Future closed-loop demo-lite work must not use A/B comparison as therapy or control.

Allowed wording:

```text
A future demo-lite may use bounded comparison fields to demonstrate non-coercive interaction adjustment logic.
```

Not allowed wording:

```text
The system uses Sal-Meter comparison to treat, diagnose, control, discipline, monitor, or rank people.
```

Closed-loop does not mean clinical loop.

Closed-loop does not mean surveillance loop.

Closed-loop does not mean therapeutic loop.

---

## Dyadic and mediation boundary

Future dyadic or mediation use must remain bounded.

A/B comparison must not decide:

```text
who is right
who is wrong
who caused harm
who is unsafe
who is more conscious
who is truthful
who should be monitored
who should be punished
who should receive therapy
```

Allowed wording:

```text
A future dyadic simulation may compare proxy-side interaction burden fields with future core-side signal fields under a bounded research-stage design.
```

Not allowed wording:

```text
The system determines who is responsible for the conflict.
```

---

## Clinical boundary

Future A/B comparison must not be described as clinical.

Do not use:

```text
patient validation
clinical validation
clinical diagnosis
clinical endpoint
treatment response
symptom improvement
clinical recovery
medical decision support
```

Use:

```text
research-stage comparison
non-clinical comparison
proxy/core comparison
helper-structure comparison
bounded benchmark comparison
```

---

## Diagnostic boundary

Future A/B comparison must not be described as diagnostic.

Do not use:

```text
diagnostic accuracy
diagnostic label
diagnostic endpoint
mental health diagnosis
stress diagnosis
anxiety detection
depression detection
psychiatric screening
```

Use:

```text
non-diagnostic proxy comparison
research-stage condition comparison
synthetic/sample comparison field
```

---

## Therapeutic boundary

Future A/B comparison must not be described as therapeutic.

Do not use:

```text
therapy effect
treatment effect
recovery intervention
healing score
clinical feedback
therapeutic feedback
intervention efficacy
```

Use:

```text
non-therapeutic interaction comparison
research-stage feedback-window comparison
demo-lite interaction adjustment boundary
```

---

## Surveillance boundary

Future A/B comparison must not be described as surveillance.

Do not use:

```text
employee monitoring
student monitoring
citizen monitoring
compliance scoring
risk scoring
disciplinary signal
threat detection
behavioral policing
```

Use:

```text
non-surveillance benchmark helper
bounded interaction-condition comparison
research-stage proxy/core comparison
```

---

## Certification boundary

Future A/B comparison must not be described as certification.

Do not use:

```text
certified benchmark
validated commercial device
approved metric
CAIS-certified
CAIS-compliant output
Sal-Meter validated output
official compliance result
```

Use:

```text
release-readiness helper
research-stage comparison design
future comparison placeholder
non-certification public helper
```

---

## Naming rule

Use:

```text
future Sal-Meter A/B comparison
proxy/core comparison
proxy-side field
future core-side input
bounded comparison design
research-stage comparison helper
future comparison placeholder
```

Do not use:

```text
validated Sal-Meter comparison
CAIS-compliant comparison
certified consciousness comparison
diagnostic comparison
clinical comparison
therapeutic comparison
ground-truth comparison
human truth comparison
```

Naming is a gate.

Bad names become bad claims.

---

## Required public note

Any public mention of future A/B comparison should include:

```text
Future comparison only.
No Sal-Meter input is present in this repository.
No CAIS compliance is granted.
No benchmark validation is claimed.
No diagnostic, clinical, therapeutic, surveillance, certification, or human-ranking authority is created.
```

This note is not decoration.

It is the guardrail.

---

## Future comparison report minimum structure

A future comparison report, if created under proper governance, should include:

```text
1. Scope
2. Data boundary
3. Proxy-side fields
4. Sal-Meter-side fields
5. Shared event markers
6. Timestamp synchronization
7. Metadata completeness
8. Label boundary
9. Leakage review
10. Split and holdout design
11. QC report
12. Negative control or limitation notes
13. Result summary
14. Claims boundary
15. Public release boundary
```

A report without boundary is not ready.

---

## Go / Hold rule

Future comparison language should follow this decision logic:

```text
GO:
  Use only as future comparison structure when boundaries are explicit.

CONDITIONAL GO:
  Use for private research planning if data rights, metadata, leakage, raw data, and claims boundary are locked.

HOLD:
  Do not publish comparison claims if Sal-Meter inputs are absent, Actions validation is blocked, metadata are incomplete, leakage review is missing, or raw/private data boundaries are unclear.

NO-GO:
  Do not claim validation, diagnosis, therapy, surveillance, certification, CAIS compliance, Sal-Meter validation, or human ranking.
```

---

## Relationship to protocol helper files

This file complements:

```text
protocol-helper/session_label_rule.md
protocol-helper/timestamp_sync_rule.md
protocol-helper/metadata_completeness_rule.md
protocol-helper/human_state_cost_construct_note.md
```

Together, these files define helper rules.

They do not validate benchmark performance.

They do not validate Sal-Meter.

They do not grant CAIS compliance.

---

## Relationship to schemas

This file complements:

```text
schemas/
```

Schemas may check structure.

Schemas do not validate comparison.

Schemas do not validate Sal-Meter.

Schemas do not grant CAIS compliance.

Schemas do not create scientific evidence.

Correct interpretation:

```text
The schema helps check whether comparison-related fields follow expected structure.
```

Incorrect interpretation:

```text
The schema proves that the comparison validates Sal-Meter.
```

---

## Relationship to sample data

This file complements:

```text
sample-data/
```

Public sample data may show future comparison placeholders.

Public sample data must not contain real Sal-Meter input.

Public sample data must not contain raw human data.

Public sample data must not be described as A/B evidence.

Correct interpretation:

```text
The public sample package demonstrates how future comparison fields may be represented.
```

Incorrect interpretation:

```text
The public sample package already compares proxy data with Sal-Meter data.
```

---

## Relationship to evaluation baseline

This file complements:

```text
evaluation-baseline/
```

Evaluation baseline scripts may later include placeholder comparison hooks.

Those hooks must remain helper-structure only.

They must not claim:

```text
benchmark validation
Sal-Meter validation
CAIS compliance
clinical validation
diagnostic validation
therapeutic validation
surveillance readiness
certification readiness
human ranking
```

---

## Relationship to root README

The root README should describe this repository as:

```text
research-stage proxy benchmark helper repository
future comparison preparation only
not Sal-Meter
not CAIS compliance
not benchmark validation
no raw human data
```

If root README language conflicts with this file, the stricter boundary should be used.

---

## Relationship to canonical authority

This GitHub repository is a helper surface.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this file conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

This file does not reinterpret canonical authority.

This file only documents public helper boundaries for future comparison.

---

## Review checklist

Before adding future A/B comparison content, check:

```text
[ ] Is it clearly marked as future comparison only?
[ ] Is it clear that no Sal-Meter input is currently present?
[ ] Is it clear that this repository is not the Sal-Meter core signal track?
[ ] Is it clear that the proxy track does not replace Sal-Meter?
[ ] Is CAIS compliance explicitly not claimed?
[ ] Is Sal-Meter validation explicitly not claimed?
[ ] Is benchmark validation explicitly not claimed?
[ ] Is raw human data excluded?
[ ] Is identifiable data excluded?
[ ] Is clinical data excluded?
[ ] Is diagnostic language avoided?
[ ] Is therapeutic language avoided?
[ ] Is surveillance language avoided?
[ ] Is certification language avoided?
[ ] Is human-ranking language avoided?
[ ] Are labels bounded?
[ ] Are timestamps bounded?
[ ] Is metadata completeness required?
[ ] Is leakage review required?
[ ] Is holdout protection required for future real comparison?
[ ] Is public/private data boundary clear?
[ ] Is DOI/canonical authority boundary preserved?
```

If the answer is uncertain, hold the claim.

---

## Acceptable public placeholder example

```text
Future Sal-Meter A/B comparison is not active in this repository.

This repository prepares proxy-side helper structure only.

If future Sal-Meter core inputs become available under separate governance, they may be compared against proxy-side benchmark fields using shared event markers, timestamp synchronization, metadata completeness, leakage review, QC reports, and claims-boundary review.

Such comparison would not automatically validate Sal-Meter, grant CAIS compliance, create clinical authority, or create human-ranking authority.
```

---

## Unacceptable public claim example

```text
This repository proves Sal-Meter works by comparing proxy data with Sal-Meter data.

The comparison validates CAIS compliance and can be used for clinical, diagnostic, therapeutic, safety, employment, and certification decisions.
```

This is not allowed.

It creates premature validation, CAIS compliance, clinical, diagnostic, therapeutic, surveillance, certification, and human-ranking claims.

---

## P2-1 issue alignment

This file implements:

```text
[P2-1] Add protocol helper boundary pack
```

It satisfies:

```text
Create protocol-helper/future_sal_meter_ab_comparison_rule.md
```

---

## Completion status

```text
Protocol helper file.
Future Sal-Meter A/B comparison rule.
Research-stage.
Public helper documentation only.
Future comparison boundary only.
No active Sal-Meter comparison.
No Sal-Meter input in this repository.
Not benchmark evidence.
Not Sal-Meter validation.
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

Future comparison may prepare the bridge.

It must not pretend the bridge has already been crossed.

Proxy data may become a mirror.

Sal-Meter input may become a separate signal.

A mirror and a signal may one day be compared.

But comparison is not coronation.

The gate stays closed until evidence, metadata, leakage control, audit trail, and claims boundary open it properly.
