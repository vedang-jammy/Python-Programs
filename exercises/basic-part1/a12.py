#Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math

p1 = [2,4]
p2 = [3,5]

result = math.sqrt((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2)

print('distance',result)