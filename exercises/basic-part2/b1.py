#Create all possible strings by using a, e, i, o, u
import random

char_list = ['a','e','i','o','u']

random.shuffle(char_list)
print(' '.join(char_list))