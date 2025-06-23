import shap
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model and data
model = joblib.load("artifacts/risk_model.pkl")
df = pd.read_csv("data/cleaned_data.csv")
X = df.drop("Bankrupt?", axis=1)

# Use SHAP
explainer = shap.Explainer(model)
shap_values = explainer(X[:100])

# Plot explanation for one sample
shap.plots.waterfall(shap_values[0])

# Or summary plot for top features
shap.summary_plot(shap_values, X)
