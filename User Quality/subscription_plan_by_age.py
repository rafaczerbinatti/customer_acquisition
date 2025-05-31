import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# 2. Define age bins (adjust edges & labels as you like)
bins = [0, 25, 35, 45, 55, 65, 200]
labels = ['<25','25–34','35–44','45–54','55–64','65+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

# 3. Compute counts and percentages
#    count per (age_group × acquisition_source)
grouped = (
    df
    .groupby(['age_group', 'subscription_plan'])
    .size()
    .reset_index(name='count')
)

#    total per age_group
grouped['total_in_bin'] = grouped.groupby('age_group')['count'].transform('sum')

#    percentage of each source within its age_group
grouped['pct'] = grouped['count'] / grouped['total_in_bin'] * 100

# 4. Pivot so rows=age_group, cols=acquisition_source, values=pct
pivot = grouped.pivot(index='age_group',
                      columns='subscription_plan',
                      values='pct').fillna(0)

# 5. Plot 100% stacked bar chart
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold'
})

ax = pivot.plot(
    kind='bar',
    stacked=True,
    figsize=(10, 6),
    width=0.8,
    rot=0
)

# Formatting
ax.set_title('Subscription Plan by Age Group')
ax.set_xlabel('')
ax.set_ylabel('')

# Show percentages on each segment (optional)
for patch in ax.patches:
    height = patch.get_height()
    if height > 3:  # only label segments large enough
        x = patch.get_x() + patch.get_width() / 2
        y = patch.get_y() + height / 2
        ax.text(x, y, f"{height:.1f}%", ha='center', va='center', color='white', fontsize=9)

# Move legend outside
ax.legend(title='Subscription Plan', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.show()
