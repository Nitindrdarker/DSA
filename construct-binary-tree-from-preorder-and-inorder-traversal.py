# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {}
        for i, val in enumerate(inorder):
            inorderIndex[val] = i
        preorder.reverse()
        

        def createTree(left, right):
            if left > right:
                return None
            val = preorder.pop()
            newNode = TreeNode(val=val)
            newNode.left = createTree(left, inorderIndex[val] - 1)
            newNode.right = createTree(inorderIndex[val] + 1, right)

            return newNode
        return createTree(0, len(inorder)-1)