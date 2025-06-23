# src/model/train_model.py

import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix

def train():
    # Load the cleaned dataset
    df = pd.read_csv("data/cleaned_data.csv")

    # Split features and target
    X = df.drop("Bankrupt?", axis=1)
    y = df["Bankrupt?"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    # Train a model (you can swap with RandomForestClassifier())
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Ensure artifacts directory exists
    os.makedirs("artifacts", exist_ok=True)

    # Save model
    joblib.dump(model, "artifacts/risk_model.pkl")
    print("✅ Model saved to artifacts/risk_model.pkl")

if __name__ == "__main__":
    train()
