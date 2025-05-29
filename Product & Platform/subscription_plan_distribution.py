# avg_revenue_by_age_group.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Bin into age groups
age_bins   = [0, 25, 35, 45, 55, 65, 200]
age_labels = ['<25','25–34','35–44','45–54','55–64','65+']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)

# Calculate average revenue
rev_by_age = (
    df
    .groupby('age_group')['revenue']
    .mean()
    .reset_index(name='avg_revenue')
    .sort_values('avg_revenue', ascending=False)
)

# Plotting
plt.figure(figsize=(6, 4))
bars = plt.bar(rev_by_age['age_group'], rev_by_age['avg_revenue'], color='mediumpurple')

# Add value labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             yval + yval * 0.01,
             f"{yval:.1f}",
             ha='center', va='bottom', fontsize=10)

# Title and axis formatting
plt.title('Avg Revenue by Age Group')
#plt.xlabel('Age Group')
plt.ylim(0, rev_by_age['avg_revenue'].max() * 1.1)

# Clean up
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
