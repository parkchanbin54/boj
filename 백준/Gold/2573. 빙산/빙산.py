import copy
import sys
from collections import deque
def bfs():
    queue = deque()
    visited = [[False] * (m) for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                queue.append((i,j))
                visited[i][j] = True
                while queue:
                    cur_x, cur_y = queue.popleft()
                    for k in range(4):
                        nx = dx[k] + cur_x
                        ny = dy[k] + cur_y

                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny]:
                                if graph[nx][ny] > 0:
                                    visited[nx][ny] = True
                                    queue.append((nx,ny))
                flag = True
                break
        if flag:
            break

    if not flag:
        return -1

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                return 1




if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int,input().split())

    graph = [list(map(int,input().split())) for _ in range(n)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    count = 0

    while True:
        r = bfs()
        if r == 1:
            print(count)
            break
        elif r == -1:
            print(0)
            break
        tmp = copy.deepcopy(graph)
        for i in range(n):
            for j in range(m):
                if graph[i][j] > 0:
                    for k in range(4):
                        cnt = 0
                        if 0 <= i+dx[k] < n and 0 <= j + dy[k] < m:
                            if tmp[i+dx[k]][j+dy[k]] <= 0:
                                cnt += 1
                        graph[i][j] -= cnt

        count += 1