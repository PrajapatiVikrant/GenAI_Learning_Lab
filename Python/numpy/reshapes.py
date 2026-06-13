'''
Reshapes ---->  Reshaping is the process of changing the shape of an array without changing its data like converting 1D array to 2D array or 3D array and vice versa
'''

import numpy as np

# 1D array
one_d_array = np.arange(1, 17)
print("1D Array:")
print(one_d_array)
print()

# Reshaping 1D array to 2D array
two_d_array = one_d_array.reshape(4, 4)
print("2D Array:")
print(two_d_array)
print()

# Reshaping 1D array to 2D array with different dimensions
two_d_array_diff = one_d_array.reshape(2, 8)
print("2D Array with different dimensions:")
print(two_d_array_diff)
print()
# Reshaping 1D array to 3D array here first argument represents the number of 2D arrays, second argument represents the number of rows and third argument represents the number of columns
three_d_array = one_d_array.reshape(2, 2, 4)
print("3D Array:")
print(three_d_array)
print(three_d_array.shape)


 