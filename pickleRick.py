import pandas as pd

EURNOK = 10.26

#data = pd.read_pickle('prices.pkl')
data = pd.read_csv('prices.csv')
print(data)
print('\n\n\n')

# Date
date = data.iloc[:,1].name
date = pd.to_datetime(date)
print(date)
print('\n\n\n')

# Kristiansand
prices = data.iloc[range(0,24),[3]].astype(float)*EURNOK/100
print(prices)