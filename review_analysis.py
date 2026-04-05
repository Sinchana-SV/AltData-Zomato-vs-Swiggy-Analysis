import pandas as pd

df = pd.read_csv("data/raw/live_reviews.csv")

print("\n--- REVIEW SUMMARY ---")

# Average rating
print(df.groupby('company')['score'].mean())

# Total reviews
print("\nTotal reviews:")
print(df['company'].value_counts())

# Positive vs negative
df['sentiment'] = df['score'].apply(lambda x: 'positive' if x >= 4 else 'negative')

print("\nSentiment breakdown:")
print(pd.crosstab(df['company'], df['sentiment']))