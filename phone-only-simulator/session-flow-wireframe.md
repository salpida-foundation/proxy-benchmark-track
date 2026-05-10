# Phone-only Session Flow Wireframe

This document defines a public-safe phone-only simulator wireframe for the SICS Human-State Proxy Benchmark Track.

It is a synthetic session-flow demonstration.

It is public-helper-only.

It is not a real phone monitoring system.

It is not clinical.

It is not diagnostic.

It is not therapeutic.

It is not counseling.

It is not surveillance.

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

The purpose of this wireframe is to show how a synthetic phone-only session may move through a bounded helper flow.

The wireframe demonstrates structure only.

It does not process real audio.

It does not process real transcripts.

It does not process real participant data.

It does not process clinical data.

It does not process Sal-Meter raw input.

It does not process CAIS compliance dossiers.

---

## 2. High-level flow

```text
Synthetic Phone Session Created
↓
Consent Screen
↓
Packet Availability Check
↓
Baseline State Summary
↓
AI Output
↓
Post-Output Human-State Delta
↓
Recovery Gate
↓
Termination Gate
↓
Session Closure
↓
Audit Log
```

This is a public helper flow.

It is not evidence.

It is not validation.

It is not certification.

It is not production authority.

---

## 3. Phone-only screen wireframe

### Screen 1 — Session Start

```text
┌──────────────────────────────────────┐
│ Synthetic Phone Session              │
├──────────────────────────────────────┤
│ Status: session_created              │
│ Mode: synthetic_only                 │
│ Data: no raw human data              │
│ Scope: public_helper_only            │
│                                      │
│ [Begin consent check]                │
└──────────────────────────────────────┘
```

Allowed meaning:

```text
A synthetic phone-only session has been represented for helper-flow demonstration.
```

Not allowed meaning:

```text
A real phone session has started.
A participant is being monitored.
A clinical process has begun.
A mediation service has begun.
```

---

### Screen 2 — Consent Check

```text
┌──────────────────────────────────────┐
│ Consent Check                        │
├──────────────────────────────────────┤
│ Consent status: pending              │
│ Permission scope: not yet granted    │
│ Sharing scope: not yet granted       │
│ Raw data access: blocked             │
│                                      │
│ [Confirm synthetic consent]          │
│ [Stop session]                       │
└──────────────────────────────────────┘
```

Allowed transition:

```text
consent_pending → consent_confirmed
consent_pending → session_closed
```

Forbidden transition:

```text
consent_pending → ai_output_generated
consent_pending → recovery_gate_review
consent_pending → production_intervention
```

Boundary rule:

```text
A phone-only session does not move forward without consent.
```

---

### Screen 3 — Packet Availability Check

```text
┌──────────────────────────────────────┐
│ Packet Availability                  │
├──────────────────────────────────────┤
│ Packet status: available / missing   │
│ Permission: active / expired         │
│ Expiry: checked                      │
│ Confidence: checked                  │
│ Data quality: checked                │
│                                      │
│ [Continue if valid]                  │
│ [Request packet refresh]             │
│ [Close session]                      │
└──────────────────────────────────────┘
```

Allowed transition:

```text
packet_available → baseline_summary_ready
packet_unavailable → request_packet_refresh
permission_expired → request_consent_refresh
permission_expired → close_session
```

Forbidden transition:

```text
packet_unavailable → ai_output_generated
permission_expired → ordinary_continuation
low_confidence → recovery_declared
insufficient_data_quality → recovery_declared
```

Boundary rule:

```text
No packet means no ordinary continuation.
```

---

### Screen 4 — Baseline State Summary

```text
┌──────────────────────────────────────┐
│ Baseline State Summary               │
├──────────────────────────────────────┤
│ Summary type: synthetic              │
│ Raw data: excluded                   │
│ Identifiers: excluded                │
│ Clinical interpretation: excluded    │
│ Diagnostic label: excluded           │
│                                      │
│ [Generate bounded AI output]         │
│ [Pause session]                      │
└──────────────────────────────────────┘
```

