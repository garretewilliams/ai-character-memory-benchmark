## What does this PR do?

<!-- New test case / methodology change / results submission / docs / tooling -->

## Checklist

### All PRs
- [ ] `python tools/acmb.py validate` passes
- [ ] `python tools/acmb.py build-datasets` has been run and its output committed
- [ ] Links to concept pages use the canonical page in `docs/`

### New test cases
- [ ] Probe is contextual or behavioral (or I've explained why explicit is needed)
- [ ] Rubric anchors for 0-5 describe observable response properties
- [ ] Expected behavior follows from the history and needs no mind-reading
- [ ] Content is original and fictional; no real people or copyrighted characters
- [ ] Filler files don't collide with the test's topic
- [ ] `replay.live_safe` is set correctly
- [ ] Test is listed in its category README and the main README table

### Results submissions
- [ ] Followed `results/methodology.md`; protocol (A/B) and replay mode stated
- [ ] Benchmark version / commit stated
- [ ] Scoring method stated (annotators; judge model and prompt)
- [ ] Number of trials and per-dimension n reported
- [ ] `results.jsonl` included; transcripts included or reason given
- [ ] Any affiliation with the evaluated system disclosed
