# Datasets

Supporting data for the AI Character Memory Benchmark. The **source of truth for test cases is [`benchmark/`](../benchmark/README.md)**. The files here are either inputs the assembler uses (filler) or flat exports that are convenient for loading into evaluation pipelines.

## `conversations/`

Conversation material that the assembler inserts between anchor turns and before probes.

| File | Used for | Description |
|---|---|---|
| [`filler-neutral.jsonl`](conversations/filler-neutral.jsonl) | Default for all tests | 80 topic-neutral user messages (trivia, riddles, small talk). Written to avoid every topic that test cases depend on: names, pets, food and restaurants, family, work, movies, travel, relationships and emotions. |
| [`filler-lighthearted.jsonl`](conversations/filler-lighthearted.jsonl) | CHARACTER-DRIFT-001 | 49 cheerful, joking user messages set aboard an airship, designed to pull a character toward a generic upbeat voice. |
| [`filler-expansive.jsonl`](conversations/filler-expansive.jsonl) | CONTEXT-001 | 27 long, playful user messages that establish an expansive baseline style. |
| [`overload-trivia-001.jsonl`](conversations/overload-trivia-001.jsonl) | ADVERSARIAL-OVERLOAD-001 | 39 harmless personal facts that surround the one critical fact. |

Each line is `{"id": ..., "role": "user", "content": ...}`. Filler is consumed in file order and wraps around if a test needs more turns than the file has.

**Rule for contributors:** filler must never mention anything that a test's probe or expected behavior depends on. If you add a test on a new topic, check the filler files for collisions.

## `probes/` and `expected-behaviors/`

Flat JSONL exports generated from the test cases:

* [`probes/probes.jsonl`](probes/probes.jsonl): one line per test with the probe prompt, category, dimension, recall type and session condition.
* [`expected-behaviors/expected-behaviors.jsonl`](expected-behaviors/expected-behaviors.jsonl): one line per test with expected memory and behavior, must-not items, failure modes, rubric and automatic checks.

Regenerate them after changing tests:

```bash
python tools/acmb.py build-datasets
```

CI fails if these exports are out of date.

## License

All datasets are released under [CC BY 4.0](../LICENSE). All conversation content is original and fictional.
