import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    price = [0] + list(map(int,input().split()))

    dp = [False for _ in range(n+1)]

    for i in range(1, n+1):
        for k in range(1, i+1):
            if dp[i] == False:
                dp[i] = dp[i-k] + price[k]
            else:
                dp[i] = min(dp[i], dp[i-k] + price[k])

    print(dp[n])