import sys
input = sys.stdin.readline
N = int(input())
graph = [[0]*N for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))
result_minus = 0
result_plus = 0
result_zero = 0

def result(x,y,n):
    global result_minus, result_zero, result_plus
    num = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j]!= num:
                for k in range(3):
                    for l in range(3):
                        result(x+k*n//3, y+l*n//3, n//3)
                return
    if num == -1:
        result_minus += 1
    elif num == 0:
        result_zero += 1
    else:
        result_plus += 1

result(0,0,N)
print(f'{result_minus}\n{result_zero}\n{result_plus}')