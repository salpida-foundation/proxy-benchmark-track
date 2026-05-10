# Mediation Policy Prompt Pack Boundary

This folder contains bounded prompt and policy scaffolding for the **SICS Human-State Proxy Benchmark Track**.

This is a research-stage, synthetic, public-helper-only prompt pack.

It is not a production mediation system.

It is not a clinical, diagnostic, therapeutic, counseling, surveillance, employment, insurance, educational, legal, eligibility, certification, device-readiness, production-deployment, or human-ranking system.

It does not validate mediation effectiveness.

It does not validate benchmark performance.

It does not validate scientific truth.

It does not validate Sal-Meter.

It does not grant CAIS compliance.

It does not process raw human data.

It does not process identifiable human data.

It does not process clinical data.

It does not process Sal-Meter raw input.

It does not process CAIS compliance dossiers.

---

## Purpose

The purpose of this folder is to define bounded prompt and policy structures for synthetic Human-State-Aware AI mediation simulation.

The prompt pack helps describe how an AI mediation output may be shaped under strict public-helper boundaries.

It exists to support:

- synthetic AI output condition examples;
- state-aware AI output condition examples;
- private cue boundary examples;
- shared mediation output boundary examples;
- pause recommendation logic;
- clarification request logic;
- scope narrowing logic;
- recovery check logic;
- termination recommendation logic;
- false recovery prevention;
- one-sided improvement caution;
- no relationship verdict;
- no human ranking;
- no diagnosis;
- no therapy;
- no counseling authority;
- no surveillance authority;
- no production closed-loop claim.

The purpose is structure.

The purpose is not proof.

The purpose is not treatment.

The purpose is not judgment.

The purpose is not production deployment.

---

## Current intended files

```text
prompts/
  README.md
  mediation_policy_v0.1.json
```

Related documentation:

```text
docs/mediation-policy-prompt-pack.md
```

Related demo-flow files:

```text
sample-data/synthetic-dyadic-session-001/
  ai_outputs.json
  dyadic_delta.json
  recovery_gate.json
  termination_gate.json
  audit_log.json
```

Related evaluator:

```text
evaluation-baseline/evaluate_dyadic_recovery_demo.py
```

---

## P4-2 position

This folder belongs to:

```text
P4-2 — Mediation Policy Prompt Pack
```

P4-2 follows the completed P4-0 / P4-1 path:

```text
P4-0 Synthetic Dyadic Demo Package
→ P4-1 Synthetic Dyadic Recovery Delta Evaluator
→ P4-2 Mediation Policy Prompt Pack
```

P4-0 demonstrates synthetic demo-flow objects.

P4-1 checks synthetic demo-flow consistency.

P4-2 defines bounded prompt / policy structures for synthetic mediation simulation.

None of these stages create benchmark evidence.

None of these stages validate mediation.

None of these stages validate Sal-Meter.

None of these stages grant CAIS compliance.

---

## Design principle

The prompt pack must preserve this chain:

```text
AI Output
→ Human-State Packet A/B
→ Dyadic Delta
→ Recovery Gate
→ Termination Gate
→ Audit Log
```

The prompt pack must not collapse that chain into a person judgment.

The prompt pack must not treat a smooth AI answer as recovery.

The prompt pack must not treat silence as recovery.

The prompt pack must not treat agreement as recovery.

The prompt pack must not treat obedience as recovery.

The prompt pack must not treat synchrony as recovery.

The prompt pack must not treat one-sided improvement as dyadic recovery.

A policy output may guide the next synthetic response.

It may not judge the person.

It may not diagnose the person.

It may not rank the person.

It may not decide the relationship.

It may not authorize real-world intervention.

---

## Prompt condition types

The prompt pack may define the following synthetic condition types:

```text
generic_ai_output
state_aware_ai_output
private_cue
shared_mediation_output
pause_recommendation
clarification_request
scope_narrowing
recovery_check
termination_recommendation
audit_note
```

These are helper categories only.

They are not clinical categories.

They are not diagnostic categories.

They are not therapeutic categories.

They are not legal categories.

They are not surveillance categories.

They are not certification categories.

They are not production action categories.

---

## Private cue boundary

A private cue is a bounded helper instruction intended only for synthetic internal mediation routing.

A private cue may describe:

