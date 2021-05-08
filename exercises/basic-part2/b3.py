# Write a Python program to count the number of each character of a given text of a text file.

counts = dict()

name = input("enter the name of the file:")

try:
    fileHandler = open(name)
except:
    print("file", name, "does not exist...")
    quit()

for line in fileHandler:
    words = line.split()
    for word in words:
        for letter in word:
            counts[letter] = counts.get(letter, 0) + 1

print(counts)
