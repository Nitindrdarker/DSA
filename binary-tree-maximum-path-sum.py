# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float("inf")
        def util(root):
            if root == None:
                return 0
            left = util(root.left)
            right = util(root.right)
            leftMax = max(left, 0)
            rightmax = max(right, 0)
            self.res = max(self.res, leftMax + rightmax + root.val)
            return max(left + root.val, right + root.val, root.val)

        v = util(root)
        return max(self.res, v)