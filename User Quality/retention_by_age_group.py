# retention_by_age_group.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.titleweight': 'bold'})

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Bin into age groups
age_bins   = [0, 25, 35, 45, 55, 65, 200]
age_labels = ['<25','25–34','35–44','45–54','55–64','65+']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)

# Flag 3m converters and 12m retained
df['converted_3m'] = df['revenue_3_m'] > 0
df['retained_12m'] = df['converted_3m'] & (df['revenue_12_m'] > df['revenue_3_m'])

# Aggregate
agg = (
    df[df['converted_3m']]
    .groupby('age_group')
    .agg(
        converted=('user_id','nunique'),
        retained =('retained_12m','sum')
    )
    .assign(retention=lambda d: d['retained']/d['converted']*100)
    .reset_index()
    .sort_values('age_group', ascending=True)
)

# Plotting
plt.figure(figsize=(6, 4))
bars = plt.bar(agg['age_group'], agg['retention'], color='mediumpurple')

# Add value labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             yval + 1,
             f"{yval:.1f}%",
             ha='center', va='bottom', fontsize=10)

# Title and axis formatting
plt.title('12-Month Retention Rate by Age Group')
#plt.xlabel('Age Group')
plt.ylim(0, agg['retention'].max() * 1.1)

# Clean up
plt.grid(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
