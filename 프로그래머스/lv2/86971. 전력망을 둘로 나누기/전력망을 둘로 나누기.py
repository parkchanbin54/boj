from collections import deque
def solution(n, wires):
    answer = -1
    graph = [[] for _ in range(n+1)]
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    ans = 1e9
    
    for i in range(n-1):
        a,b = wires[i][0], wires[i][1]
        
        visited = [False] * (n+1)
        queue = deque()
        queue.append(a)
        visited[a] = True
        while queue:
            q = queue.popleft()
            
            for x in graph[q]:
                if x == b:
                    continue
                else:
                    if not visited[x]:
                        queue.append(x)
                        visited[x] = True
        
        cnt = visited.count(True)
        ans = min(ans, abs((n - cnt) - cnt))

    
    
    answer = ans
    return answer