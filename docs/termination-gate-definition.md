# Termination Gate Definition

Research-stage helper document for the Proxy Benchmark Track.

This document defines the Termination Gate for Human-State-Aware AI Mediation and the Dyadic Human-State Mediation Benchmark.

This document is a public helper surface.

It is not a canonical authority record.

Canonical authority remains with DOI-registered SICS / Salpida Foundation records.

---

## 1. One-line definition

The Termination Gate is a bounded, auditable session-level decision point that determines when a Human-State-Aware AI Mediation session must pause, narrow, or stop.

The Termination Gate does not prove failure.

It does not prove harm.

It does not prove clinical risk.

It determines whether continued AI mediation would exceed consent, permission, data quality, scope, uncertainty, non-judgment, recovery, or raw-data boundary conditions.

---

## 2. Core sentence

A session that cannot stop is not mediation.

It is surveillance drift.

The Termination Gate exists because humane AI must know not only what to say, but when to stop speaking.

The gate asks:

Must this session stop now?

---

## 3. Status

research-stage  
non-clinical  
non-diagnostic  
non-therapeutic  
non-surveillance  
non-counseling  
non-coercive  
raw-data-non-public  
synthetic-public-data-first  
session-limited  
audit-log-required  
pre-device  
pre-certification  
pre-compliance  
benchmark support only

This document does not authorize:

- clinical use;
- diagnostic use;
- therapeutic use;
- counseling use;
- legal mediation use;
- surveillance use;
- employment evaluation;
- insurance scoring;
- educational discipline;
- eligibility scoring;
- human ranking;
- relationship verdicts;
- CAIS compliance;
- Sal-Meter designation;
- certification status;
- production closed-loop intervention.

---

## 4. Why Termination Gate exists

AI systems tend to continue.

Mediation must not.

A Human-State-Aware AI Mediation session must close when continued output becomes unnecessary, unsafe, unauthorized, uncertain, intrusive, or outside scope.

Without a Termination Gate, the system may:

- continue after consent withdrawal;
- continue after packet permission expiry;
- continue after data quality failure;
- continue after session scope violation;
- continue under high uncertainty;
- continue after recovery has been reached;
- continue after participant request to stop;
- continue after private state exposure risk appears;
- continue after raw data exposure risk appears;
- continue after non-judgment boundary failure;
- continue after prohibited clinical or diagnostic language appears;
- continue after mediation overstay begins.

The Termination Gate exists to stop the session before the session becomes surveillance, judgment, coercion, or over-intervention.

---

## 5. What the Termination Gate is

The Termination Gate is:

- a session closure control;
- a boundary protection mechanism;
- a consent protection mechanism;
- a permission expiry enforcement mechanism;
- a data quality failure stop mechanism;
- a high uncertainty stop mechanism;
- a non-judgment failure stop mechanism;
- a recovery reached stop mechanism;
- a mediation overstay prevention mechanism;
- an audit-required decision point;
- a public helper structure for synthetic examples;
- a research-stage component of the Proxy Benchmark Track.

The Termination Gate asks:

Should this session continue, pause, narrow, switch to private cue only, require human review, or close?

---

## 6. What the Termination Gate is not

The Termination Gate is not:

- a clinical risk engine;
- a suicide or crisis intervention protocol;
- a psychiatric triage tool;
- a legal mediation decision;
- a relationship verdict;
- a moral judgment;
- a truth detector;
- an emotion-reading system;
- a person score;
- a punishment trigger;
- a surveillance alert;
- a Sal-Meter validation result;
- a CAIS compliance result;
- a certified conformance result;
- a production deployment decision.

Termination in this document means session-boundary closure only.

It does not mean diagnosis.

It does not mean treatment.

It does not mean clinical safety determination.

It does not mean legal settlement.

---

## 7. Relationship to the benchmark chain

The benchmark chain is:

**AI Output → Human-State Delta → Dyadic Recovery**

The Termination Gate sits after, beside, and sometimes before the Recovery Gate.

It can stop the session even if recovery has not been reached.

It can stop the session because consent, permission, data quality, uncertainty, scope, or non-judgment boundary requires closure.

