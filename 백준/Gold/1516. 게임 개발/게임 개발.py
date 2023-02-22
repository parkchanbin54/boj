import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    graph = [[] for _ in range(n+1)]
    degree = [0 for _ in range(n+1)]
    time = [0] * (n+1)
    for i in range(1,n+1):
        tmp = list(map(int,input().split()))
        time[i] = tmp[0]
        for j in range(1,len(tmp)-1):
            graph[tmp[j]].append(i)
            degree[i] += 1

    queue = deque()

    for i in range(1,n+1):
        if degree[i] == 0:
            queue.append(i)

    ans = [0] * (n+1)

    while queue:
        tmp = queue.popleft()
        ans[tmp] += time[tmp]

        for k in graph[tmp]:
            degree[k] -= 1
            ans[k] = max(ans[k], ans[tmp])
            if degree[k] == 0:
                queue.append(k)

    for a in ans[1:]:
        print(a)