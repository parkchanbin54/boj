import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())
    graph = [[0] * n for _ in range(n)]
    graph2 = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int,input().split())
        graph[a-1][b-1] = 1
        graph2[b-1][a-1] = 1


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
                if graph2[i][k] and graph2[k][j]:
                    graph2[i][j] = 1
    ans = 0
    for i in range(n):
        if graph[i].count(0) < n//2 + 1:
            ans += 1
        elif graph2[i].count(0) < n//2 + 1:
            ans += 1

    print(ans)