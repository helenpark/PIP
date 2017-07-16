
# Add two array of digit numbers

# https://leetcode.com/problems/add-two-numbers-ii/#/description

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1, list2 = []
        count1, count2 = 0
        
        while (l1 != None) {
            list1[count] = l1.val
            l1 = l1.next
        }
        while (l2 != None) {
            list2[count] = l2.val
            l2 = l2.next
        }
        
        i,j=count1, count2
        carry = 0
        sum = 0
        
        while (i>0 or j>0 or carry>0) :
            sum = carry;
            if i>=0: sum += list1[i]
            if j>=0: sum += list2[j]
            
            carry = sum / 10
            print(sum%10 + " ") 
            
            i=i-1
            j=j-1
        
        return 0
        
        