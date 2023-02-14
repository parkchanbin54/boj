import sys
if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    t = []
    b = []
    for _ in range(n):
        ti, be = map(int,input().split())
        t.append(ti)
        b.append(be)
    m = 0

    dp = [0 for _ in range(n+1)]
    for i in range(n):
        m = max(m, dp[i])
        if i + t[i] <= n:
            dp[i+t[i]] = max(dp[i+t[i]] , b[i] + m)

    print(max(dp))