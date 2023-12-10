from PIL import Image
import os
import imagehash

folder_path = 'test_pictures'
files = os.listdir(folder_path)

image_files = [file for file in files]
hashes = []

images = []
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    extension = os.path.splitext(image_file)[-1]

    if extension != ".HEIC":
        with Image.open(image_path) as img:
            print(image_path)
            print(imagehash.phash(img))

            images.append(img.copy())