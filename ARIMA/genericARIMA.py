
#code from machinelearningmastery.com

# ARIMA example
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot as plt
import pandas as pd
# contrived dataset
df = pd.read_csv('TMUSEdit.csv')
print(df.head())
# fit model
#df['date_col'] =  pd.to_datetime(df['Date'], format='%m/%d/%Y')#converts date some date are missing though
smalldf = df[['Close']]
model = ARIMA(smalldf.astype(float),order=(1,1,1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(smalldf), len(smalldf), typ='levels')
print(yhat)
num = df[['Num']].values
plt.plot(num,smalldf)
plt.plot(yhat,'or')
plt.show()
