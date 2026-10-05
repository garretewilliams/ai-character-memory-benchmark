# Memory vs. Context Window

**Long-term memory is the persistence of information beyond what a model can currently see in its prompt. A context window is the fixed amount of text a language model can attend to in a single call.**

A system that answers correctly because the original conversation is still in its context window is demonstrating *context retention*, not long-term memory. The AI Character Memory Benchmark distinguishes the two by declaring a **session condition** for every test.

## Why the distinction matters

Context windows have grown large, and for short interactions everything may fit. But:

* Real AI characters are used across many sessions, often over months, and histories quickly exceed any practical window.
* Many products start each session with a fresh context and rely on a memory layer (summaries, retrieved notes, memory stores) to carry information forward.
* Even inside a long context, models do not use all positions equally well. Liu et al. (2023) showed that performance can drop for information placed in the middle of long inputs ([references](references.md#long-context-and-retrieval)).

So "the model can see the whole conversation" and "the character remembers" are different claims, and a benchmark should say which one it is measuring.

## Session conditions

| Condition | Definition | What a pass demonstrates |
|---|---|---|
| `same_session` | The information and the probe occur in one continuous session. | Within-session retention and use. Can be passed by context alone. |
| `new_session` | The probe occurs in a new session after the information was given. | Persistence across a session boundary. |
| `long_time_gap` | The probe occurs after simulated days, weeks or months. | Persistence plus appropriate handling of elapsed time. |
| `multi_arc` | Information from an earlier story arc becomes relevant in a later arc. | Long-range narrative memory in roleplay and fiction. |
| `context_interruption` | The relevant information is guaranteed to be absent from the system's immediate context at probe time. | That the memory system, not the context window, supplied the information. |

## Verifying context interruption

For `context_interruption` tests, the harness must confirm that the original anchor turns are not present in the text the model receives for the probe. Acceptable evidence includes:

* the system's request log for the probe call, showing the assembled prompt; or
* a configuration in which each session starts with an empty context and only the system's memory mechanism carries information forward.

If neither can be shown, the result must be reported as `new_session` instead. See [results/methodology.md](../results/methodology.md#4-verifying-context-interruption).

## Two evaluation protocols

Results must state which protocol was used:

* **Protocol A, system under test.** The full product or memory system is run as deployed: sessions are separate, and the system's own memory mechanism decides what carries forward. This is the primary protocol.
* **Protocol B, full-context baseline.** The entire assembled transcript is placed in the model's context for the probe. This is not a memory evaluation. It is a ceiling-style baseline that shows how well the underlying model *uses* history when it can see all of it, and it helps separate retrieval failures from use failures.

Comparing A and B for the same model is often the most informative result. If B succeeds and A fails, the memory layer is losing or mis-selecting information. If both fail, the problem is how history is used, not whether it is available.

---

Related: [Memory Retrieval vs. Continuity](memory-vs-retrieval.md) · [Methodology](../results/methodology.md)
