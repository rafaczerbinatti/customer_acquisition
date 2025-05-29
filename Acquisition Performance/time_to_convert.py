import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

# Style (no gridlines)
sns.set_theme(style="white", palette="muted")
plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold'
})

# Load
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Define discrete “time to first revenue” flags
df['conv_1m']  = df['revenue_1_m']  > 0
df['conv_3m']  = (df['revenue_1_m'] == 0) & (df['revenue_3_m']  > 0)
df['conv_6m']  = (df['revenue_1_m'] == 0) & (df['revenue_3_m'] == 0) & (df['revenue_6_m']  > 0)
df['conv_12m'] = (df['revenue_1_m'] == 0) & (df['revenue_3_m'] == 0) & (df['revenue_6_m'] == 0) & (df['revenue_12_m'] > 0)

# Aggregate counts & compute rates
agg = (
    df.groupby('acquisition_source')
      .agg(
          total=('user_id','nunique'),
          c1   =('conv_1m' , 'sum'),
          c3   =('conv_3m' , 'sum'),
          c6   =('conv_6m' , 'sum'),
          c12  =('conv_12m','sum'),
      )
      .assign(
          pct_1m  = lambda d: d['c1']  / d['total'] * 100,
          pct_3m  = lambda d: d['c3']  / d['total'] * 100,
          pct_6m  = lambda d: d['c6']  / d['total'] * 100,
          pct_12m = lambda d: d['c12'] / d['total'] * 100,
      )
      .reset_index()
)

# Prepare for plot
sources = agg['acquisition_source']
periods = ['1 Month','2–3 Months','4–6 Months','7–12 Months']
rates   = agg[['pct_1m','pct_3m','pct_6m','pct_12m']].values

# Plot
fig, ax = plt.subplots(figsize=(8,5))
for i, src in enumerate(sources):
    ax.plot(periods, rates[i], marker='o', label=src)

# Percent formatter on y-axis
ax.yaxis.set_major_formatter(mtick.PercentFormatter())

# Labels & style
ax.set_title('Time-to-Convert Rates by Acquisition Source')
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_ylim(0, rates.max() * 1.1)
ax.legend(title='Acquisition Source', loc='best')

# Remove all gridlines and spines
ax.grid(False)
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
