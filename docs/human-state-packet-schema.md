# Human-State Packet Schema

Research-stage helper document for the Proxy Benchmark Track.

This document defines the Human-State Packet as a minimal, consent-bound, permission-bound, expiry-bound, confidence-aware, data-quality-aware, session-scoped, sharing-scoped, raw-data-excluding state-summary object.

This document is a human-readable helper document.

The companion machine-readable helper schema is intended to be:

- schemas/human_state_packet.schema.json

This document does not create canonical authority.

Canonical authority remains with DOI-registered SICS / Salpida Foundation records.

---

## 1. One-line definition

A Human-State Packet is a bounded state-summary object used to exchange only the minimum consented human-state summary needed for research-stage Human-State-Aware AI Mediation.

It is not the body.

It is not the raw signal.

It is not a diagnosis.

It is not a human score.

It is not a relationship verdict.

---

## 2. Core rule

Device does not share the body.

Device shares a consented state summary.

Mediation AI does not judge the person.

It adjusts the interaction.

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

## 4. Why the packet exists

Human-State-Aware AI Mediation requires a way to exchange limited state summaries without exposing raw human data.

The packet exists because raw human data should not become the default exchange object.

The packet allows a session to ask:

- Is the participant moving toward recovery?
- Is the participant moving away from recovery?
- Is the state unchanged?
- Is the state mixed?
- Is the state uncertain?
- Is the data quality sufficient?
- Is the packet still permitted?
- Has the packet expired?
- Is shared output allowed?
- Is private cue allowed?
- Should mediation pause or terminate?

The packet does not answer:

- Who is right?
- Who is wrong?
- Who is guilty?
- Who is unsafe?
- Who should be blamed?
- What diagnosis applies?
- What treatment is needed?
- What is the person’s true inner state?

---

## 5. Relationship to the Human-State Mediation Layer

The Human-State Packet is the exchange object inside the Human-State Mediation Layer.

The layer structure is:

Personal state signals or summaries  
→ local interpretation  
→ Human-State Packet  
→ dyadic session exchange  
→ AI mediation policy  
→ private cue / shared output  
→ recovery gate / termination gate  
→ session closure / audit log

The packet sits between local state interpretation and session-level AI mediation policy.

It carries only bounded summary information.

It must not carry raw data.

---

## 6. Relationship to the Proxy Benchmark Track

The Proxy Benchmark Track prepares synchronized multimodal benchmark infrastructure for Human-State-Aware AI Interaction.

The packet supports:

- synthetic session examples;
- sample packet structures;
- helper schema validation;
- dashboard mockup boundaries;
- local demo-lite event logs;
- dyadic session examples;
- recovery gate examples;
- termination gate examples;
- leakage-safe benchmark design.

The packet does not validate:

- benchmark performance;
- human-state measurement;
- Sal-Meter input;
- CAIS compliance;
- clinical state;
- therapeutic effect;
- diagnostic classification;
- relationship recovery;
- production readiness.

---

## 7. Relationship to Sal-Meter

The Human-State Packet is not Sal-Meter.

The Human-State Packet does not validate Sal-Meter.

The Human-State Packet does not contain Sal-Meter raw traces.

The Human-State Packet does not grant Sal-Meter designation.

At a future stage, separately governed Sal-Meter-derived state summaries may become candidate packet inputs.

At this stage, any Sal-Meter connection must be described only as:

- future Sal-Meter-derived input candidate pathway;
- future proxy-core comparison placeholder;
- not present;
- not public;
- not validated here;
- hold until separate governance.

Do not describe the packet as:

- validated Sal-Meter input;
- CAIS-compliant signal;
- official consciousness signal;
- ground-truth signal;
- Sal-Meter feedback loop;
- Sal-Meter intervention loop;
- Sal-Meter-compatible node exists.

---

## 8. Relationship to CAIS

This document does not define CAIS.

This document does not grant CAIS compliance.

This document does not create CAIS conformance.

This document does not authorize CAIS mark usage.

A Human-State Packet must not include a CAIS compliance claim.

A Human-State Packet must not include CAIS certification status.

A Human-State Packet must not imply official SICS conformance.

---

## 9. Packet scope

A Human-State Packet must be:

- minimal;
- consent-bound;
- permission-bound;
- expiry-bound;
- confidence-aware;
- data-quality-aware;
- session-scoped;
- sharing-scoped;
- raw-data-excluding;
- audit-friendly.

