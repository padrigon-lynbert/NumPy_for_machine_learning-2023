import numpy as np
from icecream import ic

# search for the hisghest numbers

Y1 = [36,42,40,42,36,34]
Y2 = [35,40,40,43,36,38]
Y3 = [38,46,45,40,38,42]
Y4 = [42,42,43,30,45,47]

all = np.concatenate([Y1,Y2,Y3,Y4])
unique = np.unique(all)

largest_three = list()

for i in range(3,0,-1):
    largest_three.append(unique[11-i])

# print(f": {largest_three}")


    

# concatenate 3 arrays, after merging them when having an even number in the array you increment 1 in x,  print x, print even numbers
from numpy import random

generate = random.default_rng()

rand1, rand2, rand3 = generate.integers(0,10,size=5), generate.integers(0,10,size=5), generate.integers(0,10,size=5)
# print(rand1,rand2, rand3)
merged = np.concatenate([rand1,rand2,rand3])

even_numbers = list(); x = 0

for i in merged:
    if (i % 2 == 0):
        x += 1
        even_numbers.append(i)

print(f"{x}: {even_numbers}")


