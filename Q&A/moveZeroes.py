
# Move Zeroes

# https://leetcode.com/problems/move-zeroes/#/description

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


def move_zeros(lst):
  n = len(lst)
  lst[:] = filter(None, lst)
  lst.extend([0] * (n - len(lst)))