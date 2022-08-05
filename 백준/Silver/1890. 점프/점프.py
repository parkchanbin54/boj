import sys
input = sys.stdin.readline
n = int(input())

graph = [[0] * n for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int,input().split()))

dp = [[0] * n for _ in range(n)]
dp[0][graph[0][0]] = 1
dp[graph[0][0]][0] = 1

for i in range(n):
    for j in range(n):
        if j + graph[i][j] < n and dp[i][j] != 0 and graph[i][j] != 0:
            dp[i][j+graph[i][j]] += dp[i][j]
        if i + graph[i][j] < n and dp[i][j] != 0 and graph[i][j] != 0:
            dp[i+graph[i][j]][j] += dp[i][j]

print(dp[n-1][n-1])