import numpy as np
from icecream import ic 
from numpy import random

#filtering np arrays using boolean index list

np1 = np.array(np.arange(10))
generate = random.default_rng()
np2 = generate.integers(0,2,10)

filtered1 = [True if i == 1 else False for i in np2]; ic(np1[filtered1])

filtered2 = [True if (i%2==0) else False for i in np1]; ic(np1[filtered2])


# shortcut

filtered3 = np1 > 5; ic(np1[filtered3])