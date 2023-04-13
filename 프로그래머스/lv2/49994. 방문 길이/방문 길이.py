from collections import deque

dir = {
    'U' : [-1,0],
    'D' : [1,0],
    'R' : [0,1],
    'L' : [0,-1],
}

way = {
    'U' : 0,
    'D' : 3,
    'R' : 2,
    'L' : 1,
}

def check(dirs):
    visited = [[[0,0,0,0] for _ in range(11)] for _ in range(11)]
    
    cnt = 0 
    
    queue = deque()
    queue.append((5,5))
    
    
    for i in range(len(dirs)):
        cur_x,cur_y = queue.popleft()
        
        nx = cur_x + dir[dirs[i]][0]
        ny = cur_y + dir[dirs[i]][1]
        
        if 0 <= nx < 11 and 0<= ny < 11:
            queue.append((nx,ny))
            if visited[nx][ny][way[dirs[i]]] == 0:
                visited[nx][ny][way[dirs[i]]] = 1
                visited[cur_x][cur_y][3-way[dirs[i]]] = 1
                cnt += 1
        else:
            queue.append((cur_x,cur_y))
                
    return cnt


def solution(dirs):
    answer = check(dirs)
    return answer