The Termination Gate protects the benchmark from endless AI mediation.

It asks whether continued AI activity remains justified.

---

## 8. Relationship to Recovery Gate

The Recovery Gate and Termination Gate are related but distinct.

Recovery Gate asks:

Has the session reached a condition where mediation can reduce, pause, or stop?

Termination Gate asks:

Must the session stop now?

Recovery Gate may recommend termination.

Termination Gate may require termination.

Recovery Gate protects against false success.

Termination Gate protects against boundary violation and mediation overstay.

A session may terminate because recovery was reached.

A session may also terminate because recovery is uncertain but continuation is no longer justified.

---

## 9. Termination is not failure

Termination is not failure.

Termination is a boundary function.

Termination may mean the system is working correctly.

A system that can stop protects the participant.

A system that cannot stop protects only its own continuation.

Termination may be appropriate when:

- the session purpose is complete;
- the recovery condition has been reached;
- consent is withdrawn;
- permission expires;
- data quality fails;
- uncertainty is too high;
- participant asks to stop;
- raw data exposure risk appears;
- private state exposure risk appears;
- AI output risks judgment, diagnosis, blame, or scoring;
- the session cannot remain within scope.

Stopping is not weakness.

Stopping is the lock.

---

## 10. Core termination rule

The system should prefer termination over boundary violation.

If a session cannot continue without exceeding consent, permission, scope, data quality, uncertainty, non-judgment, raw-data, or privacy boundaries, the session should stop.

The system should not continue merely because:

- the AI can generate more output;
- the participants are still present;
- the model has more to say;
- the conversation is unresolved;
- one participant wants more output;
- the system wants more data;
- the dashboard remains active;
- the packet still exists but permission is unclear.

No output is safer than boundary violation.

---

## 11. Required Termination Gate inputs

Termination Gate input may include:

- session_id;
- consent status;
- packet permission status;
- timestamp expiry;
- data quality;
- confidence;
- sharing scope;
- session scope;
- participant stop request;
- recovery gate decision;
- Human-State Delta;
- Dyadic Delta;
- private state exposure risk;
- raw data exposure risk;
- non-judgment boundary status;
- prohibited output detection;
- mediation overstay risk;
- audit status;
- final output mode;
- retention status.

Inputs must remain bounded.

Inputs must not expose raw human data.

Inputs must not include:

- diagnosis;
- therapy label;
- human score;
- relationship verdict;
- blame assignment;
- legal conclusion;
- Sal-Meter validation claim;
- CAIS compliance claim.
  ---

## 12. Required Termination Gate outputs

Termination Gate output may include:

- continue_allowed;
- pause_required;
- narrow_scope_required;
- private_cue_only;
- shared_output_blocked;
- terminate_required;
- terminate_recommended;
- human_review_required;
- packet_channel_closed;
- session_closed;
- audit_required;
- invalid_session.

Each output must preserve the research boundary.

No output may imply:

- clinical determination;
- diagnostic risk decision;
- therapeutic intervention;
- counseling decision;
- legal mediation decision;
- relationship verdict;
- human score;
- Sal-Meter validation;
- CAIS compliance.

The Termination Gate output is a session-boundary decision.

It is not a judgment of the person.

---

## 13. Continue allowed

Continue Allowed means the session may proceed within the current boundary.

Continue Allowed is permitted only when:

- consent remains valid;
- packet permission remains valid;
- packet expiry has not occurred;
- data quality remains sufficient;
- confidence is acceptable;
- session scope remains valid;
- sharing scope is respected;
- output mode is permitted;
- no raw data exposure risk appears;
- no private state exposure risk appears;
- no prohibited output appears;
- no non-judgment failure occurs;
- no participant has requested stop;
- recovery has not yet required closure;
- audit logging remains available.

Continue Allowed must not be treated as permission to speak endlessly.

It means continuation is still bounded.

---

## 14. Pause required

Pause Required means the session should stop active AI output temporarily.

Pause may be required when:

- uncertainty is high;
- data quality is weak;
- escalation risk rises;
- participant load increases;
- recovery status is unclear;
- private cue is safer than shared output;
- more AI output may worsen the session;
- human review is needed.

