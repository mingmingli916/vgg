from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

model = VGG16(weights='imagenet', include_top=False, pooling='max')

img_path = 'data/dog.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)


print(x.shape)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

features = model.predict(x)
print(features.shape)
# print(features)