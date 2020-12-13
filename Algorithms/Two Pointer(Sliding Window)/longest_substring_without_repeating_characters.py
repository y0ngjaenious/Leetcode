# question link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        _max = 1
        p1 = 0
        p2 = 1
        
        dic = {}
        dic[s[0]] = 1
        
        while p2 < len(s):
            
            if s[p2] not in dic or dic[s[p2]] == 0:
                dic[s[p2]] = 1
                cur = p2 - p1 + 1
                if cur > _max:
                    _max = cur
            else:
                while dic[s[p2]] >=1 :
                    dic[s[p1]] -= 1
                    p1 += 1
                dic[s[p2]] = 1
                cur = p2 - p1 + 1
                if cur > _max:
                    _max = cur
            p2 += 1
        return _max
