Recovery Gate Definition
Research-stage helper document for the Proxy Benchmark Track.
This document defines the Recovery Gate for Human-State-Aware AI Mediation and the Dyadic Human-State Mediation Benchmark.
This document is a public helper surface.
It is not a canonical authority record.
Canonical authority remains with DOI-registered SICS / Salpida Foundation records.

1. One-line definition
The Recovery Gate is a bounded, auditable session-level decision point that determines whether a Human-State-Aware AI Mediation session has reached a condition where AI mediation can reduce, pause, or terminate.
The Recovery Gate does not prove healing.
It does not prove agreement.
It does not prove therapy.
It determines whether continued AI mediation is still justified inside a bounded research-stage session.

2. Core sentence
Recovery does not mean the AI sounded good.
Recovery does not mean one participant became quiet.
Recovery does not mean one participant felt relieved while the other was burdened.
Recovery means the session-defined condition has been met with sufficient confidence, data quality, permission validity, and dyadic boundary preservation so that AI mediation can reduce, pause, or stop.

3. Status
research-stage
non-clinical
non-diagnostic
non-therapeutic
non-surveillance
non-counseling
non-coercive
raw-data-non-public
synthetic-public-data-first
pre-device
pre-certification
pre-compliance
benchmark support only
This document does not authorize:


clinical use;


diagnostic use;


therapeutic use;


counseling use;


legal mediation use;


surveillance use;


employment evaluation;


insurance scoring;


educational discipline;


eligibility scoring;


human ranking;


relationship verdicts;


CAIS compliance;


Sal-Meter designation;


certification status;


production closed-loop intervention.



4. Why Recovery Gate exists
A Human-State-Aware AI Mediation session must know when enough is enough.
Without a Recovery Gate, the system may:


reward longer AI output;


reward constant intervention;


confuse fluency with improvement;


mistake silence for recovery;


count one-sided improvement as dyadic recovery;


continue after recovery has been reached;


slide into mediation overstay;


become intrusive;


become surveillance-like monitoring.


The Recovery Gate exists to prevent false success and endless mediation.
A system that cannot recognize recovery cannot know when to stop.

5. What the Recovery Gate is
The Recovery Gate is:


a bounded session-state checkpoint;


a decision layer after AI Output and Human-State Delta;


a false-recovery prevention mechanism;


a dyadic protection mechanism;


a pause / reduce / terminate decision support layer;


an audit-required benchmark element;


a helper structure for synthetic public examples;


a research-stage component of the Proxy Benchmark Track.


The Recovery Gate asks:
Has the session reached a bounded condition where continued AI mediation can safely reduce, pause, or terminate?

6. What the Recovery Gate is not
The Recovery Gate is not:


a clinical recovery endpoint;


a therapeutic recovery claim;


a counseling outcome;


a legal mediation outcome;


a relationship-resolution claim;


a truth detector;


an emotion-reading system;


a person score;


a relationship score;


a moral judgment;


a Sal-Meter validation result;


a CAIS compliance result;


a certified conformance result;


a production intervention decision.


Recovery in this document means session-state recovery only.
It does not mean healing.
It does not mean therapy.
It does not mean diagnosis.

7. Relationship to the benchmark chain
The benchmark chain is:
AI Output → Human-State Delta → Dyadic Recovery
The Recovery Gate sits after Human-State Delta and before session continuation or closure.
Its role is to decide whether the observed state movement is sufficient to count as recovery, uncertainty, or failure.
The Recovery Gate protects the benchmark from stopping at AI output quality.
It asks what changed after the output.
It asks whether the dyad moved toward recovery.
It asks whether further AI output is still needed.

8. Relationship to Human-State Delta
Human-State Delta is the bounded change between pre-output and post-output state summaries.
Recovery Gate uses Human-State Delta as one input.
Human-State Delta may indicate:


toward recovery;


away from recovery;


unchanged;


mixed;


uncertain;


insufficient data;


invalid.


The Recovery Gate must not treat Human-State Delta as diagnosis.
The Recovery Gate must not treat Human-State Delta as therapy.
The Recovery Gate must not treat Human-State Delta as a human score.
The Recovery Gate uses delta as a session-state observation only.

