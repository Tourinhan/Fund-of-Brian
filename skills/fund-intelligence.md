# skills/fund-intelligence.md — Fund Intelligence

> This skill defines how the system manages the lifecycle of opportunities beyond
> the initial screening: decay, revival, external signals, and follow-up. It's the
> foundation of the fund's long-term knowledge repository.

---

## What Fund Intelligence is

Fund Intelligence is the layer that makes sure no relevant opportunity gets lost.
Three main functions:

1. **Decay tracking** — every company has an implicit timeline depending on its
   tier. When that timeline is reached with no new signal, a decision needs to be
   made.
2. **Revival detection** — external signals (emails, news, recontacts) that
   reactivate an opportunity that was on hold or discarded (except Tier 4).
3. **Weekly intelligence** — a weekly summary of relevant ecosystem movements and
   pipeline status.

---

## Active watchlist (illustrative example)

> This table is the operational source of truth for decay. Update it the first
> Monday of every month or after any relevant event at a company.
> Companies in Analysis or IC have their own flow — they don't appear here.

| Company | Tier | CRM Stage | Checkpoint | Signal that would trigger a Tier 1 upgrade | Status |
|---|---|---|---|---|---|
| Northstar Learning | Tier 2 | Watch soon | Next Dec | Confirmed VC lead + recurring MRR >€50K | No update |
| CalmWave | Tier 2 | Watch soon | Next Dec | Pivot to B2B2C with European insurers | No update |
| FieldSense | Tier 3 | Watch later | Next Nov | European expansion + real ARR >€1M | No update |
| NeuroTrace | Tier 3 | Watch later | Next Oct | Round with quality co-investors + ARR >€500K | No update |
| PulseCheck | Tier 3 | Watch later | **Overdue** | Seed round with co-investors + confirmed tech transfer | No update — decide: Pass |

> ⚠️ Overdue = checkpoint has already passed. Requires an explicit decision to Pass
> or renew the checkpoint with justification.

---

## Monthly update protocol

Every first Monday of the month, the system reviews this table and, for each row,
assesses:
1. Has the upgrade signal arrived? → Update the tier, move to Analysis if
   appropriate.
2. Has the checkpoint passed with no signal? → Propose downgrading to Tier 3 or
   Pass to the responsible partner.
3. Is there a medium signal that doesn't reach the upgrade threshold? → Update the
   Status column, keep the tier.

---

## Decay rules by tier

| CRM stage | Expected action | No signal in… | Consequence |
|---|---|---|---|
| Watch soon | Active re-contact | 6 months | Review downgrade to Watch later or Pass |
| Watch later | Passive follow-up | 12 months | Automatic Move to Pass |
| Pass (Tier 1-3) | — | — | Can be reactivated if a strong signal arrives |
| Pass (Tier 4) | — | — | Never reactivated |

**Practical decay rule:** the checkpoint in the watchlist is the concrete
implementation of these timelines. There's no need to review the CRM every week —
just looking at the "Checkpoint" column of the table is enough.

---

## Weekly review protocol

Run every Monday. Estimated time: 15–20 minutes.

**The system runs these steps in order:**

### Step 1 — Review the watchlist
Has any checkpoint expired or is it expiring this week? → Flag for a decision.
Has any company had "No update" for more than 8 weeks? → Flag as a candidate for a
tier downgrade.

### Step 2 — Search for external signals
Search this week's inbox for emails from founders or co-investors related to
pipeline companies. For each email identified, assess the signal type (strong /
medium / weak) and act accordingly.

### Step 3 — Cross-check against active deals
For each deal in Analysis or IC: is there a blocker that should have been resolved
this week and hasn't been? Is there an upcoming IC or meeting date?

### Step 4 — Generate the weekly summary
1. Companies with an expired or upcoming checkpoint — decision required.
2. External signals detected this week and recommended action.
3. Upcoming critical dates for active deals.
4. A single priority recommendation for the week.

---

## Revival signals

**Strong signals (trigger an immediate tier review):**
- Founder re-contacts directly to announce a new round
- A reference co-investor brings the opportunity or mentions it positively
- Public announcement of a closed round
- Institutional partnership with a hospital, pharma company, CRO, or insurer

**Medium signals (update Status in the watchlist, review in the next cycle):**
- Founder shares a metrics update without mentioning a round
- Appearance in a relevant accelerator
- Mention in sector press
- New key team member

**Weak signals (log in the history if new; ignore if recurring):**
- Social media post with no substantial content
- Casual mention at an event with no concrete data

---

## Revival flow via email

When an email arrives from a founder or co-investor related to a pipeline company:

1. Identify the company by domain or name.
2. Look up the corresponding row in the watchlist.
3. Assess the signal type per the classification above.
4. If it's a strong or medium signal: update Status in the watchlist, update the
   Stage in the CRM if appropriate, add a comment with date/summary/recommended
   action, add it to the week's priorities.
5. If the company doesn't exist in either the CRM or the watchlist: create a new
   item, assign it to the responsible analyst, add a comment with the email's
   context, assess whether to add it to the watchlist based on the resulting tier.

---

## External signal scoring

| Signal | Base score | Decay |
|---|---|---|
| Reference co-investor brings the opportunity | +30 | 90 days |
| Round closed with a quality lead investor | +25 | 60 days |
| Partnership with a hospital or pharma company | +20 | 90 days |
| Participation in a top accelerator | +15 | 120 days |
| Appearance in sector press | +10 | 30 days |
| Direct re-contact from the founder | +10 | 30 days |
| Social media post with no substance | +2 | 7 days |

When a signal arrives about a watchlist company, add the points to the original ICP
score. If the new total exceeds the Tier 1 threshold (≥75 points) → review for a
tier upgrade immediately.

---

## Learning history

| Date | Learning |
|---|---|
| T-12m | Defined 4 tiers with explicit decay timelines (6m / 12m / Pass / Never) |
| T-12m | Tier 4 / Anti-ICP never gets revived — permanent rule |
| T-12m | Revival signals classified into strong, medium, and weak |
| T-1m | Active watchlist moved to this file — decay should live where it's executed, not where it's defined |
| T-1m | Weekly review protocol formalized with concrete steps |
| T-1m | External signals explicitly connected to the scoring rubric — a strong signal can raise the tier if the updated score exceeds the threshold |
