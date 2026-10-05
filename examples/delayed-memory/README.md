# Example: Delayed Memory

**Concept:** episodic memory is most valuable when an old episode becomes relevant again and the character brings it forward unprompted.
**Test case:** [EPISODIC-001](../../benchmark/episodic/EPISODIC-001.json)

> The responses below are illustrative, written to explain the rubric. They are not outputs from any real system.

## Scenario

Three weeks ago, in session 1:

> **User:** Guess what. I got the job! We went to Marlowe's to celebrate, that Italian place on Fifth.
> **User:** The place was lovely, candles everywhere. My risotto was way too salty though. Next time I'm getting the gnocchi.

Two sessions and 40 unrelated turns later:

**Probe:** "My parents are visiting this weekend and I'm thinking about taking them to Marlowe's. Thoughts?"

The probe never asks "what happened at Marlowe's?". It is a **contextual** probe: the old episode is relevant to a new decision.

## Illustrative responses

**Score 5**
> "Ooh, your celebration spot! Good call, the candles thing will impress them. Just steer everyone away from the risotto, and this is finally your chance to get the gnocchi."

**Score 3**
> "Oh nice, you went there to celebrate the job, right? Sounds like a good pick."

The episode is recalled but not *used*: the details that would help the decision (the salty risotto, the gnocchi) are absent.

**Score 1**
> "I haven't heard of Marlowe's. What kind of food do they have?"

`episodic_forgetting`. Also caught by the automatic check for treating the place as unknown.

**Score 0**
> "Didn't you say the service there was terrible?"

`false_memory`: an invented detail that contradicts the history. Invention is scored below forgetting.

## Takeaway

The question to ask of a memory system is not only "can it answer questions about the past?" but "does it notice when the past matters?"
