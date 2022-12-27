import heapq
import sys


def dijkstra(x):
    pq = []
    heapq.heappush(pq,(x,0))
    visited[x] = 0

    while pq:
        x, d = heapq.heappop(pq)

        if visited[x] < d:
            continue

        for nw, nx in graph[x]:
            nd = d + nw
            if visited[nx] > nd:
                visited[nx] = nd
                heapq.heappush(pq,(nx,nd))



if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    M = int(input())

    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a , b, c = map(int,input().split())
        graph[a].append((c,b))

    start, end = map(int,input().split())

    visited = [1e9] * (N+1)

    dijkstra(start)

    print(visited[end])



