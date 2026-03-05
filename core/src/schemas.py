"""
Schemas: single source of truth for data contracts.
Keep this module dependency-light.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class HealthCheck:
    status: str = "ok"
