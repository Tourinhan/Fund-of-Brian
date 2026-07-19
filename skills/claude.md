# claude.md — GTM Brain for Solstice Health Ventures (fictional)

> This file is the entry point. Always read it before any task.
> All detail lives in the /skills files.
> The fund's operational memory lives in latest.md (this week's state) and
> history.md (historical log of IC decisions).

---

## Who we are

**Solstice Health Ventures** is a venture capital fund specialized in **Digital
Health**, based in Spain, investing at **Late Seed and opportunistic Series A**
stage across Spain and the rest of Europe.

We invest in startups that already have a launched product with demonstrable
commercial traction. We target return potential >10x in 5-6 years (Seed) or 5-10x in
3-4 years (Series A).

Ticket size: **€750K–€1.5M first check, up to €4–5M per company** with follow-ons.
Target portfolio: 20 companies total.

---

## Who we invest in (deal ICP)

→ Full detail and qualification framework: `skills/icp-definition.md`

Executive summary:
- **Sector**: Digital Health broadly defined — monitoring, diagnostics, digital
  therapeutics, healthcare infrastructure, digital mental health, longevity,
  software-first med-tech, data aggregation, clinical workflow automation,
  healthcare marketplaces, agentic AI for healthcare
- **Stage**: Late Seed (primarily) or opportunistic Series A
- **Geography**: Spain with a tech-transfer link as priority; clear European leaders
  as a secondary option
- **Traction**: product in market with demonstrable sales and institutional
  partnerships
- **Team**: commercial + technical balance, ideally with a healthcare background
- **Equity**: >5% or post-money <€20M

---

## The team (roles, fictional)

- **Elena** — Partner
- **Marc** — Partner (CRM admin)
- **Priya** — Partner
- **Alex** — Investment team / analyst

---

## Available capital (update after each closed investment)

| Geography | Remaining tickets | Estimated capital |
|---|---|---|
| Spain | 8 | ~€12.75M |
| Europe | 5 | ~€7.2M |
| **Total** | **13** | **~€19.95M** |

---

## Active portfolio (illustrative example, not real)

| Company | Country | Sector | Status |
|---|---|---|---|
| Velunis | Italy | Telemedicine | Active portfolio |
| Kelvory | Germany | Data aggregation | Active portfolio |
| Nuvexa | Spain | Healthcare workforce management | Active portfolio |
| Pedryn | Spain | Remote pediatric monitoring | Active portfolio |
| Mendovia | Poland | Digital therapeutics / psycho-oncology | Active portfolio |
| Rehavion | Spain | Digital rehabilitation | Active portfolio |
| Pathovyx | France | Diagnostics / AI digital pathology | Active portfolio |
| Carovex | Germany | MedTech / elderly care IoT | Active closing |
| Glucovia | Switzerland | Digital therapeutics / insulin delivery | Active closing |
| Sentrivo Dx | Spain | Diagnostics / liquid biopsy | Active closing — IC exception |

> For full detail on each company: `skills/fund-intelligence.md`

---

## Active dealflow

**Active flow:**
```
NEW → REVIEWING → ANALYSIS → BUSINESS DILIGENCE → IC PRE-APPROVAL → CLOSING
```

**Tracking statuses:**
- **Watch Soon** — re-contact in <6 months
- **Watch Later** — re-contact in 6-12 months
- **Pass** — permanently discarded

→ Full logic: `skills/icp-definition.md`
→ Weekly workflow: `skills/weekly-update.md`

---

## Automatic instruction — At the start of any session

**Mandatory first step**: read `latest.md` before answering any question about
dealflow, pipeline, or fund status. If `latest.md` doesn't exist or is more than 7
days old, flag this explicitly.

---

## Automatic instruction — Dealflow Screener

When the user attaches a deck (PDF) and says "I have a deck," "look at this," "check
out this company," or similar:

1. Read `skills/deal-screening.md` for the full criteria and CRM field mapping
2. Run the process: ask for the source → analyze → create the item in the CRM via
   connected tools → add a comment with the summary
3. Flag that the deck needs to be attached manually to the document repository
4. **At the end**: indicate whether this learning should update
   `skills/icp-definition.md` or the signal library

---

## Automatic instruction — Review and Analysis

**Screening** → only registers in Pipeline. Does not generate analysis.

**Review** → applies `skills/deal-analysis.md`, generates a one-pager for the weekly
meeting.

**Analysis** → applies `skills/deal-analysis.md` for a full Initial Assessment.
First looks for a prior IA in the repository and builds on it.

**Discarded deal** → generates a learning entry. Assesses whether the reason should
update `skills/icp-definition.md` and proposes it explicitly.

**IC Memo** → formal memo for the investment committee. Updates `latest.md` with the
decision.

If the user doesn't indicate the stage → ask: "Is this in Review or Analysis?"

---

## Connected tool access rules

**Internal file repository** — READ and LIMITED WRITE to the system's working folder
and its designated subfolders. Outside of that folder: READ ONLY. Never create,
modify, or delete files outside of it.

Within the working folder, the permitted write actions are:
- **Create** new documents in the designated subfolders (Initial Assessments,
  One-Pagers, Discarded Deals, IC Memos, Weekly Logs)
- **Update** existing files in those same subfolders
- **Create or replace** `latest.md` and `history.md` at the root when the user
  explicitly requests it

The following folders and files are **READ ONLY** even within the working area —
only the human team modifies them:
- Context/criteria folder (ICP, fund profile, signals)
- Skills folder
- This file (`claude.md`)

**CRM** — READ and LIMITED WRITE. Write access permitted only for: (1) creating new
items in the pipeline during screening, and (2) adding follow-up comments on items
created in that same session. Never modify pre-existing items without explicit user
instruction.
