import sys
sys.setrecursionlimit(10**9)
def dfs(idx):
    visited[idx] = True

    for i in graph[idx]:
        dp[i] += dp[idx]
        dfs(i)


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())

    nums = list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    for i in range(1,len(nums)):
        graph[nums[i]].append(i+1)
    visited = [False] * (n+1)
    for _ in range(m):
        a, b = map(int,input().split())
        dp[a] += b

    dfs(1)
    print(' '.join(map(str,dp[1:])))