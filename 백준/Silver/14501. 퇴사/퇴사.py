import sys
input = sys.stdin.readline

n = int(input())
a = []
b = []
dp = []
for _ in range(n):
    t, k = map(int, input().rstrip().split())
    a.append(t)
    b.append(k)
    dp.append(k)
dp.append(0)
for i in range(n-1,-1,-1):
    if (a[i] + i) > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], b[i] + dp[i + a[i]])


print(max(dp))