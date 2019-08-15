import keras
import numpy as np
from keras.applications import vgg16
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt
import os

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

vgg = vgg16.VGG16(weights='imagenet')

file = __BASE_DIR__ + '/src/puppy.jpg'
org = load_img(file, target_size=(224, 224))
image = img_to_array(org)

# plt.imshow(np.uint8(image))
# plt.show()

x = np.expand_dims(image, axis=0)
x = vgg16.preprocess_input(x)

pred = vgg.predict(x)

label = decode_predictions(pred)

# print(label)

"""
[[('n02085936', 'Maltese_dog', 0.7064417),
('n02098286', 'West_Highland_white_terrier', 0.1227724),
('n02096437', 'Dandie_Dinmont', 0.054703273),
('n02113624', 'toy_poodle', 0.026998468),
('n02113712', 'miniature_poodle', 0.022263894)]]
"""

vgg.summary()