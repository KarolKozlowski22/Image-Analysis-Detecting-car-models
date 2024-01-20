import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

def create_augmented_images(base_dir, directories):
    it = 0
    for folder in directories:
        folder_path = os.path.join(base_dir, folder)
        for image_file in os.listdir(folder_path):
            print(it)
            if 'aug_' in image_file:
                break
            if image_file.endswith('jpg'):
                image_path = os.path.join(folder_path, image_file)
                img = load_img(image_path)
                x = img_to_array(img)
                x = x.reshape((1,) + x.shape)
                prefix = 'aug_' + os.path.splitext(image_file)[0]
                it+=1
                for i, batch in enumerate(datagen.flow(x, batch_size=1, save_to_dir=folder_path, save_prefix=prefix, save_format='jpg')):
                    if i>=5:
                        break
    print("Data augmentation finished.")


               