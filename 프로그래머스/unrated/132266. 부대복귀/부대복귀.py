import heapq

def dijkstra(graph,n,x):
    visited = [1e9] * (n+1)
    visited[x] = 0
    pq = []
    heapq.heappush(pq,(0,x))
    
    while pq:
        d,x = heapq.heappop(pq)
        
        if visited[x] < d:
            continue
        
        for nw, nx in graph[x]:
            nd = nw + d
            if visited[nx] > nd:
                visited[nx] = nd
                heapq.heappush(pq,(nd,nx))
                
    return visited
    
def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] * (n+1) for _ in range(n+1)]
    
    for r in roads:
        graph[r[0]].append((1,r[1]))
        graph[r[1]].append((1,r[0]))
        
    vis = dijkstra(graph,n,destination)
    
    for s in sources:
        result = vis[s]
        if result == 1e9:
            answer.append(-1)
        else:
            answer.append(result)
    
    
        
    return answer