import numpy as np 

# Normal numpy example
# numpy_array=np.array([1.65,2.36,5.3,5.65,9.65])
# print(numpy_array)
# print(type(numpy_array))

# 2D array
# np_2d=np.array([[1.65,2.65,3.69,5.65],
# 			   [6.35,4.65,9.64,8.69]])
# # print(np_2d)
# # print(type(np_2d))
# print(np_2d[1,2:4])   # o/p : [9.64 8.69] i.e. Row 1st , 2 to 4 element i.e. columns
# print(np_2d[:,0])     # o/p : [1.65 6.35] i.e. All row and first colum i.e first column data for all rows

# Find an average value of an array
'''
In some version of numpy there is another imporant difference that you must be aware:
average do not take in account masks, so compute the average over the whole set of data.
mean takes in account masks, so compute the mean only over unmasked values
'''
# print(np.mean(([1.09,2.45,5.56,2.36,9.65,8.65,4.25,7.85])))
# print(np.average(([1.09,2.45,5.56,2.36,9.65,8.65,4.25,7.85])))
# print(np.median(([1.09,2.45,5.56,2.36,9.65,8.65,4.25,7.85])))

##########MATPLOTLIB##########################
# Basic example where year at x axis and pop as y axis
import matplotlib.pyplot as plt
year=[1950,1975,2000,2025]
pop=[1.2,2.4,1.6,6.7]
# # plt.plot(year,pop)
# # plt.show()
# plt.scatter(year,pop)               # as point
# plt.show()

# Histogram

# values=[1.1,2.4,3.5,4.6,5.7,6.8,7.9,8.2,9.3]
# plt.hist(values,bins=3)
# plt.show()

# Customization
plt.xlabel('year')
plt.ylabel('pop')
plt.title("World population")
plt.plot(year,pop)
plt.fill_between(year,pop,0,color='green')
plt.show()