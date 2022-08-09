import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())


queue = deque()
queue.append((n))
visited = [[-1, 0] for _ in range(100001)]

visited[n][0] = 0
visited[n][1] = 1

while queue:
    x = queue.popleft()

    for i in [x-1, x+1, x*2]:
        if 0 <= i <= 100000:
            if visited[i][0] == -1:
                visited[i][0] = visited[x][0] + 1
                visited[i][1] = visited[x][1]
                queue.append(i)
            elif visited[i][0] == visited[x][0] + 1:
                visited[i][1] += visited[x][1]

print(visited[m][0])
print(visited[m][1])