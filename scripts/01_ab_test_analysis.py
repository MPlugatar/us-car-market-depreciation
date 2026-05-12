import pandas as pd
from scipy import stats

# ==========================================
# STEP 1: Data Loading & Sanity Check
# ==========================================
print("--- Step 1: Data Loading ---")

df = pd.read_csv("raw_cars_for_stats.csv")
print(f"Initial dataset size: {df.shape[0]} rows")

print("\nFuel type distribution (Raw):")
print(df["fuel_type"].value_counts())

# ==========================================
# STEP 2: Data Cleaning & Filtering
# ==========================================
print("\n--- Step 2: Sample Cleaning ---")

# Filter out low-volume models (N < 30) to ensure statistical reliability
# and eliminate edge-case outliers.
df_clean = df.groupby("model").filter(lambda x: len(x) >= 30)

print(f"Dataset size after dropping rare models: {df_clean.shape[0]} rows")

print("\nFuel type distribution (A/B Test ready):")
print(df_clean["fuel_type"].value_counts())

# ==========================================
# STEP 3: Cohort Definition & EDA
# ==========================================
print("\n--- Step 3: Cohort Analysis ---")

ice_drops = df_clean[df_clean["fuel_type"] == "gasoline"]["drop_percent"]
ev_drops = df_clean[df_clean["fuel_type"] == "electric"]["drop_percent"]

print(f"Average depreciation (ICE): {ice_drops.mean():.2f}%")
print(f"Average depreciation (EV): {ev_drops.mean():.2f}%")

# ==========================================
# STEP 4: Statistical Validation (Welch's T-test)
# ==========================================
print("\n--- Step 4: Statistical Testing ---")

# Using Welch's T-test (equal_var=False) due to significantly different sample sizes
t_stat, p_value = stats.ttest_ind(ice_drops, ev_drops, equal_var=False)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.10f}")

# ==========================================
# STEP 5: Business Conclusion
# ==========================================
print("\n--- BUSINESS CONCLUSION ---")

if p_value < 0.05:
    print("Result: Statistically SIGNIFICANT difference (p < 0.05)")
    print(
        "Insight: EVs and ICE vehicles exhibit fundamentally different depreciation patterns."
    )
    print(
        "Actionable: Safe to use fuel type as a reliable predictor for residual value modeling."
    )
else:
    print("Result: NOT statistically significant (p >= 0.05)")
    print(
        "Insight: Failed to reject the null hypothesis. The observed difference might be random noise."
    )
