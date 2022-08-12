import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0] * m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int,input().split()))

visited = [[0] * m for _ in range(n)]

result = 0

big = 0

queue = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(queue):
    tmp = 0
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            rx = cur_x + dx[i]
            ry = cur_y + dy[i]

            if 0 <= rx < n and 0 <= ry < m:
                if visited[rx][ry] == 0 and graph[rx][ry] == 1:
                    visited[rx][ry] = 1
                    queue.append((rx,ry))
                    tmp +=1
    return tmp




for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            queue.append((i,j))
            tmp = bfs(queue)
            if tmp == 0:
                tmp = 1
            if tmp > big:
                big = tmp
            result +=1

print(result)
print(big)

