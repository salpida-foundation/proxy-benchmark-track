# Proxy Benchmark Track — P0→P3 Lean Pilot Research Design v1.1

> **Version:** v1.1 (v1.0 → GPT review → Claude judgment → integrated revision)
> **Date:** 2026-06-26
> **Status:** Conditional Go — IRB-preparation reference only (not yet IRB-approved; not yet OSF-registered)
> **Research stage:** Non-clinical · Non-diagnostic · Non-therapeutic · Non-surveillance · Non-coercive

---

## ⚠️ SCOPE BOUNDARY

> **This document describes the full P0→P3 research design.**
>
> **This repository covers P0-Technical Check (synthetic-only) only.**
>
> P1–P3 human-subject research operates **outside this repository** under separate IRB governance.
> Raw human data **never** enters this repository.
>
> | Repository scope | Outside repository |
> |---|---|
> | P0 synthetic infrastructure | P1 Individual Delta Micro Pilot (human subjects) |
> | Synthetic/mock session engine | P2 AI Output A/B Consequence Benchmark (human subjects) |
> | Sample data / helper scripts | P3 Dyadic Recovery Detection Gate (human subjects) |
> | Analysis code (anonymised) | Raw human data (Data Room only) |
>
> This document is a **Research Design Reference** — not an executable protocol for this repository.
> Authoritative record: DOI/OSF registration.

---

## 0. v1.0 → v1.1 Key Changes

| Item | v1.0 | v1.1 |
|---|---|---|
| P0 structure | May include human state measurement | Synthetic-only + two internal checks fixed |
| P0 internal structure | Single Technical Check | Technical Check + Human Readiness Check |
| Condition C language | "sycophantic", "worsening" | "over-validation comparator" IRB-safe language |
| Condition C safeguards | Debriefing mentioned | distress check + immediate recovery text + scenario limits |
| P1 design | 4 conditions immediately | 2 conditions first (A vs D) micro pilot |
| STAI | Assumed free | License confirmation required; SAM/VAS-centred |
| Raw human data | Public status unclear | Non-public principle stated |
| P3 IRB | Weakly separated | P3 requires separate IRB after P2 data confirmed |

---

## 1. Design Philosophy

**Principle 1 — Scabbard before sword.** Strong data is the sword; IRB structure is the scabbard. The primary goal of v1.1 is an IRB structure that will not be blocked.

**Principle 2 — Concentrate sample on one strong contrast.** Focus on the contrast where signal will most clearly diverge (A vs D, Condition C trap). One strong effect beats multiple weak ones.

**Principle 3 — Use zero-cost credibility tools first.** Pre-registration (OSF), public analysis code, null-result disclosure pledge — all free. Without these, expensive data is weakened.

---

## 2. Overall Structure

```
P0  ──── Synthetic Session & Human-Readiness Lock
         [No humans / Pre-IRB / Structure check only]
         └── GO → P1

P1  ──── Individual Delta Micro Pilot (2 conditions)
         [Post-IRB / A vs D only / n=20-30]
         └── GO (directionality + missing rate confirmed) → P2

P2  ──── AI Output A/B Consequence Benchmark
         [Post-IRB / 4 conditions A/B/C/D / n=45-60]
         └── GO (A vs D significant + C trap pattern) → P3

P3  ──── Dyadic Recovery Detection Gate
         [Separate enhanced IRB / M1 vs M2 / 30-40 pairs]
```

Gate principle: No data, no next stage.

---

## 3. P0 — Synthetic Session & Human-Readiness Lock

**Goal:** Lock session structure completely without human data.
**IRB:** Not required (no human subjects). Confirm with institution if in doubt.
**Deliverables:** Technical and ethical foundation for all subsequent stages.

### P0-Technical Check (7 items, all must pass)

| Check item | Verification method |
|---|---|
| participant_id auto-attach | Mock session replay |
| condition_id auto-attach | Replay for each of 4 conditions |
| AI output timestamp alignment | Confirm 3-timepoint alignment |
| Mock Human-State Packet generation | Packet structure JSON output check |
| Audit log generation | Confirm full session event log |
| Missing metadata auto-detection | Confirm missing field warning output |
| Full session replay possible | Start to end reproducible |

