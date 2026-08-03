#!/usr/bin/env python3
"""Unit tests for tools/icp_scorer.py — standard library only."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from icp_scorer import (  # noqa: E402
    Deal,
    SCORERS,
    blocking_flags_for,
    load_deals,
    score_deal,
    score_moic,
    score_valuation,
    tier_for_score,
)

SAMPLE_DEALS_PATH = Path(__file__).resolve().parent / "sample_deals.json"

TIER_1 = "Tier 1 — Supernova"
TIER_2 = "Tier 2 — Watch soon"
TIER_3 = "Tier 3 — Watch later"
TIER_4 = "Tier 4 / Anti-ICP — Pass"

MOIC_FLAG = (
    "MOIC blocking flag (0-5 pts): blocks advancement to Analysis "
    "unless a formal IC exception is approved by partners."
)
VALUATION_FLAG = (
    "Valuation/equity blocking flag (0-3 pts, no board seat): "
    "direct discard (Tier 4) unless a formal IC exception applies."
)


def _deal_by_name_prefix(deals: list[Deal], prefix: str) -> Deal:
    for deal in deals:
        if deal.name.startswith(prefix):
            return deal
    raise ValueError(f"No bundled deal found with name prefix: {prefix!r}")


def _base_deal(**overrides) -> Deal:
    defaults = {
        "name": "Synthetic test deal",
        "stage": "seed",
        "base_case_multiple": 8.0,
        "exit_point_validated": True,
        "arr_eur": 200_000,
        "yoy_growth_pct": 50,
        "has_institutional_paid_contracts": True,
        "churn_pct": 2,
        "founder_prior_exit_in_health": False,
        "founder_prior_exit_other_sector": False,
        "technical_cofounder_present": True,
        "joint_prior_experience": False,
        "sector_fit": "core",
        "coinvestor_tier": "mid_tier_committed",
        "geography": "spain_tt",
        "post_money_eur": 12_000_000,
        "board_seat_confirmed": True,
    }
    defaults.update(overrides)
    return Deal(**defaults)


class SampleDealScoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deals = load_deals(SAMPLE_DEALS_PATH)

    def test_veltrix_analytics_scores_tier_1(self):
        result = score_deal(_deal_by_name_prefix(self.deals, "Veltrix Analytics"))
        self.assertEqual(result.total, 95)
        self.assertEqual(result.tier, TIER_1)
        self.assertEqual(tier_for_score(result.total), TIER_1)

    def test_cortavia_scores_tier_2(self):
        result = score_deal(_deal_by_name_prefix(self.deals, "Cortavia"))
        self.assertEqual(result.total, 62)
        self.assertEqual(result.tier, TIER_2)
        self.assertEqual(tier_for_score(result.total), TIER_2)

    def test_kestrion_scores_tier_3(self):
        result = score_deal(_deal_by_name_prefix(self.deals, "Kestrion"))
        self.assertEqual(result.total, 46)
        self.assertEqual(result.tier, TIER_3)
        self.assertEqual(tier_for_score(result.total), TIER_3)

    def test_zendrax_scores_tier_4(self):
        result = score_deal(_deal_by_name_prefix(self.deals, "Zendrax"))
        self.assertEqual(result.total, 21)
        self.assertEqual(result.tier, TIER_4)
        self.assertEqual(tier_for_score(result.total), TIER_4)


class BlockingFlagTests(unittest.TestCase):
    def test_moic_blocking_flag_when_moic_scores_five_or_below(self):
        deal = _base_deal(base_case_multiple=1.0, exit_point_validated=False)
        moic = score_moic(deal)
        self.assertLessEqual(moic.points, 5)

        dimensions = [scorer(deal) for scorer in SCORERS]
        flags = blocking_flags_for(dimensions, deal)

        self.assertIn(MOIC_FLAG, flags)

        result = score_deal(deal)
        self.assertIn(MOIC_FLAG, result.blocking_flags)

    def test_valuation_blocking_flag_when_valuation_scores_three_or_below_without_board_seat(self):
        deal = _base_deal(post_money_eur=50_000_000, board_seat_confirmed=False)
        valuation = score_valuation(deal)
        self.assertLessEqual(valuation.points, 3)

        dimensions = [scorer(deal) for scorer in SCORERS]
        flags = blocking_flags_for(dimensions, deal)

        self.assertIn(VALUATION_FLAG, flags)

        result = score_deal(deal)
        self.assertIn(VALUATION_FLAG, result.blocking_flags)


if __name__ == "__main__":
    unittest.main()
