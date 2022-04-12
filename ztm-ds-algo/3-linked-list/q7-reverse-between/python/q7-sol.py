# // LeetCode 92.
# // https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseLinkedList(head, position, right):
    prevNode, currNode = None, head
    
    while position <= right:
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
        position += 1
    
    return prevNode, currNode

#   1   ->  2  -> 3 ->   4    ->  5 
# start   tail         header    end

#   1   ->   4   -> 3 ->   2    ->  5 
# start    header         tail     end

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        position = 1
        start = curr = head
        
        while position < left:
            start = curr
            curr = curr.next
            position += 1
        
        tail = curr
        
        header, end = reverseLinkedList(curr, position, right)
            
        start.next = header
        tail.next = end
        
        return head if left > 1 else header

# time: O(n)
# space: O(1)