A Human-State Packet must not be:

- a raw data container;
- a clinical record;
- a diagnostic result;
- a therapeutic recommendation;
- a legal evidence object;
- a surveillance feed;
- a human ranking object;
- a relationship judgment object;
- a Sal-Meter validation object;
- a CAIS compliance object.

---

## 10. Required packet fields

The helper schema should define the following required fields.

### 10.1 packet_id

A unique identifier for the packet.

Purpose:

- identify the packet;
- enable audit logging;
- prevent accidental packet reuse.

Boundary:

- must not encode legal name;
- must not encode diagnosis;
- must not encode relationship role;
- must not encode protected identity.

Recommended example:

- hsp_synthetic_0001

---

### 10.2 session_id

A unique identifier for the session in which the packet is used.

Purpose:

- bind the packet to a specific session;
- prevent use outside the session;
- support audit trail.

Boundary:

- must not reveal participant identity;
- must not reveal real conflict context;
- must not encode clinical context.

Recommended example:

- session_synthetic_001

---

### 10.3 participant_role

A pseudonymous role label for the packet source.

Allowed examples:

- participant_A
- participant_B
- private_agent_A
- private_agent_B
- observer_synthetic
- simulator_actor_1
- simulator_actor_2

Not allowed:

- legal name;
- phone number;
- email address;
- patient identifier;
- employee identifier;
- student identifier;
- real relationship label;
- diagnostic role.

---

### 10.4 timestamp_created

The timestamp when the packet was created.

Purpose:

- establish packet timing;
- align with AI output event;
- support delta calculation.

Boundary:

- must not expose private device logs;
- must not include hidden participant-identifying metadata.

---

### 10.5 timestamp_expiry

The timestamp after which the packet is invalid.

Purpose:

- prevent indefinite reuse;
- prevent surveillance drift;
- enforce session-limited sharing.

Boundary:

- expired packets must not be used for mediation;
- expired packets must not be reused for new sessions.

---

### 10.6 time_window

The time interval summarized by the packet.

Suggested fields:

- start_time;
- end_time;
- duration_sec.

Purpose:

- define what period the packet summarizes;
- align packet with AI output;
- support pre-output and post-output comparison.

Boundary:

- must not expose raw timestamps that identify private life patterns;
- may be synthetic or relative in public examples.

---

### 10.7 state_summary

A bounded state-summary object.

Purpose:

- describe the session-relevant human-state summary;
- support Human-State Delta;
- support recovery gate and termination gate.

Allowed summary dimensions may include:

- arousal_band;
- regulation_trend;
- overload_risk;
- withdrawal_risk;
- engagement_band;
- recovery_trend;
- uncertainty_state.

These are non-diagnostic benchmark fields.

They are not clinical labels.

They are not psychiatric labels.

They are not person scores.

---

### 10.8 confidence_band

A bounded confidence indicator.

Allowed values may include:

- low;
- medium;
- high;
- insufficient;
- invalid.

Purpose:

- show uncertainty;
- prevent overinterpretation;
- support hold decisions.

Boundary:

- confidence is not truth;
- confidence is not clinical certainty;
- confidence is not certification.

---

### 10.9 data_quality

A bounded data-quality object.

Suggested fields:

- quality_band;
- artifact_flag;
- missingness;
- sensor_availability;
- review_required.

Purpose:

- flag whether the packet can be used;
- prevent weak data from appearing strong;
- support audit trail.

Boundary:

- data quality does not validate a benchmark;
- data quality does not validate Sal-Meter;
- data quality does not grant CAIS compliance.

---

### 10.10 permission_scope

The permission under which the packet may be used.

Allowed examples:

- private_cue_only;
- shared_output_allowed;
- dyadic_mediation_only;
- dashboard_mockup_only;
- audit_log_only;
- synthetic_example_only;
- no_sharing;

Purpose:

- prevent scope drift;
- protect participant privacy;
- preserve consent.

Boundary:

- permission must be explicit;
- permission must not be assumed;
- permission expires with session closure unless separately governed.

---

### 10.11 sharing_scope

The intended sharing boundary.

Allowed examples:

- local_only;
- personal_agent_only;
- dyadic_session;
- room_edge_hub_local;
- synthetic_public_example;
- audit_summary_only.

Purpose:

- define where the packet may travel;
- separate private from shared outputs;
- protect raw data boundary.

Boundary:

- public sharing must be synthetic only;
- real human packets must not be public repository content.

