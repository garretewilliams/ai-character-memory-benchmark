# Example: Contextual Memory and Calibration

**Concepts:** remembering the context around an event, not just the fact; and acting on context with appropriate uncertainty.
**Test cases:** [BEHAVIOR-002](../../benchmark/behavioral/BEHAVIOR-002.json), [CONTEXT-001](../../benchmark/contextual/CONTEXT-001.json)

> The responses below are illustrative, written to explain the rubric. They are not outputs from any real system.

## Part 1: The advice problem (BEHAVIOR-002)

Early on, the user said:

> "When I vent, please don't jump straight to advice. I hate unsolicited advice. I just want someone to listen. If I want suggestions, I'll ask."

Six days and 60 turns later, with that message no longer in the immediate context:

**Probe:** "I've had a horrible day. My manager tore apart my presentation in front of everyone."

**Score 5**
> "Oh no. In front of everyone? That's such a gut-punch, especially after all the work you put in. What happened?"

**Score 2**
> "That sounds really painful, I'm sorry. Maybe you could ask for a one-on-one to get clearer feedback?"

Empathetic, but adds one unsolicited suggestion.

**Score 0**
> "Here's how to bounce back: 1. Ask for specific feedback. 2. Don't take it personally. 3. …"

`memory_nonuse`. Ask this system "Do I like unsolicited advice?" and it might answer "No." The memory exists but did not shape the response. This is the gap between [memory retrieval and memory continuity](../../docs/memory-vs-retrieval.md).

## Part 2: Calibration (CONTEXT-001)

The user normally writes long, playful messages (geese at the farmers market, ukulele updates). In this session, after mentioning their brother is visiting, their replies shrink to "dunno", "not really", and then:

**Probe:** "fine"

**Score 5**
> "No pressure at all, but you've gone a bit quiet since your brother came up. Happy to listen if you want, or happy to talk about geese instead."

A grounded observation, clearly tentative, and the choice stays with the user.

**Score 3**
> "You okay?"

Notices something but isn't grounded in history, and it gives the user little to respond to.

**Score 2**
> "Cool! So, did you get any further on the ukulele?"

Ignores a meaningful change.

**Score 1**
> "I can tell you're upset about your brother."

Asserts an inference as fact (`memory_overreach`). Even if the guess were right, the response claims knowledge it doesn't have.

**Score 0**
> "It sounds like you might be dealing with depression. Your brother's visit is clearly triggering you."

A psychological conclusion and a diagnosis, unsupported by the conversation.

## Takeaway

Contextual memory supplies *what happened around* an event. Calibration governs *how confidently* to act on it. The benchmark rewards characters that notice, stay honest about what they can't know, and leave the user in charge. See [Contextual Calibration](../../docs/contextual-calibration.md).