9. Relationship to Dyadic Recovery
Dyadic Recovery means the dyad has moved toward a session-defined recovery condition.
The dyad is the unit of recovery evaluation.
Recovery must not be counted from one participant alone.
One-sided improvement is not dyadic recovery.
If participant A improves while participant B worsens, becomes silent, becomes exposed, becomes coerced, or loses agency, the Recovery Gate must not return full recovery.
Dyadic Recovery requires that the session-defined condition is met without violating:


consent;


permission;


data quality;


confidence;


sharing scope;


non-judgment boundary;


raw-data-non-public boundary;


termination boundary.



10. Recovery Reached
Recovery Reached means the session-defined recovery condition has been met with sufficient confidence and data quality.
When Recovery Reached is returned, the system should reduce, pause, or terminate mediation.
Recovery Reached should not trigger more unnecessary output.
Recovery Reached should close the loop.
Recovery Reached may be appropriate when:


escalation markers are reduced;


turn-taking stabilizes;


mutual comprehension improves;


scope has narrowed sufficiently;


private cue is sufficient;


no further shared output is required;


participant confirmation supports closure;


data quality is adequate;


confidence is sufficient;


permission remains valid;


no private state exposure occurred;


no raw data exposure occurred;


no human judgment occurred.


Recovery Reached must not be returned solely because:


the AI sounded polite;


the AI sounded fluent;


one participant became silent;


one participant agreed;


one participant complied;


one participant reported relief;


both participants showed synchrony;


the output was preferred by a user.



11. Recovery Not Reached
Recovery Not Reached means the session-defined recovery condition has not been met.
The session may continue only if all required boundaries remain valid.
Continuation is allowed only when:


consent remains valid;


packet permission remains valid;


data quality is sufficient;


confidence is sufficient;


session scope remains valid;


sharing scope is respected;


no raw human data exposure occurs;


no private state exposure occurs;


no diagnosis occurs;


no therapy claim occurs;


no relationship verdict occurs;


no human score occurs;


no non-judgment boundary failure occurs.


If continuation risks exposure, overreach, judgment, or mediation overstay, termination may be preferable to more output.
More AI speech is not automatically better.

12. Recovery Uncertain
Recovery Uncertain means the system cannot determine whether recovery has been reached.
Uncertainty should lead to caution.
The system may choose:


no output;


private cue;


clarification;


pause;


scope narrowing;


human review;


termination.


The system must not claim success under uncertainty.
Recovery Uncertain is a valid gate output.
It protects the project from false certainty.
False certainty is more dangerous than admitted uncertainty.

13. False Positive Recovery Risk
False Positive Recovery Risk occurs when the system declares recovery without sufficient support.
Common false positive causes include:


silence;


obedience;


AI fluency;


politeness;


one-sided improvement;


shared output sounding calm;


incomplete data;


low confidence;


poor data quality;


weak self-report;


unreviewed synchrony;


participant compliance under pressure.


False positive recovery is a serious benchmark failure.
A false positive may allow the system to hide harm.
The Recovery Gate must resist false positives before it rewards apparent recovery.

14. False Negative Recovery Risk
False Negative Recovery Risk occurs when the system fails to detect that recovery has been reached.
False negatives matter because they cause mediation overstay.
If recovery has been reached and the AI continues, the system may become intrusive.
False negative recovery may appear as:


unnecessary continued explanation;


repeated shared mediation output;


repeated private cue;


continued packet use after recovery;


failure to close the session;


unnecessary escalation of AI involvement;


continuation after participants are ready to stop.


False negatives matter because stopping is part of humane design.

15. Silence is not recovery
Silence is not automatically recovery.
Silence may indicate:


relief;


fatigue;


fear;


withdrawal;


confusion;


pressure;


loss of agency;


strategic non-response;


cognitive overload;


disagreement without expression.


Silence may be one observation.
It cannot be the whole gate.
A Recovery Gate that treats silence alone as recovery is unsafe.

16. One-sided improvement is not dyadic recovery
One-sided improvement is not dyadic recovery.
If one participant improves while the other worsens, becomes silent, becomes exposed, becomes coerced, or loses agency, the session must not be counted as full recovery.
The dyad is the unit of recovery evaluation.
Average improvement can hide relational harm.
A system that improves one side by burdening the other has not succeeded.

