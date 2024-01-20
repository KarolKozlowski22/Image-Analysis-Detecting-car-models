from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from data_for_model import prepare_data_for_model
from data_augmentation import create_augmented_images
from create_model import create_model
from cost_function import plot_cost_function
import os 
import numpy as np

base_dir=os.getcwd()
directories = ['skoda', 'mercedes', 'volkswagen', 'lexus', 'inne']
# create_augmented_images(base_dir, directories)

image_array, init_labels = prepare_data_for_model(base_dir, directories)
model=create_model()

num_classes = 5
labels = to_categorical(init_labels, num_classes)
X_train, X_val, y_train, y_val = train_test_split(image_array, labels, test_size=0.2, shuffle=True, random_state=42)

model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
early_stopping = EarlyStopping(monitor='val_loss', patience = 3, restore_best_weights = True)
num_of_img_in_each_folder = []
for folder in directories:
        folder_path=os.path.join(base_dir, folder)
        num_of_img_in_each_folder.append(len(os.listdir(folder_path)))
print(num_of_img_in_each_folder)
history = model.fit(X_train, y_train, epochs=15, batch_size=64, validation_data=(X_val, y_val), callbacks=[early_stopping])
model.save('model1.keras')
plot_cost_function(history)




