import sys
from collections import deque
def sol():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    graph = [list(input().rstrip()) for _ in range(n)]

    dx = [1,-1, 0, 0]
    dy = [0, 0, 1, -1]

    total_sheep = 0
    total_wolf = 0

    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            sheep = 0
            wolf = 0
            if visited[i][j] == 0:
                if graph[i][j] == '#':
                    visited[i][j] = 1
                    continue
                elif graph[i][j] =='v': wolf += 1
                elif graph[i][j] == 'k': sheep += 1

                visited[i][j] = 1
                queue = deque()
                queue.append((i,j))

                while queue:
                    cur_x, cur_y = queue.popleft()
                    for k in range(4):
                        nx = cur_x + dx[k]
                        ny = cur_y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                            tmp = graph[nx][ny]
                            if tmp == 'k':
                                sheep += 1
                            elif tmp == 'v':
                                wolf += 1
                            if tmp != '#':
                                queue.append((nx,ny))
                            visited[nx][ny] = 1
                if sheep > wolf:
                    total_sheep += sheep
                else:
                    total_wolf += wolf
    print(total_sheep, total_wolf)

if __name__ == '__main__':
    sol()