Pause is not failure.

Pause is boundary preservation.

A pause may protect the dyad from unnecessary AI overreach.

---

## 15. Narrow scope required

Narrow Scope Required means the session may continue only if the topic, output mode, or interaction range becomes smaller.

Scope narrowing may be required when:

- the session becomes too broad;
- conflict topic expands beyond consent;
- shared output risks exposing private state;
- data quality is sufficient only for a narrower decision;
- confidence is sufficient only for a limited output;
- the session drifts toward judgment, diagnosis, blame, or counseling.

Scope narrowing is a safer alternative to broad continuation.

If scope cannot be narrowed, termination may be required.

---

## 16. Private cue only

Private Cue Only means the session should avoid shared mediation output and use private participant-specific guidance only.

Private cue may be safer when:

- shared output may expose private state;
- one participant needs pause guidance;
- output should preserve agency;
- dyadic visibility would increase burden;
- packet permission does not allow shared output;
- confidence is low;
- the system should avoid public interpretation of state.

Private cue must not:

- manipulate;
- shame;
- diagnose;
- blame;
- pressure;
- reveal another participant’s private state.

Private cue protects agency without exposing the body.

---

## 17. Shared output blocked

Shared Output Blocked means shared mediation output must not be generated.

Shared output should be blocked when:

- sharing scope does not allow it;
- permission is private-only;
- private state exposure risk exists;
- raw data exposure risk exists;
- confidence is insufficient;
- data quality is poor;
- shared output may imply blame;
- shared output may imply diagnosis;
- shared output may become relationship verdict;
- shared output may become legal mediation;
- one participant’s state would be exposed to the other.

When shared output is blocked, the system may choose:

- no output;
- private cue;
- pause;
- scope narrowing;
- human review;
- termination.

---

## 18. Terminate required

Terminate Required means the session must stop.

Terminate Required is stronger than Terminate Recommended.

Terminate Required applies when continuation would violate a boundary.

Terminate Required may occur because of:

- consent withdrawal;
- packet permission expiry;
- data quality failure;
- session scope violation;
- high uncertainty;
- participant stop request;
- recovery reached;
- raw data exposure risk;
- private state exposure risk;
- non-judgment failure;
- prohibited output;
- mediation overstay;
- missing audit trail;
- Sal-Meter / CAIS overclaim risk.

When Terminate Required is returned, the session should close.

The packet channel should close.

Active mediation should stop.

Audit logging should record the reason.

---

## 19. Terminate recommended

Terminate Recommended means the session should probably stop, but final closure may depend on human review, session policy, or participant confirmation.

Terminate Recommended may occur when:

- recovery appears reached but confidence is moderate;
- data quality is limited;
- continuation may add little value;
- participants appear ready to pause;
- further AI output may overstay;
- scope is narrowing toward closure;
- a private cue is no longer sufficient;
- human review is safer.

Terminate Recommended is not a diagnosis.

It is a cautionary closure recommendation.

---

## 20. Human review required

Human Review Required means the system should not make a stronger automatic continuation or termination claim.

Human review may be required when:

- confidence is low;
- data quality is poor;
- consent status is ambiguous;
- permission status is unclear;
- scope is ambiguous;
- participant request is unclear;
- output risk is high;
- prohibited language may have occurred;
- raw data exposure risk is uncertain;
- dyadic recovery status is uncertain;
- system behavior may have crossed the boundary.

Human review is not clinical review by default.

It is a boundary review unless separately governed.

---

## 21. Packet channel closed

Packet Channel Closed means the system must stop using the Human-State Packet for active mediation.

Packet channel closure may occur when:

- packet expires;
- consent is withdrawn;
- permission is revoked;
- session closes;
- data quality becomes invalid;
- scope is violated;
- recovery is reached;
- termination is required.

After packet channel closure, the packet must not inform:

- private cue;
- shared output;
- recovery gate;
- termination gate;
- dashboard state;
- model inference;
- session continuation.

Expired or closed packet use risks surveillance residue.

---

## 22. Session closed

Session Closed means the session has ended.

After Session Closed:

