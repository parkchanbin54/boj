import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())
    start_x, start_y = 0,0
    des_x, des_y = 0,0
    graph = []
    water = []

    des = [[0] * m for _ in range(n)]
    for i in range(n):
        tmp = list(input())
        graph.append(tmp)
        for t in tmp:
            if t == 'S':
                start_x = i
                start_y = tmp.index(t)
            elif t == '*':
                water.append((i,tmp.index(t)))
            elif t == 'D':
                des_x,des_y = i, tmp.index(t)

    queue = deque()

    queue.append((start_x,start_y))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for w in water:
        queue.append(w)

    while queue:
        cur_x, cur_y= queue.popleft()
        if graph[des_x][des_y] == 'S':
            print(des[des_x][des_y])
            break
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[cur_x][cur_y] == 'S':
                    graph[nx][ny] = 'S'
                    queue.append((nx,ny))
                    des[nx][ny] = des[cur_x][cur_y] + 1
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[cur_x][cur_y] == '*':
                    graph[nx][ny] = '*'
                    queue.append((nx,ny))
    else:
        print("KAKTUS")