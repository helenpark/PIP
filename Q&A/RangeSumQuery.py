# Range Sum Query

# https://leetcode.com/problems/range-sum-query-immutable/#/solutions

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# The idea is fairly straightforward: create an array accu that stores the accumulated sum for nums such that accu[i] = nums[0] + ... + nums[i - 1] in the initializer of NumArray. Then just return accu[j + 1] - accu[i] in sumRange. You may try the example in the problem statement to convince yourself of this idea.



class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums: 
            self.accu += self.accu[-1] + num,

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int 
        :type j: int
        :rtype: int 
        """
        return self.accu[j + 1] - self.accu[i]