from fastapi import APIRouter
from datetime import datetime, timezone

from .models import RouteRequest, RouteResponse
from .audit import record_event, list_events

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/")
def root():
    return {"status": "ok"}

@router.get("/meta")
def meta():
    return {
        "service": "portfolio_router",
        "version": "0.1.0",
        "env": "dev",
        "ts": datetime.now(timezone.utc).isoformat(),
    }

@router.post("/v1/route", response_model=RouteResponse)
def v1_route(req: RouteRequest):
    # Deterministic stub routing (no chain-of-thought; only decision labels)
    chosen = "default"
    tags = ["router_v1", f"risk_{req.risk_tier}"]

    if "refund" in req.intent.lower():
        chosen = "billing"
        tags.append("intent_refund")
    elif "injury" in req.intent.lower():
        chosen = "safety_triage"
        tags.append("intent_injury")

    record_event(path="/v1/route", method="POST", status_code=200, risk_tier=req.risk_tier)

    return RouteResponse(
        chosen_route=chosen,
        confidence=0.72,
        decision_tags=tags,
    )

@router.get("/v1/audit/events")
def v1_audit_events(limit: int = 50):
    return [e.model_dump() for e in list_events(limit=limit)]
