import sys
input = sys.stdin.readline
n = int(input())
dp = [0 for _ in range(100)]
dp[0]=1
dp[1]=1
dp[2]=1
dp[3]=2
for _ in range(n):
    k = int(input())
    if k > 4:
        for i in range(4, k):
            dp[i] = dp[i-3]+dp[i-2]
    print(dp[k-1])
