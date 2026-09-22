from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]

REQUIRED_PATHS = [
    "src/dnr_quant/semantic/s01_strategy_capital",
    "src/dnr_quant/semantic/s02_market_universe",
    "src/dnr_quant/semantic/s03_feature_research",
    "src/dnr_quant/semantic/s04_simulation",
    "src/dnr_quant/semantic/s05_evidence",
    "src/dnr_quant/semantic/s06_validation",
    "src/dnr_quant/semantic/s07_suitability",
    "src/dnr_quant/semantic/s08_recommendation",
    "src/dnr_quant/integration/composition",
    "src/dnr_quant/infra/acquisition",
    "src/dnr_quant/infra/persistence",
    "src/dnr_quant/infra/workflow",
    "src/dnr_quant/infra/control",
    "src/dnr_quant/infra/observability",
    "web",
    "src/dnr_quant/app/operator_api",
    "src/dnr_quant/security/identity_holdout",
    "src/dnr_quant/security/config_secrets",
    "src/dnr_quant/security/recovery",
    "src/dnr_quant/compute/runtime",
]


class RepositoryTopologyTest(unittest.TestCase):
    def test_all_frozen_component_roots_exist(self) -> None:
        missing = [path for path in REQUIRED_PATHS if not (ROOT / path).exists()]
        self.assertEqual([], missing, f"Missing P6 E02-B03 component roots: {missing}")


if __name__ == "__main__":
    unittest.main()
