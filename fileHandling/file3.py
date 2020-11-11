# this is another example for file handling
fileHandler = open("mbox.txt")
for line in fileHandler:
    line = line.rstrip()
    words = line.split()
    # guardian : It protects code from throwing errors
    # if len(words) < 3:
    #     continue
    if len(words) < 3 or words[0] != "From":  # we can use either one method
        continue
    print(words[2])
