import os 
from PIL import Image
import numpy as np

def prepare_data_for_model(base_dir, directories):
    images = []
    labels = []
    num_of_img_in_each_folder = []
    for folder in directories:
        folder_path=os.path.join(base_dir, folder)
        num_of_img_in_each_folder.append(len(os.listdir(folder_path)))
    min_num_of_img = min(num_of_img_in_each_folder)
    for folder in directories:
        it=0
        folder_path = os.path.join(base_dir, folder)
        for image_file in os.listdir(folder_path):
            if image_file.lower().endswith('.jpg'):
                image_path = os.path.join(folder_path, image_file)
                img = Image.open(image_path)
                img = img.convert('L')  
                img = img.resize((128, 128))  
                if folder == 'volkswagen':
                    labels.append(0)
                elif folder == 'skoda':
                    labels.append(1)
                elif folder == 'mercedes':
                    labels.append(2)
                img_array = np.array(img)
                images.append(img_array)
                it+=1
            if it == min_num_of_img:
                break
                
    image_array = np.array(images)
    image_array = image_array / 255.0
    image_array = image_array.reshape(-1, 128, 128, 1)
    return image_array, labels