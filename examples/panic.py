# this is the example to understand list slicing
phrase = "Don't panic!"
plist = list(phrase)
newPhrase = "".join(plist[1:3])
newPhrase = newPhrase + "".join([plist[5], plist[4], plist[7], plist[6]])
print(newPhrase)
