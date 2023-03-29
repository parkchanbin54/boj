import heapq

def dijkstra(x,visited,graph):
    visited[x][1] = 0
    pq = []
    heapq.heappush(pq,(0,x))
    
    while pq:
        d,x = heapq.heappop(pq)
        
        if visited[x][1] < d:
            continue
        
        for w,nx in graph[x]:
            nd = w + d
            if visited[nx][1] > nd:
                visited[nx][1] = nd
                heapq.heappush(pq,(nd,nx))

def solution(n, edge):
    answer = 1
    
    graph = [[] for _ in range(n+1)]
    
    for a,b in edge:
        graph[a].append((1,b))
        graph[b].append((1,a))
    
    visited = [[i,1e9] for i in range(n+1)]
    
    dijkstra(1,visited,graph)
    visited = visited[1:]
    visited.sort(key =lambda x : -x[1])
    prev = visited[0][1]
    
    for i in range(1,n):
        if visited[i][1] != prev:
            break
        answer += 1
    
    
    return answer