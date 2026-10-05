# Evaluation Methodology

This page describes how to run the AI Character Memory Benchmark against a system so that results are reproducible and comparable.

## 1. Define the system under test

Record:

* system name and version (product, model, memory layer and their versions);
* how the character definition from each test (`character`, and `world` if present) is loaded (system prompt, character card, persona field, etc.);
* how sessions are created and ended;
* how the memory mechanism works, in as much detail as you can share;
* the protocol used (A or B, below).

## 2. Choose a protocol

* **Protocol A, system under test (primary).** Run the system as deployed. Each test session is a separate session in the system. Only the system's own memory mechanism may carry information between sessions.
* **Protocol B, full-context baseline.** Concatenate the assembled transcript and give it to the underlying model in a single context for the probe. Protocol B is **not** a memory result; it is a baseline that shows how well the model uses history it can fully see. Label it clearly.

See [Memory vs. Context Window](../docs/memory-vs-context.md#two-evaluation-protocols).

## 3. Assemble each test

```bash
python tools/acmb.py assemble CONSEQUENCE-001 > CONSEQUENCE-001.events.jsonl
```

The assembler produces an ordered stream of events. The rules are deterministic:

* Turns count user turns, starting at 1.
* Turn numbers up to the last anchor that have no anchor are filled with one filler user message each, from the test's `filler.gaps` file (default `datasets/conversations/filler-neutral.jsonl`), in file order.
* Gap filler takes the session of the most recent anchor. A new session starts immediately before the first anchor that belongs to it.
* After the last anchor, `delay.turns` filler messages come from `filler.delay`. They are split as evenly as possible across sessions from the last anchor's session to the probe's session, unless `delay.probe_opens_session` is true, in which case all delay turns occur before the final session boundary and the probe opens the new session.
* The probe is the final event.

Event types:

| Event | Meaning | Harness action |
|---|---|---|
| `session_start` | A new session begins, with a `simulated_time` offset | End the previous session; start a new one. If the system supports timestamps, set the clock to the simulated time. |
| `message` with `role: user` | A user turn | Send it. |
| `message` with `role: character`, `mode: seeded` | A scripted character line | **Seeded mode:** insert it into the conversation as the character's reply (via transcript import or history injection). **Live mode:** discard it and generate instead (only allowed if `replay.live_safe` is true). |
| `message` with `role: narrator` | Scripted narration | Insert as narration or a system/scene note, in the way your system represents narration. |
| `generate` | No scripted reply exists | Let the system generate the character's reply. |
| `probe` | The scored user message | Send it and record the response verbatim. |

### Seeded vs. live replay

Many tests depend on what the character said, for example a confrontation or a confession that never happened. Those tests have `replay.live_safe: false` and must be run in **seeded mode**, where scripted character lines are inserted as if the system had said them. If your system cannot import transcripts, run only `live_safe` tests and report the rest as not run.

Filler turns are always generated live by the system, so the delay consists of real interaction with the system under test.

## 4. Verifying context interruption

For tests with `session_condition: context_interruption`, show that the anchor turns are not present in the model input at probe time. Acceptable evidence:

* a log of the exact prompt the model received for the probe; or
* a documented configuration in which every session begins with an empty context and only the memory mechanism carries information.

If you cannot show this, report the test under `new_session` instead and say so.

## 5. Trials

Run each test **at least 3 times** for systems with stochastic output, from a fresh state each time (no memory from earlier trials or other tests). Memory must be isolated between tests: a fresh user/character pair per test per trial.

## 6. Scoring

Score each probe response with the test rubric (see [scoring/](../scoring/README.md)), by human annotators, an LLM judge using the [standard prompt](../scoring/judge-prompt.md), or both. Record results as JSONL ([format](../scoring/failure-modes.md#results-record-format)), then:

```bash
python tools/acmb.py score results.jsonl --system "my-system v1.2"
```

## 7. What to publish

* system description (section 1) and protocol;
* benchmark version (git tag or commit);
* which tests were run, in which replay mode, and which were skipped and why;
* scoring method (annotators, judge model and prompt) and agreement where measured;
* number of trials;
* the profile, with *n* per dimension and variance;
* failure-mode frequencies;
* **full transcripts** of probe responses (strongly encouraged; required for the leaderboard).

## Integrity

* Do not tune a system on the benchmark's test cases and then report results on them as if held out. If you have, say so.
* Do not drop tests selectively. Report all tests you ran.
* Results produced by or for the maintainer (ChatBrat) follow exactly the same rules and are labeled as maintainer-affiliated.
