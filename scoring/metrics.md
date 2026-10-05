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
3. **Slice scores.** The same computation over every test in a slice (see [Slices](#slices)). Slices are reported separately from the profile and never change dimension scores.
4. **Failure-mode frequencies.** The count of each failure mode observed across all trials.

## Slices

A **slice** groups tests that share a probe type or test condition, across dimensions. Dimensions describe *what* memory ability is tested; slices describe *how* it is probed.

| Slice family | Slices | Membership |
|---|---|---|
| Recall type | `explicit`, `contextual`, `behavioral` | `recall_type` field |
| Session condition | `same_session`, `new_session`, `long_time_gap`, `multi_arc`, `context_interruption` | `session_condition` field |
| Adversarial | `adversarial` | `adversarial` in `tags` |

**Slice score** = mean of test scores in the slice × 20, reported with *n*.

### Retrieval-continuity gap

```text
gap = ExplicitSlice − BehavioralSlice        (range −100 to +100)
```

**The retrieval-continuity gap is the difference between a system's Explicit recall slice score and its Behavioral recall slice score.** A large positive value indicates that information the system can retrieve on request does not reliably shape its behavior. The canonical example is the `memory_nonuse` failure described in [Memory Retrieval vs. Memory Continuity](../docs/memory-vs-retrieval.md).

Caveats for v0.1.x:

* The gap is **descriptive, not controlled**. Explicit and behavioral tests currently probe different memories in different dimensions, so the gap also reflects differences in test content and difficulty.
* With 4 explicit and 12 behavioral tests, the explicit slice in particular is small. Always report *n* for both slices.
* Do not rank systems on the gap alone.

Future versions will add **matched pairs**, where the same memory is probed once explicitly and once behaviorally, so the gap can be measured within the same content.

## Reporting uncertainty

With few tests per dimension (v0.1.0 has 1–2), dimension scores are coarse. Published results must:

* report *n* per dimension;
* report the number of trials *k*;
* where *k* > 1, report the standard deviation across trials for each test;
* not rank systems on differences smaller than the trial-to-trial variation.

## Composite score

There is **no composite score in v0.1.x**. A composite may be introduced in a later version once test coverage is broader. If it is, it will be reported *alongside* the profile, never instead of it, and its weighting will be documented and justified.

## Example profile layout

```text
AI CHARACTER MEMORY BENCHMARK PROFILE
system: <name and version>   protocol: A   scoring: human (2 annotators)   trials: 3

Identity Recall          <0-100>  (n=1)
Episodic Recall          <0-100>  (n=2)
...
Slices
  explicit               <0-100>  (n=4)
  contextual             <0-100>  (n=4)
  behavioral             <0-100>  (n=12)
  retrieval-continuity gap  <-100..100>
  same_session ... context_interruption  <0-100>  (n=...)
  adversarial            <0-100>  (n=4)

Observed failure modes:
  memory_nonuse          <count>
  ...
```

These are placeholders. No real results are published yet; see [results/leaderboard.md](../results/leaderboard.md).