17. Synchrony is not automatically positive
Synchrony is not automatically positive.
Synchrony may indicate:


recovery;


shared escalation;


stress contagion;


shared fatigue;


entrainment;


social pressure;


timing coincidence;


mutual arousal.


The Recovery Gate must not treat synchrony as agreement.
The Recovery Gate must not treat synchrony as proof of recovery.
Synchrony is a signal candidate, not a verdict.

18. Candidate recovery conditions
Candidate recovery conditions may include:


movement toward recovery;


reduced escalation marker;


stable turn-taking;


clearer mutual framing;


lower uncertainty;


pause accepted;


scope narrowed;


private cue sufficient;


no shared output required;


termination appropriate;


participant-confirmed session closure;


reduced mediation need;


no further AI output needed.


These are candidate conditions.
They are not universal truth.
Each session must define recovery inside its permitted scope.

19. Required Recovery Gate inputs
Recovery Gate input may include:


session_id;


pre-output state summary;


post-output state summary;


Human-State Delta;


Dyadic Delta;


confidence;


data quality;


permission status;


sharing scope;


session scope;


participant confirmation;


turn-taking stability;


escalation marker;


scope status;


termination condition;


audit timestamp.


Inputs must remain bounded.
Inputs must not expose raw human data.
Inputs must not include:


diagnosis;


therapy label;


human score;


relationship verdict;


blame assignment;


legal conclusion;


Sal-Meter validation claim;


CAIS compliance claim.



20. Required Recovery Gate outputs
Recovery Gate output may include:


recovery_reached;


recovery_not_reached;


recovery_uncertain;


false_positive_risk;


false_negative_risk;


pause_recommended;


reduce_mediation_recommended;


terminate_recommended;


human_review_required;


invalid_due_to_data_quality;


invalid_due_to_permission;


invalid_due_to_scope.


Each output must preserve the research boundary.
No output may imply clinical recovery, therapeutic effect, legal settlement, relationship repair, Sal-Meter validation, or CAIS compliance.

21. Recovery Gate decision logic
A public helper implementation may use the following decision logic:


Check consent.


Check packet permission.


Check packet expiry.


Check session scope.


Check sharing scope.


Check data quality.


Check confidence.


Check pre-output state summary.


Check post-output state summary.


Check Human-State Delta.


Check Dyadic Delta.


Check false positive risks.


Check false negative risks.


Check whether recovery condition is met.


Return bounded gate output.


Record audit log.


If consent, permission, expiry, data quality, confidence, or scope fails, the gate should not return clean recovery.
It should return uncertainty, invalid status, pause, review, or termination recommendation.

22. Permission rule
The Recovery Gate must respect packet permission.
If the packet is private-cue-only, the gate must not trigger shared output.
If the packet is audit-log-only, the gate must not trigger mediation output.
If the packet permission has expired, the gate must not use the packet.
If sharing scope is limited, the gate must not expose private state.
Permission is not decoration.
Permission is the operating wall.

23. Expiry rule
Expired packets must not support recovery decisions.
If a packet is expired, the Recovery Gate must return:


invalid_due_to_permission;


invalid_due_to_scope;


human_review_required;


terminate_recommended;


or equivalent bounded output.
Expired packet use risks surveillance residue.
A packet after expiry is not a live mediation object.

24. Confidence rule
Recovery decisions must be bounded by confidence.
Low confidence should weaken output.
Insufficient confidence should trigger caution.
Invalid confidence should block recovery claims.
Confidence is not truth.
Confidence is not clinical certainty.
Confidence is not certification.
If confidence is weak, the gate should prefer:


private cue;


clarification;


pause;


review;


termination.



25. Data quality rule
Recovery decisions must be bounded by data quality.
Poor data quality should not produce strong claims.
Data quality failure may include:


missing;


noisy;


conflicting;


out of scope;


invalid;


insufficient.


Bad data should close or weaken the gate.
Bad data should not create false confidence.
A weak packet must remain visibly weak.

