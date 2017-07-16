
# Reverse singly linked list

# https://leetcode.com/problems/reverse-linked-list/#/description

def reverse_list(head):
    new_head = None  
    while head:
        temp = head  
        head = temp.next  
        temp.next = new_head  
        new_head = temp
    return new_head