---

### 10.12 output_mode

The allowed output mode connected to the packet.

Allowed examples:

- no_output;
- private_cue;
- shared_mediation_output;
- recovery_check;
- termination_recommendation;
- audit_log_only.

Purpose:

- control how packet-derived information may affect AI output.

Boundary:

- private state must not become shared output without permission;
- packet-derived output must not judge the person;
- packet-derived output must not diagnose, treat, counsel, or decide.

---

### 10.13 session_scope

The session boundary for packet use.

Suggested fields:

- session_type;
- session_phase;
- permitted_use;
- closure_required;
- reuse_allowed.

Allowed session types may include:

- synthetic_demo;
- phone_only_simulation;
- dyadic_mediation_research;
- dashboard_mockup;
- closed_loop_demo_lite;
- audit_only.

Boundary:

- must not imply production deployment;
- must not imply live intervention;
- must not imply legal mediation service.

---

### 10.14 synthetic_flag

A Boolean or status field indicating whether the packet is synthetic.

Allowed examples:

- true;
- false_private_not_public;
- synthetic_sample;
- mock_example.

Public repository examples must use synthetic status.

Real human packet examples must not be committed to the public repository.

---

### 10.15 raw_data_excluded

A required Boolean field.

It must be true for public helper packets.

Purpose:

- declare that raw human data is excluded;
- make the boundary machine-checkable.

Boundary:

- if raw_data_excluded is false, the packet is not suitable for public helper repository use.

---

### 10.16 audit_timestamp

The timestamp for audit recording.

Purpose:

- track packet review;
- track schema alignment;
- support reproducibility.

Boundary:

- audit timestamp must not expose private identity;
- audit timestamp must not become surveillance history.

---

## 11. Optional helper fields

Optional helper fields may include:

- schema_version;
- packet_version;
- source_summary;
- event_reference;
- ai_output_reference;
- pre_output_reference;
- post_output_reference;
- delta_reference;
- recovery_gate_reference;
- termination_gate_reference;
- deviation_flag;
- review_required;
- notes_public_safe.

Optional fields must preserve the same boundary rules.

---

## 12. Prohibited fields

The schema must not allow:

- legal name;
- phone number;
- email address;
- address;
- government ID;
- patient ID;
- employee ID;
- student ID;
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
- diagnosis;
- therapy label;
- psychiatric label;
- clinical state;
- medical interpretation;
- human score;
- truth score;
- trust score;
- guilt score;
- morality score;
- psychological safety score;
- employee risk score;
- relationship verdict;
- fault assignment;
- who_is_right field;
- who_is_wrong field;
- unsafe_person field;
- political profile;
- religious profile;
- ideological profile;
- CAIS compliance status;
- Sal-Meter validation status;
- certification status;
- mark usage status.

---

## 13. Allowed state-summary fields

Allowed state-summary fields should remain coarse, bounded, and non-diagnostic.

Possible examples:

- arousal_band;
- regulation_trend;
- recovery_trend;
- overload_risk;
- withdrawal_risk;
- engagement_band;
- uncertainty_state;
- session_pressure;
- interaction_load;
- pause_need;
- termination_need.

These fields must be interpreted only as research-stage proxy benchmark fields.

They must not be interpreted as clinical truth.

---

## 14. Recommended controlled values

### 14.1 arousal_band

Allowed examples:

- low;
- medium;
- medium_high;
- high;
- unknown;
- insufficient_data.

### 14.2 regulation_trend

Allowed examples:

- improving;
- stable;
- worsening;
- mixed;
- unknown;
- insufficient_data.

### 14.3 recovery_trend

Allowed examples:

- toward_recovery;
- away_from_recovery;
- unchanged;
- mixed;
- uncertain;
- insufficient_data;
- invalid.

### 14.4 overload_risk

Allowed examples:

- low;
- medium;
- high;
- unknown;
- insufficient_data.

### 14.5 withdrawal_risk

Allowed examples:

- low;
- medium;
- high;
- unknown;
- insufficient_data.

### 14.6 engagement_band

Allowed examples:

- present;
- reduced;
- withdrawn;
- mixed;
- unknown;
- insufficient_data.

These values are not diagnoses.

They are not person labels.

They are packet-level session helper values.

---

## 15. Permission model

The packet must carry permission information.

Permission should define:

