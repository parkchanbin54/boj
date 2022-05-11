import sys


n = int(sys.stdin.readline())
dp = [0] * (n + 1)
dp[0] = 1

two = [2 ** k for k in range(21)] # 2^k
for i in two:
    if i <= n:
        for j in range(i, n + 1):
            dp[j] += (dp[j - i]) % 1000000000

print(dp[n] % 1000000000)