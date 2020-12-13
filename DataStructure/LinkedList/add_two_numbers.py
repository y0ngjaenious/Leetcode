# question link: https://leetcode.com/problems/add-two-numbers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        solHead = ListNode()
        solcur = solHead
        while l1 is not None and l2 is not None:
            l1next = l1.next
            l2next = l2.next
            
            cur_val = l1.val + l2.val + carry
            val = cur_val % 10
            carry = cur_val // 10
            
            newnode = ListNode(val)
            solcur.next = newnode
            solcur = newnode
            
            l1 = l1next
            l2 = l2next
        
        while l1 is not None:
            l1next = l1.next
            
            cur_val = l1.val + carry
            if cur_val >= 10:
                cur_val -= 10
                carry = 1
            else:
                carry = 0
                
            newnode = ListNode(cur_val)
            solcur.next = newnode
            solcur = newnode
            
            l1 = l1next
            
        while l2 is not None:
            l2next = l2.next
            
            cur_val = l2.val + carry
            if cur_val >= 10:
                cur_val -= 10
                carry = 1
            else:
                carry = 0
                
            newnode = ListNode(cur_val)
            solcur.next = newnode
            solcur = newnode
            
            l2 = l2next
        
        if carry == 1:
            newnode = ListNode(1)
            solcur.next= newnode
            solcur = newnode
        
        return solHead.next
