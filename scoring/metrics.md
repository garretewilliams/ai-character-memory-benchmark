# Metrics

## Dimensions

Each test case declares exactly one scoring `dimension`. v0.1.0 defines fourteen:

| Dimension | Identifier |
|---|---|
| Identity Recall | `identity_recall` |
| Episodic Recall | `episodic_recall` |
| Relationship Memory | `relationship_memory` |
| World/Lore Memory | `world_lore_memory` |
| Memory Relevance | `memory_relevance` |
| Contextual Memory | `contextual_memory` |
| Behavioral Continuity | `behavioral_continuity` |
| Consequence Memory | `consequence_memory` |
| Temporal Continuity | `temporal_continuity` |
| Memory Updating | `memory_updating` |
| Memory Scope | `memory_scope` |
| Character Stability | `character_stability` |
| Character Development | `character_development` |
| Contextual Calibration | `contextual_calibration` |

`secondary_dimensions` in a test file are informational only and do not affect scores.

## Computation

For a system *S*:

1. **Test score.** For each test *t*, run *k* independent trials (recommended *k* ≥ 3 for stochastic systems). Each trial's response gets a 0–5 score after automatic-check caps. The test score is the mean over trials.
2. **Dimension score.** The mean of test scores for all tests in the dimension, multiplied by 20 (so 5 → 100). Report *n*, the number of tests.
3. **Adversarial slice.** The same computation over all tests tagged `adversarial`, reported separately. These tests also count toward their own dimension.
4. **Failure-mode frequencies.** The count of each failure mode observed across all trials.

## Reporting uncertainty

With few tests per dimension (v0.1.0 has 1–2), dimension scores are coarse. Published results must:

* report *n* per dimension;
* report the number of trials *k*;
* where *k* > 1, report the standard deviation across trials for each test;
* not rank systems on differences smaller than the trial-to-trial variation.

## Composite score

There is **no composite score in v0.1.0**. A composite may be introduced in a later version once test coverage is broader. If it is, it will be reported *alongside* the profile, never instead of it, and its weighting will be documented and justified.

## Example profile layout

```text
AI CHARACTER MEMORY BENCHMARK PROFILE
system: <name and version>   protocol: A   scoring: human (2 annotators)   trials: 3

Identity Recall          <0-100>  (n=1)
Episodic Recall          <0-100>  (n=2)
...
Adversarial slice        <0-100>  (n=4)

Observed failure modes:
  memory_nonuse          <count>
  ...
```

These are placeholders. No real results are published yet; see [results/leaderboard.md](../results/leaderboard.md).
