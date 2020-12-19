# question link: https://leetcode.com/problems/longest-palindromic-substring/

## DP version: TLE...(I don't know why)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        l = len(s)
        
        M = [[False for i in range(l)] for j in range(l)]
        
        res = s[0]
            
        for i in range(l-1, -1, -1):
            for j in range(i, l):
                if i == j:
                    M[i][j] = True
                elif j == i + 1:
                    M[i][j] = s[i] == s[j]
                elif j > i + 1:
                    M[i][j] = s[i] == s[j] and M[i + 1][j - 1]
                    
                if M[i][j] and j - i + 1 > len(res):
                    res = s[i:j + 1]
        
        return res
"""

## Accepted version
class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            cur = self.expendCenter(s, i, i)
            if len(cur) > len(res):
                res = cur
            
            cur = self.expendCenter(s, i, i+1)
            if len(cur) > len(res):
                res = cur
        return res
 

    def expendCenter(self, s, l, r):
        while l >= 0 and (r < len(s) and s[l] == s[r]):
            l -= 1; r += 1
        
        return s[l+1:r]
