# ikitaku-engine

Formal reasoner. Invoked by a language model only when the task is
comparing several options or hypotheses, or reading a numeric series
or a short control sketch.

The source of the reasoner is still `sera5m/ikitaku` under
`rs_vm/ikitaku/`. This repo is the tool surface: when to call, the
JSON contract, and the English-to-concept mapping notes.

## When to call

Call when:

- the user has two or more concrete options and wants a structural compare
- the input is a numeric series and the question is "what pattern"
- the input is a short control sketch (`loop`, `if`, `wait`, `print`, `sort`)

Do not call for open questions, chat, or anything that needs world knowledge.

## Contract

Input: `{ "text": "1 2 4 8 16", "mode": "series|image|auto" }`

Output (target): `{ "english", "purpose", "form", "confidence", "used_series", "used_image", "hypos" }`

Host today: `host/iki_think.cpp` in `sera5m/ikitaku`.

## Composition

Layer 5 verbs compose. Order matters. `cycle-add` is `loop n { var++ }`.
`add-cycle` is a different form. See `COMPOSITION.md`.

Viewer: `sera5m/ikitaku-galaxy`.
