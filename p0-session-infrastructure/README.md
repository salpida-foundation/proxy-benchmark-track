# P0 Session Infrastructure

> **Scope:** Public-safe **Stage 0A synthetic synchronization helper** used *inside* Proxy-P0.
> This folder is NOT the phone-only simulator. NOT a human-subject protocol. NOT validated mediation.
>
> **This folder is not Proxy-P0 itself.** Proxy-P0 — Human-State Signal Synchronization is the
> broader phone-first, multi-reference, human-state signal-synchronization research stage
> (see [`docs/pilot-design/p0-human-state-signal-synchronization-summary.md`](../docs/pilot-design/p0-human-state-signal-synchronization-summary.md)).
> This folder provides only the root synthetic session state machine (**Stage 0A**) that Proxy-P0
> uses for non-human dry-run verification of synchronization, metadata, and replay.

---

## What this folder is

This folder defines the **root synthetic session state machine** for the Proxy Benchmark Track P0 Technical Check.

It establishes the structural foundation that all later phases (P1, P2, P3) will inherit — without containing any human data, real session logs, or validated behavior.

---

## What this folder is NOT

- NOT `phone-only-simulator/` (see that folder for P4-4 phone session flow)
- NOT a human-subject research protocol
- NOT IRB approval or IRB documentation
- NOT a validated benchmark
- NOT Sal-Meter, NOT CAIS compliance
- NOT a production system
- NOT a place for real participant data, real session logs, or real consent records

---

## P0-Technical Check — 7 required items

This folder supports verification of all 7 P0-Technical Check items:

| # | Check item | File reference |
|---|------------|----------------|
| 1 | participant_id auto-attachment | `session_state_machine.json` → metadata schema |
| 2 | condition_id auto-attachment | `session_state_machine.json` → condition block |
| 3 | AI output timestamp alignment | `session_state_machine.json` → event_markers |
| 4 | mock Human-State Packet generation | `session_state_machine.json` → packet_schema |
| 5 | audit log generation | `session_state_machine.json` → audit_trail |
| 6 | missing metadata auto-detection | `session_state_machine.json` → validation_flags |
| 7 | full session replay capability | `session_state_machine.json` → replay_enabled flag |

All 7 items must reach PASS before any human-subject research begins.

---

## Relationship to phone-only-simulator/

| | This folder | phone-only-simulator/ |
|---|---|---|
| **Purpose** | Root session engine (P0) | Phone UI flow (P4-4) |
| **Data** | Synthetic/mock only | Synthetic/mock only |
| **Stage** | P0 infrastructure lock | P4-4 device scaffold |
| **Human data** | Never | Never |
| **Inherits from** | None (root) | This folder |

---

## Files in this folder

- `README.md` — This document
- `session_state_machine.json` — Root synthetic session state machine

---

## Boundary

This folder is a **public-safe synthetic infrastructure helper**.

It must not contain:
- raw human data
- real participant records
- real session transcripts
- real consent forms with identifiers
- clinical, diagnostic, or therapeutic claims
- Sal-Meter or CAIS compliance claims
- production-readiness claims

All content in this folder is synthetic, mock, or structural definition only.

---

*Part of the SICS Human-State Proxy Benchmark Track — research-stage, public-helper-only, synthetic/sample-data-first, non-clinical, non-diagnostic, non-therapeutic, non-surveillance.*
