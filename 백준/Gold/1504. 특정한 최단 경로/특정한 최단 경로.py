import sys
import heapq

def dijkstra(x):
    pq = []
    heapq.heappush(pq,(0,x))
    visited = [1e9 for _ in range(n + 1)]
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

    n, e = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        a, b, c = map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))

    v1, v2 = map(int,input().split())
    flag = True

    start = dijkstra(1)
    v1_ = dijkstra(v1)
    v2_ = dijkstra(v2)
    ans = min(start[v1] + v1_[v2] + v2_[n], start[v2] + v2_[v1] + v1_[n])

    if ans < 1e9:
        print(ans)
    else:
        print(-1)
