import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    a = [0] + list(input().rstrip())
    b = [0] + list(input().rstrip())
    c = [0] + list(input().rstrip())

    graph = [[[0] * len(c) for _ in range(len(b))] for _ in range(len(a))]

    for i in range(1,len(a)):
        for j in range(1,len(b)):
            for k in range(1,len(c)):
                if a[i] == b[j] and b[j] == c[k]:
                    graph[i][j][k] = graph[i-1][j-1][k-1] + 1
                else:
                    graph[i][j][k] = max(graph[i-1][j][k], graph[i][j-1][k], graph[i][j][k-1])

    ans = -1

    for i in range(len(a)):
        for j in range(len(b)):
            ans = max(max(graph[i][j]), ans)

    print(ans)