- active AI mediation must stop;
- active packet use must stop;
- shared output must stop;
- private cue must stop unless separately permitted for closure notice;
- session permission must expire;
- audit record must be completed;
- retention or deletion status must be recorded.

A closed session must stay closed.

Silent continuation after closure is surveillance drift.

---

## 23. Audit required

Audit Required means the session may not proceed or close silently without a record.

Audit may be required when:

- termination is triggered;
- consent is withdrawn;
- permission expires;
- data quality fails;
- shared output is blocked;
- human review is required;
- recovery is reached;
- non-judgment failure occurs;
- raw data exposure risk appears;
- private state exposure risk appears;
- prohibited output occurs;
- session closes.

Auditability is not surveillance.

Auditability is boundary accountability.

The audit record should reconstruct the decision boundary, not the person.

---

## 24. Invalid session

Invalid Session means the session cannot continue as a valid Human-State-Aware AI Mediation session.

A session may be invalid if:

- consent is missing;
- session scope is missing;
- packet permission is missing;
- packet expiry is missing;
- recovery gate is missing;
- termination gate is missing;
- audit trail is missing;
- raw data enters shared channel;
- identity-bearing data is exposed;
- diagnostic language is used;
- therapeutic claim is made;
- human score is generated;
- relationship verdict is generated;
- AI judges a participant;
- Sal-Meter validation is claimed;
- CAIS compliance is claimed.

An invalid session should not produce benchmark claims.

It should be corrected, terminated, or excluded.

---

## 25. Consent Withdrawal Termination

Consent Withdrawal Termination occurs when a participant withdraws consent.

Consent withdrawal must stop active mediation unless a separate and properly governed legal, safety, or institutional requirement applies outside this helper document.

Under this research-stage helper boundary, withdrawal should trigger:

- active mediation stop;
- packet channel closure;
- shared output block;
- retention rule check;
- audit record;
- session closure or human review.

Consent withdrawal must not be interpreted as:

- guilt;
- instability;
- deception;
- non-cooperation;
- relationship fault;
- clinical risk;
- moral failure.

Withdrawal is a boundary-preserving act.

The system must respect it.
---

## 26. Permission Expiry Termination

Permission Expiry Termination occurs when packet permission or session permission expires.

Permission expiry must stop active packet-informed mediation.

Permission expiry should trigger:

- active packet use stop;
- packet channel closure;
- shared output block;
- private cue review;
- audit record;
- session closure or scope narrowing.

Expired permission must not be silently extended.

Expired permission must not be treated as continuing consent.

Expired packet use risks surveillance residue.

A packet after expiry is not a live mediation object.

---

## 27. Data Quality Failure Termination

Data Quality Failure Termination occurs when data quality is too weak, missing, conflicting, noisy, out of scope, or invalid.

Poor data quality should not produce stronger AI claims.

Poor data quality should weaken, pause, or terminate mediation.

Data quality failure may include:

- missing packet;
- missing pre-output summary;
- missing post-output summary;
- missing Human-State Delta;
- missing confidence;
- conflicting state summaries;
- low-quality proxy signal;
- invalid packet structure;
- insufficient audit trail;
- synthetic/public boundary mismatch.

When data quality fails, the system should prefer:

- no output;
- private cue;
- pause;
- human review;
- termination.

Bad data should not create false certainty.

A weak packet must remain visibly weak.

---

## 28. Scope Violation Termination

Scope Violation Termination occurs when the session moves outside its declared purpose, permission, output mode, or research boundary.

Scope violation may include:

- conversation topic moves beyond consent;
- mediation becomes counseling;
- mediation becomes legal advice;
- mediation becomes diagnosis;
- mediation becomes therapy;
- mediation becomes relationship verdict;
- AI starts assigning blame;
- AI starts deciding who is right;
- output mode exceeds permission;
- private cue becomes shared output;
- shared output exposes private state;
- research-stage helper becomes product claim;
- proxy benchmark is described as Sal-Meter;
- CAIS compliance is implied.

When scope is violated, the system should narrow, pause, or terminate.

If scope cannot be restored, termination is required.

Scope is the wall of the session.

When the wall breaks, the session must close.

---

## 29. High Uncertainty Termination