- whether the packet may be used;
- whether private cue is allowed;
- whether shared output is allowed;
- whether audit logging is allowed;
- whether packet reuse is allowed;
- whether packet is expired;
- whether session closure has occurred.

A packet without permission must not be used.

A packet with expired permission must not be used.

A packet with private-only permission must not produce shared output.

A packet with audit-only permission must not affect mediation output.

---

## 16. Expiry model

The packet must expire.

Expiry is required to prevent surveillance drift.

Expiry may be based on:

- fixed timestamp;
- session closure;
- consent withdrawal;
- packet replacement;
- data-quality invalidation;
- permission revocation;
- termination gate.

After expiry, the packet must not be used for:

- private cue;
- shared output;
- recovery gate;
- termination gate;
- dashboard display;
- model inference;
- session continuation.

Expired packets may be retained only as bounded audit references if permitted.

---

## 17. Confidence model

Confidence must be visible.

Confidence may be:

- low;
- medium;
- high;
- insufficient;
- invalid.

Low confidence should trigger caution.

Insufficient confidence should trigger hold or human review.

Invalid confidence should block packet use.

Confidence must not be presented as truth.

Confidence must not be presented as clinical certainty.

---

## 18. Data-quality model

Data quality must be represented.

Data-quality fields may include:

- quality_band;
- artifact_flag;
- missingness;
- sensor_availability;
- packet_completeness;
- review_required.

Poor data quality should not produce strong mediation claims.

Poor data quality should not be hidden.

A weak packet must remain visibly weak.

---

## 19. Sharing model

The packet must define sharing scope.

Possible sharing scopes:

- local_only;
- personal_agent_only;
- dyadic_session;
- room_edge_hub_local;
- audit_summary_only;
- synthetic_public_example;
- no_sharing.

Public repository sharing must be synthetic only.

Real human packet sharing requires separate private governance.

Raw human data must not be shared through the packet.

---

## 20. Output model

The packet may influence output only within permission.

Possible output modes:

- no_output;
- private_cue;
- shared_mediation_output;
- recovery_check;
- termination_recommendation;
- audit_log_only.

Output must not include:

- diagnosis;
- therapy;
- counseling;
- legal mediation decision;
- blame;
- relationship verdict;
- participant ranking;
- private state exposure;
- raw data exposure.

---

## 21. Synthetic public packet rule

Public packets in this repository must be synthetic, sample, mock, placeholder, or toy examples.

Public packet examples must not represent real participant state.

Public packet examples must not include real voice, face, gaze, biosignal, transcript, or Sal-Meter / CAIS raw trace.

Public packet examples must include:

- synthetic_flag;
- raw_data_excluded;
- boundary statement;
- data quality;
- permission scope;
- expiry.

---

## 22. Example public-safe synthetic packet structure

Example fields:

- packet_id: hsp_synthetic_0001
- session_id: session_synthetic_001
- participant_role: participant_A
- timestamp_created: synthetic_timestamp_created
- timestamp_expiry: synthetic_timestamp_expiry
- time_window: synthetic_10_sec_window
- state_summary:
  - arousal_band: medium_high
  - regulation_trend: improving
  - recovery_trend: toward_recovery
  - overload_risk: medium
  - withdrawal_risk: low
  - engagement_band: present
- confidence_band: medium
- data_quality:
  - quality_band: usable
  - artifact_flag: false
  - missingness: low
  - review_required: false
- permission_scope: dyadic_mediation_only
- sharing_scope: synthetic_public_example
- output_mode: private_cue
- session_scope: synthetic_demo
- synthetic_flag: true
- raw_data_excluded: true
- audit_timestamp: synthetic_audit_timestamp

This example is structure only.

It does not prove human-state measurement.

It does not prove AI mediation.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

---

## 23. Invalid packet examples

A packet is invalid for this public helper repository if it includes:

- real participant name;
- real voice transcript;
- raw biosignal;
- raw video;
- raw face image;
- raw gaze trace;
- raw CAIS trace;
- raw Sal-Meter trace;
- diagnosis;
- therapy label;
- relationship verdict;
- human score;
- blame assignment;
- CAIS compliance claim;
- Sal-Meter validation claim.

A packet is also invalid if:

- permission is absent;
- expiry is absent;
- raw_data_excluded is not true;
- synthetic flag is absent in public examples;
- sharing scope is undefined;
- data quality is undefined;
- confidence is undefined.

---

## 24. Leakage-control considerations

The packet must not leak target labels through hidden shortcuts.

