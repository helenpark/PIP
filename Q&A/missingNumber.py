# Missing number

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
# find the one that is missing from the array.

def missingNumber(self, nums):
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)