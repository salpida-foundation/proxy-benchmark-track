# Timestamp Sync Rule

This document defines timestamp and synchronization rules for the **SICS Human-State Proxy Benchmark Track**.

It is a public helper rule document.

It is not the Sal-Meter core signal track.

It does not define CAIS.

It does not grant CAIS compliance.

It does not validate Sal-Meter.

It does not validate benchmark performance.

It does not create diagnostic, therapeutic, clinical, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

---

## Purpose

The purpose of this document is to prevent timestamps from becoming claims.

Timestamps are necessary for organizing multimodal proxy benchmark structure.

Timestamps are dangerous when they are treated as proof of physiological causality, psychological causality, consciousness transition, AI causality, therapeutic response, or clinical state.

This document defines how timestamps, event markers, clock sources, synchronization methods, drift notes, and alignment fields should be used in a bounded research-stage helper repository.

---

## Core rule

A timestamp is an alignment marker.

A timestamp is not physiology.

A timestamp is not causality.

A timestamp is not diagnosis.

A timestamp is not recovery.

A timestamp is not harm.

A timestamp is not consciousness transition.

A timestamp is not Sal-Meter validation.

A timestamp is not CAIS compliance.

Correct sentence:

```text
The timestamp marks when an event, window, sample, or annotation was recorded or aligned.
```

Incorrect sentence:

```text
The timestamp proves that the AI system caused a human-state change.
```

---

## Recommended timestamp format

For public synthetic/sample files, use an explicit ISO 8601 UTC-like format where possible:

```text
YYYY-MM-DDTHH:MM:SSZ
```

Example:

```text
2026-04-28T09:00:00Z
```

For synthetic/sample data, this timestamp may be fictional.

If local time is used, the convention must be documented.

Avoid ambiguous timestamps such as:

```text
04/28/26 9:00
9 AM
2026.4.28
28-04-2026
morning baseline
after task
during recovery
```

Ambiguous time is weak metadata.

Weak metadata becomes weak evidence.

---

## Public synthetic timestamp rule

Public sample timestamps may be synthetic.

If timestamps are synthetic, the file must make that visible.

Use fields such as:

```text
timestamp_source: synthetic_clock
synthetic_status_declared: true
public_data_status: synthetic
```

Allowed meaning:

```text
This timestamp supports synthetic structure demonstration.
```

Not allowed meaning:

```text
This timestamp proves real physiological timing.
This timestamp proves real human response.
This timestamp proves real AI impact.
```

---

## Timestamp fields

Recommended timestamp-related fields include:

```text
session_start
session_end
event_timestamp
window_start
window_end
source_timestamp
device_timestamp
software_timestamp
operator_timestamp
simulator_timestamp
processing_timestamp
timestamp_source
clock_id
sync_method
sync_quality_flag
drift_note
dropout_note
deviation_note
```

These fields support auditability.

They do not validate benchmark performance.

They do not validate Sal-Meter.

They do not grant CAIS compliance.

---

## Session start and end rule

`session_start` and `session_end` define the outer time boundary of a session.

Example:

```json
{
  "session_start": "2026-04-28T09:00:00Z",
  "session_end": "2026-04-28T09:20:00Z"
}
```

Allowed meaning:

```text
The session is represented as starting and ending within this timestamp range.
```

Not allowed meaning:

```text
The participant entered or exited a validated psychological state during this range.
```

---

## Event timestamp rule

`event_timestamp` marks a discrete event.

