# Simple OpenCV to read , show and save an image

# Libraries to be import
import numpy as np 
import cv2
from matplotlib import pyplot as plt

# Image Read
img=cv2.imread(r'C:\Users\DHAVAL\Desktop\IMG_20180504_190959.jpg',1)

# Image Display
cv2.imshow('image',img)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('bhachoo.png',img)

# Matplotlib to plot an image
img = cv2.imread(r'C:\Users\DHAVAL\Desktop\IMG_20180504_190959.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
