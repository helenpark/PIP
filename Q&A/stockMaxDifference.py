
# Stock Max Difference

# Given an array of ints, determine the max profit from buying
# and selling once each. You must buy before you sell. if the array continuously 
# decreases, return -1.

def maxDifference( a):
    maxDiff = -1
    low = a[0]
    
    for i in a[1:]:
        if i - low > maxDiff: maxDiff = i - low 
        if i < low: low = i
            
    return maxDiff

# Time Complexity: Primality

# If possible, try to come up with an  primality algorithm, or see what 
# sort of optimizations you can come up with for an  algorithm.
# https://www.hackerrank.com/challenges/ctci-big-o/copy-from/30793312

import math

def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or (n & 1) == 0:
        return False
    
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    
    return True

p = int(input())
for i in range(0, p):
    x = int(input())
    
    s = "Prime" if (isPrime(x)) else "Not prime"
    print(s);