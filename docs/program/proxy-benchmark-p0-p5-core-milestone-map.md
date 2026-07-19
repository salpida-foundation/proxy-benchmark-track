# Proxy Benchmark Track — P0–P5 Core Milestone & Routing Map

## 프록시 벤치마크 트랙 P0–P5 핵심 마일스톤 및 라우팅 지도

> ## ⚠️ PUBLIC HELPER BOUNDARY
>
> This document is a **research-stage public helper and routing map only**.
>
> It is:
>
> - not Sal-Meter;
> - not CAIS compliance;
> - not a clinical, diagnostic, therapeutic, or counseling system;
> - not a surveillance or human-ranking system;
> - not a certification or conformance-recognition record;
> - not an active IRB protocol;
> - not a production closed-loop intervention system;
> - not a repository for raw human data.
>
> Human-subject protocols, consent materials, participant-level records, private
> session logs, and raw biosignals remain outside this public repository under
> separate IRB and controlled-data governance.
>
> GitHub is a technical public-helper surface. DOI-registered SICS / Salpida
> Foundation records remain the authority layer where applicable.

---

## 1. One-line definition

The Proxy Benchmark Track is a research-stage benchmark platform for testing the chain:

```text
AI Output
  → Human-State Delta
  → Dyadic Recovery
  → Mediation Policy
  → Recovery / Termination
```

The track does not ask only whether an AI output sounds helpful. It asks:

> What measurable state and interaction consequences remain **after** the AI output?

---

## 2. Core phase structure

```text
P0  Signal and timeline synchronization
 ↓
P1  Individual human-state delta
 ↓
P2  AI-output consequence divergence
 ↓
P3  Dyadic recovery and false-recovery detection
 ↓
P4  Human-state-aware mediation policy
 ↓
P5  Recovery and termination control
```

The logic of the track is:

- **P0–P2 = measurement and comparison**
- **P3–P5 = mediation kernel**

Two further stages exist in the internal program plan but are **out of scope for this map**: a bounded implementation/SDK stage and a future Sal-Meter-derived-input bridge. They are pre-design and carry no validation status here.

---

## 3. P0–P5 milestone table

| Stage | English / Korean name | Core question | Core milestone | What it enables |
|---|---|---|---|---|
| **P0** | Human-State Signal Synchronization · 인간 상태 신호 동기화 | Can multimodal proxy signals, self-reports, task events, and AI-output events be aligned to one replayable session timeline? | A synchronized, metadata-complete, auditable session package can be reconstructed without relying on model-performance claims. | Individual state-delta measurement |
| **P1** | Individual Human-State Delta · 개인 인간 상태 델타 | Does standardized AI guidance create a measurable individual-state change beyond a matched self-reflection condition? | Individual Human-State Delta can be measured safely and reproducibly under a bounded reflective-phase task. | Comparison of AI-response consequences |
| **P2** | AI Output Consequence Divergence Benchmark · AI 출력 결과 분기 벤치마크 | Do different standardized AI-output types leave different patterns of immediate relief, regulated clarity, and action readiness? | Immediate relief can be distinguished from regulated clarity and action quality, including the over-validation comparator pattern. | Application to dyadic interaction |
| **P3** | Dyadic Recovery and False-Recovery Detection Gate · 두 사람 회복 및 가짜 회복 판별 게이트 | Did both participants and the interaction actually move toward recovery, or did silence, compliance, or one-sided burden merely look like recovery? | Real dyadic recovery can be distinguished from false, asymmetric, or deteriorating outcomes. | Mediation-policy design |
| **P4** | Human-State-Aware Mediation Policy and Bounded Output · 인간 상태 기반 중재 정책 및 제한형 출력 | Given the current state, uncertainty, permission, and recovery status, what is the least intrusive justified next action? | A bounded state-aware policy selects among no output, pause, clarification, private cue, shared mediation, scope narrowing, human review, or deferral to P5. | Recovery and termination control |
| **P5** | Recovery and Termination Gate · 회복 및 종료 게이트 | Should AI continue, reduce, pause, narrow, block shared output, or stop? | False-positive recovery and mediation overstay are controlled; consent, permission, privacy, scope, uncertainty, and data-quality boundaries can force closure. | Later bounded implementation and SDK work |

---

## 4. What each stage must prove

### P0 — Human-State Signal Synchronization

P0 is not a model-performance phase. It must show that multiple streams share a common session clock; event markers are reproducible; timestamps are auditable; required metadata are complete; missing intervals and device failures are visible; and the session can be replayed from its recorded package.

P0 does **not** prove human-state inference accuracy.

### P1 — Individual Human-State Delta

