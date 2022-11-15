import sys
input = sys.stdin.readline
n, m = map(int,input().split())

graph = list(input().rstrip() for _ in range(n))
result = 0
test = list(input().rstrip() for _ in range(m))

for i in range(m):
    graph.append(test[i])
    if len(set(graph)) != len(graph):
        result += 1
    del graph[n]
print(result)
