import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    f,s,g,u,d = map(int,input().split())

    ans = []
    queue = deque()
    queue.append((s,0))
    flag = False

    visited = [False] * (f + 1)
    while queue:
        cur, cnt = queue.popleft()
        if visited[cur]:
            continue
        visited[cur] = True

        if cur == g:
            print(cnt)
            flag = True
            break

        if cur + u <= f:
                queue.append((cur + u,cnt+1))
        if cur - d > 0:
                queue.append((cur - d,cnt+1))

    if not flag:
        print("use the stairs")