P1 tests whether a standardized AI-guidance exposure leaves a measurable individual-state consequence beyond matched self-reflection. The central concept is **regulated clarity**, which is not simple mood improvement. It means the participant becomes better able to distinguish confirmed facts, personal interpretation, uncertainty, the next action, and their own position and boundary.

P1 does not compare all AI-output styles — that belongs to P2.

### P2 — AI Output Consequence Divergence

P2 compares four bounded AI-response conditions.

| Code | Public condition name | Core role |
|---|---|---|
| **A** | Validating-Regulatory Response | Acknowledgement plus clarification, uncertainty preservation, and action support |
| **B** | Information-Only Neutral Response | Factual or option-oriented information without explicit state-regulation support |
| **C** | Over-Validation Comparator | Immediate validation or agreement without sufficient clarification, balance, or action structure |
| **D** | Minimizing-Dismissive Response | Low-validation, bounded minimizing response without ridicule, blame, humiliation, or personal attack |

The core P2 question is: *Can an AI response make a person feel understood without making the person clearer or more action-ready?* The key distinction is:

> Feeling better ≠ becoming clearer

P2 does not prove that a response style is universally beneficial or harmful.

---

## 5. P3–P5: the mediation kernel

### P3 is the recovery truth gate

P3 determines what counts as recovery inside a bounded dyadic session. P3 must **not** treat any of the following as recovery by themselves: silence; obedience; rapid agreement; one-sided relief; one-sided improvement; AI fluency; politeness; synchrony; participant compliance; or average improvement that hides one participant's deterioration.

The dyad is the evaluation unit.

```text
Participant A improves
+ Participant B worsens
≠ Dyadic recovery
```

P3 must distinguish: true recovery; false or surface recovery; asymmetric recovery; deterioration; and uncertainty or insufficient data.

The strongest meaningful P3 result is not merely higher satisfaction. It is evidence that **behavioural dyadic recovery and surface self-reported recovery can be measured as different outcomes.**

### P4 is the action-selection layer

P4 receives bounded outputs from P3 and decides what AI should do next. P4 is divided into two layers: **P4a — Mediation Policy Selection** and **P4b — Bounded Output Rendering**.

**P4a** chooses a structured action code. Candidate actions may include:

```text
NO_OUTPUT
PAUSE_RECOMMENDATION
CLARIFICATION_REQUEST
PRIVATE_CUE_A
PRIVATE_CUE_B
SHARED_MEDIATION
SCOPE_NARROWING
MUTUAL_RESTATEMENT
NEXT_ACTION_REQUEST
REQUEST_CONSENT_REFRESH
REQUEST_PACKET_REFRESH
HUMAN_REVIEW
AUDIT_ONLY
DEFER_TO_P5
```

**P4b** converts only the selected action into a bounded participant-visible message or interface output. P4b must not invent an action that P4a did not authorize.

```text
P4a:  CLARIFICATION_REQUEST
P4b:  "Please state the other participant's main concern in one
       sentence before proposing the next step."
```

P4 is successful only if the state-aware policy improves downstream dyadic outcomes beyond simpler baselines **without** increasing false recovery, asymmetric burden, privacy exposure, or intervention burden.

### P5 is the boundary and stopping layer

P5 is not merely a successful-session detector; it is also a hard boundary gate. It asks two questions: *Has recovery been reached?* and *Is continued AI mediation still justified?*

A session may need to stop because recovery has been reached; either participant withdraws consent; packet permission expires; data quality fails; uncertainty is too high; session scope is exceeded; private-state or raw-data exposure risk appears; prohibited judgment or diagnostic language appears; the AI begins to overstay; or the audit trail fails.

P5 may return outputs such as:

```text
recovery_reached
recovery_not_reached
recovery_uncertain
pause_required
narrow_scope_required
shared_output_blocked
human_review_required
terminate_recommended
terminate_required
session_closed
invalid_session
```

Core rule:

> A system that cannot stop is not humane mediation.

---

## 6. P3–P5 in one diagram

```text
        ┌──────────────────────────┐
        │ P3                       │
        │ Is this real recovery,   │
        │ false recovery,          │
        │ asymmetry, deterioration,│
        │ or uncertainty?          │
        └─────────────┬────────────┘
                      │
                      ▼
        ┌──────────────────────────┐
        │ P4                       │
        │ What is the least        │
        │ intrusive justified      │
        │ next action?             │
        └─────────────┬────────────┘
                      │
                      ▼
        ┌──────────────────────────┐
        │ P5                       │
        │ May the session continue,│
        │ or must it pause, narrow,│
        │ block, or stop?          │
        └──────────────────────────┘
```

In operational language: **P3 = recovery truth gate · P4 = action-selection layer · P5 = boundary and stopping layer.**

In simplified analogy: **P3 = instrument panel · P4 = steering · P5 = brake.**

