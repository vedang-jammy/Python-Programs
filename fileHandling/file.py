# this is the example of file handling
file = open("test.txt")
lineNo = 0
for lines in file:
    print(lines)
    lineNo = lineNo + 1
print("linecount:", lineNo)
