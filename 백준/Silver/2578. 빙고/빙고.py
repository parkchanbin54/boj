import sys
input = sys.stdin.readline

board = dict()
check = [[0]*5 for i in range(5)]
for i in range(5):
    a = list(map(int,input().split()))
    for j in range(5):
        board[a[j]] = (i,j)

tick = 0
for _ in range(5):
    a = list(map(int,input().split()))
    for i in range(5):
        tick += 1
        
        if a[i] in board:
            check[board[a[i]][0]][board[a[i]][1]] = 1
            
            bingo = 0
            for j in range(5):
                if sum(check[j]) == 5:
                    bingo+=1
                if sum([k[j] for k in check]) == 5:
                    bingo+=1
            if check[0][4]+check[1][3]+check[2][2]+check[3][1]+check[4][0] == 5:
                bingo+=1
            if check[0][0]+check[1][1]+check[2][2]+check[3][3]+check[4][4] == 5:
                bingo+=1
                
            if bingo >= 3:
                print(tick)
                sys.exit()