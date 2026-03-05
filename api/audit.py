from __future__ import annotations
from typing import List, Optional
from datetime import datetime, timezone
import uuid

from .models import AuditEvent, RiskTier

_EVENTS: List[AuditEvent] = []

def record_event(
    *,
    path: str,
    method: str,
    status_code: int,
    risk_tier: Optional[RiskTier] = None,
) -> AuditEvent:
    evt = AuditEvent(
        event_id=str(uuid.uuid4()),
        ts=datetime.now(timezone.utc),
        path=path,
        method=method,
        status_code=status_code,
        risk_tier=risk_tier,
    )
    _EVENTS.append(evt)
    return evt

def list_events(limit: int = 50) -> List[AuditEvent]:
    if limit < 1:
        limit = 1
    if limit > 200:
        limit = 200
    return _EVENTS[-limit:]
