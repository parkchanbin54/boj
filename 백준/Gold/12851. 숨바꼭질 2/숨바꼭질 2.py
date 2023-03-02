import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())

    visited = [[-1,0] for _ in range(100001)]

    visited[n][0] = 0
    visited[n][1] = 1

    queue = deque()
    queue.append(n)

    while queue:
        cur = queue.popleft()

        for i in [cur-1, cur+1, cur*2]:
            if 0 <= i <= 100000:
                if visited[i][0] == -1:
                    visited[i][0] = visited[cur][0] + 1
                    visited[i][1] = visited[cur][1]
                    queue.append(i)
                elif visited[i][0] == visited[cur][0] + 1:
                    visited[i][1] += visited[cur][1]

    print(visited[m][0])
    print(visited[m][1])