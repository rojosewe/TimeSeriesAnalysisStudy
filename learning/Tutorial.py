'''
Created on Oct 19, 2016

@author: root
'''
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime
# %matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_csv('../AirPassengers.csv', parse_dates=True, index_col='Month',date_parser=dateparse)
print(data.head())
print('\n Data Types:')
print(data.dtypes)
print(data.index)

ts = data["#Passengers"]
print(ts.head(10))

print(ts[datetime(1949,1,1)])
print(ts["1949-01-01"])

print(ts[:].head(10))
print(ts[0:10])

print(ts["1949"])

plt.plot(ts)