import pandas as pd

# Load Google Trends data
df = pd.read_csv("data/raw/google_trends.csv")

print("FIRST 5 ROWS:")
print(df.head())

print("\nCOLUMNS:")
print(df.columns)

print("\nSHAPE:")
print(df.shape)

print("\nMISSING VALUES:")
print(df.isnull().sum())

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Drop rows where date is missing
df = df.dropna(subset=["date"])

# Convert keyword columns to numbers
df["Zomato"] = pd.to_numeric(df["Zomato"], errors="coerce")
df["Swiggy"] = pd.to_numeric(df["Swiggy"], errors="coerce")

# Drop rows with missing trend values
df = df.dropna(subset=["Zomato", "Swiggy"])

# Save cleaned trends data
df.to_csv("data/processed/cleaned_trends.csv", index=False)

print("\nCLEANED DATA PREVIEW:")
print(df.head())

print("\nSaved cleaned trends data!")