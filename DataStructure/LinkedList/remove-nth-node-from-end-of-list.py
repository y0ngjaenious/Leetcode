# question link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nth = None
        prevnth = None
        cur = head
        
        while cur is not None:
            cur = cur.next
            n = n - 1
            if n == 0:
                nth = head
            elif n == -1:
                nth = nth.next
                prevnth = head
            elif n < -1:
                nth = nth.next
                prevnth = prevnth.next
        if prevnth is None:
            return nth.next
        prevnth.next = nth.next
        
        return head
