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
            if visited[nx] > nd:
                visited[nx] = nd
                parent[nx] = x
                heapq.heappush(pq,(nd,nx))


if __name__ == '__main__':
    input = sys.stdin.readline

    N, M = map(int,input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a,b,c = map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))

    parent = [0] * (N+1)

    visited = [1e9 for _ in range(N+1)]

    dijkstra(1)


    print(N-1)
    for i in range(2, N+1):
        print(str(i)+" "+str(parent[i]))
