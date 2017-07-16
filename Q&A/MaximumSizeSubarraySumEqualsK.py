
# Maximum Size Subarray Sum Equals k

# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/#/description

# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

# Given nums = [-2, -1, 2, 1], k = 1,
# return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans, acc = 0, 0               # answer and the accumulative value of nums
        mp = {0:-1}                 #key is acc value, and value is the index
        for i in xrange(len(nums)):
            print(mp)
            acc += nums[i]
            if acc not in mp:
                mp[acc] = i 
            if acc-k in mp:
                print("here")
                print("k=",k)
                print("acc=", acc)
                print(acc-k)
                ans = max(ans, i-mp[acc-k])
        return ans