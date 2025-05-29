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

# Define cumulative conversion flags
df['conv_1m']  = df['revenue_1_m']  > 0
df['conv_3m']  = df['revenue_3_m']  > 0
df['conv_6m']  = df['revenue_6_m']  > 0
df['conv_12m'] = df['revenue_12_m'] > 0

# Aggregate counts and compute percentages relative to total onboarded
agg = (
    df.groupby('acquisition_source')
      .agg(
          total        = ('user_id',    'nunique'),
          conv1_count  = ('conv_1m',    'sum'),
          conv3_count  = ('conv_3m',    'sum'),
          conv6_count  = ('conv_6m',    'sum'),
          conv12_count = ('conv_12m',   'sum'),
      )
      .assign(
          pct_conv_1m  = lambda d: d['conv1_count']  / d['total'] * 100,
          pct_conv_3m  = lambda d: d['conv3_count']  / d['total'] * 100,
          pct_conv_6m  = lambda d: d['conv6_count']  / d['total'] * 100,
          pct_conv_12m = lambda d: d['conv12_count'] / d['total'] * 100,
      )
      .reset_index()
)

# Prepare data for plotting
sources = agg['acquisition_source']
periods = ['1 Month', '3 Months', '6 Months', '12 Months']
rates   = agg[['pct_conv_1m','pct_conv_3m','pct_conv_6m','pct_conv_12m']].values

# Plotting
plt.figure(figsize=(6, 4))
for i, src in enumerate(sources):
    plt.plot(periods, rates[i], marker='o', label=src)

# Format y-axis as percentages
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())

# Style adjustments
plt.title('Cumulative Conversion Rates by Acquisition Source')
plt.xlabel('')
plt.ylabel('')
plt.ylim(0, rates.max() * 1.1)
plt.legend(title='Acquisition Source')
plt.grid(False)

# Remove chart borders
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
