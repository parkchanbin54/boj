import sys
from collections import deque
import copy
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = [list(map(int,input().split())) for _ in range(n)]

best = 0
def makewall(count):
    if count == 3:
        dfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    makewall(count + 1)
                    graph[i][j] = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs():
    graph2 = copy.deepcopy(graph)
    global best
    for i in range(n):
        for j in range(m):
            if graph2[i][j] == 2:
                queue = deque()
                queue.append((i,j))
                while queue:
                    cur_x, cur_y = queue.popleft()
                    for k in range(4):
                        nx = cur_x + dx[k]
                        ny = cur_y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if graph2[nx][ny] == 0:
                                graph2[nx][ny] = 2
                                queue.append((nx,ny))
    result = 0
    for i in range(n):
        result += graph2[i].count(0)
    best = max(result, best)
makewall(0)
print(best)