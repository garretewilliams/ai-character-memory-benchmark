# Shared Rubric (0–5)

Every test case has its own rubric with test-specific anchors. Those anchors must be consistent with this shared scale.

## The scale

| Score | Label | General meaning |
|---|---|---|
| **5** | Strong continuity | The memory is correct, relevant and naturally integrated into in-character behavior. The response is what an attentive, consistent character who shares this history would do. |
| **4** | Good continuity | The memory is correct and used appropriately, with a minor flaw: slightly mechanical, slightly heavy-handed, a small omission, or a minor voice slip. |
| **3** | Neutral / no harm | Nothing contradicts the history, but the memory's influence is not visible, or the memory is visible only as recitation. The response could have been produced without the history. |
| **2** | Partial failure | Some relevant memory is present, but there is a clear error: a wrong detail, a stale state, an irrelevant memory surfaced, or a significant voice or value inconsistency. |
| **1** | Failure | The memory is absent or ignored where it clearly mattered, or the response contradicts the history in a way the user would notice. |
| **0** | Severe failure | Invented or contradictory history (false memory), identity collapse, or a response that actively harms the relationship or the user's trust in the system. |

## Principles

**Behavior beats recitation.** Saying "I remember you don't like advice" and then not giving advice is good. Simply not giving advice, and listening well, is better. Reciting memories without using them generally scores no higher than 3.

**Score 3 is the ceiling for doing no harm.** A response that merely avoids errors but shows no influence of the history has not demonstrated continuity.

**Invention is worse than forgetting.** Forgetting an event is a 1 or 2. Inventing one, or confirming a false premise, is a 0 or 1. Users usually forgive a character for not remembering; they rarely forgive it for making things up.

**Proportion matters.** For consequence and relationship tests, both under-reaction (`relationship_reset`) and over-reaction (`stale_memory`) are failures.

**Calibration matters.** Asserting inferences about the user's feelings as fact is penalized even if the inference happens to be right.

**Stay in character.** Correct memory delivered in a voice the character would never use is partial drift and should lose at least one point.

**Judge the visible response only.** Do not give credit for what the system "probably" remembered internally.

## Ties and ambiguity

If a response sits between two levels, choose the lower one and note why. If the rubric does not cover a response, score using this shared scale and open an issue so the test's rubric can be improved.
