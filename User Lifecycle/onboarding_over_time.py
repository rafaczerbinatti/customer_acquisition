import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Convert onboarding_month to datetime
df['onboarding_month'] = pd.to_datetime(df['onboarding_month'])

# Group by month and count users
onboarding_counts = df.groupby(df['onboarding_month'].dt.to_period('M')).size().reset_index(name='user_count')

# Format month to 'Jan 2023'
onboarding_counts['month_str'] = onboarding_counts['onboarding_month'].astype(str)
onboarding_counts['month_str'] = pd.to_datetime(onboarding_counts['month_str']).dt.strftime('%b %Y')

# Plot
plt.figure(figsize=(10, 5))
bars = plt.bar(onboarding_counts['month_str'], onboarding_counts['user_count'],
               color='mediumpurple')

# Add value labels inside the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval / 2, f"{int(yval):,}",
             ha='center', va='center', fontsize=10, color='white', fontweight='bold')

# Title only, no axis labels
plt.title('User Onboarding Over Time')
plt.xlabel('')
plt.ylabel('')
plt.xticks(rotation=45)

# Clean up style
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
