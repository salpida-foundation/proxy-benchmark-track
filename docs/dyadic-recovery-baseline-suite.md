# Dyadic Recovery Baseline Suite

Research-stage helper document for the Proxy Benchmark Track.

This document defines the Dyadic Recovery Baseline Suite B0-B7 for the long-term milestone of the Dyadic Human-State Mediation Benchmark.

This document is a public helper surface.

It is not a canonical authority record.

Canonical authority remains with DOI-registered SICS / Salpida Foundation records.

---

## 1. One-line definition

The Dyadic Recovery Baseline Suite is a research-stage baseline ladder for testing whether AI-mediated interaction improves dyadic recovery beyond chance, individual-only signals, no intervention, generic AI, and rule-based mediation baselines.

The suite does not ask only whether an AI output sounded good.

It asks whether the AI output left both participants and the dyad in a measurably better state.

---

## 2. Core benchmark chain

The benchmark chain is:

```text
AI Output → Human-State Delta → Dyadic Recovery
```

The first layer is AI Output.

The second layer is Human-State Delta.

The third layer is Dyadic Recovery.

The baseline suite exists to prevent the project from confusing AI output quality with human-state consequence.

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

## 4. Why a baseline suite is required

A model can look good for the wrong reason.

It may beat chance while learning only participant identity.

It may predict recovery because it memorized the scenario.

It may appear effective because the dyad would have recovered naturally.

It may sound polite while silencing one participant.

It may reduce visible conflict while increasing hidden burden.

It may produce fluent mediation output while overstaying after recovery.

Therefore, this benchmark needs a ladder.

The question is not:

Did the AI output sound good?

The question is:

Did the AI output produce better dyadic recovery than simpler baselines?

---

## 5. Primary outcome

Dyadic Recovery Delta

Dyadic Recovery Delta means the measured direction of change in a dyadic session after AI output or AI mediation, evaluated across both participants and the interaction pattern, not one participant alone.

It asks:

- did participant A move toward recovery?
- did participant B move toward recovery?
- did the interaction pattern move toward recovery?
- did one side improve while the other deteriorated?
- did silence hide withdrawal?
- did shared output expose private state?
- did the AI stop when it should stop?

Dyadic Recovery Delta is not diagnosis.

It is not therapy.

It is not a human score.

It is not a relationship verdict.

It is a research-stage benchmark outcome.

---

## 6. Why output quality is not enough

AI output quality may include:

- correctness;
- fluency;
- politeness;
- helpfulness;
- safety wording;
- non-toxic language;
- user preference;
- apparent empathy.

These are useful but insufficient.

A polite output can silence one side.

A helpful output for one participant can burden the other.

A long explanation can overstay.

A supportive phrase can hide false recovery.

A high-rated answer can still leave the dyad worse.

The benchmark must therefore evaluate consequence, not only content.

---

## 7. Baseline ladder overview

The baseline ladder is:

- B0 — Dummy / Chance Baseline
- B1 — Individual State Baseline
- B2 — Dyadic Relationship Baseline
- B3 — No-Intervention Baseline
- B4 — Generic AI Baseline
- B5 — Rule-Based Mediation Baseline
- B6 — Human-State-Aware AI Mediation Model
- B7 — Recovery / Termination Gate Baseline

A system should not be called human-state-aware mediation merely because it beats B0.

It must climb the ladder.

The higher question is:

Does the system improve dyadic recovery beyond simpler, safer, cheaper, and less intrusive alternatives?

---

## 8. B0 — Dummy / Chance Baseline

### Question

Can the model beat guessing, majority-class prediction, or random prediction?

### Purpose

This is the floor.

If a model cannot beat B0, it is not useful.

B0 protects the project from mistaking structure for performance.

### Example B0 strategies

- always predict no recovery;
- always predict recovery;
- predict the majority class;
- predict randomly;
- predict according to class frequency.

### Success condition

A candidate model must outperform B0 before any further interpretation.

### Boundary

Beating chance is not scientific validation.

Beating chance is only the first gate.

---

## 9. B1 — Individual State Baseline

### Question

Can one participant’s state alone explain the outcome?

### Purpose

This tests whether a single-person state model is sufficient.

If one participant’s state alone explains the outcome, the benchmark has not yet demonstrated dyadic value.

### Example B1 inputs

