import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# 2. Define age bins & labels
bins  = [0, 25, 35, 45, 55, 65, 200]
labels = ['<25','25–34','35–44','45–54','55–64','65+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

# 3. Define mutually‐exclusive feature‐usage flags
df['only_interest'] = df['has_interest_pocket'] & ~df['is_investor_funds'] & ~df['is_investor_sipp']
df['only_funds']    = df['is_investor_funds']    & ~df['is_investor_sipp']    & ~df['has_interest_pocket']
df['only_sipp']     = df['is_investor_sipp']     & ~df['is_investor_funds']    & ~df['has_interest_pocket']
df['all_feats']     = df['has_interest_pocket']  & df['is_investor_funds']     & df['is_investor_sipp']

# 4. Aggregate and compute % of total onboarded by age_group
agg = (
    df
    .groupby('age_group')
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

# 5. Rename for display (optional)
metrics = agg.rename(columns={
    'only_interest': 'Only Interest',
    'only_funds':    'Only Funds',
    'only_sipp':     'Only SIPP',
    'all_feats':     'All Features'
})

# 6. Plot heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(
    metrics,
    annot=True, fmt=".1f", cmap="Blues",
    cbar_kws={'format':'%.0f%%'}
)
plt.title('Feature Adoption Rates by Age Group')
plt.ylabel('Age Group')
plt.xlabel('')
plt.tight_layout()
plt.show()
