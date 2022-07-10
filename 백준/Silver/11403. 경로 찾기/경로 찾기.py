import sys
input = sys.stdin.readline
N = int(input())
ad = [list(map(int, input().split()))for _ in range(N)]

chk = [0 for _ in range(N)]

def dfs(x):
    for i in range(N):
        if ad[x][i] == 1 and chk[i] ==0:
            chk[i] = 1
            dfs(i)

for i in range(N):
    dfs(i)
    for j in range(N):
        if chk[j] == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
    chk = [0 for _ in range(N)]