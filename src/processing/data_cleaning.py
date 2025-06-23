import pandas as pd
from sklearn.preprocessing import StandardScaler

def clean_data(filepath="./data/company_data.csv", save_path="./data/cleaned_data.csv"):
    df = pd.read_csv(filepath)
    
    # Drop rows with missing values
    df.dropna(inplace=True)

    # Separate features and target
    X = df.drop(columns=["Bankrupt?"])
    y = df["Bankrupt?"]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Recombine
    df_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    df_scaled["Bankrupt?"] = y.values

    # Save cleaned data
    df_scaled.to_csv(save_path, index=False)
    print(f"✅ Cleaned data saved to {save_path}")

if __name__ == "__main__":
    clean_data()
