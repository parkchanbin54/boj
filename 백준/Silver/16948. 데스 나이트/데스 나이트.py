import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    moves = [(-2,-1), (-2,1), (0,-2), (0,2), (2,-1), (2,1)]

    N = int(input())

    target = list(map(int,input().split()))

    if target[0] == target[2] and target[1] == target[3]:
        print(0)
        
    queue = deque()

    visited = [[0] * N for _ in range(N)]

    queue.append((target[0], target[1]))


    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(6):
            nx = cur_x + moves[i][0]
            ny = cur_y + moves[i][1]

            if 0 <= nx < N and  0 <= ny < N:
                if visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[cur_x][cur_y] + 1
    
    if visited[target[2]][target[3]] == 0:
        print(-1)
    else: 
        print(visited[target[2]][target[3]])