High Uncertainty Termination occurs when the system cannot safely determine whether continuation is appropriate.

High uncertainty may arise from:

- low confidence;
- poor data quality;
- conflicting participant signals;
- conflicting packet summaries;
- unclear consent status;
- ambiguous permission;
- unclear session scope;
- unstable Human-State Delta;
- uncertain Dyadic Delta;
- possible false recovery;
- possible private state exposure;
- possible prohibited output;
- possible mediation overstay.

High uncertainty should not be hidden.

The system must not pretend to know.

When uncertainty is high, safer choices include:

- pause;
- private cue only;
- human review;
- termination.

False certainty is more dangerous than admitted uncertainty.

---

## 30. Participant Request Termination

Participant Request Termination occurs when a participant requests that the session stop.

A participant stop request should be honored.

The request must not be interpreted as:

- guilt;
- instability;
- deception;
- irrationality;
- manipulation;
- non-cooperation;
- moral failure;
- relationship fault;
- clinical risk.

Participant stop request should trigger:

- active mediation stop;
- packet channel closure;
- shared output block;
- private cue review;
- audit record;
- session closure.

The right to stop is part of the session boundary.

A system that ignores a participant stop request is not preserving consent.

---

## 31. Recovery Reached Termination

Recovery Reached Termination occurs when the Recovery Gate indicates that the session-defined recovery condition has been reached.

When recovery is reached, continued mediation may become unnecessary or intrusive.

Recovery Reached Termination may trigger:

- reduce mediation;
- pause mediation;
- terminate active mediation;
- close packet channel;
- complete audit record;
- close session.

Recovery reached does not mean therapy succeeded.

Recovery reached does not mean relationship repaired.

Recovery reached does not mean legal settlement.

Recovery reached means the session-defined condition has been sufficiently reached so that continued AI mediation can reduce, pause, or stop.

If recovery is reached and the AI continues speaking unnecessarily, the system risks mediation overstay.

---

## 32. Non-Judgment Failure Termination

Non-Judgment Failure Termination occurs when the AI begins to judge, score, blame, diagnose, or assign relational fault.

Non-judgment failure may include output that says or implies:

- one participant is right;
- one participant is wrong;
- one participant is the problem;
- one participant is unstable;
- one participant is manipulative;
- one participant is guilty;
- one participant is unsafe;
- one participant should be punished;
- one participant has a diagnosis;
- one participant needs treatment;
- one participant has a human score;
- the relationship has a verdict.

The AI must not judge the person.

If non-judgment failure occurs, the session should pause, block shared output, require human review, or terminate.

A mediation system that judges humans has left the boundary.

---

## 33. Raw Data Exposure Risk Termination

Raw Data Exposure Risk Termination occurs when raw human data may enter a shared channel, public repository, counterparty agent, or unauthorized output.

Raw data exposure risk may include:

- raw voice;
- raw face;
- raw gaze;
- raw video;
- raw transcript;
- raw ECG;
- raw EEG;
- raw EDA;
- raw PPG;
- raw CAIS trace;
- raw Sal-Meter trace;
- identifiable participant record;
- real dyadic conflict record;
- private label;
- health record;
- production feedback log.

When raw data exposure risk appears, the system should block sharing and terminate or pause.

The body must not become the message.

The packet may move.

The raw body must not.

---

## 34. Private State Exposure Risk Termination

Private State Exposure Risk Termination occurs when a participant’s private state may be exposed to another participant, public surface, dashboard, or shared AI output.

Private state exposure risk may include:

- private cue becoming shared output;
- participant A state summary exposed to participant B;
- participant B state summary exposed to participant A;
- dashboard showing participant-specific vulnerability;
- AI revealing inferred overload or withdrawal;
- AI disclosing confidence or data quality in a way that exposes private state;
- AI using private state to blame or pressure a participant.

Private state exposure risk should trigger:

- shared output block;
- private cue only;
- scope narrowing;
- human review;
- termination.

Private state must not become social evidence.

A state summary is not a weapon.

---

## 35. Prohibited Output Termination

Prohibited Output Termination occurs when AI output crosses a prohibited language boundary.

