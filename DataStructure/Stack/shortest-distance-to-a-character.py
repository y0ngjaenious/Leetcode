# question link: https://leetcode.com/problems/shortest-distance-to-a-character/

# DP version
"""
def shortestToChar(self, S, C):
        n = len(S)
        res = [0 if c == C else n for c in S]
        for i in range(1, n):
            res[i] = min(res[i], res[i - 1] + 1)
        for i in range(n - 2, -1, -1):
            res[i] = min(res[i], res[i + 1] + 1)
        return res
"""    
        
# Stack version

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        if len(s) == 1:
            return [0]
        
        l_stack = []        
        r_stack = []
        sol = [10 ** 5 for i in range(len(s))] 
        l = 0
        r = len(s) - 1
        left_flag = False
        right_flag = False 
        l_cnt = 0
        r_cnt = 0
        while l <= r:
            if s[l] == c:
                sol[l] = 0
                cnt = 0
                while l_stack:
                    p = l_stack.pop()
                    cnt += 1
                    sol[p] = min(sol[p], cnt)
                l += 1
                l_cnt = 0
                left_flag = True
            else:
                if left_flag:
                    l_cnt += 1
                    sol[l] = min(sol[l], l_cnt)
                l_stack.append(l)
                l += 1
                
            if s[r] == c:
                sol[r] = 0
                cnt = 0
                while r_stack:
                    p = r_stack.pop()
                    cnt += 1
                    sol[p] = min(sol[p], cnt)
                r -= 1
                r_cnt = 0
                right_flag = True
            else:
                if right_flag:
                    r_cnt += 1
                    sol[r] = min(sol[r], r_cnt)  
                r_stack.append(r)    
                r -= 1
                
        if l > r + 1:
            l_cnt -= 1
            r_cnt -= 1
        cnt = 0  
        while l_stack:
            if not right_flag:
                break
            p = l_stack.pop()    
            cnt += 1
            sol[p] = min(sol[p], r_cnt + cnt)
        cnt = 0
        while r_stack:
            if not left_flag:
                break
            p = r_stack.pop()    
            cnt += 1
            sol[p] = min(sol[p], l_cnt + cnt)
        return sol
