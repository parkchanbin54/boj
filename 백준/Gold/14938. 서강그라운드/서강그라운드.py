import sys
input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())
item = list(map(int,input().rstrip().split()))

inf = 1e9
graph = [[inf]*n for _ in range(n)]

for _ in range(r):
    a, b, c = map(int, input().rstrip().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

high=0
for i in range(n):
    temp = 0
    for j in range(n):
        if graph[i][j] <= m:
            temp += item[j]
    if high < temp:
        high = temp

print(high)