# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:43:50 2019

@author: jocel
"""

def prime (n):
    prime = [2]
    primeCheck = 1
    while len(prime) < n:
        isPrime = True
        primeCheck += 2
        for i in prime:
            if (primeCheck % i == 0):
                isPrime = False
        if isPrime == True:
            prime.append(primeCheck)
    print(prime)
    return prime[n-1]

prime(100)