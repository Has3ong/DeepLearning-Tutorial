
import pandas as pd
import requests
import matplotlib.pyplot as plt
from keras.layers import *
from keras.models import *
from sklearn.preprocessing import *

plt.style.use('bmh')

request = requests.get('https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1405699200&end=9999999999&period=86400')
json = request.json()
data = pd.DataFrame(json)

scaler = MinMaxScaler()
data[['close']] = scaler.fit_transform(data[['close']])
price = data['close'].values.tolist()

window_size = 5
X = []
Y = []

for i in range(len(price)-window_size):
    X.append([price[i+j] for j in range(window_size)])

for i in range(len(price)-window_size):
    Y.append(price[window_size + i])


X = np.asarray(X)
Y = np.asarray(Y)

# X_train (1000, 5)
train_test_split = 1000
X_train = X[ : train_test_split, : ]
Y_train = Y[ : train_test_split]

X_test = X[train_test_split :, : ]
Y_test = Y[train_test_split : ]

# X_train(1000, 5, 1)
X_train = np.asarray(np.reshape(X_train, (X_train.shape[0], window_size, 1)))
X_test = np.asarray(np.reshape(X_test, (X_test.shape[0], window_size, 1)))


model = Sequential()
model.add(LSTM(128, input_shape=(5, 1)))
model.add(Dropout(0.2))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam')

model.summary()

hist = model.fit(x=X_train, y=Y_train, epochs=30, batch_size=1, verbose=1)


train_predict = model.predict(X_train)
test_predict = model.predict(X_test)
plt.figure(figsize=(10,10))

plt.plot(price)

split_pt = train_test_split + window_size

plt.plot(np.arange(window_size,split_pt,1),train_predict,color = 'b')
plt.plot(np.arange(split_pt,split_pt + len(test_predict),1),test_predict,color = 'r')

plt.show()