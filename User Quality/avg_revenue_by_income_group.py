# avg_revenue_by_income_group.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({
    'font.size':       12,
    'axes.titlesize':  14,
    'axes.titleweight':'bold'
})

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Define your custom income bins
bins   = [30000, 50000, 70000, 90000, float('inf')]
labels = ['£30–50k','£50–70k','£70–90k','£90k+']
df['income_group'] = pd.cut(df['gross_income'], bins=bins, labels=labels, right=False)

# Calculate average revenue per income group
rev_by_income = (
    df
    .groupby('income_group')['revenue']
    .mean()
    .reset_index(name='avg_revenue')
    .sort_values('avg_revenue', ascending=False)
)

# Plotting
plt.figure(figsize=(6, 4))
bars = plt.bar(rev_by_income['income_group'], rev_by_income['avg_revenue'], color='mediumpurple')

# Add value labels on top
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        yval + yval * 0.01,
        f"{yval:.1f}",
        ha='center', va='bottom', fontsize=10
    )

# Title & formatting
plt.title('Avg Revenue by Income Group', pad=20)
#plt.xlabel('Income Group')
plt.ylim(0, rev_by_income['avg_revenue'].max() * 1.1)

# Remove gridlines and borders
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
