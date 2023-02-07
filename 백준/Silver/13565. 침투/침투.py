import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    m, n = map(int, input().split())

    graph = [list(map(int,input().rstrip())) for _ in range(m)]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    queue = deque()

    start = []

    for i in range(len(graph[0])):
        if graph[0][i] == 0:
            start.append(i)

    flag = False
    visited = [[False] * n for _ in range(m)]
    for s in start:

        visited[0][s] = True
        queue.append((0,s))

        while queue:
            cur_x, cur_y = queue.popleft()

            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if 0 <= nx < m and 0 <= ny < n:
                    if not visited[nx][ny]:
                        if graph[nx][ny] == 0:
                            visited[nx][ny] = True
                            if nx == m-1:
                                flag= True
                                break
                            queue.append((nx,ny))
        if flag:
            break

    if flag:
        print("YES")
    else:
        print("NO")




