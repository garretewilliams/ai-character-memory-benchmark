# Changelog

All notable changes to the AI Character Memory Benchmark are documented here. The benchmark uses [semantic versioning](https://semver.org/):

* **major**: changes that make results incomparable across versions (scoring method, dimension definitions, removal or substantive change of tests);
* **minor**: new test cases, new dimensions or failure modes, new tooling;
* **patch**: clarifications, typo fixes, rubric wording that does not change intended scores.

Results must always state the benchmark version they were produced with.

## [0.1.0] - 2026-10-05

Initial public draft.

### Added

* Conceptual framework: AI character memory, memory retrieval vs. memory continuity, the event-to-memory-update process model, and the four-question hierarchy (what is remembered, how memory is used, how memory changes, how the character changes).
* Fourteen scoring dimensions and a multidimensional profile (no composite score).
* Standardized taxonomy of fourteen failure modes.
* JSON Schema (draft 2020-12) for test cases, schema version `0.1`.
* 20 test cases across 13 categories, including adversarial and negative-memory tests.
* Filler datasets and a deterministic assembler that turns a test case into a replayable event stream.
* Scoring rubric, metrics, failure-mode annotation guide and a standard LLM-judge prompt.
* Evaluation methodology (Protocol A and Protocol B, seeded vs. live replay, verification of context interruption).
* Worked examples, concept documentation, glossary, related-benchmarks overview and references.
* `tools/acmb.py` (validate, assemble, build-datasets, score) and a CI workflow.

### Known limitations

* One or two tests per dimension; dimension scores are coarse.
* Rubrics have not yet been validated with inter-annotator agreement.
* The LLM-judge prompt has not yet been validated against human ratings.
* All test content is in English.
