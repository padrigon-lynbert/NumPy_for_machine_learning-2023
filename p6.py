import numpy as np 
from icecream import ic 

#iterate through np arrays


#1-d
# np1 = np.array(np.arange(1,11,1))

# for i in np1:
#     print(i)


# 2-d
# np2 = np.array([np.arange(1,6,1), np.arange(6,11,1)])

# for i in np2:
#     for j in i:
#         print(j)


# 3-d 

np3 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])

# for i in np3:
#     for j in i:
#         for k in j:
#             print(k)


# nditer (easier way)

for i in np.nditer(np3):
    print(i)

