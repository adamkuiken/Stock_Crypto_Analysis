#Mass Forescaster
#By Joe Pickering and Adam Kuiken

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
import glob


for file in glob.glob('/stonks/*.csv'):
    stockName = file.name
    df = pd.read_csv('file')
    print(df.head())
    # fit model
    df['Date'] =  pd.to_datetime(df['Date'], format='%Y/%m/%d')#converts date some date are missing though
    
    model = ARIMA(df[['Close']].astype(float),order=(1,1,1))
    model_fit = model.fit(disp=False)
    # make prediction
    yhat = model_fit.predict(len(smalldf), len(smalldf), typ='levels')
    print(yhat)       
    changeInY = yhat-df[["Close",200]].values
    
    print("Stock: {} prediction: {} Change: {}".format(stockName,yhat,changeInY))
