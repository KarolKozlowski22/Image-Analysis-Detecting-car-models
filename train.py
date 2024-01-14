from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import os
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from data_for_model import prepare_data_for_model
from data_augmentation import create_augmented_images
from create_model import create_model
from cost_function import plot_cost_function

base_dir=os.getcwd()
directories = ['mercedes', 'skoda', 'volkswagen']
create_augmented_images(base_dir, directories)
image_array, init_labels = prepare_data_for_model(base_dir, directories)
model=create_model()

num_classes = 3
labels = to_categorical(init_labels, num_classes)
X_train, X_test, y_train, y_test = train_test_split(image_array, labels, test_size=0.2, random_state=42)
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
early_stopping = EarlyStopping(monitor='val_loss', patience = 3, restore_best_weights = True)
history = model.fit(X_train, y_train, epochs=15, batch_size=64, validation_data=(X_test, y_test), callbacks=[early_stopping])
model.save('model3.h5')
plot_cost_function(history)




