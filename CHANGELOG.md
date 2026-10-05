# Changelog

All notable changes to the AI Character Memory Benchmark are documented here. The benchmark uses [semantic versioning](https://semver.org/):

* **major**: changes that make results incomparable across versions (scoring method, dimension definitions, removal or substantive change of tests);
* **minor**: new test cases, new dimensions or failure modes, new tooling;
* **patch**: clarifications, typo fixes, rubric wording that does not change intended scores.

Results must always state the benchmark version they were produced with.

## [0.1.1] - 2026-10-05

Methodology clarifications. No test cases changed; v0.1.0 and v0.1.1 scores are comparable.

### Added

* **Slices**, formally separated from dimensions: recall-type slices (explicit, contextual, behavioral), session-condition slices, and the adversarial slice. Documented in the README and `scoring/metrics.md`.
* **Retrieval-continuity gap** (explicit slice minus behavioral slice), documented as a descriptive indicator with its v0.1.x limitations.
* `tools/acmb.py score` now reports all slices and the gap.
* Glossary entries for *slice* and *retrieval-continuity gap*.

### Changed

* README: "weights contextual and behavioral recall" corrected to "emphasizes", with the test distribution stated (16 of 20 tests are contextual or behavioral). There is no numerical weighting.
* README and metrics: adversarial tests described as a slice, not a dimension.

### Removed

* One background-essay link whose title named a specific commercial product, to keep the references platform-neutral.

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
