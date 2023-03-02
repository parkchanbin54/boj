import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())

    queue = deque()

    queue.append(n)
    visited = [-1] * 100001
    route = [-1] * 100001

    visited[n] = 0
    while queue:
        c = queue.popleft()


        if c == m:
            print(visited[c])
            break

        for i in [c-1, c+1, c*2]:
            if 0 <= i < 100001:
                if visited[i] == -1:
                    queue.append(i)
                    route[i] = c
                    visited[i] = visited[c] + 1

    result = [m]
    for i in range(visited[m]):
        result.append(route[result[-1]])

    print(' '.join(map(str,result[::-1])))