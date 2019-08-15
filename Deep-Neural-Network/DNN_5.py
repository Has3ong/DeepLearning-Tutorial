import matplotlib.pyplot as plt
import pandas as pd
from keras.layers import *
from keras.models import *
from sklearn.preprocessing import *
from sklearn.model_selection import train_test_split
import os

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

concrete_data = pd.read_excel(__BASE_DIR__ + '/data/Concrete_Data.xls')

# print(concrete_data.columns)
"""
Index(['Cement (component 1)(kg in a m^3 mixture)',
       'Blast Furnace Slag (component 2)(kg in a m^3 mixture)',
       'Fly Ash (component 3)(kg in a m^3 mixture)',
       'Water  (component 4)(kg in a m^3 mixture)',
       'Superplasticizer (component 5)(kg in a m^3 mixture)',
       'Coarse Aggregate  (component 6)(kg in a m^3 mixture)',
       'Fine Aggregate (component 7)(kg in a m^3 mixture)', 'Age (day)',
       'Concrete compressive strength(MPa, megapascals) '],
      dtype='object')
"""
# print(concrete_data.head())
# print(concrete_data.describe())

concrete_data = concrete_data.rename(columns={
        'Cement (component 1)(kg in a m^3 mixture)' : 'cement',
       'Blast Furnace Slag (component 2)(kg in a m^3 mixture)' : 'blast',
       'Fly Ash (component 3)(kg in a m^3 mixture)' : 'fly',
       'Water  (component 4)(kg in a m^3 mixture)' : 'water',
       'Superplasticizer (component 5)(kg in a m^3 mixture)' : 'super',
       'Coarse Aggregate  (component 6)(kg in a m^3 mixture)' : 'coarse' ,
       'Fine Aggregate (component 7)(kg in a m^3 mixture)' : 'fine',
        'Age (day)' : 'age',
       'Concrete compressive strength(MPa, megapascals) ' : 'strength'
})

X = concrete_data.drop(['strength'], axis=1)
Y = concrete_data['strength']

scaler = MinMaxScaler()
X = scaler.fit_transform(X)
# sns.pairplot(concrete_data)
# plt.show()

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(8, )))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='relu'))

model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

model.summary()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

hist = model.fit(X_train, Y_train, epochs=500, validation_split=0.2)

plt.figure(figsize=(10, 10))
plt.plot(hist.history['loss'], color='r')
plt.plot(hist.history['val_loss'], color='b')
plt.title('loss')
plt.show()