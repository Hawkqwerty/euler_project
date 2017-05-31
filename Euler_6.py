# -*- coding: utf-8 -*-

"""
Find the difference between the sum of the squares of 
the first one hundred natural numbers and the square of the sum.

"""

b = 0
q = 0
for i in range (1, 101):
    b += i**2
for k in range (1, 101):
    q += k
z = q**2
print (z - b)
