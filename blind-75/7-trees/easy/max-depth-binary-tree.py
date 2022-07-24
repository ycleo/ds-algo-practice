# solution 1. recursive DFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
    
# time: O(n)
# space: O(h) or O(log(n)) -> O(n) when skew tree

# =============================================================================

# solution 2. iterative BFS
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 0
        q = deque([root])

        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth

# time: O(n) time
# space: O(leaf) or O(2^h) or O(2^log(n))

# =============================================================================

# solution 3. recursive DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res        
    
# time: O(n)
# space: O(h) or O(log(n))
            
