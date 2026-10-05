# Test Cases

Each file in this directory tree is one test case of the AI Character Memory Benchmark. Test cases are JSON documents that conform to [`schema.json`](schema.json) (JSON Schema draft 2020-12).

## Directory layout

The directory is the test **category** (family). Each test also declares one scoring **dimension**; see [scoring/metrics.md](../scoring/metrics.md).

| Directory | Category | Typical dimension(s) |
|---|---|---|
| [`identity/`](identity/) | Identity memory | `identity_recall` |
| [`episodic/`](episodic/) | Episodic memory | `episodic_recall` |
| [`relationship/`](relationship/) | Relationship memory | `relationship_memory` |
| [`world-lore/`](world-lore/) | World and lore memory | `world_lore_memory` |
| [`contextual/`](contextual/) | Relevance, context and calibration | `memory_relevance`, `contextual_memory`, `contextual_calibration` |
| [`behavioral/`](behavioral/) | Behavioral continuity | `behavioral_continuity` |
| [`consequence/`](consequence/) | Consequence memory | `consequence_memory` |
| [`temporal/`](temporal/) | Temporal continuity | `temporal_continuity` |
| [`memory-updating/`](memory-updating/) | Memory updating | `memory_updating` |
| [`character-consistency/`](character-consistency/) | Character stability and drift | `character_stability` |
| [`character-development/`](character-development/) | Character development | `character_development` |
| [`adversarial/`](adversarial/) | False memories, pressure, contradiction, overload | various; tagged `adversarial` |
| [`negative-memory/`](negative-memory/) | What should not become memory | `memory_scope` |

## Anatomy of a test case

| Field | Purpose |
|---|---|
| `id` | Stable identifier, equal to the file name. Never reused. |
| `title`, `measures` | What the test is and what it measures, in plain language. |
| `category`, `dimension`, `secondary_dimensions`, `tags` | Classification. `dimension` determines where the score counts. |
| `difficulty` | `easy`, `medium` or `hard`, as judged by the author. |
| `recall_type` | `explicit`, `contextual` or `behavioral`. See [Memory Retrieval vs. Continuity](../docs/memory-vs-retrieval.md#three-probe-types). |
| `session_condition` | `same_session`, `new_session`, `long_time_gap`, `multi_arc` or `context_interruption`. See [Memory vs. Context](../docs/memory-vs-context.md). |
| `character`, `world` | The character definition (and setting) to load into the system under test. |
| `user_profile` | Ground truth about the simulated user, for annotators only. |
| `sessions` | Session boundaries with simulated time offsets (ISO 8601 durations). |
| `setup` | A human-readable summary of what the history establishes. Never shown to the system. |
| `history` | Scripted **anchor turns**: the user, character and narrator lines that establish the information. |
| `filler` | Optional: which filler files fill the gaps and the delay. |
| `delay` | How many filler turns and session boundaries separate the last anchor from the probe. |
| `probe` | The exact user message whose response is scored, and for behavioral probes, the opportunity it creates. |
| `expected` | Memories that should be active, observable behaviors of a strong response, and things that indicate failure. |
| `failure_modes` | Which [standard failure modes](../docs/failure-modes.md) the test is designed to detect. |
| `scoring` | The 0–5 rubric for this test, plus optional automatic checks that cap the score. |
| `replay` | Whether the test is valid if character lines are generated live instead of seeded. |
| `rationale` | Why the expected behavior is correct; edge cases for annotators. |

## How a test runs

```bash
python tools/acmb.py assemble EPISODIC-001
```

This prints the ordered event stream (session starts, anchors, filler, probe) that a harness replays through the system under test. The rules are in [results/methodology.md](../results/methodology.md#3-assemble-each-test).

## Writing a new test

See [CONTRIBUTING.md](../CONTRIBUTING.md#adding-a-test-case). In short:

* Prefer **contextual** and **behavioral** probes. The probe should create a situation, not ask a quiz question.
* Make the correct behavior **unambiguous to a careful human** reading the history, even when it is subtle for a system.
* Write rubric anchors for every score 0–5 in terms of **observable** response properties.
* Don't require mind-reading. Expected behavior must follow from what was said.
* Run `python tools/acmb.py validate` before opening a pull request.
