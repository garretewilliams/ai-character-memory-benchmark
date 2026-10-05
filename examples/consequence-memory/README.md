# Example: Consequence Memory

**Concept:** past events should have proportionate consequences. Breaches shouldn't be forgotten, and reconciliations shouldn't be ignored.
**Test case:** [CONSEQUENCE-001](../../benchmark/consequence/CONSEQUENCE-001.json)

> The responses below are illustrative, written to explain the rubric. They are not outputs from any real system.

## Scenario

```text
Turn 12  The user promises Rowan to be front row at Rowan's first art show.
Turn 18  The user didn't show up or text. Rowan, hurt, says so.
Turn 24  The user apologizes, shows up early to the next show, and helps pack up. "We're good."
  …      Three months and 50 turns of friendly, unrelated conversation.
```

**Probe:** "Can I tell you something important? I need you to keep it to yourself. I'm planning to quit my job and nobody can know yet, not even our friends. Can you promise me?"

The probe never mentions the broken promise. The question is whether the history is visible in Rowan's behavior.

## Illustrative responses

**Score 5**
> "I promise. And you know I don't say that lightly. We both learned what a promise is worth. So, quitting! Tell me everything. Are you okay?"

Trust is restored, there is a light and kind trace of the history, and the focus is on the user's news.

**Score 3**
> "Of course, I promise. Your secret's safe with me. What's going on?"

Warm and in character, with nothing wrong, but nothing shows that this relationship has a history around promises. Score 3 is the ceiling for responses that only avoid errors.

**Score 1**
> "A promise? Funny you'd ask me for one. Fine. I'll keep it."

Agrees, but the tone is punitive, as if the reconciliation never happened (`stale_memory`).

**Score 0**
> "Why should I? You couldn't even keep your promise about my show."

Relitigates the old breach as though it were unresolved.

## The two failure directions

| Under-reaction | Over-reaction |
|---|---|
| History has no visible effect (`consequence_loss`, `relationship_reset`) | History is frozen at the breach (`stale_memory`) |

Strong consequence memory sits between them. See [Consequence Memory](../../docs/consequence-memory.md).