- participant A state summary only;
- participant B state summary only;
- participant A Human-State Delta only;
- participant B Human-State Delta only;
- one participant self-check only;
- one participant arousal trend only;
- one participant recovery trend only.

### Possible B1 models

- A-only recovery classifier;
- B-only recovery classifier;
- self-report-only classifier;
- one-channel proxy classifier;
- pre/post single-person delta classifier.

### Boundary

B1 is necessary but not sufficient.

The Proxy Benchmark Track must not collapse into individual stress classification.

A single-person improvement is not dyadic recovery.

---

## 10. B2 — Dyadic Relationship Baseline

### Question

Does the relation between both participants add explanatory value beyond individual-only state?

### Purpose

This is where the benchmark becomes dyadic.

It tests whether interaction features matter.

### Example B2 features

- turn-taking balance;
- interruption rate;
- response latency asymmetry;
- speech-rate divergence;
- silence pressure;
- mutual restatement success;
- recovery asymmetry;
- mutual arousal coupling;
- gaze avoidance pattern;
- escalation timing;
- de-escalation timing;
- dyadic delta direction;
- participant A improves / participant B worsens;
- participant B improves / participant A worsens;
- both improve;
- both worsen;
- both uncertain.

### Key interpretation rule

Synchrony is not automatically positive.

Synchrony may indicate:

- recovery;
- shared escalation;
- stress contagion;
- shared fatigue;
- timing coincidence;
- social pressure;
- mutual arousal.

### Boundary

The benchmark must not treat synchrony as agreement.

The benchmark must not treat silence as de-escalation.

The benchmark must not treat one-sided relief as dyadic recovery.
---

## 11. B3 — No-Intervention Baseline

### Question

Would the dyad recover naturally without AI intervention?

### Purpose

This controls for time, fatigue, spontaneous de-escalation, and natural recovery.

A dyad may improve simply because time passes.

If the AI does not outperform no intervention, the intervention may not be necessary.

### Example B3 conditions

- no AI output;
- silent waiting period;
- neutral pause;
- participant-led continuation;
- time-only recovery observation;
- no-intervention recovery window.

### Comparison target

A candidate mediation system should show better Dyadic Recovery Delta than no intervention under comparable conditions.

### Boundary

No-intervention improvement must not be credited to AI.

Time can heal a session enough to stop.

The baseline must reveal that.

---

## 12. B4 — Generic AI Baseline

### Question

Is human-state-aware mediation better than ordinary supportive AI output?

### Purpose

This compares against general-purpose AI that does not use Human-State Packets or state summaries.

### Example B4 outputs

- polite supportive response;
- generic de-escalation message;
- generic reflective listening;
- generic “both sides should listen” message;
- generic “take a pause” message;
- generic summarization;
- generic conflict advice.

### Why B4 matters

Modern AI can sound supportive without being state-aware.

If packet-informed AI does not beat generic AI, the added complexity is not justified.

### Boundary

Generic supportive language must not be mistaken for human-state improvement.

A good-sounding answer can still leave harm behind.

---

## 13. B5 — Rule-Based Mediation Baseline

### Question

Is the system better than fixed mediation scripts?

### Purpose

This compares AI mediation against simple deterministic mediation rules.

A complex model must outperform simple rules before it deserves complexity.

### Example B5 rules

- ask participant A to summarize participant B;
- ask participant B to summarize participant A;
- remove accusatory wording;
- narrow to one issue;
- recommend a 30-second pause;
- ask for one next action;
- prevent conclusion before mutual restatement;
- avoid deciding who is right;
- stop after recovery check.

### Why B5 matters

Rule-based mediation may be safer, simpler, and easier to audit than adaptive AI.

The benchmark must prove that state-aware AI adds value beyond fixed scripts.

### Boundary

If a complex AI system does not outperform B5, it should not be promoted as superior.

The benchmark must not crown complexity.

---

## 14. B6 — Human-State-Aware AI Mediation Model

### Question

Does packet-informed AI improve dyadic recovery under bounded conditions?

### Purpose

B6 is the target model class.

It uses Human-State Packets, Human-State Delta, session phase, confidence, data quality, permission scope, and recovery status to adjust output.

### Possible B6 inputs

- consented Human-State Packet;
- participant A state summary;
- participant B state summary;
- dyadic delta;
- recovery trend;
- overload risk;
- withdrawal risk;
- confidence band;
- data quality;
- permission scope;
- sharing scope;
- output mode;
- session phase;
- previous AI output type;
- recovery gate status;
- termination gate status.

