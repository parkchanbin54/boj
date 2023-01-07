import sys
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]

    ans = []

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append((b,0))
        graph[b].append((a,0))

    def dijkstra():
        pq = []
        heapq.heappush(pq,(0,1))

        while pq:
            dis, cur = heapq.heappop(pq)
            if dis >= 2:
                continue
            for c in graph[cur]:
                ans.append(c[0])
                heapq.heappush(pq,(dis + 1,c[0]))

    dijkstra()
    if len(ans) == 0:
        print(0)
    else:
        print(len(set(ans))-1)