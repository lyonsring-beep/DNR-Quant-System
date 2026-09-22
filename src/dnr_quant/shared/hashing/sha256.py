"""SHA-256 helpers for immutable content evidence.

A digest proves byte equality under a chosen serialization. It does not prove
semantic truth, currentness, authorization, or deployment readiness.
"""

from __future__ import annotations

import hashlib


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_utf8(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))
