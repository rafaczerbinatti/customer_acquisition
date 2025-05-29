import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Set Seaborn style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Adjusted bins and labels
bins = [30000, 50000, 70000, 90000, float('inf')]
labels = ['£30–50k', '£50–70k', '£70–90k', '£90k+']

# Create income group column
df['income_group'] = pd.cut(df['gross_income'], bins=bins, labels=labels, include_lowest=True)

# Count users in each group, sorted DESC
group_counts = df['income_group'].value_counts().sort_values(ascending=False)

# Plot
plt.figure(figsize=(8, 5))
bars = sns.barplot(x=group_counts.index, y=group_counts.values, palette='crest')

# Add value labels on top of each bar
for bar in bars.patches:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval + yval * 0.01,
        f"{int(yval):,}",
        ha='center', va='bottom',
        fontsize=10
    )

# Title only, no axis labels
plt.title('User Distribution by Income Group')
plt.xlabel('')
plt.ylabel('')

# Remove gridlines and spines
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
