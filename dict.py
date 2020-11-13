# This is an example of dictionary
count = dict()
line = input("Enter the lines of text: ")
sLine = line.split()
for word in sLine:
    count[word] = (
        count.get(word, 0) + 1
    )  # it does the same thing as below if statements
    # if name not in count:
    #     count[name] = 1
    # else:
    #     count[name] = count[name] + 1
print(count)
