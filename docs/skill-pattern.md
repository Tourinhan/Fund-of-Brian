# The pattern: skills as operational knowledge

## The problem with a monolithic system prompt

The naive approach to "giving an LLM business context" is to dump everything into a
single prompt: investment criteria, workflows, decision history, all together. This
fails in practice for several reasons:

1. **It's not safely editable.** If a scoring criterion changes, someone has to find
   and edit the right block within a giant piece of text, risking breaking something
   else unintentionally.
2. **It doesn't distinguish who can change what.** A monolithic prompt has no notion
   of "the system updates this after learning something new" vs. "only the fund's
   partners change this."
3. **It's not auditable.** There's no way to know when a criterion changed or why,
   unless someone maintains a separate changelog — which in practice nobody does.
4. **It mixes definition with execution.** "What makes a good deal" and "how do you
   execute the screening of a deal" are different questions with different change
   cycles — the definition changes a few times a year, execution gets adjusted
   constantly with small learnings.

## The alternative pattern: files with their own owner and lifecycle

Each piece of knowledge lives in its own file, with:

- **A single, explicit purpose** (see the header of each skill in this repo: "use
  this skill for...")
- **Explicit access rules** — some files are read-only for the model (e.g.
  `icp-definition.md` in its "official" form is only edited by the human team when
  they decide to change the investment criteria), others get updated by the system
  itself after each cycle (e.g. the watchlist inside `fund-intelligence.md`)
- **A versioned learning history at the end of the file** — every time a nuance is
  discovered or a criterion is corrected, a row gets added with date and reason:

  ```markdown
  | Date | Learning |
  |---|---|
  | Jun 2026 | Category X only applies to already-diagnosed conditions; preventive platforms → a different category |
  | Jul 2026 | Correction: category Y is not limited to patient-facing products — it applies equally to B2B solutions |
  ```

  This is the key difference from "editing the prompt": the previous criterion
  doesn't disappear without a trace. It stays documented *that* it existed, *why* it
  was changed, and *when* — useful both for auditing past decisions and for the
  model itself to understand the reasoning behind the current rule, not just the
  rule in isolation.

## Separating definition from execution

In this system:
- `icp-definition.md` answers **"what is a good deal?"** — the most stable layer,
  changes a few times a year
- `deal-screening.md` / `deal-analysis.md` answer **"how do I execute each stage of
  the process?"** — these change more often, every time an operational nuance is
  learned (e.g. how to map a specific CRM field, what to do when data is missing)
- `fund-intelligence.md` answers **"what do I do with what I already evaluated and
  didn't move forward?"** — it lives on its own time cycle (monthly/weekly),
  separate from the initial evaluation cycle

This separation matters because it lets the team edit one aspect of the system
without touching the others, and lets the model know which file to consult based on
the type of question — not all knowledge is relevant to every task.

## Golden rule applied in this system: absence of data ≠ negative conclusion

A concrete example of why this level of detail in the skills matters: the system has
an explicit rule stating that if an automated search finds no public information
about a company, **that is not the same as classifying it as "interesting but too
early."** These are different judgments:

- "I found no information" = a limit of the search method
- "It's Tier 3 (interesting but too early)" = a positive conclusion that requires
  evidence

Without this distinction documented explicitly as a rule in the skill, a search
failure (generic name, typo in the source list) could silently translate into a
classification that, under the system's own decay rules, ended up in automatic
rejection after 12 months without anyone reviewing it. This kind of rule — born from
an observed real case — is exactly what goes into the corresponding skill's learning
history, so it doesn't happen again.

## Summary

The pattern isn't "prompt engineering" in the sense of finding the magic phrase — it
is knowledge system design: what lives where, who edits it, how the change gets
audited, and how the parts that change at different rates get separated.
