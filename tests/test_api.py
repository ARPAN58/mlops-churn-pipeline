import pytest
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"


def test_predict_batch():
    payload = {
        "instances": [
            {"tenure_months": 1, "monthly_charges": 100, "contract_type": 0},
            {"tenure_months": 24, "monthly_charges": 30, "contract_type": 2},
        ]
    }
    res = client.post("/predict", json=payload)
    assert res.status_code == 200
    body = res.json()
    assert "predictions" in body and "probabilities" in body
    assert len(body["predictions"]) == 2
    assert len(body["probabilities"]) == 2


