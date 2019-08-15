
from keras.utils.np_utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import *
from keras.datasets import cifar10

(X_train, Y_train), (X_test, Y_test) = cifar10.load_data()

# X_train.shape (50000, 32, 32, 3)

X_train = X_train / 255.0
X_test = X_test / 255.0

Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)

model = Sequential()

model.add(Conv2D(filters=16, kernel_size=4, padding='same', strides=1, activation='relu', input_shape=(32, 32, 3)))
model.add(MaxPool2D(pool_size=2))
model.add(Conv2D(filters=16, kernel_size=4, padding='same', strides=1, activation='relu'))
model.add(MaxPool2D(pool_size=2))
model.add(Conv2D(filters=16, kernel_size=4, padding='same', strides=1, activation='relu'))
model.add(MaxPool2D(pool_size=2))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

hist = model.fit(X_train, Y_train, batch_size=150, epochs=10, validation_split=0.2)

score = model.evaluate(X_test, Y_test)
print(score)
