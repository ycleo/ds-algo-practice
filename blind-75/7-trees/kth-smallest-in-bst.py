# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# approach 1: Use recursive inorder traversal


class Solution:
    def inOrder(self, root, stack):
        if root:
            self.inOrder(root.left, stack)
            stack.append(root.val)
            self.inOrder(root.right, stack)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        self.inOrder(root, stack)
        return stack[k - 1]

# time: O(n)
# space: O(n)

# approach 2: Use iterative inorder traversal


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            root = curr.right

# T: O(H + k)
# H is a tree height. This complexity is defined by the stack, which contains at least H+k elements, since before starting to pop out one has to go down to a leaf. This results in O(log⁡N+k) for the balanced tree and O(N+k) for completely unbalanced tree with all the nodes in the left subtree.
