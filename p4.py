from sklearn.linear_model import LinearRegression
import csv
import pandas as pd
import numpy as np 

import matplotlib.pyplot as plt 
import seaborn
from matplotlib import style

df = pd.read_csv('data.csv')


df = df.dropna()

df.set_index('timestamp',inplace=True)
print(df.head())

#Define dependent expanatory variabeles
df['s_1'] = df['open'].shift(1).rolling(window=3).mean()
df['s_9']= df['close'].shift(1).rolling(window=9).mean() 
df['s_9']= ((df['close']-df['open'])/df['open']).shift(1).rolling(window=5).mean() 
df = df.dropna()
X = df[['s_1','s_9']]
print(df.head())

Y = df['open']

#get training data
t = .8
t = int(t*len(df))

#train
X_train = X[:t]
Y_train = Y[:t]

#test
X_test = X[t:]
Y_test = Y[t:]

linear = LinearRegression().fit(X_train,Y_train)

#print("Gold ETF Price = {0}\n* 3 Days Moving Average {1}\n* 9 Days Moving Average {2}".format(round(linear.coef_[0],2),round(linear.coef_[1],2),round(linear.intercept_,2)))
print("Gold ETF Price = {0}".format(round(linear.coef_[1],2)))
predicted_price = linear.predict(X_test)
predicted_price = pd.DataFrame(predicted_price,index=Y_test.index,columns = ['open'])
predicted_price.plot(figsize=(10,5))

Y_test.plot()
plt.legend(['predicted_price','actual_price'])

#plt.xlabel("time")
plt.ylabel("Stock price")
#plt.plot(x,y)
plt.show()

r2_score = linear.score(X[t:],Y[t:])*100  

rr  = float("{0:.2f}".format(r2_score))
print(rr)