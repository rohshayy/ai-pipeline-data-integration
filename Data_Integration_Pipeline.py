import pandas as pd
import numpy as np

# --- STEP 0: Setup Dummy Data (For demonstration) ---
data_a = {
    'Student_ID': [101, 102, 103],
    'Math_Score': [85, np.nan, 90],
    'Physics_Score': [88, 76, np.nan]
}
data_b = {
    'Student_ID': [104, 105, 106],
    'Math_Score': [70, 95, np.nan],
    'Physics_Score': [np.nan, 82, 89]
}
df_extra_info = pd.DataFrame({
    'Student_ID': [101, 102, 103, 104, 105, 106],
    'City': ['New York', 'London', 'New York', 'Paris', 'London', 'Paris']
})

branch_a = pd.DataFrame(data_a)
branch_b = pd.DataFrame(data_b)

# --- STEP 1: Load & Stack (Concatenate) ---
# We stack Branch A on top of Branch B
university_df = pd.concat([branch_a, branch_b], ignore_index=True)
print("--- Unified University Data ---")
print(university_df, "\n")

# --- STEP 2: The Merge Challenge ---
# Left join ensures we keep all students and add city info where IDs match
university_df = pd.merge(university_df, df_extra_info, on='Student_ID', how='left')

# --- STEP 3: Math-Cleaning Logic ---
# Filling Math with Mean
math_mean = university_df['Math_Score'].mean()
university_df['Math_Score'] = university_df['Math_Score'].fillna(math_mean)

# Filling Physics with Median
physics_median = university_df['Physics_Score'].median()
university_df['Physics_Score'] = university_df['Physics_Score'].fillna(physics_median)

print("--- Cleaned Data (No NaNs) ---")
print(university_df, "\n")

# --- STEP 4: The AI Feature (Normalization) ---
# Normalizing to a 0-1 range: $ \text{Score} = \frac{\text{Math} + \text{Physics}}{200} $
university_df['Total_Score_Normalized'] = (university_df['Math_Score'] + university_df['Physics_Score']) / 200

# --- STEP 5: Final Aggregation ---
# Group by city and find the mean of our normalized score
city_performance = university_df.groupby('City')['Total_Score_Normalized'].mean().sort_values(ascending=False)

print("--- Final City Ranking (Avg Normalized Score) ---")
print(city_performance)