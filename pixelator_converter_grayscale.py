from PIL import Image

img = Image.open('my_fitz_roy.jpg').convert('LA')
img.save('greyscale.png')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

img = mpimg.imread('my_fitz_roy.jpg')

gray = rgb2gray(img)

plt.imshow(gray, cmap = plt.get_cmap('gray'))

plt.savefig('lena_greyscale.png')
plt.show()
