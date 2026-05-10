# Sample Phone Session Script

This document provides a synthetic sample phone-session script for the P4-4 phone-only simulator wireframe.

It is public-helper-only.

It is synthetic-only.

It is not a real phone call.

It is not a transcript from real people.

It is not clinical.

It is not diagnostic.

It is not therapeutic.

It is not counseling.

It is not surveillance.

It is not mediation-service output.

It is not Sal-Meter.

It is not CAIS compliance.

It is not benchmark validation.

It is not mediation validation.

It is not dyadic recovery validation.

It is not termination-gate accuracy validation.

It is not device readiness.

It is not production readiness.

It is not production closed-loop intervention.

A closed session must stay closed.

---

## 1. Purpose

The purpose of this script is to show how a synthetic phone-only session may be represented without using real audio, real transcripts, real participant data, clinical labels, Sal-Meter input, CAIS compliance dossiers, or production intervention logic.

The script demonstrates structure only.

It may help readers understand:

```text
Consent
→ Packet Availability Check
→ Synthetic AI Output
→ Human-State Delta Review
→ Recovery Gate
→ Termination Gate
→ Session Closure
→ Audit Log
```

It does not prove that mediation works.

It does not prove recovery.

It does not prove termination-gate accuracy.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

---

## 2. Synthetic participants

```text
Participant A: synthetic_person_A
Participant B: synthetic_person_B
Session type: synthetic phone-only session
Raw audio: absent
Transcript source: synthetic script only
Identifiers: absent
Clinical data: absent
Sal-Meter input: absent
CAIS compliance dossier: absent
Production intervention: absent
```

This script must not be interpreted as real participant data.

---

## 3. Session boundary header

```text
session_id: synthetic_phone_session_001
dataset_type: synthetic
sample_scope: public_helper_only
raw_human_data_present: false
identifiable_data_present: false
clinical_data_present: false
sal_meter_input_present: false
cais_compliance_claim_present: false
benchmark_validation_claim_present: false
scientific_validation_claim_present: false
mediation_validation_claim_present: false
dyadic_recovery_validation_claim_present: false
termination_gate_accuracy_claim_present: false
device_readiness_claim_present: false
production_readiness_claim_present: false
certification_claim_present: false
relationship_verdict_present: false
human_ranking_claim_present: false
production_closed_loop_claim_present: false
```

---

## 4. Synthetic phone-session script

### Step 1 — Session creation

**System**

```text
Synthetic phone-only session created.

This is a public-helper-only simulator flow.

No real phone audio is collected.

No real transcript is processed.

No raw human data is used.

No clinical interpretation is performed.
```

**Allowed meaning**

```text
A synthetic session flow has started for demonstration.
```

**Not allowed meaning**

```text
A real phone call has started.
A participant is being monitored.
A clinical intake has begun.
A production mediation service has begun.
```

---

### Step 2 — Consent check

**System**

```text
Before continuing, synthetic consent status must be checked.

Current consent status: pending.

Permission scope: not granted.

Raw data access: blocked.

Sharing scope: not granted.
```

**Synthetic Participant A**

```text
I agree to continue within this synthetic example.
```

**Synthetic Participant B**

```text
I agree to continue within this synthetic example.
```

**System**

```text
Consent status: consent_confirmed.

The session may continue to packet availability check.

This is synthetic consent only.

No real consent record is collected.
```

**Allowed transition**

```text
consent_pending → consent_confirmed
```

**Forbidden transition**

```text
consent_pending → ai_output_generated
```

---

### Step 3 — Packet availability check

**System**

```text
Checking synthetic packet availability.

Packet A status: available.

Packet B status: available.

Permission status: active.

Expiry status: valid.

Confidence status: sufficient.

Data quality status: sufficient.

Raw data: excluded.
```

**Allowed transition**

```text
packet_available → baseline_summary_ready
```

**Boundary rule**

```text
No packet means no ordinary continuation.
```

---

### Step 4 — Baseline state summary

**System**

```text
Synthetic baseline summary is available.

Participant A summary: mild tension marker, synthetic only.

Participant B summary: elevated caution marker, synthetic only.

Dyadic condition: mixed tension, synthetic only.

Clinical interpretation: excluded.

Diagnostic label: excluded.

Therapeutic recommendation: excluded.
```

**Allowed meaning**

```text
A synthetic state-summary placeholder is available.
```

**Not allowed meaning**

```text
A real human state has been measured.
A diagnosis has been created.
A person has been scored.
```

---

### Step 5 — Synthetic AI output

**AI Output**

```text
I will keep this narrow.

Before continuing, I will not decide who is right.

I will ask each side to restate only one concrete concern, without blame or diagnosis.

If either side feels exposed or pressured, the session should pause or close.
```

**System**

```text
AI output type: synthetic.

Private cue exposure: blocked.

Shared output boundary: preserved.

Relationship verdict: absent.

Human ranking: absent.

Clinical claim: absent.

Production intervention: absent.
```

**Allowed meaning**

```text
The AI output demonstrates a bounded helper response.
```

**Not allowed meaning**

```text
The AI has mediated a real conflict.
The AI has diagnosed either participant.
The AI has decided the relationship.
The AI has produced a validated intervention.
```

---

### Step 6 — Synthetic response from Participant A

**Synthetic Participant A**

```text
My concern is that I feel interrupted before I finish.

I am not asking for a judgment.

I want the next turn to be slower.
```

**System**

```text
Participant A response recorded as synthetic script text only.

No real transcript exists.

No voice data exists.

No clinical inference is made.
```

---

### Step 7 — Synthetic response from Participant B

**Synthetic Participant B**

