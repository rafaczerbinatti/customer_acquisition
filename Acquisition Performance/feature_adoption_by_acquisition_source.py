import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Define mutually‐exclusive feature‐usage flags
df['only_interest'] = df['has_interest_pocket'] & ~df['is_investor_funds'] & ~df['is_investor_sipp']
df['only_funds']    = df['is_investor_funds'] & ~df['is_investor_sipp'] & ~df['has_interest_pocket']
df['only_sipp']     = df['is_investor_sipp'] & ~df['is_investor_funds'] & ~df['has_interest_pocket']
df['all_feats']     = df['has_interest_pocket'] & df['is_investor_funds'] & df['is_investor_sipp']

# Aggregate and compute % of total onboarded
agg = (
    df.groupby('acquisition_source')
      .agg(
          only_interest=('only_interest','sum'),
          only_funds   =('only_funds',   'sum'),
          only_sipp    =('only_sipp',    'sum'),
          all_feats    =('all_feats',    'sum'),
          total        =('user_id',      'nunique')
      )
      .assign(
          only_interest=lambda x: x['only_interest']/x['total']*100,
          only_funds   =lambda x: x['only_funds']   /x['total']*100,
          only_sipp    =lambda x: x['only_sipp']    /x['total']*100,
          all_feats    =lambda x: x['all_feats']    /x['total']*100
      )
      .loc[:, ['only_interest','only_funds','only_sipp','all_feats']]
)

# Rename for display
metrics = agg.rename(columns={
    'only_interest': 'only_interest',
    'only_funds':    'only_funds',
    'only_sipp':     'only_sipp',
    'all_feats':     'all_feats'
})

# Plot
plt.figure(figsize=(6,4))
sns.heatmap(
    metrics,
    annot=True, fmt=".1f", cmap="Blues",
    cbar_kws={'format':'%.0f%%'}
)
plt.title('Feature Adoption Rates by Acquisition Source')
plt.ylabel('')
plt.xlabel('')
plt.tight_layout()
plt.show()
