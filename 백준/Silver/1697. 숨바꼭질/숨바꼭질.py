import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())

    queue = deque()

    queue.append((n,0))
    visited = [False] * 100001
    while queue:
        cur, d  = queue.popleft()

        if cur == m:
            print(d)
            break

        for i in [cur-1, cur+1, cur*2]:
            if 0 <= i < 100001:
                if visited[i]:
                    continue
                queue.append((i, d+1))
                visited[i] = True

