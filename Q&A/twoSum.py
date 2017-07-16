
# Two Sum

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    matches = {}
    for i in xrange(1, len(nums)):
        print(nums[i])
        print(matches)
        if nums[i] in matches:
            return [matches[nums[i]], i]
        else: 
            matches[target - nums[i]] = i
    return "no matches :("