- uncertainty;
- packet availability;
- consent status;
- permission status;
- confidence level;
- data-quality limitation;
- one-sided improvement risk;
- possible false recovery risk;
- need to pause;
- need to narrow scope;
- need to terminate the session.

A private cue must not expose:

- raw human data;
- raw voice;
- raw face;
- raw gaze;
- raw transcript;
- private state details;
- clinical interpretations;
- diagnostic interpretations;
- therapeutic interpretations;
- hidden labels;
- identity-bearing information;
- relationship verdicts;
- blame assignments;
- human scores.

Correct boundary sentence:

```text
A private cue is a bounded synthetic routing helper, not a disclosure of private human state.
```

---

## Shared mediation output boundary

A shared mediation output is a bounded synthetic message visible to the simulated participants.

It may:

- slow down escalation;
- ask for clarification;
- restate scope;
- suggest pausing;
- ask for consent confirmation;
- avoid assigning blame;
- avoid declaring recovery;
- avoid ranking participants;
- avoid diagnosing participants;
- avoid exposing private packet details;
- recommend closure when continuation is not safe within the session boundary.

It must not:

- reveal private cue content;
- reveal raw human data;
- reveal hidden packet details;
- declare who is right;
- declare who is wrong;
- declare who is guilty;
- declare who is unsafe;
- declare who is emotionally defective;
- declare who should be punished;
- declare who should be monitored;
- declare who should be treated;
- declare that the relationship is resolved;
- declare that the relationship has failed;
- declare that dyadic recovery has occurred without gate support;
- create a clinical, diagnostic, therapeutic, legal, employment, insurance, educational, eligibility, surveillance, certification, or human-ranking outcome.

Correct boundary sentence:

```text
A shared mediation output is a bounded synthetic communication helper, not a relationship judgment.
```

---

## Allowed policy actions

A policy may recommend:

```text
continue_with_clarification
continue_with_scope_narrowing
continue_with_private_cue_only
continue_with_shared_mediation_output
request_consent_refresh
request_packet_refresh
pause_session
close_session
terminate_session
audit_only
```

A policy may not recommend:

```text
diagnose_participant
treat_participant
rank_participant
score_person
assign_blame
declare_relationship_verdict
override_consent
bypass_permission
reuse_expired_packet
expose_private_state
publish_raw_data
start_production_intervention
claim_benchmark_validation
claim_mediation_validation
claim_sal_meter_validation
claim_cais_compliance
```

---

## Recovery caution

The prompt pack must preserve false recovery prevention.

A synthetic policy should not mark recovery when:

- only one participant improves;
- one participant becomes silent;
- one participant becomes compliant;
- both participants merely agree verbally;
- the AI output sounds supportive but the dyadic delta remains mixed;
- the recovery gate is not passed;
- consent or permission has expired;
- data quality is insufficient;
- private state would be exposed by continuation;
- the termination gate recommends pause or closure.

Correct boundary sentence:

```text
One-sided improvement is not dyadic recovery.
```

---

## Termination caution

The prompt pack must preserve termination logic.

A synthetic policy should pause, narrow, or close when:

- consent is withdrawn;
- permission expires;
- packet confidence is too low;
- data quality is insufficient;
- uncertainty is high;
- continuation would expose private state;
- the AI has exceeded session scope;
- the mediation would become endless;
- the session is already closed;
- a new session is required for continuation.

Correct boundary sentence:

```text
A closed session must stay closed.
```

---

## Prompt output layers

The prompt pack should distinguish at least three layers:

```text
1. internal_policy_decision
2. private_cue
3. shared_mediation_output
```

The internal policy decision is for synthetic routing.

The private cue is for bounded internal helper use.

The shared mediation output is the only layer intended to appear as a participant-visible synthetic message.

These layers must not be merged.

Private cue content must not leak into shared mediation output.

Raw human data must not enter any layer.

---

## Required boundary flags

Every prompt policy object should include explicit boundary flags.

Required false flags:

```text
raw_human_data_present: false
identifiable_data_present: false
clinical_data_present: false
sal_meter_input_present: false
cais_compliance_claim_present: false
benchmark_validation_claim_present: false
mediation_validation_claim_present: false
production_intervention_claim_present: false
human_ranking_claim_present: false
relationship_verdict_present: false
```

Required status fields:

