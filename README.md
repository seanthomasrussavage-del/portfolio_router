# portfolio_router

**Governance-first AI routing service with human-in-the-loop controls.**

---

## What This Is

`portfolio_router` is a FastAPI service that demonstrates how governance constraints can be embedded directly into an AI routing layer — not bolted on afterward.

Every request is validated against a policy schema before reaching a model. Every response is audited before returning to the caller. No request bypasses the gate. No exception is silent.

**AI systems should be auditable, constrained, and human-overridable by design.**

---

## Architecture

Request → Policy Gate (schema validation, risk scan, scope check) → Router (model selection) → Audit Layer (append-only log, drift detection) → Response

Three layers. Each independently testable. None bypassable.

---

## Quickstart

git clone https://github.com/seanthomasrussavage-del/portfolio_router.git
cd portfolio_router
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install pytest
pytest -q
uvicorn api.app.main:app --reload

---

## Governance Principles

Policy-first routing — gate runs before model selection
Append-only audit — no log entry modified or deleted
Schema enforcement — all requests validated against typed schemas
Human override — available at all decision points
Drift prevention — dependencies locked, environments isolated
Test-gated changes — CI blocks merge on test failure

---

## Related Repos

llm-governance-gate | multi-agent-router-hitl | drift-ledger-amendments | governance-test-suite | systems-notes

https://github.com/seanthomasrussavage-del

---

MIT © 2026 Sean Thomas Russavage
