from pydantic import BaseModel, Field
from typing import List, Literal, Optional
from datetime import datetime

RiskTier = Literal["low", "medium", "high"]


class RouteRequest(BaseModel):
    intent: str = Field(..., min_length=1, max_length=200)
    constraints: List[str] = Field(default_factory=list, max_length=20)
    risk_tier: RiskTier = "low"


class RouteResponse(BaseModel):
    chosen_route: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    decision_tags: List[str] = Field(default_factory=list)


class AuditEvent(BaseModel):
    event_id: str
    ts: datetime
    path: str
    method: str
    status_code: int
    risk_tier: Optional[RiskTier] = None
