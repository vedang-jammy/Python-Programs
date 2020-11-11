# this is another example for file handling
# fhand = open("test.txt")
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith("This"):
#         print(line)
fhand = open("test.txt")  # we can use both methods.this one or commented one.
for line in fhand:
    line = line.rstrip()
    if not line.startswith("This"):
        continue
    print(line)
    if "is" in line:  # use of 'in' operator in the file
        print(line)
