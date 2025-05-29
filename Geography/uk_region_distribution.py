import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Set style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Region counts
region_counts = df['uk_region'].value_counts().sort_values(ascending=False).reset_index()
region_counts.columns = ['region', 'user_count']

# Plot
plt.figure(figsize=(10, 6))
bars = sns.barplot(x='user_count', y='region', data=region_counts, palette='crest')

# Add value labels
for bar in bars.patches:
    xval = bar.get_width()
    yval = bar.get_y() + bar.get_height() / 2
    plt.text(xval + xval * 0.005, yval, f"{int(xval):,}", va='center', fontsize=10)

# Clean up axes and borders
plt.title('User Distribution by UK Region')
plt.xlabel('')
plt.ylabel('')
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()