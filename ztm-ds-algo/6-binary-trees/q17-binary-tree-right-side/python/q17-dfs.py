# // LeetCode 199.
# // https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        def dfs(node, currLevel):
            if node is None:
                return
            if currLevel >= len(ans):
                ans.append(node.val)
            if node.right:
                dfs(node.right, currLevel + 1)
            if node.left:
                dfs(node.left, currLevel + 1)
        
        ans = []
        dfs(root, 0)
        return ans

# // time: O(n)
# // space: O(n)