# Portfolio Router — System Docs

## What this is
Portfolio Router is a governance-first routing service:
- **core/** is the source-of-truth (logic, schemas, validation, tests)
- **api/** is a thin FastAPI wrapper (parse → call core → format response)
- **ts-client/** is a consumer-only typed client

## Design Laws (non-negotiables)
1. No business logic in `api/`
2. All behavior must be test-gated
3. No silent evolution: changes are versioned + logged

## Start Here
- Architecture Baseline ADR: `docs/adr/0001-architecture-baseline.md`
- Decisions Log: `docs/DECISIONS.md` (if present)