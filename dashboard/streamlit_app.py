import streamlit as st
import requests

# Title
st.set_page_config(page_title="Corporate Risk Analyzer")
st.title("📊 Corporate Risk Analyzer")
st.markdown("Predict the risk of bankruptcy based on company financials.")

# Sidebar for API settings
st.sidebar.header("API Configuration")
api_url = st.sidebar.text_input("Backend API URL", "http://127.0.0.1:8000/predict")

# Input fields
st.header("📝 Company Financial Info")

# These must match your model features
form_data = {
    "ROAC_before_interest_and_depreciation_before_interest": st.number_input("Roac Before Interest And Depreciation Before Interest", value=0.02),
    "ROAA_before_interest_and_percent_after_tax": st.number_input("Roaa Before Interest And Percent After Tax", value=0.0),
    "ROAB_before_interest_and_depreciation_after_tax": st.number_input("Roab Before Interest And Depreciation After Tax", value=0.0),
    "Operating_Gross_Margin": st.number_input("Operating Gross Margin", value=0.0),
    "Realized_Sales_Gross_Margin": st.number_input("Realized Sales Gross Margin", value=0.0),
    "Operating_Profit_Rate": st.number_input("Operating Profit Rate", value=0.1),
    "Pre_tax_net_Interest_Rate": st.number_input("Pre Tax Net Interest Rate", value=0.0),
    "After_tax_net_Interest_Rate": st.number_input("After Tax Net Interest Rate", value=0.0),
    "Non_industry_income_and_expenditure_per_revenue": st.number_input("Non Industry Income And Expenditure Per Revenue", value=0.0),
    "Continuous_interest_rate_after_tax": st.number_input("Continuous Interest Rate After Tax", value=0.0),
    "Operating_Expense_Rate": st.number_input("Operating Expense Rate", value=0.0),
    "Research_and_development_expense_rate": st.number_input("Research And Development Expense Rate", value=0.0),
    "Cash_flow_rate": st.number_input("Cash Flow Rate", value=0.0),
    "Interest_bearing_debt_interest_rate": st.number_input("Interest Bearing Debt Interest Rate", value=0.0),
    "Tax_rate_A": st.number_input("Tax Rate A", value=0.0),
    "Net_Value_Per_Share_B": st.number_input("Net Value Per Share B", value=15.0),
    "Net_Value_Per_Share_A": st.number_input("Net Value Per Share A", value=0.0),
    "Net_Value_Per_Share_C": st.number_input("Net Value Per Share C", value=0.0),
    "Persistent_EPS_in_the_Last_Four_Seasons": st.number_input("Persistent Eps In The Last Four Seasons", value=0.03),
    "Cash_Flow_Per_Share": st.number_input("Cash Flow Per Share", value=0.0),
    "Revenue_Per_Share_Yuan": st.number_input("Revenue Per Share Yuan", value=0.0),
    "Operating_Profit_Per_Share_Yuan": st.number_input("Operating Profit Per Share Yuan", value=0.0),
    "Per_Share_Net_profit_before_tax_Yuan": st.number_input("Per Share Net Profit Before Tax Yuan", value=0.0),
    "Realized_Sales_Gross_Profit_Growth_Rate": st.number_input("Realized Sales Gross Profit Growth Rate", value=0.0),
    "Operating_Profit_Growth_Rate": st.number_input("Operating Profit Growth Rate", value=0.0),
    "After_tax_Net_Profit_Growth_Rate": st.number_input("After Tax Net Profit Growth Rate", value=0.0),
    "Regular_Net_Profit_Growth_Rate": st.number_input("Regular Net Profit Growth Rate", value=0.0),
    "Continuous_Net_Profit_Growth_Rate": st.number_input("Continuous Net Profit Growth Rate", value=0.0),
    "Total_Asset_Growth_Rate": st.number_input("Total Asset Growth Rate", value=0.0),
    "Net_Value_Growth_Rate": st.number_input("Net Value Growth Rate", value=0.0),
    "Total_Asset_Return_Growth_Rate_Ratio": st.number_input("Total Asset Return Growth Rate Ratio", value=0.0),
    "Cash_Reinvestment_percent": st.number_input("Cash Reinvestment Percent", value=0.0),
    "Current_Ratio": st.number_input("Current Ratio", value=0.0),
    "Quick_Ratio": st.number_input("Quick Ratio", value=1.2),
    "Interest_Expense_Ratio": st.number_input("Interest_Expense_Ratio", value=0.0),
    "Total_debt_per_Total_net_worth": st.number_input("Total_debt_per_Total_net_worth", value=0.0),
    "Debt_ratio_percent": st.number_input("Debt_ratio_percent", value=0.0),
    "Net_worth_per_Assets": st.number_input("Net_worth_per_Assets", value=0.0),
    "Long_term_fund_suitability_ratio_A": st.number_input("Long_term_fund_suitability_ratio_A", value=0.0),
    "Borrowing_dependency": st.number_input("Borrowing_dependency", value=0.0),
    "Contingent_liabilities_per_Net_worth": st.number_input("Contingent_liabilities_per_Net_worth", value=0.0),
    "Operating_profit_per_Paid_in_capital": st.number_input("Operating_profit_per_Paid_in_capital", value=0.0),
    "Net_profit_before_tax_per_Paid_in_capital": st.number_input("Net_profit_before_tax_per_Paid_in_capital", value=0.0),
    "Inventory_and_accounts_receivable_per_Net_value": st.number_input("Inventory_and_accounts_receivable_per_Net_value", value=0.0),
    "Total_Asset_Turnover": st.number_input("Total_Asset_Turnover", value=0.0),
    "Accounts_Receivable_Turnover": st.number_input("Accounts_Receivable_Turnover", value=0.0),
    "Average_Collection_Days": st.number_input("Average_Collection_Days", value=0.0),
    "Inventory_Turnover_Rate_times": st.number_input("Inventory_Turnover_Rate_times", value=0.0),
    "Fixed_Assets_Turnover_Frequency": st.number_input("Fixed_Assets_Turnover_Frequency", value=0.0),
    "Net_Worth_Turnover_Rate_times": st.number_input("Net_Worth_Turnover_Rate_times", value=0.0),
    "Revenue_per_person": st.number_input("Revenue_per_person", value=0.0),
    "Operating_profit_per_person": st.number_input("Operating_profit_per_person", value=0.0),
    "Allocation_rate_per_person": st.number_input("Allocation_rate_per_person", value=0.0),
    "Working_Capital_to_Total_Assets": st.number_input("Working_Capital_to_Total_Assets", value=0.0),
    "Quick_Assets_per_Total_Assets": st.number_input("Quick_Assets_per_Total_Assets", value=0.0),
    "Current_Assets_per_Total_Assets": st.number_input("Current_Assets_per_Total_Assets", value=0.0),
    "Cash_per_Total_Assets": st.number_input("Cash_per_Total_Assets", value=0.0),
    "Quick_Assets_per_Current_Liability": st.number_input("Quick_Assets_per_Current_Liability", value=0.0),
    "Cash_per_Current_Liability": st.number_input("Cash_per_Current_Liability", value=0.0),
    "Current_Liability_to_Assets": st.number_input("Current_Liability_to_Assets", value=0.0),
    "Operating_Funds_to_Liability": st.number_input("Operating_Funds_to_Liability", value=0.0),
    "Inventory_per_Working_Capital": st.number_input("Inventory_per_Working_Capital", value=0.0),
    "Inventory_per_Current_Liability": st.number_input("Inventory_per_Current_Liability", value=0.0),
    "Current_Liabilities_per_Liability": st.number_input("Current_Liabilities_per_Liability", value=0.0),
    "Working_Capital_per_Equity": st.number_input("Working_Capital_per_Equity", value=0.0),
    "Current_Liabilities_per_Equity": st.number_input("Current_Liabilities_per_Equity", value=0.0),
    "Long_term_Liability_to_Current_Assets": st.number_input("Long_term_Liability_to_Current_Assets", value=0.0),
    "Retained_Earnings_to_Total_Assets": st.number_input("Retained_Earnings_to_Total_Assets", value=0.0),
    "Total_income_per_Total_expense": st.number_input("Total_income_per_Total_expense", value=0.0),
    "Total_expense_per_Assets": st.number_input("Total_expense_per_Assets", value=0.0),
    "Current_Asset_Turnover_Rate": st.number_input("Current_Asset_Turnover_Rate", value=0.0),
    "Quick_Asset_Turnover_Rate": st.number_input("Quick_Asset_Turnover_Rate", value=0.0),
    "Working_capitcal_Turnover_Rate": st.number_input("Working_capitcal_Turnover_Rate", value=0.0),
    "Cash_Turnover_Rate": st.number_input("Cash_Turnover_Rate", value=0.0),
    "Cash_Flow_to_Sales": st.number_input("Cash_Flow_to_Sales", value=0.0),
    "Fixed_Assets_to_Assets": st.number_input("Fixed_Assets_to_Assets", value=0.0),
    "Current_Liability_to_Liability": st.number_input("Current_Liability_to_Liability", value=0.0),
    "Current_Liability_to_Equity": st.number_input("Current_Liability_to_Equity", value=0.0),
    "Equity_to_Long_term_Liability": st.number_input("Equity_to_Long_term_Liability", value=0.0),
    "Cash_Flow_to_Total_Assets": st.number_input("Cash_Flow_to_Total_Assets", value=0.0),
    "Cash_Flow_to_Liability": st.number_input("Cash_Flow_to_Liability", value=0.0),
    "CFO_to_Assets": st.number_input("CFO_to_Assets", value=0.0),
    "Cash_Flow_to_Equity": st.number_input("Cash_Flow_to_Equity", value=0.0),
    "Current_Liability_to_Current_Assets": st.number_input("Current_Liability_to_Current_Assets", value=0.0),
    "Liability_Assets_Flag": st.number_input("Liability_Assets_Flag", value=0.0),
    "Net_Income_to_Total_Assets": st.number_input("Net_Income_to_Total_Assets", value=0.0),
    "Total_assets_to_GNP_price": st.number_input("Total_assets_to_GNP_price", value=0.0),
    "No_credit_Interval": st.number_input("No_credit_Interval", value=0.0),
    "Gross_Profit_to_Sales": st.number_input("Gross_Profit_to_Sales", value=0.0),
    "Net_Income_to_Stockholders_Equity": st.number_input("Net_Income_to_Stockholders_Equity", value=0.0),
    "Liability_to_Equity": st.number_input("Liability_to_Equity", value=0.0),
    "Degree_of_Financial_Leverage_DFL": st.number_input("Degree_of_Financial_Leverage_DFL", value=0.0),
    "Interest_Coverage_Ratio_Interest_expense_to_EBIT": st.number_input("Interest_Coverage_Ratio_Interest_expense_to_EBIT", value=0.0),
    "Net_Income_Flag": st.number_input("Net_Income_Flag", value=0.0),
    "Equity_to_Liability": st.number_input("Equity_to_Liability", value=0.0)
}


# Submit
if st.button("🔍 Analyze Risk"):
    try:
        with st.spinner("Sending data to API..."):
            response = requests.post(api_url, json=form_data)
            if response.status_code == 200:
                result = response.json()
                st.success(f"Risk Prediction: **{result['risk_prediction']}**")
                st.info(f"Confidence Score: **{result['probability']}**")
            else:
                st.error(f"API Error: {response.status_code} - {response.json().get('detail')}")
    except Exception as e:
        st.error(f"Request failed: {e}")
