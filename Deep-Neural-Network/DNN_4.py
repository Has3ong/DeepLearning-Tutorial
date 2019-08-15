import matplotlib.pyplot as plt
import pandas as pd
from keras.layers import *
from keras.models import *
from keras.utils import *
from sklearn.preprocessing import *
import os

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

iris_data = pd.read_csv(__BASE_DIR__ + '/data/iris.data', index_col=False, names=['sepal_length', 'sepal_width', 'petal_lengh', 'petal_width', 'class'])
print(iris_data.columns)
"""
Index(['sepal_length', 'sepal_width', 'petal_lengh', 'petal_width', 'class'], dtype='object')
"""

Y = LabelEncoder().fit_transform(iris_data['class'])
Y = to_categorical(Y)

iris_data.describe()

X = iris_data.drop('class', axis=1)

X.head()


model = Sequential()
model.add(Dense(512, input_shape=(4,), activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

history = model.fit(X, Y, epochs=20, validation_split=0.1)


plt.figure(figsize=(10,10))
plt.subplot(1, 2, 1)
plt.plot(history.history['acc'], color='r')
plt.plot(history.history['val_acc'], color='b')
plt.title('acc')
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], color='r')
plt.plot(history.history['val_loss'], color='b')
plt.title('loss')
plt.show()






