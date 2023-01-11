import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    dx = [1,-1,0,0,-1,1]
    dy = [0,0,1,-1,0,0]

    while True:
        l, r, c = map(int,input().split())
        if l == r == c == 0:
            break

        stairs = [[] for _ in range(l)]

        for i in range(l):
            stairs[i] = [list(input().rstrip()) for _ in range(r+1)]

        for i in range(l):
            for j in range(r):
                for k in range(c):
                    if stairs[i][j][k] == 'S':
                        start_s = i
                        start_x = j
                        start_y = k

        queue = deque()

        queue.append((start_s,start_x,start_y))
        visited = [[[0] * c for _ in range(r)] for _ in range(l)]
        flag = False

        while queue:
            cur_s,cur_x,cur_y = queue.popleft()
            if stairs[cur_s][cur_x][cur_y] == 'E':
                flag = True
                print("Escaped in "+ str(visited[cur_s][cur_x][cur_y])+" minute(s).")
                break
            for i in range(6):
                if i < 4:
                    nx = cur_x + dx[i]
                    ny = cur_y + dy[i]

                    if 0 <= nx < r and 0 <= ny < c:
                        if visited[cur_s][nx][ny] == 0 and stairs[cur_s][nx][ny] != '#':
                            visited[cur_s][nx][ny] = visited[cur_s][cur_x][cur_y] + 1
                            queue.append((cur_s,nx,ny))
                else:
                    ns = cur_s + dx[i]

                    if 0 <= ns < l:
                        if visited[ns][cur_x][cur_y] == 0 and stairs[ns][cur_x][cur_y] != '#' :
                            visited[ns][cur_x][cur_y] = visited[cur_s][cur_x][cur_y] + 1
                            queue.append((ns,cur_x,cur_y))
        if not flag:
            print("Trapped!")
