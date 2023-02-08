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
                result[nx] = x
                visited[nx] = nd
                heapq.heappush(pq,(nd,nx))



if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int,input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))


    for i in range(1,n+1):
        visited = [(1e7 + 1) for _ in range(n + 1)]
        result = [0 for _ in range(n+1)]
        dijkstra(i)

        for t in range(1,n+1):
            if result[t] == i:
                result[t] = t
            else:
                while True:
                    if result[result[t]] == result[t]:
                        break
                    if result[result[t]] == i:
                        result[t] = result[t]
                        break
                    else:
                        result[t] = result[result[t]]
        result = list(map(str,result[1:]))

        for k in range(len(result)):
            if result[k] == "0":
                result[k] = "-"


        print(' '.join(result))
