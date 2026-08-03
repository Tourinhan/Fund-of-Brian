# Roadmap

> Public version. The full internal document includes market analysis, financing
> strategy, and detailed go-to-market planning that isn't published — what follows
> is the vision, the phases, and the architecture principles behind them.

---

## Starting constraint: solo build

This has been designed, built, and operated solo — no dedicated engineering
resource, no co-founder. The phase structure below isn't a funding roadmap; it's a
map of what needs to be true operationally before more scope makes sense, given
that constraint. While operating solo, only one heavy build track gets full
attention at a time — everything else has to reuse what already exists or wait for
more capacity, whatever form that takes later.

## Vision

An operating system for how an early-stage fund actually runs its dealflow — not a
set of scripts, a system: connected knowledge, workflows, and tools that hold up
under real use, expanding in scope as the operational foundation proves itself.
Built and operated by one person as both architect and operator — the fastest way
to learn what a fund actually needs is to run one.

## Phase 0 — Preconditions

Whatever needs resolving before scope expands beyond one fund: IP ownership,
appropriate structure if this ever serves more than one fund at once.

## Phase 1 — Core pipeline — ✅ in production

Track A (Dealflow Screener, Review one-pager, Analysis / IC memo) and Track B
(Fund Intelligence — decay tracking, revival detection, historical archive) are
both live and in active use, not prototypes.

## Phase 2 — Adoption expansion — 🔧 in construction (current work)

Use the now-proven Phase 1 pipeline as the credibility base to open up LP and
portfolio reporting — the natural next layer once the core pipeline is trusted
enough to be worth a second fund's attention.

Compliance (SOC 2, RBAC, multi-fund segregation) gets scoped in this phase, not
built — real engineering work that waits for more capacity than one person has.

## Phase 3 — Multi-fund, multi-sector — gated on capacity, not calendar

Multi-CRM (the fund picks its stack, the system adapts), multi-sector (configurable
ICP and workflows), real compliance, external data integrations, and the start of a
network-effects layer: aggregated, anonymized benchmarking across funds using the
system — each new fund improves the signal for the ones already on it. Worthless
below a minimum number of contributing funds, so it doesn't launch commercially
before that threshold. This phase needs engineering bandwidth beyond one person —
whatever shape that takes.

## Phase 4 — Platform + Exit Prediction

Goal: close the full loop of a fund's business, with exit prediction as the
flagship module — conditional on the multi-fund data volume accumulated in Phase 3,
not on a calendar date.

Upsell modules: LP Relations, Fundraising Kit, Co-investor Network (aggregated,
historical — never live pipeline), Fund Analytics.

## Why build it this way

The underlying problem isn't specific to one fund: dealflow gets disorganized,
analysis quality depends on who happens to be doing it that week, and institutional
knowledge disappears when an analyst leaves. Generic CRM tools handle the
relationship layer well; they don't encode how a specific fund actually judges a
deal. That judgment only gets captured by running a real fund and building the
system around what actually happens — not by designing it in the abstract first.
Whether this stays a personal operating system or becomes something else later is
an open question; the architecture doesn't require deciding that now.

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
