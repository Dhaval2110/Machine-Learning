# Luma value calculation in python
'''
References : 
https://www.codementor.io/innat_2k14/image-data-analysis-using-numpy-opencv-part-1-kfadbafx6
https://stackoverflow.com/questions/6442118/python-measuring-pixel-brightness
https://www.hackerearth.com/practice/notes/extracting-pixel-values-of-an-image-in-python/
https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv
'''


# Global Imports
import os
import xlwt 

# Local Imports
from PIL import Image
from xlwt import Workbook 

os.chdir(r'C:\Users\DHAVAL\Desktop\Luma4')                        # Changing directory to folder itself
for filename in os.listdir(os.getcwd()):                          # List out all the files to run one by one
	#print(filename)
	imag = Image.open(filename)
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
	 
  ######## NEED TO WORK HERE MORE ###########
	# # Workbook is created 
	# wb = Workbook()   
	# # add_sheet is used to create sheet. 
	# sheet1 = wb.add_sheet('Sheet 1')   
	# sheet1.write(1, 0, filename) 
	# sheet1.write(1, 1, luma) 
	# wb.save('xlwt_example.xls')
	with open('out.txt', 'w') as f:
			print(luma, filename,file=f)
		
'''
Try this too:
os.chdir(r'C:\Users\DHAVAL\Desktop\Luma4')
for filename in os.listdir(os.getcwd()):
	imag = Image.open(filename,'r')
	pix_val = list(imag.getdata())
	pix_val_flat = [x for sets in pix_val for x in sets]
	avg=mean(pix_val_flat)
	print(avg)
	
	replace with dictionary and then 

import os
import pandas as pd
dataset = pd.read_csv("dhaval.csv")
x=dataset.iloc[0: , 0]
x=list(x)
print(x)
'''
