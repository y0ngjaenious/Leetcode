# question link: https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        pp = 1
        pn = 2
        for i in range(2, n):
            cur = pp + pn
            pp = pn
            pn = cur
        return cur
