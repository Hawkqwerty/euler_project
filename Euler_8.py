# -*- coding: utf-8 -*-

"""
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

"""

import re

pattern = re.compile('[^0-9]')
k = 0
a = []
w = []

with open ('data.txt') as f:
   for line in f:
       a += [int(x) for x in pattern.sub('', line)]
       
while len (a) > 13:
    count = 1      
    for i in range (0, 13):
        count *= a [i] 
    w.append(count)
    a.pop(0)
    
print (max(w))