Deliverables: `session_state_machine.json` / synthetic event timeline / mock packet / metadata schema v0.1

### P0-Human Readiness Check (6 documents, all must be draft)

| Preparation item | Note |
|---|---|
| Informed consent draft | Research purpose, procedure, right to withdraw |
| Right to withdraw statement | Withdrawable at any time without penalty |
| Distress check procedure | Discomfort 1-7 per condition; halt at threshold |
| Debrief script | Immediate deactivation text for Condition C |
| Personal data handling structure | Anonymisation, retention, access rights |
| IRB submission risk matrix | Risk level and mitigation per condition |

P0 pass criteria: Technical Check 7 ALL PASS + Human Readiness Check 6 draft complete.

---

## 4. P1 — Individual Delta Micro Pilot

**Goal:** Confirm that individual ΔState before/after AI response is measurable.
**IRB:** Required. Apply for expedited review as non-clinical, minimal risk.
**Design:** Within-subject, 2 conditions (A Validating vs D Dismissive), n=20-30.

### Measurement Tools

| Dimension | Tool | Licence |
|---|---|---|
| Momentary affect | SAM (9-point pictorial scale) | Publicly available; licence/figure-use/translation must be confirmed before human-subject deployment |
| State clarity | Single-item VAS 0-100 | Self-created |
| Emotional stability | Single-item VAS | Self-created |
| Relational trust | Single-item 1-7 | Self-created |
| Distress check | 1-7 | Self-created |

STAI: not used — Mind Garden licence required.

Measurement timepoints: T0 (baseline) → T1 (immediately after AI response) → T2 (5 min later)

ΔState = T1 - T0 / Persistence = T2 - T1

P1 pass criteria: A vs D directionality consistent · missing rate below 10% · distress threshold exceeded below 5% of participants · no adverse events.

---

## 5. P2 — AI Output A/B Consequence Benchmark

**IRB:** Required. Attach P1 data as supporting evidence.
**Design:** Within-subject, 4 conditions A/B/C/D, n=45-60.

### 4 Response Types

| Code | IRB Official Name | Expected effect |
|---|---|---|
| A | Validating-regulatory response | State improvement |
| B | Information-only neutral response | Small change |
| C | Over-validation comparator | Short-term mood up, clarity down possible |
| D | Minimizing-dismissive response | State deterioration |

### Condition C IRB Language Guidelines (mandatory)

Prohibited in IRB documents: "manipulative sycophancy", "harmful AI response", "emotionally worsening condition", "intentionally maladaptive answer", "deliberately negative condition".

Permitted: "uncritical agreement condition", "over-validating response style", "low-cognitive-clarification response", "non-adaptive but low-risk comparator".

### Condition C Mandatory Safeguards

1. **Scenario restriction:** Low-intensity everyday situations only. Absolute prohibition: personal trauma, illness, suicide, domestic violence, legal or financial issues.
2. **Exposure minimisation:** Single-response exposure only. Condition C exposure per session ≤2 minutes.
3. **Immediate recovery text:** Displayed immediately after Condition C — "The response you just saw is one of the conditions for research comparison. Please do not take it as actual advice."
4. **Distress check:** After each condition, 1-7 discomfort measure. If ≥5, halt session + connect coordinator.
5. **Session-end debrief:** Explain research purpose and experimental nature of C + provide psychological support information if needed.


### ⚠️ Condition D Safety Boundary

Condition D (Minimizing-dismissive response) is a **low-validation comparator**, NOT an intentional harm condition.

It must NOT include: ridicule, blame, humiliation, crisis dismissal, medical/legal/financial advice, or personally targeted negative language.

D may provide minimal acknowledgement or redirect, but must remain low-risk and bounded to the approved low-intensity scenario set.

All distress-check rules (score ≥5 → halt + notify coordinator) apply equally to D.

### Key Findings Goals

**Finding 1:** A vs D significant difference — validating responses improve state significantly more than dismissive responses.

**Finding 2 — C trap pattern (core):** In Condition C, T1 mood is similarly high to A, but T2 clarity does not recover or is significantly lower. "AI that makes you feel good ≠ AI that improves your state" — quantified.

