import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    nums = list(map(int,input().split()))
    dp = [0] * (n+1)

    for i in range(n):
        dp[i+1] = dp[i]
        minv = maxv = nums[i]

        j = i-1
        while j >= 0 and (nums[j] < minv or nums[j] > maxv):
            minv, maxv = min(nums[j], minv), max(nums[j], maxv)
            dp[i+1] = max(dp[i+1], dp[j] + maxv - minv)
            j -= 1

    print(dp[-1])
