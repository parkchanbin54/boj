import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    a = [0] + list(input().rstrip())
    b = [0] + list(input().rstrip())
    graph = [[0] * len(b) for _ in range(len(a))]

    for i in range(1,len(a)):
        for j in range(1,len(b)):
            if a[i] == b[j]:
                graph[i][j] = graph[i-1][j-1] + 1
            else:
                graph[i][j] = max(graph[i-1][j], graph[i][j-1])

    print(graph[-1][-1])

