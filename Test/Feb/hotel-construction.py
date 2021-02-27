def bfs(graph, s, t):
    l = 0
    visited = set([s])
    prev = {}
    queue = deque([s])
    while queue:
        u = queue.popleft()
        if u == t:
            break
        for v in graph[u]:
            if v not in visited:
                queue.append(v)
                visited.add(v)
                prev[v] = u
                
    while u != s:
        u = prev[u]
        l += 1
    return l
  
def numberOfWays(roads):
    sol = 0
    n = len(roads) + 1
    cities = [i for i in range(n)]
    g = [[] for i in range(n)]
    for u, v in roads:
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    for i, j, k in combinations(cities, 3):
        _1 = bfs(g, i, j)
        _2 = bfs(g, j, k)
        _3 = bfs(g, k, i)
        if _1 == _2 == _3:
            sol += 1
    
    return sol