```text
dataset_type: synthetic
prompt_policy_scope: public_helper_only
mediation_status: not_validated
benchmark_status: not_validated
sal_meter_status: not_sal_meter
cais_status: not_cais_compliance
```

---

## Minimal policy object concept

The JSON policy file should be structured around the following conceptual fields:

```text
policy_id
policy_version
dataset_type
prompt_policy_scope
input_condition_type
allowed_output_type
private_cue_boundary
shared_output_boundary
recovery_gate_dependency
termination_gate_dependency
false_recovery_prevention
one_sided_improvement_caution
prohibited_claims
required_boundary_flags
audit_note
final_boundary_status
```

This is a helper structure.

It is not a schema.

It is not a benchmark standard.

It is not a clinical protocol.

It is not a CAIS compliance record.

---

## Relationship to P4-1 evaluator

The P4-1 evaluator checks synthetic demo-flow consistency.

The prompt pack defines bounded policy options that may later feed synthetic AI output examples.

The evaluator and the prompt pack must remain separate.

The evaluator checks structure.

The prompt pack describes policy shape.

Neither proves recovery.

Neither proves mediation effectiveness.

Neither validates science.

Neither validates Sal-Meter.

Neither grants CAIS compliance.

---

## Allowed language

Use:

```text
synthetic prompt policy
public helper prompt pack
bounded mediation policy scaffold
private cue boundary
shared mediation output boundary
pause recommendation
scope narrowing
termination recommendation
false recovery prevention
one-sided improvement caution
synthetic demo-flow consistency
research-stage
non-clinical
non-diagnostic
non-therapeutic
non-counseling
non-surveillance
non-certification
non-human-ranking
not Sal-Meter
not CAIS compliance
not benchmark validation
not mediation validation
no raw human data
```

Avoid:

```text
validated mediation prompt
clinical mediation prompt
diagnostic prompt
therapeutic prompt
production mediation engine
relationship scoring prompt
human ranking prompt
emotion-reading prompt
surveillance prompt
certified mediation policy
Sal-Meter validated prompt
CAIS-compliant mediation prompt
AI harm detector
human-state detector
```

---

## Public release rule

Before adding any prompt file to this folder, confirm:

```text
raw_human_data_present == false
identifiable_data_present == false
clinical_data_present == false
sal_meter_input_present == false
cais_compliance_claim_present == false
benchmark_validation_claim_present == false
mediation_validation_claim_present == false
production_intervention_claim_present == false
human_ranking_claim_present == false
relationship_verdict_present == false
```

If any of the above cannot be confirmed, the file does not belong in this public repository.

---

## Future validation posture

Future helper checks may confirm:

- the prompt policy file exists;
- the prompt policy file parses as JSON;
- required boundary flags are present;
- prohibited output categories are excluded;
- private cue and shared output are separated;
- recovery gate dependency is explicit;
- termination gate dependency is explicit;
- one-sided improvement caution is explicit;
- no production closed-loop claim is present.

A successful check would mean only:

```text
The synthetic prompt policy object follows the expected public helper structure.
```

A successful check would not mean:

```text
The policy is scientifically validated.
The policy improves mediation.
The policy is clinically useful.
The policy is diagnostic.
The policy is therapeutic.
The policy is Sal-Meter.
The policy is CAIS-compliant.
The policy is production-ready.
```

---

## Authority rule

This folder is a GitHub helper surface.

It is not a canonical authority layer.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this folder conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

---

## Completion target

P4-2 is complete when:

```text
prompts/README.md exists.
prompts/mediation_policy_v0.1.json exists.
docs/mediation-policy-prompt-pack.md exists.
Private cue and shared mediation output are clearly separated.
Pause, narrow, and terminate options are represented.
False recovery prevention is explicit.
One-sided improvement caution is explicit.
No raw human data is introduced.
No benchmark validation claim is introduced.
No mediation validation claim is introduced.
No Sal-Meter validation claim is introduced.
No CAIS compliance claim is introduced.
No production closed-loop claim is introduced.
```

---

## Final rule

The prompt is not the person.

The cue is not disclosure.

The shared output is not judgment.

The policy is not therapy.

The session is not surveillance.

The gate may pause.

The gate may close.

The gate must not crown recovery without evidence.

A closed session must stay closed.
