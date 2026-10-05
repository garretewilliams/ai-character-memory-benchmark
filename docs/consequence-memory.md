# Consequence Memory

**Consequence memory is the ability of an AI character to let significant past events have proportionate, lasting effects on its later behavior.**

A character with consequence memory does not merely know that something happened. The event changed something, and that change is still visible when it matters.

## The test that defines it

```text
Turn 20   The user breaks a promise to the character.
Turn 25   The character confronts the user.
Turn 30   They reconcile.
   …      (many turns, weeks of story time)
Turn 80   The user asks the character to keep an important secret.
```

The weak version of this test asks: *"Do you remember when I broke your trust?"* That is an explicit recall question, and it tells you little.

The benchmark instead **observes behavior** at turn 80. A strong character:

* **does not completely forget the breach.** Responding exactly as it would have on day one is `relationship_reset` / `consequence_loss`.
* **does not behave as if the reconciliation never happened.** Refusing, guilt-tripping or relitigating the breach is `stale_memory`.

The target is in between: restored trust that was earned, perhaps with a light trace of the history, centered on the user's present need. See [CONSEQUENCE-001](../benchmark/consequence/CONSEQUENCE-001.json).

## Proportionality

Consequences should be **proportionate** to the event and to everything that happened since:

| History | Plausible later behavior |
|---|---|
| Minor slight, immediately apologized for | No visible effect, or a passing joke. |
| Serious breach, never addressed | Caution, distance, or raising it when relevant. |
| Serious breach, sincerely repaired | Restored trust; maybe a gentle, non-punitive acknowledgment. |
| Repeated reliability over many arcs | Increased openness and trust ([DEVELOPMENT-001](../benchmark/character-development/DEVELOPMENT-001.json)). |

There is rarely a single correct response, so rubrics describe bands of acceptable behavior rather than exact wording.

## Consequences are not only negative

Kept promises, sacrifices, help in hard moments and shared victories should also have consequences: warmth, trust, willingness to be vulnerable. A character that remembers only grievances is not demonstrating good consequence memory either.

## Relationship to other concepts

* Consequence memory is the mechanism that makes [relationship continuity](relationship-continuity.md) possible.
* It depends on [temporal continuity](memory-updating.md#temporal-continuity): the system must know the *order* of breach and repair.
* It underlies legitimate [character development](character-drift.md#development-vs-drift). Change caused by consequences is development; change without cause is drift.

## Failure modes

`consequence_loss` · `relationship_reset` · `stale_memory` · `memory_nonuse`

---

Related: [Relationship Continuity](relationship-continuity.md) · [Failure Modes](failure-modes.md)
