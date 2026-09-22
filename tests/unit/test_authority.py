import unittest

from dnr_quant.shared.contract_primitives.authority import (
    LIVE_TRADING_AUTHORITY,
    SYSTEM_AUTHORITY,
    assert_no_live_trading_authority,
)


class AuthorityBoundaryTest(unittest.TestCase):
    def test_frozen_authority_boundary(self) -> None:
        self.assertEqual("ADVISORY / RESEARCH ONLY", SYSTEM_AUTHORITY)
        self.assertEqual("NONE", LIVE_TRADING_AUTHORITY)
        assert_no_live_trading_authority()


if __name__ == "__main__":
    unittest.main()
