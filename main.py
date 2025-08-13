import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Simulate A/B test data with different levels of personalization
n_emails = 1000
group_a = pd.DataFrame({
    'group': ['A'] * n_emails,
    'clicks': np.random.binomial(1, 0.1, n_emails), # 10% baseline click-through rate
    'personalization_level': ['low'] * n_emails
})
group_b = pd.DataFrame({
    'group': ['B'] * n_emails,
    'clicks': np.random.binomial(1, 0.12, n_emails), # Slightly higher CTR for moderate personalization
    'personalization_level': ['moderate'] * n_emails
})
group_c = pd.DataFrame({
    'group': ['C'] * n_emails,
    'clicks': np.random.binomial(1, 0.08, n_emails), # Lower CTR for high personalization - example of over-personalization
    'personalization_level': ['high'] * n_emails
})
df = pd.concat([group_a, group_b, group_c], ignore_index=True)
# --- 2. Data Cleaning and Analysis ---
# (In this synthetic example, data cleaning is minimal)
# Calculate click-through rates for each group
ctr_a = group_a['clicks'].mean()
ctr_b = group_b['clicks'].mean()
ctr_c = group_c['clicks'].mean()
# Perform statistical tests to compare groups (e.g., chi-squared test)
contingency_table = pd.crosstab(df['group'], df['clicks'])
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
print("Click-Through Rates:")
print(f"Group A (Low Personalization): {ctr_a:.4f}")
print(f"Group B (Moderate Personalization): {ctr_b:.4f}")
print(f"Group C (High Personalization): {ctr_c:.4f}")
print(f"\nChi-squared test p-value: {p:.4f}") # Assess statistical significance of differences
# --- 3. Visualization ---
plt.figure(figsize=(8, 6))
plt.bar(['Low', 'Moderate', 'High'], [ctr_a, ctr_b, ctr_c], color=['skyblue', 'lightgreen', 'coral'])
plt.ylabel('Click-Through Rate')
plt.xlabel('Personalization Level')
plt.title('A/B Test Results: Click-Through Rates by Personalization Level')
plt.ylim(0, 0.15) # Set y-axis limits for better visualization
# Save the plot to a file
output_filename = 'ab_test_results.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")