# Scoring

The AI Character Memory Benchmark reports a **multidimensional profile**, not a single score. Memory is not one ability. A system can be excellent at fact recall and poor at consequence memory, and a single number would hide exactly the information a developer needs.

## How scoring works

1. **Each test case is scored 0–5** against its own rubric, which is anchored to the [shared rubric](rubric.md).
2. **Automatic checks** (where a test defines them) can **cap** a score, for example capping at 1 if a disliked nickname appears. They never raise a score.
3. **Failure modes** observed in the response are recorded using the [standard taxonomy](../docs/failure-modes.md) ([annotation guide](failure-modes.md)).
4. **Dimension scores** are the mean test score within each dimension, rescaled to 0–100. See [metrics](metrics.md).
5. **Results are published as a profile**, with the number of tests per dimension, the protocol used, and how scoring was done (human, LLM judge, or both).

## Who scores

Scores may come from human annotators, an LLM judge, or both. Every published result must say which. If an LLM judge is used:

* use the [standard judge prompt](judge-prompt.md), or publish the prompt you used;
* name the judge model and version;
* report agreement with human annotation on a sample when possible.

LLM judges are known to diverge from human judgments in some settings (see [references](../docs/references.md#evaluation-methodology)). Human scores take precedence where both exist.

## Files

* [rubric.md](rubric.md): the shared 0–5 scale and general principles.
* [metrics.md](metrics.md): how test scores become dimension scores and the profile.
* [failure-modes.md](failure-modes.md): how to annotate and report failure modes.
* [judge-prompt.md](judge-prompt.md): standard LLM-judge prompt.

To compute a profile from scored results: `python tools/acmb.py score results.jsonl --system "name"`.