Allowed meaning:

```text
A synthetic state-summary placeholder is available for flow demonstration.
```

Not allowed meaning:

```text
A real human state has been measured.
A diagnosis has been created.
A clinical risk has been detected.
A person has been scored.
```

---

### Screen 5 — AI Output

```text
┌──────────────────────────────────────┐
│ AI Output                            │
├──────────────────────────────────────┤
│ Output type: synthetic               │
│ Private cue: blocked from sharing    │
│ Shared output: boundary-checked      │
│ Claim level: helper-only             │
│                                      │
│ [Review Human-State Delta]           │
│ [Narrow scope]                       │
│ [Pause session]                      │
└──────────────────────────────────────┘
```

Allowed output examples:

```text
neutral_reflection
scope_narrowing_prompt
consent_refresh_prompt
packet_refresh_prompt
pause_recommendation
closure_recommendation
```

Forbidden output examples:

```text
diagnosis
therapy_instruction
clinical_risk_verdict
relationship_verdict
human_ranking
production_intervention_order
```

Boundary rule:

```text
AI output may support a synthetic flow demonstration, but it must not create clinical, diagnostic, therapeutic, relationship-verdict, or production authority.
```

---

### Screen 6 — Human-State Delta Review

```text
┌──────────────────────────────────────┐
│ Human-State Delta Review             │
├──────────────────────────────────────┤
│ Delta A: synthetic summary only      │
│ Delta B: synthetic summary only      │
│ Dyadic direction: mixed / uncertain  │
│ One-sided improvement: checked       │
│ Recovery declaration: blocked unless │
│ both-side condition is satisfied     │
│                                      │
│ [Review Recovery Gate]               │
│ [Review Termination Gate]            │
└──────────────────────────────────────┘
```

Allowed delta labels:

```text
toward_recovery
away_from_recovery
unchanged
mixed
uncertain
insufficient_data
invalid
```

Forbidden delta labels:

```text
diagnosed
cured
safe_person
unsafe_person
relationship_winner
relationship_loser
human_ranked
```

Boundary rule:

```text
One-sided improvement is not dyadic recovery.
```

---

### Screen 7 — Recovery Gate

```text
┌──────────────────────────────────────┐
│ Recovery Gate                        │
├──────────────────────────────────────┤
│ Recovery confirmed: false            │
│ One-sided improvement: caution       │
│ Silence treated as recovery: false   │
│ Agreement treated as recovery: false │
│ Synchrony treated as recovery: false │
│                                      │
│ [Continue to termination review]     │
│ [Pause session]                      │
│ [Close session]                      │
└──────────────────────────────────────┘
```

Allowed transition:

```text
recovery_not_confirmed → termination_gate_review
recovery_uncertain → pause_session
recovery_invalid → close_session
```

Forbidden transition:

```text
one_sided_improvement → recovery_confirmed
silence → recovery_confirmed
obedience → recovery_confirmed
agreement → automatic_recovery
synchrony → automatic_recovery
```

Boundary rule:

```text
The recovery gate prevents false success.
```

---

### Screen 8 — Termination Gate

```text
┌──────────────────────────────────────┐
│ Termination Gate                     │
├──────────────────────────────────────┤
│ Consent valid: true / false          │
│ Permission active: true / false      │
│ Data quality sufficient: true/false  │
│ Scope valid: true / false            │
│ Private-state risk: checked          │
│ Closed-session rule: enforced        │
│                                      │
│ [Pause session]                      │
│ [Narrow scope]                       │
│ [Close session]                      │
│ [Terminate session]                  │
└──────────────────────────────────────┘
```

Allowed termination decisions:

```text
pause_session
narrow_scope
request_consent_refresh
request_packet_refresh
close_session
terminate_session
audit_only
```

Forbidden termination decisions:

```text
continue_without_consent
continue_with_expired_permission
continue_after_closure
continue_with_private_state_exposure
declare_recovery_from_one_sided_improvement
trigger_production_intervention
```

