import sys
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())

    graph = [[] for _ in range(n+1)]
    degree = [0 for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        degree[b] += 1
    queue = []

    for i in range(1,n+1):
        if degree[i] == 0:
            heapq.heappush(queue,i)

    ans = []

    while queue:
        tmp = heapq.heappop(queue)
        ans.append(tmp)

        for i in graph[tmp]:
            degree[i] -= 1
            if degree[i] == 0:
                heapq.heappush(queue,i)

    print(' '.join(map(str,ans)))