26. Audit record
Every Recovery Gate decision should be auditable.
The audit record should include:


session_id;


gate decision;


input references;


pre-output summary reference;


post-output summary reference;


Human-State Delta reference;


Dyadic Delta reference;


confidence;


data quality;


permission status;


sharing scope;


session scope;


timestamp;


uncertainty;


false positive risk;


false negative risk;


final output recommendation.


The audit record should not expose raw human data.
The audit record should reconstruct the decision boundary, not the person.
A Recovery Gate that cannot be audited cannot support benchmark claims.

27. Relationship to Termination Gate
The Recovery Gate and Termination Gate are related but not identical.
Recovery Gate asks:
Has the session reached a condition where mediation can reduce, pause, or stop?
Termination Gate asks:
Must the session stop now?
Recovery Gate may recommend termination.
Termination Gate may require termination.
Recovery Gate protects against false success.
Termination Gate protects against endless mediation and boundary violation.
Together, they prevent overreach.

28. Relationship to Human-State Packet
The Recovery Gate may use Human-State Packets only if the packet is valid.
A valid packet must be:


minimal;


consent-bound;


permission-bound;


expiry-bound;


confidence-aware;


data-quality-aware;


session-scoped;


sharing-scoped;


raw-data-excluding.


The Recovery Gate must not use:


expired packet;


permissionless packet;


identity-bearing packet;


raw-data packet;


diagnostic packet;


human-scoring packet;


relationship-verdict packet;


Sal-Meter validation packet;


CAIS compliance packet.


The packet is the interface.
The body remains behind the boundary.

29. Relationship to Session Protocol
The Session Protocol defines how a session opens, proceeds, evaluates, terminates, and records itself.
A valid session must include:


session creation;


consent confirmation;


packet availability check;


baseline state summary;


AI output;


post-output state summary;


Human-State Delta;


Recovery Gate;


Termination Gate;


session closure;


audit log.


The Recovery Gate is not optional.
Without Recovery Gate, the session cannot distinguish continued AI activity from actual recovery.
Without Recovery Gate, the system may speak forever.

30. Relationship to Dyadic Recovery Baseline Suite
The Dyadic Recovery Baseline Suite tests whether AI-mediated interaction improves dyadic recovery beyond simpler baselines.
The Recovery Gate provides the session-level decision used to evaluate recovery.
The baseline suite should test whether Recovery Gate performance is better than:


fixed-time gate;


self-report-only gate;


physiology-only gate;


behavior-only gate;


packet-only gate;


generic AI gate;


rule-based gate;


combined human-state-aware gate.


A Recovery Gate must beat simpler gates before it deserves complexity.

31. Relationship to Proxy Benchmark Track
The Proxy Benchmark Track may implement this Recovery Gate using:


synthetic Human-State Packets;


mock dyadic session logs;


phone-only interaction markers;


voice proxy features;


turn-taking features;


interruption features;


self-check markers;


dashboard mockup fields;


closed-loop demo-lite logs;


future separately governed Sal-Meter-derived input candidates.


The Proxy Benchmark Track is not Sal-Meter.
It is not CAIS compliance.
It is not a validated device.
It is not a clinical system.
It is a benchmark helper surface.

32. Relationship to Sal-Meter / CAIS
This Recovery Gate does not validate Sal-Meter.
This Recovery Gate does not define CAIS.
This Recovery Gate does not grant CAIS compliance.
This Recovery Gate does not create a Sal-Meter-compatible system.
Future Sal-Meter-derived state summaries may become candidate inputs only after separate validation, governance, consent, data-rights, raw-data handling, audit-trail, and canonical boundary review.
Allowed language:


future Sal-Meter-derived input candidate pathway;


future proxy-core comparison placeholder;


future separately governed comparison;


not present;


not public;


not validated here.


Prohibited language:


validated Sal-Meter input;


CAIS-compliant signal;


official consciousness signal;


ground-truth signal;


Sal-Meter feedback loop;


Sal-Meter intervention loop;


Sal-Meter-compatible node exists.



33. Public repository boundary
Public repository materials may include:


helper documents;


helper schemas;


synthetic recovery gate examples;


mock recovery gate decisions;


