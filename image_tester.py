import os
from PIL import Image

# this script checks for corrupted images
# enter the path to the folder that needs to be checked below

folder = '../classifying_illuminated_charters/data/train_recto_verso/val/1/'

for filename in os.listdir(folder):
    try:
        im = Image.open(folder + filename)
        im.verify()
        im.close()
        im = Image.open(folder + filename) 
        im.transpose(Image.FLIP_LEFT_RIGHT) # check for truncated images
        im.close()
    except:
        print("Cannot load : {}".format(filename))