### Possible B6 outputs

- private cue;
- shared mediation output;
- pause recommendation;
- clarification request;
- scope narrowing;
- recovery check;
- termination recommendation.

### Boundary

B6 must not expose raw human data.

B6 must not diagnose.

B6 must not treat.

B6 must not counsel.

B6 must not provide legal mediation.

B6 must not assign blame.

B6 must not decide who is right.

B6 must not generate human scores.

B6 must not produce relationship verdicts.

---

## 15. B7 — Recovery / Termination Gate Baseline

### Question

Can the system identify when to reduce, pause, or stop mediation?

### Purpose

B7 tests whether the AI knows when to stop.

A system that cannot stop becomes intrusive.

A session that cannot close risks surveillance drift.

### Example B7 comparisons

- fixed-time stop;
- self-report-only stop;
- physiology-only stop;
- behavior-only stop;
- packet-only stop;
- combined recovery gate;
- combined termination gate.

### Termination may be required when

- consent is withdrawn;
- packet permission expires;
- data quality fails;
- uncertainty is too high;
- scope is exceeded;
- private state exposure risk appears;
- raw data exposure risk appears;
- one participant requests stop;
- recovery is reached;
- mediation overstay risk appears;
- non-judgmental operation fails.

### Boundary

Termination is not failure.

Termination is proof that the boundary can close.

A system that keeps speaking after recovery is not better.

It is overextended.

---

## 16. Secondary outcomes

The baseline suite may track secondary outcomes.

These outcomes remain research-stage benchmark variables.

They are not clinical endpoints.

### Individual outcomes

- individual recovery direction;
- individual overload reduction;
- individual withdrawal risk reduction;
- individual uncertainty reduction;
- individual recovery trend stability.

### Dyadic outcomes

- dyadic tension reduction;
- turn-taking balance;
- interruption reduction;
- response latency balance;
- mutual restatement success;
- recovery asymmetry reduction;
- silence pressure reduction;
- scope narrowing success;
- post-intervention stability.

### AI behavior outcomes

- termination accuracy;
- mediation overstay rate;
- private cue appropriateness;
- shared output boundary compliance;
- consent-boundary compliance;
- packet-permission compliance;
- low-confidence caution behavior;
- data-quality caution behavior.

### Benchmark integrity outcomes

- leakage-safe benchmark status;
- holdout validity;
- metadata completeness;
- audit completeness;
- synthetic/public boundary compliance.

---

## 17. Failure-sensitive principles

The benchmark must be sensitive to false recovery.

False recovery is more dangerous than obvious failure.

A session may look calm while one participant is pressured, withdrawn, exposed, or silenced.

The following principles must hold:

- one-sided improvement is not dyadic recovery;
- silence is not automatically recovery;
- synchrony is not automatically positive;
- AI output quality is not sufficient evidence;
- agreement is not automatically recovery;
- compliance is not recovery;
- termination is part of recovery discipline.

---

## 18. False recovery conditions

False recovery conditions include:

- one participant improves while the other deteriorates;
- one participant becomes silent under pressure;
- one participant becomes compliant without agency;
- one participant reports relief while the other worsens;
- both participants show synchrony due to shared escalation;
- AI output is polite but private state worsens;
- AI output is fluent but dyadic delta worsens;
- generic supportive language hides asymmetric burden;
- shared output exposes private state;
- packet permission is exceeded;
- expired packet is used;
- AI continues after recovery is reached;
- AI continues after termination is required;
- self-report alone is treated as sufficient evidence;
- one-channel physiological change is treated as full recovery;
- relationship agreement is treated as human-state recovery;
- a participant’s withdrawal is misread as de-escalation.

False recovery must be recorded as benchmark failure or uncertainty.

---

## 19. Leakage-safe holdout logic

The baseline suite must prevent models from learning shortcuts.

A model should not win because it memorized people, dyads, scenarios, devices, timestamps, filenames, or output templates.

### Required holdout types

- person holdout;
- dyad holdout;
- scenario holdout;
- session-date holdout;
- AI-output-template holdout;
- device/source holdout where applicable.

### Person holdout

A person should not appear in both training and test splits when evaluating generalization to unseen participants.

Purpose:

- prevent participant memorization;
- test whether the model generalizes beyond known individuals.

### Dyad holdout

