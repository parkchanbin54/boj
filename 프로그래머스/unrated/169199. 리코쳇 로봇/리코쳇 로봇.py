from collections import deque





def solution(board):
    global ans
    answer = -1
    visited = [[0] * len(board[0]) for _ in range(len(board))]
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                x ,y = i, j
                break
                
    queue = deque()
    visited[x][y] = 1
    queue.append((x,y))
    ans = []
    while queue:
        x,y = queue.popleft()
        if board[x][y] == 'G':
            answer = visited[x][y]
            break
        for i in range(4):
            nx = x
            ny = y
            
            while True:
                nx += dx[i]
                ny += dy[i]
                if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
                    nx -= dx[i]
                    ny -= dy[i]
                    break

                if board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
    if answer > 0:
        answer -= 1
    return answer