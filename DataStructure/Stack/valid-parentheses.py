# question link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not stack or stack[-1] != dic[i]:
                    return False
                else:
                    stack.pop(-1)
        if stack:
            return False
        return True
