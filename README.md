# GTM Brain — Agentic AI Ops for VC Dealflow

> **Note**: this repository is an architecture case study. All fund names, company
> names, people, and internal identifiers are fictional. The real system this is
> based on operates on confidential data belonging to a venture capital fund and is
> not published — what's documented here is the design, not the content.

> **Status (jul 2026)**: Fase 1 complete and in production — the full pipeline
> (Screening, Review, Analysis/IC memo) and Fund Intelligence are live and in
> active use, solo-built and solo-operated. Fase 2 (LP + Portfolio reporting) is
> the current work in construction. See
> [`docs/roadmap.md`](docs/roadmap.md) for the full picture.

---

## What this is

**GTM Brain** is an agentic AI ops system that connects an LLM (Claude) to the
operational tools of a venture capital fund — an internal file repository, a
CRM-type system, and Notion — to run the investment pipeline: from screening a new
company toward preparing the Investment Committee (IC). No oracle, no crystal ball —
just a system that reads what the fund already knows and applies it consistently.

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
                 ┌───────────────────────────────────┐
                 │          Knowledge layer          │
                 │ (skills/ — read at session start) │
                 │                                   │
                 │    • Fund profile and mandate     │
                 │ • ICP definition + scoring rubric │
                 │   • Workflows per funnel stage    │
                 │      • Decay / revival rules      │
                 │   • Versioned learning history    │
                 └───────────────────────────────────┘
                                   │
          ┌────────────────────────────────────────────────┐
          │                  LLM (Claude)                  │
          │       orchestrates reading + reasoning +       │
          │         writing across connected tools         │
          └──┬─────────────────────┬─────────────────────┬─┘
             │                     │                     │
   ┌─────────▼────────┐  ┌─────────▼────────┐  ┌─────────▼────────┐
   │  Internal Files  │  │    CRM (MCP)     │  │      Notion      │
   │   (documents,    │  │    (pipeline,    │  │ (founder notes,  │
   │   IAs, memos)    │  │scoring, updates) │  │    data room)    │
   └──────────────────┘  └──────────────────┘  └──────────────────┘
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

## What the system does today

| Funnel stage | Status | What the Brain does |
|---|---|---|
| **Screening** | ✅ In production | Receives a deck or a list of companies → classifies against the ICP → scores it → creates the item in the CRM with all fields → adds the summary as a comment |
| **Review** | ✅ In production | Generates the one-pager for the weekly meeting from deck + founder call, distinguishing verified data from assumption, without hiding red flags |
| **Analysis / IC prep** | ✅ In production | Builds the iterative Initial Assessment (10 sections); anticipates the toughest IC questions with the team's likely answers and the main risks |
| **Fund Intelligence** | ✅ In production | Runs decay/revival tracking on active watchlist entries systematically, not ad hoc; historical archive of past discarded/approved deals structured with scoring and decay |

"IC-grade" here means: good enough to support a real investment decision without a
major rewrite by a partner — the bar Fase 1 was built to clear before moving on to
Fase 2.

## Scoring model

The rubric weighs 7 categories, each scored independently, then applies a
multiplier derived from 4 qualitative moats — not as extra additive categories
(which would double-count against Product & IP and Competitors), but as a modifier
on the base score.

| Category | Weight |
|---|---|
| Team | 30% |
| Opportunity size | 25% |
| Product & IP | 15% |
| Business model | 10% |
| Traction | 10% |
| Competitors | 5% |
| Round economics | 5% |

The 4 moats (Dorsey framework: intangible assets, switching costs, network effects,
cost advantages) are each scored 1–10 on the **credibility of the path** to that
moat — not whether it exists today. Their average maps linearly to a multiplier
between 0.75x (average 1) and 1.50x (average 10):
`multiplier = 0.75 + (average − 1) / 12`.

Final score = Base score × Moat multiplier. This uncaps the scale above 100 by
design (a strong base with strong moats can exceed it) — tiering reads the
thresholds as minimums, not closed ranges.

**Scope**: this model applies to pre-seed through Series A. The weighting (Team +
Opportunity size = 55% of the base) assumes there isn't much operating data yet to
judge. For Series B, the system deliberately shows no computed score — financial
due diligence replaces the scorecard at that stage.

