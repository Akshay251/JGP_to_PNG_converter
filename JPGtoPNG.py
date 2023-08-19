import os
import sys
from PIL import Image, ImageFilter

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):
    img = Image.open(f'{source_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.filter(ImageFilter.SHARPEN).save(f'{destination_folder}{clean_name}.png', 'png')
    print(f'{clean_name} is processed')
