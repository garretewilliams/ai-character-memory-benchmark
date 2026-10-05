# What Is AI Character Memory?

**AI character memory is the ability of an AI character to retain, retrieve, interpret, update, and appropriately use information from previous interactions in future conversations.**

An **AI character** is any conversational AI presented with a persistent identity: an AI companion, a roleplay character, a game NPC, a tutor persona, a branded assistant with a name and personality, or a character in an interactive story. What separates an AI character from a stateless assistant is that people return to it, and they expect it to know who they are and what has happened between them.

That expectation makes memory a character problem, not only a storage problem. The interesting question is not "is the fact in the database?" but "does this character behave like someone who shares this history?"

## The four kinds of things a character remembers

The benchmark groups remembered content into four types. They are not a theory of human memory; they are a practical partition of what AI characters need to carry forward.

### Identity memory

**Identity memory** is memory of stable facts about who someone is: the user's name, birthday, occupation, location (when appropriate), preferences and important personal facts, and equally the character's own identity, traits and history.

*Example:* "My name is Sarah. My favorite flower is lavender." Fifty turns and a new session later, the character still knows both. Tested by [IDENTITY-001](../benchmark/identity/IDENTITY-001.json).

### Episodic memory

**Episodic memory** is memory of events: what happened, when, who was involved, what was said, and what was promised. The term comes from cognitive psychology, where Endel Tulving distinguished memory for personally experienced events from general knowledge ([references](references.md#cognitive-science-of-memory)). Here it is used descriptively.

Good episodic tests do not only ask "what happened at the restaurant?". They make the episode *relevant* later and check whether the character brings it forward. Tested by [EPISODIC-001](../benchmark/episodic/EPISODIC-001.json) and [ADVERSARIAL-FALSE-MEMORY-001](../benchmark/adversarial/ADVERSARIAL-FALSE-MEMORY-001.json).

### Relationship memory

**Relationship memory** is memory of how a relationship has developed: shared experiences, trust, conflicts and reconciliations, inside jokes, promises, milestones, familiarity and boundaries. It is covered in depth in [Relationship Continuity](relationship-continuity.md).

### World and lore memory

**World or lore memory** is memory of a fictional setting: locations, characters and their relationships, rules (such as how magic works), factions, objects, world history, backstories and current story state. It makes the benchmark relevant to AI roleplay, NPCs, interactive fiction and game characters, not only companions. Tested by [LORE-001](../benchmark/world-lore/LORE-001.json).

## What a character does with memory

Remembering is half the job. The other half, and the part this benchmark emphasizes, is what the memory *does*:

* **Relevance:** choosing the memory that matters now. See [Memory Retrieval vs. Continuity](memory-vs-retrieval.md#relevance).
* **Context:** remembering what surrounded an event and why it mattered. See [Contextual Calibration](contextual-calibration.md#contextual-memory).
* **Behavioral continuity:** letting memory shape behavior without being asked. See [Memory Retrieval vs. Continuity](memory-vs-retrieval.md#behavioral-recall).
* **Consequences:** letting significant events have proportionate effects later. See [Consequence Memory](consequence-memory.md).

## How memory changes, and how characters change

Memory is not a write-once archive. Preferences change, facts get corrected, relationships move forward, and some things should never have been stored as permanent facts. See [Memory Updating](memory-updating.md). Characters also change, sometimes legitimately (development) and sometimes not (drift). See [Character Drift](character-drift.md).

## The process view

```text
EVENT → MEMORY → RELEVANCE → CONTEXT → INTERPRETATION → RESPONSE → BEHAVIOR → OUTCOME → MEMORY UPDATE → FUTURE INTERACTION
```

A failure at any step looks to the user like forgetting. A character that stored the fact but retrieved the wrong memory, or retrieved it without its context, or retrieved it and ignored it, has still "forgotten" from the user's point of view. This is why the benchmark measures behavior, not only recall.

## Why it matters

People form ongoing relationships with conversational agents. HCI research on long-term relational agents (for example Bickmore and Picard, 2005) treats relationship-maintaining behaviors, including continuity with past interactions, as part of what sustains engagement over weeks of use. Studies of companion chatbot users (for example Skjuve et al., 2021) describe relationships with chatbots that develop over time through repeated interaction ([references](references.md#human-computer-interaction-and-ai-companions)). For AI characters in particular, inconsistency is noticed. A character that forgets a promise, resets a hard-won relationship, or changes personality for no reason breaks the experience the person came for.

## The central thesis

> AI character memory is not simply the ability to retrieve the past. It is the ability to carry relevant history forward so that previous interactions meaningfully influence future understanding and behavior, while allowing the character and relationship to evolve over time.

The simplest version: **Does the past change the present?**

---

Related: [Memory vs. Context Window](memory-vs-context.md) · [Failure Modes](failure-modes.md) · [Glossary](glossary.md)
