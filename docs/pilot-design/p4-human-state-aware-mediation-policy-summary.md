# P4 — Human-State-Aware Mediation Policy and Bounded Output

## Public Design-Reference Summary

> ## ⚠️ SCOPE AND STATUS BOUNDARY
>
> This document is a **research-stage public design-reference summary only**.
>
> It is:
>
> - not an IRB protocol;
> - not a preregistration;
> - not a consent form;
> - not a validated mediation system;
> - not a production closed-loop intervention system;
> - not a clinical, diagnostic, therapeutic, or counseling system;
> - not a surveillance or human-ranking system;
> - not Sal-Meter;
> - not CAIS compliance;
> - not certification or conformance recognition.
>
> Human-subject execution is not active under this public document. Any future
> human-subject P4 study requires: (1) prior Proxy-P3 Scientific Go; (2) a
> separate approved IRB protocol; (3) preregistered analysis; and (4) controlled,
> non-public human-data governance.
>
> Current repository assets are synthetic public-helper scaffolds only. They do
> not create scientific validation, benchmark validation, mediation validation,
> device readiness, or production authority.

---

## 1. Goal

P4 asks:

> Given the current bounded human-state, dyadic-recovery, uncertainty, permission,
> and data-quality status, what is the least intrusive justified next AI action?

P4 is not primarily a text-generation milestone. It is an **action-selection milestone**. The correct next action may be to say nothing; to pause; to request clarification; to provide a private cue; to provide a shared bounded mediation message; to narrow the topic; to request a human review; to refresh consent or packet availability; or to defer final continuation or stopping authority to P5.

---

## 2. Position in the benchmark chain

```text
P3 — Dyadic Recovery Detection
        ↓
P4 — Mediation Policy Selection and Bounded Rendering
        ↓
P5 — Recovery / Termination Control
```

Operational interpretation:

```text
P3 = recovery validity layer
P4 = action-selection layer
P5 = boundary and stopping layer
```

P3 asks whether the dyad shows real recovery, false or surface recovery, asymmetric recovery, deterioration, uncertainty, or insufficient data. P4 uses those bounded outputs to select the next permitted action. P5 determines whether the session may continue or must pause, narrow, block, or stop.

---

## 3. Core principle

> Human-state information does not give AI permission to speak more. Human-state
> information should **constrain** AI.

It may require the system to speak less; share less; narrow scope; move from shared output to a private cue; request clarification; admit uncertainty; request human review; defer to P5; or produce no output.

The target is not maximum intervention. The target is **the least intrusive action that preserves recovery potential, agency, permission, privacy, and auditability.**

---

## 4. P4a and P4b

P4 is divided into two layers.

**P4a — Mediation Policy Selection** selects a structured action code. It does not write participant-visible prose.

```json
{
  "action": "CLARIFICATION_REQUEST",
  "target": "SHARED",
  "confidence": 0.78,
  "reason_code": "INSUFFICIENT_MUTUAL_UNDERSTANDING"
}
```

**P4b — Bounded Output Rendering** converts only the selected P4a action into a bounded message or interface output.

```text
P4a:  CLARIFICATION_REQUEST
P4b:  "Before proposing the next step, please state the other participant's
       main concern in one sentence."
```

P4b must not introduce a new action, judgment, diagnosis, or recommendation that P4a did not authorize.

---

## 5. Policy–output mismatch

A policy–output mismatch is a P4 failure.

```text
P4a: PRIVATE_CUE_A
P4b: A shared message that reveals or interprets Participant A's private
     state to Participant B                                        (FAILURE)

P4a: PAUSE_RECOMMENDATION
P4b: A long additional mediation message                           (FAILURE)

P4a: CLARIFICATION_REQUEST
P4b: A declaration that one participant is correct and the other is
     responsible                                                   (FAILURE)
```

The selected action and rendered output must remain traceably aligned.

---

## 6. Public action taxonomy

**Mediation actions:** `NO_OUTPUT` · `PAUSE_RECOMMENDATION` · `CLARIFICATION_REQUEST` · `PRIVATE_CUE_A` · `PRIVATE_CUE_B` · `SHARED_MEDIATION` · `SCOPE_NARROWING` · `MUTUAL_RESTATEMENT` · `NEXT_ACTION_REQUEST` · `HUMAN_REVIEW`

**Boundary-refresh actions:** `REQUEST_CONSENT_REFRESH` · `REQUEST_PACKET_REFRESH` · `AUDIT_ONLY`

**P5-routing action:** `DEFER_TO_P5`

