import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Count users per acquisition source, sorted by count
source_counts = df['acquisition_source'].value_counts().reset_index()
source_counts.columns = ['acquisition_source', 'user_count']

# Plot
plt.figure(figsize=(8, 4))
bars = plt.bar(source_counts['acquisition_source'], source_counts['user_count'], color='mediumpurple')

# Add value labels inside bars
for bar in bars:
    y = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, y / 2, f"{int(y):,}",
             ha='center', va='center', fontsize=10, color='white', fontweight='bold')

# Title only
plt.title('User Distribution by Acquisition Source')
plt.xlabel('')
plt.ylabel('')

# Style cleanup
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
