# Proxy Reference Benchmark and Sal-Meter Bridge

**Public Design-Reference Summary**

> Status: research-stage · non-clinical · non-diagnostic · non-therapeutic · non-surveillance · benchmark-support
>
> This page is a technical **helper surface**. It summarizes and routes; it does not define canonical authority, which remains with the DOI-registered records and the OSF research hub. This document contains **no OE/EE/RE internals, model weights, operating thresholds, Sal-Meter signal-processing internals, or raw human data**.
>
> The Proxy Benchmark Track is **not** Sal-Meter. Any Sal-Meter comparison described here is a future step, gated by the Sal-Meter core track's own milestones.

---

## Why a proxy reference benchmark is needed

Human-State Delta (HSD) and false recovery have no single absolute ground truth in the way blood glucose does. So the benchmark is not one absolute number. It is a fixed comparison baseline built from a frozen proxy measurement stack, standardized scenarios, personal baselines, behavioral and self-report and relational outcomes, recovery trajectories, and quality/missingness/abstention rules.

Its purpose is to make later signals comparable. If a new signal appears — including a future Sal-Meter signal — a fixed baseline is what makes it possible to ask whether that signal is actually *more useful* rather than merely *new*.

## Two end-of-P3 artifacts

The Measurement Stack Validation Subtrack (see the companion summary) issues two distinct artifacts at the end of P3. They have different jobs:

- **Proxy Measurement Stack Freeze** — fixes *which* devices and signals are used: deployment profiles (e.g., phone-only, phone-plus-wearable, room-assisted, high-assurance research), per-modality confidence and abstention rules, and out-of-scope conditions.
- **Proxy Reference Benchmark** — fixes *what is compared and how*: standardized scenarios, event timelines, personal baselines, HSD feature families, genuine/false/asymmetric recovery definitions, behavioral outcomes, quality/missingness/abstention rules, analysis metrics, and holdout/repeatability criteria.

Naming note: "Freeze" is used rather than "Lock" to keep these distinct from the Sal-Meter core track's LOCK milestones.

**The Proxy Reference Benchmark does not claim to be an absolute ground truth of human state.**

## Scenario families

Conflict, general stress, and meditation move state in different directions and are not collapsed into one unified score. The conflict P1–P3 baseline is locked first; stress and meditation are treated as separate benchmark families for later expansion.

## The Sal-Meter Bridge (future comparison)

A Sal-Meter signal, once available, is added onto the frozen baseline rather than replacing it. The comparison is framed as a same-session, four-view design:

- **A. Phone-only**
- **B. Frozen Proxy Stack**
- **C. Sal-Meter-only bounded signal view**
- **D. Frozen Proxy Stack + Sal-Meter**

Two comparisons matter:

- **Sal-Meter alone vs. the existing proxy stack** — does it provide similar information with fewer devices, capture change earlier, discriminate false recovery better, or repeat more reliably?
- **Incremental value (most important)** — added on top of the existing proxy stack, does it actually increase predictive/discriminative power, add non-redundant information, and better capture false recovery or asymmetric burden?

"Better" is judged on a balance of HSD sensitivity, state discrimination, recovery discrimination, lead time, repeatability, incremental value, simplicity, robustness, abstention, and burden/privacy — never accuracy alone. **Novelty of a Sal-Meter signal alone does not establish superiority.**

## Sequencing and gating

```
P0 synchronization / candidate stack
→ P1 HSD sensitivity → P2 consequence discrimination → P3 recovery validity
→ Proxy Measurement Stack Freeze + Proxy Reference Benchmark
→ P4–P5 policy / termination (bounded summaries only)
→ Sal-Meter core-track LOCK milestones
→ future four-view incremental-value comparison
```

The proxy track is not a temporary stand-in until Sal-Meter arrives. It is the track that builds the yardstick against which any deeper or simpler future signal is judged.

## Boundary

Public material is limited to the rationale, the freeze/benchmark concepts, scenario-family separation, and the four-view comparison structure. Not published: OE/EE/RE internal formulas, model weights, real cutoffs, Sal-Meter signal-processing internals, feature-fusion internals, operating thresholds, per-participant mappings, and any raw human data. GitHub helps builders; the DOI/OSF records define authority.
