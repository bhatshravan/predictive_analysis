import datetime
from sklearn.linear_model import LinearRegression 

import pandas as pd 

import numpy as np 
import matplotlib.pyplot as plt 

import seaborn
from pandas_datareader import data,wb
import fix_yahoo_finance as yf

# Read data 

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2018,1,1)

Df = data.DataReader("googl","yahoo",start,end)

Df=Df[['Close']] 
Df= Df.dropna() 

Df['S_3'] = Df['Close'].shift(1).rolling(window=3).mean() 

Df['S_9']= Df['Close'].shift(1).rolling(window=9).mean() 

Df= Df.dropna() 

X = Df[['S_3','S_9']] 

y = Df['Close']

t=.8 

t = int(t*len(Df)) 

# Train dataset 

X_train = X[:t] 

y_train = y[:t]  

# Test dataset 

X_test = X[t:] 

y_test = y[t:]
linear = LinearRegression().fit(X_train,y_train) 
predicted_price = linear.predict(X_test)  

predicted_price = pd.DataFrame(predicted_price,index=y_test.index,columns = ['price'])  

predicted_price.plot(figsize=(10,5))  

y_test.plot()  

plt.legend(['predicted_price','actual_price'])  

plt.ylabel("Gold ETF Price")  

plt.show()