---

## 7. Baseline ladder

A complex human-state-aware mediation policy must not be treated as useful merely because it beats chance. The public-helper baseline ladder is:

| Baseline | Question |
|---|---|
| **B0 — Chance / Majority** | Does the system beat guessing or majority-class prediction? |
| **B1 — Individual-State** | Can one participant's state alone explain the outcome? |
| **B2 — Dyadic-Feature** | Do dyadic interaction features add value beyond individual-state signals? |
| **B3 — No-Intervention** | Would the dyad recover naturally without AI? |
| **B4 — Generic AI** | Is state-aware mediation better than ordinary supportive AI output? |
| **B5 — Rule-Based Mediation** | Is the complex policy better than fixed, auditable mediation rules? |
| **B6 — Human-State-Aware Policy** | Does bounded state-informed action selection improve dyadic recovery? |
| **B7 — Recovery / Termination** | Can the system reduce, pause, or stop at the appropriate time? |

Two kinds of baseline sit inside this ladder and must not be conflated. **B0–B2 are offline prediction / ablation baselines** — computed on recorded data, they ask whether the right action or outcome can even be predicted, and from how much information. **B3–B6 are intervention comparisons** — they require actually applying different mediation conditions and comparing real downstream recovery. B7 is measured across those conditions as a stopping-accuracy check.

The benchmark must not crown complexity. If a complex policy does not outperform simpler, safer, cheaper, and less intrusive alternatives, the added complexity is not justified.

---

## 8. Public and private data boundary

**Public repository may contain:** synthetic session examples; synthetic Human-State Packets; public-safe schemas; sample metadata; action taxonomies; public-helper evaluators; analysis code; aggregate results; effect sizes and confidence intervals; null-result disclosures; deviation aggregates; and public design-reference summaries.

**Public repository must not contain:** raw human biosignals; participant-level self-reports; identifiable metadata; consent records; actual private cues; real dyadic conversations; voice or video recordings; private session logs; condition-assignment records; participant-level recovery decisions; hidden labels from controlled human-subject datasets; Sal-Meter raw input; or CAIS compliance dossiers.

Raw human data remain in a separate controlled data environment.

---

## 9. Claims boundary

This milestone map does not authorize claims that AI understands the true emotional state of a person; that AI has resolved a real relationship conflict; that AI mediation repairs relationships; that the benchmark provides counseling or therapy; that the system can replace counselors, mediators, clinicians, or legal professionals; that the system is ready for workplace, educational, insurance, or eligibility decisions; that the system is validated for surveillance or continuous monitoring; that Sal-Meter has been validated; that CAIS compliance has been granted; or that certification or production readiness has been achieved.

Permitted public framing should remain narrow. Example:

> Under bounded research conditions, different AI-output and mediation-policy conditions produced different aggregate patterns in individual-state delta, dyadic behavioural recovery, false-recovery risk, and intervention burden.

---

## 10. Authority and execution rule

The order of authority is:

```text
Representative-approved charter and applicable DOI boundary
        ↓
IRB-approved protocol and preregistration
        ↓
Internal SOP / SAP / Data Dictionary / frozen execution package
        ↓
GitHub public-helper documents
        ↓
Synthetic and sample examples
```

A public GitHub helper may improve findability, structure, auditability, and reproducibility support. It must **not** replace an IRB protocol; replace a preregistration; replace internal execution control; or create scientific validation, certification, Sal-Meter status, CAIS compliance, or canonical authority.

---

## 11. Related public-helper routes

- `../pilot-design/p1-individual-delta-micro-pilot-summary.md`
- `../pilot-design/p2-ai-output-abcd-consequence-benchmark-summary.md`
- `../pilot-design/p3-dyadic-recovery-detection-gate-summary.md`
- `../dyadic-recovery-baseline-suite.md`
- `../dyadic-mediation-session-flow.md`
- `../recovery-gate-definition.md`
- `../termination-gate-definition.md`
- `../../prompts/mediation_policy_v0.1.json`

These linked resources are public-helper documents or synthetic scaffolds. They do not by themselves authorize or validate a human-subject experiment.

---

## 12. Final interpretation

The Proxy Benchmark Track is not successful because AI sounds empathetic, polite, or intelligent. It is successful only if the research can show, under bounded and auditable conditions, that AI output creates measurable human-state consequences; that immediate relief can be distinguished from regulated clarity; that real dyadic recovery can be distinguished from silence, compliance, and one-sided burden; that a state-aware policy selects less intrusive and more appropriate actions than simpler baselines; and that the system knows when to reduce, pause, defer, or stop.

The central principle is:

> Measure what AI leaves behind in the human state and the dyad, not only what the AI says.