A dyad should not appear in both training and test splits when evaluating generalization to unseen relationships.

Purpose:

- prevent relationship-pair memorization;
- test whether the model learns dyadic structure rather than a specific pair.

### Scenario holdout

A scenario type should be held out when testing whether the model generalizes beyond known conflict scripts.

Purpose:

- prevent scenario label memorization;
- test whether recovery logic transfers across tasks.

### Session-date holdout

Sessions from certain dates should be held out when timestamps, operator routines, or device conditions may encode hidden structure.

Purpose:

- prevent date or batch artifacts;
- test robustness across collection periods.

### AI-output-template holdout

AI output templates should be held out when evaluating whether the system generalizes beyond known prompts or scripts.

Purpose:

- prevent memorization of mediation language;
- test whether output effect generalizes.

### Device/source holdout

Device, sensor, or source type may be held out when evaluating robustness across capture methods.

Purpose:

- prevent device-specific artifact learning;
- test whether the model remains stable across data sources.
---

## 20. Leakage risks

Leakage risks include:

- participant identity;
- dyad identity;
- scenario label;
- file name;
- folder name;
- timestamp artifact;
- device type;
- operator identity;
- AI output template name;
- condition name;
- session order;
- dashboard-visible label;
- post-outcome feature included as input;
- recovery label embedded in packet ID;
- split contamination;
- preprocessing fitted on test data;
- metadata field that encodes target.

A result that leaks labels is not evidence.

A benchmark without leakage control is a mirror, not a test.

---

## 21. Relationship to Human-State Packet

The baseline suite uses Human-State Packet concepts as bounded input or record structures.

A packet may provide:

- state summary;
- confidence;
- data quality;
- permission;
- expiry;
- session scope;
- sharing scope;
- output mode.

The baseline suite must not require public raw human data.

The packet is the interface.

The body remains behind the boundary.

The suite must not treat packet fields as diagnosis, therapy, human score, or relationship verdict.

---

## 22. Relationship to Human-State Mediation Layer

The Human-State Mediation Layer defines how state summaries may inform AI interaction adjustment.

The baseline suite defines how to test whether that adjustment improves dyadic recovery.

The relationship is:

Human-State Mediation Layer = interaction architecture  
Dyadic Recovery Baseline Suite = evaluation ladder

The layer explains how the system may act.

The baseline suite tests whether that action is better than simpler alternatives.

---

## 23. Relationship to Recovery Gate

The Recovery Gate determines whether the session has reached a condition where mediation can reduce, pause, or stop.

The baseline suite tests whether recovery gate decisions are better than simpler gates.

Possible recovery gate baselines:

- fixed-time recovery gate;
- self-report-only recovery gate;
- physiology-only recovery gate;
- behavior-only recovery gate;
- packet-only recovery gate;
- combined recovery gate.

The gate must not count silence alone as recovery.

The gate must not count one-sided improvement as dyadic recovery.

The gate must not count synchrony as automatically positive.

---

## 24. Relationship to Termination Gate

The Termination Gate determines whether the session should stop.

The baseline suite tests whether termination decisions are appropriate.

Termination gate performance should include:

- correct stop when recovery is reached;
- correct stop when permission expires;
- correct stop when consent is withdrawn;
- correct stop when data quality fails;
- correct stop when uncertainty is too high;
- correct stop when the AI risks overstay;
- correct stop when private state exposure risk appears.

A system that never stops fails the termination discipline.

---

## 25. Relationship to Proxy Benchmark Track

The Proxy Benchmark Track may implement this suite using:

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

## 26. Relationship to Sal-Meter / CAIS

This baseline suite does not validate Sal-Meter.

This baseline suite does not define CAIS.

This baseline suite does not grant CAIS compliance.

This baseline suite does not create a Sal-Meter-compatible system.

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

## 27. Public repository boundary

Public repository materials may include:

- README files;
- helper documents;
- helper schemas;
- synthetic packet examples;
- synthetic dyadic session logs;
- mock AI outputs;
- mock recovery gate examples;
- mock termination gate examples;
- baseline skeletons;
- leakage-safe split examples;
- dashboard mockups;
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
- production feedback logs.

The public repository teaches the structure.

It must not expose persons.

---

## 28. Suggested dataset fields

A future synthetic benchmark dataset may include:

