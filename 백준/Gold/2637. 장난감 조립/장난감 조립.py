import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n+1)]
    degree = [0 for _ in range(n+1)]
    needs = [[0] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[b].append((a,c))
        degree[a] += 1

    queue = deque()

    for i in range(1,n+1):
        if degree[i] == 0:
            queue.append(i)


    while queue:
        now = queue.popleft()
        for next, next_need in graph[now]:
            if needs[now].count(0) == n+1:
                needs[next][now] += next_need
            else:
                for i in range(1,n+1):
                    needs[next][i] += needs[now][i] * next_need
            degree[next] -= 1
            if degree[next] == 0:
                queue.append(next)

    for x in enumerate(needs[n]):
        if x[1] > 0:
            print(*x)