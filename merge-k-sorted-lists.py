# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.



# Definition for singly-linked list.
from ast import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        def merge(node1, node2):
            dummy = node = ListNode()
            while(node1 and node2):
                if node1.val < node2.val:
                    node.next = node1
                    node1 = node1.next
                    node = node.next
                else:
                    node.next = node2
                    node2 = node2.next
                    node = node.next
            if node1:
                node.next = node1
            if node2:
                node.next = node2
            return dummy.next
        dummy = ListNode()
        dummy.next = lists[0]
        for i in range(1, len(lists)):
            dummy.next = merge(dummy.next, lists[i])
        return dummy.next



