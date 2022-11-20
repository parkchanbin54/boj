import sys
from collections import deque

def check(start, end, x):
    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [1,2,2,1,-1,-2,-2,-1]
    checked = [[0] * x for _ in range(x)]
    queue = deque()
    queue.append(start)
    checked[start[0]][start[1]] = 0


    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(8):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < x and 0 <= ny < x and checked[nx][ny] == 0:
                checked[nx][ny] = checked[cur_x][cur_y] + 1
                queue.append((nx,ny))

    return checked[end[0]][end[1]]


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        x = int(input())
        start = list(map(int,input().split()))
        end = list(map(int, input().split()))
        if start == end:
            print(0)
        else : print(check(start,end,x))