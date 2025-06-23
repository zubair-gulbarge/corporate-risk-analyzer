from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model/risk_model.pkl")

@app.get("/")
def read_root():
    return {"message": "Corporate Risk Analyzer API"}

@app.post("/predict")
def predict_risk(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return {"risk": "High" if prediction == 1 else "Low"}
