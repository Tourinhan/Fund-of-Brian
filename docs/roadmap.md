# Roadmap

> Public version. The full internal document includes market analysis, financing
> strategy, and detailed go-to-market planning that isn't published — what follows
> is the vision, the phases, and the architecture principles behind them.

---

## Starting point

A VC fund specialized in Digital Health, late seed / Series A, building an
investment operating system on Claude (Anthropic) and monday.com since June 2026.

The first module in production is the **Dealflow Screener**: a flow that
automatically analyzes a startup's deck against the fund's ICP, classifies the
company, and creates the item in the Pipeline with all fields correctly filled.

Not a demo. A system tested in production, with real deals, real failures, and
real fixes.

## Starting constraint: solo build

This is being built solo, with no fixed calendar date per phase, until there's real
product validation — an external fund using the pipeline recurrently, with explicit
positive feedback. The technical co-founder joins after that validation, not
before. While working solo, there's only real bandwidth for one heavy-engineering
track at a time — everything else has to be either cheap to build (reuses something
that already exists) or scoping work a co-founder can execute fast once they arrive.

## Vision

Build the standard operating system for early-stage funds — starting with one real
fund as a lab. The competitive advantage isn't the technology (Claude is available
to anyone) but the operational knowledge: knowing exactly what flows a fund needs,
how deals get classified, which fields matter, where automation breaks and how it
gets fixed. That knowledge only comes from operating a real fund.

## Phase 0 — Preconditions

Resolve whatever would block commercializing the system the day that's decided: IP
ownership, corporate vehicle if billing third parties.

## Phase 1 — Solo core (in progress)

Goal: get the core pipeline to "IC-grade" — good enough to support a real
investment decision without a major rewrite.

**Track A — Pipeline core** (sequential, sole engineering priority):
1. Dealflow Screener ✅ in production
2. Review one-pager — automatic generation for the weekly dealflow meeting
3. Analysis / IC memo — full memo with red flags, questions for the team, capable
   of supporting an IC decision without a major rewrite

**Track B — Fund intelligence** (parallel, low cost — reorganizing data that
already exists, not new engineering):
- History of discarded and approved deals, with explicit scoring and decay
- Portfolio Management — the post-investment mirror of Dealflow Meetings (board
  reasoning, metrics, risks, milestones)

End of Phase 1 = Track A at IC-grade and Track B with the historical archive fully
structured. No calendar date — a quality bar.

## Phase 2 — Adoption expansion

Use the now-mature Phase 1 pipeline as the credibility base to open up LP and
portfolio reporting — the easiest cold-sell angle to a second or third fund that
doesn't yet trust the system's judgment.

Compliance (SOC 2, RBAC, multi-fund segregation) gets scoped in this phase, not
built — that's heavy engineering that waits for the technical co-founder.

## Phase 3 — With a co-founder (post-validation)

Multi-CRM (the fund picks its stack, the system adapts), multi-sector (configurable
ICP and workflows), real compliance, external data integrations, and the start of a
network-effects layer: aggregated, anonymized benchmarking across funds using the
system — each new fund improves the signal for the ones already on it. Worthless
below a minimum number of contributing funds, so it doesn't launch commercially
before that threshold.

## Phase 4 — Platform + Exit Prediction

Goal: close the full loop of a fund's business, with exit prediction as the
flagship module — conditional on the multi-fund data volume accumulated in Phase 3,
not on a calendar date.

Upsell modules: LP Relations, Fundraising Kit, Co-investor Network (aggregated,
historical — never live pipeline), Fund Analytics.

## Why build it this way

The problem is universal — thousands of early-stage VC and PE funds run on the same
chaos: disorganized dealflow, inconsistent analysis, institutional knowledge that
disappears when an analyst leaves. Established CRM players own the relationship
layer, not the analytical judgment layer. The moat is operational knowledge
encoded deal by deal, reinforced by aggregated data once the network-effects layer
exists — until then it's a softer, more replicable moat, and that's a deliberately
honest statement about where the project stands today.

## The architecture that makes it possible

The engine (workflows, document generation, CRM integration) is generic; domain
knowledge (ICP, signals, fields, classification logic) lives in swappable
configuration files. A fund in a different sector should be able to onboard by
configuring its own `CLAUDE.md` and `skills/`. The engine doesn't change — the
context does.

## Cross-cutting architecture rule: single source of truth

A direct lesson from production, not a theoretical one: a module kept its own table
of watchlist company status for weeks, in parallel to the real status in the CRM.
It drifted out of sync without anyone noticing — the system flagged it week after
week and nobody fixed it, because hand-correcting a doc isn't a sustainable process.

Resulting rule, applies to every future module that tracks state: no file or module
should cache a value that the source system already maintains as live truth. It
gets queried, never copied. The only thing a module can keep on its own is
knowledge no other system holds — reasoning, objections, qualitative checkpoints.

## Current stack

| Layer | Tool |
|---|---|
| AI | Claude (Anthropic) via Claude Projects |
| CRM | monday.com |
| Knowledge | MD files in the project (CLAUDE.md, skills/) |
| Automation | MCP connected to Claude |

---

*Last updated: July 2026 · public version*
