# this is modified version of network.py
import urllib.request, urllib.parse, urllib.error

fileHandler = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
# we can use this document as a file
count = dict()
for line in fileHandler:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)
