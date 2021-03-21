# question link: https://leetcode.com/problems/keys-and-rooms/

from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for i in range(len(rooms))]
        
        visit_count = 0
        
        q = deque([0])
        visited[0] = True
        visit_count += 1
        while q:
            u = q.popleft()
            for room in rooms[u]:
                if not visited[room]:
                    visited[room] = True
                    visit_count += 1
                    q.append(room)
        
        return visit_count == len(rooms)
