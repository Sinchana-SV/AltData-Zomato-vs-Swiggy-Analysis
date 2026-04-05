import os
import pandas as pd
import matplotlib.pyplot as plt

# Create visuals folder if it doesn't exist
os.makedirs("visuals", exist_ok=True)

# -----------------------------
# 1. Load datasets
# -----------------------------
apps = pd.read_csv("data/processed/cleaned_apps.csv")
trends = pd.read_csv("data/processed/cleaned_trends.csv")
reviews = pd.read_csv("data/raw/live_reviews.csv")

# Convert date column
trends["date"] = pd.to_datetime(trends["date"], errors="coerce")
trends = trends.dropna(subset=["date"])

# -----------------------------
# 2. Zomato app metrics chart
# -----------------------------
zomato = apps[apps["App"].str.contains("Zomato", case=False, na=False)]

avg_rating = zomato["Rating"].mean()
total_reviews = zomato["Reviews"].sum()
total_installs = zomato["Installs"].sum()

# -----------------------------
# 2A. Rating chart (separate)
# -----------------------------
plt.figure(figsize=(6, 4))
plt.bar(["Zomato Rating"], [avg_rating])
plt.title("Zomato Average Rating")
plt.ylabel("Rating (out of 5)")
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig("visuals/zomato_rating.png")
plt.close()

# -----------------------------
# 2B. Engagement chart
# -----------------------------
engagement_metrics = ["Total Reviews", "Total Installs"]
engagement_values = [total_reviews, total_installs]

plt.figure(figsize=(8, 5))
plt.bar(engagement_metrics, engagement_values)
plt.title("Zomato Engagement Metrics")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("visuals/zomato_engagement.png")
plt.close()

# -----------------------------
# 3. Google Trends line chart
# -----------------------------
plt.figure(figsize=(10, 5))
plt.plot(trends["date"], trends["Zomato"], label="Zomato")
plt.plot(trends["date"], trends["Swiggy"], label="Swiggy")
plt.title("Google Trends: Zomato vs Swiggy")
plt.xlabel("Date")
plt.ylabel("Search Interest")
plt.legend()
plt.tight_layout()
plt.savefig("visuals/google_trends_comparison.png")
plt.close()

# -----------------------------
# 4. Sentiment breakdown
# -----------------------------
reviews["sentiment"] = reviews["score"].apply(
    lambda x: "positive" if x >= 4 else "negative"
)

sentiment_counts = pd.crosstab(reviews["company"], reviews["sentiment"])

sentiment_counts.plot(kind="bar", figsize=(8, 5))
plt.title("Sentiment Breakdown: Zomato vs Swiggy")
plt.xlabel("Company")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("visuals/sentiment_breakdown.png")
plt.close()

# -----------------------------
# 5. Positive sentiment %
# -----------------------------
positive_pct = (
    sentiment_counts["positive"] /
    (sentiment_counts["positive"] + sentiment_counts["negative"])
) * 100

plt.figure(figsize=(8, 5))
plt.bar(positive_pct.index, positive_pct.values)
plt.title("Positive Sentiment Percentage")
plt.xlabel("Company")
plt.ylabel("Positive Review %")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("visuals/positive_sentiment_percentage.png")
plt.close()

print("Visuals created successfully!")
print("Saved files:")
print("- visuals/zomato_app_metrics.png")
print("- visuals/google_trends_comparison.png")
print("- visuals/sentiment_breakdown.png")
print("- visuals/positive_sentiment_percentage.png")