import heapq
import sys

def dijkstra(x):
    pq = []
    heapq.heappush(pq,(0,x))
    visited[x] = 0

    while pq:
        d, x = heapq.heappop(pq)

        if visited[x] < d:
            continue

        for nw, nx in graph[x]:
            nd = d + nw

            if visited[nx] > nd:
                visited[nx] = nd
                heapq.heappush(pq, (nd, nx))




if __name__ == '__main__':
    input = sys.stdin.readline
    V, E = map(int,input().split())

    K = int(input())

    graph = [[] for _ in range(V+1)]

    visited = [1e9] * (V + 1)

    for _ in range(E):
        a, b, c = map(int,input().split())
        graph[a].append((c,b))


    dijkstra(K)

    for i in range(1,V+1):
        print("INF" if visited[i]==1e9 else(visited[i]))
