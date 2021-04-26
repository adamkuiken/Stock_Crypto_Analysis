#My test ARIMA
#Adam Kuiken
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot as plt


df = pd.read_csv('TMUSEdit.csv')
df['Date'] = pd.to_datetime(df['Date'],format = '%Y/%m/%d')
print(df.head())
mini_df = df[['Date','Close']]
plt.plot(df[['Date']],df[['Close']])
plt.show()
