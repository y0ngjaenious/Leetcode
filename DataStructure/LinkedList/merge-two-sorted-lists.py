# question link: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sol = None
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                if sol is None:
                    sol = l1
                    solcur = l1
                    l1 = l1.next
                else:
                    solcur.next = l1
                    solcur = l1
                    l1 = l1.next
            else:
                if sol is None:
                    sol = l2
                    solcur = l2
                    l2 = l2.next
                else:
                    
                    solcur.next = l2
                    solcur = l2
                    l2 = l2.next
            
        if l1 is None:
            while l2 is not None:
                if sol is None:
                    sol = l2
                    solcur = l2
                    l2 = l2.next
                else:
                    solcur.next = l2
                    solcur = l2
                    l2 = l2.next
        else:
            while l1 is not None:
                if sol is None:
                    sol = l1
                    solcur = l1
                    l1 = l1.next
                else:
                    solcur.next = l1
                    solcur = l1
                    l1 = l1.next
                
                
        return sol
