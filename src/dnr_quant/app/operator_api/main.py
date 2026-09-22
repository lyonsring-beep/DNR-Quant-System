"""FastAPI application bootstrap.

This module establishes the P6-selected backend framework without inventing
domain API contracts. E04 owns concrete API/message semantics.
"""

from fastapi import FastAPI

app = FastAPI(
    title="DNR Quant Platform",
    version="0.1.0",
    description="Advisory / research only. No live trading authority.",
)
