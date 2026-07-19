# GTM Brain — Agentic AI Ops for VC Dealflow

> **Note**: this repository is an architecture case study. All fund names, company
> names, people, and internal identifiers are fictional. The real system this is
> based on operates on confidential data belonging to a venture capital fund and is
> not published — what's documented here is the design, not the content.

---

## What this is

**GTM Brain** is an agentic AI ops system that connects an LLM (Claude) to the
operational tools of a venture capital fund — an internal file repository, a
CRM-type system, and Notion — to run the investment pipeline end to end: from
screening a new company to preparing the Investment Committee (IC).

It's not a chatbot with extra context. It's a layer of structured operational
knowledge (investment criteria, scoring rubrics, decay rules, workflows) plus a set
of connected tools, designed so the LLM executes complete tasks — not just answers
questions — with the same consistency a human analyst would bring to following the
fund's playbook.

## The problem it solves

A VC fund in an active investment phase processes a constant flow of companies —
inbound decks, events, referrals — and needs to:

1. **Classify fast** against an ICP (Ideal *Company* Profile, in this case) without
   burning partner time on companies that don't fit
2. **Keep scoring reproducible** — two analysts evaluating the same deal should reach
   similar conclusions
3. **Not lose opportunities** that don't fit *now* but might in 6-12 months (decay
   and revival tracking)
4. **Produce quality documentation** (one-pagers, Initial Assessments, IC memos)
   iteratively, without rewriting from scratch on every update
5. **Execute on the team's real tools** (CRM, file storage, communication) without
   friction from copying and pasting between systems

## Architecture

```
                    ┌─────────────────────────────────────┐
                    │         Knowledge layer                │
                    │  (skills/ — read at session start)      │
                    │                                        │
                    │  • Fund profile and mandate             │
                    │  • ICP definition + scoring rubric      │
                    │  • Workflows per funnel stage           │
                    │  • Decay / revival rules                │
                    │  • Versioned learning history            │
                    └───────────────┬───────────────────────┘
                                    │
                    ┌───────────────▼───────────────────────┐
                    │              LLM (Claude)               │
                    │   orchestrates reading + reasoning +    │
                    │   writing across connected tools         │
                    └───┬───────────────┬──────────────┬─────┘
                        │               │              │
                 ┌──────▼─────┐  ┌──────▼──────┐  ┌────▼─────┐
                 │  Internal    │  │  CRM (MCP)  │  │  Notion  │
                 │  Files       │  │  (pipeline, │  │ (founder │
                 │ (documents,  │  │  scoring,   │  │  notes,  │
                 │  IAs, memos) │  │  updates)   │  │data room)│
                 └──────────────┘  └─────────────┘  └──────────┘
```

See [`docs/architecture.md`](docs/architecture.md) for the detail of each layer.

## The core pattern: skills as operational knowledge, not loose prompts

Instead of one giant system prompt, the knowledge is organized into files (`skills/`)
that the model explicitly reads at the start of each session and consults depending
on the task. Each skill:

- Has a **clear owner** (some are editable by the system, others are read-only — only
  the human team modifies them)
- Includes a **versioned learning history** at the end — when the team corrects a
  criterion or discovers a nuance, it's documented with date and reason, not silently
  overwritten
- Separates **definition** (what the ICP is, what a Tier is) from **execution** (how
  to screen a deal, how to run the weekly review) — each lives in its own file

See [`docs/skill-pattern.md`](docs/skill-pattern.md) for the full reasoning behind
this design and why it works better than stuffing everything into a monolithic
prompt.

## What the system does in practice

| Funnel stage | What the Brain automates |
|---|---|
| **Screening** | Receives a deck or a list of companies → classifies against the ICP → scores with a 7-dimension rubric (0–100 pts) → creates the item in the CRM with all fields → adds the summary as a comment |
| **Review** | Generates the one-pager for the weekly meeting from deck + founder call, distinguishing verified data from assumption, without hiding red flags |
| **Analysis** | Builds the iterative Initial Assessment (10 sections) that grows with each new piece of information — Q&A with the team, data room, calls with co-investors |
| **IC prep** | Anticipates the toughest questions the committee will ask, with the founding team's likely answers and the main risks, without trying to "sell" the deal |
| **Fund Intelligence** | Tracks decay (waiting companies that have gone too long without a signal) and revival (emails, news, or recontacts that reactivate an opportunity) systematically, not ad hoc |

## Design principles applied

1. **Auditable scoring, not a black box**: the rubric breaks the decision down into 7
   weighted dimensions with concrete descriptive anchors — the goal is that two
   people evaluating the same deal land within ±5 points of each other, not that the
   model decides "just because."
