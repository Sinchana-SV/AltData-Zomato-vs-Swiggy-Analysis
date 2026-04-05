import pandas as pd

# Load cleaned data
apps = pd.read_csv("data/processed/cleaned_apps.csv")
trends = pd.read_csv("data/processed/cleaned_trends.csv")

print("APPS DATA:")
print(apps)

print("\nTRENDS DATA:")
print(trends.head())

print("\n--- ZOMATO PRODUCT METRICS ---")

zomato = apps[apps['App'].str.contains("Zomato", case=False)]

print("Total Zomato entries:", len(zomato))
print("Average Rating:", zomato['Rating'].mean())
print("Total Reviews:", zomato['Reviews'].sum())
print("Total Installs:", zomato['Installs'].sum())

print("\n--- TREND ANALYSIS ---")

# Latest values
latest = trends.iloc[-1]

print("Latest Zomato interest:", latest['Zomato'])
print("Latest Swiggy interest:", latest['Swiggy'])

print("\n--- MARKET COMPARISON ---")

if latest['Zomato'] > latest['Swiggy']:
    print("Zomato has higher current search interest")
else:
    print("Swiggy has higher current search interest")

print("\n--- GROWTH TREND ---")

# Compare first vs last
first = trends.iloc[0]

zomato_growth = latest['Zomato'] - first['Zomato']
swiggy_growth = latest['Swiggy'] - first['Swiggy']

print("Zomato growth:", zomato_growth)
print("Swiggy growth:", swiggy_growth)

with open("report/insights.txt", "w") as f:
    f.write("ZOMATO ANALYSIS\n")
    f.write(f"Average Rating: {zomato['Rating'].mean()}\n")
    f.write(f"Total Reviews: {zomato['Reviews'].sum()}\n")
    f.write(f"Total Installs: {zomato['Installs'].sum()}\n\n")

    f.write("MARKET TRENDS\n")
    f.write(f"Latest Zomato Interest: {latest['Zomato']}\n")
    f.write(f"Latest Swiggy Interest: {latest['Swiggy']}\n")
    f.write(f"Zomato Growth: {zomato_growth}\n")
    f.write(f"Swiggy Growth: {swiggy_growth}\n")

print("\nInsights saved to report/insights.txt")