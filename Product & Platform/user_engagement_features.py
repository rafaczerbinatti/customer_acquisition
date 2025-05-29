import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set consistent style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Load dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Define engagement feature columns
feature_columns = {
    'is_investor_funds': 'Investor Funds',
    'is_investor_sipp': 'SIPP',
    'has_interest_pocket': 'Interest Pocket'
}

# Count True values for each feature
feature_counts = df[list(feature_columns.keys())].apply(lambda col: col.fillna(False).astype(bool).sum())

# Create a dataframe with readable labels
feature_df = pd.DataFrame({
    'feature': [feature_columns[col] for col in feature_counts.index],
    'user_count': feature_counts.values
}).sort_values(by='user_count', ascending=False)

# Plot
plt.figure(figsize=(8, 4))
bars = plt.bar(feature_df['feature'], feature_df['user_count'], color='mediumpurple')

# Add value labels on top of the bars
for bar in bars:
    y = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, y + max(feature_df['user_count']) * 0.01, f"{int(y):,}",
             ha='center', va='bottom', fontsize=10)

# Title only
plt.title('User Engagement with Product Features')
plt.xlabel('')
plt.ylabel('')

# Clean style
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
