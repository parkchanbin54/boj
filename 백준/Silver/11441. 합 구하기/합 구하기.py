import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    nums = list(map(int,input().split()))

    m = int(input())
    dp = [0 for _ in range(n+1)]
    dp[1] = nums[0]
    for i in range(2, n+1):
        dp[i] = dp[i-1] + nums[i-1]

    for k in range(m):
        a, b = map(int,input().split())
        print(dp[b]-dp[a-1])