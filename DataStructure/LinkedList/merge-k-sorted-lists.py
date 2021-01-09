# question link: https://leetcode.com/problems/merge-k-sorted-lists/

import heapq
from collections import defaultdict
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = None
        num_empty = 0
        heap = []
        dic = defaultdict(int)
        for i in lists:
            if i is None:
                num_empty += 1
                continue
            dic[i.val] += 1
            heapq.heappush(heap, (int(i.val), dic[i.val], i))
        cur = None
        while num_empty < len(lists):
            _next = heapq.heappop(heap)[2]
            if head is None:
                head = _next
            else:
                cur.next = _next
            update = _next.next
            _next.next = None
            cur = _next
            if update is None:
                num_empty += 1
            else:
                dic[update.val] += 1
                heapq.heappush(heap, (update.val, dic[update.val], update))
        return head
                
