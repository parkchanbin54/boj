import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

array = list(map(int,input().split()))

result = 0

for i in range(1, n+1):
    if i == 1:
        for arr in array:
            if arr == m:
                result += 1
    else:
        tmp = list(combinations(array, i))
        for t in tmp:
            if sum(t) == m:
                result += 1

print(result)