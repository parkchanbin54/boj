import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    moves = [(0,1), (0,-1),(1,1),(1,-1),(1,0),(-1,0),(-1,1),(-1,-1)]
    ans = 0
    queue = deque()

    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                queue.append((i,j))
                visited[i][j] = True
                while queue:
                    cur_x, cur_y = queue.popleft()

                    for k in range(8):
                        nx = cur_x + moves[k][0]
                        ny = cur_y + moves[k][1]
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                            if graph[nx][ny] == 1:
                                visited[nx][ny] = True
                                queue.append((nx,ny))

                ans += 1

    print(ans)