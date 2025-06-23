from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# Load the trained model
MODEL_PATH = "artifacts/risk_model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Trained model not found at: {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

# FastAPI app
app = FastAPI(title="Corporate Risk Analyzer API", version="1.0")

# Define expected input structure (replace with all model feature names)
class CompanyData(BaseModel):
    ROA_C_before_interest_and_depreciation_before_interest: float
    persistent_EPS_in_the_Last_Four_Seasons: float
    operating_profit_rate: float
    net_value_per_share_B: float
    quick_ratio: float
    # 👉 Add all features used during training here, in the same order

@app.get("/")
def read_root():
    return {"message": "✅ Corporate Risk Analyzer API is live!"}

@app.post("/predict")
def predict_risk(data: CompanyData):
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([data.dict()])

        # Predict using the loaded model
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        return {
            "risk_prediction": "High" if prediction == 1 else "Low",
            "probability": round(probability, 2),
            "message": "Prediction successful."
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
