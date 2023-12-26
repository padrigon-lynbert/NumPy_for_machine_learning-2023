import numpy as np 
from icecream import ic 

#sort()

#numerical
np1 = np.array([1,5,6,4,8,9,7,3,2,0])
ic(np1, np.sort(np1))


#Alphabetical

np2 = np.array(["Elijah", "Rafael", "Benedict", "Steeve", "Lynbert"])
print(str(np2) + f"\n{np.sort(np2)}")

sort_a_word = sorted(list(np2[4])); print(sort_a_word) #using list()

sort_a_word2 = sorted([char for char in np2[4]]); print(sort_a_word2) #using list comprehension, both very pythonic way ig
    #these last two isnt part of the numpy tutorial I'm just messing up a little to aid my boredom and feed my curiosity

#bool
sleep = [True, False, False, True]
ic(np.sort(sleep))


# return the copy, original not change by the sort()
ic(np1)

# 2-d 
np4 = np.array([[2,3,5,4,1], [6,10,9,8,7]])
ic(np4, np.sort(np4))