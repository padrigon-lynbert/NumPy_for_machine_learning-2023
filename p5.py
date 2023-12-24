import numpy as np
from icecream import ic as p 

# array dimensions

# create a 1-D array, get shape
np1 = np.array(np.arange(1,13,1))
print(np1.shape)

# 2-d arr, get shape
np2 = np.array([np.arange(1,7,1), np.arange(7,13,1)])
p(np2)
print(np2.shape) #output: (row, column/elements)

# reshape 2-D
np3 = np1.reshape(3, 4)
p(np3)
p(np3.shape)

# reshape 3-D
np4 = np1.reshape(2,3,2)
p(np4)
p(np4.shape)

# flatten 1-D
np5 = np4.reshape(-1)
p(np5)
p(np5.shape)