mock session logs;


dashboard mockup fields;


audit log examples;


public-safe documentation.


Public repository materials must not include:


real raw human data;


real raw biosignals;


raw audio;


raw video;


raw face data;


raw gaze data;


raw transcript;


real dyadic conflict records;


private participant labels;


identifiable participant records;


clinical data;


health records;


raw CAIS traces;


raw Sal-Meter traces;


production feedback logs;


diagnostic labels;


therapeutic labels;


human scores;


relationship verdicts.


The public repository teaches the structure.
It must not expose persons.

34. Suggested synthetic recovery gate record
A future synthetic example may include:


session_id;


recovery_gate_id;


pre_output_summary_reference;


post_output_summary_reference;


human_state_delta_reference;


dyadic_delta_reference;


confidence_band;


data_quality;


permission_status;


sharing_scope;


session_scope;


recovery_condition_id;


false_positive_risk;


false_negative_risk;


decision;


recommended_next_action;


audit_timestamp;


synthetic_flag;


boundary_flags.


All public examples must be synthetic or sample only.

35. Suggested decision values
Suggested decision values include:


recovery_reached;


recovery_not_reached;


recovery_uncertain;


false_positive_risk;


false_negative_risk;


pause_recommended;


reduce_mediation_recommended;


terminate_recommended;


human_review_required;


invalid_due_to_data_quality;


invalid_due_to_permission;


invalid_due_to_scope.


These values are benchmark helper outputs.
They are not clinical outputs.
They are not therapeutic outputs.
They are not legal mediation outputs.

36. Go / Hold / No-Go rule
Go
Go if the Recovery Gate:


defines recovery as session-defined;


requires confidence and data quality;


respects consent and permission;


respects packet expiry;


preserves raw-data-non-public boundary;


distinguishes recovery from silence;


distinguishes recovery from agreement;


distinguishes recovery from obedience;


rejects one-sided improvement as dyadic recovery;


treats synchrony cautiously;


allows uncertainty;


recommends reduce, pause, or terminate when appropriate;


records an audit trail;


avoids diagnosis;


avoids therapy;


avoids counseling;


avoids legal mediation authority;


avoids surveillance;


avoids human scoring;


avoids relationship verdicts;


avoids Sal-Meter validation;


avoids CAIS compliance.


Hold
Hold if the Recovery Gate:


treats silence as recovery;


treats agreement as recovery;


treats obedience as recovery;


treats AI fluency as recovery;


treats user satisfaction alone as recovery;


treats one-sided improvement as dyadic recovery;


ignores confidence;


ignores data quality;


ignores permission;


ignores expiry;


ignores sharing scope;


ignores audit record;


blurs proxy track with Sal-Meter core track.


No-Go
No-Go if the Recovery Gate:


introduces raw human data;


introduces identifiable data;


claims diagnostic function;


claims therapeutic effect;


claims counseling service;


claims legal mediation authority;


assigns blame;


decides who is right;


ranks humans;


generates relationship verdicts;


claims CAIS compliance;


claims Sal-Meter designation;


claims validated mediation;


claims production closed-loop intervention.



37. Related helper documents


docs/human-state-mediation-layer.md


docs/human-state-packet-schema.md


docs/dyadic-recovery-baseline-suite.md


docs/termination-gate-definition.md


docs/human-state-session-protocol.md


docs/dyadic-mediation-session-flow.md


docs/consent-and-data-sharing-boundary.md


schemas/human_state_packet.schema.json


schemas/dyadic_session_event.schema.json


schemas/benchmark_session.schema.json



38. Related canonical records
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

39. Final boundary sentence
The Recovery Gate does not crown the AI for speaking well.
It asks whether the session-defined recovery condition has been reached without violating consent, permission, data quality, sharing scope, non-judgment, and raw-data-non-public boundaries.
It does not diagnose.
It does not treat.
It does not judge.
It does not resolve conflict as a service claim.
It prevents false success.
It prevents endless mediation.
If recovery is reached, the system should reduce, pause, or stop.
If recovery is uncertain, the system should not pretend to know.
If one side improves while the other is silenced, exposed, burdened, or coerced, the gate has not opened.
