# // LeetCode 430: 
# // https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

# Could the "head" point to None?  ->  Yes
# How to do for child pointer after flattening?  ->  points to None 

# Test Cases:
    # None => None
    
    # 1 -> 2 -> 3 -> 4        1->2->5->7->8->6->3->4
    #      |
    #      5 -> 6          => 
    #      |
    #      7 -> 8
    
    # 1   => 1->2->3
    # 2
    # 3

# Algo:
    # curr = head
    # curr will travel through the list -> while curr is not None
        # if curr doesn't have a child -> keep moving on
        # else
            #   curr -> curr.next = currNext
            #    |
            #   curr.child = temp
            
            #  let temp travel through the line where child at
            #  temp will connect with currNext
            #  curr.next = curr.child
            #  curr.child = None
            #  curr will move to the next
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        
        curr = head
        while curr is not None:
            if curr.child is None:
                curr = curr.next
            else:
                currNext = curr.next
                temp = curr.child
                while temp.next is not None:
                    temp = temp.next
                    
                if curr.next is not None:
                    temp.next = currNext
                    currNext.prev = temp
                
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
                curr = curr.next
        return head
    
# time: O(n)
# space: O(1)