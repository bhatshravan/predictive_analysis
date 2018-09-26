import pandas as pd
import datetime
import mpld3


from pandas_datareader import data,wb
import matplotlib.pyplot as plt 
from matplotlib import style 

style.use('ggplot')

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2018,1,1)

df = data.DataReader("XOM","yahoo",start,end)
print(df.head())

df['Adj Close'].plot()
df['High'].plot()
df['Low'].plot()

#plt.show()

mpld3.fig_to_html()
mpld3.show()