# avg_revenue_by_subscription_plan.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Calculate average revenue
rev_by_plan = (
    df
    .groupby('subscription_plan')['revenue']
    .mean()
    .reset_index(name='avg_revenue')
    .sort_values('avg_revenue', ascending=False)
)

# Plotting
plt.figure(figsize=(6, 4))
bars = plt.bar(rev_by_plan['subscription_plan'], rev_by_plan['avg_revenue'], color='mediumpurple')

# Add value labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             yval + yval * 0.01,
             f"{yval:.1f}",
             ha='center', va='bottom', fontsize=10)

# Title and axis formatting
plt.title('Avg Revenue by Subscription Plan')
#plt.xlabel('Subscription Plan')
plt.ylim(0, rev_by_plan['avg_revenue'].max() * 1.1)

# Clean up
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
