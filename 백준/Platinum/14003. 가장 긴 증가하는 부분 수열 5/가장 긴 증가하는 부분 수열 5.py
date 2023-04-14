import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int,input().split()))
    dp = [0] * (n+1)
    mem = [-1000000001]
    for i,num in enumerate(nums):
        if mem[-1] < num:
            mem.append(num)
            dp[i] = len(mem) - 1
        else:
            left = 0
            right = len(mem)

            while left < right:
                mid = (left + right)//2

                if mem[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            dp[i] = right
            mem[right] = nums[i]
    m = max(dp)
    print(m)
    answer = []

    for i in range(n-1,-1,-1):
        if dp[i] == m:
            answer.append(nums[i])
            m -= 1


    print(' '.join(map(str,answer[::-1])))