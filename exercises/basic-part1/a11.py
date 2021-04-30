#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

def sumOfintegers(a,b,c) :
    sum1 = 0
    if a==b or a==c or c==b:
        sum1 = 0
    else:
        sum1 = a+b+c
    return sum1
    
print(sumOfintegers(2,4,4))