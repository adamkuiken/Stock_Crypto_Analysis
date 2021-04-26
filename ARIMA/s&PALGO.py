import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv('TMUSEdit.csv')
print(df.head())
#df['date_col'] =  pd.to_datetime(df['Date'], format='%m/%d/%Y')#converts date some date are missing though
X = df[['Open','High','Low','Close']].values
y = df['NextClose'].values #prediction value

smallX = X[:600]
smallY = y[:600]

X_train, X_test, y_train, y_test = train_test_split(smallX,smallY)

model = LogisticRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

y_pred = model.predict(X_test)
print("accuracy:", accuracy_score(y_test, y_pred))
print("precision:", precision_score(y_test, y_pred))
print("recall:", recall_score(y_test, y_pred))
print("f1 score:", f1_score(y_test, y_pred))

