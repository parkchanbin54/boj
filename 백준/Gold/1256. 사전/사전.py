import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m, k = map(int,input().split())

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dp[i][0] = 1

    for j in range(1,m+1):
        dp[0][j] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    if k > dp[-1][-1]:
        print(-1)

    else:
        ans = ''
        while n > 0 and m > 0:
            split = dp[n-1][m]

            if  k <= split:
                n -= 1
                ans += 'a'
            else:
                m -= 1
                k -= split
                ans += 'z'
        else:
            ans += ('a' * n + 'z'* m)
        print(ans)
