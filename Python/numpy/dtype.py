'''
dtype parameter ---> which can help us out with deciding about the size of the data we are going to 
store inside array
'''

import numpy as np


# this array can only store integer values and it will take 32 bytes of memory for each element
numpy_arr = np.array([1,2,3,4], dtype=np.int8)

print(numpy_arr)

numpy_arr = np.array([1.4,2.5,3.6,4.7], dtype=np.float64)
print(numpy_arr)