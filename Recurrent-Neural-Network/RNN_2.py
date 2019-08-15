
import pandas as pd
import matplotlib.pyplot as plt
from keras.layers import *
from keras.models import *
from keras.utils import *
from sklearn.preprocessing import *
import os

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

label = ['attr_{}'.format(i) for i in range(73)]

data = pd.read_csv(__BASE_DIR__ + '/data/eighthr.data', names=label)
print(data.columns)
"""
Index(['attr_0', 'attr_1', 'attr_2', 'attr_3', 'attr_4', 'attr_5', 'attr_6',
       'attr_7', 'attr_8', 'attr_9', 'attr_10', 'attr_11', 'attr_12',
       'attr_13', 'attr_14', 'attr_15', 'attr_16', 'attr_17', 'attr_18',
       'attr_19', 'attr_20', 'attr_21', 'attr_22', 'attr_23', 'attr_24',
       'attr_25', 'attr_26', 'attr_27', 'attr_28', 'attr_29', 'attr_30',
       'attr_31', 'attr_32', 'attr_33', 'attr_34', 'attr_35', 'attr_36',
       'attr_37', 'attr_38', 'attr_39', 'attr_40', 'attr_41', 'attr_42',
       'attr_43', 'attr_44', 'attr_45', 'attr_46', 'attr_47', 'attr_48',
       'attr_49', 'attr_50', 'attr_51', 'attr_52', 'attr_53', 'attr_54',
       'attr_55', 'attr_56', 'attr_57', 'attr_58', 'attr_59', 'attr_60',
       'attr_61', 'attr_62', 'attr_63', 'attr_64', 'attr_65', 'attr_66',
       'attr_67', 'attr_68', 'attr_69', 'attr_70', 'attr_71', 'attr_72'],
      dtype='object')
"""

# data type string -> numeric(float64)
data = data.apply(pd.to_numeric, errors='coerce')
data = data.dropna()

Y = data['attr_72']
Y = to_categorical(Y)

data = data.drop(['attr_72'], axis=1)


X_train = np.asarray(data[:-100].values.tolist(), dtype=np.float64)
X_test = np.asarray(data[-100:].values.tolist(), dtype=np.float64)

Y_train = Y[:-100]
Y_test = Y[-100:]

X_train = X_train[:1700]
Y_train = Y_train[:1700]

X_train = X_train.reshape(-1, 10, 72)
Y_train = Y_train.reshape(-1, 10, 2)

model = Sequential()
model.add(LSTM(128, input_shape=(10, 72,), return_sequences=True))
model.add(LSTM(256, return_sequences=True))
model.add(Dense(2, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

hist = model.fit(X_train, Y_train, epochs=10, batch_size=1, validation_split=0.2)

X_test = X_test.reshape(-1, 10, 72)
Y_test = Y_test.reshape(-1, 10, 2)

score = model.evaluate(X_test, Y_test)
print(score)
