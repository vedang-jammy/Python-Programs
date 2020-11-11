# this is the example for file handling in python

file = input("enter the file name: ")
try:
    fhand = open(file)  # we use try and except to avoid error for nonexixting file
except:
    print("file", file, "doesn't exist")
    quit()
count = 0
for line in fhand:
    count = count + 1
print("there are", count, "lines in file")
