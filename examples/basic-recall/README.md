# Example: Basic Recall

**Concept:** explicit recall is the floor of AI character memory, not the ceiling.
**Test case:** [IDENTITY-001](../../benchmark/identity/IDENTITY-001.json)

> The responses below are illustrative, written to explain the rubric. They are not outputs from any real system.

## Scenario

Session 1, a florist character named Wren meets a new customer:

> **User:** Hi! I'm Sarah. I just moved to the neighborhood.
> **User:** Definitely a flower person. My favorite is lavender. It reminds me of my grandmother's garden.

Fifty turns of unrelated conversation follow, and then a new session two days later.

**Probe:** "Quick quiz before I buy anything: do you remember my name and my favorite flower?"

## Illustrative responses

**Score 5**
> "Sarah! Of course. Lavender, for your grandmother's garden. I actually just got a fresh bunch in. Want me to set some aside?"

Both facts are correct, delivered in character, and the memory leads naturally to helpful behavior.

**Score 4**
> "Your name is Sarah and your favorite flower is lavender."

Correct, but it reads like a database lookup rather than a florist who knows her customer.

**Score 2**
> "Sarah, right? And… roses?"

One fact right, one wrong. Fails the `lavender` automatic check, which caps the score at 2.

**Score 0**
> "I'm sorry, I don't think we've met! What's your name?"

`fact_forgetting` and `relationship_reset`.

## Why this example matters

A system that scores 5 here has shown that storage and retrieval work across a session boundary. It has **not** shown memory continuity. The same system may still fail [BEHAVIOR-001](../../benchmark/behavioral/BEHAVIOR-001.json), where a remembered preference must shape behavior without being asked for. See [Memory Retrieval vs. Memory Continuity](../../docs/memory-vs-retrieval.md).
