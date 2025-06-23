import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv("data/sample.csv")  # Replace with actual data path

# Preprocess
X = df.drop("bankrupt", axis=1)
y = df["bankrupt"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save model
joblib.dump(clf, "model/risk_model.pkl")
