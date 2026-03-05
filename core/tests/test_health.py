"""
Portfolio Router — Health Endpoint Test

Purpose
-------
Basic smoke test to verify the FastAPI service
responds to the /health endpoint correctly.

This test validates the public API surface
rather than internal modules.
"""

import sys
from pathlib import Path
from starlette.testclient import TestClient

# Ensure project root is available to Python path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from app.main import app


client = TestClient(app)


def test_health_endpoint():
    """
    Health endpoint should return HTTP 200
    and include a 'status' field in JSON response.
    """

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert "status" in data
