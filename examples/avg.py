# this is another example of for Loop
numbers = [1, 45, 76, 33, 3, 67, 899, 9, 3, 67, 99]
count = 0
sum = 0
for num in numbers:
    count = count + 1
    sum = sum + num
print("average no. is: ", sum // count)
