# question link: https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        return 2 - (s == s[::-1])
