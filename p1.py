import numpy as np
from icecream import ic

lst = [1,2,3,4,5]
print(lst)

# numpy - numeric python
# ndarray - n-dimensional array

np0 = np.zeros(10); ic(np0)

np1 = np.array([1,2,3,4,5,6,7,8,9])

np2 = np.arange(10); ic(np2)

np3 = np.arange(0,10,2); ic(np3)

# multimensional zeroes

np4 = np.zeros((2,5)); ic(np4)

# full()

np5 = np.full((5), 7); print(np5)

# convert python list to numpy

my_list = [1,2,3,4,5,6]
np6 = np.array(my_list); ic(np6)

# accesing certain element
print(np6[5])

