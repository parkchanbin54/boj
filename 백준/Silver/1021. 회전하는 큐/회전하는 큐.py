import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

solve = list(map(int,input().split()))

queue = deque()

for i in range(1, n+1):
    queue.append(i)

result = 0
for sol in solve:
    while True:
        if queue[0] == sol:
            queue.popleft()
            break
        if queue.index(sol) <= len(queue)/2:
            while queue[0] != sol:
                queue.append(queue.popleft())
                result +=1
        else:
            while queue[0] != sol:
                queue.appendleft(queue.pop())
                result += 1

print(result)