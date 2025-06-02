# Given a binary tree root and an integer target, delete all the leaf nodes with value target.

# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).



# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def util(node):
            if node == None:
                return None
            node.left = util(node.left)
            node.right = util(node.right)
            # print(node.val, node.left, node.right)
            if node.left == None and node.right == None and node.val == target:
                return None
            return node
            
        return util(root)
        
        
