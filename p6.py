from sklearn.linear_model import LinearRegression
import csv
import pandas as pd
import numpy as np 
import quandl as Quandl
import math
from sklearn import preprocessing, cross_validation, svm
import matplotlib.pyplot as plt 
import seaborn
from matplotlib import style

#df = pd.read_csv('data.csv')
#df = df.dropna()
#df.set_index('timestamp',inplace=True)
#print(df.head())
df = Quandl.get("WIKI/GOOGL")
df['OP_PC']=(df['High']-df['Low'])/df['Close'] *100.0
df['PC_CHG']=(df['Close']-df['Open'])/df['Open'] * 100.0

df = df[['Close', 'Volume','OP_PC','PC_CHG']]
print(df.head())

forecast_col = 'close'
df.fillna(value=-9999,inplace=True)

forecast_out = int(math.ceil(0.01 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

#df.dropna()

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X = X[:-forecast_out]
df.dropna(inplace=True)
y = np.array(df['label'])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print(confidence)