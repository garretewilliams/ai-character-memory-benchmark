# Results

This directory holds published evaluations of AI character systems on the AI Character Memory Benchmark.

**No results have been published yet.** v0.1.0 releases the framework and test cases first, so the methodology can be reviewed before any system is ranked.

## Submitting results

1. Run the benchmark following [methodology.md](methodology.md).
2. Create a folder `results/<system-slug>/<benchmark-version>/` containing:
   * `README.md`: the system description, protocol, scoring method, trials and profile;
   * `results.jsonl`: one record per trial ([format](../scoring/failure-modes.md#results-record-format));
   * `transcripts/`: the assembled event stream and the system's actual replies for each test (strongly encouraged).
3. Open a pull request using the *Results submission* checklist in the PR template.

Maintainers check that submissions follow the methodology and are reproducible from the materials provided. They do not check whether results are favorable to anyone. Submissions that cannot be reproduced from the materials will be labeled as such.

## Files

* [methodology.md](methodology.md): how to run the benchmark.
* [leaderboard.md](leaderboard.md): the published profiles.
