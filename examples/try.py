# this is the example of try and except
num = input("enter a number: ")
try:
    numInt = int(num)
except:  # if try block fails , then and only then except block executes
    numInt = (
        -1
    )  # try and except is useful to avoid traceback error ehich occurs when an condition or statement doesnt work
if numInt > 0:
    print("good work")
else:
    print("This is not a number.")