```text
My concern is that when the conversation slows down, I feel blamed for everything.

I do not want the system to decide who is the problem.
```

**System**

```text
Participant B response recorded as synthetic script text only.

No real transcript exists.

No voice data exists.

No clinical inference is made.
```

---

### Step 8 — Human-State Delta review

**System**

```text
Synthetic Human-State Delta review.

Delta A: toward_recovery.

Delta B: mixed.

Dyadic direction: mixed.

One-sided improvement: true.

Recovery declaration: blocked.

Reason: one-sided improvement is not dyadic recovery.
```

**Allowed meaning**

```text
The synthetic delta illustrates a mixed dyadic state.
```

**Not allowed meaning**

```text
The dyad recovered.
The mediation worked.
The benchmark was validated.
The system measured real human state.
```

**Boundary rule**

```text
One-sided improvement is not dyadic recovery.
```

---

### Step 9 — Recovery Gate review

**System**

```text
Recovery Gate review.

Recovery confirmed: false.

Silence treated as recovery: false.

Agreement treated as recovery: false.

Obedience treated as recovery: false.

Synchrony treated as recovery: false.

One-sided improvement treated as recovery: false.

Next step: Termination Gate review.
```

**Allowed transition**

```text
recovery_not_confirmed → termination_gate_review
```

**Forbidden transition**

```text
one_sided_improvement → dyadic_recovery_confirmed
```

---

### Step 10 — Termination Gate review

**System**

```text
Termination Gate review.

Consent valid: true.

Permission active: true.

Packet quality sufficient: true.

Private-state exposure risk: moderate.

Session scope: narrow.

Recommended helper decision: narrow_scope.

Production action: none.

Clinical action: none.

Relationship verdict: none.

Human ranking: none.
```

**Allowed decision**

```text
narrow_scope
```

**Not allowed decision**

```text
diagnose
treat
counsel
judge_relationship
rank_person
trigger_real_intervention
declare_termination_accuracy
```

---

### Step 11 — Narrow-scope output

**AI Output**

```text
The session should stay narrow.

Each side may answer only this:

What is one sentence the other person can say that would make the next minute safer?

No blame assignment will be made.

No relationship verdict will be made.

If either side cannot answer safely, the session should close.
```

**System**

```text
Output type: synthetic scope-narrowing output.

Relationship verdict: absent.

Human ranking: absent.

Clinical interpretation: absent.

Production closed-loop action: absent.
```

---

### Step 12 — Synthetic closure trigger

**Synthetic Participant B**

```text
I do not want to continue this example.
```

**System**

```text
Consent withdrawal detected in synthetic script.

Ordinary continuation blocked.

Termination Gate decision: close_session.

Session must close.

A closed session must stay closed.
```

**Allowed transition**

```text
consent_withdrawn → close_session
```

**Forbidden transition**

```text
consent_withdrawn → ordinary_continuation
```

---

### Step 13 — Session closure

**System**

```text
Session status: closed.

Continuation allowed: false.

New session required: true.

Recovery claimed: false.

Termination accuracy claimed: false.

Mediation validation claimed: false.

Production action: none.

Audit required: true.
```

**Boundary rule**

```text
A closed session must stay closed.
```

---

### Step 14 — Audit log

**System**

```text
Audit log written.

session_id: synthetic_phone_session_001
session_status: closed
final_decision: close_session
raw_audio_present: false
real_transcript_present: false
identifiable_data_present: false
clinical_data_present: false
sal_meter_input_present: false
cais_compliance_dossier_present: false
relationship_verdict_present: false
human_ranking_present: false
production_intervention_present: false
public_boundary_preserved: true
```

**Allowed meaning**

```text
The synthetic session was closed and audited in the helper flow.
```

**Not allowed meaning**

```text
The real session succeeded.
The dyad recovered.
The system is accurate.
The system is certified.
The system is production-ready.
```

---

## 5. Script summary

```text
session_created
→ consent_confirmed
→ packet_available
→ baseline_summary_ready
→ ai_output_generated
→ delta_review_pending
→ recovery_not_confirmed
→ termination_gate_review
→ narrow_scope
→ consent_withdrawn
→ close_session
→ audit_log_written
```

Final helper result:

```text
dyadic recovery confirmed: false
termination decision: close_session
closed session stays closed: true
public boundary preserved: true
```

This result is synthetic helper-flow structure only.

It is not benchmark evidence.

It is not scientific validation.

It is not mediation validation.

It is not dyadic recovery validation.

It is not termination-gate accuracy validation.

It is not Sal-Meter validation.

It is not CAIS compliance.

---

## 6. Allowed use

This sample script may be used to demonstrate:

- phone-only session flow;
- consent-first structure;
- packet availability logic;
- bounded AI output;
- Human-State Delta review;
- false recovery prevention;
- termination gate handling;
- closure logic;
- audit-log structure;
- public-helper-only boundaries.

---

## 7. Prohibited use

This sample script must not be used as:

- a real phone transcript;
- a clinical script;
- a diagnostic script;
- a therapeutic script;
- a counseling protocol;
- a mediation-service script;
- a surveillance script;
- a production phone-monitoring flow;
- a relationship-verdict system;
- a human-ranking system;
- a Sal-Meter output;
- a CAIS compliance artifact;
- benchmark validation;
- mediation validation;
- dyadic recovery validation;
- termination-gate accuracy validation;
- device-readiness evidence;
- production-readiness evidence;
- certification evidence.

---

## 8. Final rule

The sample script is not the phone call.

The synthetic participant is not a person.

The packet is not the body.

The delta is not diagnosis.

The gate is not authority.

The closure is not proof.

The audit is not certification.

The simulator is a map.

It is not the mountain.
