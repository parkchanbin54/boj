import sys
from collections import deque


if __name__ == '__main__':
    input = sys.stdin.readline
    a, b, n, m = map(int,input().split())
    moves = [1, -1, a, b, -a, -b]
    jumps = [a,b]
    visited = [False] * 100001
    queue = deque()
    queue.append((n,0))

    while queue:
        cur, ind = queue.popleft()
        if cur == m:
            print(ind)
            break
        for i in range(2):
            tmp = cur * jumps[i]
            if 0 <= tmp <= 100000 and not visited[tmp]:
                visited[tmp] = True
                queue.append((tmp, ind +1))

        for i in range(6):
            tmp = cur + moves[i]
            if 0 <= tmp <= 100000 and not visited[tmp]:
                visited[tmp] = True
                queue.append((tmp, ind + 1))

