# question link: https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        node_dic = {} 
        cur = head
        sol_cur = Node(cur.val)
        sol_head = sol_cur
        while cur:
            node_dic[cur] = sol_cur
            if cur.random:
                if cur.random in node_dic:
                    _random = node_dic[cur.random]
                else:
                    _random= Node(cur.random.val)
                    node_dic[cur.random] = _random
            else:
                _random = None    
            if cur.next in node_dic:
                _next = node_dic[cur.next]     
            else:
                if cur.next:
                    _next = Node(cur.next.val)    
                else:
                    _next = None    
            sol_cur.next = _next
            sol_cur.random = _random
            sol_cur = sol_cur.next
            cur = cur.next
            
        return sol_head 
