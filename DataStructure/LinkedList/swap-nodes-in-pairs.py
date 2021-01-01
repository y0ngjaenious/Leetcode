# question link: https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        isHead = True
        while cur is not None and cur.next is not None:
            _next = cur.next
            cur.next = _next.next
            _next.next = cur
          
            if isHead:
                head = _next
                isHead = False
            else:
                prev.next = _next
            prev = cur
            cur = cur.next

        return head
