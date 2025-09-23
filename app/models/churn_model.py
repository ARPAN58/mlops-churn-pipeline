from typing import Dict, List, Tuple


class ChurnModel:
    """Stub model. Replace with your trained model load and inference.

    For demo purposes, we compute a simple linear score from three features and
    threshold at 0.5 to produce a churn prediction.
    """

    def __init__(self) -> None:
        # In real use: load artifacts from disk (e.g., joblib.load("model.joblib"))
        self.coefficients = {
            "tenure_months": -0.02,
            "monthly_charges": 0.01,
            "contract_type": -0.2,  # 0 month-to-month, 1 one-year, 2 two-year
        }
        self.bias = 0.3

    def _sigmoid(self, x: float) -> float:
        import math

        return 1.0 / (1.0 + math.exp(-x))

    def predict_one(self, features: Dict[str, float]) -> Tuple[int, float]:
        score = self.bias
        for name, weight in self.coefficients.items():
            score += float(features.get(name, 0.0)) * weight
        prob = float(self._sigmoid(score))
        pred = 1 if prob >= 0.5 else 0
        return pred, prob

    def predict_batch(self, batch: List[Dict[str, float]]) -> Tuple[List[int], List[float]]:
        preds: List[int] = []
        probs: List[float] = []
        for row in batch:
            p, pr = self.predict_one(row)
            preds.append(p)
            probs.append(pr)
        return preds, probs


