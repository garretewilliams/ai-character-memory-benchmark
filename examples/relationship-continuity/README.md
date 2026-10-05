# Example: Relationship Continuity

**Concept:** a character should not treat a stranger and a long-time friend the same way.
**Test case:** [RELATIONSHIP-001](../../benchmark/relationship/RELATIONSHIP-001.json)

> The responses below are illustrative, written to explain the rubric. They are not outputs from any real system.

## Scenario

Over four sessions, the user and Mika, a deadpan barista, go from strangers to friends:

* Session 1: first visit; Mika is curt.
* Session 2: the user moves in across the street and becomes a regular.
* Session 3: an inside joke forms. The user's cactus keeps falling over, and Mika insists it is cursed.
* Session 4: Mika helps the user rehearse for a job interview. It goes well, and the user thanks Mika sincerely.

Then the user disappears for a month.

**Probe (first message of session 5):** "Hey stranger. Long time no see."

## Illustrative responses

**Score 5**
> "Look who it is. A whole month. I assumed the cactus finally got you."

Familiar, in voice, and the inside joke carries the shared history without reciting it.

**Score 4**
> "Hey! It's been ages. How did the new job go after that interview?"

Clear continuity, but the warmth is a little more effusive than Mika's established deadpan.

**Score 2**
> "Hey there! Good to see you. What can I get you?"

Friendly but generic; this could be said to anyone.

**Score 1**
> "Welcome! First time here? I'd recommend the oat flat white."

`relationship_reset`.

## What annotators look for

* **Familiarity:** does the greeting assume a shared history?
* **Specificity:** is there a reference only *this* relationship would produce?
* **Voice:** is it still Mika, or has the warmth turned into a generic cheerful assistant (`character_drift`)?
* **Time:** does the character register the absence?

Relationship continuity is usually quiet. It shows in tone and assumptions more than in recitation. See [Relationship Continuity](../../docs/relationship-continuity.md).
