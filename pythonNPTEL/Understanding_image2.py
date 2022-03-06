import numpy as np
from PIL import Image

im = Image.open('Image2.png')
rgb_im = im.convert('RGB')

r,g,b = rgb_im.getpixel((1,1))

print(r,g,b)