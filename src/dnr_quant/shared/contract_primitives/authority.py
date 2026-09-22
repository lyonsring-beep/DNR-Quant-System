"""Frozen system-authority constants.

These constants expose upstream authority boundaries to implementation code.
They do not grant authority.
"""

SYSTEM_AUTHORITY = "ADVISORY / RESEARCH ONLY"
LIVE_TRADING_AUTHORITY = "NONE"


def assert_no_live_trading_authority() -> None:
    if LIVE_TRADING_AUTHORITY != "NONE":
        raise RuntimeError("live trading authority must remain NONE")
