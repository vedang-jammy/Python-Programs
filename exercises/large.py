# this is example of list
numbers = [
    1,
    4,
    6,
    7,
    3,
    8,
    3,
    8,
    2,
    8,
    4,
    8,
    4,
    8,
    43,
]
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print(max)