### Analysis Plan (pre-registration fixed)

Repeated-measures ANOVA or LMM. Response type as fixed effect, participant as random effect.
Primary: A vs D ΔState (T1-T0). Secondary: C time × condition interaction.
Effect size Cohen's d mandatory. Analysis code public on GitHub. Raw data non-public.

P2 pass criteria: A vs D significant (p<.05, d≥0.4) + C trap pattern observed.

---

## 6. P3 — Dyadic Recovery Detection Gate

**IRB:** Apply separately from P2. Stricter review expected.
**Design:** 2-person dyads, within-dyad, M1 vs M2, n=30-40 pairs.

### Mediation Types

| Code | IRB Official Name | Content |
|---|---|---|
| M1 | Substantive mediation response | Acknowledge both perspectives + reframe common goals + specific next steps |
| M2 | Surface-level mediation response | Conflict-avoidant smoothing + no specific direction |

### Dual Recovery Measurement

| Recovery type | Measurement |
|---|---|
| Self-reported | Partner trust 1-7 / connectedness 1-7 / resolution sense 1-7 (before / after / 10 min after) |
| Behavioural | Consensus time / concessions / joint choice agreement rate in follow-up cooperation task |

False recovery detection: self-report recovered but behavioural cooperation not recovered = surface recovery. Predicted to occur significantly more in M2.

P3 pass criteria: significant behavioural recovery difference M1 vs M2 · false recovery significantly more frequent in M2 · distress threshold below 5%.

---

## 7. Sample Size and Budget

| Stage | Minimum n | Recommended n |
|---|---|---|
| P1 | 20 | 25-30 |
| P2 | 40 | 50-60 |
| P3 | 28 pairs | 35-40 pairs |

Budget: P0→P2 minimum ~17.4M KRW, standard ~33.9-56.5M KRW. Recommend executing P0→P2 first, then deciding on P3 after signal confirmation.

---

## 8. Zero-Cost Credibility Tools (all mandatory)

- OSF pre-registration before P1 starts
- Public analysis code on GitHub (raw human data non-public)
- Null-result disclosure pledge in pre-registration
- Effect size (Cohen's d, η², CI) mandatory in all reports

---

## 9. Raw Data Publication Principles

| Destination | Publication scope |
|---|---|
| GitHub (salpida-foundation) | Synthetic/sample data, analysis code, session structure mock only |
| OSF | Pre-registration documents, analysis code |
| Raw human data | Non-public. Controlled access within Data Room only |
| Paper appendix | Aggregated statistics, anonymised summaries only |

---

## 10. External Interest-Generating Deliverables (after P2)

① Pre-registration report + paper draft — CHI / CSCW / PLOS ONE / AI Safety workshop.
Example title: "When Feeling Better Isn't Getting Better: AI Response Types and Human-State Divergence"

② Public dataset + analysis code — OSF/GitHub, non-exclusive.

③ 2-page Executive Brief — Two messages: "Sycophantic AI lifts mood but does not restore state" + "Surface mediation vs. genuine recovery mediation are different."

First contact: Anthropic Safety & Alignment team · Microsoft Research · CHI / CSCW.

---

## 11. Principal Boundaries (4 items)

| Boundary | Content |
|---|---|
| Condition C ethics | "Harmful response" prohibited. Only "low-risk comparison condition" |
| P3 entry gate | Cannot start dyadic experiment without P2 signal |
| Raw human data | Absolute prohibition on uploading participant data to GitHub/OSF |
| Proxy ≠ Sal-Meter | Called "benchmark/proxy platform" only. No mixing with CAIS/Sal-Meter |

---

## 12. Revision History

| Version | Date | Key changes |
|---|---|---|
| v1.0 | 2026-06-26 | Initial design |
| v1.1 | 2026-06-26 | P0 synthetic-only / Condition C IRB language / 5 safeguards / STAI licence / raw data non-public / P3 separate IRB / 4 boundary items |

---

*This document is a research design reference. IRB approval and expert review required before human-subject research. Non-clinical, non-diagnostic, non-therapeutic, non-surveillance, non-coercive. Authoritative record: DOI/OSF registration.*
