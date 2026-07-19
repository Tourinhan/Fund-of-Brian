# tools/icp_scorer.py

A runnable reference implementation of the ICP scoring rubric described in
[`skills/icp-definition.md`](../skills/icp-definition.md). Every branch in the code
maps directly to a row in that document's tables — read them side by side.

This isn't a production scoring engine. It exists to prove the rubric described in
prose is precise enough to actually be code, not just a well-written vibe.

## Run it

No dependencies beyond the Python standard library (3.9+).

```bash
# Run the 4 bundled fictional deals (Tier 1 through Tier 4)
python3 icp_scorer.py

# Run against your own deals
python3 icp_scorer.py --deal sample_deals.json

# Machine-readable output
python3 icp_scorer.py --json
```

## What it shows

- Each of the 7 weighted dimensions scored independently, with a one-line rationale
  per dimension
- The total score and resulting Tier (1–4)
- **Blocking flags**: a high total score doesn't guarantee Tier 1 if MOIC or
  Valuation/Equity hit a blocking threshold — this mirrors the "auditable scoring,
  not a black box" principle from the main README

## Extending it

`sample_deals.json` shows the input schema for a deal. Add your own (fictional!)
deals to a JSON file and pass it with `--deal your_file.json`.