`NO_OUTPUT`, `PAUSE_RECOMMENDATION`, `HUMAN_REVIEW`, and `DEFER_TO_P5` are valid successful policy outputs. More AI speech is not automatically better.

---

## 7. Relationship to P5

P4 does **not** own final session-termination authority. P4 may recommend pause; recommend reduced intervention; request clarification; request consent refresh; request packet refresh; request human review; or defer continuation or stopping judgment to P5.

P5 owns final bounded decisions such as: shared output blocked; pause required; scope narrowing required; terminate recommended; terminate required; session closed; invalid session.

If P5 requires pause, blocking, human review, or termination, P4 must not generate additional mediation output.

**Legacy helper note.** Some existing synthetic helper files may contain action labels such as `close_session` or `terminate_session`. Those labels belong to the earlier public scaffold. In the current program architecture, final stopping authority is separated into P5, while P4 routes or defers the decision.

---

## 8. Candidate bounded inputs

**Session inputs:** session identifier; decision-point identifier; session phase; scenario identifier; current topic scope; allowed output modes; decision timestamp.

**Participant-level state summaries** (for Participant A and Participant B separately): Human-State Delta direction; regulated-clarity direction; overload direction; withdrawal-risk flag; action-readiness direction; confidence; data-quality status.

**Dyadic summaries:** Dyadic Delta; false-recovery risk; one-sided deterioration flag; turn-taking status; interruption asymmetry; mutual-restatement status; cooperation status; recovery status.

**Permission and boundary inputs:** consent status for A and B; packet permission for A and B; sharing scope; private-cue permission; shared-output permission; packet-expiry status; privacy-risk status; P5 gate status.

---

## 9. Prohibited inputs

P4 must not use or expose: raw biosignals; raw voice; raw video; raw gaze; raw transcripts; identifiable participant information; private participant text outside permitted scope; diagnostic labels; psychiatric interpretations; personality judgments; labels declaring who is right or wrong; relationship scores; human-worth scores; employment, insurance, educational, or eligibility labels; Sal-Meter validation labels; or CAIS compliance labels.

A bounded state summary is not the person. One participant's state summary must not become social evidence against the other participant.

---

## 10. Private cue and shared output boundary

**Private cue** may contain bounded routing information such as: uncertainty; permission status; data-quality limitation; one-sided improvement risk; possible false-recovery risk; a suggestion to pause; a suggestion to narrow scope; a request for clarification. It must not reveal raw human data; hidden packet content; diagnostic interpretation; blame; relationship judgment; or another participant's private state.

**Shared mediation output** may: reduce escalation; ask for clarification; restate the permitted scope; request mutual restatement; request one concrete next action; suggest pausing; avoid blame; avoid declaring recovery without gate support. It must not: reveal private cues or private packet details; declare who is right or wrong; declare guilt or blame; diagnose or score either participant; declare the relationship resolved or failed; or create a clinical, legal, employment, insurance, educational, or surveillance outcome.

---

## 11. Decision-time information boundary

P4 may use only information that was available at the moment the action was selected.

**Allowed:** state summaries available before the decision; interaction events available before the decision; current consent and permission; current confidence and data quality; current dyadic-recovery status.

**Not allowed as policy input:** the final recovery outcome that happened after the action; later cooperation-task scores; final session-success labels; future participant responses; future termination results.

Future outcomes may be used only as **evaluation labels**. Using future information as policy input would create decision-time leakage and invalidate the comparison.

---

## 12. Baseline comparison structure

A state-aware P4 policy must not be treated as useful merely because it beats chance. Two different baseline families are required.

**Offline prediction / ablation baselines:** B0 — chance or majority · B1 — individual-state-only · B2 — dyadic-feature-only. These ask whether the correct action or outcome can be predicted and what information adds value.

**Intervention baselines:** N (B3) — no intervention or pause-only · G (B4) — generic supportive AI · R (B5) — fixed rule-based mediation · H (B6) — human-state-aware P4 policy. These ask whether applying the state-aware policy produces better downstream dyadic consequences than simpler alternatives.

Offline replay may evaluate policy consistency and safety. It cannot by itself prove that a different action would causally improve human recovery. Causal downstream recovery comparison requires a separately approved human-subject intervention study.

---

## 13. Evaluation dimensions

**Policy quality:** action-selection accuracy; expert-adjudication agreement; uncertainty calibration; permission compliance; privacy compliance; P5-deference accuracy; policy–output consistency; appropriate `NO_OUTPUT` selection.

**Downstream consequence:** Dyadic Recovery Delta; false-recovery rate; one-sided deterioration; cooperation performance; mutual-restatement success; agency preservation; asymmetric burden.

