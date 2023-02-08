import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, d = map(int,input().split())

    li = [list(map(int,input().split())) for _ in range(n)]

    dp = [i for i in range(d + 1)]

    for i in range(d):
        if dp[i] + 1 < dp[i+1]:
            dp[i+1] = dp[i] + 1

        for s, e, c in li:
            if e <= d:
                if dp[e] > dp[s] + c:
                    dp[e] = dp[s] + c
    print(dp[d])