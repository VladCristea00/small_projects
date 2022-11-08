import sys
import os
from PIL import Image

#python JPG2PNGconverter.py pokemoni\ new\
 
# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

#check if new folder exists, otherwise create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through pokemoni and then convert images to PNG
#save them to the new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    print(clean_name)
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done')