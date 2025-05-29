# retention_by_platform.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Flag 3m converters and 12m retained
df['converted_3m'] = df['revenue_3_m'] > 0
df['retained_12m'] = df['converted_3m'] & (df['revenue_12_m'] > df['revenue_3_m'])

# Aggregate
agg = (
    df[df['converted_3m']]
    .groupby('platform')
    .agg(
        converted=('user_id','nunique'),
        retained =('retained_12m','sum')
    )
    .assign(retention=lambda d: d['retained']/d['converted']*100)
    .reset_index()
    .sort_values('retention', ascending=False)
)

# Plotting
plt.figure(figsize=(6, 4))
bars = plt.bar(agg['platform'], agg['retention'], color='mediumpurple')

# Add value labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             yval + 1,
             f"{yval:.1f}%",
             ha='center', va='bottom', fontsize=10)

# Title and axis formatting
plt.title('12-Month Retention Rate by Platform')
#plt.xlabel('Platform')
plt.ylim(0, agg['retention'].max() * 1.1)

# Clean up
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
