import sys
if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    graph = [list(map(int,input().split())) for _ in range(n)]
    dp = [0 for _ in range(n+1)]
    m = 0
    for i in range(n):
        m = max(m, dp[i])
        if i + graph[i][0] <= n:
            dp[i + graph[i][0]] = max(graph[i][1] + m, dp[i + graph[i][0]])

    print(max(dp))