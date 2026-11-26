from pathlib import Path

import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd

from urlSplit import extraction_features, NUM_COLS

app = FastAPI(title="Phishing link prediction", description="Phishing link or not prediction model with probabilty")

MODEL_PATH = Path(__file__).resolve().parent.parent