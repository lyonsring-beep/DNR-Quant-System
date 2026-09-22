"""Non-authoritative technical error base types."""

from __future__ import annotations


class DnrTechnicalError(Exception):
    """Base class for technical implementation failures."""


class ContractViolationError(DnrTechnicalError):
    """Raised when an implementation-level contract invariant is violated."""
