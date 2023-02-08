import sys
import heapq

def dijkstra(x):
    pq = []
    heapq.heappush(pq,(0,x))
    visited[x][0] = 0
    while pq:
        d, x = heapq.heappop(pq)
        

        for nw, nx in graph[x]:
            nd = nw + d
            if nd < visited[nx][k-1]:
                visited[nx][k-1] = nd
                visited[nx].sort()
                heapq.heappush(pq,(nd,nx))


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m, k = map(int,input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((c,b))

    visited = [[1e10] * k for _ in range(n+1)]

    dijkstra(1)

    for i in range(1, n+1):
        if visited[i][k-1] == 1e10:
            print(-1)
        else:
            print(visited[i][k-1])




