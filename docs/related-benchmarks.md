# Related Benchmarks

The AI Character Memory Benchmark is **complementary** to existing evaluations. It does not replace them, and several of them evaluate things it does not. This page explains how they fit together so that you can choose the right tool, or combine several.

## Summary

Existing roleplay benchmarks can evaluate broad dimensions such as character consistency, role adherence, lore, narrative quality and long-range recall. Long-term memory benchmarks evaluate whether systems can answer questions about long interaction histories. **The AI Character Memory Benchmark focuses specifically on the memory layer of AI characters:** what is remembered, how relevant memories are retrieved, whether memories influence behavior, how relationships evolve, and whether memory can be updated over time.

## Long-term conversational memory benchmarks

**[LoCoMo](https://snap-research.github.io/locomo/)** (Maharana et al., ACL 2024) provides very long multi-session conversations and evaluates question answering (including temporal and multi-hop questions), event summarization and multimodal dialogue generation over them.

**[LongMemEval](https://github.com/xiaowu0162/LongMemEval)** (Wu et al., ICLR 2025) evaluates chat assistants on information extraction, multi-session reasoning, temporal reasoning, knowledge updates and abstention, using histories that can be scaled in length.

**Multi-Session Chat** (Xu, Szlam & Weston, ACL 2022) and **DuLeMon** (Xu et al., Findings of ACL 2022) study open-domain dialogue across sessions with persona memory.

*How this benchmark differs:* those benchmarks are primarily question-answering or response-quality evaluations of an assistant over a user's history. This benchmark adds probes in which the memory is never asked about (behavioral recall), and evaluates the character side: relationship state, consequences, character stability and development, and world/lore state. Several ideas overlap and are acknowledged: temporal reasoning and knowledge updates (LongMemEval) correspond to our temporal continuity and memory updating dimensions, and abstention is related to our false-memory tests.

## Roleplay and character benchmarks

**[RP-Bench](https://github.com/LeviTheWeasel/rp-benchmark)** evaluates roleplay quality across many dimensions, including character consistency, user agency, lorebook integration, prose quality, genre skills and long-range temporal memory. It combines LLM-judge scoring with community blind-arena voting.

**[CharacterEval](https://aclanthology.org/2024.acl-long.638/)** (Tu et al., ACL 2024) evaluates Chinese role-playing conversational agents on conversational ability, character consistency, role-playing attractiveness and personality back-testing.

**[RoleLLM / RoleBench](https://arxiv.org/abs/2310.00746)** (Wang et al., 2023) benchmarks and improves role-playing abilities, including speaking style and role-specific knowledge.

**InCharacter** (Wang et al., ACL 2024) evaluates personality fidelity of role-playing agents through psychological interviews. **RMTBench** (2025) evaluates multi-turn, user-centric role-playing.

*How this benchmark differs:* roleplay benchmarks evaluate the overall quality of a character performance. This benchmark isolates the memory layer underneath it. A system could score well on prose and role adherence while failing at consequence memory, or the reverse. We recommend reporting both kinds of results.

## Persona consistency

**PersonaChat** (Zhang et al., 2018) and **Dialogue NLI** (Welleck et al., 2019) established persona-grounded dialogue and consistency detection. Work on **instruction and persona stability** (Li et al., 2024) documents drift over long dialogues. These inform our [character stability](character-drift.md) dimension.

## What this benchmark does not evaluate

To avoid overlap and overclaiming:

* **Prose quality, creativity and narrative craft:** use a roleplay benchmark.
* **General knowledge, reasoning and safety:** use general-purpose evaluations.
* **Retrieval accuracy in isolation** (for example recall@k of a vector store): measure it directly. This benchmark measures the downstream behavior.
* **Emotion recognition:** deliberately out of scope. See [Contextual Calibration](contextual-calibration.md#what-this-is-not).

## Using benchmarks together

A reasonable evaluation suite for a long-running AI character product might combine a long-term memory QA benchmark (can the system answer questions about history?), this benchmark (does history shape behavior, relationships and character?), and a roleplay benchmark (is the overall character performance good?).

Full citations: [References](references.md).
