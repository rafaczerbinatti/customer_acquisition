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

# Load dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Flag who converted in month 1 and who of those converted again by month 12
df['converted_3m'] = df['revenue_3_m'] > 0
df['retained_12m'] = (df['revenue_12_m'] > df['revenue_3_m']) & df['converted_3m']

# Aggregate counts by acquisition source
agg = (
    df.groupby('acquisition_source')
      .agg(
          count_converted=('converted_3m', 'sum'),
          count_retained =('retained_12m',  'sum'),
      )
      .assign(
          pct_retained=lambda d: d['count_retained'] / d['count_converted'] * 100
      )
      .reset_index()
      .sort_values('pct_retained', ascending=False)  # order descending
)

# Plot
plt.figure(figsize=(6, 4))
bars = plt.bar(agg['acquisition_source'], agg['pct_retained'], color='mediumpurple')

# Value labels
for bar in bars:
    y = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        y + 1,
        f"{y:.1f}%",
        ha='center', va='bottom', fontsize=10
    )

# Style adjustments
plt.title('12-Month Retention Rate by Acquisition Source', pad=20)
plt.ylabel('')
plt.ylim(0, agg['pct_retained'].max() * 1.1)
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.grid(False)

# Remove chart borders
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
