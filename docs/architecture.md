# Architecture

## The three layers

### 1. Knowledge layer (`skills/`)

Versioned markdown files that define:
- Who the fund is, its mandate and constraints (geography, ticket size, sector)
- What an ideal deal looks like and how it's scored (a 0–100 point rubric across 7
  dimensions)
- How each stage of the funnel is executed (screening → review → analysis → IC)
- How knowledge is managed over the long term (decay, revival, watchlist)

This layer doesn't live in a fixed system prompt — it lives in files that the model
explicitly reads at the start of a session (`claude.md` as the entry point, which
references the rest). This allows:
- The human team to edit investment criteria without touching code or prompts
- The model to explicitly cite which part of the criteria a decision is based on
- The change history to be auditable (who changed which criterion, and why)

### 2. Reasoning layer (LLM)

The model acts as orchestrator: it reads the relevant part of the knowledge layer for
the task, decides which connected tools it needs, executes calls to those tools, and
produces the output (document, CRM item, summary) following the format defined in the
corresponding skill.

Relevant design points:
- **Write permissions scoped by tool and folder/board.** The model has explicit
  rules about what it can create/modify and what is strictly read-only (e.g. the
  investment criteria files themselves — the model reads them but never edits them
  on its own initiative).
- **No deletion, ever.** The system has no permission to delete anything in any
  connected tool — if something gets placed wrong, a human fixes it.
- **Explicit confirmation before irreversible actions** (sending an email, publishing
  a decision) — the model prepares the draft, the human approves it.

### 3. Tools layer (MCP)

Three connected systems via MCP (Model Context Protocol), each with a distinct role:

| Tool | Role | What it stores |
|---|---|---|
| **CRM** | Source of truth for the pipeline | Status of each company, structured fields (sector, geography, round), follow-up comments |
| **Internal file repository** | Document repository | Initial Assessments, one-pagers, IC memos, historical logs |
| **Notion** | Shared space with founders / data rooms | Founder notes, documentation shared by companies in process |

The model cross-references information across the three when the task requires it —
for example, when preparing an Initial Assessment, it may need to read the CRM
status, the deck in the file repository, and the notes from the latest founder call
in Notion, all within the same working session.

## Typical data flow: screening a new company

```
1. User attaches a deck (PDF)
        │
2. The model reads skills/deal-screening.md
        │
3. Asks for the source type (event, referral, inbound...) if not obvious
        │
4. Extracts fields from the deck (sector, geography, traction, team, round)
        │
5. Applies the rubric from skills/icp-definition.md → 0–100 score + Tier
        │
6. Creates the item in the CRM with the mapped fields
        │
7. Adds a comment/update with the summary (what it does · traction · team · Tier)
        │
8. Flags whether this deal's learnings should update the ICP criteria
```

## Why MCP instead of custom API integrations

Using MCP as the connection layer lets the same knowledge + reasoning pattern be
reused over any combination of tools the team uses, without rewriting integration
logic every time a tool in the stack changes. The operational knowledge (skills/) is
independent of which CRM or which document repository sits underneath.
