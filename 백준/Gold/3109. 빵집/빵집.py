import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int,input().split())

    graph = [list(input().rstrip()) for _ in range(n)]
    cnt = 0
    direction = [(-1,-1), (-1,0), (-1,1)]

    def dfs(x,y):
        global cnt
        if x == 0:
            cnt += 1
            return True

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if  0 <= nx and 0 <= ny and ny < n and graph[ny][nx] == '.':
                graph[ny][nx] = 'x'
                if dfs(nx,ny):
                    return True
        return False

    for y in range(n):
        dfs(m-1,y)

    print(cnt)

