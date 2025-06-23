import streamlit as st
import requests

st.title("Corporate Risk Analyzer")

# Input form
company_data = {
    "revenue": st.number_input("Revenue"),
    "expenses": st.number_input("Expenses"),
    "employees": st.number_input("Employee Count")
}

if st.button("Predict Risk"):
    res = requests.post("http://localhost:8000/predict", json=company_data)
    result = res.json()
    st.success(f"Risk Prediction: {result['risk']}")
