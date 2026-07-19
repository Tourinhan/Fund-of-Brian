# skills/deal-analysis.md — Skill: Startup Analysis

> Use this skill for any startup analysis task.
> Covers every stage of the process: from screening to IC preparation.

---

## The full analysis process

```
PIPELINE         REVIEW                      MEETING              ANALYSIS              IC
(Screened)  ─►  Analyst calls           ─►  3 partners      ─►  Partner leads    ─►  IC
                the founder                  weigh in            with analyst          decision
                requests data room           ┌ OK × 3 → Analysis  more calls
                prepares one-pager           ├ Doubts → stays     CEO Q&A
                                            │  in Review           full data room
                                            └ Reject → archive     IA iterations
```

**Process rules:**
- Review is initiated by the analyst alone, after a call with the founder
- Moving from Review to Analysis requires the OK of all **3 partners** at the
  weekly meeting
- In Analysis, **one partner leads** the opportunity together with the analyst
- The number of Analysis iterations isn't fixed — it depends on available
  information

---

## Stage 1 — Screening

See `skills/deal-screening.md`.

---

## Stage 2 — Review: one-pager for the meeting

**Who**: analyst, alone, before the meeting
**Goal**: does this company deserve the OK of all 3 partners to move to Analysis?
**Output**: a max. 2-page one-pager

**What the one-pager IS**: the tool that lets the analyst save the team's time when
presenting a new opportunity — a quick, sufficient first pass to decide whether the
deal is worth pursuing further.

**What the one-pager is NOT**: it is never generated from an already-existing
Initial Assessment. The order is always one-pager → (if it clears the meeting) →
Initial Assessment v1. The one-pager is the source, not the summary. If an IA
already exists for a deal that's still in Review, **it is not used as input for the
one-pager** — they're artifacts of different stages of the process with different
owners and objectives.

**The level of detail in the one-pager varies with the actual data room access at
that point in time** — this is a variable of the process, not a flaw in the
document.

**Rule for sections with no information**: if a section couldn't be filled in yet,
mark it explicitly as "Pending — available in [source]" instead of leaving it blank
or inventing content. "This information doesn't exist" is not the same as "it exists
but hasn't been extracted yet."

**Rule of data vs. assumption**: any traction or financial figure must indicate
where it comes from:
- Verified data: state the source (e.g. "€212K ARR — deck, data as of [date]")
- Projection or estimate: state the assumption behind it
- Discrepancy between sources: flag it explicitly, don't merge it (e.g. "deck: +30
  hospitals; call: 18 active sites — to reconcile")

**Rule of honesty about negative data**: any negative fact known during Review must
appear in the one-pager, not be omitted to make the deal "look better" at the
meeting. Partners who discover surprises in diligence that weren't in the one-pager
lose trust in the analyst and in the deal.

**Standard for the "Why NOT" section**: this isn't a list of generic risks. It's the
strongest objection a skeptical partner would raise if they wanted to vote against
the deal — articulated with specific evidence and, where possible, with the
response or nuance that offsets it. A weak "Why NOT" ("competitive market,"
"early stage") makes partners wonder whether the analyst actually looked for
reasons not to invest.

### One-pager contents

1. Snapshot (3 lines: what it does, for whom, business model)
2. ICP score (Tier + score + criteria met and not met)
3. Detected signals (with scoring and decay)
4. Why yes (max. 3 reasons)
5. Why not (max. 3 objections — be honest here)
6. Recommendation (advance to Analysis / Watch soon / Pass)
7. Concrete next step

---

## Stage 3 — Meeting: decision

**Who**: analyst presents, the 3 partners weigh in
**Possible output**:
- **OK from all 3 partners** → moves to Analysis, a partner lead is assigned
- **Doubts** → returns to Review, with specifics on what to resolve
- **Reject** → archived with the documented reason

**Note**: if only 1 or 2 partners give the OK, the deal goes back to Review — it
does not move to Analysis. All 3 partners must weigh in for the decision to be
valid.

---

## Stage 4 — Analysis: iterative Initial Assessment

**Who**: partner lead + analyst
**Goal**: build enough understanding to take the deal to the IC — or discard it
with evidence
**Input**: one-pager + CEO Q&A + full data room + co-investor calls + founding team
video call
**Output**: a document that grows with each iteration (10 sections)

### When a deal in Analysis is ready for IC:

1. The main blockers resolved (typically: real traction + modeled return for the
   fund)
2. "Why we should NOT invest" completed by all 3 partners
3. No unresolved red flags
4. Video call with the full founding team completed
5. Partner lead has spoken with the round's lead investor

---

## Stage 5 — IC preparation

**Who**: partner lead prepares, presents to the IC
**Goal**: anticipate the tough questions before the committee asks them
**Input**: full Initial Assessment (latest iteration)

### What this stage produces:

1. The 5 toughest questions the IC will ask (based on the fund's criteria, past
   rejections, and open items in the IA)
2. The founding team's answer to each question
3. The 3 main risks the IC will flag
4. The base-case and central MOIC with an estimated ticket and expected dilution
5. Why YES in one sentence / Why NOT in one sentence

**Be brutally honest. The goal is to anticipate objections, not sell the deal.**

---

## Universal red flags — look for these at any stage

- **Traction that doesn't survive scrutiny**: the deck says one thing, the data
  room says another
- **A team that hasn't lived the problem**: the unfair advantage is narrative, not
  real experience
- **Dependence on a single client >70%**: with no credible diversification plan
- **Valuation that blocks the target equity**: <5% with no room to negotiate
- **Unrealistic exit plan**: year 4-5 of the plan is the ceiling, not the central
  scenario
- **Co-investors of convenience**: names that sound good but don't bring anything
  beyond the check
- **Generic AI/technology with no real technical edge**: a language model over
  public data with no demonstrable moat
- **Unverified mandate fit**: for non-Spanish companies, confirm whether they
  qualify for the European tranche or only the restricted tranche before the
  meeting

---

## Learning history

| Date | Learning |
|---|---|
| T-6m | The Review one-pager is never generated from an already-existing Initial Assessment, even if one is available for the deal. It's an independent artifact that precedes the IA |
| T-6m | The one-pager's level of detail depends on the actual data room access at the time of Review — it's a legitimate variable of the process, not a flaw |
| T-1m | Rule of data vs. assumption: any figure must state its source or the assumption it rests on. Discrepancies between sources are flagged explicitly, not merged |
| T-1m | Rule of honesty about negative data: negative facts known during Review must appear in the one-pager, not be omitted |
| T-1m | Standard for "Why NOT": the strongest possible objection, not a generic list of risks |
