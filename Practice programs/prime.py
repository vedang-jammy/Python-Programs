"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
num = 600851475143
current_div = 2
while num > current_div:
    if num % current_div == 0:
        num = num / current_div
        current_div = 2
    else:
        current_div += 1
print(current_div)
