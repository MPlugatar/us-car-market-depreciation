# 🚗 US Car Market Depreciation Analysis: EV vs ICE

## 📌 Project Overview
This project analyzes the secondary car market in the US to determine which vehicles depreciate the fastest over a 5-year period. The primary goal was to test the hypothesis and compare the residual value of Internal Combustion Engine (ICE) vehicles versus Electric Vehicles (EV).

## 🛠 Tools & Technologies
* **Database:** SQLite (DBeaver)
* **Visualization:** Tableau Public
* **Querying:** CTEs, Advanced JOINs, Aggregation, Data Cleaning

## 📂 Dataset
The raw data consists of over 760,000 car listings from the US market. 

## 🧹 Data Cleaning (ETL)
The initial dataset contained significant noise. I wrote SQL scripts to filter out anomalies:
* Removed rows with `NULL` prices, years, or mileage.
* Filtered out fake/erroneous listings (prices outside the $2,000 - $150,000 range).
* Removed extreme mileage outliers (retained only 1,000 - 300,000 miles).
* Cleaned and standardized fuel types using string manipulation `TRIM(LOWER())`.
* **Result:** Reduced the dataset to ~702,000 clean, reliable rows.

## 📊 Methodology (Feature Engineering)
To calculate the 5-year depreciation drop, I used Common Table Expressions (CTEs):
1. Created a `new_cars` virtual table for recent models (2022-2023).
2. Created a `used_cars` virtual table for 5-year-old models (2018).
3. Merged them using an `INNER JOIN` on three keys: `brand`, `model`, and `fuel_type`.
4. Calculated the percentage drop: `((New Price - Used Price) / New Price) * 100`.

## 💡 Key Insights & Findings
1. **Premium ICE loses value rapidly:** Luxury gasoline SUVs and sedans (e.g., Cadillac Escalade, BMW 5/7 Series) are the absolute leaders in depreciation, losing up to **60-62%** of their value in just 5 years.
2. **EVs hold value surprisingly well:** Despite market stereotypes, established EVs like the Tesla Model 3 showed strong retention, dropping only around **18-25%** over the same period.

## 📈 Visualizations
*Here is the dashboard showing the top US models depreciating the fastest over 5 years:*

![Dashboard ICE](https://raw.githubusercontent.com/MPlugatar/us-car-market-depreciation/refs/heads/main/images/highest%20price%20drop%20visualisation.png)

*Comparison with the EV market:*

![Dashboard EV](https://raw.githubusercontent.com/MPlugatar/us-car-market-depreciation/refs/heads/main/images/EV%20cars%20top%20price%20drop.png)

---
*Check out the full logic in the `analysis.sql` file.*

## 🔬 V2: Statistical Validation (A/B Testing)

To ensure the observed 9% difference in depreciation isn't due to the disparity in sample sizes (~30,000 ICE vehicles vs ~400 EVs), a Welch's T-test was conducted. 

**Files used for this iteration:**
* [`v2_extract_for_ab_test.sql`](sql/02_extract_for_ab_test.sql) - Query to extract raw, unaggregated data for 2018 vehicles.
* [`stats_analysis.py`](scripts/01_ab_test_analysis.py) - Python script using `pandas` for filtering and `scipy.stats` for the A/B test.

**Results:**
* **ICE Average Depreciation:** 34.7%
* **EV Average Depreciation:** 25.6%
* **T-statistic:** 22.99
* **P-value:** < 0.001

**Conclusion:** The difference is statistically significant (p < 0.05). However, a critical analytical limitation was identified during the process.

## ⚠️ Limitations & V3 Roadmap (Stratified Analysis)

While the math proves EV prices drop slower in this specific dataset, there is a strong confounding variable: **Price Segment / Vehicle Class**. 
EVs from 2018 are predominantly premium/expensive vehicles, whereas the ICE dataset includes thousands of budget-friendly economy cars. The slower depreciation of EVs might be attributed to their premium status rather than their fuel type.

**Next Steps for V3 Iteration:**
1. Calculate the average MSRP of the EV cohort.
2. Filter the ICE dataset to only include vehicles within the exact same price tier (Apple-to-Apple comparison).
3. Re-run the A/B test strictly within this controlled price segment.
