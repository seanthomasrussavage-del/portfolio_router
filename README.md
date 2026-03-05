# portfolio_router

Governance-first AI routing service built with FastAPI.

This service routes requests between AI agents and workflows while enforcing
schema validation, governance gates, drift logging, and optional
human-in-the-loop approval steps.

The goal is to make LLM-based systems **safe, observable, and auditable**.

---

## Architecture

```
Client
   │
   ▼
FastAPI Router
   │
   ├── Schema Validation
   ├── Governance Gates
   ├── Drift Detection
   └── HITL Approval (optional)
   │
   ▼
AI Agents / Tools
```

The router acts as the central control point for multi-agent systems.

---

## Features

- FastAPI service layer
- strict schema validation
- governance gate enforcement
- drift logging for auditing
- optional human-in-the-loop approval
- modular architecture

---

## Project Structure

```
api/            FastAPI routes
core/           routing logic
docs/           governance documentation
tests/          validation tests
ts-client/      example client integration
requirements.lock   dependency lock file
```

---

## Related Repositories

This project is part of a governance-focused AI system architecture:

- `llm-governance-gate`
- `multi-agent-router-hitl`
- `governance-test-suite`
- `drift-ledger-amendments`

Together these repositories demonstrate safe orchestration patterns
for AI-driven systems.

---

## Run Locally

```
pip install -r requirements.lock
uvicorn api.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

to view the Swagger interface.

---

## Purpose

Most LLM systems focus on **capability**.

This project focuses on **control**.

Safe AI systems require:

- routing controls
- governance gates
- validation layers
- audit trails

`portfolio_router` provides that foundation.

---
