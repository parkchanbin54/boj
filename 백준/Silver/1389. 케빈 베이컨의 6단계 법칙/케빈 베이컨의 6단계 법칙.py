import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

result = [[] for _ in range(n+1)]

total = []
for i in range(m):
    a,b = map(int,input().split())
    result[a].append(b)
    result[b].append(a)

def dfs(graph,start):
    num = [0] * (n+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)

    return sum(num)

for i in range(1, n+1):
    total.append(dfs(result,i))

print(total.index(min(total))+1)




