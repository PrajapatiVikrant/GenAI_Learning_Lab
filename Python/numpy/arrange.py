import numpy as np

# store 0 to 9 number in numpy array mean
arr = np.arange(10)
print(arr)   # store [0,1,2,3,4,5,6,7,8,9]

# if we want to store specific number to given range then arange method contain two argument
arr = np.arange(5,10)  # store [5,6,7,8,9]
print(arr)

# if we want to store specific number to given range with specific step then arange method contain three argument
arr = np.arange(0,10,2)  # store [0,2,4,6,8]
print(arr)