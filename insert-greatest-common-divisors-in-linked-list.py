# Given the head of a linked list head, in which each node contains an integer value.

# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

# Return the linked list after insertion.

# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.



# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def calcGCD(a, b):
            while a != 0:
                a, b = b % a, a
            return b

        
        dummy = node = ListNode()
        dummy.next = head
        node = node.next
        while(node and node.next):
            firstNum = node.val
            secondNum = node.next.val
            newNode = ListNode(calcGCD(firstNum, secondNum))
            nxt = node.next
            node.next = newNode
            node = node.next
            node.next = nxt
            node = node.next
        return dummy.next



        
        
        