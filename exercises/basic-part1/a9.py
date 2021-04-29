#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum

def sum_of_three(a,b,c):
    sum = a+b+c
    if a==b==c:
        sum = sum*3
    return sum

print(sum_of_three(4,2,5))
print(sum_of_three(5,5,5))
        