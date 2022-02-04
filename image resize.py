import PIL
import os
import os.path
from PIL import Image

f = r'C:\Users\aminu\OneDrive\Desktop\gadgetnow\images - Copy'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((600,600))
    img.save(f_img)

print("Done Image Resize")