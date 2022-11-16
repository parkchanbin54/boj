import sys
def big(n):
    k = n // 2
    result = ""
    for i in range(k-1):
        result += '1'
    if n % 2 == 1:
        return "7"+result
    return "1"+result

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    dp = [200000000000000 for _ in range(101)]

    dp[2] = 1
    dp[3] = 7
    dp[4] = 4
    dp[5] = 2
    dp[6] = 6
    dp[7] = 8

    for i in range(8,101):
        for k in range(2,8):
            if k == 6:
                dp[i] = min(dp[i], int(str(int(dp[i-k])) +"0"))
            else:
                dp[i] = min(dp[i], int(str(int(dp[i-k])) +str(dp[k])))

    for _ in range(n):
        t = int(input())
        print(str(dp[t])+" "+big(t))