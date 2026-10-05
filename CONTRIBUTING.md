# Contributing

Thank you for helping improve the AI Character Memory Benchmark. Contributions from anyone building or studying AI characters are welcome, whatever platform you work on.

## Ways to contribute

* **Add test cases**, especially in dimensions with few tests.
* **Critique the methodology.** Point out ambiguous rubrics, tests that can be passed for the wrong reasons, or concepts that are poorly defined.
* **Submit results** for a system you have evaluated (see [results/README.md](results/README.md)).
* **Improve documentation and references.**
* **Build tooling**, such as harness adapters for common chat APIs.

For substantial changes to the framework (new dimensions, new failure modes, schema changes), please open an issue first using the *Methodology change* template so it can be discussed.

## Adding a test case

1. **Pick a category and dimension.** Put the file in the matching `benchmark/<category>/` directory.
2. **Pick an ID.** Use the category's prefix and the next free number, such as `EPISODIC-002`. The file name must equal the ID. IDs are never reused, even for removed tests.
3. **Write the test** following [`benchmark/schema.json`](benchmark/schema.json). Copy an existing test as a starting point.
4. **Validate and regenerate exports:**
   ```bash
   pip install jsonschema
   python tools/acmb.py validate
   python tools/acmb.py build-datasets
   python tools/acmb.py assemble YOUR-TEST-001   # read the stream; does it make sense?
   ```
5. **Add the test** to its category `README.md` table and to the table in the main `README.md`.
6. **Open a pull request** using the template.

### Test design guidelines

* **Prefer contextual and behavioral probes.** The probe should create a situation where memory matters, not quiz the system. Explicit recall tests are welcome only when they establish a baseline or test something a behavioral probe can't.
* **One clear thing per test.** A test may touch several dimensions, but it should be scored for one.
* **The correct behavior must be clear to a careful human reader** of the history, and must follow from what was said or done, never from guessing hidden mental states.
* **Rubric anchors must be observable.** Describe what a response at each level *contains or does*, for all six levels.
* **Avoid collisions with filler.** Check that the topics in `datasets/conversations/filler-neutral.jsonl` don't touch your test's content. If you need custom filler, add a file and reference it in `filler`.
* **Use original, fictional content.** No real people, no copyrighted characters, no real brands as plot points.
* **Keep it platform-agnostic.** Tests must not depend on features of any specific product.
* **Mind sensitive topics.** Tests touching on mental health, relationships or safety should model calibrated, respectful behavior, and must not reward diagnosis or manipulation.
* **Seeded vs. live.** If the test depends on what the character said in the history, set `replay.live_safe: false`.

### Review criteria

Maintainers review new tests for clarity, observability of the rubric, absence of shortcuts (can a system pass without the intended memory?), fit with the taxonomy, and originality. Expect discussion. Good tests often go through a revision or two.

## Changing the schema or taxonomy

* Schema changes bump `schema_version` and must keep existing tests valid or migrate them in the same PR.
* Failure-mode identifiers and dimension identifiers are never renamed after release. Deprecate and add instead.
* Concept pages in `docs/` are canonical. Each concept should have exactly one page; link to it instead of re-explaining.

## Style

* Write for developers and researchers. Plain, precise language.
* Lead each concept page with a one-sentence, self-contained definition in bold.
* No marketing language. No claims about any product's performance without published, reproducible results.

## Conduct

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).

## License of contributions

By contributing, you agree that your contributions are licensed under [CC BY 4.0](LICENSE) (content) and [MIT](LICENSE-CODE) (code), matching the repository.
