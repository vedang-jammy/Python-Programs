# Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations

a1 = []
a2 = []
a3 = []


def equal_values(a1, a2, a3, target):
    for n in range(0, len(a1) + 1):
        if a1[n] + a2[n] + a3[n] == target:
            print("values are:", a1[n], a2[n], a3[n])


target = int(input("enter the target value:"))
size = int(input("enter the size of array:"))

for i in range(0, size):
    num = int(input("enter elements of 1st array:"))
    a1.append(num)
for i in range(0, size):
    num = int(input("enter elements of 2nd array:"))
    a2.append(num)
for i in range(0, size):
    num = int(input("enter elements of 3rd array:"))
    a3.append(num)

equal_values(a1, a2, a3, target)
