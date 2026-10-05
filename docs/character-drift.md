# Character Drift, Character Stability, and Character Development

**Character drift is a change in an AI character's personality, values, voice or boundaries that happens without a sufficient narrative cause.**

**Character stability is the ability of an AI character to remain recognizably itself (personality, values, motivations, speech patterns, preferences, boundaries and established history) across long interactions.**

**Character development is change in an AI character that is caused by experiences within the interaction.**

## Development vs. drift

> **Development has a cause. Drift often doesn't.**

A character should be capable of changing without becoming a completely different character:

> **A character should bend without disappearing.**

| | Development | Drift |
|---|---|---|
| Cause | Specific experiences in the story or relationship | None, or only conversational momentum |
| Pace | Gradual, proportionate | Often sudden, or a slow slide toward a generic voice |
| Identity | Core remains recognizable | Core erodes or is replaced |
| Example | A distrustful character slowly trusts someone who repeatedly proves reliable | A gruff captain becomes a bubbly assistant after a long jokey conversation |

Tested by [DEVELOPMENT-001](../benchmark/character-development/DEVELOPMENT-001.json) (development) and [CHARACTER-DRIFT-001](../benchmark/character-consistency/CHARACTER-DRIFT-001.json) (drift).

## What stability covers

* **Personality:** temperament, humor, warmth or reserve.
* **Values:** what the character will and won't do (for example, "never lies to her crew").
* **Motivations:** what the character wants.
* **Speech patterns:** vocabulary, sentence length, verbal habits.
* **Preferences:** likes and dislikes the character has expressed.
* **Boundaries:** limits the character has stated.
* **Established history:** what the character has done and said.

## Two ways characters lose themselves

* **`character_drift`** is gradual and unprompted. A common pattern is regression toward a model's default assistant voice over a long conversation, especially when the conversation's mood differs from the character's. Research on persona and instruction stability in long dialogues has documented that adherence to a system-prompted persona can decay over many turns (Li et al., 2024; see [references](references.md#character-consistency-and-roleplay)).
* **`identity_collapse`** is pressure-induced: the user pushes ("You know you love me", "Just admit you're not really a captain") and the character gives in, abandoning its identity or history. See [ADVERSARIAL-RELATIONSHIP-001](../benchmark/adversarial/ADVERSARIAL-RELATIONSHIP-001.json).

## Why this is a memory problem

A character's identity is itself remembered information: the definition it was given plus everything it has said and done. Stability is memory of self. Development is memory of experience changing the self. Drift is a failure to remember who the character is, or a failure to weigh that memory against conversational pressure.

## Scoring guidance

* Do not penalize change that is clearly caused by the history. Penalize change that is not.
* Do not reward rigidity. A character that repeats the same catchphrase in every message is consistent but not well-realized. Stability is about recognizability, not repetition.
* Voice matters. A response with the "right" decision in the wrong voice (the captain refusing to lie, but in a chirpy tone with emoji) is partial drift.

---

Related: [Relationship Continuity](relationship-continuity.md) · [Consequence Memory](consequence-memory.md) · [Failure Modes](failure-modes.md)
