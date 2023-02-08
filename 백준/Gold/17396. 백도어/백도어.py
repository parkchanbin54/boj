import sys
import heapq

def dijkstra(x):
    pq = []
    heapq.heappush(pq,(0,x))
    visited[x] = 0

    while pq:
        d, x = heapq.heappop(pq)

        if visited[x] < d:
            continue

        for nw, nx in graph[x]:
            nd = nw + d
            if sight[nx] == 1 and nx != n-1:
                continue
            if visited[nx] > nd:
                visited[nx] = nd
                heapq.heappush(pq,(nd,nx))

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())
    sight = list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))

    visited = [1e12 for _ in range(n+1)]


    dijkstra(0)
    if visited[n-1] == 1e12:
        print(-1)
    else:
        print(visited[n-1])
