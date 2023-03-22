import sys
sys.setrecursionlimit(10**9)

def dfs(idx):
    visited[idx] = True
    dp[idx][1] = 1
    dp[idx][0] = 0

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)
            dp[idx][0] += dp[i][1]
            dp[idx][1] += min(dp[i][0], dp[i][1])

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    graph =[[] * (n+1) for _ in range(n+1)]
    dp = [[0,0] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n+1)

    dfs(1)
    print(min(dp[1][1],dp[1][0]))

