import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())

    graph_up = [[0]* n for _ in range(n)]
    graph_down = [[0]*n for _ in range(n)]

    for _ in range(m):
        a, b = map(int,input().split())
        graph_up[a-1][b-1] = 1
        graph_down[b-1][a-1] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph_up[i][k] and graph_up[k][j]:
                    graph_up[i][j] = 1
                if graph_down[i][k] and graph_down[k][j]:
                    graph_down[i][j] = 1

    ans = 0

    for j in range(n):
        if graph_up[j].count(1) > n//2 or graph_down[j].count(1) > n//2:
            ans += 1

    print(ans)