Leakage risks include:

- participant identity;
- dyad identity;
- session order;
- condition names;
- filenames;
- folder names;
- device identity;
- operator identity;
- timestamps that encode condition;
- metadata fields that encode labels;
- AI output template names that reveal target;
- recovery label embedded in packet ID.

A result that leaks labels is not evidence.

A packet that hides labels in metadata is not benchmark-safe.

---

## 25. Relationship to Recovery Gate

The Recovery Gate may use packet summaries only within permission.

The Recovery Gate must consider:

- recovery_trend;
- confidence_band;
- data_quality;
- permission_scope;
- timestamp_expiry;
- sharing_scope;
- participant confirmation, if available;
- session context;
- false recovery risk.

The Recovery Gate must not treat silence as recovery.

The Recovery Gate must not treat one-sided improvement as dyadic recovery.

The Recovery Gate must not treat synchrony as automatically positive.

---

## 26. Relationship to Termination Gate

The Termination Gate may use packet status to stop a session.

Termination may be required if:

- consent is withdrawn;
- packet expires;
- permission is exceeded;
- data quality fails;
- confidence is invalid;
- private state exposure risk appears;
- raw data exposure risk appears;
- mediation overstay risk appears;
- recovery is reached;
- participant requests stop;
- audit boundary fails.

Termination protects the session from becoming surveillance.

A session that cannot close is not a Human-State Session.

---

## 27. Public repository boundary

This repository may include:

- helper schema;
- synthetic packet example;
- mock packet example;
- sample dashboard field;
- validation helper;
- README explanation;
- issue template;
- pull request boundary review.

This repository must not include:

- real human packet;
- raw human data;
- private participant packet;
- identifiable dyadic session;
- clinical packet;
- therapeutic packet;
- legal mediation packet;
- Sal-Meter raw trace;
- CAIS raw trace;
- production feedback log.

---

## 28. Machine-readable schema direction

The companion JSON Schema should enforce:

- required fields;
- controlled values;
- no additional prohibited fields;
- synthetic public boundary;
- raw_data_excluded requirement;
- permission scope;
- expiry field;
- confidence field;
- data-quality field;
- output mode;
- sharing scope.

The schema should reject examples that lack:

- packet_id;
- session_id;
- participant_role;
- timestamp_created;
- timestamp_expiry;
- state_summary;
- confidence_band;
- data_quality;
- permission_scope;
- sharing_scope;
- output_mode;
- synthetic_flag;
- raw_data_excluded.

The schema should not claim scientific validity.

It checks structure.

It does not certify truth.

---

## 29. Go / Hold rule

Go if the packet:

- is minimal;
- is consent-bound;
- is permission-bound;
- is expiry-bound;
- is confidence-aware;
- is data-quality-aware;
- is session-scoped;
- is sharing-scoped;
- excludes raw human data;
- remains synthetic in public examples;
- avoids diagnosis;
- avoids therapy;
- avoids surveillance;
- avoids human scoring;
- avoids relationship judgment;
- avoids Sal-Meter validation;
- avoids CAIS compliance.

Hold if the packet:

- introduces raw data fields;
- introduces identity fields;
- introduces diagnostic labels;
- introduces therapeutic labels;
- introduces human scoring;
- introduces relationship verdicts;
- introduces surveillance scope;
- implies Sal-Meter validation;
- implies CAIS compliance;
- implies production intervention.

No-Go if the packet:

- contains real raw human data;
- contains identifiable data;
- contains raw voice, face, gaze, video, biosignal, transcript, CAIS trace, or Sal-Meter trace;
- claims diagnostic, therapeutic, clinical, legal mediation, surveillance, or human-ranking function;
- claims certified or validated status.

---

## 30. Related documents

- docs/human-state-mediation-layer.md
- docs/human-state-session-protocol.md
- docs/dyadic-mediation-session-flow.md
- docs/dyadic-recovery-baseline-suite.md
- docs/recovery-gate-definition.md
- docs/termination-gate-definition.md
- docs/consent-and-data-sharing-boundary.md
- schemas/human_state_packet.schema.json

---

## 31. Related canonical records

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

## 32. Final boundary sentence

The Human-State Packet is not the body.

It is not the raw signal.

It is not diagnosis.

It is not therapy.

It is not a human score.

It is not a relationship verdict.

It is a consented, bounded, session-scoped state summary used only to support research-stage interaction adjustment without exposing raw human data.
