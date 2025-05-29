import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Set Seaborn style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Count values
gender_counts = df['gender'].value_counts().reset_index()
gender_counts.columns = ['gender', 'user_count']

# Plot
plt.figure(figsize=(6, 4))
bars = plt.bar(gender_counts['gender'], gender_counts['user_count'], color='mediumpurple')

# Add value labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + yval * 0.01, f"{int(yval):,}",
             ha='center', va='bottom', fontsize=10)

# Title
plt.title('Gender Distribution')

# Style cleanup
plt.xlabel('')
plt.ylabel('')
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()