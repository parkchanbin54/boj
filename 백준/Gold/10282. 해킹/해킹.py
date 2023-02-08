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
                heapq.heappush(pq,(nd,nx))

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())

    for _ in range(N):
        n,D,c = map(int,input().split())

        graph = [[] for _ in range(n+1)]

        visited = [(1e7+1) for _ in range(n+1)]

        for _ in range(D):
            a,b,s = map(int,input().split())
            graph[b].append((s,a))

        dijkstra(c)
        ans_num = 0
        ans_time = 0
        for v in visited:
            if v != 1e7+1:
                ans_num += 1
                if v > ans_time:
                    ans_time = v

        print(str(ans_num)+" " +str(ans_time))