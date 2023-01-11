import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int,input().split()))    

    dp = [[0]* 21 for _ in range(n)]

    dp[0][nums[0]] = 1

    for i in range(1,n-1):
        for j in range(21):
            if dp[i-1][j] != 0:
                if  0 <= j + nums[i] <= 20: dp[i][nums[i]+j] += dp[i-1][j]
                if  0 <= j - nums[i] <= 20: dp[i][j-nums[i]] += dp[i-1][j]

    print(dp[n-2][nums[n-1]])