Examples:

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
The event marker indicates when a session event was logged.
```

Not allowed meaning:

```text
The event marker proves that a true human-state transition occurred.
```

---

## Window timestamp rule

`window_start` and `window_end` define an analysis window.

Example:

```json
{
  "window_label": "synthetic_baseline",
  "window_start": "2026-04-28T09:01:00Z",
  "window_end": "2026-04-28T09:05:00Z"
}
```

Allowed meaning:

```text
This window defines a bounded segment for synthetic/sample analysis.
```

Not allowed meaning:

```text
This window proves a clinically meaningful baseline, stress, recovery, or consciousness state.
```

---

## Clock source rule

Every timestamp should have a documented clock source.

Recommended values:

```text
synthetic_clock
operator_clock
device_clock
software_clock
simulator_clock
lsl_clock
brainflow_clock
timeflux_clock
system_clock
manual_marker
unknown
```

For public synthetic/sample files, use:

```text
synthetic_clock
```

or clearly explain why another source is shown.

If `unknown` is used, the limitation must be explicit.

Unknown clock source weakens auditability.

---

## Synchronization method rule

Every multimodal package should declare a synchronization method.

Recommended values:

```text
synthetic_timestamp_alignment
shared_timestamp_column
lsl_marker_alignment
brainflow_timestamp_alignment
timeflux_pipeline_alignment
device_clock_alignment
software_clock_alignment
simulator_event_alignment
manual_operator_alignment
posthoc_alignment
not_applicable
unknown
```

Allowed meaning:

```text
The sync method describes how timestamps or event windows are aligned.
```

Not allowed meaning:

```text
The sync method proves that the synchronized signals measure a true human state.
```

---

## Sync quality flag rule

A session may include a `sync_quality_flag`.

Recommended values:

```text
pass
review
fail
unknown
not_applicable
```

Meaning:

```text
pass            = helper-level structure appears aligned enough for demonstration or planned analysis
review          = timing or alignment requires human review
fail            = timing or alignment is not usable for the intended helper analysis
unknown         = no reliable sync assessment is available
not_applicable  = synchronization is not relevant for this file
```

`pass` does not mean scientific validation.

`pass` does not mean benchmark validation.

`pass` does not mean Sal-Meter validation.

`pass` does not mean CAIS compliance.

---

## Drift rule

Clock drift must be documented when known.

Recommended fields:

```text
drift_detected
drift_direction
drift_estimate_ms
drift_correction_applied
drift_note
```

Example:

```json
{
  "drift_detected": false,
  "drift_direction": "not_applicable",
  "drift_estimate_ms": 0,
  "drift_correction_applied": false,
  "drift_note": "Synthetic sample only."
}
```

Allowed meaning:

```text
The package documents whether timing drift was observed, estimated, or corrected.
```

Not allowed meaning:

```text
Absence of documented drift proves physiological validity.
```

---

## Dropout rule

Signal or event dropout must be documented when known.

Recommended fields:

```text
dropout_detected
dropout_window
dropout_signal
dropout_reason
dropout_note
```

Allowed meaning:

```text
The package documents missing or interrupted data.
```

Not allowed meaning:

```text
A clean dropout note proves the benchmark is valid.
```

A missing dropout note should not be treated as proof of clean data.

---

## Latency rule

Latency must be documented when relevant.

Latency may include:

```text
device latency
software latency
operator marker delay
simulator event delay
AI response delay
feedback delivery delay
dashboard refresh delay
file-writing delay
postprocessing delay
```

Recommended fields:

```text
latency_known
latency_estimate_ms
latency_source
latency_note
```

Allowed meaning:

```text
Latency documentation supports auditability of event timing.
```

Not allowed meaning:

```text
Latency documentation proves AI causality or human-state causality.
```

---

## AI interaction timing rule

AI interaction windows must be treated as interaction-condition windows.

Recommended event markers:

```text
ai_interaction_start
feedback_event
task_end
recovery_start
```

Allowed meaning:

```text
The AI interaction window marks when an AI-related condition was active.
```

Not allowed meaning:

```text
The AI interaction window proves that AI caused a specific human-state outcome.
```

AI timing is a context marker.

It is not a cause by itself.

---

## Feedback timing rule

Feedback timing may be recorded for closed-loop demo-lite or future research-stage interaction studies.

Recommended fields:

```text
feedback_event_id
feedback_timestamp
feedback_source
feedback_type
feedback_delivery_status
feedback_latency_ms
feedback_note
```

Allowed meaning:

```text
The feedback timestamp documents when a feedback event was generated or delivered.
```

Not allowed meaning:

```text
The feedback timestamp proves therapeutic effect, clinical improvement, recovery, safety, or validated mediation.
```

Feedback timing is not therapy.

Feedback timing is not counseling.

Feedback timing is not legal mediation.

Feedback timing is not clinical intervention.

---

## Cross-modal alignment rule

If multiple streams are present, their alignment must be documented.

Example streams:

```text
ECG
HRV
EDA
PPG
EEG
eye tracking
gaze
webcam-derived proxy
simulator events
operator markers
AI interaction logs
dashboard events
```

Recommended alignment fields:

```text
stream_name
timestamp_source
sampling_rate_hz
sync_method
sync_quality_flag
known_offset_ms
offset_correction_applied
drift_note
dropout_note
```

Allowed meaning:

```text
The streams are organized for helper-level synchronized analysis.
```

Not allowed meaning:

```text
The streams prove a validated multimodal human-state measurement.
```

---

## Sampling rate rule

Every signal stream should document sampling rate where applicable.

Example:

```json
{
  "signal_name": "synthetic_eda",
  "sampling_rate_hz": 32,
  "timestamp_source": "synthetic_clock"
}
```

Allowed meaning:

```text
The sampling rate describes how often a signal stream is represented.
```

Not allowed meaning:

```text
The sampling rate proves physiological validity.
```

For irregular event streams, use:

```text
event_based
irregular
not_applicable
```

or document the convention clearly.

---

## Annotation timing rule

Annotations must include timestamp context.

Recommended fields:

```text
annotation_id
annotation_timestamp
annotation_source
annotation_type
annotation_note
operator_confirmed
```

Allowed meaning:

```text
The annotation timestamp marks when an annotation was made or attached.
```

Not allowed meaning:

```text
The annotation timestamp proves that the annotation is true.
```

Operator confirmation is an audit marker.

It is not scientific proof.

---

## Deviation timing rule

Protocol deviations should include timing context.

Recommended fields:

```text
deviation_id
deviation_timestamp
deviation_type
deviation_source
deviation_note
impact_on_sync
impact_on_analysis
```

Allowed meaning:

```text
The deviation timestamp records when a deviation was observed or logged.
```

Not allowed meaning:

```text
The deviation note proves the data are still valid.
```

Deviations should be visible.

Hidden deviations poison reproducibility.

---

## Timezone rule

Timezone must not be ambiguous.

Preferred public synthetic/sample format:

```text
UTC with Z suffix
```

Example:

```text
2026-04-28T09:00:00Z
```

If local time is used, include the local timezone or offset.

Example:

```text
2026-04-28T18:00:00+09:00
```

Avoid:

```text
2026-04-28 18:00
April 28 evening
local time
Korea time
server time
```

unless the convention is explicitly documented.

---

## Ordering rule

Timestamp order should be logically consistent.

Expected order for a simple synthetic session:

```text
session_start
baseline_start
task_start
ai_interaction_start
feedback_event
task_end
recovery_start
session_end
```

A different order is allowed only if documented.

Unexpected order should trigger review.

Review does not mean failure.

Review means the timing story needs an audit trail.

---

## Boundary between time and causality

Temporal order alone does not prove causality.

The following is not enough:

```text
AI event happened before signal change.
```

A timestamp can support a hypothesis.

A timestamp cannot prove the hypothesis by itself.

Correct sentence:

```text
The event occurred before the synthetic/sample feature window in this package.
```

Incorrect sentence:

```text
The event caused the human-state change.
```

---

## Boundary between time and recovery

A recovery window label does not prove recovery.

Correct sentence:

```text
This window is labeled as a synthetic recovery window for structure demonstration.
```

Incorrect sentence:

```text
The participant recovered during this window.
```

Recovery is not proven by a timestamp.

Recovery is not proven by a label.

Recovery is not proven by a toy baseline.

---

## Boundary between time and safety

A timestamped feedback event does not prove safety.

Correct sentence:

```text
The feedback event was logged at this timestamp.
```

Incorrect sentence:

```text
The AI system became safe at this timestamp.
```

Safety claims require separate governance, evidence, and validation.

This repository does not create safety certification.

---

## Boundary between time and Sal-Meter

Proxy timestamps are not Sal-Meter input.

Proxy timestamps do not validate Sal-Meter.

Proxy timestamps do not define CAIS.

Proxy timestamps do not grant CAIS compliance.

Correct sentence:

```text
These timestamps may support future comparison infrastructure if Sal-Meter core inputs become available under proper boundary conditions.
```

Incorrect sentence:

```text
These timestamps prove Sal-Meter signal validity.
```

---

## Future Sal-Meter A/B timing boundary

Future Sal-Meter A/B comparison may require timestamp alignment between proxy streams and Sal-Meter core inputs.

That future comparison is not open in this repository.

If future comparison occurs, it must document:

```text
proxy stream timestamps
Sal-Meter input timestamps
shared event markers
clock source
sync method
known offset
drift review
dropout review
metadata completeness
raw data boundary
audit trail
```

Even then, timestamp alignment alone will not prove Sal-Meter validity.

It will only support comparison.

---

## Human-State Cost timing boundary

Human-State Cost is a proxy construct.

Timing may help define the windows used to calculate the construct.

Timing does not convert Human-State Cost into:

```text
a clinical score
a diagnostic score
a psychological safety score
a consciousness score
an employee score
a legal score
an eligibility score
a person ranking
```

Correct sentence:

```text
The Human-State Cost proxy value is associated with a defined interaction window.
```

Incorrect sentence:

```text
The timestamped Human-State Cost value proves the person became unsafe.
```

---

## Dyadic and mediation timing boundary

Future dyadic or mediation benchmark work may require timing of:

```text
speaker turn
AI intervention
conflict prompt
de-escalation prompt
feedback event
recovery window
termination gate
operator annotation
```

These timestamps must not be used to claim:

```text
legal mediation
therapy
counseling
relationship diagnosis
fault assignment
who-is-right decision
blame attribution
fitness decision
surveillance readiness
human ranking
```

Allowed future meaning:

```text
The timestamp marks a synthetic or low-risk simulated interaction event.
```

Not allowed meaning:

```text
The timestamp proves that mediation succeeded in a legal, clinical, or therapeutic sense.
```

---

## Leakage rule

Timestamps can leak labels.

Leakage may occur through:

```text
session ordering
fixed condition order
window duration
file creation time
folder names
event spacing
operator timing patterns
device start delay
known protocol sequence
train/test split timing
public release timing
```

Bad examples:

```text
all stress sessions begin at 09:10
all recovery sessions have 5-minute windows
all task sessions are recorded on a specific day
all labels are inferable from event order
all filenames contain condition timing
```

Better practice:

```text
document timing clearly
separate labels from features
avoid embedding labels in file names
review whether time fields reveal targets
use leakage-safe split design
state known leakage risks
```

A timestamp that leaks the label can destroy the benchmark.

---

## Split timing rule

Train/test split design must consider timestamp leakage.

Risk examples:

```text
training sessions occur earlier than test sessions
condition labels follow fixed chronological order
participant sequence reveals target
operator shift reveals target
device batch reveals target
```

Recommended review fields:

```text
split_strategy
time_based_leakage_reviewed
session_order_leakage_reviewed
operator_time_leakage_reviewed
device_time_leakage_reviewed
known_risks
```

A split that leaks time structure is not evidence.

---

## Public release timing rule

Public release timestamps should not imply validation status.

A release date does not mean:

```text
benchmark validated
Sal-Meter validated
CAIS compliant
scientifically proven
clinical-ready
device-ready
certified
```

A release date only means:

```text
This helper repository state was published or updated at that time.
```

Do not turn release timing into authority.

---

## Operator log timing rule

Operator logs should record relevant timing context.

Recommended entries:

```text
session start observed
baseline window started
task window started
AI interaction started
feedback event delivered
task ended
recovery window started
session ended
deviation observed
dropout observed
manual correction applied
```

Operator logs should not include:

```text
participant name
clinical interpretation
mental-health judgment
diagnostic statement
therapeutic judgment
employment judgment
relationship blame
human ranking
```

Operator timing is audit support.

It is not clinical interpretation.

---

## QC timing rule

QC reports should include timing and synchronization review.

Recommended fields:

```text
timestamp_format_checked
clock_source_declared
sync_method_declared
event_order_checked
window_order_checked
drift_reviewed
dropout_reviewed
latency_reviewed
leakage_reviewed
deviation_reviewed
final_qc_status
```

QC status should not be overread.

Correct sentence:

```text
QC indicates whether the helper structure passed the defined checks.
```

Incorrect sentence:

```text
QC proves the benchmark or system is scientifically valid.
```

---

## Schema relationship

This rule document complements:

```text
schemas/session-metadata.schema.json
schemas/event-markers.schema.json
schemas/streams-manifest.schema.json
schemas/features-baseline.schema.json
schemas/labels.schema.json
schemas/splits.schema.json
schemas/qc-report.schema.json
```

Schemas check structure.

This document explains timestamp and synchronization boundaries.

Neither validates benchmark performance.

Neither validates Sal-Meter.

Neither grants CAIS compliance.

---

## Sample data relationship

This rule document complements:

```text
sample-data/
```

Public sample data may demonstrate timestamp structure.

Public sample data must not be treated as scientific evidence.

Correct interpretation:

```text
The public synthetic timestamp demonstrates how timing fields may be represented.
```

Incorrect interpretation:

```text
The public synthetic timestamp proves a real human-state transition.
```

---

## Evaluation baseline relationship

Evaluation baseline scripts may load timestamped windows.

This does not validate the timestamps.

This does not validate the model.

This does not validate the benchmark.

This does not validate Sal-Meter.

This does not grant CAIS compliance.

Correct interpretation:

```text
The baseline script demonstrates how timestamped files may be loaded and checked.
```

Incorrect interpretation:

```text
The baseline script proves that the timing structure captures true human state.
```

---

## Recommended timestamp checklist

Before publishing or using a timestamped package, check:

```text
[ ] Are timestamps in a documented format?
[ ] Is timezone or UTC status clear?
[ ] Is timestamp_source declared?
[ ] Is sync_method declared?
[ ] Is event order logically reviewable?
[ ] Are session_start and session_end present when needed?
[ ] Are window_start and window_end present when needed?
[ ] Are event_timestamp values present when needed?
[ ] Are drift risks documented?
[ ] Are dropout risks documented?
[ ] Are latency risks documented?
[ ] Are deviation notes present when needed?
[ ] Has timestamp leakage been reviewed?
[ ] Are labels separated from feature timing where possible?
[ ] Is synthetic/public status visible?
[ ] Are Sal-Meter and CAIS overclaims avoided?
[ ] Are diagnostic, clinical, therapeutic, surveillance, certification, and human-ranking claims avoided?
```

If the timestamp story cannot be audited, the package is not ready.

---

## Acceptable public synthetic example

```csv
event_id,session_id,event_type,event_timestamp,event_source,event_description,operator_confirmed,condition_label
SYN-EVT-001,SYN-SESSION-001,session_start,2026-04-28T09:00:00Z,synthetic,Synthetic session start,true,not_applicable
SYN-EVT-002,SYN-SESSION-001,baseline_start,2026-04-28T09:01:00Z,synthetic,Synthetic baseline window begins,true,synthetic_baseline
SYN-EVT-003,SYN-SESSION-001,task_start,2026-04-28T09:05:00Z,synthetic,Synthetic task window begins,true,synthetic_task_ai_interaction
SYN-EVT-004,SYN-SESSION-001,ai_interaction_start,2026-04-28T09:07:30Z,synthetic,Synthetic AI interaction begins,true,synthetic_task_ai_interaction
SYN-EVT-005,SYN-SESSION-001,feedback_event,2026-04-28T09:10:00Z,synthetic,Synthetic non-coercive feedback timing adjustment,true,synthetic_feedback
SYN-EVT-006,SYN-SESSION-001,task_end,2026-04-28T09:15:00Z,synthetic,Synthetic task window ends,true,synthetic_task_ai_interaction
SYN-EVT-007,SYN-SESSION-001,recovery_start,2026-04-28T09:16:00Z,synthetic,Synthetic recovery window begins,true,synthetic_recovery
SYN-EVT-008,SYN-SESSION-001,session_end,2026-04-28T09:20:00Z,synthetic,Synthetic session end,true,not_applicable
```

This is acceptable because it is clearly synthetic.

It must not be described as benchmark evidence.

---

## Unacceptable timestamp interpretation

The following interpretation is not allowed:

```text
Because the feedback event occurred at 09:10 and the recovery window started at 09:16, the AI feedback caused recovery.
```

Correct interpretation:

```text
The synthetic package represents a feedback event before a recovery-labeled synthetic window. This demonstrates structure only.
```

---

## Future private benchmark rule

If future private human-subject benchmark data are collected, timestamp governance must be stricter than public synthetic examples.

At minimum, future private benchmark work must define:

```text
clock source
timestamp format
timezone convention
sync method
event marker source
operator marker delay
device clock behavior
software clock behavior
drift handling
dropout handling
latency handling
annotation timing
label timing
split timing
leakage review
deviation log
audit trail
public release boundary
```

Private timestamped human data must not be uploaded to this public repository.

---

## Prohibited timestamp uses

Timestamps must not be used for:

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
Create protocol-helper/timestamp_sync_rule.md
```

---

## Completion status

```text
Protocol helper file.
Timestamp sync rule.
Research-stage.
Public helper documentation only.
Timing and synchronization discipline only.
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

A timestamp must help reconstruct the sequence.

A timestamp must not become causality.

A sync method must help audit alignment.

A sync method must not become validation.

A clean event order must not become proof.

A recovery window must not become recovery.

A feedback event must not become therapy.

A future comparison timestamp must not pretend to be current Sal-Meter validation.

Time is the spine of audit.

Time is not the soul of proof.
