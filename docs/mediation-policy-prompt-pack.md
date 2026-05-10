# Mediation Policy Prompt Pack

## 1. Purpose

This document defines the **P4-2 Mediation Policy Prompt Pack** for the SICS Human-State Proxy Benchmark Track.

This is a research-stage, synthetic, public-helper-only prompt and policy scaffold.

It defines how synthetic AI mediation outputs may be shaped under bounded conditions.

It does not create a production mediation system.

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

## 2. Position in the P4 path

P4-2 follows the completed P4-0 / P4-1 path.

```text
P4-0 Synthetic Dyadic Demo Package
→ P4-1 Synthetic Dyadic Recovery Delta Evaluator
→ P4-2 Mediation Policy Prompt Pack
```

P4-0 demonstrates synthetic demo-flow objects.

P4-1 evaluates synthetic demo-flow consistency.

P4-2 defines bounded prompt and policy structures for synthetic mediation simulation.

This document does not prove recovery.

This document does not prove mediation effectiveness.

This document does not validate a benchmark.

This document does not validate Sal-Meter.

This document does not grant CAIS compliance.

---

## 3. Related files

Prompt folder:

```text
prompts/
  README.md
  mediation_policy_v0.1.json
```

Related synthetic demo-flow files:

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

This document explains the policy boundary.

The JSON file defines the machine-readable helper object.

The evaluator remains separate.

The evaluator checks synthetic demo-flow consistency only.

The policy prompt pack defines bounded mediation-output scaffolding only.

---

## 4. Core chain preserved by the prompt pack

The prompt pack must preserve the following chain:

```text
AI Output
→ Human-State Packet A/B
→ Dyadic Delta
→ Recovery Gate
→ Termination Gate
→ Audit Log
```

The prompt pack must not collapse this chain into:

```text
person judgment
relationship verdict
clinical interpretation
diagnosis
therapy
human ranking
surveillance output
production intervention
```

The policy may guide a synthetic next response.

It may not decide the person.

It may not diagnose the person.

It may not rank the person.

It may not decide the relationship.

It may not authorize real-world intervention.

---

## 5. Policy objective

The policy objective is to define bounded prompt decisions for synthetic mediation simulation.

The policy may support:

- generic AI output condition;
- state-aware AI output condition;
- private cue handling;
- shared mediation output handling;
- pause recommendation;
- clarification request;
- scope narrowing;
- recovery check;
- termination recommendation;
- audit-only output;
- false recovery prevention;
- one-sided improvement caution.

The policy must prevent:

- diagnosis;
- therapy;
- counseling authority;
- surveillance authority;
- relationship verdicts;
- blame assignments;
- human ranking;
- person scoring;
- production intervention;
- Sal-Meter validation claims;
- CAIS compliance claims;
- benchmark validation claims;
- mediation validation claims.

---

## 6. Prompt output layers

The prompt pack separates three output layers.

```text
1. internal_policy_decision
2. private_cue
3. shared_mediation_output
```

### 6.1 Internal policy decision

The internal policy decision is a synthetic routing decision.

It may decide whether the next step should be:

```text
continue
clarify
narrow_scope
request_consent_refresh
request_packet_refresh
pause
close
terminate
audit_only
```

It is not participant-visible.

It is not clinical.

It is not diagnostic.

It is not therapeutic.

It is not legal mediation.

It is not production intervention.

### 6.2 Private cue

A private cue is a bounded synthetic routing helper.

It may contain:

- uncertainty;
- packet availability;
- consent status;
- permission status;
- confidence level;
- data-quality limitation;
- one-sided improvement risk;
- false recovery risk;
- need to pause;
- need to narrow scope;
- need to terminate the session.

It must not contain:

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

### 6.3 Shared mediation output

A shared mediation output is a bounded synthetic message visible to simulated participants.

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
- create a clinical outcome;
- create a diagnostic outcome;
- create a therapeutic outcome;
- create a legal outcome;
- create an employment outcome;
- create an insurance outcome;
- create an educational outcome;
- create an eligibility outcome;
- create a surveillance outcome;
- create a certification outcome;
- create a human-ranking outcome.

