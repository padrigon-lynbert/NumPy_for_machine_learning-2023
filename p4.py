import numpy as np 
from icecream import ic as p 

# copy vs view in numpy 

#view - original and copy variable are connected, if one is changed another one adapt and copy the changes
p("view")
np1 = np.array([1,2,3,4,5,6,7,8,9])
np1view = np1.view()

np1[0] = 44

p(np1, np1view)

np1 = np.array([1,2,3,4,5,6,7,8,9])
np1view = np1.view()

np1view[0] = 44

p(np1, np1view)

# copy - the original and the copy variables are not connected
p("copy")

np1 = np.array([1,2,3,4,5,6,7,8,9])
np1copy = np1.copy()

np1[0] = 44

p(np1, np1copy)

np1 = np.array([1,2,3,4,5,6,7,8,9])
np1copy = np1.copy()

np1copy[0] = 44

p(np1, np1copy)

