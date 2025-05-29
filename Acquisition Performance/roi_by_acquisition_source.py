import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Load dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Group by acquisition source
grouped = df.groupby('acquisition_source').agg(
    total_revenue=('revenue_12_m', 'sum'),
    total_users=('user_id', 'count'),
    avg_revenue_per_user=('revenue_12_m', 'mean'),
    avg_cpa=('cpa', 'mean')
).reset_index()

# Calculate ROI
grouped['roi'] = grouped['total_revenue'] / (grouped['avg_cpa'] * grouped['total_users'])

# Sort by ROI
grouped = grouped.sort_values(by='roi', ascending=False)

# Plot
plt.figure(figsize=(9, 5))
bars = plt.bar(grouped['acquisition_source'], grouped['roi'], color='mediumpurple')

# Add detailed labels on top
for idx, bar in enumerate(bars):
    y = bar.get_height()
    revenue = grouped.iloc[idx]['total_revenue']
    arpu = grouped.iloc[idx]['avg_revenue_per_user']
    cpa = grouped.iloc[idx]['avg_cpa']
    label = f"Rev: £{int(revenue):,}\nARPU: £{arpu:.1f}\nCPA: £{cpa:.1f}"
    plt.text(bar.get_x() + bar.get_width()/2, y + y * 0.01, label,
             ha='center', va='bottom', fontsize=9)

# Title only
plt.title('ROI by Acquisition Source')
plt.xlabel('')
plt.ylabel('')  # can add 'ROI (Revenue ÷ CPA)' if preferred

# Clean styling
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
