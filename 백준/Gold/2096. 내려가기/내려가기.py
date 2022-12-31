import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    max_dp = [0] * 3
    min_dp = [0] * 3

    max_tmp = [0] * 3
    min_tmp = [0] * 3

    for i in range(n):

        a,b,c = map(int,input().split())
        for j in range(3):
            if j == 0:
                min_tmp[j] = a + min(min_dp[j], min_dp[j+1])
                max_tmp[j] = a+ max(max_dp[j], max_dp[j+1])
            elif j == 1:
                min_tmp[j] = b + min(min_dp[j-1], min_dp[j], min_dp[j+1])
                max_tmp[j] = b + max(max_dp[j-1], max_dp[j], max_dp[j+1])
            elif j == 2:
                min_tmp[j] = c + min(min_dp[j], min_dp[j-1])
                max_tmp[j] = c + max(max_dp[j], max_dp[j-1])
        for k in range(3):
            min_dp[k] = min_tmp[k]
            max_dp[k] = max_tmp[k]

    print(max(max_dp),min(min_dp))
