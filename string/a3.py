# this is another string related program in which we will learn about formatted string and much more
firstName = "John"
lastName = "doe"
work = f"{firstName} [{lastName}] is a worker"  # f"" is string formatter
print(work)

# to get length
print("length of string is " + str(len(work)))
# to convert to upper or lower case
print(work.upper())  # alternatively we can use lower()
# to find a character or sequence of characters
print(work.find("is"))  # it gives first occurence of given character
# to replace a character or string
print(work.replace("worker", "coder"))
# in operator
print("worker" in work)  # it prints if given string is present or not
