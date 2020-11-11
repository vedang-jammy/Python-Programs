# this is the the example for split function

line = input("enter your sentence: ")
lineSplit = line.split()  # split function splits the line into list of words .
for item in lineSplit:  # we can use it to do operations on line easily.
    print(
        item
    )  # split uses whitespace as a delimmiter when its without parameters, but we can use other characters as dellimitter. eg split(;)
