"""Integrity and reproduction tests. Run from the repo root:

    python -m unittest discover -s tests -v
"""
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
import analysis  # noqa: E402


class TestDataIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = analysis.load_data(analysis.DEFAULT_DATA)
        cls.audit = pd.read_csv(ROOT / "data" / "coding_audit_trail.csv")

    def test_35_unique_organizations(self):
        self.assertEqual(len(self.df), 35)
        self.assertEqual(self.df["organization"].nunique(), 35)

    def test_performance_conversion_matches_published_two_decimals(self):
        published = pd.read_csv(analysis.DEFAULT_DATA)["cybersecurity_performance_0_to_100"]
        self.assertLess((self.df["Cybersecurity_Performance"] - published).abs().max(), 0.01)

    def test_audit_trail_matches_dataset(self):
        raw = pd.read_csv(analysis.DEFAULT_DATA)
        self.assertEqual(list(raw["organization"]), list(self.audit["organization"]))
        self.assertEqual(list(raw["ai_adoption_1_to_5"]), list(self.audit["audited_score"]))

    def test_every_organization_has_a_source_url(self):
        self.assertTrue(self.audit["primary_source_url"].str.startswith("http").all())


class TestReproduction(unittest.TestCase):
    """Values that DO reproduce from data/organizations.csv (Tables 3 [SD, range], 5)."""

    @classmethod
    def setUpClass(cls):
        cls.df = analysis.load_data(analysis.DEFAULT_DATA)
        cls.reg, cls.fit = analysis.regression(cls.df)

    def test_table3_performance_and_employees(self):
        d = analysis.descriptives(self.df)
        self.assertAlmostEqual(d.loc["Cybersecurity_Performance", "mean"], 85.38, places=2)
        self.assertAlmostEqual(d.loc["Cybersecurity_Performance", "std"], 3.72, places=2)
        self.assertAlmostEqual(d.loc["Employees", "mean"], 282583.43, places=2)
        self.assertAlmostEqual(d.loc["AI_Adoption", "std"], 1.34, places=2)

    def test_table3_ai_mean_and_table4_correlations(self):
        self.assertAlmostEqual(analysis.descriptives(self.df).loc["AI_Adoption", "mean"], 2.03, places=2)
        c = analysis.correlations(self.df)
        self.assertAlmostEqual(c.iloc[0]["coefficient"], 0.101, places=3)
        self.assertAlmostEqual(c.iloc[0]["p"], 0.564, places=3)
        self.assertAlmostEqual(c.iloc[1]["coefficient"], 0.055, places=3)
        self.assertAlmostEqual(c.iloc[1]["p"], 0.753, delta=0.001)

    def test_table5_regression(self):
        # Published Table 5 was computed from performance scores rounded to 2 decimals,
        # whereas analysis.py uses unrounded UpGuard/950*100, so allow a 0.01 tolerance.
        r = self.reg.set_index("predictor")
        self.assertAlmostEqual(r.loc["Constant", "B"], 81.941, delta=0.01)
        self.assertAlmostEqual(r.loc["AI_Adoption", "B"], 0.471, delta=0.01)
        self.assertAlmostEqual(r.loc["AI_Adoption", "p"], 0.363, delta=0.01)
        self.assertAlmostEqual(r.loc["Transportation & Logistics", "B"], 10.264, delta=0.01)
        self.assertAlmostEqual(self.fit["R2"], 0.455, delta=0.001)
        self.assertAlmostEqual(self.fit["adj_R2"], 0.258, delta=0.001)
        self.assertAlmostEqual(self.fit["F"], 2.316, delta=0.01)
        self.assertAlmostEqual(self.fit["F_p"], 0.047, delta=0.001)

    def test_ols_matches_closed_form_on_toy_data(self):
        rng = np.random.default_rng(0)
        X = np.column_stack([np.ones(30), rng.normal(size=(30, 2))])
        y = X @ np.array([1.0, 2.0, -1.0]) + rng.normal(scale=0.1, size=30)
        tab, fit = analysis.ols(X, y, ["c", "a", "b"])
        np.testing.assert_allclose(tab["B"], [1, 2, -1], atol=0.2)
        self.assertGreater(fit["R2"], 0.99)


if __name__ == "__main__":
    unittest.main()
