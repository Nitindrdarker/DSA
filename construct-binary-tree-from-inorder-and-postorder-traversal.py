# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {}
        for i, val in enumerate(inorder):
            inorderIndex[val] = i
        
        

        def createTree(left, right):
            if left > right:
                return None
            val = postorder.pop()
            newNode = TreeNode(val=val)
            newNode.right = createTree(inorderIndex[val] + 1, right)
            newNode.left = createTree(left, inorderIndex[val] - 1)
            

            return newNode
        return createTree(0, len(inorder)-1)