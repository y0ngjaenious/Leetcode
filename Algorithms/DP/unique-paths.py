# question link: https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        T = m + n - 2
        num = 1
        denom = 1
        for i in range(n - 1):
            num *= T - i
            denom *= i + 1
                
        return num // denom
