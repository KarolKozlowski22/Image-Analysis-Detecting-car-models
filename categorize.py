import tensorflow as tf
from PIL import Image

def categorize(image_path):
    model = tf.keras.models.load_model('model3.h5')
    image = Image.open(image_path)
    resized_image = image.resize((128, 128))
    resized_image = resized_image .convert('L')
    normalized_image = tf.keras.preprocessing.image.img_to_array(resized_image) / 255.0
    expanded_image = tf.expand_dims(normalized_image, axis=0)
    predictions = model.predict(expanded_image)
    category_index = tf.argmax(predictions, axis=1).numpy()[0]
    
    if category_index == 0:
        return "Volkswagen"
    elif category_index == 1:
        return "Skoda"
    elif category_index == 2:
        return "Mercedes"
    else:
        return "None"


