from collections import deque

def solution(x, y, n):
    answer = -1

    visited = [False] * (y+1)
    queue = deque()
    queue.append((x,0))
    
    while queue:
        x, w = queue.popleft()
        
        if x == y:
            answer = w
            break
        
        if x > y:
            continue
        
        if x*3 <= y and not visited[x*3]:
            queue.append((x*3, w+1))
            visited[x*3] = True
        if x*2 <= y and not visited[x*2]:
            queue.append((x*2, w+1))
            visited[x*2] = True
        if x+n <= y and not visited[x+n]:
            queue.append((x+n, w+1))
            visited[x+n] = True
        
        

    return answer