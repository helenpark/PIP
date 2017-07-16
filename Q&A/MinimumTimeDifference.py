# Minimum Time Difference

# https://leetcode.com/problems/minimum-time-difference/#/description
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
# Input: ["23:59","00:00"]
# Output: 1

class Solution(object):
    
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        lowest = sys.maxint
        
        minArr = []
        for time in timePoints:
            temp = time.split(":")
            minArr.append(60*int(temp[0])+int(temp[1]))
            
        minArr = sorted(minArr)
        print(minArr)
        
        for i in xrange(1, len(minArr)):
            lowest = min(lowest, minArr[i] - minArr[i-1])
            
        # edge case: check left and right side of array 
        lowest = min(lowest, minArr[0]+1440 - minArr[len(minArr)-1])