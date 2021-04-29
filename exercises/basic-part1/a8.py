#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
number = int(input('enter the number:'))
if number  > 17:
    print('double the difference:',abs(17-number)*2)
else:
    print('difference:',17-number)