import matplotlib.pyplot as plt
import numpy as np
from keras.layers import *
from keras.models import *
from keras.utils import *

x = np.linspace(1, 10, 100)
y = 2 * x + 1

# Model Settings
model = Sequential()

# Settings output shape = 1, activation function = linear, input shape = 1
model.add(Dense(1, activation='linear', input_shape=(1, )))
model.summary()

# Settings loss function = mse, optimizer = sgd
model.compile(loss='mse', optimizer='sgd')

# model training, training count = epochs
model.fit(x, y, epochs=100)

# model prediction, x = 15, 18
prediction_x = []
prediction_x = np.append(prediction_x, 15)
prediction_x = np.append(prediction_x, 18)

prediction_y = model.predict(prediction_x)

# model prediction result y
print(prediction_y)

# result
plt.plot(x, y)
plt.scatter(prediction_x, prediction_y)
plt.show()