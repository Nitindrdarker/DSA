# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        diff = right - left
        if diff == 0 or not head:
            return head
        dummy = ListNode(0, head)
        node = dummy
        for i in range(left - 1):
            node = node.next
        curr = node.next
        prev = None
        for i in range(diff + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        tail = node.next
        node.next = prev
        tail.next = curr
        return dummy.next
        