Correct boundary sentence:

```text
A shared mediation output is a bounded synthetic communication helper, not a relationship judgment.
```

---

## 7. Allowed policy actions

The policy may recommend:

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

These actions are synthetic helper actions.

They are not clinical actions.

They are not diagnostic actions.

They are not therapeutic actions.

They are not counseling actions.

They are not legal mediation actions.

They are not production intervention actions.

They are not surveillance actions.

They are not certification actions.

---

## 8. Prohibited policy actions

The policy must not recommend:

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

Any policy object that permits one of these actions is outside the public-helper boundary.

---

## 9. False recovery prevention

The policy must preserve false recovery prevention.

A synthetic policy must not mark dyadic recovery when:

- only one participant improves;
- one participant becomes silent;
- one participant becomes compliant;
- both participants merely agree verbally;
- both participants show synchrony without gate support;
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

## 10. Termination dependency

The policy must preserve termination logic.

A synthetic policy should pause, narrow, close, or terminate when:

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

## 11. Recovery Gate dependency

A policy must not declare recovery independently.

A policy may only support a recovery check if:

- the session remains within consent;
- permission is active;
- packet scope has not expired;
- data quality is sufficient;
- uncertainty is bounded;
- both participants are considered at the dyadic level;
- one-sided improvement is not treated as recovery;
- Recovery Gate remains the controlling decision layer.

Recovery Gate dependency prevents the prompt from becoming a victory machine.

The prompt may ask.

The gate decides.

---

## 12. Termination Gate dependency

A policy must respect Termination Gate status.

If the Termination Gate indicates pause or closure, the policy must not continue ordinary mediation.

If the session is closed, the policy must not reopen it automatically.

If a new session is required, the policy must not reuse the prior session as if it were still active.

Termination Gate dependency prevents endless mediation.

The prompt may route.

The gate may close.

---

## 13. Boundary flags

Every machine-readable mediation policy object should include explicit boundary flags.

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
production_status: not_production_ready
certification_status: not_certified
```

---

## 14. Machine-readable object

The machine-readable object is:

```text
prompts/mediation_policy_v0.1.json
```

It should describe:

- policy identity;
- version;
- milestone;
- dataset type;
- public-helper scope;
- prompt condition types;
- output layers;
- allowed policy actions;
- prohibited policy actions;
- private cue boundary;
- shared output boundary;
- recovery gate dependency;
- termination gate dependency;
- false recovery prevention;
- prohibited claims;
- boundary flags;
- audit note;
- final boundary status.

The object is a helper structure.

It is not a schema.

It is not a benchmark standard.

It is not a clinical protocol.

It is not a production policy engine.

It is not a CAIS compliance record.

---

## 15. Relationship to P4-1 evaluator

The P4-1 evaluator checks synthetic demo-flow consistency.

The P4-2 policy prompt pack defines bounded policy options that may later inform synthetic AI output examples.

They must remain separate.

```text
P4-1 evaluator = structure check
P4-2 policy pack = prompt / policy scaffold
```

The evaluator does not prove mediation.

The policy pack does not prove mediation.

The evaluator does not validate Sal-Meter.

The policy pack does not validate Sal-Meter.

The evaluator does not grant CAIS compliance.

The policy pack does not grant CAIS compliance.

---

## 16. Public release rule

Before any prompt or policy file is added, confirm:

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

If any of the above cannot be confirmed, the file does not belong in this repository.

---

## 17. Allowed language

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

## 18. Future helper-check posture

Future helper checks may confirm:

- `prompts/mediation_policy_v0.1.json` exists;
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

## 19. Completion target

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

## 20. Authority rule

This document is a GitHub helper document.

It is not a canonical authority layer.

DOI-registered SICS / CAIS / Sal-Meter / CCF records remain the authority layer.

If this document conflicts with a higher-level DOI-registered canonical record, the higher-level canonical record prevails automatically.

---

## 21. Final rule

The prompt is not the person.

The cue is not disclosure.

The shared output is not judgment.

The policy is not therapy.

The session is not surveillance.

The gate may pause.

The gate may close.

The gate must not crown recovery without evidence.

A closed session must stay closed.