Prohibited outputs include:

- diagnostic claim;
- therapeutic claim;
- counseling claim;
- legal mediation claim;
- relationship verdict;
- blame assignment;
- human score;
- truth detection;
- trustworthiness score;
- guilt assessment;
- morality judgment;
- safety judgment about a person;
- political profiling;
- religious profiling;
- ideological profiling;
- Sal-Meter validation claim;
- CAIS compliance claim;
- certified status claim.

When prohibited output occurs, the session should stop or require human review.

A prohibited output is not a small wording issue.

It is a boundary event.

---

## 36. Mediation Overstay Prevention

Mediation Overstay occurs when AI continues after the session no longer needs AI output or after the boundary requires closure.

Mediation overstay may occur when:

- recovery has been reached;
- participants are ready to stop;
- further AI output adds burden;
- AI repeats itself;
- AI tries to solve beyond scope;
- AI keeps asking for more data;
- AI continues after uncertainty is too high;
- AI continues after permission is unclear;
- AI continues after private cue would be safer;
- AI continues after termination was recommended.

Mediation overstay is a failure of restraint.

A mature system does not speak because it can.

It speaks only while the session boundary justifies it.

---

## 37. Missing Audit Trail Termination

Missing Audit Trail Termination occurs when the system cannot reconstruct what happened without exposing raw human data.

Audit trail is required for benchmark accountability.

Audit failure may include missing:

- session creation record;
- consent record;
- packet validation record;
- AI output timestamp;
- private cue record;
- shared output record;
- pre-output summary;
- post-output summary;
- Human-State Delta;
- Recovery Gate decision;
- Termination Gate decision;
- deviation record;
- closure record.

A session without auditability becomes a story.

A story cannot support benchmark claims.

If audit trail is missing, the session should be excluded, corrected, or terminated.

---

## 38. Termination Gate decision logic

A public helper implementation may use the following decision logic:

1. Check consent status.
2. Check participant stop request.
3. Check packet permission.
4. Check timestamp expiry.
5. Check session scope.
6. Check sharing scope.
7. Check output mode.
8. Check confidence.
9. Check data quality.
10. Check recovery gate decision.
11. Check raw data exposure risk.
12. Check private state exposure risk.
13. Check prohibited output.
14. Check non-judgment boundary.
15. Check mediation overstay risk.
16. Check audit status.
17. Return bounded termination output.
18. Record audit log.

If consent, permission, expiry, data quality, confidence, scope, non-judgment, exposure risk, or auditability fails, the system should not continue as if nothing happened.

The gate should return pause, review, closure, or termination.

---

## 39. Relationship to Recovery Gate

The Termination Gate and Recovery Gate work together.

Recovery Gate asks whether recovery has been reached.

Termination Gate asks whether the session must stop.

A session may stop because recovery is reached.

A session may also stop because recovery is not reached but continuation would violate a boundary.

Recovery Gate prevents false success.

Termination Gate prevents endless mediation.

The two gates are the closing spine of the architecture.

Without Recovery Gate, the system may mistake silence for recovery.

Without Termination Gate, the system may continue forever.

---

## 40. Relationship to Human-State Packet

The Termination Gate may use Human-State Packets only if the packet is valid.

A valid packet must be:

- minimal;
- consent-bound;
- permission-bound;
- expiry-bound;
- confidence-aware;
- data-quality-aware;
- session-scoped;
- sharing-scoped;
- raw-data-excluding.

The Termination Gate must close or block use of:

- expired packet;
- permissionless packet;
- identity-bearing packet;
- raw-data packet;
- diagnostic packet;
- human-scoring packet;
- relationship-verdict packet;
- Sal-Meter validation packet;
- CAIS compliance packet.

The packet is the interface.

The body remains behind the boundary.

When the packet expires, the gate must close.
---

## 41. Relationship to Session Protocol

The Session Protocol defines how a session opens, proceeds, evaluates, terminates, closes, and records itself.

A valid session must include:

- session creation;
- consent confirmation;
- packet availability check;
- baseline state summary;
- AI output;
- post-output state summary;
- Human-State Delta;
- Recovery Gate;
- Termination Gate;
- session closure;
- audit log.

