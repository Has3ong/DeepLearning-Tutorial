
from keras.utils.np_utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import *
from keras.datasets import mnist

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# X_train (60000, 28, 28) to (60000, 28, 28, 1)
X_train = X_train.reshape(60000, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)

X_train = X_train / 255.0
X_test = X_test / 255.0

model = Sequential()
model.add(Conv2D(filters=16, kernel_size=(5, 5), padding='valid', strides=1, activation='relu', input_shape=(28, 28, 1, )))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Conv2D(filters=36, kernel_size=(5, 5), padding='valid', strides=1, activation='relu'))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

hist = model.fit(X_train, Y_train, batch_size=200, epochs=50, validation_split=0.2)

score = model.evaluate(X_test, Y_test)
print(score)
