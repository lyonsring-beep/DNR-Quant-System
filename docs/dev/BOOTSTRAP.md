# P7 Bootstrap

This repository follows the Frozen P6 E02 implementation envelope.

## Toolchain pins

- CPython 3.14.7, standard GIL x64
- uv 0.12.5
- Node.js 24.19.0 LTS
- pnpm 11.21.0

## Canonical dependency surfaces

Python:
- declaration: `pyproject.toml`
- exact lock: `uv.lock`

Web:
- declaration: `web/package.json`
- exact lock: `web/pnpm-lock.yaml`

No component-local canonical resolver graphs are permitted.

## Current bootstrap status

The repository topology and manifests are established.
Lock artifacts must be generated using the exact pinned toolchain before Phase 0 can be declared complete.
