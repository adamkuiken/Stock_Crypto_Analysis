#Skeleton Project
#By Joe Pickering and Adam Kuiken
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.vector_ar.var_model import VAR


df = pd.read_csv('TMUSEdit.csv') #tmobile stock for 1yr
df['Date'] = pd.to_datetime(df['Date'],format = '%Y-%m-%d')
print(df.head())

data = df.drop(['Date'], axis=1)

df['mean'] = df['Close'].rolling(window=3,center=False).mean()
df['std'] = df['Close'].rolling(window=3,center=False).std()
#mini_df['rolling_std'] = mini_df.rolling(window = 12).std()
print(df.head())

df['df_log'] = np.log(df[['Close']])
'''
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
'''

#Advanced Forecasting
advMod = VAR(endog =data)
advResults = advMod.fit()
pred = advResults.forecast(advResults.y,steps=1)
#pred = advResults.forecast(start=pd.to_datetime('2019-06-17'), dynamic=False)
#pred_ci = pred.conf_int()
#ax = df['Close'].plot(label='observed')



advResults.plot_forecast(steps = 1, alpha=.7)


#x = df['Date']
#y1 = df['Close']
#y2 = df['pred']

#fig, ax = plt.subplots()

#line1, = ax.plot(x, y1)
#line2, = ax.plot(x,y2)



plt.xlabel('Date')
plt.ylabel('Forecast of Close')

plt.legend()
plt.show()
#plt.plot(df[['Close','mean','std','df_log']])

plt.show()
