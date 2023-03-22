import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    dp = [0] * (1001)
    dp[1] = 1
    dp[3] = 1

    for i in range(5,n+1):
        if max(dp[i-1], dp[i-3]) == 0:
            dp[i] = 1

    if dp[n] == 0:
        print("SK")
    else:
        print("CY")
