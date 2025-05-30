# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def util(root, currMax):
            if root == None:
                return 0
            val = 0
            if root.val >= currMax:
                val += 1
            left = util(root.left, max(currMax, root.val))
            right = util(root.right, max(currMax, root.val))
            return val + left + right
        return util(root, root.val)