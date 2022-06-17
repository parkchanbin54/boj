n,m,v = map(int,input().split())
graph = [[] * n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (n+1)
def dfs(v):
    print(v,end=' ')
    global visited, graph
    visited[v] = 1
    for i in sorted(graph[v]):
        if visited[i]!=1:
            dfs(i)
dfs(v)
print()
from collections import deque
visited = [0] * (n+1)
def bfs(start):
    global visited, graph
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in sorted(graph[v]):
            if visited[i]!=1:
                queue.append(i)
                visited[i] = 1
bfs(v)