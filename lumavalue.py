# Luma value calculation in python

from PIL import Image 
imag = Image.open(r"C:\Users\DHAVAL\Desktop\DSC08361.JPG")
#Convert the image te RGB if it is a .gif for example
imag = imag.convert ('RGB')
#coordinates of the pixel
X,Y = 0,0
#Get RGB
pixelRGB = imag.getpixel((X,Y))
R,G,B = pixelRGB 
luma = 0.2126*R + 0.7152*G + 0.0722*B
#brightness = sum([R,G,B])/3 
print(luma,"Luma")
