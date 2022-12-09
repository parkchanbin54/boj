import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().split())
    ladder = dict()
    snake = dict()
    for _ in range(n):
        i, j = map(int,input().split())
        ladder[i] = j
    for _ in range(m):
        i, j = map(int,input().split())
        snake[i] = j

    queue = deque()
    queue.append(1)

    visited = [False] * 101

    result = [0] * 101

    while queue:
        cur = queue.popleft()
        for m in range(1,7):
            ncur = cur + m
            if 0 < ncur <= 100 and not visited[ncur]:

                if ncur in ladder.keys():
                    ncur = ladder[ncur]

                if ncur in snake.keys():
                    ncur = snake[ncur]

                if not visited[ncur]:
                    queue.append(ncur)
                    visited[ncur] = True
                    result[ncur] = result[cur] + 1

    print(result[100])


