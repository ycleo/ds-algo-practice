# // LeetCode 222.
# // https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root):
        def getHeight(root):
            height = 0
            currNode = root
            while currNode.left is not None:
                currNode = currNode.left
                height += 1
            return height
        
        
        def dfs(node, currLevel, lastLevelNum):
            if node is None:
                return
            if currLevel == height:
                lastLevelNum.append(node)
            
            if node.left is not None:
                dfs(node.left, currLevel + 1, lastLevelNum)
            if node.right is not None:
                dfs(node.right, currLevel + 1, lastLevelNum)
            else:
                return
        
        # edge case
        if root is None:
            return 0
        
        # count the node number except the last level 
        height = getHeight(root) # O(logN)
        count = 2**height - 1
        
        # count the last level node number
        lastLevelNum = []
        dfs(root, 0, lastLevelNum)
        
        return count + len(lastLevelNum)

# time: O(n)
# space: O(n)