# Measurement Stack Validation Subtrack

**Public Design-Reference Summary**

> Status: research-stage · non-clinical · non-diagnostic · non-therapeutic · non-surveillance · benchmark-support
>
> This page is a technical **helper surface**. It summarizes and routes; it does not define canonical authority, which remains with the DOI-registered records and the OSF research hub. This document contains **no internal thresholds, statistical criteria, device operating values, or raw human data**.

---

## Why this subtrack exists

Across the Proxy Benchmark Track, each phase has a clear primary research question — P0 synchronization, P1 individual state delta, P2 AI-output consequence divergence, P3 genuine/false recovery. A separate question sits *underneath* all of them and was previously implicit:

> Which sensor / device combination most honestly captures Human-State Delta (HSD) and best distinguishes genuine from false recovery?

Finding that combination is not a side task. It is a primary methodological contribution of the track, because:

- **It creates the reference.** Without a fixed comparison baseline for HSD and false recovery, downstream claims have weak footing.
- **It enables future comparison.** Any later signal (including a Sal-Meter signal) can only be judged *more useful* — simpler, faster, better at false-recovery discrimination — against a fixed proxy baseline. Without one, a new signal is only known to be *new*, not *useful*.

The Measurement Stack Validation Subtrack (MSV) makes this cross-cutting question explicit.

## It is a cross-cutting axis, not a new phase

MSV is not a new P-stage. It runs alongside P0–P3. Each phase keeps its own primary question and gate; the same data is used in parallel to evaluate device contribution.

```
P0 ─┐
P1 ─┼─ Measurement Stack Validation (secondary analysis at each phase)
P2 ─┤
P3 ─┘
   → Proxy Measurement Stack Freeze + Proxy Reference Benchmark
   → deployment profiles (later) → future incremental-value comparison (later)
```

## What each stage reveals about the stack

| Stage | Primary phase milestone | Cross-cutting measurement question |
|---|---|---|
| P0 (Capture Readiness) | Signal/event synchronization | Which devices connect, synchronize, and replay reliably; burden, dropout, drift |
| P1 (HSD Sensitivity) | Individual state delta (R vs Q) | Which modalities track within-person change; repeatability; residual signal after motion contamination; phone-only vs. full-reference agreement; phone+wearable increment |
| P2 (Consequence Discrimination) | AI-output consequence divergence | Which combinations distinguish output-condition differences; false-alarm-only arousal vs. clarity/behavioral outcome; phone-only retention; incremental value of added sensors |
| P3 (Recovery Validity) | Genuine / false / asymmetric recovery | Which combinations avoid missing false recovery and one-sided burden; behavioral-stability vs. physiological-burden discordance |

Two constraints hold throughout:

- Sensor analysis is a **secondary analysis** at each phase and does not replace that phase's primary gate. (P1's primary effect is R vs Q, not sensor performance.)
- **No premature sensor reduction before the end of P3.** Final reduction waits until recovery-validity evidence exists.

To answer the stack question at all, each phase carries either an instrumented subset within the main study or a parallel measurement cohort using the same task.

## The goal is not a single winning sensor

HSD has no single absolute ground-truth device. The output is therefore not one winning device but a set of purpose-specific deployment profiles — for example a phone-only core, a phone-plus-wearable configuration, a room-assisted configuration, and a high-assurance research configuration. Device combinations are judged on a balance of HSD sensitivity, consequence-discrimination, recovery-validity, generalization across people/days/devices, robustness, abstention quality, and burden/privacy — never accuracy alone.

## End-of-P3 outputs

At the end of P3, MSV issues two distinct artifacts (see the companion summary, *Proxy Reference Benchmark and Sal-Meter Bridge*):

- **Proxy Measurement Stack Freeze** — fixes *which* devices/signals are used.
- **Proxy Reference Benchmark** — fixes *what is compared and how*.

The naming uses "Freeze" (not "Lock") to keep this distinct from the Sal-Meter core track's LOCK milestones.

## Boundary

Public material for this subtrack is limited to the cross-phase design concept, the per-stage sensor questions, deployment-profile categories, and the freeze/benchmark concept. Not published: internal statistics and power/sample-size criteria, sensor-reduction cutoffs, feature-fusion internals, model weights, device operating values, per-participant contributions, and any raw human data. GitHub helps builders; the DOI/OSF records define authority.
