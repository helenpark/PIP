# Contains Duplicate III

# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

# solution 1: not fast enough

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        candidates = {}
        for i in xrange(len(nums)):
            print(candidates)
            if nums[i] in candidates:
                for index in candidates[nums[i]]:
                    if abs(index - i) <= k:
                        return True
            
            for a in xrange(nums[i]-t, nums[i]+t+1):
                if a not in candidates:
                    candidates[a] = [i]
                else:
                    candidates[a].append(i)
                
        return False