# question link: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        stack = []
        sol = 0
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if dic[stack[-1]] >= dic[i]:
                    stack.append(i)
                else:
                    cur = dic[i]
                    while stack and dic[stack[-1]] < dic[i]:
                        cur -= dic[stack.pop()]
                    sol += cur
                    
        while stack:
            sol += dic[stack.pop()]
            
        return sol
