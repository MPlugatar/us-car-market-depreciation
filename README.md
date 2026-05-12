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

![Dashboard ICE](https://raw.githubusercontent.com/MPlugatar/us-car-market-depreciation/refs/heads/main/highest%20price%20drop%20visualisation.png)

*Comparison with the EV market:*

![Dashboard EV](https://raw.githubusercontent.com/MPlugatar/us-car-market-depreciation/refs/heads/main/EV%20cars%20top%20price%20drop.png)

---
*Check out the full logic in the `analysis.sql` file.*
