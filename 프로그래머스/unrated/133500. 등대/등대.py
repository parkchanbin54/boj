import sys
sys.setrecursionlimit(10**9)
def dfs(idx,visited,dp,graph):
    visited[idx] = True
    dp[idx][0] = 0
    dp[idx][1] = 1
    
    for i in graph[idx]:
        if not visited[i]:
            dfs(i,visited,dp,graph)
            dp[idx][0] += dp[i][1]
            dp[idx][1] += min(dp[i][0],dp[i][1])
        
    
def solution(n, lighthouse):
    answer = 0
    dp = [[0,0] for _ in range(n+1)]
    
    graph = [[] for _ in range(n+1)]
    
    for house in lighthouse:
        graph[house[0]].append(house[1])
        graph[house[1]].append(house[0])
        
    visited = [False for _ in range(n+1)]
    
    dfs(1,visited,dp,graph)
    
    answer = min(dp[1][0],dp[1][1])
    return answer