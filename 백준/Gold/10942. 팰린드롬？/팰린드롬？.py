import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    nums = list(map(int,input().split()))
    dp = [[0] * n for _ in range(n)]

    m = int(input())

    for l in range(n):
        for s in range(n - l):
            e = s + l

            if s == e:
                dp[s][e] = 1
            elif nums[s] == nums[e]:
                if s + 1 == e: dp[s][e] = 1
                elif dp[s+1][e-1] == 1: dp[s][e] = 1

    for q in range(m):
        s, e = map(int,input().split())
        print(dp[s-1][e-1])

