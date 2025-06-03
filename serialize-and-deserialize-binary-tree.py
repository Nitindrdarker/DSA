# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself



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

        # preorder serilization
        s = []
        def util(root):
            if root == None:
                s.append("@")
                return
            s.append(str(root.val))
            util(root.left)
            util(root.right)
            return None
        util(root)
        return ','.join(s)
        

    def deserialize(self, data):
        s = data.split(',')
        # print(s)
        self.index = 0
        def create():
            if s[self.index] == '@':
                self.index += 1
                return None
            root = TreeNode(val = int(s[self.index]))
            self.index += 1
            root.left = create()
            root.right = create()
            return root
        return create()
            