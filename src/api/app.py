from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# Constants
MODEL_PATH = "artifacts/risk_model.pkl"

# Load trained model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Trained model not found at: {MODEL_PATH}")

try:
    model = joblib.load(MODEL_PATH)
    print("✅ Model loaded successfully.")
except Exception as e:
    raise RuntimeError(f"❌ Failed to load model: {str(e)}")

# FastAPI app
app = FastAPI(
    title="Corporate Risk Analyzer API",
    version="1.0",
    description="An API for predicting company bankruptcy risk"
)

# Input schema (✅ Replace/add all features used in training)
class CompanyData(BaseModel):
    ROA_C_before_interest_and_depreciation_before_interest: float
    ROA_A_before_interest_and_percent_after_tax: float
    ROA_B_before_interest_and_depreciation_after_tax: float
    Operating_Gross_Margin: float
    Realized_Sales_Gross_Margin: float
    Operating_Profit_Rate: float
    Pre_tax_net_Interest_Rate: float
    After_tax_net_Interest_Rate: float
    Non_industry_income_and_expenditure_per_revenue: float
    Continuous_interest_rate_after_tax: float
    Operating_Expense_Rate: float
    Research_and_development_expense_rate: float
    Cash_flow_rate: float
    Interest_bearing_debt_interest_rate: float
    Tax_rate_A: float
    Net_Value_Per_Share_B: float
    Net_Value_Per_Share_A: float
    Net_Value_Per_Share_C: float
    Persistent_EPS_in_the_Last_Four_Seasons: float
    Cash_Flow_Per_Share: float
    Revenue_Per_Share_Yuan: float
    Operating_Profit_Per_Share_Yuan: float
    Per_Share_Net_profit_before_tax_Yuan: float
    Realized_Sales_Gross_Profit_Growth_Rate: float
    Operating_Profit_Growth_Rate: float
    After_tax_Net_Profit_Growth_Rate: float
    Regular_Net_Profit_Growth_Rate: float
    Continuous_Net_Profit_Growth_Rate: float
    Total_Asset_Growth_Rate: float
    Net_Value_Growth_Rate: float
    Total_Asset_Return_Growth_Rate_Ratio: float
    Cash_Reinvestment_percent: float
    Current_Ratio: float
    Quick_Ratio: float
    Interest_Expense_Ratio: float
    Total_debt_to_Total_net_worth: float
    Debt_ratio_percent: float
    Net_worth_to_Assets: float
    Long_term_fund_suitability_ratio_A: float
    Borrowing_dependency: float
    Contingent_liabilities_to_Net_worth: float
    Operating_profit_to_Paid_in_capital: float
    Net_profit_before_tax_to_Paid_in_capital: float
    Inventory_and_accounts_receivable_to_Net_value: float
    Total_Asset_Turnover: float
    Accounts_Receivable_Turnover: float
    Average_Collection_Days: float
    Inventory_Turnover_Rate: float
    Fixed_Assets_Turnover_Frequency: float
    Net_Worth_Turnover_Rate: float
    Revenue_per_person: float
    Operating_profit_per_person: float
    Allocation_rate_per_person: float
    Working_Capital_to_Total_Assets: float
    Quick_Assets_to_Total_Assets: float
    Current_Assets_to_Total_Assets: float
    Cash_to_Total_Assets: float
    Quick_Assets_to_Current_Liability: float
    Cash_to_Current_Liability: float
    Current_Liability_to_Assets: float
    Operating_Funds_to_Liability: float
    Inventory_to_Working_Capital: float
    Inventory_to_Current_Liability: float
    Current_Liabilities_to_Liability: float
    Working_Capital_to_Equity: float
    Current_Liabilities_to_Equity: float
    Long_term_Liability_to_Current_Assets: float
    Retained_Earnings_to_Total_Assets: float
    Total_income_to_Total_expense: float
    Total_expense_to_Assets: float
    Current_Asset_Turnover_Rate: float
    Quick_Asset_Turnover_Rate: float
    Working_capitcal_Turnover_Rate: float
    Cash_Turnover_Rate: float
    Cash_Flow_to_Sales: float
    Fixed_Assets_to_Assets: float
    Current_Liability_to_Liability: float
    Current_Liability_to_Equity: float
    Equity_to_Long_term_Liability: float
    Cash_Flow_to_Total_Assets: float
    Cash_Flow_to_Liability: float
    CFO_to_Assets: float
    Cash_Flow_to_Equity: float
    Current_Liability_to_Current_Assets: float
    Liability_Assets_Flag: float
    Net_Income_to_Total_Assets: float
    Total_assets_to_GNP_price: float
    No_credit_Interval: float
    Gross_Profit_to_Sales: float
    Net_Income_to_Stockholders_Equity: float
    Liability_to_Equity: float
    Degree_of_Financial_Leverage: float
    Interest_Coverage_Ratio: float
    Net_Income_Flag: float
    Equity_to_Liability: float


@app.get("/")
def read_root():
    return {"message": "✅ Corporate Risk Analyzer API is live!"}

@app.post("/predict")
def predict_risk(data: CompanyData):
    try:
        # Convert request to DataFrame
        input_df = pd.DataFrame([data.dict()])
        print("📥 Input to model:\n", input_df)

        # Perform prediction
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        # Return formatted result
        return {
            "risk_prediction": "High" if prediction == 1 else "Low",
            "probability": round(probability, 2),
            "message": "✅ Prediction successful"
        }

    except Exception as e:
        print("❌ Prediction error:", str(e))
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
