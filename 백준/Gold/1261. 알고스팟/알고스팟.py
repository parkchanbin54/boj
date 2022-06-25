from collections import deque


m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                elif graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return visited[n - 1][m - 1]


print(bfs(0, 0))