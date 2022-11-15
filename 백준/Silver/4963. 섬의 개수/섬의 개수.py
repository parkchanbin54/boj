import sys
from collections import deque

def dfs(graph):
    dx = [1, -1, 0, 0,1,1,-1,-1]
    dy = [0, 0, 1, -1,-1,1,1,-1]

    n, m= len(graph),len(graph[0])
    result = 0
    visited = [[0] * m for _ in range(n)]
    queue = deque()


    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] != 1:
                visited[i][j] = 1
                queue.append((i,j))
                result += 1
                while queue:
                    cur_x, cur_y = queue.popleft()
                    for k in range(8):
                        nx = cur_x + dx[k]
                        ny = cur_y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                                visited[nx][ny] = 1
                                queue.append((nx,ny))

    return result

if __name__ == '__main__':
    input = sys.stdin.readline
    while True:
        n, m = map(int,input().split())
        if m == 0 and n == 0 :
            break
        graph = [list(map(int,input().split())) for _ in range(m)]
        print(dfs(graph))

