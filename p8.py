import numpy as np 
from icecream import ic 

#search

np1 = np.concatenate((np.arange(10), [3])); print(np1)

x = np.where(np1 == 3); print(x)

ic(x[0], np1[x[0]])

y = np.where(np1 % 2 == 0); print(y) 

#? 