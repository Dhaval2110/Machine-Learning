import numpy as np 

# Normal numpy example
# numpy_array=np.array([1.65,2.36,5.3,5.65,9.65])
# print(numpy_array)
# print(type(numpy_array))

# 2D array
np_2d=np.array([[1.65,2.65,3.69,5.65],
			   [6.35,4.65,9.64,8.69]])
# print(np_2d)
# print(type(np_2d))
print(np_2d[1,2:4])   # o/p : [9.64 8.69] i.e. Row 1st , 2 to 4 element i.e. columns
print(np_2d[:,0])     # o/p : [1.65 6.35] i.e. All row and first colum i.e first column data for all rows
 