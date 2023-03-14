import sys


def divide(x):
    cnt = 1
    min_x = nums[0]
    max_x = nums[0]
    for i in range(1,n):
        min_x = min(nums[i],min_x)
        max_x = max(nums[i],max_x)
        if max_x - min_x > x:
            cnt += 1
            min_x = nums[i]
            max_x = nums[i]

    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().split())
    nums = list(map(int,input().split()))
    left = 0
    right = max(nums)
    ans = 0
    while left <= right:
        mid = (left + right)//2
        if divide(mid) > m:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1

    print(ans)
