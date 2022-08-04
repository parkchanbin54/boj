import sys
input = sys.stdin.readline
d, k = map(int, input().split())

dp = [ 0 for _ in range(d+1)]

dp[0] = 1
dp[1] = 1

for i in range(2,d+1):
    dp[i] = dp[i-2] + dp[i-1]

for i in range(1, k//d):
    if (k - (dp[d-3] * i)) > 0 and ((k - (dp[d-3] * i))) % dp[d-2] == 0:
        print(i)
        print((k - dp[d-3] * i) / dp[d-2])
        break