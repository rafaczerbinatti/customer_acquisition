import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

# Set Seaborn style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold'
})

# Load the dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Calculate counts and percentages of subscription plans by acquisition source
plan_counts = (
    df
    .groupby(['acquisition_source','subscription_plan'])
    .size()
    .unstack(fill_value=0)
)
plan_pct = plan_counts.div(plan_counts.sum(axis=1), axis=0) * 100

# Plot stacked bar chart
plt.figure(figsize=(6, 4))
x = range(len(plan_pct))
bottom = [0] * len(plan_pct)

for plan in plan_pct.columns:
    plt.bar(
        x,
        plan_pct[plan],
        bottom=bottom,
        label=plan
    )
    bottom = [i + j for i, j in zip(bottom, plan_pct[plan])]

# Value labels on each segment (optional)
for i, src in enumerate(plan_pct.index):
    cum = 0
    for plan in plan_pct.columns:
        height = plan_pct.loc[src, plan]
        if height > 3:  # only label segments >3%
            plt.text(
                i,
                cum + height/2,
                f"{height:.0f}%",
                ha='center',
                va='center',
                fontsize=10,
                color='white'
            )
        cum += height

# Style adjustments
plt.title('Subscription Plan by Acquisition Source', pad=20)  # add padding here
plt.xticks(x, plan_pct.index, rotation=0)
plt.ylabel('')
plt.ylim(0, 100)
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100))
plt.grid(False)

# Legend
plt.legend(
    title='Subscription Plan',
    bbox_to_anchor=(1, 1),
    frameon=False
)

# Remove chart borders
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
