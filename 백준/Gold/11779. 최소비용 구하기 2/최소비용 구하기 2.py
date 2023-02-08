import sys
import copy
import heapq

def dijkstra(x):
    pq = []
    heapq.heappush(pq,(0,x))
    visited[x] = 0

    while pq:
        d, x = heapq.heappop(pq)

        if visited[x] < d :
            continue

        for nw, nx in graph[x]:
            nd = nw + d
            if visited[nx] > nd:
                visited[nx] = nd
                result[nx] = x
                heapq.heappush(pq,(nd, nx))


if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input().rstrip())
    m = int(input().rstrip())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b,c = map(int,input().split())

        graph[a].append((c,b))


    start, end = map(int,input().split())

    visited = [(1e10 + 1) for _ in range(n + 1)]
    result = [0 for _ in range(n+1)]
    dijkstra(start)
    ans = []
    t = copy.deepcopy(end)

    while True:
        if result[t] == start:
            break
        ans.append(result[t])
        t = result[t]

    ans.reverse()
    ans = list(map(str,ans))
    
    print(visited[end])
    print(len(ans)+2)
    print(str(start)+" "+ ' '.join(ans)+" "+str(end))

