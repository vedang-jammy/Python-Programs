#Write a Python program to remove and print every third number from a list of numbers until the list becomes empty

num_list = []

def print_function(num_list):
    while len(num_list) >= 3:
        print(num_list.pop(2))

items = int(input('enter numbers of items in list:'))

for n in range(1,items+1):
    element = int(input('enter item:'))
    num_list.append(element)

print_function(num_list)