import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Set Seaborn and Matplotlib style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Plot: Age Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['age'], bins=10, kde=True, color='mediumpurple')

plt.title('Age Distribution')

plt.xlabel('')
plt.ylabel('')

plt.grid(False)

for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()