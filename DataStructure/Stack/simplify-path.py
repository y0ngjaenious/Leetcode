# question link: https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for i in path:
            if i == "/":
                if cur == "..":
                    if stack:
                        stack.pop()    
                    cur = ""   
                elif cur == ".":
                    cur = ""
                elif cur:
                    stack.append(cur)
                    cur = ""
            else:       
                cur += i
        if cur == "..":
            if stack:
                stack.pop()         
        elif cur and cur != ".":
            stack.append(cur)         
        if not stack:
            return "/"   
        sol = ""
        while stack:
            sol = "/" + stack.pop() + sol
            
        return sol
