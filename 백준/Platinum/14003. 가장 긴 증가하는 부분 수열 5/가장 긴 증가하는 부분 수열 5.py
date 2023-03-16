import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    nums = [0] + list(map(int,input().split()))
    dp = [0] * (n+1)

    mem = [-1000000001]

    for i in range(1,n+1):
        if mem[-1] < nums[i]:
            mem.append(nums[i])
            dp[i] = len(mem) - 1

        else:
            left = 0
            right = len(mem)

            while left < right:
                mid = (left + right)//2

                if mem[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            dp[i] = right
            mem[right] = nums[i]

    m = max(dp)
    ans = []
    for i in range(n,0,-1):
        if dp[i] == m:
            ans.append(nums[i])
            m -= 1

    print(len(ans))
    print(*ans[::-1])