# // LeetCode 142.
# // https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        
        while head is not None:
            if head.val is None:
                return head
            head.val = None
            head = head.next
        return None
    
# time: O(n)
# space: O(1)