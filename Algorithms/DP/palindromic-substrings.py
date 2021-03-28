# question link: http://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        sol = 0
        for i in range(len(s)):
            sol += self.helper_odd(s, i)
            if i < len(s) - 1:
                sol += self.helper_even(s, i)
        return sol
    def helper_odd(self, s, i):
        sub_sol = 0
        left = i
        right = i
        while (left >= 0 and right < len(s)):
            if s[left] == s[right]:
                sub_sol += 1
                left -= 1
                right += 1
            else:
                break
        return sub_sol
    def helper_even(self, s, i):
        sub_sol = 0
        left = i
        right = i + 1
        while (left >= 0 and right < len(s)):
            if s[left] == s[right]:
                sub_sol += 1
                left -= 1
                right += 1
            else:
                break
        return sub_sol
