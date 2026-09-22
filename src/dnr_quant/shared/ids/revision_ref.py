"""Exact immutable revision-reference primitives.

Grounded in P6 E01:
- identity and immutable revision reference are distinct;
- normative exact refs require an explicit revision suffix;
- implicit-latest references are not valid exact normative refs.

This module is deliberately non-semantic.
"""

from __future__ import annotations

from dataclasses import dataclass
import re

_EXACT_REVISION_REF = re.compile(
    r"^(?P<object_id>[A-Z0-9][A-Z0-9_.-]*)@r(?P<revision>[1-9][0-9]*)$"
)


@dataclass(frozen=True, slots=True)
class ExactRevisionRef:
    object_id: str
    revision: int

    def __post_init__(self) -> None:
        if not self.object_id:
            raise ValueError("object_id must not be empty")
        if self.revision < 1:
            raise ValueError("revision must be >= 1")

    @classmethod
    def parse(cls, value: str) -> "ExactRevisionRef":
        match = _EXACT_REVISION_REF.fullmatch(value)
        if match is None:
            raise ValueError(
                "exact revision reference must have the form "
                "'<ObjectId>@r<positive integer>'"
            )
        return cls(
            object_id=match.group("object_id"),
            revision=int(match.group("revision")),
        )

    def __str__(self) -> str:
        return f"{self.object_id}@r{self.revision}"
