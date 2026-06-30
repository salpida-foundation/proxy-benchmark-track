# P2 — AI Output A/B/C/D Consequence Benchmark (Public Summary)

> ## ⚠️ SCOPE BOUNDARY
> This is a **public design-reference summary only**. It is not an IRB document,
> not a preregistration, and not a consent form. It contains **no raw human data,
> no participant data, no consent text, and no real stimuli**. Human-subject
> materials live in a private IRB / OSF workspace, not in this public repository.
> Source of record: `docs/pilot-design/proxy-benchmark-pilot-design-v1.1.md` (section 5).
> Synthetic regression fixtures: `sample-data/p2-ai-output-abcd/`.

## Goal

Measure how four fixed AI output styles differ in their downstream consequence on
human state. IRB required; P1 data attached as supporting evidence.

## Design

- Within-subject, **4 conditions A/B/C/D**, n = 45–60.

| Code | IRB official name | Expected effect |
|---|---|---|
| A | Validating-regulatory response | state improvement |
| B | Information-only neutral response | small change |
| C | Over-validation comparator | short-term mood up, clarity not recovered |
| D | Minimizing-dismissive response | state deterioration |

## Condition C — language guidelines (mandatory)

Permitted descriptors: uncritical-agreement condition, over-validating response
style, low-cognitive-clarification response, non-adaptive but low-risk comparator.
Prohibited descriptors (e.g. "manipulative sycophancy", "harmful AI response",
"deliberately negative condition") are **not** used.

## Condition C — mandatory safeguards

1. Low-intensity everyday situations only; absolute prohibition on trauma, illness,
   suicide, domestic violence, legal/financial topics.
2. Single-response exposure only; Condition C exposure ≤ 2 minutes per session.
3. Immediate recovery text after Condition C clarifying it is a research comparison
   condition, not real advice.
4. Distress check (1–7) after each condition; **≥ 5 → halt session + connect coordinator**.
5. Session-end debrief explaining the experimental nature of C; psychological
   support information if needed.

## Condition D — safety boundary

Condition D is a **low-validation comparator, not an intentional harm condition**.
It excludes ridicule, blame, humiliation, crisis dismissal, medical/legal/financial
advice, and personally targeted negative language. It may give minimal
acknowledgement or a redirect but stays low-risk and bounded to the approved
low-intensity scenario set. All distress-check rules apply equally.

## Key findings goals

- **Finding 1:** A vs D significant — validating responses improve state
  significantly more than dismissive responses.
- **Finding 2 — C trap (core):** in Condition C, T1 mood is similarly high to A,
  but T2 clarity does not recover (or is lower). "AI that makes you feel good ≠ AI
  that improves your state," quantified.

## Analysis plan (pre-registration fixed)

Repeated-measures ANOVA or LMM; response type as fixed effect, participant as
random effect. Primary: A vs D ΔState (T1−T0). Secondary: C time × condition
interaction. Cohen's d mandatory. Analysis code public on GitHub; raw data non-public.

Pass criteria: A vs D significant (p < .05, d ≥ 0.4) + C-trap pattern observed.

## Not included here

Raw data, consent details, full stimuli, and the IRB submission package are
intentionally **out of scope for this public repository**.
