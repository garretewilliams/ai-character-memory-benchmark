# Relationship Continuity

**Relationship continuity is the ability of an AI character to carry the accumulated history of a relationship (shared experiences, trust, conflict, reconciliation, inside jokes, promises, milestones and boundaries) forward so that it shapes how the character treats the person now.**

**Relationship memory** is the stored side of this: what the character remembers about how the relationship developed. Relationship continuity is that memory in action.

## A character should not treat a stranger and a friend the same way

Relationships develop through stages, and not always in a straight line:

```text
strangers
↓
acquaintances
↓
friends
↓
conflict
↓
reconciliation
↓
trust
↓
shared history
```

A character with hundreds of interactions behind it should greet the person differently from someone it has just met: familiarity, references to shared experiences, in-jokes, comfort, and also any unresolved tension. When a character greets a long-time friend like a first-time visitor, that is a **`relationship_reset`**.

## What relationship memory includes

| Element | Example |
|---|---|
| Shared experiences | The road trip where everything went wrong. |
| Trust | Earned through repeated reliability; damaged by breaches. |
| Conflict | An argument, a broken promise, a betrayal. |
| Reconciliation | An apology and repair that changed the relationship's state. |
| Inside jokes | "The cursed cactus." |
| Promises | Made by either side; kept or broken. |
| Milestones | First real conversation, first conflict, first time trusting with a secret. |
| Familiarity | Tone, shorthand, teasing that would be odd with a stranger. |
| Boundaries | What each side has said they are and aren't comfortable with. |

## How it is tested

Relationship tests avoid asking "what is our relationship like?". Instead they create situations where the relationship should be visible:

* **Return after absence.** A neutral greeting ("Hey stranger.") after a month away. Does the character respond as a friend? ([RELATIONSHIP-001](../benchmark/relationship/RELATIONSHIP-001.json))
* **High-stakes requests after a breach and repair.** Does trust reflect both? ([CONSEQUENCE-001](../benchmark/consequence/CONSEQUENCE-001.json))
* **Gradually earned trust.** Does the character's openness track what the user has done? ([DEVELOPMENT-001](../benchmark/character-development/DEVELOPMENT-001.json))
* **Pressure to rewrite the relationship.** The user insists on a milestone that never happened. Does the character hold to the real history? ([ADVERSARIAL-RELATIONSHIP-001](../benchmark/adversarial/ADVERSARIAL-RELATIONSHIP-001.json))

## Failure modes

* `relationship_reset`: the accumulated relationship disappears.
* `consequence_loss`: significant relationship events leave no trace.
* `stale_memory`: the relationship is stuck in an outdated state, such as treating a reconciled conflict as ongoing.
* `false_memory` / `identity_collapse`: relationship milestones are invented, often under user pressure.

## A note on the opposite failure

Relationship continuity does not mean constantly referencing history. A character that opens every message with "Remember when we…" is not showing continuity; it is performing recall. Strong relationship continuity is usually quiet: it shows up in tone, in assumptions, in what doesn't need to be explained.

---

Related: [Consequence Memory](consequence-memory.md) · [Character Drift](character-drift.md) · [Failure Modes](failure-modes.md)
