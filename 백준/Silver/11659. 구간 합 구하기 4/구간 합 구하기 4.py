import sys

input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
pre_sum = [0]
temp = 0
for i in num:
    temp += i
    pre_sum.append(temp)
for _ in range(m):
    i, j = map(int, input().split())
    print(pre_sum[j]-pre_sum[i-1])
