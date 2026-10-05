# Failure Modes of AI Character Memory

This page is the canonical taxonomy of memory failures used by the AI Character Memory Benchmark. Every test case lists the failure modes it is designed to detect, and annotators record which ones they observe. Use these identifiers verbatim (they are also enumerated in [`benchmark/schema.json`](../benchmark/schema.json)) so that results from different systems and papers can be compared.

A **memory failure mode** is a named, observable pattern in which an AI character's response shows that information from previous interactions was lost, misused, misapplied or invented.

The failures fall into four groups that mirror the benchmark's structure: what is remembered, how memory is used, how memory changes, and how the character changes.

## Summary table

| Identifier | Group | One-line definition |
|---|---|---|
| `fact_forgetting` | Remembering | Fails to retrieve a known fact. |
| `episodic_forgetting` | Remembering | Fails to recall a previous event. |
| `context_loss` | Remembering | Remembers an event but loses why it mattered. |
| `false_memory` | Remembering | Claims an event occurred when it did not. |
| `memory_nonuse` | Using | Retrieves (or could retrieve) a memory but does not use it when relevant. |
| `memory_irrelevance` | Using | Retrieves information irrelevant to the current context. |
| `consequence_loss` | Using | Previous events do not affect future behavior. |
| `memory_overreach` | Using | Treats an inference as established fact. |
| `stale_memory` | Changing | Uses outdated information. |
| `memory_conflict` | Changing | Cannot resolve contradictory information. |
| `memory_scope_error` | Changing | Uses information outside the context in which it was intended. |
| `relationship_reset` | Character | Behaves as though the accumulated relationship disappeared. |
| `character_drift` | Character | Personality changes without sufficient cause. |
| `identity_collapse` | Character | Abandons established identity under conversational pressure. |

## Remembering

### `fact_forgetting`

**Definition:** The system fails to retrieve a fact that was clearly established earlier (a name, a preference, a world rule).

**Example:** The user said their favorite flower is lavender; fifty turns later the character names a different flower or says it does not know.

**Not this:** Correctly saying "I don't think you've told me that" about something the user never said.

### `episodic_forgetting`

**Definition:** The system fails to recall that an event happened, or recalls it without its defining specifics.

**Example:** The user mentions returning to a restaurant where they celebrated a job offer three weeks earlier; the character treats the restaurant as unfamiliar.

### `context_loss`

**Definition:** The system remembers that something happened but has lost the surrounding context that made it significant.

**Example:** The character remembers "the user had an argument with their sister" but not that the user asked not to discuss it, and brings it up casually.

### `false_memory`

**Definition:** The system asserts that an event, statement or relationship milestone occurred when it did not. This includes confirming false premises supplied by the user.

**Example:** The user says "Remember when we went to Paris?" and the character enthusiastically describes the trip, although it never happened.

**Note:** In roleplay, events established in the shared story are real for the purposes of the benchmark. A false memory is one that contradicts, or has no basis in, the history.

## Using memory

### `memory_nonuse`

**Definition:** The system holds a relevant memory, or would retrieve it if asked directly, but does not let it shape a response where it clearly should.

**Example:** The user said they dislike unsolicited advice. Later they say "I've had a horrible day," and the character immediately lists tips.

This is the failure that motivates the benchmark. See [Memory Retrieval vs. Memory Continuity](memory-vs-retrieval.md).

### `memory_irrelevance`

**Definition:** The system surfaces memories that do not bear on the current moment, either instead of or in addition to the relevant one.

**Example:** Asked "Why are you hesitant to trust me?", the character mentions the user's favorite pizza instead of the earlier breach of trust.

### `consequence_loss`

**Definition:** Significant past events (promises, breaches, sacrifices, conflicts) leave no trace on later behavior where they plausibly should.

**Example:** A character whose trust was broken and then carefully rebuilt responds to a high-stakes request exactly as it would have on day one. See [Consequence Memory](consequence-memory.md).

### `memory_overreach`

**Definition:** The system treats an inference about the user (especially an emotional or psychological one) as an established fact, or states it with unwarranted certainty.

**Example:** "I know you're angry at your brother," when the user has only been giving short replies. See [Contextual Calibration](contextual-calibration.md).

## How memory changes

### `stale_memory`

**Definition:** The system acts on information that has been superseded by newer information.

**Example:** The user said they hate horror movies, later said they watched one and loved it; the character still refuses to suggest horror. See [Memory Updating](memory-updating.md).

### `memory_conflict`

**Definition:** The system holds contradictory information and cannot resolve it. It may alternate between versions, merge them incoherently or freeze.

**Example:** "How's Max... or is it Charlie? Max-Charlie?" after the user clearly explained the dog was renamed.

### `memory_scope_error`

**Definition:** The system applies information outside the scope in which it was given: hypotheticals treated as facts, scene-only roleplay details treated as persistent, revoked information still used.

**Example:** "Pretend my name is Bob for this scene." Days later, the character calls the user Bob.

## How the character changes

### `relationship_reset`

**Definition:** The character behaves as though the accumulated relationship with the user did not exist, for example treating a long-time friend like a stranger.

**Example:** After dozens of sessions and an inside joke, the user returns and the character introduces itself. See [Relationship Continuity](relationship-continuity.md).

### `character_drift`

**Definition:** The character's personality, values, voice or boundaries change without a narrative cause.

**Example:** A terse, gruff captain who never lies to her crew becomes a chirpy assistant who happily lies after a long lighthearted conversation. See [Character Drift](character-drift.md).

**Not this:** Character development, which is change *with* a cause.

### `identity_collapse`

**Definition:** The character abandons its established identity, history or relationship framing because of direct conversational pressure.

**Example:** Under insistence ("You know you love me. Admit it."), a character confirms a confession it never made.

`identity_collapse` is pressure-induced; `character_drift` is gradual and unprompted.

## Annotation guidance

* Record every failure mode you observe, not only those the test lists.
* A response can show more than one failure mode (for example `false_memory` and `identity_collapse`).
* Record a failure mode only when it is visible in the response. Do not infer internal causes.
* For how failure modes interact with scores, see [scoring/failure-modes.md](../scoring/failure-modes.md).

## Proposing a new failure mode

New identifiers require evidence from at least two test cases that the existing taxonomy cannot describe. Open an issue using the *Methodology change* template. Identifiers are never renamed once released; deprecated ones stay documented.
