from PIL import Image
import os

def resize_images(folder_path, target_size=(224, 224)):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(folder_path, filename))
            img = img.resize(target_size)
            img.save(os.path.join(folder_path, filename))

resize_images('F:\Coding\TEMPLE_RECOGNITION\temple_recognition\recognition\ml_models')
