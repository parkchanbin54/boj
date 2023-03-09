import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    s1 = [' '] + list(input().rstrip())
    s2 = [' '] + list(input().rstrip())

    graph = [[0] * len(s1) for _ in range(len(s2))]

    for i in range(1, len(s2)):
        for j in range(1, len(s1)):
            if s1[j] == s2[i]:
                graph[i][j] = graph[i-1][j-1] + 1
            else:
                graph[i][j] = 0

    ans = 0

    for g in graph:
        ans = max(max(g), ans)

    print(ans)