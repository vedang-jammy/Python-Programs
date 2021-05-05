#Find the maximum and minimum numbers from a sequence of numbers

data = []

def max_min(data):
    largest_num = data[0]
    smallest_num = data[0]
    for num in data:
        if num > largest_num:
            largest_num = num
        elif num < smallest_num:
            smallest_num = num
    return largest_num , smallest_num

for i in range(1,7):
    number = int(input('enter list of numbers:'))
    data.append(number)

print('(max,min):',max_min(data))