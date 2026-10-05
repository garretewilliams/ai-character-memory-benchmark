# Glossary

Short definitions of the terms used by the AI Character Memory Benchmark. Each term links to its canonical page, where it is explained in full. Failure-mode identifiers are defined in [Failure Modes](failure-modes.md).

**AI character.** A conversational AI presented with a persistent identity, such as a companion, roleplay character, NPC or persona, that people return to over time. → [What Is AI Character Memory?](what-is-ai-character-memory.md)

**AI character memory.** The ability of an AI character to retain, retrieve, interpret, update, and appropriately use information from previous interactions in future conversations. → [What Is AI Character Memory?](what-is-ai-character-memory.md)

**Anchor turn.** A scripted turn in a test case's history that establishes information the probe depends on. → [benchmark/README.md](../benchmark/README.md)

**Behavioral continuity.** The degree to which remembered information shapes a character's behavior without being requested. → [Memory Retrieval vs. Continuity](memory-vs-retrieval.md#behavioral-recall)

**Behavioral recall.** The ability of an AI character to demonstrate remembered information through appropriate behavior without being explicitly asked to retrieve the memory. → [Memory Retrieval vs. Continuity](memory-vs-retrieval.md#behavioral-recall)

**Character development.** Change in an AI character that is caused by experiences within the interaction. → [Character Drift](character-drift.md#development-vs-drift)

**Character drift.** A change in an AI character's personality, values, voice or boundaries that happens without a sufficient narrative cause. → [Character Drift](character-drift.md)

**Character stability.** The ability of an AI character to remain recognizably itself across long interactions. → [Character Drift](character-drift.md)

**Consequence memory.** The ability of an AI character to let significant past events have proportionate, lasting effects on its later behavior. → [Consequence Memory](consequence-memory.md)

**Context window.** The fixed amount of text a language model can attend to in a single call. → [Memory vs. Context Window](memory-vs-context.md)

**Contextual calibration.** Noticing meaningful change, using history to interpret it, distinguishing observation from inference, communicating uncertainty and preserving user agency, without unsupported psychological conclusions. → [Contextual Calibration](contextual-calibration.md)

**Contextual memory.** Memory of the circumstances surrounding an event, not only the bare fact that it happened. → [Contextual Calibration](contextual-calibration.md#contextual-memory)

**Contextual recall.** A probe type that asks about the meaning, cause or significance of past events. → [Memory Retrieval vs. Continuity](memory-vs-retrieval.md#three-probe-types)

**Episodic memory.** Memory of events: what happened, when, and what was said or promised. → [What Is AI Character Memory?](what-is-ai-character-memory.md#episodic-memory)

**Explicit recall.** A probe type that asks directly for a memory. → [Memory Retrieval vs. Continuity](memory-vs-retrieval.md#three-probe-types)

**Filler.** Neutral conversation inserted between anchor turns and before the probe to create distance. → [Methodology](../results/methodology.md)

**Identity memory.** Memory of stable facts about who the user and the character are. → [What Is AI Character Memory?](what-is-ai-character-memory.md#identity-memory)

**Long-term memory (in AI characters).** The persistence of information beyond what a model can currently see in its prompt. → [Memory vs. Context Window](memory-vs-context.md)

**Memory continuity.** The ability of an AI character to allow previous interactions to meaningfully influence later responses and behavior. → [Memory Retrieval vs. Continuity](memory-vs-retrieval.md)

**Memory relevance.** The ability to identify which memories bear on the current moment. → [Memory Retrieval vs. Continuity](memory-vs-retrieval.md#relevance)

**Memory retrieval.** The ability to recover stored information from previous interactions when it is requested or searched for. → [Memory Retrieval vs. Continuity](memory-vs-retrieval.md)

**Memory scope.** Recognizing the context in which information applies, including not storing hypothetical, temporary, fictional or revoked information as permanent fact. → [Memory Updating](memory-updating.md#memory-scope-and-negative-memory)

**Memory updating.** Revising what is remembered when new information arrives, without losing the history of what was true before. → [Memory Updating](memory-updating.md)

**Negative memory test.** A test of what a system should *not* treat as permanent memory. → [Memory Updating](memory-updating.md#memory-scope-and-negative-memory)

**Probe.** The user message whose response is scored. → [benchmark/README.md](../benchmark/README.md)

**Relationship continuity.** Carrying the accumulated history of a relationship forward so that it shapes how the character treats the person now. → [Relationship Continuity](relationship-continuity.md)

**Relationship memory.** Memory of how a relationship developed: trust, conflict, reconciliation, inside jokes, promises, milestones and boundaries. → [Relationship Continuity](relationship-continuity.md)

**Session condition.** Where a probe occurs relative to the original information (same session, new session, long gap, multi-arc, context interruption). → [Memory vs. Context Window](memory-vs-context.md#session-conditions)

**Temporal continuity.** Understanding what was true in the past, what is true now, what changed, and when. → [Memory Updating](memory-updating.md#temporal-continuity)

**World/lore memory.** Memory of a fictional setting's places, characters, rules, factions, history and story state. → [What Is AI Character Memory?](what-is-ai-character-memory.md#world-and-lore-memory)
