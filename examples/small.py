# This is the example for the smallest number
numbers = [2, 5, 6, 1, 34, 67, 22, 12, 67, 44, 90, 15]
smallNumber = None
for num in numbers:
    if smallNumber is None:
        smallNumber = num
    elif num < smallNumber:
        smallNumber = num
print("smallest number is:", smallNumber)
