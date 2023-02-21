import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    degree = [0 for _ in range(n+1)]
    for _ in range(m):
        tmp = list(map(int,input().split()))

        for i in range(1,tmp[0]):
            graph[tmp[i]].append(tmp[i+1])
            degree[tmp[i+1]] += 1

    queue = deque()

    for i in range(1,n+1):
        if degree[i] == 0:
            queue.append(i)

    ans = []
    while queue:
        tmp = queue.popleft()
        ans.append(tmp)

        for k in graph[tmp]:
            degree[k] -= 1
            if degree[k] == 0:
                queue.append(k)
    if len(ans) != n:
        print(0)
    else:
        for a in ans:
            print(a)
