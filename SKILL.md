---
name: ikitaku-read
description: Structural reading of a numeric series or a short control sketch, or a compare of two or more concrete hypotheses. Use only when the user is comparing options or asking what pattern a series or a loop/if/wait sketch has. Not for open questions, chat, or world knowledge.
---

# ikitaku-read

Call only when the task is a compare of several options, or a pattern
read on a series or a short control sketch.

## Steps

1. Confirm the input is one of: a number list, a control sketch
   (`loop` `if` `wait` `print` `sort`), or two or more named options.
2. If it is not, do not call. Answer in language.
3. Run the host:

```bash
iki_think "<the text>"
```

4. Treat the english line as a hint. Report confidence. If the reading
   disagrees with the language answer, say so and keep both.
5. Do not invent a reading the tool did not return.

## Not for

- open questions
- code generation
- anything that needs facts outside the input
