# question link: class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(target), len(stamp)
        t, s = list(target), list(stamp)
        answer = []
        def check(i):
            change = False
            for j in range(m):
                if t[i + j] == "?":
                    continue
                if t[i + j] == s[j]:
                    change = True 
                else:
                    return False
            if change:
                t[i:i + m] = ["?"] * m
                answer.append(i)
            return change
        change = True
        while change:
            change = False
            for i in range(n - m + 1):
                change |= check(i)
        return answer[::-1] if t == ["?"] * n else []
