# this is another file handling example and dictionaries example

counts = dict()
name = input("enter name of the file: ")
try:
    fileHandler = open(name)
except:
    print("file", name, "does not exist")
    quit()
for line in fileHandler:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
bigCount = None
bigWord = None
for (
    word,
    count,
) in counts.items():  # python supports duel iteration variables for dictionaries
    if bigCount is None or count > bigCount:
        bigCount = count
        bigWord = word
print(
    "word occured maximum times: ", bigWord, "\n no. of times word occured: ", bigCount
)
