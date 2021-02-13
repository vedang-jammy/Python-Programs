"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
pal_list = []
for i in range(100, 1000):
    for j in range(100, 1000):
        mul = i * j
        if str(mul) == str(mul)[::-1]:
            pal_list.append(mul)
print(max(pal_list))
