# skills/weekly-update.md — Investment OS Weekly Workflow

> This workflow integrates the system into the fund's real operations.
> Cadence: fixed weekly meeting with partners on Fridays. The automated weekly
> summary runs every Monday.

---

## Week overview

| Moment | Task | Estimated time |
|---|---|---|
| Monday, automatic | Weekly review (signals, revival, agenda, priorities) | Automatic |
| Monday / Tuesday | Act on the weekly review's priorities | 30-60 min |
| Wednesday / Thursday | Prepare one-pagers (Review) and update analyses (Analysis) for Friday | 20-45 min per deal |
| Friday | Meeting with partners | 2h |
| Friday, post-meeting | Document decisions made | 15 min |
| Whenever a deck arrives | Automatic screening → item in pipeline | Automatic |

---

## MONDAY — Automatic weekly review

Produces:
1. **New dealflow signals** — rounds, partnerships, ecosystem news
2. **Repository audit** — expired signals, criteria to update, blocked deals
3. **Automatic revival** — this week's emails that trigger recontacts or new items
4. **Week's agenda** — preparatory actions for each event
5. **Week's priorities** — a list of up to 7 prioritized tasks

**Action after the weekly review:** review the output and execute the top 3
priorities before Wednesday.

---

## WEDNESDAY / THURSDAY — Preparing Friday's meeting

### For companies in Review (one-pager)

```
This company is going to Friday's meeting in Review stage.
Generate the one-pager following skills/deal-analysis.md.
```

### For companies in Analysis (assessment update)

```
This company is in Analysis. Attaching new information after [call / Q&A /
data room].
Update the initial assessment following skills/deal-analysis.md.
Indicate which blocking questions remain open and which have been resolved.
```

### For companies going to IC

```
This deal is going to the IC. Prepare:
1. The 5 toughest questions the committee will ask
2. The answers the founding team would give based on what we know
3. The 3 main risks the committee will flag
4. A one-sentence summary of why yes and why not to invest
Be brutally honest — the goal is to anticipate objections, not sell the deal.
```

---

## FRIDAY — Post-meeting (15 min)

### If a company advances to Analysis:
```
The team decided to advance [NAME] to Analysis.
Partner lead: [PARTNER NAME]
Main reason: [REASON]
Update the Stage and create the Initial Assessment file with the approved
one-pager as its base.
```

### If a company is discarded:
```
The team discarded [NAME] at the meeting / IC.
Reason: [REASON]
ICP criterion not met: [CRITERION]
Generate the learning entry.
Indicate whether this should update anything in the ICP.
```

### If the ICP evolves:
If the team mentions that something in the criteria has changed, update the ICP
definition with the learning and the date.

---

## WHEN A DECK ARRIVES — Automatic screening

1. Analysis against the ICP → Tier 1/2/3/4 classification
2. Ask for the source type and source
3. Create the item in the pipeline with all fields
4. Add a comment with the summary

See `skills/deal-screening.md` for the full criteria.

---

## WHEN A RELEVANT EMAIL ARRIVES — Signal processing

```
This email just arrived. Identify whether it's a revival signal for any company
in the pipeline, assess the signal type per fund-intelligence.md, and tell me what
action to take.
```

1. Identify the company
2. Assess the signal (strong / medium / weak)
3. Recommend an action (update Stage, add a comment, reply to the email)
4. If it's a strong signal, generate a draft reply

---

## Repository files and when to update them

| File | When to update |
|---|---|
| `skills/icp-definition.md` | After every IC with a new learning; when the team changes criteria |
| `skills/deal-screening.md` | When something new is learned about field classification |
| `skills/deal-analysis.md` | When the Review/Analysis/IC process changes |
| `skills/fund-intelligence.md` | When decay timelines or revival signals change |
