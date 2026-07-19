# skills/deal-screening.md — Deal Screening Guide

> This file documents the logic and criteria learned during the process of
> screening companies for the fund's pipeline. Update after every relevant
> iteration.

---

## What screening is

Screening is the first phase of the investment funnel. Its goal is to quickly
register a company in the CRM with the correct fields so the team can follow up.

**It does not generate any analysis** — that belongs to Review and Analysis.
Screening only classifies and registers.

There are two screening modes, depending on the available input:

- **Mode A — With a deck**: full flow below.
- **Mode B — Without a deck** (e.g. exhibitor/contact lists from an event, only
  name + country): see dedicated section.

### Full flow (Mode A — with deck)

1. A deck (PDF) is received
2. The system asks for the source type and the source
3. It analyzes the deck and extracts the fields
4. It creates the item in the pipeline with all the fields
5. It adds the follow-up comments to the item
6. The deck is attached manually to the document repository

---

## Mode B — Screening without a deck (name + country only)

Applies when a list of companies is received (e.g. exhibitors from an event) with no
deck attached.

**Process:**

1. Register the item with the available fields: name, country, responsible analyst,
   source type, source.
2. Run **1 targeted web search** per company. If the name is generic and brings back
   noise from unrelated namesakes, discard those results instead of forcing a
   classification with them.
3. With what's found, fill in whatever fields are possible following the same
   classification criteria as in Mode A. **Leave blank what can't be found — never
   invent.**
4. Add an **estimated Tier / score**, explicitly marked as a partial estimate given
   the missing deck.
5. Follow-up comment: same format and level of detail as Mode A, with no method
   prefixes or classification recaps that are redundant with the CRM's columns.
6. If the search turns up nothing useful: leave the comment as "no relevant public
   information found — pending deck or direct contact" and don't force any
   classification.

**Efficiency note:** generic or short company names tend to return mostly irrelevant
results — one well-targeted search is enough; if nothing clear turns up, move on to
the next item.

### Rule: absence of public information does NOT equal Tier 3

**"I found no information" and "Tier 3" are different judgments and must not be
conflated.**

- **Tier 3** is a positive, qualitative claim: the company exists, there's some
  information available, and it fits the "interesting but premature timing" pattern.
  It requires minimal evidence to hold up.
- **"No public information"** is a gap in evidence, not a data point. It's usually
  due to limitations of the search method itself (a generic name, a single search
  for efficiency, a transcription error in the source list) — not necessarily
  because the company lacks real traction.

**Why this matters especially here:** per `fund-intelligence.md`, a Tier 3 company
that shows no signal within 12 months gets an **automatic Pass with no human
review**. If "no information" defaults to Tier 3, a search failure can silently kill
a potentially good deal without anyone reviewing it.

**How to proceed instead:**

1. **Generic or ambiguous name** (multiple unrelated namesakes, inconclusive result)
   → don't score. Leave the standard "no information — pending deck or direct
   contact" comment, with no Tier assigned.
2. **Specific, unambiguous name, and still no real digital footprint at all** (no
   website, no LinkedIn, no press/directory mention) → that total absence is itself a
   signal, but it points more toward **Anti-ICP** ("pre-product with no traction and
   no real market signal") than Tier 3, which by definition implies a positive
   assessment ("interesting, but early") that can't be sustained without data. Even in
   this case, mark it explicitly as a very low-confidence estimate, not a firm
   classification.
3. In both cases, the default goal remains **don't force any classification** unless
   case 2 is unambiguous.

---

## ICP classification (operational summary)

### Tier 1 — Supernova
Meets return, equity/valuation, sector, geography, traction, team, and co-investor
criteria per `skills/icp-definition.md`.

### Tier 2 — Partial fit
Meets sector + geography + team but is missing traction, co-investors, reasonable
valuation, or sufficient return.

### Anti-ICP — Discard
Pre-product with no traction, team with no relevant background, pure B2C with no
institutional channel, insufficient equity with no room to negotiate, no possibility
of a board seat, geography outside the mandate, direct competition with no
technological edge, or excessive dependence on a single client.

---

## Field classification criteria (generic example)

These criteria are simplified relative to the real system — the goal is to show the
*type* of nuance a classification system needs to document, not the complete field
mapping for any specific CRM.

### Therapeutic category vs. support platform

A recurring distinction in Digital Health: a solution that **digitally treats an
already-diagnosed condition** (e.g. an app for managing a diagnosed chronic disease)
is one case; a **preventive or support platform with no direct therapeutic
component** is another, even though both can look similar at first glance.

**Important nuance learned**: the support/preventive platform is not limited to
patient-facing products — a 100% B2B solution (for doctors, pharma, insurers, other
healthtech companies) can still be a "support platform" as long as it doesn't treat
a diagnosed condition. What defines the category is the absence of treatment for a
diagnosed condition, not who the end user is.

### Process automation vs. data management

Another frequent point of confusion, both "B2B / infrastructure" but distinct:
- An assistant that automates a *task* (documenting a consultation, scheduling,
  regulatory compliance) → process automation.
- A solution that works on the *data* itself — structuring it, connecting it across
  systems, harmonizing it → data management and interoperability.

Practical signal: if the pitch talks about "unlocking/structuring/harmonizing data,"
"interoperability," "dataset" → data management. If it talks about
"automating/streamlining a task" → process automation.

### Medical specialty

Maximum two labels per company, never three or more — avoids diluting the
classification.

### Funding stage

| Stage | Criterion |
|---|---|
| Pre-seed | Basic MVP with no pilots, no traction, no revenue |
| Seed | First pilots or incipient revenue |
| Bridge Seed→Series A | Traction but needing more capital to scale |
| Series A | Demonstrable traction and scaling |

---

## Creating the follow-up record

After creating the item in the CRM, it is mandatory to create the follow-up
comment/update with the summary: what the company does · traction · team · round
status · Tier.

**Format — substance only**: straight to the content, with no method prefixes (e.g.
don't mention whether it was "Mode A" or "Mode B" in the text) or classification
recaps already reflected in the CRM's structured fields — that's redundant noise.

---

## Learning history

| Date | Learning |
|---|---|
| T-12m | Therapeutic vs. preventive distinction: the therapeutic category only applies to already-diagnosed conditions |
| T-12m | Medical specialty: max 2 labels, never 3 |
| T-6m | Added Mode B: screening without a deck. 1 targeted search per company, fill in only what's found, Tier marked as a partial estimate, no invented data |
| T-1m | The follow-up comment goes straight to substance — no method prefixes or recaps redundant with the CRM columns |
| T-1m | Explicit rule: absence of public information does NOT equal Tier 3. Generic/ambiguous name → don't score; specific name with no real digital footprint at all → consider Anti-ICP (not Tier 3), and only as a low-confidence estimate |
| T-2wk | Important correction: the "support platform" category is not limited to patient-facing products — it applies equally to B2B solutions as long as they don't treat a diagnosed condition |
| T-2wk | Added the distinction between process automation and data management/interoperability as separate categories |
