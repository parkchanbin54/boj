import heapq
import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M, K, X = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    distance = [1e9 for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int,input().split())
        graph[a].append((b,1))

    def dijkstra(start):
        pq = []
        heapq.heappush(pq,(0,start))
        distance[start] = 0

        while pq:
            dist, now = heapq.heappop(pq)

            if distance[now] < dist: continue
            for i in graph[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(pq,(cost, i[0]))

    dijkstra(X)
    flag = False
    for i in range(len(distance)):
        if distance[i] == K:
            print(i)
            flag = True
    if not flag:
        print(-1)
