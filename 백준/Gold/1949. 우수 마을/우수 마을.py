import sys
sys.setrecursionlimit(10 ** 9)
def dfs(idx):
    visited[idx] = True
    dp[idx][0] = 0
    dp[idx][1] = vil[idx]

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)
            dp[idx][1] += dp[i][0]
            dp[idx][0] += max(dp[i][0],dp[i][1])


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    vil = [0] + list(map(int,input().split()))

    graph = [[] for _ in range(n+1)]

    dp = [[0,0] for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(n-1):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1)

    print(max(dp[1][0],dp[1][1]))

