from collections import deque
import sys


if __name__ == '__main__':
    input = sys.stdin.readline
    n, l, r = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    dic = dict()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    ans = 0
    queue = deque()
    while True:
        cnt = -1
        flag = False
        visited = [[-1] * n for _ in range(n)]
        tmp = [0 for _ in range(n * n)]
        for i in range(n):
            for j in range(n):
                if visited[i][j] == -1:
                    cnt += 1
                    tmp[cnt] = 1
                    visited[i][j] = cnt
                    dic[cnt] = graph[i][j]
                queue.append((i,j))

                while queue:
                    cur_x, cur_y = queue.popleft()

                    for k in range(4):
                        nx = cur_x + dx[k]
                        ny = cur_y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n:

                            if visited[nx][ny] == -1:
                                if l <= abs(graph[cur_x][cur_y] - graph[nx][ny]) <= r:
                                    flag = True
                                    visited[nx][ny] = visited[cur_x][cur_y]
                                    dic[cnt] += graph[nx][ny]
                                    tmp[cnt] += 1
                                    queue.append((nx,ny))
        for u in range(n):
            for p in range(n):
                graph[u][p] = dic[visited[u][p]]//tmp[visited[u][p]]

        ans += 1
        if not flag:
            break

    print(ans-1)



