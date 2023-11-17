import collections
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.serialized_string = ""

        def serializeHelper(node):
            if not node:
                self.serialized_string += "x,"
            else:
                self.serialized_string += str(node.val) + ','
                serializeHelper(node.left)
                serializeHelper(node.right)

        serializeHelper(root)
        return self.serialized_string

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = collections.deque(data.split(','))

        def dfs():
            if data_list[0] == 'x':
                data_list.popleft()
                return None
            root = TreeNode(int(data_list.popleft()))
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# T: O(N)
# S: O(N)
