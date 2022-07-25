import sys

n = int(input())
jump = list(map(int, sys.stdin.readline().split()))
dp = [n + 1] * n
dp[0] = 0

for i in range(n):
	for j in range(1, jump[i] + 1):
		if i + j < n:
			dp[i + j] = min(dp[i] + 1, dp[i + j])

if dp[n - 1] == n + 1:
	print(-1)
else:
	print(dp[n - 1])