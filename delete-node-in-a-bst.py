# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def util(root, key):
            if root == None:
                return None
            if key > root.val:
                root.right = util(root.right, key)
            elif key < root.val:
                root.left = util(root.left, key)
            else:
                #found the node
                if root.left == None and root.right == None:
                    return None
                elif root.left == None:
                    return root.right
                elif root.right == None:
                    return root.left
                else:
                    temp = root.right
                    while(temp.left):
                        temp = temp.left
                    root.val = temp.val
                    root.right = util(root.right, temp.val)
            return root
        return util(root, key)