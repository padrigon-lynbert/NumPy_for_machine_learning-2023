import numpy as np
from icecream import ic as p

# numpy universal function

np1 = np.array([1,2,3,4,5,6,7,8,9]); p(np1)

# qsrt
# p(np.round(np.sqrt(np1),2))

np2 = np.array([-3,-5,0,6,9])
# absolute value
p(np.absolute(np2))

# exponentials
p(np.exp(np1))

# min, max

print("min, max: ", np.max(np1), np.min(np1))

# positive/negative?
p(np2,"\n", np.sign(np2))

# trig

p(np.sin(np1))
p(np.log(np1))