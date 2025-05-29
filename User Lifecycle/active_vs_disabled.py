import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set chart style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Classify customers
df['status'] = df['disabled_month'].isna().map({True: 'Active', False: 'Disabled'})

# Count each status
counts = df['status'].value_counts()

# Create bar chart
plt.figure(figsize=(6, 4))
bars = plt.bar(counts.index, counts.values, color=['mediumpurple', 'slateblue'])

# Add value labels
for bar in bars:
    y = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, y / 2, f"{int(y):,}",
         ha='center', va='center', fontsize=10, color='white', fontweight='bold')

# Title only
plt.title('User Distribution: Active vs Inactive')
plt.xlabel('')
plt.ylabel('')

# Remove gridlines and borders
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
