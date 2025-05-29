import pandas as pd

# Load your data
df = pd.read_csv(r'C:\Users\Rafael\Documents\Python Projects\Customer Acquisition\customer_acquisition.csv')

# Compute the quartile edges
quantiles = df['gross_income'].quantile([0, 0.25, 0.5, 0.75, 1.0])
print(quantiles)
