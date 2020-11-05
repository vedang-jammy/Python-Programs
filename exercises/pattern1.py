# this is the example for nested loops

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    count = ""
    for y in range(x):
        count += "x"
    print(count)
