import numpy as np
from icecream import ic

# slicing array

np1 = np.array([1,2,3,5,6,7,8,9])

# return 2-5
print(np1[1:4])

# return something til the end of the array
print(np1[1:])

# return negative slices
print(np1[-5:-2])

# steps
print(np1[ : :3])

# slice a 2d array
np2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
ic(np2)

# pull slices
print(np2[0:2, 1:3])
print(np2[0,3])

#pull whole arrays

print(np2[0], np2[1])
