import pandas as pd

# Load data
df = pd.read_csv("data/raw/google_play_store.csv")

print("Before Cleaning:")
print(df.head())

# Clean Installs column
df['Installs'] = df['Installs'].str.replace(',', '')
df['Installs'] = df['Installs'].str.replace('+', '')
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

df = df.dropna(subset=['Installs', 'Reviews', 'Rating'])

df_filtered = df[df['App'].str.contains("Zomato|Swiggy", case=False, na=False)]

print("\nFiltered Data:")
print(df_filtered[['App', 'Installs', 'Rating', 'Reviews']])

df_filtered.to_csv("data/processed/cleaned_apps.csv", index=False)

print("\nSaved cleaned data!")

print("\nApps containing 'swig':")
print(df[df['App'].str.contains("swig", case=False, na=False)][['App', 'Installs', 'Rating', 'Reviews']])

print("\nApps containing 'zomato':")
print(df[df['App'].str.contains("zomato", case=False, na=False)][['App', 'Installs', 'Rating', 'Reviews']])