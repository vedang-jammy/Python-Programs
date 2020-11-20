# This is the example of tuple where we print first 10 most common words in the file using tuple and dictionary
file = input("enter the file name:")
fileHandler = open(file)
count = dict()
for line in fileHandler:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1
lists = list()
for (key, value) in count.items():
    newTuple = key, value
    lists.append(newTuple)
lists = sorted(lists, reverse=True)
for value, key in lists[:10]:
    print(key, value)
