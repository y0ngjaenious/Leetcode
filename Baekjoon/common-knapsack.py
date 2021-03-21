# question link: https://www.acmicpc.net/problem/12865

import sys
N, K = map(int, sys.stdin.readline().split())
item = [[0, 0]]
for i in range(1, N + 1):
    item.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * (K + 1) for _ in range(N+1)]    
for i in range(1, N + 1):
    for j in range(1, K + 1):
        w, v = item[i][0], item[i][1]
        dp[i][j] = dp[i - 1][j] if j < w else max(dp[i - 1][j], dp[i - 1][j - w] + v)
        
print(dp[N][K])
