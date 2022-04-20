# // LeetCode 102.
# // https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS method
from collections import deque 

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        ans = []
        q = deque([root])
        
        while len(q) > 0:
            temp = []
            currLen = len(q)
            
            for _ in range(currLen):
                currNode = q.popleft()
                temp.append(currNode.val)
                if currNode.left is not None:
                    q.append(currNode.left)
                if currNode.right is not None:
                    q.append(currNode.right)
                    
            ans.append(temp)
        return ans

# // time: O(n)
# // space: O(n)