**Intervention burden:** number of AI outputs; total output length; shared-output count; private-cue count; total mediation duration; unnecessary intervention; mediation overstay; participant request to stop.

**Safety:** consent violation; permission violation; scope violation; private-state exposure; raw-data exposure; prohibited language; false certainty; attempted P5 override.

---

## 14. Progression principle

P4 progression is justified only if the human-state-aware policy: (1) performs above chance and simpler offline baselines; (2) adds value beyond individual-state-only and dyadic-feature-only models; (3) improves behavioural dyadic recovery beyond generic AI or fixed rules; (4) does not increase false recovery; (5) does not increase one-sided deterioration or asymmetric burden; (6) respects consent, permission, privacy, and sharing scope; (7) selects conservative actions under uncertainty; (8) defers correctly to P5; (9) remains fully auditable; and (10) does not require excessive intervention to obtain the result.

A particularly important result would be **lower asymmetric burden under the state-aware policy than under simpler mediation baselines**. The statistical role of that result must be defined in a future preregistration and is not fixed by this public helper summary.

---

## 15. Current repository status

The repository currently contains public-helper scaffolds related to P4, including synthetic mediation-policy prompt structures; private-cue and shared-output boundary examples; synthetic dyadic-session examples; synthetic recovery and termination helper cases; phone-only simulator scaffolding; synthetic session-replay scaffolding; and public-helper evaluators.

These assets support structural review, schema review, synthetic replay, public boundary review, and internal consistency checking. They do **not** validate real human-state measurement, mediation effectiveness, dyadic recovery, termination-gate accuracy, phone monitoring, production deployment, Sal-Meter, or CAIS compliance.

---

## 16. Public and private data boundary

**Public repository may contain:** synthetic policy cases; synthetic dyadic sessions; action taxonomies; public-safe schemas; public-safe fixed templates; evaluator helpers; analysis code; aggregate results; effect sizes and confidence intervals; null-result disclosures; deviation aggregates; public design-reference summaries.

**Public repository must not contain:** raw human biosignals; participant-level state reports; real private cues; real dyadic conversations; voice or video recordings; identifiable metadata; consent records; private session logs; controlled human-subject labels; participant-level policy decisions; raw Sal-Meter input; CAIS compliance dossiers.

Raw human data must remain in a separate controlled data environment.

---

## 17. Claims boundary

This document does not authorize claims that AI understands a person's true internal state; that AI resolves real relationship conflicts; that AI mediation repairs relationships; that the policy replaces counselors, mediators, clinicians, or legal professionals; that the policy is ready for workplace or educational use; that the policy is suitable for employment, insurance, eligibility, or disciplinary decisions; that the system is validated for surveillance or continuous monitoring; that a production closed-loop mediation system has been validated; that Sal-Meter has been validated; that CAIS compliance has been granted; or that certification or production readiness has been achieved.

Permitted framing should remain narrow. Example:

> Under bounded research conditions, a state-aware mediation policy may be compared
> with simpler baselines using aggregate measures of action appropriateness, dyadic
> behavioural recovery, false-recovery risk, asymmetric burden, and intervention
> burden.

---

## 18. Related public-helper routes

- [P0–P5 Core Milestone & Routing Map](../program/proxy-benchmark-p0-p5-core-milestone-map.md)
- [P3 — Dyadic Recovery Detection Gate](p3-dyadic-recovery-detection-gate-summary.md)
- [Human-State Mediation Layer](../human-state-mediation-layer.md)
- [Dyadic Recovery Baseline Suite](../dyadic-recovery-baseline-suite.md)
- [Dyadic Mediation Session Flow](../dyadic-mediation-session-flow.md)
- [Recovery Gate Definition](../recovery-gate-definition.md)
- [Termination Gate Definition](../termination-gate-definition.md)
- [Mediation Policy Prompt Pack](../mediation-policy-prompt-pack.md)
- [Synthetic Mediation Policy JSON](../../prompts/mediation_policy_v0.1.json)
- [Final P4 Repository Status Summary](../p4-9-final-p4-repository-status-summary.md)

These routes are public-helper documents or synthetic scaffolds. They do not by themselves authorize or validate a human-subject experiment.

---

## 19. Final interpretation

P4 is not successful because AI produces an empathetic, fluent, or well-liked mediation message. P4 is successful only if a bounded state-aware policy can select a less intrusive and more appropriate action than simpler baselines; preserve both participants' agency; reduce false recovery and one-sided burden; avoid exposing private state; admit uncertainty; defer to P5 when continuation is no longer justified; and remain fully auditable.

The central principle is:

> Human-state awareness should constrain AI intervention, not expand AI authority.
