# End-to-end example (100% fictional)

This example illustrates how the system chains screening → one-pager → Initial
Assessment for a made-up company, "Cortavia" — it does not correspond to any real
company.

---

## Input

The user attaches a deck and says: *"I have a deck for this company, take a look."*

## Step 1 — Screening

The system:
1. Asks for the source type → the user answers "Sector event"
2. Reads `skills/deal-screening.md` and extracts from the deck:
   - **Cortavia** — Spain (Valencia), a spinoff from a university cardiovascular
     research group
   - Product: remote post-discharge monitoring platform for cardiovascular
     patients, with predictive alerts
   - Traction: 3 public hospitals in a paid pilot, €85K ARR, 6 months of commercial
     history
   - Team: CEO who is a cardiologist (no prior exit), CTO with a background in
     biomedical signal processing, no CCO yet
   - Round: Seed, €1.8M target, €9M pre-money, no lead confirmed, two business
     angels with a healthcare track record already in
3. Applies the model from `skills/icp-definition.md`:

   **Base score (7 weighted categories, each scored 1–10):**

   | Category | Score | Weight | Points | Reason |
   |---|---|---|---|---|
   | Team | 6/10 | 30% | 18 | Strong founder-market fit (cardiologist CEO) but no prior exit and missing a CCO |
   | Opportunity size | 7/10 | 25% | 17.5 | Real institutional market, expansion path plausible but unproven beyond 3 hospitals |
   | Product & IP | 6/10 | 15% | 9 | Predictive alerts add real differentiation, no filed IP yet |
   | Business model | 6/10 | 10% | 6 | Pilot-based revenue, scalable model not yet proven at more sites |
   | Traction | 6/10 | 10% | 6 | €85K ARR with paid institutional pilots, still small scale |
   | Competitors | 5/10 | 5% | 2.5 | Moderately competitive monitoring space, no clear moat yet |
   | Round economics | 5/10 | 5% | 2.5 | €9M pre-money, ~7% equity with standard ticket, no lead confirmed |
   | **Base score** | | | **61.5** | |

   **Moat multiplier (4 moats, scored 1–10 on credibility of path):**

   | Moat | Score | Reason |
   |---|---|---|
   | Intangible assets | 5 | Some IP potential in the prediction algorithm, unproven |
   | Switching costs | 6 | Once integrated into hospital care pathways, credible lock-in |
   | Network effects | 2 | One-sided monitoring product, no multi-sided dynamic |
   | Cost advantages | 3 | No meaningful scale economics at this stage |

   Average = 4.0 → multiplier = 0.75 + (4.0 − 1)/12 = **1.00x**

   **Final score = 61.5 × 1.00 = 61.5 → Tier 2, Watch soon**

4. Creates the item in the pipeline (Tier 2, Watch soon) with the mapped fields
5. Adds the follow-up comment: *"Cortavia (Valencia) — university spinoff,
   cardiovascular post-discharge monitoring. €85K ARR, 3 hospitals in paid pilot.
   Cardiologist CEO + technical CTO, missing a CCO. Seed €1.8M @ €9M pre, no lead
   yet. Score 61.5 — Tier 2, watch soon. Re-contact if they confirm a lead or
   MRR >€15K."*
6. Notes: *"This deal doesn't require updating the ICP — it fits the already
   defined criteria in a standard way."*

## Step 2 — Three months later: a revival signal

The founder writes in to announce a partnership with a private insurer and that a
European health fund is evaluating leading the Seed round.

The system, following `skills/fund-intelligence.md`:
1. Identifies the signal as **strong** (a reference co-investor evaluating to lead +
   a new institutional partnership)
2. Re-scores the categories the signal actually changes — it doesn't add flat
   points to the old total, since the score isn't additive anymore:
   - **Team** 6→9 (a credible lead evaluating the round raises confidence in the
     founders' ability to close quality backers)
   - **Traction** 6→8 (an institutional insurer partnership is a materially
     stronger signal than pilot-stage hospital contracts)
   - **Opportunity size** 7→8 (the insurer channel plausibly expands reach beyond
     direct hospital sales)
   - **Business model** 6→7 (the partnership validates a second monetization path)
   - Switching costs moat nudges 6→7 (an insurer relationship further embeds the
     product into the care pathway)
   - Everything else unchanged
3. New base score: Team 27 + Opportunity size 20 + Product&IP 9 + Business model 7
   + Traction 8 + Competitors 2.5 + Round economics 2.5 (unchanged) = **76.0**. New
   moat average (5+7+2+3)/4 = 4.25 → multiplier 0.75 + (4.25−1)/12 = **1.0208x**.
   Final score = 76.0 × 1.0208 ≈ **77.6 → crosses into Tier 1**
4. Flags the company for an immediate review for a Tier 1 upgrade — the recalculated
   score, not the original one, is what triggers the flag
5. Updates the status in the watchlist and recommends moving to Reviewing

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