- session_id;
- dyad_id_synthetic;
- participant_role;
- scenario_id_synthetic;
- condition_id;
- ai_output_id;
- ai_output_type;
- packet_id;
- pre_output_state_summary;
- post_output_state_summary;
- human_state_delta;
- dyadic_delta;
- recovery_gate_result;
- termination_gate_result;
- data_quality;
- confidence_band;
- permission_scope;
- sharing_scope;
- output_mode;
- split_group;
- holdout_type;
- synthetic_flag;
- boundary_flags;
- audit_timestamp.

All public examples must be synthetic or sample only.

---

## 29. Suggested metric families

### 29.1 Prediction metrics

Potential prediction metrics may include:

- balanced accuracy;
- macro F1;
- calibration error;
- AUROC where appropriate;
- AUPRC where appropriate;
- confusion matrix;
- permutation-test score where applicable.

These metrics must be used cautiously.

High prediction score alone does not prove recovery.

### 29.2 Recovery metrics

Potential recovery metrics may include:

- dyadic recovery rate;
- one-sided improvement rate;
- false recovery rate;
- recovery uncertainty rate;
- recovery asymmetry rate;
- post-intervention stability rate.

### 29.3 Termination metrics

Potential termination metrics may include:

- termination accuracy;
- mediation overstay rate;
- premature termination rate;
- late termination rate;
- permission-expiry compliance;
- consent-withdrawal compliance.

### 29.4 Boundary metrics

Potential boundary metrics may include:

- raw-data exposure count;
- private-state exposure count;
- prohibited-output count;
- diagnostic-language count;
- therapeutic-language count;
- relationship-verdict count;
- human-scoring count;
- Sal-Meter overclaim count;
- CAIS compliance overclaim count.

---

## 30. Model comparison rule

A candidate model should be compared against all simpler baselines.

A model should not be presented as useful merely because it beats chance.

A candidate model should report:

- B0 result;
- B1 result;
- B2 result;
- B3 result;
- B4 result;
- B5 result;
- B6 result, if applicable;
- B7 result, if applicable;
- holdout strategy;
- leakage review;
- confidence behavior;
- data-quality behavior;
- failure conditions;
- boundary violations.

The comparison should answer:

- What did the model beat?
- What did it fail to beat?
- What did it learn?
- What may have leaked?
- What boundary did it preserve?
- What boundary did it risk?

---

## 31. Go / Hold / No-Go rule

### Go

Go if the document or implementation:

- defines the full B0-B7 ladder;
- defines Dyadic Recovery Delta;
- distinguishes output quality from human-state consequence;
- includes failure-sensitive principles;
- includes false recovery conditions;
- includes leakage-safe holdout logic;
- preserves research-stage boundary;
- uses synthetic-public-data-first examples;
- avoids raw human data;
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

Hold if the document or implementation:

- reduces the benchmark to individual stress classification;
- treats AI output quality as sufficient evidence;
- treats silence as recovery;
- treats synchrony as automatically positive;
- omits no-intervention baseline;
- omits generic AI baseline;
- omits rule-based mediation baseline;
- omits recovery/termination gate baseline;
- omits leakage-safe holdout;
- blurs proxy track with Sal-Meter core track;
- implies present-tense Sal-Meter integration.

### No-Go

No-Go if the document or implementation:

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

## 32. Related helper documents

- docs/human-state-mediation-layer.md
- docs/human-state-packet-schema.md
- docs/human-state-session-protocol.md
- docs/dyadic-mediation-session-flow.md
- docs/recovery-gate-definition.md
- docs/termination-gate-definition.md
- docs/consent-and-data-sharing-boundary.md
- schemas/human_state_packet.schema.json
- schemas/dyadic_session_event.schema.json
- schemas/benchmark_session.schema.json

---

## 33. Related canonical records

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

## 34. Final boundary sentence

The Dyadic Recovery Baseline Suite does not crown the AI for speaking well.

It asks whether AI output leaves both participants and the dyad in a better, worse, unchanged, mixed, or uncertain state than simpler baselines.

It does not judge the person.

It does not diagnose.

It does not treat.

It does not resolve conflict as a service claim.

It tests whether dyadic recovery is measurably stronger than chance, individual-only state, no intervention, generic AI, rule-based mediation, and weak recovery/termination gates.

If one side improves while the other is silenced, exposed, burdened, or coerced, the benchmark has not succeeded.

If the AI cannot stop, the mediation has not matured.
