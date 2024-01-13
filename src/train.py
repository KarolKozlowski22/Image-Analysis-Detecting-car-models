from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Conv2D, AveragePooling2D, Flatten, Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import os 
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import MaxPooling2D

base_dir='/home/bkonopka/pliki/is_semestr_5/Image-Analysis-Detecting-car-models/src'
directories = ['volkswagen', 'skoda', 'mercedes']
images = []
lbl=[]

for folder in directories:
    it=0
    folder_path = os.path.join(base_dir, folder)
    current_size=len(os.listdir(folder_path))
    for image_file in os.listdir(folder_path):
        if image_file.lower().endswith('.jpg'):
            image_path = os.path.join(folder_path, image_file)
            #print(str(it) + "/" + str(current_size))
            img = Image.open(image_path)
            img = img.convert('L')  # Convert image to grayscale
            img = img.resize((128, 128))  # Compress image to size 100x100
            if folder == 'volkswagen':
                lbl.append(0)
            elif folder == 'skoda':
                lbl.append(1)
            elif folder == 'mercedes':
                lbl.append(2)
            # if it%50 == 0:
            #     plt.imshow(img)
            #     plt.show()
            img_array = np.array(img)
            images.append(img_array)
            it+=1
        # if it==1500:
        #     break
image_array = np.array(images)
image_array = image_array / 255.0
image_array = image_array.reshape(-1, 128, 128, 1)

# print(image_array.shape)

# # def build_lenet(input_shape):
# model = Sequential()
#     # Warstwa konwolucyjna C1
# model.add(Conv2D(filters=6, kernel_size=(5, 5), strides=1, activation='tanh', input_shape=(128, 128, 1)))
# # Pooling (Subsampling) Layer S2
# model.add(AveragePooling2D(pool_size=(2, 2), strides=2))

#     # Warstwa konwolucyjna C3
# model.add(Conv2D(filters=16, kernel_size=(5, 5), strides=1, activation='tanh'))
# # Pooling (Subsampling) Layer S4
# model.add(AveragePooling2D(pool_size=(2, 2), strides=2))

# # Warstwa konwolucyjna C5
# model.add(Conv2D(filters=120, kernel_size=(5, 5), strides=1, activation='tanh'))

# # Flatten the CNN output to feed it with fully connected layers
# model.add(Flatten())

# # Warstwa w pełni połączona F6
# model.add(Dense(units=84, activation='tanh'))
# model.add(Dropout(0.5))

model = Sequential()

# Layer 1: Convolutional layer with 64 filters of size 11x11x3
model.add(Conv2D(filters=64, kernel_size=(11,11), strides=(4,4), padding='valid', activation='relu', input_shape=(128,128,1)))

# Layer 2: Max pooling layer with pool size of 3x3
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2)))

# Layer 3-5: 3 more convolutional layers with similar structure as Layer 1
model.add(Conv2D(filters=192, kernel_size=(5,5), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2)))
model.add(Conv2D(filters=384, kernel_size=(3,3), padding='same', activation='relu'))
model.add(Conv2D(filters=256, kernel_size=(3,3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2)))

# Layer 6: Fully connected layer with 4096 neurons
model.add(Flatten())
model.add(Dense(4096, activation='relu'))

# Layer 7: Fully connected layer with 4096 neurons
model.add(Dense(4096, activation='relu'))
# Wyjście
model.add(Dense(units=3, activation='softmax'))  # Zmień liczbe jednostek na ilość klas, które masz

# return model

num_classes = 3
labels = to_categorical(lbl, num_classes)
X_train, X_test, y_train, y_test = train_test_split(image_array, labels, test_size=0.2, random_state=42)

model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
early_stopping = EarlyStopping(monitor='val_loss', patience = 3, restore_best_weights = True)
history = model.fit(X_train, y_train, epochs=15, batch_size=64, validation_data=(X_test, y_test), callbacks=[early_stopping])
plt.plot(history.history['loss'], label='Training loss')
plt.plot(history.history['val_loss'], label='Validation loss')
plt.title('Loss Function Evolution During Training')
plt.ylabel('Loss value')
plt.xlabel('No. epoch')
plt.legend(loc="upper left")
plt.show()

model.save('model3.h5')

#a
# def train():
#     file = open('ex.txt', 'a')
#     file.close()
#     print("Training model")