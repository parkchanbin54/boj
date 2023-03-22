import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    nums = list(map(int,input().split()))
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1
    for i in range(1,n):
        for j in range(i+1):
            if i == j:
                dp[j][i] = 1
            elif nums[i] == nums[j]:
                if j+1 == i: dp[j][i] = 1
                elif dp[j+1][i-1] == 1:
                    dp[j][i] = 1

    t = int(input())

    for _ in range(t):
        a,b = map(int,input().split())
        print(dp[a-1][b-1])
