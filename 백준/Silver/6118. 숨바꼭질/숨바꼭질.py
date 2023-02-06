import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())
    roads = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int,input().split())
        roads[a].append(b)
        roads[b].append(a)

    queue = deque()
    graph = [0 for _ in range(n+1)]
    graph[1] = -1
    queue.append((1,0))

    while queue:
        x, y = queue.popleft()

        for r in roads[x]:
            if graph[r] == 0:
                graph[r] = y+1
                queue.append((r,y+1))

    length = max(graph)
    quan = 0
    ans = 0
    for i in range(len(graph)):
        if graph[i] == length:
            if quan == 0:
                ans = i
            quan += 1

    print(str(ans)+" "+str(length)+" "+str(quan))