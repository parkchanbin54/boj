import sys
if __name__ == '__main__':
    input = sys.stdin.readline

    arr =[0] + list(input().rstrip())
    l = len(arr)

    if arr[1] == '0':
        print(0)
    else:
        dp = [0] * l

        dp[0],dp[1] = 1,1

        for i in range(2,l):
            f = int(arr[i])
            t = int(arr[i-1]+arr[i])
            if f > 0: dp[i] += dp[i-1]
            if 10 <= t <= 26: dp[i] += dp[i-2]

        print(dp[-1]%1000000)