2. **Absence of data ≠ negative data**: an explicit rule of the system is that "I
   found no public information" and "this company is low priority" are different
   judgments — conflating them can silently kill a valid opportunity just because the
   automated search found nothing.
3. **Honesty forced by design**: the output document format explicitly requires a
   "why NOT to invest" section with the standard of the strongest possible
   objection — not a generic filler list of risks.
4. **Knowledge gets corrected, not rewritten**: every skill file has a learning
   history at the end. When a criterion changes, a row gets added with date and
   reason — the previous criterion is never silently deleted.
5. **Explicitly scoped write access**: the system has very specific write permissions
   per folder/board (what it can create, what it can only read) — this prevents an
   agent with broad access from modifying something outside its responsibility.

## Where this is headed

This repository documents **Phase 0**: the dealflow core (screening → review →
analysis → IC prep). It's the first module of a broader idea — an operating layer
for how an early-stage fund runs, not just how it sources deals.

The architecture is deliberately split so that the same pattern — domain knowledge
in swappable skill files, a general-purpose engine underneath — can extend to
adjacent fund workflows once the dealflow core is solid, without redesigning the
system from scratch:

- **Fund Intelligence workflows** (partially covered here already) extending toward
  LP communication — quarterly updates, standardized portfolio metrics reporting
- **Portfolio company tracking** post-investment — the same structured, auditable
  approach applied to monitoring companies after the check is wired, not just
  screening them before

Neither of these is built yet. They're the natural next step once the dealflow core
is mature — the same way a tool built to solve one workflow well often turns out to
be the seed of something that connects a fund's entire operating cadence, not just a
single task. The point isn't automating one thing in isolation; it's building the
connective tissue so institutional knowledge compounds instead of resetting with
every new hire or every new tool the team adopts.

## Stack

- **LLM**: Claude, via Claude Projects (persistent context) + MCP for connected tools
- **CRM**: via MCP — GraphQL for mutations not covered by the native tool
- **Documents**: internal file repository via MCP — root folder with write
  permissions scoped to specific subfolders
- **Founder notes / shared data rooms**: Notion via MCP
- **Long document generation**: Python/Node to build `.docx` files with the fund's
  house format (Initial Assessments, IC memos)

## Try it yourself

The scoring rubric described in `skills/icp-definition.md` isn't just prose — it's
precise enough to run. [`tools/icp_scorer.py`](tools/icp_scorer.py) is a small,
dependency-free Python script that implements the same 7-dimension rubric and scores
four fictional example deals, one per tier:

```bash
python3 tools/icp_scorer.py
```

```
============================================================
MedFlow Analytics (Tier 1 example)
============================================================
  Return potential (MOIC)      20/20  ████████████████████
    └─ Base case clears the fund's top band with a validated exit point.
  Commercial traction          19/20  ███████████████████░
    └─ ARR >€500K, growing >100% YoY, churn <5% — top band.
  ...
  TOTAL                        95/100
  TIER                         Tier 1 — Supernova
```

See [`tools/README.md`](tools/README.md) for usage details.

## Repository structure

```
skills/                  The 6 operational knowledge files (sanitized)
├── claude.md             Entry point — who we are, tool access rules
├── icp-definition.md     ICP definition + 7-dimension scoring rubric
├── deal-screening.md     Screening workflow (with and without deck) + CRM field mapping
├── deal-analysis.md      Full Review → Analysis → IC workflow
├── fund-intelligence.md  Decay tracking, revival detection, weekly intelligence
└── weekly-update.md      The team's weekly operating cadence

docs/
├── architecture.md       Detail of the architecture and data flow between layers
└── skill-pattern.md       Why skills > monolithic prompt, with examples

examples/
└── sample-flow.md        An end-to-end flow with a 100% fictional company:
                           deck → screening → one-pager → Initial Assessment

tools/
├── icp_scorer.py          Runnable reference implementation of the scoring rubric
├── sample_deals.json      Example fictional deals (one per tier, 1 through 4)
└── README.md              Usage instructions
```

## Results (aggregated, not tied to specific deals)

- Cuts the time to produce a first-draft Initial Assessment from several hours to a
  single guided iteration session
- Reproducible ICP scoring across sessions — same deal, same inputs, stable score
  within a ±5 point range
- Zero deals lost to "we just forgot to follow up," thanks to explicit tracking of
  decay checkpoints
- Full traceability: every scoring decision and every criterion change is documented
  with a date and reason, not just kept in the analyst's head

---

*This repository is a technical/product portfolio piece. It does not represent or
contain information from any real investment fund.*
