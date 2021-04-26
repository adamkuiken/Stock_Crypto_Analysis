#Skeleton Project
#By Joe Pickering and Adam Kuiken
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA


df = pd.read_csv('TMUSEdit.csv') #tmobile stock for 1yr
df['Date'] = pd.to_datetime(df['Date'],format = '%Y-%m-%d')
print(df.head())

df['mean'] = df['Close'].rolling(window=3,center=False).mean()
df['std'] = df['Close'].rolling(window=3,center=False).std()
#mini_df['rolling_std'] = mini_df.rolling(window = 12).std()
print(df.head())

df['df_log'] = np.log(df[['Close']])

model1 = ARIMA(df[['df_log']].values, order=(1, 1, 1))
results1 = model1.fit()
results1.plot_predict(1, 300)
plot1= plt.figure(1)
plt.xlabel('Days')
plt.ylabel('Log')

model2 = ARIMA(df[['Close']].values, order=(1, 1, 1))
results2 = model2.fit()
results2.plot_predict(1, 300)
plot2= plt.figure(2)
plt.xlabel('Days')
plt.ylabel('Close')

#Advanced Forecasting
advMod = ARIMA(df[['Close']].values, order=(1, 1, 1))
advResults = advMod.fit()
pred = advResults.predict(start=pd.to_datetime('2019-06-17'), dynamic=False)
pred_ci = pred.conf_int()
ax = df['Close'].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
ax.fill_between(pred_ci.index,pred_ci.iloc[:, 0],pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('Forecast of Close')
plt.legend()
plt.show()
#plt.plot(df[['Close','mean','std','df_log']])

plt.show()
