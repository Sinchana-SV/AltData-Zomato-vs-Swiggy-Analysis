from google_play_scraper import reviews
import pandas as pd
import os

# Create folder
os.makedirs("data/raw", exist_ok=True)

# HARDCODED app IDs (more reliable)
APPS = {
    "zomato": "com.application.zomato",
    "swiggy": "in.swiggy.android"
}

all_reviews = []

for company, app_id in APPS.items():
    print(f"\nFetching {company} reviews...")

    try:
        result, _ = reviews(
            app_id,
            lang='en',
            country='in',
            count=2000
        )

        df = pd.DataFrame(result)

        if df.empty:
            print(f"No reviews found for {company}")
            continue

        df = df[['content', 'score', 'at']]
        df['company'] = company

        all_reviews.append(df)

        print(f"{company}: {len(df)} reviews collected")

    except Exception as e:
        print(f"Error fetching {company}: {e}")

# Combine
if all_reviews:
    final_df = pd.concat(all_reviews, ignore_index=True)
    final_df.to_csv("data/raw/live_reviews.csv", index=False)
    print("\nSaved live_reviews.csv successfully!")
else:
    print("No data collected.")