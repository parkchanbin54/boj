import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int,input().split())

    graph = [[] for _ in range(n+1)]
    degree = [0 for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        degree[b] += 1

    queue = deque()

    for i in range(1,n+1):
        if degree[i] == 0:
            queue.append(i)

    ans = [1 for _ in range(n+1)]
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            ans[next] = max(ans[next], ans[now] + 1)
            degree[next] -= 1
            if degree[next] == 0:
                queue.append(next)

    print(*ans[1:])