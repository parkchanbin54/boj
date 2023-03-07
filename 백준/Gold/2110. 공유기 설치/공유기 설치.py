import sys
def binary_search(arr,start,end):
    while start <= end:
        mid = (start + end)//2
        cur = arr[0]
        cnt = 1

        for i in range(1,n):
            if nums[i] >= cur + mid:
                cnt += 1
                cur = nums[i]

        if cnt >= m:
            global ans
            start = mid + 1
            ans = mid
        else:
            end = mid - 1


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int,input().split())

    nums = [int(input()) for _ in range(n)]
    nums.sort()
    ans = 0

    binary_search(nums, 0, nums[-1] - nums[0])
    print(ans)