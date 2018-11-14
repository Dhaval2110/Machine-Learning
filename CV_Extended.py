"""
Yes, it is possible to extract the RGB value of the region in the bounding box.

Assuming you read the image with CV2, then the image is already represented as BGR. All you'd have to do is find a point in the bounding box and extract the BGR value of the point. Note I'm using BGR because that is how OpenCV reads images.

Using the bounding box vertices you used, just calculate a midpoint in the bounding box and extract the BGR value of that midpoint in the image.

# midpoint is ((y_max - y_min) // 2 + y_min, (x_max - x_min) // 2 + x_min)
point = ((70 - 45) // 2 + 45, (250 - 150) // 2 + 150)

b, g, r = image[point]
If the pixels in the bounding boxes have varying colors though, this method won't work. In that case, maybe you want to get the mean BGR values.

# image[y_min:y_max, x_min:x_max]
region = image[45:70, 150:250]

b, g, r = np.mean(region, axis=(0, 1))


INPUTS: https://stackoverflow.com/questions/53304188/how-to-find-rgb-value-of-a-bounded-region-in-an-image-using-python/53305160#53305160
http://marksolters.com/programming/2015/02/27/rgb-histograph.html
"""



import numpy as np
import matplotlib.pyplot as plt
import cv2


i=cv2.imread(r'C:\Users\DHAVAL\Desktop\71Icb3wd6DL._SL1500_.jpg')
im=cv2.resize(i,(1020,880))
#cv2.rectangle(im,(850,586),(840,580),(0,255,0),5)
op=cv2.rectangle(im,(534,56),(510,158),(0,255,0),3)
kk=cv2.imwrite("doc.jpg",op)
#cv2.imshow("image",kk)
#cv2.waitKey(0)
# region = kk[45:70,150:250]

# b, g, r = np.mean(region, axis=(0, 1)

point = (( 158- 56) // 2 + 45, (534-510) // 2 + 510)

b, g, r = kk[point]

print(b)
print(g)
print(r)