See [`skills/icp-definition.md`](skills/icp-definition.md) for the full rubric with
anchors and calibration examples.

## Design principles applied

None of these are aspirational. Each one exists because something broke without it.

1. **Auditable scoring, not a black box**: the rubric breaks the decision down into
weighted, independently-scored dimensions with concrete anchors — the goal is that
two people evaluating the same deal land within a few points of each other, not
that the model decides "just because."
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
6. **Single source of truth, no cached state**: no file in the system stores a
value that a connected tool (the CRM) already tracks live — it's queried, never
copied. This came from a real production failure: a status table lived in two
places, drifted apart over several weeks, and kept getting flagged without being
fixed, because hand-correcting a doc isn't a sustainable process. Every module now
either reads live from the source of truth or stores only what no other system
holds (reasoning, objections, checkpoints).

## Stack

- **LLM**: Claude, via Claude Projects (persistent context) + MCP for connected tools
- **CRM**: via MCP — GraphQL for mutations not covered by the native tool
- **Documents**: internal file repository via MCP — root folder with write
permissions scoped to specific subfolders
- **Founder notes / shared data rooms**: Notion via MCP
- **Long document generation**: Python/Node to build `.docx` files with the fund's
house format (Initial Assessments, IC memos)

## Repository structure

```
skills/                  The operational knowledge files (sanitized)
├── claude.md             Entry point — who we are, tool access rules
├── icp-definition.md     ICP definition + 7-category scoring rubric + moat multiplier
├── deal-screening.md     Screening workflow (with and without deck) + CRM field mapping
├── deal-analysis.md      Full Review → Analysis → IC workflow
├── fund-intelligence.md  Decay tracking, revival detection, weekly intelligence
└── weekly-update.md      The team's weekly operating cadence

docs/
├── architecture.md       Detail of the architecture and data flow between layers
├── skill-pattern.md      Why skills > monolithic prompt, with examples
└── roadmap.md            Where this is going, and what has to be true before each phase starts

examples/
└── sample-flow.md        An end-to-end flow with a 100% fictional company:
                           deck → screening → one-pager → Initial Assessment
```

## Where this is going

Fase 1 is done. The phases below are vision for what comes after — gated behind
explicit triggers, not calendar dates. Aspiration with a trigger attached, not a
promise with a date. Full detail, including why each trigger is what it is, in
[`docs/roadmap.md`](docs/roadmap.md).

- **Now (Fase 2, in construction)**: LP + Portfolio reporting, building on a
pipeline that's already proven itself in daily use.
- **Fase 3 (gated on engineering capacity beyond solo, triggered by the first
external fund using this recurrently)**: multi-CRM, multi-sector, real compliance,
data integrations.
- **Fase 4 (conditional on multi-fund data volume, not calendar)**: LP Relations,
Fundraising Kit, Co-investor Network, Fund Analytics, and exit-pattern signal as
the flagship module — only once there's enough aggregated data across funds for it
to mean something.

*(Mockups of the Fase 2/4 modules — Portfolio Management, LP Relations,
Fundraising Kit, Co-investor Network, Fund Analytics — exist as a design
prototype; screenshots below illustrate the direction, not shipped functionality.
Fund Intelligence itself is already live, not mocked up — see the status above.)*

<!-- Lovable screenshots go here -->

## Results (what's actually measurable today)

- The full pipeline — Screening through IC prep — goes from deck to a
partner-ready decision packet without starting from a blank page each time
- Reproducible ICP scoring across sessions — same deal, same inputs, stable score
- Systematic decay tracking: every watchlist company gets an explicit checkpoint
and expected signal instead of relying on someone remembering. This surfaces gaps —
it doesn't eliminate them by itself; someone still has to act on what the system
flags, and design principle 6 above exists because that didn't always happen in
practice
- Full traceability: every scoring decision and every criterion change is documented
with a date and reason, not just kept in the analyst's head

Fase 2 modules (LP Relations, Portfolio Management, and the rest) aren't claimed
here — those are 🔧, shown only as design direction above.

---

*This repository is a technical/product portfolio piece. It does not represent or
contain information from any real investment fund. Not a prophet. Just auditable.*