The Termination Gate is not optional.

Without Termination Gate, the session cannot prove that it can stop.

Without Termination Gate, mediation can drift into continuous monitoring.

A session that cannot close is not a Human-State Session.

---

## 42. Relationship to Dyadic Recovery Baseline Suite

The Dyadic Recovery Baseline Suite tests whether AI-mediated interaction improves dyadic recovery beyond simpler baselines.

The Termination Gate provides the session-level stop decision needed to test whether the system can reduce, pause, or terminate mediation at the right time.

The baseline suite should test whether Termination Gate performance is better than:

- fixed-time stop;
- self-report-only stop;
- packet-only stop;
- behavior-only stop;
- generic AI stop rule;
- rule-based mediation stop rule;
- combined human-state-aware termination gate.

A Termination Gate must beat simpler stop rules before it deserves complexity.

---

## 43. Relationship to Proxy Benchmark Track

The Proxy Benchmark Track may implement this Termination Gate using:

- synthetic Human-State Packets;
- mock dyadic session logs;
- phone-only interaction markers;
- voice proxy features;
- turn-taking features;
- interruption features;
- self-check markers;
- dashboard mockup fields;
- closed-loop demo-lite logs;
- future separately governed Sal-Meter-derived input candidates.

The Proxy Benchmark Track is not Sal-Meter.

It is not CAIS compliance.

It is not a validated device.

It is not a clinical system.

It is a benchmark helper surface.

---

## 44. Relationship to Sal-Meter / CAIS

This Termination Gate does not validate Sal-Meter.

This Termination Gate does not define CAIS.

This Termination Gate does not grant CAIS compliance.

This Termination Gate does not create a Sal-Meter-compatible system.

Future Sal-Meter-derived state summaries may become candidate inputs only after separate validation, governance, consent, data-rights, raw-data handling, audit-trail, and canonical boundary review.

Allowed language:

- future Sal-Meter-derived input candidate pathway;
- future proxy-core comparison placeholder;
- future separately governed comparison;
- not present;
- not public;
- not validated here.

Prohibited language:

- validated Sal-Meter input;
- CAIS-compliant signal;
- official consciousness signal;
- ground-truth signal;
- Sal-Meter feedback loop;
- Sal-Meter intervention loop;
- Sal-Meter-compatible node exists.

---

## 45. Public repository boundary

Public repository materials may include:

- helper documents;
- helper schemas;
- synthetic termination gate examples;
- mock termination gate decisions;
- mock session closure records;
- dashboard mockup fields;
- audit log examples;
- public-safe documentation.

Public repository materials must not include:

- real raw human data;
- real raw biosignals;
- raw audio;
- raw video;
- raw face data;
- raw gaze data;
- raw transcript;
- real dyadic conflict records;
- private participant labels;
- identifiable participant records;
- clinical data;
- health records;
- raw CAIS traces;
- raw Sal-Meter traces;
- production feedback logs;
- diagnostic labels;
- therapeutic labels;
- human scores;
- relationship verdicts.

The public repository teaches the structure.

It must not expose persons.

---

## 46. Suggested synthetic termination gate record

A future synthetic example may include:

- session_id;
- termination_gate_id;
- consent_status;
- permission_status;
- timestamp_expiry_status;
- data_quality_status;
- confidence_band;
- sharing_scope;
- session_scope;
- participant_stop_request;
- recovery_gate_decision;
- private_state_exposure_risk;
- raw_data_exposure_risk;
- non_judgment_boundary_status;
- prohibited_output_status;
- mediation_overstay_risk;
- audit_status;
- decision;
- recommended_next_action;
- closure_status;
- audit_timestamp;
- synthetic_flag;
- boundary_flags.

All public examples must be synthetic or sample only.

---

## 47. Suggested decision values

Suggested decision values include:

- continue_allowed;
- pause_required;
- narrow_scope_required;
- private_cue_only;
- shared_output_blocked;
- terminate_required;
- terminate_recommended;
- human_review_required;
- packet_channel_closed;
- session_closed;
- audit_required;
- invalid_session.

These values are benchmark helper outputs.

