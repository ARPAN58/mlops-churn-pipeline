<<<<<<< HEAD
# Churn Prediction MLOps (FastAPI + Docker + GitHub Actions + Cloud Run)

Production-ready skeleton for a churn prediction API with CI/CD.

## Quickstart (local)

1. Create venv and install
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .venv\\Scripts\\Activate.ps1
     pip install -U pip
     pip install -r requirements.txt -r requirements-dev.txt
     ```
2. Run app
   ```powershell
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
3. Open docs: http://localhost:8000/docs

## Tests
```powershell
pytest
```

## Docker
```powershell
docker build -t churn-api:local .
docker run -p 8000:8000 churn-api:local
```

## Deploy to Cloud Run (GitHub Actions)
- Configure repo secrets: `GCP_PROJECT_ID`, `GCP_REGION`, `GCP_SA_KEY_JSON`
- Push to `main`. The workflow builds, tests, pushes image to GAR, deploys.


=======
# mlops-churn-pipeline
>>>>>>> e05a4f2aca2042443d2e0b8c061b2924bcab373e
