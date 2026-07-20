# Proxy-P0 — Human-State Signal Synchronization

**Public Design-Reference Summary**

> Status: research-stage · non-clinical · non-diagnostic · non-therapeutic · non-surveillance · benchmark-support
>
> This page is a technical **helper surface**. It summarizes and routes; it does not define canonical authority. Canonical authority remains with the DOI-registered records and the OSF research hub. This document contains **no raw human data, no internal thresholds, and no device-specific operating values**.
>
> Proxy-P0 is **not** Sal-Meter, **not** Sal-Meter Internal Phase 0, and **not** External Layer-0. It is the first research phase of the Proxy Benchmark Track.

---

## What Proxy-P0 is

Proxy-P0 is the first phase of the SICS Human-State Proxy Benchmark Track. Its job is to align a smartphone stream together with a minimal set of reference proxy sensors, fixed audio/video, and task/AI/self-report event markers onto a **single, auditable, replayable session timeline**, and to generate — from the *same* session — three comparable data views:

- **Full-Reference View** — the richest proxy comparison baseline
- **Deployment-Realistic View** — a realistic higher-assurance everyday configuration
- **Phone-Only View** — the broadly deployable configuration

The single P0 question is technical, not interpretive:

> Can multi-proxy signals, self-report, task events, and AI-output events be aligned on one replayable session timeline such that Full-Reference, Deployment-Realistic, and Phone-Only views can be reproducibly generated from the same session?

## What Proxy-P0 is *not* (claims boundary)

Proxy-P0 does **not** claim, and completion of P0 does not support claiming, any of the following:

- that a smartphone reads consciousness, or measures OE / EE / RE
- that EDA is a ground truth of emotion, or that ECG/HRV proves recovery
- that facial expression reveals true internal state
- that the Full-Reference View is a ground truth of human state
- that P0 validated human-state inference accuracy
- that P0 validated Sal-Meter
- that a phone-only AI-safety system has been completed

P0 proves only that signals arrive, align on a shared timeline, expose their own gaps/noise/drift, and can be replayed.

## Core principle — Phone-first · Multi-reference · Modular expansion

**Phone-first.** The smartphone is the deployment-facing input and is collected in every P0 human session from the first session. Phone-first is **not** phone-only: a phone-only P0 without reference proxies is out of scope, because without reference signals it is not possible to know what the phone misses (e.g., an outwardly calm session where sympathetic-arousal or cardiac signals have not recovered).

**Multi-reference.** Reference proxies are not a ground truth of human state; they are a richer comparison view than the phone alone. Human-State Delta (HSD) has no single ground-truth device, so the design relies on repeated agreement across physiology, behavior, self-report, temporal change, AI condition, and relational outcome — not on any one sensor.

**Modular expansion.** Devices with higher future-deployment relevance (a representative smartwatch, gaze/eye devices, smart glasses, a room node) have their connection schema and adapters prepared from P0, but are **not** required in every session. Their contribution to HSD is assessed later, across P1–P3, not asserted in P0.

## The three views

| View | Composition (summary) | Purpose |
|---|---|---|
| Full-Reference | Phone + reference physiological proxies + fixed audio/video + event timeline | Richest comparison baseline; sensor-ablation reference; phone-only failure-condition analysis |
| Deployment-Realistic | Phone + one wearable, or phone + room node | Realistic higher-assurance configuration; incremental-value assessment |
| Phone-Only | Front camera + microphone + touch/typing + IMU + screen/task events | Broadly deployable configuration; information-retention vs. full-reference; abstention under low quality |

Phone-only is not a late product question — it is a core question from P0 onward. Multi-device P0 data functions as **teacher data** for the phone-only view (reference = teacher, phone = deployment-target student).

## Measurement Stack Validation Subtrack (P0 → P3)

Which sensor/device combination best captures HSD and best distinguishes genuine from false recovery is **not fixed at P0**. It is evaluated progressively as a cross-phase subtrack that runs alongside each phase's primary question:

| Stage | Primary phase milestone | Cross-cutting measurement milestone |
|---|---|---|
| P0 | Signal/event synchronization | Which devices connect, synchronize, and replay reliably |
| P1 | Individual state delta | Which modalities are sensitive to individual HSD change |
| P2 | AI-output consequence divergence | Which combinations distinguish soothing vs. clarity vs. behavioral outcome |
| P3 | Genuine / false / asymmetric recovery | Which combinations do not miss false recovery or one-sided burden |

Sensor analysis is a **secondary analysis** at each phase; it does not replace that phase's primary gate. **No premature sensor reduction before the end of P3.**

## Proxy Reference Benchmark and the Sal-Meter Bridge (concept)

At the end of P3 the subtrack issues two distinct artifacts:

- **Proxy Measurement Stack Freeze** — fixes *which* devices/signals are used (deployment profiles + confidence/abstention rules + out-of-scope conditions).
- **Proxy Reference Benchmark** — fixes *what is compared and how* (standardized scenarios, event timelines, personal baselines, recovery definitions, quality/missingness/abstention rules, analysis metrics).

The Proxy Reference Benchmark does **not** claim to be an absolute ground truth of human state.

Any future Sal-Meter comparison happens later, on this fixed baseline, and only after the Sal-Meter core track's own gates. It is framed as a same-session four-view comparison — Phone-only, Frozen Proxy Stack, Sal-Meter-only, and Frozen Proxy Stack + Sal-Meter — assessing HSD sensitivity, false-recovery discrimination, repeatability, simplicity, and **incremental value**. Novelty of a Sal-Meter signal alone does not establish superiority.

## Scenario families (concept)

Conflict, general stress, and meditation change state in different directions and are **not** collapsed into a single unified HSD score. The conflict P1–P3 baseline is locked first; stress and meditation are treated as separate benchmark families for later expansion.

## Data boundary

Raw human data is not published. Public repositories carry only synthetic/sample material, schemas, evaluators, example code, and aggregate/effect-size/null results. Raw physiological signals, audio/video, real conversation, touch logs, participant-level self-report, condition assignments, identifiers, and per-participant HSD estimates are held in a controlled data room and are never placed on public GitHub or public OSF. Smartphone collection is a bounded, explicitly consented session with a defined start and end — never silent monitoring.

## Relationship to adjacent tracks

| Name | Meaning | Is it Proxy-P0? |
|---|---|---|
| Cross-Phase Program Infrastructure | GitHub · OSF · DOI · CI · public/private boundary · synthetic samples | No — shared support layer for P0–P7 |
| **Proxy-P0** | Synchronization and replayable session construction for phone + proxy sensors + events | **Yes** |
| Sal-Meter Internal Phase 0 (SM-P0) | G-only internal core state-separation phase | No — separate core track |
| External Layer-0 | iodine-redox / thiol interface external feasibility | No — separate chemistry track |

## Canonical records

This helper surface routes to, and is subordinate to, the DOI-registered records and the OSF research hub, which hold canonical authority. GitHub helps builders; DOI/OSF records define authority.
