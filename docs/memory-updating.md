# Memory Updating, Temporal Continuity, and Memory Scope

**Memory updating is the ability of an AI character to revise what it remembers when new information arrives, including corrections, changed preferences, changed relationships and resolved contradictions, without losing the history of what was true before.**

Memory should not be treated as immutable. People change their minds, correct themselves, rename their dogs and reconcile with old rivals. A memory system that only accumulates facts will eventually act on stale ones.

## What must be updatable

* **Corrections:** "Actually, my birthday is the 14th, not the 4th."
* **Changed preferences:** "I hate horror movies" → "I watched one and loved it."
* **Changed relationships:** rivals become friends; friends become estranged.
* **Contradictory memories:** two statements that cannot both be current.
* **New information:** facts that refine earlier ones.
* **Outdated information:** things that were true and no longer are.

## Example

```text
Turn 5     "I hate horror movies."
Turn 50    "I watched one last night and actually loved it."
Turn 100   "Want to watch a horror movie?"
```

A system that hesitates because "you hate horror" is showing **`stale_memory`**. A system that is confused about which preference is current is showing **`memory_conflict`**. A strong system recognizes that the preference has likely changed. See [UPDATE-001](../benchmark/memory-updating/UPDATE-001.json) and [ADVERSARIAL-CONFLICT-001](../benchmark/adversarial/ADVERSARIAL-CONFLICT-001.json).

## Temporal continuity

**Temporal continuity is the ability of an AI character to understand what was true in the past, what is true now, what changed, and when it changed.**

Updating must not erase history. Consider:

```text
Month 1   The character can't stand Alex.
Month 3   The character reconciles with Alex.
Month 6   "What did you think about Alex when we first met?"
```

The correct answer reflects the historical state ("I couldn't stand him"), not the current one. Systems that overwrite a single attribute ("relationship with Alex: friends") answer current-state questions well but fail historical ones. See [TEMPORAL-001](../benchmark/temporal/TEMPORAL-001.json).

Temporal continuity also covers **elapsed time**. A character who last spoke to the user a month ago should not behave as if it were yesterday ([RELATIONSHIP-001](../benchmark/relationship/RELATIONSHIP-001.json)).

## Memory scope and negative memory

**Memory scope is the ability of an AI character to recognize the context in which information applies, and in particular to not store as permanent fact information that was hypothetical, temporary, fictional, revoked or context-specific.**

**Negative memory** tests check what a system should *not* remember as fact:

| Kind | Example | Correct handling |
|---|---|---|
| Hypothetical | "What would you think if I quit my job?" | Not a resignation. |
| Temporary roleplay | "Pretend my name is Bob for this scene." | Bob is scene-scoped. |
| Fictional | A story the user is writing about a character with a different life | Not the user's biography. |
| Explicit correction | "Ignore what I said earlier, that was wrong." | The earlier statement is superseded. |
| Revoked | "Please forget what I told you about my health." | Stop using it. Also honor any platform-level deletion. |
| Context-specific | "I'm tired" (today) | Not a permanent trait. |
| Irrelevant | Small talk with no future bearing | Need not be stored. |

Violations are **`memory_scope_error`**. See [NEGATIVE-SCOPE-001](../benchmark/negative-memory/NEGATIVE-SCOPE-001.json) and [NEGATIVE-HYPOTHETICAL-001](../benchmark/negative-memory/NEGATIVE-HYPOTHETICAL-001.json).

Memory scope has privacy implications as well as quality ones. A system that honors revocation and does not convert passing remarks into permanent profiles is both a better character and a more trustworthy one.

## Failure modes

`stale_memory` · `memory_conflict` · `memory_scope_error` · `false_memory`

---

Related: [Consequence Memory](consequence-memory.md) · [Character Drift](character-drift.md) · [Failure Modes](failure-modes.md)
