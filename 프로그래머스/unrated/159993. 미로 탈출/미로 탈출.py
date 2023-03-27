from collections import deque

graph = []
def bfs(start,end,n,m):
    queue = deque()
    queue.append(start)
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[0] * m for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            while 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] != 'X':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
                if nx == end[0] and ny == end[1]:
                    break
    
    return visited[end[0]][end[1]]
            

def solution(maps):
    answer = 0
    global graph
    graph = [list(m) for m in maps]
    
    start = []
    end = []
    labber = []
    
    n = len(maps)
    m = len(maps[0])

    for i in range(n):
        for j in range(m):
            if graph[i][j] == "S":
                start = [i,j]
            elif graph[i][j] == "E":
                end = [i,j]
            elif graph[i][j] == "L":
                labber = [i,j]
    
    r1 = bfs(start,labber,n,m)
    r2 = bfs(labber,end,n,m)
    
    answer = r1 + r2 if r1 != 0 and r2 != 0 else -1
    return answer