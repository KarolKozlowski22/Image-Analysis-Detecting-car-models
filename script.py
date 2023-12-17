import cv2
import numpy as np
import os

def add_noise(img, noise_level):
    noise = np.random.normal(0, noise_level, img.shape)
    noisy_img = img + noise
    noisy_img = np.clip(noisy_img, 0, 255)
    noisy_img = np.uint8(noisy_img)
    return noisy_img

def main():
    folder_path = "./volkswagen"
    file_list = os.listdir(folder_path)

    for file in file_list:
        if file.endswith(".jpg"):
            img_path = os.path.join(folder_path, file)
            img = cv2.imread(img_path)

            if img is not None:
                noise_level = 25
                noisy_img = add_noise(img, noise_level)
                noisy_img_name = "noisy_" + file
                noisy_img_path = os.path.join(folder_path, noisy_img_name)

                cv2.imwrite(noisy_img_path, noisy_img)

if __name__ == "__main__":
    main()
