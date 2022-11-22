import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = map(int,input().split())

    coins = [int(input()) for _ in range(n)]

    dp = [1e9] * (k+1)
    for coin in coins:
        if coin < k:
            dp[coin] = 1

    for i in range(1,k+1):
        for coin in coins:
            if i-coin > 0:
                dp[i] = min(dp[i], dp[i-coin] + dp[coin])
    
    if dp[k] == 1e9:
        print(-1)
    else:
        print(dp[k])
