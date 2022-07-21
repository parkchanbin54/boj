import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))
dp = [1] * n
for i in range(1, n):
    s = []
    for j in range(i):
        if array[i] < array[j]:
            s.append(dp[j])
    if not s:
        continue
    else:
        dp[i] += max(s)
print(max(dp))