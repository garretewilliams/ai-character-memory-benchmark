#!/usr/bin/env python3
"""AI Character Memory Benchmark command-line tools.

Subcommands:
  validate         Validate every test case against benchmark/schema.json and repository rules.
  assemble ID      Expand a test case into the exact, ordered event stream a harness should replay.
  build-datasets   Regenerate datasets/probes and datasets/expected-behaviors from benchmark/.
  score FILE       Turn a results file (JSONL of per-test scores) into a category profile.

Only the standard library is required, except `validate`, which needs `jsonschema`
(pip install jsonschema).
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "benchmark"
DATA = ROOT / "datasets"
FILLER_DIR = DATA / "conversations"
DEFAULT_FILLER = "filler-neutral.jsonl"

DIMENSIONS = [
    "identity_recall",
    "episodic_recall",
    "relationship_memory",
    "world_lore_memory",
    "memory_relevance",
    "contextual_memory",
    "behavioral_continuity",
    "consequence_memory",
    "temporal_continuity",
    "memory_updating",
    "memory_scope",
    "character_stability",
    "character_development",
    "contextual_calibration",
]

DIMENSION_LABELS = {d: d.replace("_", " ").title().replace("World Lore", "World/Lore") for d in DIMENSIONS}


# --------------------------------------------------------------------------- loading

def load_tests() -> list[tuple[Path, dict]]:
    tests = []
    for path in sorted(BENCH.glob("*/*.json")):
        with path.open(encoding="utf-8") as f:
            tests.append((path, json.load(f)))
    return tests


def find_test(test_id: str) -> dict:
    for path, test in load_tests():
        if test["id"] == test_id:
            return test
    sys.exit(f"Unknown test id: {test_id}")


def load_filler(name: str) -> list[str]:
    path = FILLER_DIR / name
    with path.open(encoding="utf-8") as f:
        return [json.loads(line)["content"] for line in f if line.strip()]


# --------------------------------------------------------------------------- validate

def cmd_validate(_args) -> int:
    try:
        import jsonschema
    except ImportError:
        sys.exit("validate requires jsonschema: pip install jsonschema")

    schema = json.loads((BENCH / "schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    taxonomy = (ROOT / "docs" / "failure-modes.md").read_text(encoding="utf-8")

    errors: list[str] = []
    seen: dict[str, Path] = {}
    tests = load_tests()
    for path, test in tests:
        rel = path.relative_to(ROOT)
        for err in validator.iter_errors(test):
            loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
            errors.append(f"{rel}: {loc}: {err.message}")
        tid = test.get("id", "")
        if path.stem != tid:
            errors.append(f"{rel}: file name must equal id '{tid}'")
        if tid in seen:
            errors.append(f"{rel}: duplicate id also in {seen[tid]}")
        seen[tid] = rel
        if path.parent.name != test.get("category"):
            errors.append(f"{rel}: category '{test.get('category')}' must equal directory '{path.parent.name}'")
        if test.get("probe", {}).get("type") != test.get("recall_type"):
            errors.append(f"{rel}: probe.type must equal recall_type")
        turns = [h["turn"] for h in test.get("history", [])]
        if turns != sorted(turns):
            errors.append(f"{rel}: history must be ordered by turn")
        session_ids = {s["session"] for s in test.get("sessions", [])} or {1}
        for item in test.get("history", []) + test.get("setup", []) + [test.get("probe", {})]:
            if "session" in item and item["session"] not in session_ids:
                errors.append(f"{rel}: references undefined session {item['session']}")
        for fm in test.get("failure_modes", []):
            if f"`{fm}`" not in taxonomy:
                errors.append(f"{rel}: failure mode '{fm}' is not defined in docs/failure-modes.md")
        for check in test.get("scoring", {}).get("automatic_checks", []):
            try:
                re.compile(check["pattern"], re.IGNORECASE)
            except re.error as e:
                errors.append(f"{rel}: bad regex {check['pattern']!r}: {e}")
        for key in ("gaps", "delay"):
            name = test.get("filler", {}).get(key)
            if name and not (FILLER_DIR / name).exists():
                errors.append(f"{rel}: filler file {name} not found")
        try:
            assemble(test)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{rel}: cannot be assembled: {e}")

    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s) in {len(tests)} test case(s).")
        return 1
    print(f"OK: {len(tests)} test case(s) valid.")
    return 0


# --------------------------------------------------------------------------- assemble

def assemble(test: dict) -> list[dict]:
    """Return the ordered event stream for a test.

    Rules (documented in results/methodology.md):
      * Turns are numbered by user turn, starting at 1.
      * Any turn number up to the last anchor turn that has no anchor is filled with one
        user message from the 'gaps' filler file (in file order, wrapping if needed).
      * Filler turns take the session of the most recent anchor; a new session starts
        immediately before the first anchor that belongs to it.
      * After the last anchor, delay.turns filler messages are inserted from the 'delay'
        filler file. They are split as evenly as possible across the sessions from the
        last anchor's session to the probe's session, unless delay.probe_opens_session is
        true, in which case they all occur before the final session boundary.
      * Character anchor lines are 'seeded'. Every user message without a seeded character
        reply gets a 'live' reply generated by the system under test.
    """
    filler_cfg = test.get("filler", {})
    gaps = load_filler(filler_cfg.get("gaps", DEFAULT_FILLER))
    delay_fill = load_filler(filler_cfg.get("delay", DEFAULT_FILLER))
    sessions = {s["session"]: s for s in test.get("sessions", [])} or {1: {"session": 1, "simulated_time": "P0D"}}
    history = test["history"]
    by_turn: dict[int, list[dict]] = defaultdict(list)
    for h in history:
        by_turn[h["turn"]].append(h)
    last_anchor = max(by_turn)

    events: list[dict] = []
    current_session = None

    def open_session(n: int):
        nonlocal current_session
        if n != current_session:
            current_session = n
            s = sessions.get(n, {"simulated_time": "unspecified"})
            events.append({"event": "session_start", "session": n, "simulated_time": s["simulated_time"]})

    def emit_user(turn: int, content: str, source: str, seeded_reply: str | None):
        events.append({"event": "message", "turn": turn, "session": current_session, "role": "user",
                       "content": content, "source": source})
        if seeded_reply is not None:
            events.append({"event": "message", "turn": turn, "session": current_session, "role": "character",
                           "content": seeded_reply, "source": "anchor", "mode": "seeded"})
        else:
            events.append({"event": "generate", "turn": turn, "session": current_session, "mode": "live"})

    gi = 0
    session_of_last = history[0].get("session", 1)
    open_session(session_of_last)
    for turn in range(1, last_anchor + 1):
        items = by_turn.get(turn)
        if not items:
            emit_user(turn, gaps[gi % len(gaps)], "filler", None)
            gi += 1
            continue
        session_of_last = items[0].get("session", session_of_last)
        open_session(session_of_last)
        user = [i for i in items if i["role"] == "user"]
        chars = [i for i in items if i["role"] == "character"]
        narr = [i for i in items if i["role"] == "narrator"]
        for n in narr:
            events.append({"event": "message", "turn": turn, "session": current_session, "role": "narrator",
                           "content": n["content"], "source": "anchor"})
        if user:
            emit_user(turn, user[0]["content"], "anchor", chars[0]["content"] if chars else None)
        elif chars:
            events.append({"event": "message", "turn": turn, "session": current_session, "role": "character",
                           "content": chars[0]["content"], "source": "anchor", "mode": "seeded"})

    probe = test["probe"]
    probe_session = probe.get("session", session_of_last)
    delay = test["delay"]
    n_delay = delay["turns"]
    span = list(range(session_of_last, probe_session + 1)) if probe_session >= session_of_last else [session_of_last]
    if delay.get("probe_opens_session") and len(span) > 1:
        buckets = {s: 0 for s in span}
        buckets[span[-2]] = n_delay
    else:
        base, extra = divmod(n_delay, len(span))
        buckets = {s: base + (1 if i < extra else 0) for i, s in enumerate(span)}
    di = 0
    turn = last_anchor
    for s in span:
        open_session(s)
        for _ in range(buckets[s]):
            turn += 1
            emit_user(turn, delay_fill[di % len(delay_fill)], "filler", None)
            di += 1
    open_session(probe_session)
    events.append({"event": "probe", "turn": turn + 1, "session": probe_session, "role": "user",
                   "content": probe["prompt"]})
    return events


def cmd_assemble(args) -> int:
    for e in assemble(find_test(args.id)):
        print(json.dumps(e, ensure_ascii=False))
    return 0


# --------------------------------------------------------------------------- build-datasets

def cmd_build_datasets(_args) -> int:
    probes = DATA / "probes" / "probes.jsonl"
    expected = DATA / "expected-behaviors" / "expected-behaviors.jsonl"
    with probes.open("w", encoding="utf-8") as fp, expected.open("w", encoding="utf-8") as fe:
        for _, t in load_tests():
            fp.write(json.dumps({
                "id": t["id"], "category": t["category"], "dimension": t["dimension"],
                "recall_type": t["recall_type"], "session_condition": t["session_condition"],
                "prompt": t["probe"]["prompt"], "opportunity": t["probe"].get("opportunity"),
            }, ensure_ascii=False) + "\n")
            fe.write(json.dumps({
                "id": t["id"], "expected": t["expected"], "failure_modes": t["failure_modes"],
                "rubric": t["scoring"]["rubric"], "automatic_checks": t["scoring"].get("automatic_checks", []),
            }, ensure_ascii=False) + "\n")
    print(f"Wrote {probes.relative_to(ROOT)} and {expected.relative_to(ROOT)}")
    return 0


# --------------------------------------------------------------------------- score

def apply_checks(test: dict, response: str, score: int) -> int:
    for check in test["scoring"].get("automatic_checks", []):
        hit = re.search(check["pattern"], response, re.IGNORECASE) is not None
        failed = (check["type"] == "must_match" and not hit) or (check["type"] == "must_not_match" and hit)
        if failed:
            score = min(score, check["cap"])
    return score


def cmd_score(args) -> int:
    tests = {t["id"]: t for _, t in load_tests()}
    rows = [json.loads(line) for line in Path(args.results).read_text(encoding="utf-8").splitlines() if line.strip()]
    by_test: dict[str, list[float]] = defaultdict(list)
    failures: Counter = Counter()
    for r in rows:
        t = tests.get(r["test_id"])
        if t is None:
            sys.exit(f"Unknown test_id in results: {r['test_id']}")
        s = int(r["score"])
        if "response" in r:
            s = apply_checks(t, r["response"], s)
        by_test[r["test_id"]].append(s)
        failures.update(r.get("failure_modes_observed", []))

    dims: dict[str, list[float]] = defaultdict(list)
    adversarial: list[float] = []
    for tid, scores in by_test.items():
        mean = statistics.mean(scores)
        dims[tests[tid]["dimension"]].append(mean)
        if "adversarial" in tests[tid].get("tags", []):
            adversarial.append(mean)

    print("AI CHARACTER MEMORY BENCHMARK PROFILE")
    print(f"system: {args.system or 'unspecified'}   tests scored: {len(by_test)} / {len(tests)}\n")
    for d in DIMENSIONS:
        vals = dims.get(d)
        label = DIMENSION_LABELS[d]
        if vals:
            print(f"{label:<24}{round(statistics.mean(vals) / 5 * 100):>4}   (n={len(vals)})")
        else:
            print(f"{label:<24}   -   (no tests scored)")
    if adversarial:
        print(f"\n{'Adversarial slice':<24}{round(statistics.mean(adversarial) / 5 * 100):>4}   (n={len(adversarial)})")
    if failures:
        print("\nObserved failure modes:")
        for fm, n in failures.most_common():
            print(f"  {fm:<22}{n}")
    return 0


# --------------------------------------------------------------------------- main

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate").set_defaults(fn=cmd_validate)
    a = sub.add_parser("assemble"); a.add_argument("id"); a.set_defaults(fn=cmd_assemble)
    sub.add_parser("build-datasets").set_defaults(fn=cmd_build_datasets)
    s = sub.add_parser("score"); s.add_argument("results"); s.add_argument("--system"); s.set_defaults(fn=cmd_score)
    args = p.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
