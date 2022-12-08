import sys
if __name__ == '__main__':
    input = sys.stdin.readline

    n,m,k = map(int,input().split())

    graph = [[0]*(m+1) for _ in range(n+1)]
    graph[0][1],cnt = 1,1

    for i in range(1,n+1):
        for j in range(1, m+1):
            if cnt == k:
                px = i
                py = j
            cnt += 1
            graph[i][j] = graph[i][j-1] + graph[i-1][j]

    if k == 0:
        print(graph[n][m])
    else:
        print(graph[px][py] * graph[n-px+1][m-py+1])
