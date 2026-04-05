# Zomato vs Swiggy: Alternative Data Analysis

## Objective
The goal of this project was to evaluate Zomato’s market position using alternative data sources that reflect both product strength and consumer demand. This was done using a YipitData-style approach by combining app-platform data with Google Trends data.

## Data Sources
1. Google Play Store Kaggle dataset  
   - Used to extract Zomato’s app-level metrics such as installs, rating, and reviews  

2. Google Trends  
   - Used to compare search interest for Zomato and Swiggy over time in India  

## Data Validation and Cleaning
The Play Store dataset was first validated for company coverage. Zomato was present, but Swiggy was not available in the dataset. Instead of forcing an incomplete comparison, Google Trends was used as a secondary data source to evaluate relative consumer interest between Zomato and Swiggy.

Data cleaning steps included:
- converting installs from text format (e.g., "10,000,000+") into numeric values  
- converting reviews and ratings into numeric fields  
- removing invalid or missing rows  
- converting trend dates into datetime format  
- removing incomplete trend records  

## Key Findings

### 1. Zomato product strength
Zomato demonstrates strong product-level performance based on Play Store metrics. The app shows approximately **20 million installs**, an average rating of **4.3**, and over **1.02 million reviews**.

This indicates high user adoption and sustained engagement, suggesting that Zomato maintains a strong consumer-facing product.

### 2. Market interest comparison
Google Trends data shows that the latest search interest for both Zomato and Swiggy is **equal (13 vs 13)**.

This suggests that both platforms currently have similar levels of consumer attention.

### 3. Growth trend
Over the observed time period:
- Zomato’s search interest decreased by **3 points**
- Swiggy’s search interest decreased by **2 points**

This indicates a **slight decline in overall demand for both platforms**, with Swiggy showing marginally better stability in search interest.

## Business Interpretation
The analysis suggests that while Zomato maintains a strong product foundation with high installs and engagement, its growth momentum in terms of consumer search interest appears to be slightly declining.

At the same time, Swiggy demonstrates comparable market interest and slightly more stable trend performance. This could indicate increasing competition and potential market saturation in the food delivery space.

Overall, Zomato appears to be a **stable but not rapidly growing player**, with competitive pressure from Swiggy.

## Relevance:
This project reflects key aspects of a data-product and alternative data workflow:

- working with incomplete and messy real-world datasets  
- validating data coverage before analysis  
- supplementing missing data with a secondary signal (Google Trends)  
- translating raw metrics into business-relevant insights  

This mirrors how institutional data products are built to inform investment decisions.

## Next Improvements
Future enhancements to this analysis could include:

- scraping live Play Store reviews for both Zomato and Swiggy  
- performing sentiment analysis on customer reviews  
- analyzing trends at a monthly or quarterly level  
- building a dashboard or investor-style summary  

## Customer Sentiment Analysis

Live Play Store reviews were collected for both Zomato and Swiggy to understand user satisfaction levels.

A total of 2000 recent reviews were analyzed for each platform.

The sentiment distribution showed:

- Zomato: 1603 positive vs 397 negative reviews (~80% positive)
- Swiggy: 1226 positive vs 774 negative reviews (~61% positive)

This indicates that Zomato users report significantly higher satisfaction compared to Swiggy users.

## Combined Insight

While Google Trends shows that both Zomato and Swiggy currently have similar levels of search interest, the sentiment analysis reveals a key difference in user experience.

Zomato demonstrates:
- stronger product engagement (high installs and reviews)
- higher customer satisfaction (~80% positive sentiment)

Swiggy, despite having comparable market interest, shows:
- lower customer satisfaction (~61% positive sentiment)
- higher proportion of negative feedback

## Final Business Conclusion

Zomato appears to be a **stronger product-driven platform with better user satisfaction**, even though overall market demand for both platforms shows slight decline.

This suggests that:
- Zomato is better positioned in terms of **customer experience and retention**
- Swiggy may be facing **product or service-related challenges**

From an investment or strategic perspective, Zomato demonstrates **stronger underlying user sentiment**, which can be a leading indicator of long-term stability.