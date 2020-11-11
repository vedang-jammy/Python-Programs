# this is another list example

nums = list()  # this defines an empty list that we can use in further program
while True:
    inp = input("enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    nums.append(value)
average = sum(nums) / len(nums)  # sum() and len() are list methods
print(average)
