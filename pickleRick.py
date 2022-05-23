import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

EURNOK = 10.26
VAT = 25
location = "Kr.sand"

#data = pd.read_pickle('prices.pkl')
data = pd.read_csv('prices.csv')
data.to_json('prices.json') # Save as json (testing)
print(data)
print('\n\n\n')

# Find price data for given location
try:
    prices = data[location].iloc[range(0,31)]
    prices = pd.to_numeric(prices)*EURNOK/100000*(1.0 + VAT/100)
except:
    print("Could not find location!")

# Labels
labels = data.iloc[:,1]
print('Labels:')
print(labels)
print('\n\n\n')

# Date
date = data.iloc[:,1].name
date = pd.to_datetime(date)
print('Timestamp:')
print(date + timedelta(hours=0))        # Can add a timedelta if we want to timestamp each hour
print('\n\n\n')

# Get price per hour
# Hour 0 is 00:00 - 01:00 etc..
print('Prices:')
print(prices.iloc[range(0,24)])
print('\n\n\n')

# Min, Max, Average, Peak
min = prices.iloc[25]
max = prices.iloc[26]
average = prices.iloc[27]
peak = prices.iloc[28]

print("Min: " + str(min))
print("Max: " + str(max))
print("Avg: " + str(average))

prices.iloc[range(0,24)].plot()
plt.show()