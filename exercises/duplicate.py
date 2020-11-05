# this is the example program for the list operations
numbers = [1, 4, 3, 7, 8, 2, 0, 6, 3, 4, 7, 9]
numbersNew = []
for number in numbers:
    if number not in numbersNew:
        numbersNew.append(number)
print(numbersNew)
