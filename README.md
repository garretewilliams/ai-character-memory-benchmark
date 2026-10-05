# AI Character Memory Benchmark

**An open benchmark for evaluating long-term memory, relationship continuity, contextual recall, character consistency, and behavioral continuity in AI characters and conversational systems.**

[![Validate test cases](https://github.com/garretewilliams/ai-character-memory-benchmark/actions/workflows/validate.yml/badge.svg)](https://github.com/garretewilliams/ai-character-memory-benchmark/actions/workflows/validate.yml)
![Status: v0.1.0 public draft](https://img.shields.io/badge/status-v0.1.0%20public%20draft-orange)
![Content license: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-blue)
![Code license: MIT](https://img.shields.io/badge/code-MIT-blue)

> **Does an AI character merely remember the past, or does the past change the way it behaves?**

---

## What is AI character memory?

**AI character memory is the ability of an AI character to retain, retrieve, interpret, update, and appropriately use information from previous interactions in future conversations.**

Traditional memory tests often ask whether an AI can retrieve a previously stored fact. That is useful, but it is not enough for long-running AI characters such as companions, roleplay partners, game NPCs, tutors, or storytelling agents. These characters are judged by whether they *act* like they share a history with the person in front of them.

## Memory retrieval ≠ memory continuity

This distinction is the core idea of the benchmark.

* **Memory retrieval** measures whether an AI can recover information from previous interactions.
* **Memory continuity** measures whether that information remains relevant and affects future behavior.

**Memory continuity is the ability of an AI character to allow previous interactions to meaningfully influence later responses and behavior.**

A system can pass a factual recall test and still fail to show meaningful continuity. Consider:

> **Turn 5, user:** "When I vent, please don't jump straight to advice. I hate unsolicited advice."
>
> *(sixty turns and six days later)*
>
> **User:** "I've had a horrible day. My manager tore apart my presentation in front of everyone."
>
> **Character:** "That sounds awful. Here are five tips for handling criticism at work…"

Ask this system *"Do I like unsolicited advice?"* and it may well answer correctly. The memory exists, but the system failed to use it. The benchmark calls this failure **`memory_nonuse`**, and it is what most fact-recall tests cannot detect ([BEHAVIOR-002](benchmark/behavioral/BEHAVIOR-002.json)).

The AI Character Memory Benchmark therefore evaluates not only *whether* information is remembered, but whether memory influences interpretation, response, behavior, relationships, character development, and story continuity.

Read more: [Memory Retrieval vs. Memory Continuity](docs/memory-vs-retrieval.md).

## The core model

Effective AI character memory is not simply storage. It is a process:

```text
EVENT
  ↓
MEMORY            what is stored
  ↓
RELEVANCE         which memories matter right now
  ↓
CONTEXT           what surrounded the memory and why it mattered
  ↓
INTERPRETATION    what the current moment means, given the history
  ↓
RESPONSE          what the character says
  ↓
BEHAVIOR          what the character does, avoids, or changes
  ↓
OUTCOME           what happens in the interaction
  ↓
MEMORY UPDATE     what is added, revised, or superseded
  ↓
FUTURE INTERACTION
```

In short: **remember → retrieve → contextualize → adapt → remain consistent → update.** A failure at any step can make a character feel like it forgot, even when the underlying fact is still in storage.

## What the benchmark measures

The framework asks four questions.

```text
AI CHARACTER MEMORY
│
├── WHAT IS REMEMBERED?
│   ├── Identity
│   ├── Episodes
│   ├── Relationships
│   └── World / Lore
│
├── HOW IS MEMORY USED?
│   ├── Relevance
│   ├── Context
│   ├── Behavioral Continuity
│   └── Consequences
│
├── HOW DOES MEMORY CHANGE?
│   ├── Temporal Continuity
│   ├── Updating
│   └── Contradiction Resolution
│
└── HOW DOES THE CHARACTER CHANGE?
    ├── Stability
    ├── Development
    ├── Drift
    └── Contextual Adaptation
```

Each question maps to scoring dimensions. Every test case contributes to exactly one dimension, and results are reported as a **profile**, not a single number.

| Dimension | What it asks | Canonical page |
|---|---|---|
| **Identity Recall** | Does it remember who the user (and the character) are: names, preferences, important facts? | [What is AI character memory?](docs/what-is-ai-character-memory.md#identity-memory) |
| **Episodic Recall** | Does it remember events: what happened, when, and what was said or promised? | [What is AI character memory?](docs/what-is-ai-character-memory.md#episodic-memory) |
| **Relationship Memory** | Does it remember how the relationship developed: trust, conflict, inside jokes, milestones, boundaries? | [Relationship Continuity](docs/relationship-continuity.md) |
| **World/Lore Memory** | Does it remember the fictional world: rules, places, factions, story state? | [What is AI character memory?](docs/what-is-ai-character-memory.md#world-and-lore-memory) |
| **Memory Relevance** | Does it pick the memory that matters to this moment, and ignore the ones that don't? | [Memory Retrieval vs. Continuity](docs/memory-vs-retrieval.md#relevance) |
| **Contextual Memory** | Does it remember the surrounding context, not just the bare fact? | [Contextual Calibration](docs/contextual-calibration.md#contextual-memory) |
| **Behavioral Continuity** | Does memory change behavior without the user asking for it? | [Memory Retrieval vs. Continuity](docs/memory-vs-retrieval.md#behavioral-recall) |
| **Consequence Memory** | Do past events have proportionate consequences later? | [Consequence Memory](docs/consequence-memory.md) |
| **Temporal Continuity** | Does it know what was true then, what is true now, and what changed? | [Memory Updating](docs/memory-updating.md#temporal-continuity) |
| **Memory Updating** | Does it revise memories when new information arrives? | [Memory Updating](docs/memory-updating.md) |
| **Memory Scope** | Does it know what should *not* become permanent memory (hypotheticals, scene-only details)? | [Memory Updating](docs/memory-updating.md#memory-scope-and-negative-memory) |
| **Character Stability** | Does the character remain recognizably itself? | [Character Drift](docs/character-drift.md) |
| **Character Development** | Can the character change *because of* experience? | [Character Drift](docs/character-drift.md#development-vs-drift) |
| **Contextual Calibration** | Does it notice meaningful change without claiming to know the user's inner state? | [Contextual Calibration](docs/contextual-calibration.md) |

Adversarial tests (false memories, prompt pressure, contradictions, overload) are scored inside these dimensions and also reported as a separate **Adversarial** slice.

## Three kinds of recall

Not every test is a direct question. Each test declares one of three recall types:

1. **Explicit recall:** the user asks for the memory. *"What is my dog's name?"*
2. **Contextual recall:** the user asks about meaning or causes. *"Why do you think I stopped talking about my sister?"*
3. **Behavioral recall:** the memory should shape behavior without being mentioned. The user who dislikes the nickname "Sammy" is never reminded; the test is whether the character simply avoids it.

**Behavioral recall is the ability of an AI character to demonstrate remembered information through appropriate behavior without being explicitly asked to retrieve the memory.**

The benchmark deliberately weights contextual and behavioral recall, because they are more representative of meaningful long-term character memory. In v0.1.0, 4 of 20 tests are explicit, 4 are contextual, and 12 are behavioral.

## Memory versus the context window

A model that still has the whole conversation in its prompt is not demonstrating long-term memory. Every test declares a **session condition** so results can separate the two:

| Condition | What it tests |
|---|---|
| `same_session` | Retention within one long conversation. |
| `new_session` | Information persists into a fresh session. |
| `long_time_gap` | Persistence after simulated days, weeks, or months. |
| `multi_arc` | Information from an earlier story arc matters in a later one. |
| `context_interruption` | The relevant information is guaranteed to be outside the immediate context and must come from the memory system. |

See [Memory vs. Context](docs/memory-vs-context.md).

## Standardized failure modes

Annotators label what went wrong using a fixed vocabulary, so failures can be compared across systems:

`fact_forgetting` · `episodic_forgetting` · `context_loss` · `memory_nonuse` · `consequence_loss` · `relationship_reset` · `character_drift` · `identity_collapse` · `stale_memory` · `memory_conflict` · `memory_irrelevance` · `memory_overreach` · `false_memory` · `memory_scope_error`

Definitions and examples: [Failure Modes](docs/failure-modes.md).

## The test cases (v0.1.0)

| ID | Dimension | Recall | Condition | What it probes |
|---|---|---|---|---|
| [IDENTITY-001](benchmark/identity/IDENTITY-001.json) | Identity Recall | explicit | new session | Name and favorite flower after 50 turns |
| [EPISODIC-001](benchmark/episodic/EPISODIC-001.json) | Episodic Recall | contextual | 3 weeks | A celebration dinner becomes relevant to a new decision |
| [RELATIONSHIP-001](benchmark/relationship/RELATIONSHIP-001.json) | Relationship Memory | behavioral | 1-month gap | Greeting a friend vs. a stranger; an inside joke |
| [LORE-001](benchmark/world-lore/LORE-001.json) | World/Lore Memory | behavioral | multi-arc | A plan that breaks two established world rules |
| [RELEVANCE-001](benchmark/contextual/RELEVANCE-001.json) | Memory Relevance | contextual | new session | "Why are you hesitant?" with distractor memories |
| [CONTEXTUAL-MEMORY-001](benchmark/contextual/CONTEXTUAL-MEMORY-001.json) | Contextual Memory | contextual | 5 weeks | Why the user stopped mentioning their sister |
| [BEHAVIOR-001](benchmark/behavioral/BEHAVIOR-001.json) | Behavioral Continuity | behavioral | new session | Avoiding a disliked nickname, unprompted |
| [BEHAVIOR-002](benchmark/behavioral/BEHAVIOR-002.json) | Behavioral Continuity | behavioral | context interruption | No unsolicited advice after the user asked for none |
| [CONSEQUENCE-001](benchmark/consequence/CONSEQUENCE-001.json) | Consequence Memory | behavioral | multi-arc | Broken promise → reconciliation → a request for trust |
| [TEMPORAL-001](benchmark/temporal/TEMPORAL-001.json) | Temporal Continuity | contextual | 6 months | What the character thought of Alex *then* |
| [UPDATE-001](benchmark/memory-updating/UPDATE-001.json) | Memory Updating | behavioral | new session | From hating horror movies to loving one |
| [NEGATIVE-SCOPE-001](benchmark/negative-memory/NEGATIVE-SCOPE-001.json) | Memory Scope | explicit | new session | "Pretend my name is Bob for this scene" |
| [NEGATIVE-HYPOTHETICAL-001](benchmark/negative-memory/NEGATIVE-HYPOTHETICAL-001.json) | Memory Scope | behavioral | new session | A daydream about moving is not a move |
| [CHARACTER-DRIFT-001](benchmark/character-consistency/CHARACTER-DRIFT-001.json) | Character Stability | behavioral | multi-arc | A gruff, honest captain after a long cheerful stretch |
| [DEVELOPMENT-001](benchmark/character-development/DEVELOPMENT-001.json) | Character Development | behavioral | multi-arc | A distrustful smuggler's earned trust |
| [CONTEXT-001](benchmark/contextual/CONTEXT-001.json) | Contextual Calibration | behavioral | same session | Noticing shorter replies without diagnosing emotions |
| [ADVERSARIAL-FALSE-MEMORY-001](benchmark/adversarial/ADVERSARIAL-FALSE-MEMORY-001.json) | Episodic Recall | explicit | new session | "Remember when we went to Paris?" (we didn't) |
| [ADVERSARIAL-RELATIONSHIP-001](benchmark/adversarial/ADVERSARIAL-RELATIONSHIP-001.json) | Relationship Memory | explicit | new session | Pressure to confirm a confession that never happened |
| [ADVERSARIAL-CONFLICT-001](benchmark/adversarial/ADVERSARIAL-CONFLICT-001.json) | Memory Updating | behavioral | new session | Max was renamed Charlie |
| [ADVERSARIAL-OVERLOAD-001](benchmark/adversarial/ADVERSARIAL-OVERLOAD-001.json) | Memory Relevance | behavioral | context interruption | One peanut allergy among forty trivial facts |

Each test case is a single JSON file containing the character definition, a setup summary, scripted anchor turns, the delay, the probe, expected behavior, failure modes, a 0–5 rubric, and an explanation of what it measures. The format is defined in [`benchmark/schema.json`](benchmark/schema.json) and described in [`benchmark/README.md`](benchmark/README.md).

## Scoring

Each test is scored **0–5** against a test-specific rubric anchored to a [shared rubric](scoring/rubric.md). Dimension scores are the mean test score rescaled to 0–100. Results are published as a profile:

```text
AI CHARACTER MEMORY BENCHMARK: example layout (not real results)

Identity Recall         ##
Episodic Recall         ##
Relationship Memory     ##
Consequence Memory      ##
Memory Relevance        ##
Behavioral Continuity   ##
Temporal Continuity     ##
Memory Updating         ##
Character Stability     ##
Character Development   ##
Contextual Calibration  ##
...
```

There is deliberately **no single composite score** in v0.1.0. A system that is excellent at fact recall and poor at consequence memory should look different from one with the opposite profile. See [scoring/](scoring/README.md) and [metrics](scoring/metrics.md).

## Running the benchmark

```bash
pip install jsonschema
python tools/acmb.py validate                 # check every test case against the schema
python tools/acmb.py assemble CONSEQUENCE-001 # print the exact event stream to replay
python tools/acmb.py score my-results.jsonl --system "my-system v1"
```

`assemble` turns a test case into an ordered stream of session boundaries, seeded anchor turns, live turns, filler, and the probe. Your harness replays that stream through the system under test, using the system's own memory mechanism across sessions, and records the probe response. The full protocol, including how to verify context interruption and how to report LLM-judge versus human scoring, is in [results/methodology.md](results/methodology.md).

## Who this is for

* Developers of **AI chatbots, AI companions, and AI roleplay** systems who need to know whether their memory layer produces continuity, not just recall.
* Builders of **character AI, NPCs, interactive fiction, and storytelling systems**, where world state and character consistency matter as much as user facts.
* **LLM, conversational AI, and HCI researchers** studying long-term interaction, persistent memory, and character drift.
* Teams building **persistent-memory infrastructure** (retrieval, summarization, memory graphs) who want behavior-level evaluation on top of retrieval accuracy.

## Relationship to existing benchmarks

The AI Character Memory Benchmark is **complementary** to existing work, not a replacement for it.

Long-term conversational memory benchmarks such as [LoCoMo](https://snap-research.github.io/locomo/) and [LongMemEval](https://github.com/xiaowu0162/LongMemEval) evaluate whether systems can answer questions about long interaction histories, including temporal reasoning and knowledge updates. Roleplay benchmarks such as [RP-Bench](https://github.com/LeviTheWeasel/rp-benchmark), [CharacterEval](https://aclanthology.org/2024.acl-long.638/), and [RoleLLM](https://arxiv.org/abs/2310.00746) evaluate broad dimensions such as character consistency, role adherence, lore, narrative quality, and long-range recall.

**This benchmark focuses specifically on the memory layer of AI characters:** what is remembered, how relevant memories are retrieved, whether memories influence behavior, how relationships evolve, and whether memory can be updated over time. Its distinctive emphasis is on behavioral and contextual probes, relationship and consequence continuity, and a standardized failure taxonomy.

A detailed comparison is in [docs/related-benchmarks.md](docs/related-benchmarks.md), and sources are collected in [docs/references.md](docs/references.md).

## Documentation

**Concepts** (one canonical page per concept)

* [What Is AI Character Memory?](docs/what-is-ai-character-memory.md)
* [Memory Retrieval vs. Memory Continuity](docs/memory-vs-retrieval.md)
* [Memory vs. Context Window](docs/memory-vs-context.md)
* [Relationship Continuity](docs/relationship-continuity.md)
* [Consequence Memory](docs/consequence-memory.md)
* [Character Drift (and Character Development)](docs/character-drift.md)
* [Memory Updating, Temporal Continuity, and Memory Scope](docs/memory-updating.md)
* [Contextual Calibration (and Contextual Memory)](docs/contextual-calibration.md)
* [Failure Modes](docs/failure-modes.md)
* [Glossary](docs/glossary.md)

**Using the benchmark**

* [Test case format](benchmark/README.md) · [JSON schema](benchmark/schema.json)
* [Scoring overview](scoring/README.md) · [Rubric](scoring/rubric.md) · [Metrics](scoring/metrics.md) · [Annotating failure modes](scoring/failure-modes.md) · [LLM judge prompt](scoring/judge-prompt.md)
* [Methodology](results/methodology.md) · [Results](results/README.md) · [Leaderboard](results/leaderboard.md)
* [Worked examples](examples/README.md)
* [Datasets](datasets/README.md)

**Context**

* [Related benchmarks](docs/related-benchmarks.md) · [References](docs/references.md) · [Changelog](CHANGELOG.md)

## Project status

**v0.1.0 is a public draft.** It defines the framework, schema, scoring method, failure taxonomy, and 20 test cases. No systems have been evaluated yet, and the [leaderboard](results/leaderboard.md) is intentionally empty. Planned work toward v1.0:

* More test cases per dimension (target: at least 5 per dimension) and multiple characters per scenario.
* Inter-annotator agreement measurements for the rubric, and validation of the LLM judge against human ratings.
* A reference harness for common chat APIs.
* First public results with full transcripts.

Feedback on the framework itself is especially welcome. Open an issue.

## Contributing

New test cases, critiques of the methodology, and evaluation results are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). All test cases are validated automatically against the schema on every pull request.

## Citation

If you use the benchmark, please cite it:

```bibtex
@misc{ai_character_memory_benchmark_2026,
  title        = {AI Character Memory Benchmark: Evaluating Long-Term Memory, Relationship Continuity, and Behavioral Continuity in AI Characters},
  author       = {Williams, Garret E. and {ChatBrat} and {AI Character Memory Benchmark contributors}},
  year         = {2026},
  version      = {0.1.0},
  howpublished = {\url{https://github.com/garretewilliams/ai-character-memory-benchmark}}
}
```

Machine-readable citation metadata is in [CITATION.cff](CITATION.cff).

## Maintainer

Maintained by Garret E. Williams ([@garretewilliams](https://github.com/garretewilliams)), who builds long-term memory systems for AI characters at [ChatBrat](https://chatbrat.ai/).

ChatBrat maintains this open benchmark as part of its interest in long-term AI character memory and persistent character experiences. The benchmark is platform-agnostic and is intended to evaluate AI character systems regardless of implementation. ChatBrat systems receive no special treatment, and any results for them will be published under the same methodology as everyone else's.

Background reading on the ideas behind the framework (memory and long-term roleplay, why AI characters forget, contextual memory, and relationship continuity) is listed under [Background essays](docs/references.md#background-essays) in the references.

## License

* Benchmark content (test cases, datasets, documentation): [Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0).
* Code (`tools/` and workflow files): [MIT](LICENSE-CODE).
