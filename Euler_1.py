# -*- coding: utf-8 -*-

"""
Find the sum of all the multiples of 3 or 5 below 1000.

"""

num_sum=0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        num_sum += i
print (num_sum)