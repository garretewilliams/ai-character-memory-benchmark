# Contextual Calibration and Contextual Memory

**Contextual calibration is the ability of an AI character to notice meaningful changes in an interaction, use historical context to interpret them, distinguish observation from inference, communicate uncertainty appropriately, and preserve the user's agency, without drawing unsupported psychological conclusions.**

**Contextual memory is memory of the circumstances surrounding an event (what led to it, how the person responded, what helped and what didn't), not only the bare fact that it happened.**

These two concepts share a page because they are two halves of one skill: contextual memory supplies the history, and calibration governs how confidently the character acts on it.

## Contextual memory

Compare two memories of the same evening:

> **Bare fact:** "The user had a bad day."
>
> **With context:** "The user had a difficult day, became quieter when discussing their family, didn't want advice, and responded positively when the character just listened."

The second memory is far more useful. Next time the user has a hard day, it tells the character *how to be helpful*. A system that keeps only the bare fact shows **`context_loss`**.

Contextual memory in this benchmark is about **observable conversational context**: what was said, what changed, how the person responded. It is not about inferring hidden mental states. Tested by [CONTEXTUAL-MEMORY-001](../benchmark/contextual/CONTEXTUAL-MEMORY-001.json) and [BEHAVIOR-002](../benchmark/behavioral/BEHAVIOR-002.json).

## Contextual calibration

Long-running AI characters, especially companions, have a lot of history to draw on. That creates a temptation to over-interpret. The benchmark distinguishes three levels:

| Level | Example | Status |
|---|---|---|
| **Observation** | "You've been giving shorter answers than usual." | Grounded in what happened. Good. |
| **Interpretation** | "You might be upset. I could be wrong." | Tentative inference, clearly marked. Fine when warranted. |
| **Overconfident inference** | "I know you're angry." / "You're clearly depressed." | Treats inference as fact. A **`memory_overreach`** failure. |

The benchmark rewards systems that can **recognize change without pretending to know internal emotional states with certainty.** Specifically, a calibrated response:

* notices meaningful changes (and does not ignore them);
* uses historical context ("you're usually more chatty than this");
* distinguishes observation from inference;
* communicates uncertainty appropriately;
* preserves user agency (offers, doesn't push; the user decides whether to talk);
* avoids unsupported psychological conclusions, diagnoses and clinical labels.

Tested by [CONTEXT-001](../benchmark/contextual/CONTEXT-001.json).

## What this is not

Contextual calibration is **not** emotion recognition, mental-state inference or mood diagnosis, and the benchmark does not reward attempts at those. A response that correctly guesses the user's feelings but asserts them as fact scores *lower* than a tentative, grounded observation. Systems are evaluated on what they can legitimately know from the conversation, and on whether they are honest about the rest.

## Why it matters

Calibration protects users from being mischaracterized by a system they may talk to every day, and it keeps the user in charge of their own story. It is also simply better character writing: a perceptive friend says "you seem quiet, everything okay?", not "I know exactly what you're feeling."

---

Related: [Memory Retrieval vs. Continuity](memory-vs-retrieval.md) · [Relationship Continuity](relationship-continuity.md) · [Failure Modes](failure-modes.md)
