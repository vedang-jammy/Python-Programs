# this is the example of comparison operators
name = input("enter your name :")
lengthOfName = len(name)
if lengthOfName < 3:
    print("name must be more than three characters")
elif lengthOfName > 50:
    print("name should be maximum 50 characters long")
else:
    print("proceed further...")
