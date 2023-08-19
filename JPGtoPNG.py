import os
import sys
from PIL import Image, ImageFilter

source_folder = sys.argv[1]         
destination_folder = sys.argv[2]

if not os.path.exists(destination_folder):        #the destination folder is created if it doesn't exist
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):        #traverse through the files in the destination folder, converts and finally saves to the destination folder
    img = Image.open(f'{source_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.filter(ImageFilter.SHARPEN).save(f'{destination_folder}{clean_name}.png', 'png')
    print(f'{clean_name} is processed')
