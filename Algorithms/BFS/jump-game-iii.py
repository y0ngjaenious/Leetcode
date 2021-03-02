# question link: https://leetcode.com/problems/jump-game-iii/

from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = {}
        visited[start] = True
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            if i + arr[i] < len(arr) and i + arr[i] not in visited:
                visited[i + arr[i]] = True
                q.append(i + arr[i])
            if i - arr[i] >= 0 and i - arr[i] not in visited:
                visited[i - arr[i]] = True
                q.append(i - arr[i])
                
        return False
        
# version2: recursion
"""
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] *= -1
            return arr[start] == 0 or self.canReach(arr, start - arr[start]) or self.canReach(arr, start + arr[start])
        
        return False
"""
