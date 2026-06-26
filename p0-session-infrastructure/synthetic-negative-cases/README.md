# Synthetic Negative Cases

> **Purpose:** Test fixtures that intentionally trigger HALT_AND_FLAG, TRANSITION_REJECTED, or BOUNDARY_VIOLATION.
> A robust P0 system must catch failures, not just confirm successes.
> All files are synthetic/mock only. No real participant data.

---

## Test Case Files

| File | Check | Expected outcome |
|------|-------|------------------|
| `missing_participant_id.json` | Check 1: participant_id | HALT_AND_FLAG |
| `missing_condition_id.json` | Check 2: condition_id | HALT_AND_FLAG |
| `missing_t1_timestamp.json` | Check 3: timestamp alignment | HALT_AND_FLAG |
| `invalid_transition_recovery_to_ai_output.json` | Forbidden transition | TRANSITION_REJECTED |
| `boundary_violation_real_data_flag.json` | Boundary flag integrity | BOUNDARY_VIOLATION_FLAGGED |

## How to Use

Run `evaluation-baseline/lint_p0_session_state_machine.py` for the main schema check.
For negative cases: load each file and confirm expected outcome is triggered.
PASS = system correctly rejects/flags. FAIL = system silently accepts invalid input.

---

*All files: synthetic test fixtures only. No real participant data. No clinical content. Not research validation.*