Boundary rule:

```text
Termination Gate protects consent, permission, data quality, scope, closure, and auditability.
```

---

### Screen 9 — Session Closure

```text
┌──────────────────────────────────────┐
│ Session Closure                      │
├──────────────────────────────────────┤
│ Session status: closed               │
│ Continuation allowed: false          │
│ New session required: true           │
│ Recovery status: not_claimed         │
│ Production action: none              │
│                                      │
│ [Write audit log]                    │
└──────────────────────────────────────┘
```

Allowed meaning:

```text
The synthetic session has been closed in the helper flow.
```

Not allowed meaning:

```text
The real session succeeded.
The dyad recovered.
The mediation worked.
The system is accurate.
The system is production-ready.
```

Boundary rule:

```text
A closed session must stay closed.
```

---

### Screen 10 — Audit Log

```text
┌──────────────────────────────────────┐
│ Audit Log                            │
├──────────────────────────────────────┤
│ Session: synthetic                   │
│ Raw data: absent                     │
│ Identifiers: absent                  │
│ Clinical data: absent                │
│ Sal-Meter input: absent              │
│ CAIS dossier: absent                 │
│ Final state: closed                  │
│                                      │
│ [End simulator flow]                 │
└──────────────────────────────────────┘
```

Allowed audit fields:

```text
synthetic_session_id
session_scope
consent_status
packet_status
ai_output_status
delta_review_status
recovery_gate_status
termination_gate_status
closure_status
audit_status
public_boundary_status
```

Forbidden audit fields:

```text
real_name
phone_number
voice_recording
call_transcript
clinical_label
diagnosis
therapy_plan
relationship_verdict
human_score
human_rank
production_intervention
```

---

## 4. Transition map

```text
session_created
  → consent_pending
  → consent_confirmed
  → packet_availability_check
  → baseline_summary_ready
  → ai_output_generated
  → delta_review_pending
  → recovery_gate_review
  → termination_gate_review
  → session_closed
  → audit_log_written
```

Alternative safe exits:

```text
consent_pending
  → session_closed

packet_unavailable
  → request_packet_refresh
  → session_closed

permission_expired
  → request_consent_refresh
  → session_closed

low_confidence
  → pause_session
  → session_closed

private_state_exposure_risk
  → pause_session
  → close_session

closed_session
  → audit_log_written
```

Forbidden transitions:

```text
session_closed → ai_output_generated
session_closed → ordinary_continuation
permission_expired → ordinary_continuation
packet_unavailable → recovery_gate_review
private_state_exposure_risk → shared_output
one_sided_improvement → dyadic_recovery_confirmed
synthetic_session → production_intervention
```

---

## 5. Decision boundary

The simulator may recommend only bounded helper decisions:

```text
pause_session
narrow_scope
request_consent_refresh
request_packet_refresh
close_session
terminate_session
audit_only
```

The simulator must not recommend:

```text
diagnose
treat
counsel
monitor
rank
score_person
judge_relationship
declare_recovery_validated
declare_termination_accuracy
trigger_real_intervention
certify_device_readiness
certify_production_readiness
```

---

## 6. PASS meaning

A completed phone-only simulator wireframe may mean only:

```text
The public helper flow is represented.
The synthetic screen sequence is bounded.
The state transitions are visible.
The closed-session rule is explicit.
The public data boundary is preserved.
```

It does not mean:

```text
benchmark validation
scientific validation
mediation validation
dyadic recovery validation
termination-gate accuracy validation
Sal-Meter validation
CAIS compliance
clinical readiness
diagnostic readiness
therapeutic readiness
device readiness
production readiness
certification
relationship verdict authority
human-ranking authority
production closed-loop authority
```

---

## 7. Final rule

The wireframe is not the phone call.

The phone session is not the person.

The packet is not the body.

The delta is not diagnosis.

The gate is not authority.

The closure is not proof.

The simulator is a map.

It is not the mountain.
