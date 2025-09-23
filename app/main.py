from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

from app.models.churn_model import ChurnModel


app = FastAPI(title="Churn Prediction Service", version="0.1.0")
model = ChurnModel()


class CustomerFeatures(BaseModel):
    # Example minimal features; replace with your real model inputs
    tenure_months: float = Field(..., ge=0)
    monthly_charges: float = Field(..., ge=0)
    contract_type: int = Field(..., ge=0, le=2)


class PredictionRequest(BaseModel):
    instances: List[CustomerFeatures]


class PredictionResponse(BaseModel):
    predictions: List[int]
    probabilities: List[float]


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    if not request.instances:
        raise HTTPException(status_code=400, detail="No instances provided")
    preds, probs = model.predict_batch([i.dict() for i in request.instances])
    return PredictionResponse(predictions=preds, probabilities=probs)


@app.get("/")
def root() -> dict:
    return {"service": "churn", "version": app.version}


