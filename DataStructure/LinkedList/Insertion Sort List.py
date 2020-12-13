#question link: https://leetcode.com/problems/insertion-sort-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        solHead = ListNode()
        cur = head
        while cur is not None:
            next = cur.next
            prev = solHead
            while prev.next is not None and prev.next.val < cur.val:
                prev = prev.next
            cur.next = prev.next
            prev.next = cur
            cur = next
       
        return solHead.next
