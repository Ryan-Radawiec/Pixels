from PIL import Image
import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
import time




########################################
#Baisc
#opens image for reading
img=Image.open('my_fitz_roy.jpg', 'r')


#resizes image for testing
newImage = img.resize((200, 200))
newImage.save('new_fitz.jpg')


#prints out all the pixel values
pixels = list(newImage.getdata())
width, height = newImage.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
print(newImage.size)
newImage.show()
print(pixels)
#End here for basic version
################################################

pixels2= [[[0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          [0,0,255],
          ]]
#reconstructs, image from pixels
#array= np.array(pixels, dtype=np.uint8)
#new_image=Image.fromarray(array)
#new_image.save('reconstructed.png')




####################################
#prints image in matplotlib
iar=np.asarray(newImage)
plt.imshow(iar)
#print(iar)
plt.show()
######################################


