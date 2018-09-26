import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from matplotlib import style

#headers = ['stocks','timestamp','open']

df = pd.read_csv('ns.csv')
# df.setindex('timestamp', inplace=True)
print(df.head())

style.use('ggplot')

x = df['timestamp']
y = df['open']

#plt.plot(df['close'])
#plt.plot(x,y)
#plt.show()