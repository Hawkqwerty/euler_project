# -*- coding: utf-8 -*-

"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.

"""

def even_fib_sum (n):
    a, b = 0, 1
    fib_sum = 0
    while a < n:
        if a % 2 == 0:
            fib_sum += a
        a, b = b, a + b
    return fib_sum
