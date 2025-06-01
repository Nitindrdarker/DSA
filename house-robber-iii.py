# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 # Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def util(node):
            if node == None:
                return [0, 0] #including curr, excluding curr

            included1, excluded1 = util(node.left)
            included2, excluded2 = util(node.right)
            return [excluded2 + excluded1 + node.val, max(included1, excluded1) + max(included2, excluded2)]
        return max(util(root))
            