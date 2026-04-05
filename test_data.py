import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/google_play_store.csv")

# Show first 5 rows
print("FIRST 5 ROWS:")
print(df.head())

# Show columns
print("\nCOLUMNS:")
print(df.columns)

# Show shape
print("\nSHAPE:")
print(df.shape)