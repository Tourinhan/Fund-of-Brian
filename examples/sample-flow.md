# End-to-end example (100% fictional)

This example illustrates how the system chains screening → one-pager → Initial
Assessment for a made-up company, "NovaCardia" — it does not correspond to any real
company.

---

## Input

The user attaches a deck and says: *"I have a deck for this company, take a look."*

## Step 1 — Screening

The system:
1. Asks for the source type → the user answers "Sector event"
2. Reads `skills/deal-screening.md` and extracts from the deck:
   - **NovaCardia** — Spain (Valencia), a spinoff from a university cardiovascular
     research group
   - Product: remote post-discharge monitoring platform for cardiovascular
     patients, with predictive alerts
   - Traction: 3 public hospitals in a paid pilot, €85K ARR, 6 months of commercial
     history
   - Team: CEO who is a cardiologist (no prior exit), CTO with a background in
     biomedical signal processing, no CCO yet
   - Round: Seed, €1.8M target, €9M pre-money, no lead confirmed, two business
     angels with a healthcare track record already in
3. Applies the rubric from `skills/icp-definition.md`:

   | Dimension | Score | Reason |
   |---|---|---|
   | MOIC | 13/20 | Base case ~4x, depends on expansion to more hospitals — a non-guaranteed event |
   | Traction | 13/20 | €85K ARR with paid institutional pilots, still small scale |
   | Team | 8/15 | Strong founder-market fit (cardiologist CEO) but no prior exit and missing a CCO |
   | Sector | 13/15 | Exact core of the thesis — monitoring + healthcare infrastructure |
   | Co-investors | 4/10 | Only business angels, no VC lead confirmed |
   | Geography | 9/10 | Spanish with documented tech transfer |
   | Valuation | 7/10 | €9M post-money, estimated equity ~7% with the standard ticket |
   | **Total** | **67/100** | **Tier 2 — Watch soon** |

4. Creates the item in the pipeline (Tier 2, Watch soon) with the mapped fields
5. Adds the follow-up comment: *"NovaCardia (Valencia) — university spinoff,
   cardiovascular post-discharge monitoring. €85K ARR, 3 hospitals in paid pilot.
   Cardiologist CEO + technical CTO, missing a CCO. Seed €1.8M @ €9M pre, no lead
   yet. Score 67/100 — Tier 2, watch soon. Re-contact if they confirm a lead or
   MRR >€15K."*
6. Notes: *"This deal doesn't require updating the ICP — it fits the already
   defined criteria in a standard way."*

## Step 2 — Three months later: a revival signal

The founder writes in to announce a partnership with a private insurer and that a
European health fund is evaluating leading the Seed round.

The system, following `skills/fund-intelligence.md`:
1. Identifies the signal as **strong** (a reference co-investor evaluating + a new
   institutional partnership)
2. Recalculates: +20 pts (partnership) — the score rises to 87/100
3. Flags the company for an immediate review for a Tier 1 upgrade
4. Updates the status in the watchlist and recommends moving to Reviewing

## Step 3 — Review: one-pager

With the founder call already done and a partial data room available, the system
generates the one-pager following `skills/deal-analysis.md`, explicitly including
in the "Why NOT" section: *"The team still has no CCO — current traction depends on
the CEO closing pilots personally, which doesn't scale beyond 5-6 hospitals without
dedicated commercial hiring."*

## Step 4 — Analysis: Initial Assessment

After the OK from all 3 partners at the meeting, the partner lead requests the
first iteration of the Initial Assessment. The system builds on the approved
one-pager, and identifies as the main blocker: *"Confirm whether the insurer
partnership includes a volume commitment or is just an uncommitted pilot — this
materially changes the traction case."*

---

*End of example. All data, names, and figures are invented to illustrate the
system's flow.*
