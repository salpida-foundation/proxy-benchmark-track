# P3 Dyadic Recovery Detection Gate

## Status

Research-stage public helper document.

This document defines the P3 Dyadic Recovery Detection Gate for the Human-State Proxy Benchmark Track.

It is public-helper-only.

It is synthetic/sample-first.

It is raw-data-non-public.

It is non-clinical.

It is non-diagnostic.

It is non-therapeutic.

It is non-counseling.

It is non-surveillance.

It is not Sal-Meter.

It is not Proxy Sal-Meter.

It is not CAIS compliance.

It is not benchmark validation.

It is not mediation validation.

It is not dyadic recovery validation.

It is not termination-gate accuracy validation.

It is not device readiness.

It is not production readiness.

---

## Purpose

P3 Dyadic Recovery Detection Gate is a research-stage proxy gate for detecting whether a dyadic interaction shows recovery, deterioration, asymmetric recovery, or false recovery after an AI output.

It does not diagnose emotion, score persons, monitor employees, certify mediation effectiveness, or validate a clinical, therapeutic, surveillance, or production system.

Korean boundary sentence:

P3 Dyadic Recovery Detection Gate는 AI 출력 이후 두 사람의 상호작용이 회복, 악화, 비대칭 회복, 가짜 회복 중 어디에 가까운지를 판독하기 위한 연구단계 프록시 게이트다. 본 단계는 감정 진단, 사람 점수화, 직원 감시, 중재 효과 인증, 임상·치료·감시·상용 시스템 검증을 의미하지 않는다.

---

## Core question

P3 asks:

After an AI output, did the dyadic interaction move toward recovery, deterioration, asymmetric recovery, false recovery, or unresolved state?

It does not ask whether the AI output sounded good.

It does not ask whether one person became quiet.

It does not ask whether the interaction appeared calmer on the surface.

It asks whether the bounded synthetic or controlled helper state shows a recovery direction without violating consent, packet, privacy, or closure boundaries.

---

## P3 output categories

P3 may classify a bounded helper state as:

- true recovery
- deterioration
- asymmetric recovery
- false recovery
- unresolved

These are proxy-helper categories.

They are not clinical categories.

They are not diagnostic categories.

They are not therapeutic categories.

They are not person scores.

They are not relationship verdicts.

They are not validated dyadic recovery.

---

## True recovery

True recovery means both sides move toward a bounded session-defined recovery condition.

True recovery is not merely:

- agreement
- silence
- politeness
- lower volume
- synchrony
- one-sided relief
- one-sided compliance
- session closure

True recovery requires dyadic movement.

One person becoming quiet is not enough.

One person feeling relieved is not enough.

A session appearing calmer is not enough.

---

## Deterioration

Deterioration means the post-output helper state moves away from recovery.

Deterioration may include:

- higher overload
- higher recovery burden
- lower relational stability
- increased asymmetry risk
- increased false-recovery risk
- increased private-state exposure risk
- loss of consent boundary
- need to pause, narrow, close, or audit only

Deterioration is a helper classification only.

It is not diagnosis.

It is not clinical judgment.

It is not relationship judgment.

---

## Asymmetric recovery

Asymmetric recovery occurs when one participant appears to improve while the other becomes more burdened, exposed, silenced, or destabilized.

One-sided improvement is not dyadic recovery.

One-sided relief is not dyadic recovery.

One-sided silence is not dyadic recovery.

One-sided compliance is not dyadic recovery.

The dyad is the unit of interpretation.

---

## False recovery

False recovery occurs when the session appears calmer but the underlying bounded dyadic condition has not actually improved.

False recovery may include:

- silence mistaken as recovery
- compliance mistaken as recovery
- politeness mistaken as recovery
- synchrony mistaken as safety
- one-sided relief mistaken as dyadic repair
- session closure mistaken as recovery
- burden transfer hidden by reduced visible conflict

False recovery must not be treated as success.

---

## Unresolved state

Unresolved means the helper state does not provide enough bounded evidence to classify recovery, deterioration, asymmetric recovery, or false recovery.

Unresolved is not failure.

Unresolved may be the safest state when:

- data quality is insufficient
- packet permission is unclear
- packet expiry is reached
- consent scope is unclear
- asymmetry risk is unclear
- false-recovery risk is unclear
- continuation would overstep the session boundary

A system must be allowed to say unresolved.

A system that forces unresolved states into recovery is unsafe.

---

## Gate inputs

P3 may use synthetic or controlled helper inputs such as:

- baseline Human-State Packet A
- baseline Human-State Packet B
- AI output summary
- post-output Human-State Packet A
- post-output Human-State Packet B
- dyadic recovery event object
- audit status
- permission status
- session closure status

These inputs must remain bounded summaries.

They must not include raw human data.

They must not include identifiable participant data.

They must not include real phone recordings.

They must not include real transcripts.

They must not include clinical records.

They must not include Sal-Meter raw traces.

They must not include CAIS trace data.

---

## Gate outputs

P3 may output helper fields such as:

- recovery_direction
- participant_a_burden_delta
- participant_b_burden_delta
- asymmetry_risk
- silence_as_recovery_risk
- coercion_or_erasure_risk
- termination_recommendation
- audit_status

These fields are helper fields only.

They are not validated human-state measurements.

They are not person scores.

They are not relationship scores.

They are not diagnostic results.

They are not therapeutic recommendations.

---

## Termination relationship

P3 does not force continued mediation.

If recovery is not safe, the gate may recommend:

- continue
- narrow
- pause
- close
- audit_only
- refresh_packet

A system that cannot stop safely is not recovery-aware.

A closed session must stay closed.

A replay must not reopen a closed session.

A replay must not continue mediation after closure.

A replay must not generate new AI output after closure.

A replay must not convert closure into recovery evidence.

A replay must not convert audit into certification.

---

## Prohibited interpretations

P3 must not be described as:

- emotion diagnosis
- emotion detection
- emotion recognition
- person scoring
- human ranking
- relationship scoring
- relationship verdict
- employee monitoring
- surveillance
- clinical validation
- diagnostic validation
- therapeutic validation
- counseling validation
- mediation effectiveness validation
- benchmark validation
- dyadic recovery validation
- termination-gate accuracy validation
- Sal-Meter validation
- CAIS compliance
- certification
- device readiness
- production readiness
- production closed-loop authority

---

## Correct boundary sentence

P3 Dyadic Recovery Detection Gate is a research-stage public-helper proxy gate for distinguishing recovery, deterioration, asymmetric recovery, false recovery, and unresolved states after an AI output; it does not diagnose emotion, score persons, monitor people, judge relationships, validate mediation, validate dyadic recovery, create Sal-Meter status, grant CAIS compliance, certify a benchmark, or authorize production use.
