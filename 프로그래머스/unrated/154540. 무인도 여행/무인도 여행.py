from collections import deque, defaultdict
def solution(maps):
    answer = [-1]
    
    graph = [list(m) for m in maps]
    
    
    n = len(maps)
    m = len(maps[0])
    ans = defaultdict(int)

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt = 0
    
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 'X':
                queue = deque()
                cnt += 1
                queue.append((i,j))
                ans[cnt] += int(graph[i][j])
                graph[i][j] = 'X'
                while queue:
                    x,y = queue.popleft()
                    
                    for k in range(4):
                        nx = dx[k] + x 
                        ny = dy[k] + y
                        
                        if 0 <= nx < n and 0 <= ny < m:
                            if graph[nx][ny] != 'X':
                                ans[cnt] += int(graph[nx][ny])
                                graph[nx][ny] = 'X'
                                queue.append((nx,ny))
    
    if len(ans) != 0:
        answer = list(ans.values())
        answer.sort()
            
            
    return answer