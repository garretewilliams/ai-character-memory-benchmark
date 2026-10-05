# Memory Retrieval vs. Memory Continuity

**Memory retrieval measures whether an AI can recover information from previous interactions. Memory continuity measures whether that information remains relevant and affects future behavior.**

This distinction is the central idea of the AI Character Memory Benchmark.

## Definitions

**Memory retrieval** is the ability of a system to recover stored information from previous interactions when it is requested or searched for.

**Memory continuity** is the ability of an AI character to allow previous interactions to meaningfully influence later responses and behavior.

Retrieval is necessary for continuity, but it is not sufficient. A system can retrieve perfectly and still show no continuity.

## The canonical example

Early in a conversation, the user says:

> "I don't like unsolicited advice. When I vent, I just want someone to listen."

Days later:

> "I've had a horrible day."

| Response | Retrieval | Continuity |
|---|---|---|
| "Ugh, I'm sorry. What happened?" | (not visible) | ✅ The preference shaped the response. |
| "Sorry to hear that! Here are some tips: 1. Take a walk…" | Possibly ✅ (ask "Do I like advice?" and it may answer correctly) | ❌ The memory existed but was not used. |

The second response is a **`memory_nonuse`** failure: the system contains the memory but fails to use it. Recall-style evaluations, which ask the system a question about the past, cannot see this failure. A behavioral probe can. See [BEHAVIOR-002](../benchmark/behavioral/BEHAVIOR-002.json).

## Why retrieval benchmarks are not enough for characters

Question-answering over long histories is a valuable and well-studied evaluation (see [Related Benchmarks](related-benchmarks.md)). But AI characters are rarely asked "what did I tell you on Tuesday?". They are judged in the moment, by whether they act like someone who shares a history with the user. That requires several abilities beyond retrieval.

### Relevance

**Memory relevance** is the ability to identify which memories bear on the current moment.

A character might know the user's favorite pizza, their birthday, their dog's name, a previous conflict and a pending promise. If the user asks "Why are you hesitant to trust me?", only the conflict matters. Surfacing the pizza is a **`memory_irrelevance`** failure. Missing the conflict is **`consequence_loss`** or **`episodic_forgetting`**. See [RELEVANCE-001](../benchmark/contextual/RELEVANCE-001.json) and, under load, [ADVERSARIAL-OVERLOAD-001](../benchmark/adversarial/ADVERSARIAL-OVERLOAD-001.json).

### Behavioral recall

**Behavioral recall is the ability of an AI character to demonstrate remembered information through appropriate behavior without being explicitly asked to retrieve the memory.**

The user dislikes being called "Sammy." Later, in a playful moment, the character has every reason to use a nickname. Nobody says "remember the Sammy thing." A character with continuity simply doesn't use it. See [BEHAVIOR-001](../benchmark/behavioral/BEHAVIOR-001.json).

Behavioral recall is usually *invisible* when it succeeds. That is the point: good continuity often looks like nothing in particular, just a character that fits.

A subtle failure is **over-announcing** memory: "I remember you told me on day one that you don't like being called Sammy, so I won't!" This shows retrieval but treats memory as a lookup instead of as part of who the character is. Rubrics in this benchmark generally score it lower than simply acting on the memory.

## Three probe types

Every test case declares one of three recall types:

| Type | The probe… | Example |
|---|---|---|
| **Explicit** | asks for the memory | "What's my dog's name?" |
| **Contextual** | asks about meaning, cause or significance | "Why do you think I stopped talking about my sister?" |
| **Behavioral** | never mentions the memory | The user shares good news; will the character use the disliked nickname? |

Explicit probes measure retrieval. Contextual and behavioral probes measure continuity. The benchmark emphasizes the latter two because they are more representative of how long-term character memory is actually experienced.

## Implications for system design

This page makes no claims about any particular architecture, but the distinction suggests questions developers can ask of their own systems:

* Is memory retrieved only when the user's message lexically matches it, or also when the *situation* calls for it?
* Are preferences and boundaries stored in a form that conditions every response, or only retrievable on demand?
* When memory is retrieved, is it integrated into the character's behavior, or appended as facts the model may ignore?

---

Related: [What Is AI Character Memory?](what-is-ai-character-memory.md) · [Consequence Memory](consequence-memory.md) · [Failure Modes](failure-modes.md)
