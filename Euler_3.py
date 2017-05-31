# -*- coding: utf-8 -*-

"""
What is the largest prime factor of the number 600851475143 ?

"""

def amount_factors(n): # returns the number of factors that an integer 'n' has.
    counter = 0
    for x in range(1,n+1):
        if n % x == 0:
            counter += 1
    return counter

def is_prime(n): # returns whether or not an integer 'n' is prime.
    if amount_factors(n) == 2 :
        return True
    else:
        return False

def list_prime_factors(n): # returns a list of all of the primes factors of an integer 'n'.            
    for x in range(1,n+1):
        if n % x == 0 and is_prime(x):
            print(x)
            if x > n**0.5:
                break
            
list_prime_factors(600851475143)   
      