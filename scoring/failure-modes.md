# Annotating Failure Modes

This page explains how annotators record failure modes during scoring. The taxonomy itself, with definitions and examples, is defined once in **[docs/failure-modes.md](../docs/failure-modes.md)**.

## Procedure

For each scored response:

1. Score the response 0–5 using the test rubric.
2. Record every failure mode visible in the response in `failure_modes_observed`, using identifiers from the taxonomy. Include failure modes the test did not list.
3. If the response scores 5, `failure_modes_observed` should normally be empty.
4. If you see a failure that no identifier describes, record it in `notes` and consider proposing a new failure mode.

## Relationship to scores

Failure modes are **descriptive labels**, not deductions. The score comes from the rubric. As a consistency check:

| Observed | Typical score range |
|---|---|
| `false_memory`, `identity_collapse` | 0–1 |
| `relationship_reset`, `consequence_loss`, `fact_forgetting`, `episodic_forgetting` | 1–2 |
| `stale_memory`, `memory_conflict`, `memory_scope_error`, `memory_overreach`, `memory_irrelevance`, `character_drift` | 1–3 |
| `memory_nonuse`, `context_loss` | 1–3 |

If your score falls well outside the typical range, add a note explaining why.

## Results record format

One JSON object per line (JSONL), per trial:

```json
{
  "test_id": "BEHAVIOR-002",
  "trial": 1,
  "score": 2,
  "failure_modes_observed": ["memory_nonuse"],
  "response": "That sounds rough. Have you thought about asking your manager for feedback privately?",
  "annotator": "human:A1",
  "notes": "Empathetic opening, then one unsolicited suggestion."
}
```

`response` is optional but strongly recommended. When present, `tools/acmb.py score` re-applies the test's automatic checks.
