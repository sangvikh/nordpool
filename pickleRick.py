from sqlite3 import Row
from numpy import row_stack
import pandas as pd

EURNOK = 10.26

table = pd.read_pickle('prices.pkl')
print(table)
print('\n\n\n')

df = pd.DataFrame(table, columns=['Kr.sand'])
#print(table)
#print('\n\n\n')

#df = pd.to_numeric(df, errors='ignore')
#df = df*EURNOK
print(table.iloc[:, 2].name)
print(table.iloc[:, 2])
print('\n\n\n')
print(table.iloc[1])
print('\n\n\n')
print(table.iloc[1].name)
print('\n\n\n')

# Date
date = table.iloc[:,0].name
date = pd.to_datetime(date)
print(date)

# Kristiansand
prices = table.iloc[range(0,24),[2]]
print(prices)