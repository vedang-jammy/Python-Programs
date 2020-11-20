# This is an example of tuple
dictionary = {"cup": 4, "dish": 2, "spoon": 20, "bowl": 11}
temp = list()
for (key, value) in dictionary.items():
    temp.append((value, key))
temp = sorted(temp, reverse=True)
print(temp)
print(sorted([(value, key) for key, value in dictionary.items()]))
# this is called list comprehension . It creates dynamic list
# It does the same thing as above for loop
