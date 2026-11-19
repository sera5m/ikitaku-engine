# Layer 5 composition

Ikitaku treats a concept as a differential polynomial over platonic
verbs. Order is part of the form. The space is non-commutative.

`cycle-add` is not `add-cycle`.

| form | outer | inner | reading |
|---|---|---|---|
| cycle-add | cycle | add | `loop n { var++ }` — accumulate on each pass |
| add-cycle | add | cycle | add once, then a loop that does not do that add |
| +cycle +add | cycle | add | compounding spiral: each pass appends |
| +cycle -add | cycle | invert(add) | depleting loop: each pass prunes |
| -cycle +add | invert(cycle) | add | rewind, then inject |
| -cycle -add | invert(cycle) | invert(add) | rollback |
| cycle xor add | cycle | wrap | modular add, ring buffer |

Signs are unary transforms on a verb, not arithmetic on the values
the verb touches.

## English mapping

English is a costume on these forms. A dictionary of verbs and nouns
can be projected onto layer 4 by asking a local model, for each word,
which layer 5 verbs it is made of and in what order.

Crude test that already works on an ordinary model:

```
user: what would cycle+add mean, with different signs
model: compounding spiral / depleting loop / rewind-and-patch / rollback / modular wrap
```

That is layer 4 generation from layer 5. The mapping is dubious until
it is checked against a fixed verb list and stored as edges, not prose.

## What to store

One row per word:

```json
{
  "word": "loop",
  "pos": "verb",
  "outer": "cycle",
  "inner": [],
  "sign": "+",
  "conf": 80,
  "source": "qwen2.5:7b"
}
```

Non-commutativity is the check: if the model says `cycle-add` and
`add-cycle` are the same, discard the row.
