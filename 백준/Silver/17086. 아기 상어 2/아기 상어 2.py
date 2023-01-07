import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int,input().rstrip().split())
    graph = [list(map(int,input().split())) for _ in range(n)]

    def bfs(queue):
        depth = [[-1] * m for _ in range(n)]
        while queue:
            cur_x, cur_y = queue.popleft()

            for k in range(8):
                nx = cur_x + dx[k]
                ny = cur_y + dy[k]

                if 0 <= nx < n and 0 <= ny < m:
                    if depth[nx][ny] != -1:
                        continue
                    if graph[nx][ny] == 1:
                        return depth[cur_x][cur_y] + 1
                    depth[nx][ny] = depth[cur_x][cur_y] + 1
                    queue.append((nx,ny))


    dx = [1,-1,1,-1,0,0,1,-1]
    dy = [1,1,0,0,1,-1,-1,-1]
    ans = 0
    for i in range(n):
       for j in range(m):
           queue = deque()
           if graph[i][j] != 1:
                queue.append((i,j))
                tmp = bfs(queue)
                ans = max(ans,tmp)


    print(ans+1)
