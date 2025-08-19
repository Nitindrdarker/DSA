# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(curr, k):
            while(curr and k > 0):
                curr = curr.next
                k -= 1
            return curr
        
        dummy = node = ListNode(-1, next=head)
        
        while True:
            end = getKth(node, k)
            if not end:
                return dummy.next
            endNext = end.next
            prev, curr = None, node.next
            while(curr != endNext):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            tail = node.next
            tail.next = endNext
            node.next = prev
            node = tail

        return dummy.next
            

        