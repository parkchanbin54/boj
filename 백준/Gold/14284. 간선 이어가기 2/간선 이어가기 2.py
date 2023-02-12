import sys
import heapq

def dijkstra(x):
    visited = [(1e7+1) for _ in range(n+1)]

    pq = []
    heapq.heappush(pq,(0,x))
    visited[x] = 0

    while pq:
        d,x = heapq.heappop(pq)

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
    n, m = map(int,input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))

    s,t = map(int,input().split())

    print(dijkstra(s)[t])

