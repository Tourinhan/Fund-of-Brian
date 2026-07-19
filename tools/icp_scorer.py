#!/usr/bin/env python3
"""
icp_scorer.py — Reference implementation of the ICP scoring rubric described in
skills/icp-definition.md.

This is a working, runnable version of the rubric the case study documents in prose.
The point isn't to be a production scoring engine — it's to show that the scoring
logic in the skill file is precise enough to actually be code, not just a vibe.
Every branch below maps directly to a row in the tables of
skills/icp-definition.md — read them side by side.

Usage:
    python3 icp_scorer.py                          # runs the 4 bundled sample deals (Tier 1-4)
    python3 icp_scorer.py --deal sample_deals.json  # score deals from a JSON file
    python3 icp_scorer.py --json                    # machine-readable output

No external dependencies — standard library only.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal


# ---------------------------------------------------------------------------
# Input schema for a single deal
# ---------------------------------------------------------------------------

Stage = Literal["seed", "series_a"]
SectorFit = Literal["core", "adjacent", "peripheral", "outside"]
CoInvestorTier = Literal["top_tier_committed", "mid_tier_committed", "only_angels", "none"]
Geography = Literal["spain_tt", "spain_no_tt", "europe_with_es_link", "europe_only", "outside_eu"]


@dataclass
class Deal:
    name: str
    stage: Stage

    # 1. Return potential
    base_case_multiple: float
    exit_point_validated: bool

    # 2. Commercial traction
    arr_eur: float
    yoy_growth_pct: float
    has_institutional_paid_contracts: bool
    churn_pct: float

    # 3. Team
    founder_prior_exit_in_health: bool
    founder_prior_exit_other_sector: bool
    technical_cofounder_present: bool
    joint_prior_experience: bool

    # 4. Sector / thesis fit
    sector_fit: SectorFit

    # 5. Co-investors
    coinvestor_tier: CoInvestorTier

    # 6. Geography / tranche
    geography: Geography

    # 7. Valuation / equity
    post_money_eur: float
    board_seat_confirmed: bool

    notes: str = ""


@dataclass
class DimensionScore:
    name: str
    points: int
    max_points: int
    rationale: str


@dataclass
class ScoreResult:
    deal_name: str
    dimensions: list[DimensionScore] = field(default_factory=list)
    total: int = 0
    tier: str = ""
    blocking_flags: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Dimension scorers — each mirrors a table in skills/icp-definition.md
# ---------------------------------------------------------------------------

def score_moic(deal: Deal) -> DimensionScore:
    """skills/icp-definition.md — '1. Retorno potencial (MOIC) — 20 pts'"""
    m = deal.base_case_multiple
    seed = deal.stage == "seed"

    if (seed and m > 10) or (not seed and m > 5):
        pts = 20 if deal.exit_point_validated else 19
        why = f"Base case {m:g}x clears the fund's top band" + (
            " with a validated exit point." if deal.exit_point_validated
            else ", but the exit point isn't validated yet."
        )
    elif (seed and m >= 7) or (not seed and m >= 3):
        pts = 15 if deal.exit_point_validated else 14
        why = f"Base case {m:g}x — solid, but upside likely hinges on a non-guaranteed event."
    elif (seed and m >= 3) or (not seed and m >= 2):
        pts = 8
        why = f"Base case {m:g}x — below the fund's top bands, fund-returning outcome needs an optimistic scenario."
    else:
        pts = 3
        why = f"Base case {m:g}x — below the fund's minimum threshold, or not reliably calculable."

    return DimensionScore("Return potential (MOIC)", pts, 20, why)


def score_traction(deal: Deal) -> DimensionScore:
    """skills/icp-definition.md — '2. Tracción comercial — 20 pts'"""
    arr, growth, churn = deal.arr_eur, deal.yoy_growth_pct, deal.churn_pct

    if arr > 500_000 and growth > 100 and churn < 5:
        pts, why = 19, "ARR >€500K, growing >100% YoY, churn <5% — top band."
    elif arr >= 100_000 or (deal.has_institutional_paid_contracts and arr >= 50_000):
        pts, why = 14, "Meaningful ARR or paid institutional pilots, growth demonstrable."
    elif arr > 0 or deal.has_institutional_paid_contracts:
        pts, why = 8, "Early revenue or unpaid pilots with relevant LOIs — concept validated, not scale."
    else:
        pts, why = 3, "Pre-revenue, no contracts or paid pilots."

    return DimensionScore("Commercial traction", pts, 20, why)


def score_team(deal: Deal) -> DimensionScore:
    """skills/icp-definition.md — '3. Equipo — 15 pts'"""
    pts = 6  # baseline: first-time founder, no exit, some sector experience
    why_parts = ["First-time founder team as baseline."]

    if deal.founder_prior_exit_in_health and deal.technical_cofounder_present:
        pts = 14
        why_parts = ["Serial founder with a prior health exit + relevant technical co-founder."]
    elif (deal.founder_prior_exit_other_sector or deal.founder_prior_exit_other_sector) and deal.technical_cofounder_present:
        pts = 10
        why_parts = ["Prior exit (any sector) or deep sector background + relevant technical co-founder."]

    bonus = 0
    if deal.joint_prior_experience:
        bonus += 1
        why_parts.append("+1 bonus: prior joint experience.")
    if deal.founder_prior_exit_other_sector:
        bonus += 1
        why_parts.append("+1 bonus: prior exit >€10M in any sector.")

    pts = min(15, pts + bonus)
    return DimensionScore("Team", pts, 15, " ".join(why_parts))


def score_sector(deal: Deal) -> DimensionScore:
    """skills/icp-definition.md — '4. Sector / Fit con tesis — 15 pts'"""
    table = {
        "core": (14, "Exact core of the thesis, precedent in the portfolio."),
        "adjacent": (10, "Confirmed Digital Health, less familiar sub-sector."),
        "peripheral": (6, "Peripheral fit — consumer component or generic horizontal tech."),
        "outside": (2, "Outside the sector or generic AI with no clinical/regulatory edge."),
    }
    pts, why = table[deal.sector_fit]
    return DimensionScore("Sector / thesis fit", pts, 15, why)


def score_coinvestors(deal: Deal) -> DimensionScore:
    """skills/icp-definition.md — '5. Co-inversores — 10 pts'"""
    table = {
        "top_tier_committed": (9, "Top-tier lead investor already committed."),
        "mid_tier_committed": (7, "Mid-to-high quality co-investor committed, or top-tier in advanced talks."),
        "only_angels": (4, "Only business angels or accelerators, no VC lead confirmed."),
        "none": (1, "No co-investors, no signal of interest from quality funds."),
    }
    pts, why = table[deal.coinvestor_tier]
    return DimensionScore("Co-investors", pts, 10, why)


def score_geography(deal: Deal) -> DimensionScore:
    """skills/icp-definition.md — '6. Geografía / Tramo — 10 pts'"""
    table = {
        "spain_tt": (9, "Spanish with documented tech transfer."),
        "spain_no_tt": (7, "Spanish without formal tech transfer but a relevant institutional link."),
        "europe_with_es_link": (6, "European with Spanish operations or relevant pipeline."),
        "europe_only": (3, "European with no Spanish presence or pipeline."),
        "outside_eu": (0, "Outside Spain/Europe with no European expansion plan."),
    }
    pts, why = table[deal.geography]
    return DimensionScore("Geography / tranche", pts, 10, why)


def score_valuation(deal: Deal) -> DimensionScore:
    """skills/icp-definition.md — '7. Valoración / Equity — 10 pts'"""
    pm = deal.post_money_eur

    if pm < 15_000_000 and deal.board_seat_confirmed:
        pts, why = 9, "Post-money <€15M, >7% equity, board seat confirmed."
    elif pm < 25_000_000:
        pts, why = 7, "Post-money €15M-€25M, ~5-7% equity, standard market terms."
    elif pm < 40_000_000:
        pts, why = 5, "Post-money €25M-€40M, ~3-5% equity, no board seat confirmed."
    else:
        pts, why = 2, "Post-money >€40M or equity <3% with no room to negotiate."

    return DimensionScore("Valuation / equity", pts, 10, why)


# ---------------------------------------------------------------------------
# Aggregation, tier conversion, and blocking flags
# ---------------------------------------------------------------------------

SCORERS = [
    score_moic,
    score_traction,
    score_team,
    score_sector,
    score_coinvestors,
    score_geography,
    score_valuation,
]


def tier_for_score(total: int) -> str:
    """skills/icp-definition.md — 'Score → Tier conversion'"""
    if total >= 75:
        return "Tier 1 — Supernova"
    if total >= 50:
        return "Tier 2 — Watch soon"
    if total >= 25:
        return "Tier 3 — Watch later"
    return "Tier 4 / Anti-ICP — Pass"


def blocking_flags_for(dimensions: list[DimensionScore], deal: Deal) -> list[str]:
    """
    skills/icp-definition.md — blocking flags override an otherwise-passing score:
    MOIC 0-5 pts, or Valuation 0-3 pts with no board seat, both block advancement
    to Analysis regardless of the total, unless a formal IC exception is granted.
    """
    flags = []
    moic_score = next(d for d in dimensions if d.name.startswith("Return"))
    valuation_score = next(d for d in dimensions if d.name.startswith("Valuation"))

    if moic_score.points <= 5:
        flags.append(
            "MOIC blocking flag (0-5 pts): blocks advancement to Analysis "
            "unless a formal IC exception is approved by partners."
        )
    if valuation_score.points <= 3 and not deal.board_seat_confirmed:
        flags.append(
            "Valuation/equity blocking flag (0-3 pts, no board seat): "
            "direct discard (Tier 4) unless a formal IC exception applies."
        )
    return flags


def score_deal(deal: Deal) -> ScoreResult:
    dimensions = [scorer(deal) for scorer in SCORERS]
    total = sum(d.points for d in dimensions)
    result = ScoreResult(
        deal_name=deal.name,
        dimensions=dimensions,
        total=total,
        tier=tier_for_score(total),
        blocking_flags=blocking_flags_for(dimensions, deal),
    )
    return result


# ---------------------------------------------------------------------------
# I/O — loading deals and printing results
# ---------------------------------------------------------------------------

def deal_from_dict(d: dict) -> Deal:
    return Deal(**d)


def load_deals(path: Path) -> list[Deal]:
    data = json.loads(path.read_text())
    return [deal_from_dict(d) for d in data]


def print_human(result: ScoreResult) -> None:
    print(f"\n{'=' * 60}")
    print(f"{result.deal_name}")
    print(f"{'=' * 60}")
    for d in result.dimensions:
        bar = "█" * d.points + "░" * (d.max_points - d.points)
        print(f"  {d.name:<28} {d.points:>2}/{d.max_points:<3} {bar}")
        print(f"    └─ {d.rationale}")
    print(f"  {'-' * 56}")
    print(f"  {'TOTAL':<28} {result.total:>2}/100")
    print(f"  {'TIER':<28} {result.tier}")
    if result.blocking_flags:
        print("  ⚠ BLOCKING FLAGS:")
        for flag in result.blocking_flags:
            print(f"    - {flag}")


def print_json(results: list[ScoreResult]) -> None:
    out = []
    for r in results:
        out.append({
            "deal_name": r.deal_name,
            "total": r.total,
            "tier": r.tier,
            "blocking_flags": r.blocking_flags,
            "dimensions": [
                {"name": d.name, "points": d.points, "max_points": d.max_points, "rationale": d.rationale}
                for d in r.dimensions
            ],
        })
    print(json.dumps(out, indent=2))


# ---------------------------------------------------------------------------
# Bundled sample deals (used when no --deal file is passed)
# ---------------------------------------------------------------------------

SAMPLE_DEALS = [
    Deal(
        name="Cortavia (Tier 2 example — see examples/sample-flow.md)",
        stage="seed",
        base_case_multiple=4.0,
        exit_point_validated=False,
        arr_eur=85_000,
        yoy_growth_pct=60,
        has_institutional_paid_contracts=True,
        churn_pct=0,
        founder_prior_exit_in_health=False,
        founder_prior_exit_other_sector=False,
        technical_cofounder_present=True,
        joint_prior_experience=False,
        sector_fit="core",
        coinvestor_tier="only_angels",
        geography="spain_tt",
        post_money_eur=9_000_000,
        board_seat_confirmed=False,
        notes="Spanish cardiovascular monitoring spinoff, 3 hospitals in paid pilot.",
    ),
    Deal(
        name="Veltrix Analytics (Tier 1 example)",
        stage="series_a",
        base_case_multiple=6.5,
        exit_point_validated=True,
        arr_eur=620_000,
        yoy_growth_pct=140,
        has_institutional_paid_contracts=True,
        churn_pct=3,
        founder_prior_exit_in_health=True,
        founder_prior_exit_other_sector=False,
        technical_cofounder_present=True,
        joint_prior_experience=True,
        sector_fit="core",
        coinvestor_tier="top_tier_committed",
        geography="spain_tt",
        post_money_eur=14_000_000,
        board_seat_confirmed=True,
        notes="Spanish clinical data interoperability platform, Series A.",
    ),
    Deal(
        name="Kestrion (Tier 3 example)",
        stage="seed",
        base_case_multiple=3.5,
        exit_point_validated=False,
        arr_eur=15_000,
        yoy_growth_pct=80,
        has_institutional_paid_contracts=False,
        churn_pct=0,
        founder_prior_exit_in_health=False,
        founder_prior_exit_other_sector=False,
        technical_cofounder_present=True,
        joint_prior_experience=False,
        sector_fit="adjacent",
        coinvestor_tier="only_angels",
        geography="europe_only",
        post_money_eur=5_000_000,
        board_seat_confirmed=False,
        notes="German wearable-based longevity monitoring, pre-seed graduating to seed, "
              "early clinical pilot, no institutional paid contracts yet.",
    ),
    Deal(
        name="Zendrax (Tier 4 / Anti-ICP example)",
        stage="seed",
        base_case_multiple=1.4,
        exit_point_validated=False,
        arr_eur=0,
        yoy_growth_pct=0,
        has_institutional_paid_contracts=False,
        churn_pct=0,
        founder_prior_exit_in_health=False,
        founder_prior_exit_other_sector=False,
        technical_cofounder_present=False,
        joint_prior_experience=False,
        sector_fit="peripheral",
        coinvestor_tier="none",
        geography="outside_eu",
        post_money_eur=45_000_000,
        board_seat_confirmed=False,
        notes="Consumer medication reminder app, pre-revenue, no institutional channel.",
    ),
]


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--deal", type=Path, default=None,
        help="Path to a JSON file with one or more deals (see sample_deals.json for the schema)",
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Print machine-readable JSON instead of the human-readable report",
    )
    args = parser.parse_args()

    deals = load_deals(args.deal) if args.deal else SAMPLE_DEALS
    results = [score_deal(d) for d in deals]

    if args.json:
        print_json(results)
    else:
        for r in results:
            print_human(r)
        print(
            "\nAll data above is fictional — see skills/icp-definition.md for the "
            "full rubric this script implements.\n"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
