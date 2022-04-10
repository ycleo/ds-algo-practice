# Easy 83. 
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        currentNode = head
        
        while currentNode is not None:
            nextNode = currentNode.next
            
            while nextNode is not None and nextNode.val == currentNode.val:
                nextNode = nextNode.next
            currentNode.next = nextNode
            
            currentNode = nextNode
        
        return head

# time: O(n)
# space: O(1)

