m, n = map(int,input().split())
grid = [[0 for _ in range(n)] for _ in range(m)]
direct = {0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]}

end = m*n-2
cnt = 0
head = 0
i,j = 0,0
grid[i][j] = "X"
while end>=0:
    condi = False
    if 0<=i+direct[head][0]<m and 0<=j+direct[head][1]<n:
        if grid[i+direct[head][0]][j+direct[head][1]] != "X":
            grid[i+direct[head][0]][j+direct[head][1]] = "X"
            i,j = i+direct[head][0],j+direct[head][1]
            condi = True
    if not condi:
        cnt += 1
        head = (head+1)%4
        i,j = i+direct[head][0],j+direct[head][1]
        grid[i][j] = "X"
    end -= 1
print(cnt)