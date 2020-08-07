from PIL import Image
import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
import time
from pixelator import *




#reconstructs, image from pixels (pixel values stored in pixelator file)
array= np.array(pixels, dtype=np.uint8)
new_image=Image.fromarray(array)
new_image.save('reconstructed.png')
new_image.show()
