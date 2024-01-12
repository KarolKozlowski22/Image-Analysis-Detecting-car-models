from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Conv2D, AveragePooling2D, Flatten, Dense, Activation
from tensorflow.keras.optimizers import Adam
import os 
import numpy as np
from PIL import Image

base_dir='/home/karol/Image-Analysis-Detecting-car-models/src'
directories = ['volkswagen', 'skoda', 'mercedes']
images = []
it=0
for folder in directories:
    folder_path = os.path.join(base_dir, folder)
    
    for image_file in os.listdir(folder_path):
        if image_file.lower().endswith('.jpg'):
            image_path = os.path.join(folder_path, image_file)
            print(it)
            img = Image.open(image_path)
            img_array = np.array(img)
            
            images.append(img_array)
            it+=1

image_array = np.array(images)

print(image_array.shape)

# def build_lenet(input_shape):
#     model = Sequential()
#      # Warstwa konwolucyjna C1
#     model.add(Conv2D(filters=6, kernel_size=(5, 5), strides=1, activation='tanh', input_shape=input_shape))
#     # Pooling (Subsampling) Layer S2
#     model.add(AveragePooling2D(pool_size=(2, 2), strides=2))

#      # Warstwa konwolucyjna C3
#     model.add(Conv2D(filters=16, kernel_size=(5, 5), strides=1, activation='tanh'))
#     # Pooling (Subsampling) Layer S4
#     model.add(AveragePooling2D(pool_size=(2, 2), strides=2))

#     # Warstwa konwolucyjna C5
#     model.add(Conv2D(filters=120, kernel_size=(5, 5), strides=1, activation='tanh'))
    
#     # Flatten the CNN output to feed it with fully connected layers
#     model.add(Flatten())
    
#     # Warstwa w pełni połączona F6
#     model.add(Dense(units=84, activation='tanh'))
    
#     # Wyjście
#     model.add(Dense(units=10, activation='softmax'))  # Zmień liczbe jednostek na ilość klas, które masz
    
#     return model

# def train():
#     file = open('ex.txt', 'a')
#     file.close()
#     print("Training model")