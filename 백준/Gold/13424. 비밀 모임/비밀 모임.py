import sys
import heapq

def dijkstra(x):
    visited = [1e9 for _ in range(n+1)]

    pq = []
    heapq.heappush(pq,(0,x))
    visited[x] = 0

    while pq:
        d, x = heapq.heappop(pq)

        if visited[x] < d:
            continue

        for nw, nx in graph[x]:
            nd = nw + d
            if visited[nx] > nd:
                visited[nx] = nd
                heapq.heappush(pq,(nd,nx))

    return visited

if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, m = map(int,input().split())

        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            a,b,c = map(int,input().split())
            graph[a].append((c,b))
            graph[b].append((c,a))

        k = int(input())
        rooms = list(map(int,input().split()))

        ans = [1e9] * (n+1)
        mi = 1e9
        for i in range(1,n+1):
            tmp = dijkstra(i)
            ans[i] = sum(tmp[f] for f in rooms)

        print(ans.index(min(ans)))
