from pytrends.request import TrendReq
import pandas as pd

# Connect to Google Trends
pytrends = TrendReq(hl='en-US', tz=330)

# Keywords we want to compare
keywords = ["Zomato", "Swiggy"]

# Build request
pytrends.build_payload(keywords, timeframe='today 5-y', geo='IN')

# Get trends over time
trends_df = pytrends.interest_over_time()

# Remove 'isPartial' column if it exists
if 'isPartial' in trends_df.columns:
    trends_df = trends_df.drop(columns=['isPartial'])

# Reset index so date becomes a normal column
trends_df = trends_df.reset_index()

# Save file
trends_df.to_csv("data/raw/google_trends.csv", index=False)

print("Google Trends data saved!")
print(trends_df.head())
print(trends_df.shape)
print(trends_df.columns)