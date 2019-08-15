import matplotlib.pyplot as plt
import numpy as np
from keras.layers import *
from keras.models import *
from keras.utils import *

# Settings Data
x = np.random.uniform(-np.pi, np.pi, 500)
y = np.random.uniform(-1, 1, 500)

# (500, 2)
X = np.asarray([[x[i], y[i]] for i in range(500)])

sin_func = np.sin(x)

#plt.scatter(x, sin_func)
#plt.scatter(X[:, 0], X[:, 1])
#plt.show()

# (500, )
Y = sin_func < X[:, 1]


#plt.scatter(x, sin_func)
#plt.scatter(X[:, 0][Y == 0], X[:, 1][Y == 0])
#plt.scatter(X[:, 0][Y == 1], X[:, 1][Y == 1])
#plt.show()

# (500, 2)
Y = to_categorical(Y)

# Model Sttings
model = Sequential()

model.add(Dense(10, activation='relu', input_shape=(2, )))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(2, activation='softmax'))

model.summary()

# Settings loss function = crossentropy, optimizer = sgd
model.compile(loss='categorical_crossentropy', optimizer='sgd')

# Model training, training count = epochs
result = model.fit(X, Y, epochs=500)

# Model evaluate
score = model.evaluate(X, Y)

a = [2, 0]
b = [-2, 0]

pred_x = np.vstack((a, b))
pred = model.predict(pred_x)
print(score)
print(pred)

plt.plot(result.history['loss'])
plt.show()

