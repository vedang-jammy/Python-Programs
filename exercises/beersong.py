# this is the fun program to understand range() funtion
import random

word = "bottles"
num = random.randint(1, 15)
for bottleNumber in range(num, 0, -1):
    print(bottleNumber, word, "of beer on the shelf")
    print(bottleNumber, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if bottleNumber == 1:
        print("No more bottles left on shelf")
    else:
        newBottleNumber = bottleNumber - 1
        if newBottleNumber == 1:
            word = "bottle"
        print(newBottleNumber, word, "left on the shelf")
