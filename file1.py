# this is another example for file handling
fhand = open("test.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("This"):
        print(line)
