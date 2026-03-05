"""
Business logic: pure functions where possible.
"""

from .schemas import HealthCheck


def health_check() -> HealthCheck:
    return HealthCheck()
