import os
import numpy as np
import pandas as pd
from keras.layers import *
from keras.models import *
from keras.utils import *
import matplotlib.pyplot as plt
from sklearn.preprocessing import *
import seaborn as sns

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

adult_data = pd.read_csv(
    __BASE_DIR__ + '/data/adult.data',
    index_col=False,
    names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'mari', 'occupation', 'relationship', 'race', 'sex', 'capital-gain',
        'capital-loss', 'hours-per-week', 'native-country', '50k'
    ]
)

# print(adult_data)
# print(adult_data.count())
# print(adult_data.isnull().any())

# sns.countplot('50k', hue='sex', data=adult_data)
# plt.show()

# sns.heatmap(adult_data.corr(), annot=True, cmap='summer_r', linewidths=0.2)
# plt.show()

# plt.figure(figsize=(10, 10))
# sns.violinplot('race', 'age', hue='50k', data=adult_data, split=True)
# plt.show()


# [' <=50K', ' <=50K', ' <=50K', ' <=50K', ' <=50K', ' <=50K', ' <=50K', ' >50K', ' >50K']
Y = adult_data['50k'].values.tolist()
# [1, 1, 1, 1, 1, 1, 1, 0, 0,]
Y = [1 if i == ' <=50K' else 0 for i in Y]
Y = to_categorical(Y)


X = adult_data.drop([
        'age', 'fnlwgt', 'education-num', 'capital-gain',
        'capital-loss', 'hours-per-week', '50k'], axis=1
)
# print(X.head())

X = pd.get_dummies(X, drop_first=True)
# print(X.head())

X = pd.concat([X,
               adult_data[[
                   'age', 'fnlwgt', 'education-num', 'capital-gain',
                   'capital-loss', 'hours-per-week']
               ]], axis=1)
# print(X.head())

scaler = MinMaxScaler()

X[['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']] = \
    scaler.fit_transform(X[['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']])
# print(X.head())


X_train, X_test = X[:-1000],  X[-1000:]
Y_train, Y_test = Y[:-1000], Y[-1000:]

# (1000, 100), (1000, 2)
# print(X_test.shape, Y_test.shape)


model = Sequential()
model.add(Dense(2048, activation='relu', input_shape=(100, )))
model.add(Dense(512, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# validation_split = 0.2% BackPropagation, accuracy check
result = model.fit(X_train, Y_train, epochs=5, validation_split=0.2)

# acc, val_acc, loss, val_loss
plt.plot(result.history['acc'])
plt.show()

score = model.evaluate(X_test, Y_test)
print(score)
