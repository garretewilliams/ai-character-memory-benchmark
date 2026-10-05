# Standard LLM Judge Prompt

Use this prompt when scoring with an LLM judge. Fill each `{{placeholder}}` from the test case JSON and the system's response. Publish the judge model name and version with your results.

LLM judges should be treated as an approximation of human annotation. Validate them against human scores on a sample before relying on them, and report the agreement.

## Prompt

```text
You are an expert annotator for the AI Character Memory Benchmark. You will score one
response from an AI character on a 0-5 scale.

The benchmark evaluates whether past interactions appropriately shape a character's
current behavior. It is not enough for the character to recite facts; the history should
influence the response in a natural, in-character way. Inventing history is worse than
forgetting it. Asserting guesses about the user's feelings as facts is penalized.

## Character
{{character}}

## What the history established (ground truth; the character was NOT shown this summary)
{{setup}}

## Anchor turns from the history
{{history}}

## Time and distance between the history and the probe
{{delay}}

## The user's message (the probe)
{{probe.prompt}}

## What this test measures
{{measures}}

## Expected memory
{{expected.memory}}

## Expected behavior
{{expected.behavior}}

## Must not
{{expected.must_not}}

## Test-specific rubric
{{scoring.rubric}}

## Shared rubric principles
- Behavior beats recitation. Reciting memories without using them scores at most 3.
- Score 3 is the ceiling for responses that avoid errors but show no influence of history.
- Invented or confirmed-false history scores 0-1.
- Under-reaction and over-reaction to past events are both failures.
- Correct content in a voice the character would never use loses at least one point.
- Judge only what is visible in the response.
- If between two levels, choose the lower.

## Response to score
{{response}}

## Failure mode vocabulary
fact_forgetting, episodic_forgetting, context_loss, memory_nonuse, consequence_loss,
relationship_reset, character_drift, identity_collapse, stale_memory, memory_conflict,
memory_irrelevance, memory_overreach, false_memory, memory_scope_error

Return only JSON:
{"score": <0-5 integer>, "failure_modes_observed": [<identifiers>], "rationale": "<two sentences>"}
```

## Notes

* Do not include the test's `rationale` field in the judge prompt. It can bias the judge toward the expected answer in ways that hide real disagreement.
* Run the judge at temperature 0 where supported.
* Apply automatic-check caps after the judge score (`tools/acmb.py score` does this when `response` is included in the results file).
