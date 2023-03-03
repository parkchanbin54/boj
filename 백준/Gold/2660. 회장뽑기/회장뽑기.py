import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    graph = [[1e9] * n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0

    while True:
        a,b = map(int, input().split())
        if a == -1 and b == -1:
            break
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] != 0 and graph[k][j] != 0:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


    ans = []
    for i in range(n):
        ans.append(max(graph[i]))

    can = min(ans)

    count = 0
    result = []
    for a in enumerate(ans):
        if a[1] == can:
            result.append(a[0]+1)
            count += 1

    print(str(can)+' '+str(count))
    print(' '.join(map(str,result)))