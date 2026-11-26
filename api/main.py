from pathlib import Path

import joblib
from fastapi import FastAPI, responses
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import pandas as pd

from urlSplit import extraction_features, NUM_COLS

app = FastAPI(title="Phishing link prediction", description="Phishing link or not prediction model with probabilty")

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "xgb_phishing.joblib"
model = joblib.load(MODEL_PATH)

@app.get("/")
def index():
    return {"message" : "Welcome home page"}

@app.get("/health")
def health():
    return JSONResponse(status_code=200, content={"status": "ok"})

