import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())

    graph = [[1e9] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a-1][b-1] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    ans = 1e9
    for i in range(n):
        for j in range(i+1,n):
            ans = min(ans,graph[i][j]+graph[j][i])

    if ans == 1e9:
        print(-1)
    else:
        print(ans)


