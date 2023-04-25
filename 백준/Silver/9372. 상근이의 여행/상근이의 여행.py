import sys
from collections import deque 

def bfs(x):
    queue = deque([x])

    visited[x] = 1
    cnt = 0

    while queue:
        queue.popleft()

        for i in range(1, n + 1):
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    graph = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1

    visited = [0] * (n + 1)

    print(bfs(1))