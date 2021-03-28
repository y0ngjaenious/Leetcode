# question link: https://leetcode.com/problems/advantage-shuffle/

from collections import defaultdict

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A = sorted(A)
        match_b = defaultdict(list)
        for b in sorted(B, reverse=True):
            if A[-1] > b:
                match_b[b].append(A.pop())
        return [(match_b[b] or A).pop() for b in B]
