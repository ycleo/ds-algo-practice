# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(node) -> int:
            if not node:
                return -1
            leftLength = dfs(node.left)
            rightLength = dfs(node.right)
            res[0] = max(res[0], 2 + leftLength + rightLength)
            
            return 1 + max(leftLength, rightLength)
            
        dfs(root)
        return res[0]
    
# time: O(n)
# space: O(h) or O(log(n))