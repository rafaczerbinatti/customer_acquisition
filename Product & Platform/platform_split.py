import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Prepare data
platform_counts = df['platform'].value_counts().reset_index()
platform_counts.columns = ['platform', 'user_count']

# Plotting
plt.figure(figsize=(6, 4))
bars = plt.bar(platform_counts['platform'], platform_counts['user_count'],
               color='mediumpurple')

# Value labels on top
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + yval*0.01, f"{int(yval):,}",
             ha='center', va='bottom', fontsize=10)

# Style adjustments
plt.title('User Distribution by Platform')
#plt.xlabel('Platform')
plt.ylim(0, max(platform_counts['user_count']) * 1.1)
plt.xticks(rotation=0)
plt.grid(False)

# Remove chart borders
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.tight_layout()
plt.show()
