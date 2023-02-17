import sys

if __name__ == '__main__':
    input = sys.stdin.readline


    n = int(input())

    graph = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        tmp = list(map(int, input().split()))
        a, b = tmp[0], tmp[1]
        c = []
        if b != 0:
            c = tmp[2:]

        graph[i].append([a,b,c])

    ans = 0

    for i in range(1,n+1):
        a, b, c = graph[i][0][0], graph[i][0][1], graph[i][0][2]

        if c == 0:
            continue

        max = 0
        for k in c:
            if max < graph[k][0][0]:
                max = graph[k][0][0]

        graph[i][0][0] = graph[i][0][0] + max
        if ans < graph[i][0][0]:
            ans = graph[i][0][0]


    print(ans)