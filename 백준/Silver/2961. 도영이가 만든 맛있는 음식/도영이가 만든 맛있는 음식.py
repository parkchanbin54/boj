import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
foods = [[0]*2 for _ in range(n)]
for i in range(n):
    foods[i] = (list(map(int,input().split())))
coms = [combinations(foods,i) for i in range(1, n+1)]
ans = 1e9
for com in coms:
    for t in com:
        S, B = 1, 0
        for s, b in t:
            S *= s
            B += b
        ans = min(ans, abs(S-B))
print(ans)
