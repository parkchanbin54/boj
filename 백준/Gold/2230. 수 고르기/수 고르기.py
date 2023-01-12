import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int,input().split())
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    diff = 2e9

    for i in range(n):
        top = n
        end = i
        while top > end:
            if m <= abs( nums[i] - nums[(top+end)//2] ):
                top = (top + end )//2
            else:
                end = (top + end)//2 + 1
        if top == n:
            top -= 1
        if m <= abs(nums[i] - nums[top]) < diff:
            diff = abs(nums[i] - nums[(top + end) // 2])
    print(diff)