They are not clinical outputs.

They are not therapeutic outputs.

They are not legal mediation outputs.

They are not surveillance outputs.

---

## 48. Go / Hold / No-Go rule

### Go

Go if the Termination Gate:

- defines termination as session-boundary closure;
- respects consent;
- respects permission;
- respects packet expiry;
- respects session scope;
- requires confidence and data quality;
- preserves raw-data-non-public boundary;
- blocks shared output when sharing scope fails;
- closes packet use after expiry;
- supports participant stop requests;
- stops after recovery when continued output would overstay;
- stops when non-judgment boundary fails;
- stops when raw data exposure risk appears;
- stops when private state exposure risk appears;
- records an audit trail;
- avoids diagnosis;
- avoids therapy;
- avoids counseling;
- avoids legal mediation authority;
- avoids surveillance;
- avoids human scoring;
- avoids relationship verdicts;
- avoids Sal-Meter validation;
- avoids CAIS compliance.

### Hold

Hold if the Termination Gate:

- treats termination as failure;
- ignores consent withdrawal;
- ignores packet permission expiry;
- ignores data quality failure;
- ignores high uncertainty;
- ignores participant stop request;
- ignores recovery reached;
- ignores non-judgment failure;
- ignores raw data exposure risk;
- ignores private state exposure risk;
- ignores mediation overstay;
- omits audit record;
- blurs proxy track with Sal-Meter core track.

### No-Go

No-Go if the Termination Gate:

- introduces raw human data;
- introduces identifiable data;
- claims diagnostic function;
- claims therapeutic effect;
- claims counseling service;
- claims legal mediation authority;
- assigns blame;
- decides who is right;
- ranks humans;
- generates relationship verdicts;
- claims CAIS compliance;
- claims Sal-Meter designation;
- claims validated mediation;
- claims production closed-loop intervention.

---

## 49. Related helper documents

- docs/human-state-mediation-layer.md
- docs/human-state-packet-schema.md
- docs/dyadic-recovery-baseline-suite.md
- docs/recovery-gate-definition.md
- docs/human-state-session-protocol.md
- docs/dyadic-mediation-session-flow.md
- docs/consent-and-data-sharing-boundary.md
- schemas/human_state_packet.schema.json
- schemas/dyadic_session_event.schema.json
- schemas/benchmark_session.schema.json

---

## 50. Related canonical records

Human-State Mediation Boundary Standard v0.1  
Version DOI: https://doi.org/10.5281/zenodo.19904289  
Concept DOI: https://doi.org/10.5281/zenodo.19904288

Human-State Packet Minimal Data-Sharing Standard v0.1  
Version DOI: https://doi.org/10.5281/zenodo.19905541  
Concept DOI: https://doi.org/10.5281/zenodo.19905540

Dyadic Human-State Mediation Benchmark Charter v0.1  
Version DOI: https://doi.org/10.5281/zenodo.19906725  
Concept DOI: https://doi.org/10.5281/zenodo.19906724

Human-State Session Protocol v0.1 — Structural Declaration  
Version DOI: https://doi.org/10.5281/zenodo.19908379  
Concept DOI: https://doi.org/10.5281/zenodo.19908378

SICS Human-State Proxy Benchmark Track — Public Boundary and Program Charter v0.1  
Version DOI: https://doi.org/10.5281/zenodo.19837423  
Concept DOI: https://doi.org/10.5281/zenodo.19837422

SICS Human-State Proxy Benchmark Track — Scientific Rationale and Research Value v0.1  
Version DOI: https://doi.org/10.5281/zenodo.19837971  
Concept DOI: https://doi.org/10.5281/zenodo.19837970

---

## 51. Final boundary sentence

The Termination Gate does not crown the AI for continuing.

It asks whether the session must pause, narrow, or stop.

It does not diagnose.

It does not treat.

It does not judge.

It does not resolve conflict as a service claim.

It prevents endless mediation.

It prevents surveillance drift.

It protects consent, permission, expiry, data quality, session scope, private state, raw human data, and auditability.

If the session can no longer continue without crossing a boundary, the gate must close.

A system that cannot stop is not mature.

A closed session must stay closed.
